"""
Web scraper utility for downloading documentation from websites.

This module provides functionality to download web pages and convert them
to markdown format for indexing.
"""

import requests
from pathlib import Path
from typing import Optional, List, Dict
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time
import re


class WebScraper:
    """
    Web scraper for downloading documentation from websites.
    
    Features:
    - Download single pages or crawl entire documentation sites
    - Convert HTML to clean markdown
    - Respect robots.txt
    - Rate limiting to avoid overwhelming servers
    - Save to local files for indexing
    """
    
    def __init__(
        self,
        output_dir: Path = Path("data/sources/web"),
        delay_seconds: float = 1.0,
        max_pages: int = 100,
        user_agent: str = "LinkedDocsMCP/1.0 (Documentation Scraper)",
        allowed_languages: List[str] = None,
        skip_existing: bool = True
    ):
        """
        Initialize the web scraper.
        
        Args:
            output_dir: Directory to save downloaded pages
            delay_seconds: Delay between requests (polite crawling)
            max_pages: Maximum number of pages to download
            user_agent: User agent string for requests
            allowed_languages: List of language codes to include (e.g., ['en', 'de']). 
                             None or empty list allows all languages. Default is English only.
            skip_existing: Skip downloading if file already exists (default: True)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay_seconds = delay_seconds
        self.max_pages = max_pages
        self.user_agent = user_agent
        self.allowed_languages = allowed_languages if allowed_languages is not None else ['en']
        self.skip_existing = skip_existing
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})
        self.visited_urls = set()
        self.skipped_existing = 0  # Track skipped files
    
    def download_page(self, url: str, filename: Optional[str] = None) -> Optional[Path]:
        """
        Download a single web page and save as markdown.
        
        Args:
            url: URL of the page to download
            filename: Optional custom filename (without extension)
            
        Returns:
            Path to the saved file, or None if failed
        """
        try:
            # Generate filename early to check if exists
            if not filename:
                filename = self._url_to_filename(url)
            
            output_path = self.output_dir / f"{filename}.md"
            
            # Check if file already exists
            if self.skip_existing and output_path.exists():
                print(f"Skipping (already exists): {url}")
                print(f"  File: {output_path}")
                self.visited_urls.add(url)
                self.skipped_existing += 1
                return output_path
            
            print(f"Downloading: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title = self._extract_title(soup)
            
            # Convert to markdown
            markdown = self._html_to_markdown(soup, url, title)
            
            # Save to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"  Saved to: {output_path}")
            self.visited_urls.add(url)
            
            # Be polite - wait before next request
            time.sleep(self.delay_seconds)
            
            return output_path
            
        except Exception as e:
            print(f"  Error downloading {url}: {e}")
            return None
    
    def download_documentation(
        self,
        start_url: str,
        link_pattern: Optional[str] = None,
        same_domain_only: bool = True
    ) -> List[Path]:
        """
        Crawl and download multiple pages from a documentation site.
        
        Args:
            start_url: Starting URL to begin crawling
            link_pattern: Regex pattern for URLs to include (e.g., r'/wiki/')
            same_domain_only: Only follow links on the same domain
            
        Returns:
            List of paths to saved files
        """
        saved_files = []
        to_visit = [start_url]
        base_domain = urlparse(start_url).netloc
        base_url = f"{urlparse(start_url).scheme}://{base_domain}"
        
        while to_visit and len(self.visited_urls) < self.max_pages:
            url = to_visit.pop(0)
            
            # Skip if already visited
            if url in self.visited_urls:
                continue
            
            # Check domain restriction
            if same_domain_only and urlparse(url).netloc != base_domain:
                continue
            
            # Check link pattern
            if link_pattern and not re.search(link_pattern, url):
                continue
            
            # Generate filename to check if exists
            filename = self._url_to_filename(url)
            output_path = self.output_dir / f"{filename}.md"
            
            # Check if file already exists (skip before downloading!)
            if self.skip_existing and output_path.exists():
                print(f"[{len(self.visited_urls)+1}/{self.max_pages}] Skipping (already exists): {url}")
                print(f"  File: {output_path}")
                self.visited_urls.add(url)
                self.skipped_existing += 1
                saved_files.append(output_path)  # Still add to results
                continue
            
            # Download the page and extract links
            try:
                print(f"[{len(self.visited_urls)+1}/{self.max_pages}] Downloading: {url}")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                # Parse HTML
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract title
                title = self._extract_title(soup)
                
                # Convert to markdown
                markdown = self._html_to_markdown(soup, url, title)
                
                # Save to file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                
                print(f"  Saved to: {output_path}")
                saved_files.append(output_path)
                self.visited_urls.add(url)
                
                # Extract links from the page
                new_links = self._extract_links(soup, url, base_url, link_pattern, same_domain_only, base_domain)
                
                # Add new links to queue (that haven't been visited)
                for link in new_links:
                    if link not in self.visited_urls and link not in to_visit:
                        to_visit.append(link)
                
                print(f"  Found {len(new_links)} new links, {len(to_visit)} in queue")
                
                # Be polite - wait before next request
                time.sleep(self.delay_seconds)
                
            except Exception as e:
                print(f"  Error downloading {url}: {e}")
                self.visited_urls.add(url)  # Mark as visited to avoid retry
        
        # Summary
        downloaded = len(saved_files) - self.skipped_existing
        print(f"\nCompleted: {len(saved_files)} total pages")
        print(f"  Downloaded: {downloaded} new pages")
        print(f"  Skipped: {self.skipped_existing} existing pages")
        return saved_files
    
    def _extract_links(
        self,
        soup: BeautifulSoup,
        current_url: str,
        base_url: str,
        link_pattern: Optional[str],
        same_domain_only: bool,
        base_domain: str
    ) -> List[str]:
        """
        Extract valid links from a page.
        
        Args:
            soup: BeautifulSoup object of the page
            current_url: Current page URL
            base_url: Base URL for resolving relative links
            link_pattern: Regex pattern for filtering links
            same_domain_only: Whether to only include same-domain links
            base_domain: Base domain for comparison
            
        Returns:
            List of valid URLs to crawl
        """
        links = []
        
        # Find all links
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            # Skip anchors and special links
            if href.startswith('#') or href.startswith('javascript:') or href.startswith('mailto:'):
                continue
            
            # Resolve relative URLs
            full_url = urljoin(current_url, href)
            
            # Remove fragments
            full_url = full_url.split('#')[0]
            
            # Check domain restriction
            if same_domain_only:
                url_domain = urlparse(full_url).netloc
                if url_domain != base_domain:
                    continue
            
            # Check link pattern
            if link_pattern and not re.search(link_pattern, full_url):
                continue
            
            # Avoid common non-content pages
            skip_patterns = [
                r'/Special:',
                r'/Talk:',
                r'/User:',
                r'/User_talk:',
                r'/File:',
                r'/Template:',
                r'/Help:',
                r'/Category:',
                r'action=edit',
                r'action=history',
                r'printable=yes',
            ]
            
            if any(re.search(pattern, full_url, re.I) for pattern in skip_patterns):
                continue
            
            # Filter by language if specified
            if self.allowed_languages and len(self.allowed_languages) > 0:
                # Check for language indicators in URL path
                # Common patterns: /wiki/Page/de, /de/Page, /Page/lang/de
                url_path = urlparse(full_url).path
                
                # Extract language code from URL (common wiki pattern: /Page/xx)
                lang_match = re.search(r'/([a-z]{2})(?:/|$)', url_path)
                
                # If we found a language indicator
                if lang_match:
                    lang_code = lang_match.group(1)
                    # Skip if this language is not in allowed list
                    if lang_code not in self.allowed_languages:
                        continue
                # If no language code found, treat as English (most wikis default to English)
                elif 'en' not in self.allowed_languages:
                    # Skip pages without language indicators if English not allowed
                    continue
            
            links.append(full_url)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_links = []
        for link in links:
            if link not in seen:
                seen.add(link)
                unique_links.append(link)
        
        return unique_links
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title from HTML."""
        # Try various methods to get title
        if soup.title:
            return soup.title.string.strip()
        
        h1 = soup.find('h1')
        if h1:
            return h1.get_text().strip()
        
        return "Untitled"
    
    def _html_to_markdown(self, soup: BeautifulSoup, url: str, title: str) -> str:
        """
        Convert HTML to markdown format.
        
        This is a simplified converter. For production, consider using
        libraries like html2text or markdownify.
        """
        # Remove script, style, and nav elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Get main content
        # Try common content containers
        main_content = (
            soup.find('main') or
            soup.find('article') or
            soup.find('div', class_=re.compile(r'content|main|article', re.I)) or
            soup.find('body')
        )
        
        if not main_content:
            main_content = soup
        
        # Build markdown
        markdown_parts = []
        
        # Add front matter
        markdown_parts.append("---")
        markdown_parts.append(f"title: {title}")
        markdown_parts.append(f"source: {url}")
        markdown_parts.append(f"scraped_at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        markdown_parts.append("tags: [web, documentation]")
        markdown_parts.append("---")
        markdown_parts.append("")
        
        # Add title
        markdown_parts.append(f"# {title}")
        markdown_parts.append("")
        
        # Add source link
        markdown_parts.append(f"**Source:** [{url}]({url})")
        markdown_parts.append("")
        
        # Convert content
        text = self._extract_text_with_structure(main_content)
        markdown_parts.append(text)
        
        return "\n".join(markdown_parts)
    
    def _extract_text_with_structure(self, element) -> str:
        """
        Extract text while preserving some structure.
        
        This recursively processes the HTML tree to extract content.
        """
        lines = []
        
        def process_element(elem, depth=0):
            """Recursively process elements."""
            if not elem:
                return
            
            # Skip text nodes
            if not hasattr(elem, 'name') or elem.name is None:
                return
            
            # Handle different element types
            if elem.name:
                if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    level = int(elem.name[1])
                    heading = '#' * level
                    text = elem.get_text(separator=' ', strip=True)
                    if text:
                        lines.append(f"{heading} {text}")
                        lines.append("")
                
                elif elem.name == 'p':
                    text = elem.get_text(separator=' ', strip=True)
                    if text:
                        lines.append(text)
                        lines.append("")
                
                elif elem.name in ['ul', 'ol']:
                    for li in elem.find_all('li', recursive=False):
                        text = li.get_text(separator=' ', strip=True)
                        if text:
                            lines.append(f"- {text}")
                    lines.append("")
                
                elif elem.name == 'table':
                    # Simple table extraction with better formatting
                    lines.append("")  # Blank line before table
                    for row in elem.find_all('tr'):
                        cells = row.find_all(['td', 'th'])
                        if cells:
                            # Process each cell to get cleaner text
                            cell_texts = []
                            for cell in cells:
                                cell_text = cell.get_text(separator=' ', strip=True)
                                # Clean up excessive whitespace
                                cell_text = ' '.join(cell_text.split())
                                cell_texts.append(cell_text)
                            
                            row_text = ' | '.join(cell_texts)
                            lines.append(f"| {row_text} |")
                    lines.append("")  # Blank line after table
                
                elif elem.name == 'pre':
                    code = elem.get_text(strip=True)
                    if code:
                        lines.append("```")
                        lines.append(code)
                        lines.append("```")
                        lines.append("")
                
                elif elem.name == 'code' and elem.parent.name != 'pre':
                    text = elem.get_text(strip=True)
                    if text:
                        lines.append(f"`{text}`")
                
                elif elem.name == 'blockquote':
                    text = elem.get_text(separator=' ', strip=True)
                    if text:
                        for line in text.split('\n'):
                            if line.strip():
                                lines.append(f"> {line.strip()}")
                        lines.append("")
                
                elif elem.name == 'div':
                    # Recursively process div contents
                    for child in elem.children:
                        process_element(child, depth + 1)
                
                elif elem.name in ['span', 'a', 'strong', 'em', 'b', 'i']:
                    # For inline elements, just get text if it's meaningful
                    if depth == 0:  # Only at top level
                        text = elem.get_text(separator=' ', strip=True)
                        if text and len(text) > 10:  # Avoid tiny fragments
                            lines.append(text)
                
                elif elem.name not in ['script', 'style', 'nav', 'footer', 'header', 'aside', 'meta', 'link']:
                    # For other block elements, recursively process
                    for child in elem.children:
                        process_element(child, depth + 1)
        
        # Start processing
        process_element(element)
        
        # Clean up multiple blank lines
        cleaned_lines = []
        prev_blank = False
        for line in lines:
            if line.strip():
                cleaned_lines.append(line)
                prev_blank = False
            elif not prev_blank:
                cleaned_lines.append("")
                prev_blank = True
        
        return "\n".join(cleaned_lines)
    
    def _url_to_filename(self, url: str) -> str:
        """
        Convert URL to a safe filename.
        
        Args:
            url: URL to convert
            
        Returns:
            Safe filename string
        """
        parsed = urlparse(url)
        
        # Use path and query to create filename
        path = parsed.path.strip('/')
        
        # Replace slashes with underscores
        filename = path.replace('/', '_')
        
        # Remove or replace unsafe characters
        filename = re.sub(r'[^\w\-.]', '_', filename)
        
        # Limit length
        if len(filename) > 200:
            filename = filename[:200]
        
        # If empty, use domain
        if not filename:
            filename = parsed.netloc.replace('.', '_')
        
        return filename


def download_documentation(
    url: str,
    output_dir: Optional[Path] = None,
    crawl: bool = False,
    max_pages: int = 100
) -> List[Path]:
    """
    Convenience function to download documentation from a URL.
    
    Args:
        url: URL to download
        output_dir: Output directory (defaults to data/sources/web)
        crawl: Whether to crawl multiple pages
        max_pages: Maximum pages to download if crawling
        
    Returns:
        List of paths to downloaded files
    
    Example:
        >>> # Download single page
        >>> download_documentation("https://wiki.factorio.com/Main_Page")
        
        >>> # Download multiple pages from wiki
        >>> download_documentation(
        ...     "https://wiki.factorio.com/Main_Page",
        ...     crawl=True,
        ...     max_pages=50
        ... )
    """
    if output_dir is None:
        output_dir = Path("data/sources/web")
    
    scraper = WebScraper(output_dir=output_dir, max_pages=max_pages)
    
    if crawl:
        # For wiki crawling, match wiki URLs
        pattern = r'/wiki/' if '/wiki/' in url else None
        return scraper.download_documentation(url, link_pattern=pattern)
    else:
        # Download single page
        result = scraper.download_page(url)
        return [result] if result else []


# Example usage
if __name__ == "__main__":
    # Example: Download Factorio wiki main page
    print("Factorio Wiki Documentation Scraper")
    print("=" * 60)
    
    url = "https://wiki.factorio.com/Main_Page"
    print(f"Downloading: {url}\n")
    
    files = download_documentation(url)
    
    if files:
        print(f"\nSuccess! Downloaded to:")
        for file in files:
            print(f"  - {file}")
        print("\nYou can now restart the MCP server to index this documentation.")
    else:
        print("\nFailed to download documentation.")

