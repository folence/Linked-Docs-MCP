---
title: Version history/0.9.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.9.0
scraped_at: 2025-10-21 15:47:01
tags: [web, documentation]
---

# Version history/0.9.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.9.0](https://wiki.factorio.com/Version_history/0.9.0)

## 0.9.8

Note, that we also updated the scenario pack to version 0.9.8

### Bugfixes

- Fixed crash when starting the game on MacOSX with less than 512MB video memory. Instead low-graphics is set on and a dialog appears with information (same behavior as on win and Linux).
- Fixed crash when using fast transfer (control click) in the demo levels 1 and 2.
- Removed 0 iron ore resource fields in demo level 1.
- Fixed bug in the map editor that created resources with 0 amount.
- Fixed that mouse button action set to close GUI didn't work over the GUI (same for similar actions). Mouse actions that interact with the map, like mining shooting etc still work only outside of the GUI.
- Slightly better allocation of count of construction robots to deconstruct entity with items inside.
- Fixed the allocation of construction robots to targets in some cases, mainly for containers built using blueprints.
- Fixed twitching of animation of some entities in special cases.

### Scripting

- Fixed gettile/gettileproperties method not fetching correct tile for floating point negative numbers.

### Graphics

- New small electric pole graphics.

## 0.9.7

Note, that we also updated the scenario pack to version 0.9.7 so it is now compatible with current version.

### Bugfixes

- Fixed bug with big biters appearing in the beginning on maps created in map editor.
- Fixed crash when a beacon is built from the blueprint.
- Fixed too big maximum zoom level.
- Belt to be deconstructed doesn't accept new items, so it can be deconstructed.
- Fixed the wrong positioning of bottom to left basic transport belt.
- Fixed bug with roboport deconstruction by its own robots.
- Fixed the error of not accessible config.ini when factorio crashes during start while the config directory doesn't exist.
- Fixed that used ammo specified in personal logistics didn't trigger logistic robots to resupply.
- Fixed the inconsistency of blueprint preview and result when the last build entity was diagonal (rail, semaphore etc.).
- Fixed the pump animation direction. It was running backwards.
- Fixed that manual rebuilding rails on top of the rail ghost didn't remove the ghost in most cases.
- Fixed that pipe/storage tank/assembling machine that was destroyed and rebuilt by construction robot did keep the fluids inside.
- Fixed alerts on map, the important ones are on top (destroyed object > damaged object > turrets firing > materials) and they don't flicker.
- Fixed wrong damage info calculation for distractor robots (they had 2.5 damage not 5).
- Fixed bug when inserters waited too long before putting new barrels to unfill to assembling machine.
- Fixed saving by double click.
- Better error reporting in windows updater.

### Balancing

- Productivity module slowdown changed from 20%->15%, consumption penalty changed from 50%, 70%, 90% -> 40%, 60%, 80%
- Distractor basic damaged increased: 2.5->3.5 and time to live increased 30s->45s.

### Scripting

- Fixed that findnoncollidingposition returns nil  instead of huge values when the position isn't found.
- Limited the game.setspeed value to be at least 0.1.

### Graphics

- Re-skin of the big electric pole.
- Updated icons (still work in progress): assembling machines, transport belts, fluids, barrels, wires.
- Fixed little glitch in the roboport animation (animation and base are separate sprites now).
- New transport belt graphics.

## 0.9.6

### Bugfixes

- Fixed load-ability of save with inserter in logistic network, that has cleared the logistic condition due to mod removal.
- Fixed of loading save with GUI element with custom mod style, when the mod was removed. Note, that we plan to remove GUI created by mod that was removed completely in the future versions.
- Fixed crash with inserter putting stuff to rail-tile when first the rail and then the inserter is removed.

### Graphics

- New transport belt graphics.

## 0.9.5

### Features

- Fixed crash when reconnecting nonempty connected ending part of underground belt.
- Fixed that migration changing logistic chest to other logistic chest with different mode works properly.
- Fixed that assembling machines with recipe were not working correctly with blueprints.
- Fixed bug when all entities (including player, biters, etc.) built in the map editor had neutral force.
- Fix of loading save that have removed/migrated items in circuit/logistic condition.
- Assembling machine isn't shown as producer in electricity statistics.
- Fixed crashes in the 32 bit Linux version.

### Graphics

- The fire of refinery emits light.

### Scripting

- Function table.deepcopy from lualib.util copies factorio Lua objects as references.

### Translations

- Added Hungarian translation.

## 0.9.4

### Known issues

If you are using Dytech mod you will need to download the new version, otherwise the game won't even start. This is due to the change of provider chest to active provider chest.

### Features

- Added passive provider chest. Provides items only for requester, construction and player. Not for storage chests.

### Bugfixes

- Moved lubricant recipe from engine technology to oil processing as lubricant is not needed for basic engine anymore.
- Enabled engine technology in the campaign level 2.
- Fixed various problems when mod changes electric usage priority of existing entities.
- Fixed a bug in displaying electricity production / consumption.
- Battery technology unlocks science pack 3 instead of rocketry.
- Fixed too wide filter selection GUI when too many items are in one subgroup.
- Limit the size of the blueprint preview, so it is usable for huge blueprints.
- Fixed that control clicking to get items from the logistic robot could crash the game in some cases.
- Fixed that having error in the mod init rewrote the config file specifying which mods are enabled.
- Fixed crash that could happen when save containing mods altering damage types is used without the original mod and car/train crash happens.
- Fixed dangling tooltip of the slot inserter logistic condition when closed.
- Fixed small-plane recipe in campaign level 4.
- Removed accumulator research and requirement from the 2nd beta level.
- Updater checks update packages to be applied before actually running them.
- Fixed that assembling machine recipe configuration was lost when using blueprints.
- Objects with even dimensions like 2X2 are centered over the cursor better when building.

### Changes

- Using subgroups and item groups for entities as well. This partially fixes problem with overflowing window for entities in the map editor.
- Dynamic window size for smaller displays.

### Modding

- Added a way to specify recipe hidden, so it doesn't appear in the crafting window.
- Added a way to specify whether to use apply_projection for rotated sprite or not.

### Scripting

- Added way to add ghost structures.
- Added way to order/cancel deconstruction from script.
- Limit the entity.energy write property by <0, max buffer size>

### Translations

- Added simplified Chinese translation.

## 0.9.3

### Bugfixes

- Fixed crash when loading save containing GUI created by script.
- Logistic robot didn't need robot flying frame to craft.
- Fixed crash when construction robots destroyed tracks under train. Now they wait for the train to move away.
- For two different pipe to ground types, the distance limit is the now the minimum of the two connections.
- Fix of crash when changing ambient when the game is not opened.
- Fixed that some of the underground belts components were given to player on game load.
- Fixed infinite map generation with too dense enemy bases.
- Fix of loading a save with equipment in armor that is from mod that is no longer active.
- Enabled engine research, so automobilism is researchable and 1. beta mission completable.
- Fixed smelting steel in prebuilt furnaces in campaign level 2.
- Fixed bug with boilers and pipe fast replace.
- Fixed bug with onentitydied notification and item count.
- Fixed bug with assembling machine connecting to pipes even without fluid recipe.
- Fixed bug with infinite output coming from mining drill when having multiple mining results.
- Fixed crash when disconnecting from character in the car.
- Laser turrets can be researched in New hope campaign level4.
- Removed one (minor) memory leak.
- Fixed gap between current and per-minute stats in production statistics GUI.
- Separate input and output counters for production statistics.
- Solved roboport left/right jitter on low graphics settings.
- Fixed incorrect button positions (and lack of resolution update) when starting Factorio as maximized.
- Fixed bug when unavailable recipes were not displayed in assembler recipe selection without subgroups.

### Scripting

- Added a way to change resize_row_to_width of style from the script.
- Vehicle passenger is accessible from the Lua API.

## 0.9.2

### Bugfixes

- Fixed crash when train stop is built in blueprint before rails.
- Fixed bug when crude oil barrels couldn't be unloaded.
- Added missing recipes for productivity module.
- Fixed bug when belts to ground could be built on top of each other.
- Fixed bug with items not going into fast / express belt to ground.
- Barrel filling was affect-able by the production module.
- Fixed segfault at research screen after researching tool belt
- Fixed missing translation after loading game in campaigns.
- Fixed bug with mining drill getting stuck on low yield resource.
- Fixed overflowing effects in the technology preview GUI.
- Displaying car rotations when building it.
- Unified the smelting recipes time to mean seconds in the stone furnace.
- Train stop and Lab built from the blueprint have proper dedicated to names.
- Fixed stuck items on transport belt in special case.
- Enabled inserter to take fuel out of the boiler.
- Fixed drawing of equipment and some of the icons in low-graphics mod.
- Fix of some of the icons scale in low graphics mode
- Fixed bug with chemical plant draining the fluid from the pipes.
- Tweaked what "size" setting does for resources.
- Fixed that repair sound ignored sound volume settings.
- Fixed that inserter couldn't (inconsistently regards to logistic robots) take out of the red (limited) part of the inventory. The limitation is now just for input.
- Fixed clouds drawing in low-graphics mode.
- Fixed that trying to build trains as ghost did create corrupted rails.
- Crafting GUI has the size that fits all groups, so it don't change size when switching groups.
- Right GUI container doesn't change size when certain entities selected.
- Fixed bounding box + connectability of underground belt build by blueprint.
- Items in the selection guis (quickbar filter, logistic filter, etc.) are ordered into subgroups.
- Fixed offshore direction when building using blueprint.

### Changes

- Assembling Machine Recipe GUI shows all the recipes, but those that are not craftable are show in red (consistent with character recipe GUI).
- Assembling Machines 2 and 3 have an input and output pipe. Electric engine unit, processing unit, filling and emptying barrels is done here.
- Locomotive can be fed by fuel even off station when not moving (on signal, out of fuel etc.)

### Balancing

- Poison capsules hurt worms as well.
- Engine unit doesn't need lubricant (so car and trains don't require the oil industry).
- Fixed: Replacing underground belt's end unearths items
- Pipe to ground is up to 10 tiles long.
- Disabled enemy spawn shift (but this might not be the cause for big biters in the beginning).
- Express belts require lubricant (because they need to run extra smooth).
- Changed the amount of wood in dry tree from 1 -> 4

### Graphics

- New assembling machines.
- New inserters.
- New copper wire.
- New light cone.
- New dark entity info background (the old one can be still switched in graphics settings).

### Scripting

- Added clearchart method to luaForce.
- Destroying/adding custom GUI element will correctly update the size and position of parent elements holding it.

### Modding

- Offshore pump can specify the fluid it will produce.
- Max on row/resize row to width in flow style can be specified.
- Pipe to ground can have multiple underground connections.
- Inserters can have arbitrary pickup and insert positions (this allows 90 degrees inserters).
- Transport belt to ground max distance is now moddable (max_distance).

## 0.9.1

### The hotfix mod

There are two bugs in the 0.9.1 that can make the game pretty much unplayable for some people. These are: the fast and express underground belts are not working properly ( http://www.factorioforums.com/forum/viewtopic.php?f=7&t=2511 ), the crude oil barrels cannot be emptied( http://www.factorioforums.com/forum/viewtopic.php?f=7&t=2484 ). These will be fixed for the 0.9.2 however since they both can be fixed by changing the factorio data files we have made a small hotfix that solves the issue for now. However this hotfix doesn't solve the bug when transport belts to ground can be built one on top of each other (and so they get blocked as well).

The hotfix can be downloaded from here: http://bit.ly/MPExrq - It is basically a tiny factorio mod so just copy the zip file to your mods directory and you should be good to go.

### Known issues

- Existing saves might take a while (10-30 seconds) to load depending on the size. This is because of the adding-new-doodads migration.
- Basic campaign and scenario pack are still broken.

### Features

- Tooltip with info of the armor equipment.
- Capsules can be used in god mode now.

### Bugfixes =

- Fixed bug when blueprint in the second quickbar would corrupt the save (already corrupted saves can be loaded again).
- Fixed bug where unloadable save was made when blueprint containing roboport/armor was as item on ground/held by inserter.
- Fixed save loading bug when oil refinery/chemical plant with reset recipe was saved.
- Fixed bug with stuck inserter when putting sulfur into chemical plant producing sulfur acid in some cases.
- Structures now get repaired even when they are in the bigger (construction) distance from roboport.
- Fixed that the alert icons weren't visible after resize in some cases.
- Fixed that steam engine rotation was wrong in rotated blueprint.
- Fixed double info in item tooltip.
- Oil processing shows oil-refinery in "made in".
- Fixed the burner inserter/locomotive energy consumption.
- Fluid input to chemical plant/refinery is limited to twice the amount in the recipe.
- Chemical plant and oil refinery accept modules.
- Fixed bugs in the automatic connection of rolling stock when being built.
- Updated migration to enable explosives recipe when explosives are researched.
- Fixed bug in assembling machine fast replace.
- Fluid inputs for chemical plant/oil refinery are now saved properly.
- Requester chest now starts working as expected after settings (filters) are copied.
- Logistic condition is now copied as well for smart inserter.
- Assembling recipe machine tooltip takes fluid amounts into consideration.
- Fixed not visible recipes when item groups are turned off (Forced in the tutorial campaign).
- Fixed leftovers of enemies on the map when they were moving.
- Fixed crash when wrong settiles command arguments were given.
- Fixed stuck construction robots with cargo to be returned.
- Fixed that some of the productivity modules had x.9 values instead of x+1
- Fixed, that the storage tank connection to pipe wasn't refreshed when it was rotated.
- Fixed that canceling crafting didn't reset the crafting time spent.
- Show energy consumption for the exoskeleton and night vision equipment in the tooltip.
- Show dimensions of equipment in the tooltip.
- Fixed the help message to open armor to be connected with the correct control (split stack).
- Fixed crash when generating map under some circumstances.
- Updated the map generation GUI to be more responsive to water settings.
- Fixed crash when throwing capsules in the God mode.
- Fixed crash when technology window is displayed over logistic condition window.
- Config file is saved as early as possible to avoid problems with switching to low graphics mode.

### Changes

- Merged the second quickbar (researched by toolbelt) with the main quickbar (now it has 2 rows). The keyboard shortcuts apply to the top row. Rows can be rotated by a button or keyboard shortcut (default X).
- Fixed transport belt to ground collision boxes, so they are more inserter friendly. It is even possible to insert into it.
- Less controls in the new game dialog.
- One of the two connected pipes to ground next to each other shows icon of fluid inside.
- Very small quantities of fluid can be pushed away / destroyed by another fluid in the neighboring pipe. This helps for instance in situations with tiny fluid leftovers after pumping.
- More doodads in the maps.
- Finished crafting sound (tsss) is played only when a full non-intermediate recipe stack finishes crafting.

### Balancing

- Merged oil gathering and oil processing into one technology.
- Barrel costs just 1 steel plate instead of 2 and can hold 25 liters of crude oil.
- Added cracking recipes (heavy oil to light oil and light oil to petroleum gas).
- Storage tank has 2.5 times bigger capacity (2500 lit-res) and takes longer to mine.
- Increased basic-grenade splash area by 30%.
- Smaller probabilities for spawning big worms close to the starting area.
- Slightly more coal is generated.

## 0.9.0

### Known issues!

- Although we were able to spend some time with testing, so the most frequent bugs should be solved, we are quite sure there are more to be found. We altered almost every aspect of the game.
- We also didn't have time to clear all the problems specified in the Bug reports thread (we solved just those that were most simple to solve for now)
- Basic campaign and scenario pack are broken as new recipes and technologies are needed and not enabled in these.
- Only a subset of the doodads is integrated into the world generation.
- Saving a game with blueprint in second quick bar will result in a corrupted save. So please avoid having blueprints in the second quick bar. This will be fixed in the 0.9.1 and the already corrupted saves will be loadable again.

### Features

- Blueprints. Blueprint item allows the player to select the area that will be copied into the item. The player can customize the icons that will represent the blueprint. While building blueprints, player can rotate these, and they can also overlap with existing entities as long as they match.
- Deconstruction tool. Allows player to order construction robots to deconstruct buildings in the selected area. When the buildings contain items (chests, transport belts etc.) construction robots first move these items out of it and place it into the logistics network.
- Oil industry. Pumpjacks mine the crude oil from the oil spills. Oil refinery processes the crude oil to oil fractions. Chemical plant processes the oil fractions to useful products.
- Added fluid storage tank.
- Added electric onshore pump (can speed up the fluid or push the fluid against the slope).
- Biomes. Gives more variation to the nature, tends to generate similar types of vegetation close together.
- Logistic network condition for smart inserters. Takes the sum of all items in storage/provider chests into consideration.
- Recipe GUI contains even recipes not craftable by player (their tooltip shows machines where they can be crafted).
- Copying entity settings (replaces the old shift build functionality). Shift + left click sets the selected entity as a copy source, shift + right click applies the settings to selected entity.
- Ghost buildings can be built (shift + right click) and mined individually.
- Saves directory can contain custom sub directories. Added delete save button.
- Game saves and mods are read / written natively to the zip files.
- CTRL in the textfields including dev console (CTRL + left/right = jump word, CTRL + backspace = delete word, CTRL + up/down = home/end).
- Roboports have separate logistic radius (now 25) and construction radius (now 50).
- Player gets separate warning icon when building is destroyed.
- Warning icons tooltip shows list of entities that are under attack/destroyed/attacking.
- Highlight inventory slots that contains results of the recipe the player already have when he is hovering the recipe slot.
- Added / updated sounds for player actions (building, mining buildings, crafting, inventory move, GUI click, etc.)
- Optional ordering of items sub-categories into individual lines in the crafting window.

### Graphics

- New pipes graphics.
- All not connected pipe connections have ending visualization.
- New 10 types of trees that replace the outdated 2 types.
- Doodads, small decorative objects that appear in the environment (grass chunks, trees, small bushes, rocks etc).
- Area visualizations (for electric poles, roboports, beacons, mining drills) are displayed under the entities.
- Roboports visualization density adds up only to a limit.
- Pipes show the fluid inside in the alt mode.
- Only every second pipe in the row has the window.
- Nicer rail diagonals/turns on minimap.

### Optimisations

- Optimisation of the logistic network update - slow performance with many robots with cargo and no place to put it.
- Optimisation of the electric network update by the factor of 5.
- Optimisation of inserters update, inserters that have nothing to do are set to sleep and woke up when their target/source changes.
- Turrets don't search for enemies when there are no enemies nearby.
- Logistic network doesn't go through empty provider chests/satisfied requester chests any more, so they don't slow down the update.
- Only chunks with changes are recharted, so the limit of 2 recharted chunks per ticks is applied only on chunk that actually changed, this allows to have much higher areas covered by radars.
- Optimisation of the building electric poles by dragging (It could get slow for big networks).
- Small optimisation of transport belt movement.

### Balancing

- Changed many existing recipes (science pack 2, science pack 3, advanced circuit, laser turret, car, diesel locomotive, logistic and construction robots, rocket, flamethrower ammo, defender capsules, most of the armor equipment, etc.)
- Nerfed down productivity modules. Best module productivity bonus changed: 15->10, it has slow down factor, and its usage in assembling machines is limited to intermediate products.
- Slightly more stone in the world.
- Pipe to ground is made in pairs and is more expensive.
- Fast/Express transport belt to ground is made from Basic/Fast transport belt to ground + gears so it can be upgraded.
- Character logistic slots technology needs only red and green science packs.
- Rail signals don't collide with player/car so it can run/walk over it.
- Halved the radar electricity consumption.

### Changes

- Multiplied all energy values by the factor of 1000.
- Optimised pipe/assembling machine/chest bounding boxes, so they obstruct the movement less.
- The green color of night vision visualization is less dense.
- Configurable key mapping for Lua console, "/" key no longer opens the console by default.
- ESC (by default) closes the windows in the game as well.
- Capsules (including the fish) are used by build action when they are in the cursor
- By default the left mouse key builds and opens GUI and the right mouse key does mining.
- Disabled loading of saves before 0.5.0 version (You can use version up to 0.6.4 to load any old saves and re-save them).
- MiningDrill can be built only if there are some resources within its radius.
- The world is slowly generated around the player up to big distance, so exploring should not matter regarding the existence of enemies.

### Bugfixes

- Modules are now transferred when fast replacing furnaces.
- Electricity icon of laser turrets in ghost mode.
- Fixed missing black text font borders in some of the texts.
- Fixed crash when opening GUI in the ghost mode that is active in some of the challenge missions.
- Fixed crash when player fed turret with ammo at the same moment it was destroyed.
- Biters can no longer destroy the shipwreck in the 3rd new hope campaign (it is indestructible).
- Fixed that the sound of walking to the left/right was played from the left/right side.
- Fixed unloadable save when mod with logistic chest(s) was removed.
- Inserter without power will not take stuff from the chest even when it's arm is above it already.
- Fixed bug with biters disappearing in the peaceful mode.
- Fixed stuck inserters when rail is nearby in some cases.
- Fixed of wrong dropTarget of inserter that pointed to train wagon and was rotated.

### Scripting

- It is possible to change tiles from script using the game.settiles
- It is possible to specify health of item.
- Read access to electric pole/pipe neighbors.
- Added connectneighbour method for electric pole.
- Stricter rules for Lua scripts (no require outside mod path, no dofile function)

### Modding

- Recipes can have multiple and randomized products.
- Both ingredients and products for the recipe can be items or fluids.
- Fixed bug, that item on ground created by script ignored the count of the stack.
- Added fluid_usage_per_tick and effectivity fields to the generator.
- Zipped mods can be loaded.

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
