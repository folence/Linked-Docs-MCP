---
title: Modding - Factorio Wiki
source: https://wiki.factorio.com/Modding
scraped_at: 2025-10-21 14:29:54
tags: [web, documentation]
---

# Modding - Factorio Wiki

**Source:** [https://wiki.factorio.com/Modding](https://wiki.factorio.com/Modding)

This page tells you how to download and install mods, and gives a quick overview of what you should keep in mind when creating a mod. For more detailed instructions on creating mods, you may view the modding tutorial page . If you are looking for the modding API, check out the official Factorio Lua API documentation website. If you wish to know where to install a mod which is in a zipped format, please read the instructions on the application directory page.

## Contents

- 1 Downloading & installing mods 1.1 Mod portal (in-game) 1.2 Mod portal (website) 1.3 Mod subforum 1.4 Dependencies 1.4.1 Required dependency 1.4.2 Optional dependency 1.4.3 Incompatibility 1.5 Automatic mod sync for saves and multiplayer games
- 2 Creating mods 2.1 API documentation 2.2 Lua scripting 2.3 Third-Party Tools
- 3 See also

## Downloading & installing mods

You can download the mods from the following places:

- Mod portal (in-game)
- Mod portal (website)
- Mod subforum

### Mod portal (in-game)

The "Mods" section of the main menu is the best way to get mods. It combines downloading & installing, checking installed mods for updates, and enabling/disabling installed mods.

### Mod portal (website)

The mod portal (website) is the center of mod hosting, where authors upload mods, and you can find previous versions, and discussions. Mods come as ZIP files, installed by copying (not unzipping) into the "mods" directory in the user data directory . Verify a successful installation by viewing the "Mods" list through the main menu, in-game.

### Mod subforum

Mod authors maintain threads in the official mod subforum to support their work. There may be experimental mods or updates here that aren't available on the main portal. They will be downloaded as ZIP files, either as forum "attachments", or with a link to a hosting site. These are installed the same way as mods downloaded from the portal.

### Dependencies

Many mods use Factorio's base mod as their only dependency which you do not have to install separately. However, some mods may require you to install other mods for them to work and can also make suggestions for you to install other mods for them to extend their functionality.

#### Required dependency

When a mod you installed requires you to install another mod for it to work, the other mod, in this case, is a required dependency. The in-game mod portal automatically downloads required dependencies when downloading any mod.

#### Optional dependency

When a mod makes a suggestion to install another mod, but if it does not need that other mod for it to work, the other mod, in this case, is an optional dependency. You can install the optional dependencies which extend the functionality of a mod to enhance your gaming experience with the mod.

#### Incompatibility

The dependencies can also be used to declare a mod to be incompatible with other mods, which prevents them from being loaded together.

### Automatic mod sync for saves and multiplayer games

When trying to join a multiplayer game that uses mods, the game will offer to synchronize the mods with the server. Confirming the mod sync will automatically download and enable all mods used by the server. The mod startup settings can be synced as well. When syncing mods to a multiplayer server, the game will download the exact same mod versions as the server is using.

When loading a save file without the mods for that save, or with changed mod settings, the game will offer to synchronize the mods with the save file. Confirming the mod sync will automatically download and enable all mods used by the save file. The mod startup settings can be synced as well. When syncing with a save file, the game will use the latest mod versions by default.

It's possible to manually sync mods to a save file by navigating to it in the "Load game" menu and clicking the "Sync mods with save" button in the top right. By default, this enables the latest version of the mods. When using CTRL + Left mouse button to click the "Sync mods with save" button, the game will use the exact same mod versions as the save file.

## Creating mods

### API documentation

- Modding API docs - Overview page of the modding API documentation website Prototype documentation — What prototypes can be added to the game, and what are their properties Documentation of the runtime API — Hook into events and change the world around the player Auxiliary modding API docs Mod structure — More details on how mods need to be structured in order to be loaded by the game.
- Factorio data GitHub repository — Tracks changes of the Lua prototype definitions in Factorio between releases
- Data.raw — Lists the names and types of all built-in prototypes

### Lua scripting

You need to use the Lua programming language (version 5.2.1) to create any mods in Factorio. The game's mod system injects your code into the startup and to the data construction stage of the game. You can use any text editor to write the code for your mod. Well-known text editors that offer syntax highlighting for Lua are Notepad++ and Visual Studio Code.

Useful resources for Lua:

- Lua tutorial
- Lua reference manual
- Lua REPL : A Lua read-eval-print-loop, essentially a sandbox.

### Third-Party Tools

There is a wide variety of tools contributed by community members to help in mod development, such as plugins for IDEs to provide auto-completion, debuggers, as well as scripts to automate common tasks regarding translations or packaging.

- Factorio sub-forum for mod development tools

## See also

- Category:Technical — Documentation of technical formats and API's not related to modding
