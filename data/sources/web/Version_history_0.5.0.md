---
title: Version history/0.5.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.5.0
scraped_at: 2025-10-21 15:47:02
tags: [web, documentation]
---

# Version history/0.5.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.5.0](https://wiki.factorio.com/Version_history/0.5.0)

## 0.5.3

### Bugfixes

- Fixed bug in saving script state (actual save happened only the very 1st time).
- Fixed bugs in scenario pack.
- Fix of loading of custom GUI styles
- Mining cargo wagon gives back items inside.
- Fixed crash in map editor when opening furnace / boiler / etc.
- Wire dragging in god mode.
- During tight spot simulation the camera can move around.
- Minor fix with arrow in demo level 01.

### Scripting

- Fix of rail not providing direction.
- Fix of setactive method (set always to active), this fixes the scenario pack as well.
- Method getEnergy works on assembling machine.

### Other

- Dropped Linux deb packages (tar packages remain)

### Translations

- Merged changes in FR translation
- Added Dutch translation.

## 0.5.2

### Bugfixes

- Fixed map editor segfaults caused by entities staged for update.
- Fixed double translation in Czech translation.
- Added player entity to the locale file.
- Fixed restart button in finished game GUI.
- Fixed crashes in map editor when building belts to ground on top of each other.
- Fixed the crafting speed description in the assembling machine.
- Fixed straight lines in the newly generated maps.
- Fixed crashes when loading maps with missing tile or resource definitions.
- Fixed setting of sizes of custom GUI elements in scripts (took effect after save, but not immediately).
- Fixed some of the line wrapping problems in tool tips.
- Fixed bug when starting chest buttons appeared when loading sandbox game.
- Fixed attacking with tool when there is no ammo.
- Limit the frequency of the message sound.

### Changes

- The assembling machine 2 speed is now slightly faster (from 1.5 to 2).

### Optimisations

- The game doesn't play (and encode) the ambient when ambient volume is 0.
- The game doesn't simulate fish (and other stuff in the future) that are far away.

## 0.5.1

### Features

- Arrows for mining drill output when building and in Alt mode.
- Vehicle riding in God mode (vehicle must be selected when pressing enter key).
- Safe and resource-rich starting area for freeplay.

### Bugfixes

- Enabled loading of saves with corrupted rail segments setup from 0.4.x versions
- Fix of crash when opening laboratory with no active research.
- Fixed map editor crash when displaying enemy turret entity info.
- Added options button to the map editor menu.
- Esc in map editor menu returns to map editing.
- Fix bug of logistic storage not updated when rebuilding chest to storage.
- Fixed bug of alt-info + logistic storage being off after shift/control click of items that don't fit into inventory.
- Added missing English translation records.
- Fixed crash when train destroyed another wagon / locomotive.
- Fixed crash when using setcommand with defins.command.gotolocation.
- Style for button pie slice progress color (used for crafting slot).
- Small GUI style fixes (car GUI, inserter GUI)
- Unified GUI title bottom styles.
- Minimal width for dialog buttons.
- Fixed crashes in updater.
- Fixed the steam engine power output indicator (allowing it to have value up to 100%)
- Fixed position of the FPS info (now in the top left)
- Fixed changing god speed on autozoom (F9)
- Boiler is fast replaceable with pipes (and vice versa).
- Fixed the bug of the wrong calculation of craftable items.
- Fixed missing file in Linux tarball.

### Changes

- Smooth progress bar for splash screen.
- Faster god movement speed.

### Graphics

- New radar graphics.
- New boiler graphics.
- New steam engine graphics.
- New pump graphics.
- New pipes graphics.

## 0.5.0

### Features

- Crafting recipes categorized into groups.
- GUI styles (changeable by mods).
- Auto updater for new versions.
- Train path finding takes two way signals into account.
- Train Schedule merging when connecting trains.
- Show what is connected to the electric pole when selected.
- Train can find the path backward when it has locomotives in the back
- Choose direction for some entities automatically (semaphore, train station, pump), when more than one direction is suitable. The R key rotates just between those.
- Alt info for the cargo wagon contents.
- Train stop building position is rounded to 2x2 grid to fix the rail grid.
- Visualization of guarded rail area by rail signal when building/selecting it.
- Blinking unplugged icon for generator/solar panel when it is not connected to any machine that can use the electricity, same icon for consumer when not connected to source.
- Multiple Train Stops for the Train Station (Train stop has GUI to change the station it belongs to)
- Updated recipe tooltip for assembling machine output and technology window.
- Inserter can pick up to 5 items when moving from inventory to inventory (when researched), this is useful for faster loading/unloading of cargo in train stations.
- Electric network statistics, accessible by opening the electric pole of the electric network, shows statistics and graphs for different intervals (5s - 50h).
- God controller (mode without a player)
- Added sandbox custom scenario (no goal, just building factories).
- Enemy base generation settings can be set in the map generation GUI.
- Load game GUI automatically selects latest save when opened.
- Added fast and express splitters.
- Crop Cache for atlas (requires less video memory to run, first load when crop cache is initialized can be slower)
- Faster loading times (sounds are loaded when needed, faster images loading)

### Graphics

- New GUI look.
- New locomotive graphics.
- New graphics for mining drills (burner and electric)
- Use shooting particles when player is shooting.
- New splitter graphics.
- New small lamp graphics.
- Rendering light sources behind the border of the screen (To the maximum distance of 15 tiles).

### Bugfixes

- Fixed bug in internal rail segment structure creation on circular rails. This could have made the save games unusable
- Fixed speed of logistic robots manager (slowdowns in games with lots of logistic chest + robots)
- Fixed slow update with big counts of smart chests connected to the circuit network (now instant).
- Fixed bug in logistic chest unregistration when the "ghost" entity to be built was held above it.
- Reload fonts when the display is found, this should solve issues of black fonts after switching from different mode/game.
- Don't allow to do quick transfer (ctrl+click) on entities that are not operable.
- Rails are not minable when there is train on them.
- Player selection controller works when player dies (and is respowned by the player port).
- Correct saving of max updates per frame to the config
- number instead of true/false.
- Fix of alt info for chests cleared by the script.
- Fix of loading saved games with mod items in crafting queue, that are not already present (mod with that item is not present, or the item was removed).
- Fixed bug of not loadable games due to different mod settings causing to have assembling machines set to recipes with more ingredients than the number of slots of the assembling machine.
- Fixed object creation in the Lua scripts (faster and no memory leaks).
- Fixed clearing temporary script data (faster).
- Fixed bug with flickering entity info.
- Character not connected to player dying doesn't lose the game..
- Fixed ordering of commands on entity die to allow clone mod.
- Confirm exit from map editor when map is not saved.
- Fixed bug of not loadable saves with entities on the edge of the region in some cases.
- Fixed automatic resizing of script-based GUI when text is element or child items are removed.

### Changes

- Larger scale of terrain features.
- Better movement on transport belts in turns and crossings.
- Rails recipe changed (made from steel, needs also stone)
- Locomotive + wagon + rails are more expensive.
- More random looking enemy base generation.
- Machines using electricity can have limited maximum input/output flow per second, so accumulators don't recharge/give energy instantly and laser turrets take energy, more continuously.
- Ambient (music) isn't loaded all at start, but instead streaming real time while playing, this reduces game starting time and memory requirements.
- Removed the limit to pickup 1 item per tick when player is picking items.
- Player picks all items in range when picking items on ground (not just 1 per tick as it was until now)

### Scripting

- Changed the 'orientation' parameter to 'direction' to be consistent, the direction is used for the 4/8 base direction of the entity. Orientation is used for 360° orientation of something.
- LuaEntity::clearitemsinside and getitemcount works on all entities (hopefully)
- Added LuaGame::findentitiesfiltered, to find entities of certain type/name faster.
- Added LuaGame::findnoncollidingposition(name, position, max perimeter, precision) to quickly find building space.
- Saving and Loading game from the script (game.load(name) and game.save(name)). Used in tight-spot and transport-belt-madness.

### Modding

- Mods can modify the GUI style of the game.
- Configurable car trunk size in the entity definition.
- Measure time spent in scripts divided in individual mods and show in time statistics info (F5).
- force.resettechnologies now loads new versions of technologies (like before), but it preserves the research and enabled state of technologies, so it is usable in migrations to reload existing technologies that changed.
- Enabled to have recipe with no prerequisites (just energy). In the crafting GUI, it shows Infinite count craftable of that item (and all items dependent on recipes that are for free).

| Versions |
| 0.1-0.6 | 0.1.0 0.1.1 0.1.2 0.2.0 0.2.1 0.2.2 0.2.3 0.2.4 0.2.5 0.2.6 0.2.7 0.2.8 0.2.9 0.2.10 0.3.0 0.3.1 0.3.2 0.4.0 0.4.1 0.5.0 0.5.1 0.5.2 0.5.3 0.6.0 0.6.1 0.6.2 0.6.3 0.6.4 |
| 0.7-0.11 | 0.7.0 0.7.1 0.7.2 0.7.3 0.7.4 0.7.5 0.8.0 0.8.1 0.8.2 0.8.3 0.8.4 0.8.5 0.8.6 0.8.7 0.8.8 0.9.0 0.9.1 0.9.2 0.9.3 0.9.4 0.9.5 0.9.6 0.9.7 0.9.8 0.10.0 0.10.1 0.10.2 0.10.3 0.10.4 0.10.5 0.10.6 0.10.7 0.10.8 0.10.9 0.10.10 0.10.11 0.10.12 0.11.0 0.11.1 0.11.2 0.11.3 0.11.4 0.11.5 0.11.6 0.11.7 0.11.8 0.11.9 0.11.10 0.11.11 0.11.12 0.11.13 0.11.14 0.11.15 0.11.16 0.11.17 0.11.18 0.11.19 0.11.20 0.11.21 0.11.22 |
| 0.12 | 0.12.0 0.12.1 0.12.2 0.12.3 0.12.4 0.12.5 0.12.6 0.12.7 0.12.8 0.12.9 0.12.10 0.12.11 0.12.12 0.12.13 0.12.14 0.12.15 0.12.16 0.12.17 0.12.18 0.12.19 0.12.20 0.12.21 0.12.22 0.12.23 0.12.24 0.12.25 0.12.26 0.12.27 0.12.28 0.12.29 0.12.30 0.12.31 0.12.32 0.12.33 0.12.34 0.12.35 |
| 0.13-0.14 | 0.13.0 0.13.1 0.13.2 0.13.3 0.13.4 0.13.5 0.13.6 0.13.7 0.13.8 0.13.9 0.13.10 0.13.11 0.13.12 0.13.13 0.13.14 0.13.15 0.13.16 0.13.17 0.13.18 0.13.19 0.13.20 0.14.0 0.14.1 0.14.2 0.14.3 0.14.4 0.14.5 0.14.6 0.14.7 0.14.8 0.14.9 0.14.10 0.14.11 0.14.12 0.14.13 0.14.14 0.14.15 0.14.16 0.14.17 0.14.18 0.14.19 0.14.20 0.14.21 0.14.22 0.14.23 |
| 0.15 | 0.15.0 0.15.1 0.15.2 0.15.3 0.15.4 0.15.5 0.15.6 0.15.7 0.15.8 0.15.9 0.15.10 0.15.11 0.15.12 0.15.13 0.15.14 0.15.15 0.15.16 0.15.17 0.15.18 0.15.19 0.15.20 0.15.21 0.15.22 0.15.23 0.15.24 0.15.25 0.15.26 0.15.27 0.15.28 0.15.29 0.15.30 0.15.31 0.15.32 0.15.33 0.15.34 0.15.35 0.15.36 0.15.37 0.15.38 0.15.39 0.15.40 |
| 0.16 | 0.16.0 0.16.1 0.16.2 0.16.3 0.16.4 0.16.5 0.16.6 0.16.7 0.16.8 0.16.9 0.16.10 0.16.11 0.16.12 0.16.13 0.16.14 0.16.15 0.16.16 0.16.17 0.16.18 0.16.19 0.16.20 0.16.21 0.16.22 0.16.23 0.16.24 0.16.25 0.16.26 0.16.27 0.16.28 0.16.29 0.16.30 0.16.31 0.16.32 0.16.33 0.16.34 0.16.35 0.16.36 0.16.37 0.16.38 0.16.39 0.16.40 0.16.41 0.16.42 0.16.43 0.16.44 0.16.45 0.16.46 0.16.47 0.16.48 0.16.49 0.16.50 0.16.51 |
| 0.17 | 0.17.0 0.17.1 0.17.2 0.17.3 0.17.4 0.17.5 0.17.6 0.17.7 0.17.8 0.17.9 0.17.10 0.17.11 0.17.12 0.17.13 0.17.14 0.17.15 0.17.16 0.17.17 0.17.18 0.17.19 0.17.20 0.17.21 0.17.22 0.17.23 0.17.24 0.17.25 0.17.26 0.17.27 0.17.28 0.17.29 0.17.30 0.17.31 0.17.32 0.17.33 0.17.34 0.17.35 0.17.36 0.17.37 0.17.38 0.17.39 0.17.40 0.17.41 0.17.42 0.17.43 0.17.44 0.17.45 0.17.46 0.17.47 0.17.48 0.17.49 0.17.50 0.17.51 0.17.52 0.17.53 0.17.54 0.17.55 0.17.56 0.17.57 0.17.58 0.17.59 0.17.60 0.17.61 0.17.62 0.17.63 0.17.64 0.17.65 0.17.66 0.17.67 0.17.68 0.17.69 0.17.70 0.17.71 0.17.72 0.17.73 0.17.74 0.17.75 0.17.76 0.17.77 0.17.78 0.17.79 |
| 0.18-1.0 | 0.18.0 0.18.1 0.18.2 0.18.3 0.18.4 0.18.5 0.18.6 0.18.7 0.18.8 0.18.9 0.18.10 0.18.11 0.18.12 0.18.13 0.18.14 0.18.15 0.18.16 0.18.17 0.18.18 0.18.19 0.18.20 0.18.21 0.18.22 0.18.23 0.18.24 0.18.25 0.18.26 0.18.27 0.18.28 0.18.29 0.18.30 0.18.31 0.18.32 0.18.33 0.18.34 0.18.35 0.18.36 0.18.37 0.18.38 0.18.39 0.18.40 0.18.41 0.18.42 0.18.43 0.18.44 0.18.45 0.18.46 0.18.47 1.0.0 |
| 1.1 | 1.1.0 1.1.1 1.1.2 1.1.3 1.1.4 1.1.5 1.1.6 1.1.7 1.1.8 1.1.9 1.1.10 1.1.11 1.1.12 1.1.13 1.1.14 1.1.15 1.1.16 1.1.17 1.1.18 1.1.19 1.1.20 1.1.21 1.1.22 1.1.23 1.1.24 1.1.25 1.1.26 1.1.27 1.1.28 1.1.29 1.1.30 1.1.31 1.1.32 1.1.33 1.1.34 1.1.35 1.1.36 1.1.37 1.1.38 1.1.39 1.1.40 1.1.41 1.1.42 1.1.43 1.1.44 1.1.45 1.1.46 1.1.47 1.1.48 1.1.49 1.1.50 1.1.51 1.1.52 1.1.53 1.1.54 1.1.55 1.1.56 1.1.57 1.1.58 1.1.59 1.1.60 1.1.61 1.1.62 1.1.63 1.1.64 1.1.65 1.1.66 1.1.67 1.1.68 1.1.69 1.1.70 1.1.71 1.1.72 1.1.73 1.1.74 1.1.75 1.1.76 1.1.77 1.1.78 1.1.79 1.1.80 1.1.81 1.1.82 1.1.83 1.1.84 1.1.85 1.1.86 1.1.87 1.1.88 1.1.89 1.1.90 1.1.91 1.1.92 1.1.93 1.1.94 1.1.95 1.1.96 1.1.97 1.1.98 1.1.99 1.1.100 1.1.101 1.1.102 1.1.103 1.1.104 1.1.105 1.1.106 1.1.107 1.1.108 1.1.109 1.1.110 |
| 2.0.0 | 2.0.7 2.0.8 2.0.9 2.0.10 2.0.11 2.0.12 2.0.13 2.0.14 2.0.15 2.0.16 2.0.17 2.0.18 2.0.19 2.0.20 2.0.21 2.0.22 2.0.23 2.0.24 2.0.25 2.0.26 2.0.27 2.0.28 2.0.29 2.0.30 2.0.31 2.0.32 2.0.33 2.0.34 2.0.35 2.0.36 2.0.37 2.0.38 2.0.39 2.0.40 2.0.41 2.0.42 2.0.43 2.0.44 2.0.45 2.0.46 2.0.47 2.0.48 2.0.49 2.0.50 2.0.51 2.0.52 2.0.53 2.0.54 2.0.55 2.0.56 2.0.57 2.0.58 2.0.59 2.0.60 2.0.61 2.0.62 2.0.63 2.0.64 2.0.65 2.0.66 2.0.67 2.0.68 2.0.69 2.0.70 2.0.71 |
