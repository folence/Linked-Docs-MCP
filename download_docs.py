"""
CLI tool for downloading web documentation for indexing.

Usage:
    python download_docs.py <url>                    # Download single page
    python download_docs.py <url> --crawl            # Crawl multiple pages
    python download_docs.py <url> --crawl --max 50   # Limit to 50 pages

Examples:
    # Download Factorio wiki main page
    python download_docs.py https://wiki.factorio.com/Main_Page

    # Download multiple wiki pages
    python download_docs.py https://wiki.factorio.com/Main_Page --crawl --max 20
"""

import argparse
import sys
from pathlib import Path
from utils.web_scraper import download_documentation


def main():
    """Main entry point for the documentation downloader."""
    parser = argparse.ArgumentParser(
        description="Download web documentation for the MCP server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "url",
        help="URL of the documentation page to download"
    )
    
    parser.add_argument(
        "--crawl",
        action="store_true",
        help="Crawl and download multiple pages (default: single page only)"
    )
    
    parser.add_argument(
        "--max",
        type=int,
        default=100,
        metavar="N",
        help="Maximum number of pages to download when crawling (default: 100)"
    )
    
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/sources/web"),
        metavar="DIR",
        help="Output directory (default: data/sources/web)"
    )
    
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        metavar="SEC",
        help="Delay between requests in seconds (default: 1.0)"
    )
    
    parser.add_argument(
        "--languages",
        type=str,
        default="en",
        metavar="CODES",
        help="Comma-separated language codes to include (default: 'en' for English only). Use 'all' for all languages."
    )
    
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download even if files already exist (default: skip existing)"
    )
    
    args = parser.parse_args()
    
    # Print header
    print("=" * 70)
    print("Documentation Downloader for Linked Documentation MCP Server")
    print("=" * 70)
    print()
    
    # Validate URL
    if not args.url.startswith(('http://', 'https://')):
        print("[ERROR] URL must start with http:// or https://")
        sys.exit(1)
    
    # Parse language codes
    if args.languages.lower() == 'all':
        allowed_languages = []  # Empty list means all languages
        lang_display = "all languages"
    else:
        allowed_languages = [lang.strip() for lang in args.languages.split(',')]
        lang_display = ', '.join(allowed_languages)
    
    # Show configuration
    print(f"URL:           {args.url}")
    print(f"Mode:          {'Crawl multiple pages' if args.crawl else 'Single page'}")
    if args.crawl:
        print(f"Max pages:     {args.max}")
    print(f"Languages:     {lang_display}")
    print(f"Output dir:    {args.output}")
    print(f"Delay:         {args.delay}s between requests")
    print(f"Skip existing: {'No (force re-download)' if args.force else 'Yes'}")
    print()
    print("=" * 70)
    print()
    
    # Download
    try:
        from utils.web_scraper import WebScraper
        
        scraper = WebScraper(
            output_dir=args.output,
            delay_seconds=args.delay,
            max_pages=args.max,
            allowed_languages=allowed_languages,
            skip_existing=not args.force  # Invert: --force means don't skip
        )
        
        if args.crawl:
            # Crawl multiple pages
            print("Starting crawl...")
            print("(This may take a while depending on the site)")
            print()
            
            # For wiki sites, look for wiki pattern
            pattern = r'/wiki/' if '/wiki/' in args.url else None
            files = scraper.download_documentation(
                args.url,
                link_pattern=pattern,
                same_domain_only=True
            )
        else:
            # Single page
            print("Downloading page...")
            print()
            result = scraper.download_page(args.url)
            files = [result] if result else []
        
        # Summary
        print()
        print("=" * 70)
        print("Download Summary")
        print("=" * 70)
        
        if files:
            downloaded = len(files) - scraper.skipped_existing
            print(f"[SUCCESS] Processed {len(files)} file(s)")
            print(f"  • Downloaded: {downloaded} new file(s)")
            print(f"  • Skipped: {scraper.skipped_existing} existing file(s)")
            print()
            print("Files in output directory:")
            # Show only first 20 files to avoid clutter
            display_files = files[:20]
            for file_path in display_files:
                print(f"  - {file_path}")
            if len(files) > 20:
                print(f"  ... and {len(files) - 20} more files")
            
            print()
            print("=" * 70)
            print("Next Steps:")
            print("=" * 70)
            print("1. Restart the MCP server to index the new documentation:")
            print("   python main.py")
            print()
            print("2. Search the documentation:")
            print("   python test_api.py")
            print()
            print("3. Or use the API directly:")
            print("   http://127.0.0.1:8000/docs")
            print("=" * 70)
        else:
            print("[ERROR] No files were downloaded")
            print("Check the URL and try again")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print()
        print()
        print("[INTERRUPTED] Download cancelled by user")
        sys.exit(130)
    
    except Exception as e:
        print()
        print(f"[ERROR] Download failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

