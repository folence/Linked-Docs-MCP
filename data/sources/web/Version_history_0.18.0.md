---
title: Version history/0.18.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.18.0
scraped_at: 2025-10-21 15:46:56
tags: [web, documentation]
---

# Version history/0.18.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.18.0](https://wiki.factorio.com/Version_history/0.18.0)

## 0.18.47

Date: 11.08.2020

### Bugfixes

- Fixed that editing upgrade planner and deconstruction planner didn't work directly in the blueprint library. ( more )

## 0.18.46

Date: 10.08.2020

### Graphics

- Electric mining drill graphics now fill bounding box more accurately.

### Bugfixes

- Fixed hovering over unit that was going toward an entity would crash if the entity was destroyed. ( more )
- Fixed crashes/desyncs related to various different operations on a shelf of a player that just joined, and his blueprint shelf meta-data hasn't be synchronized yet.
- Fixed crashes/desyncs related to swapping item with a blueprint/book in the blueprint library that is not yet fully transferred into the game. ( more )
- Fixed electric mining drill circuit connection graphics.
- Fixed crash when picking up something using the quickbar while setting up a blueprint from the inventory.
- Fixed that blueprint book GUI was scrolling to the top whenever something was done. ( more )

## 0.18.45

Date: 07.08.2020

### Graphics

- Fixed mistakes in some technology icons. (Flipped underground belt in Logistics, and graphical artifacts in modules)

### Sounds

- Improved various sounds, mainly inserters, assembling machines and laser beam.
- Tweaked various sound levels.

### Bugfixes

- Fixed empty spacing in Rocket silo stats GUI. ( more )
- Fixed wave defence bonuses persisting between rounds if you lost via rocket silo dying. ( more )

## 0.18.44

Date: 07.08.2020

### Graphics

- Reworked Electric mining drill graphics, removing their vertical structure - to fix tile overlapping and other issues introduced with redesign.

### Bugfixes

- Added equipment icon to Personal laser defense technology icon. ( more )
- Fixed logistic chest shadows were shorter than other chests. ( more )
- Fixed that unit groups could get stuck after getting close to their target. ( more )
- Fixed loading Blueprint books before version 0.18.42.
- Fixed that when importing blueprint string, the error had success sound and the success had error sound. ( more )
- Fixed the small shortcut buttons didn't follow the same color settings as the big ones.
- Added better error when attempting to load NPE save.

### Gui

- Tweaked the loading progress bar styles a bit, so they are slimmer and can fit more text.

## 0.18.43

Date: 06.08.2020

### Graphics

- Updated the technology icons.
- Updated the "Make a copy of blueprint" icon.

### Gui

- Added simple credits gui.
- Updated the style of progressbar dialogs.
- Updated the style of map editor.

### Changes

- Changed the default debug settings to only show grid and nothing else.

### Bugfixes

- Fixed that Blueprint books in the library didn't propagate its modded icon backups properly into the game.
- Fixed that Blueprint books in item form did loose its modded icon backed up state when saved between versions 0.18.37 and 0.18.42
- Fixed that swapping ghost cursor with an item didn't clear the quickbar selection immediately.
- Fixed PvP script error when starting a new round with duplicate starting areas. ( more )
- Fixed PvP scenario not restoring character bonuses after respawn. ( more )
- Fixed that most of the windows were not squashing as they should when they couldn't fit the screen.
- Fixed squashing of save name label in the load/save map dialog and load/save map progress windows.
- Fixed that biters could attack entities beyond their attack range. ( more )
- Fixed crash when opening train gui through non-locomotive while in map view in latency state. ( more )
- Fixed that the deconstruction planner was ignoring specified tile filters when removing tile ghosts.
- Fixed that the deconstruction planner with normal tile setting was ignoring tiles when the selection contained only tile ghosts + tiles.
- Fixed that the deconstruction planner with tile ghost filter selected didn't select (with whitelist) or ignore (with blacklist) the tile ghosts.
- Fixed that the deconstruction planner with tiles and rocks only and blacklist always ignored tiles.
- Fixed lights of entities just outside of right or bottom border of screen were drawn twice sometimes.
- Fixed drag-placing ghost item in zoomed-to-world view would drag the view instead. ( more )
- Fixed that barreling recipes were generated for "fluid-unknown".

### Scripting

- Empty LuaPrototype collision masks will now return an empty table, rather than nil.
- LuaEntity::circuit_connected_entities and LuaEntity::circuit_connection_definitions return data for entity ghosts. ( more )

## 0.18.42

Date: 03.08.2020

### Bugfixes

- Fixed a crash when holding a blueprint book.
- Fixed that blueprint book in an item form didn't have mod-persistent icons.
- Don't drag map when in zoomed in map mode and building blueprints.
- Don't place map tags when building blueprints.
- Fixed crash in rendering due to game state being modified by buildability checks for drawing blueprint placement visualization on chunks in fog-of-war when zoomed-to-world.

## 0.18.41

Date: 03.08.2020

### Changes

- The tiles and entities filtering logic in the deconstruction planner is now independent.
- Selecting first entity filter switches tile mode to never when it has the default normal mode and no filters.

### Bugfixes

- Probably fixed problem with blueprint preview data not being empty when blueprint is empty.
- Improved layering of rocket in rocket silo, so it occludes inserter hands. ( more )
- Fixed inventory consistency check failing when loading some saves. ( more )
- Fixed inventory error messages in god and editor controller. ( more )
- Fixed smoke might not be spawned from generator entity if its animation was too short. ( more )
- Fixed underground belts and loaders would not draw half-belt with layers correctly. ( more )
- Fixed localised strings in text objects created through script rendering API, would be untranslated after saving and loading. ( more )
- Fixed that right-clicking blueprint book with empty blueprint being selected destroyed the whole book.
- Fixed that cut and copy created empty blueprint when nothing was selected with alternative selection type.
- Fixed that the mouse "cross" selection cursor was not present when selection tools from the blueprint library were held in the cursor.
- Fixed that the latency state of deconstructing using tool from library didn't take the tool settings into consideration.
- Fixed the alert tooltips showing all surface names in the tooltip when multiple surfaces existed.

### Modding

- Added LuaEntityPrototype::rocket_entity_prototype read.

## 0.18.40

Date: 01.08.2020

### Bugfixes

- New release to fix standalone Windows version having only demo content.

## 0.18.39

Date: 01.08.2020

### Bugfixes

- Fixed clearing ghost from cursor would not clear quickbar selection. ( more )
- Fixed blueprint book not shrinking when the last item was destroyed.
- Fixed crash when Lua received event of player selecting area to deconstruct.
- Fixed upgrading book by item would not work while being in editor. ( more )
- Fixed biters not grouping before attacking an artillery outpost. ( more )
- Fixed crash related to saving blueprint which has all the entities/tiles as question marks.
- Fixed desync when loading blueprint shelf with modded entities. ( more )
- Fixed that swapping blueprint cursor into a non transferred blueprint didn't trigger the transfer.
- Fixed that cycling blueprint book in the shared blueprint library could also cycle the index for other players holding the same book.
- Fixed that cycling book wouldn't mark blueprint storage to be resaved, so the indexes would be lost if no other changes were done.
- Fixed a desync when returning to a multiplayer game while the book active index was changed in a different game. ( more )
- Fixed that the action to put item into a blueprint library was not based on the latency hiding state of held item, which could result into the action doing nothing when the item held was not in the server state yet.
- Fixed that quickbar links into items contained in blueprint books in the player inventory didn't work.
- Fixed that it was possible to setup empty blueprint of other player if the original player was still having the quickbar link to it.
- Fixed that quickbar links did work only for the main inventory of player, so it didn't work for currently equipped armor for example.
- Fixed that LuaInventory.insert() didn't work properly for blueprint books. ( more )
- Fixed crash when reassigning blueprint with non-even snap grid size to contain rails. ( more )
- Fixed crash when holding a blueprint from the blueprint library while being dead. ( more )
- Fixed that the info for selecting entities to be upgraded was mentioning entities that were marked for deconstruction, even when these are ignored by the upgrade planner.
- Fixed that ordering deconstruction didn't cancel upgrade order. ( more )

## 0.18.38

Date: 30.07.2020

### Graphics

- Improved the blueprint grid visualisation, so it shows a rectangle instead of just the corners.
- Added blueprint grid visualisation when building in the world.

### Bugfixes

- Fixed cleaning ghost cursor. ( more )
- Fixed crash when clicking a blueprint book upgrade slot with an upgrade planner in hand.
- Fixed navigating in a blueprint book item when opened directly from a quickbar. ( more )
- Fixed that it was possible to put book into itself using hand->swap and clean cursor.
- Fixed that the hand functionality didn't work properly for gun and ammo and gave misleading error messages in some cases.
- Fixed "slice" property of animation definition was interpreted as dicing parameter, possibly causing large memory allocations. ( more )
- Fixed that grabbing gun/ammo, swapping it with some other item in the inventory and pressing Q, gave a message of inventory full, instead of the item in cursor not being returnable to the hand location
- Fixed that Internal inventory stack transfer messages weren't specific enough, or not present at all.

### Modding

- Renamed sprite and animation properties for sprite dicing from "slice", "slice_x" and "slice_y" to "dice", "dice_x" and "dice_y", because "slice" collided with property of rotated animation definition used for defining spritesheet sliced into multiple files. Sprite dicing is a technique of chopping large sprite into smaller ones to improve packing in sprite atlas.

### Scripting

- Fixed a typo (per vs pre) in the on_pre_permission_group_deleted event name.

## 0.18.37

Date: 29.07.2020

### Major Features

- New blueprint library GUI. Its user interface had been aligned with the way inventory works in as many ways as possible. ( https://www.factorio.com/blog/post/fff-356 )

### Features

- Added blueprint building from the map view.
- Blueprints can have snapping dimensions specified. When they are built by dragging, they are only built in the grid relative to where the build started.
- Blueprints can have absolute map snapping specified, so the blueprints are always aligned to the global grid.
- Blueprint books can be inserted into blueprint books, cycling through the books works in a hierarchical way.
- Upgrade planners and deconstruction planners can be inserted into blueprint books and the blueprint library.
- Blueprint books, upgrade planners and deconstruction planners can now have custom icons specified.
- All blueprints tools have an editable description.
- Added Blueprint reassign tool. It allows to set new contents of a blueprint by world selection.
- All blueprint tools have a copy function.
- All the blueprint tools are usable directly from the blueprint library.
- Quickbar links to blueprint tools are persistent when moving them between library shelves and inventories.
- Most of the blueprint tools manipulation in the blueprint library is part of a multiplayer latency hiding.
- Icons on the blueprint tools and filters in the upgrade planners/deconstruction planners are preserving the original values so whenever the mods would be re-added, the original values can be restored, unless the player clears the related icons manually.
- Any blueprint contents that are not available due to mod removal are also kept in the blueprint persistently, so blueprints can be copied and transferred in multiplayer without losing its original data.
- Added downgrading feature to upgrade planner. It works on blueprints, books and also when applying in the world.
- Clicking an upgrade planner button in the blueprint or a book now provides a list of all available upgrade planners to be applied.
- Upgrade planners now also update the relevant icons of blueprints and books.

### Minor Features

- Grabbing an item from a blueprint book has the same hand item functionality as when holding an item from inventory, so it goes back to the original position when clean cursor is triggered.

### Gui

- All the blueprint tools now show all possible actions it can perform in the tooltip.
- Control settings search now also searches by the currently assigned key-binding.

### Optimizations

- Decreased the header size of blueprint-storage and of individual blueprints with backed up modded entities, as only the id mapping relevant to the blueprints (and whole storage) is now saved.

### Bugfixes

- Fixed that exporting blueprint didn't include the unconfirmed blueprint changes into the exported string.
- Fixed blueprint preview icons rendering scale when blueprint was held in cursor.
- Fixed that blueprint was not detecting modded data to be lost when loading unless one of the top level entities or tiles were to be lost. This means, that a blueprint with vanilla constant combinator (for example) with a modded signal will no longer silently lose the modded signals on resaving the blueprint storage when the mod is not currently active.
- Fixed that biters when faced with a rock might get stuck in an infinite pathfinding loop. ( more )
- Fixed that clicking a technology in the research queue, holding the mouse down and moving it over the cancel button would make the cancel button flicker. ( more )
- Fixed slider tooltip would show old value. ( more )
- Fixed terrain particles would be spawned when walking over belts. ( more )
- Fixed player movement on belts in latency state was not exactly matched with the real game state logic. ( more )
- Fixed that the set-request GUI didn't respect the show-all-items setting. ( more )
- Fixed that burner assembling machines could cause inserters to get stuck holding extra fuel in some cases. ( more )
- Fixed noise.terrace function did not assert that constant parameters are constant.
- Fixed that item durability tooltips used the wrong locale key in some places. ( more )
- Fixed that upgrading inserters in blueprints wouldn't preserve modded pickup/drop locations. ( more )
- Fixed that exporting empty blueprint books didn't work correctly. ( more )
- Fixed that the mods GUI didn't have any mod selection by default. ( more )
- Fixed that positions of entities in blueprint string were not properly fixed to be aligned to grid according to our rules and centered.
- Fixed a crash when mods destroy the character entity during the on_gui_closed event. ( more )
- Fixed a crash when canceling loading some modded saves. ( more )
- Fixed that artillery turrets didn't fully use the shooting speed research. ( more )
- Reduced flicker of mining drill indicator lights when zoomed out. ( more )
- Fixed lua documentation for LuaGuiElement::index read. ( more )
- Fixed that biters would try to attack over large distances individually instead of in groups. ( more )
- Map tag edit GUI can now be confirmed with Enter key even when the textbox is not focused. ( more )
- Fixed a pathfinder crash related to entities and tiles using collision layers 11 to 15. ( more )
- Fixed the changelog GUI indentation.

### Modding

- Implemented compileIntoCurrentProcedure for the "if-else-chain" noise expression type. This allows non-constant values to be used as conditions.
- Added "modulo", "ceil" and "floor" noise expression types.
- Added "bitwise-and", "bitwise-or", "bitwise-xor" and "bitwise-not" noise expression types.
- Added "sin", "atan2" and "cos" noise expression types.
- Added "less-than", "less-or-equal" and "equals" noise expression types.
- Changed turret base_picture animation to actually play the animation.
- Added several properties to ExplosionPrototype to control light fading through applying a multiplier to the light's size and intensity. "light_intensity_factor_initial" (default 0), "light_intensity_factor_final" (default 0), "light_intensity_peak_start_progress" (default 0), "light_intensity_peak_end_progress" (default 0.9), "light_size_factor_initial" (default 0.05), "light_size_factor_final" (default 0.1), "light_size_peak_start_progress" (default 0.1), "light_size_peak_end_progress" (default 0.5)

### Scripting

- Added permission events: on_permission_group_edited, on_pre_permission_string_imported, on_permission_string_imported, on_per_permission_group_deleted, on_permission_group_deleted, and on_permission_group_added.
- Simplified the rules of entity positions aligned to grid in the blueprint. Now they have the same rules as entities in the world.

## 0.18.36

Date: 15.07.2020

### Gui

- New high resolution tips and tricks images.
- Visual improvements to the tips and tricks GUI and the rocket silo stats GUI.

### Graphics

- New remnants for assembling machines and land mine.
- New visual effects for slowdown capsule.

### Changes

- Changed sorting order of items: Same items but without data are first. Descending order of Health/Ammo/Durability.
- Units are now affected by the 'movement_slow_down_factor' defined in their attack parameters.
- Slowdown capsules slowdown factor increased from 50% to 75%.

### Sounds

- Updated sounds for assembling machines 1, 2, and 3.
- New sounds for mining and eating fish.
- New sound for spitter spawner, repairing robots.
- New sound for throwing capsules, grenades, combat robots.
- Various levels adjusted including new default sound settings.

### Bugfixes

- Fixed that force.reset() wouldn't clear saved research progress. ( more )
- Fixed disabling, renaming or destroying unreachable train stop would not cause repath of trains in NO_PATH to go to next station.
- Fixed bonuses GUI showing duplicate entries if it was open when a research finished. ( more )
- Fixed auto-launch would send rocket when there were still empty slots for payload. ( more )
- Fixed corruption related to sorting module inventories.
- Fixed logistic robots would keep trying to feed chest which has item stacks over the stack size. ( more )
- Fixed entities with wire rendering disabled in entity prototype would still have wires rendered in screenshots. ( more )
- Fixed upgrading mining drill would disable input fluid box if resource was depleted. ( more )
- Fixed pause game control input was not working when in multiplayer. ( more )
- Fixed that the RCON interface would sometimes send an extra empty reply. ( more )
- Fixed that groups of enemies wouldn't be distracted by a player in a car or tank. ( more )
- Fixed tank icon having accidental border. ( more )

### Optimizations

- Improved performance of sorting inventories.
- Improved performance of inventory highlights.

### Scripting

- Added on_player_flushed_fluid event.
- Added LuaPlayer::hand_location. ( more )

## 0.18.35

Date: 06.07.2020

### Graphics

- High resolution power switch graphics.

### Bugfixes

- Entities of other forces that are mined and brought back by undo are now set to have player force upon the undo application. ( more )
- Fixed a desync when unit group radius settings are changed.
- Fixed that the final health value in the entity damaged event was wrong. ( more )
- Fixed a performance problem with the production stats GUI. ( more )
- Fixed the double slider with discrete values functionality. ( more )
- Fix 'Train stop names' checkbox showing tooltip with no locale entry. ( more )
- Fixed rendering of pipe pictures and covers when fluid box compound covers some fluid boxes without pipe pictures or covers. ( more )

### Gui

- Visual improvements to the bonuses GUI.
- Visual improvements to the tutorial list GUI.

### Minor Features

- Gps tags are now surface aware.

### Scripting

- Added on_player_clicked_gps_tag event.

## 0.18.34

Date: 26.06.2020

### Bugfixes

- Fixed desync related to non-deterministic transport belt merging order when multiple merges happen in the same tick. ( more )
- Fixed alignment of number input entries.
- Fixed that undo didn't remove deconstruction task to remove things in the way. ( more )
- Fixed stray tooltip bug in the map generator window. ( more )
- Fixed of saving control inputs related to mouse buttons 4+. ( more )
- Fixed minor clipping issue. ( more )
- Fixed that train fuel request were unreliable. ( more )

### Gui

- Windows with item and count to be selected have count/confirm buttons disabled when item is not yet selected.
- Logistic request related item and count windows now have notched sliders for 0 to 10 stacks selection. Different numbers that are not multiplies of stacks can be still written into the textboxes.
- Added an interface option to show both crafting and logistic windows in the character screen.

## 0.18.33

Date: 24.06.2020

### Changes

- Full English text proofreading and corrections.

### Bugfixes

- Fixed Trains gui listbox labels not being readable when hovered. ( more )
- Fixed a crash when using LuaChunkIterator. ( more )
- Fixed a desync related to placing blueprint with assembling machine with not yet researched recipe. ( more )

### Gui

- Windows with item and count to be selected are now merged into single window and double click on the item auto-confirms the window with the default count. Windows affected are logistic request, signal selection and (debug tool)infinity count selections.

### Modding

- All mining results of resources are forced to be unlocked in the selection lists, even when recipe to create them exists as well. ( more )
- Added ItemPrototypeFlags::always_show, which forces the prototype to be always visible in the selection lists regardless of related recipes.
- Added RecipePrototype::unlock_results bool (true by default). When set to false, the recipe doesn't unlock the item to be shown in selection lists.
- Added RotatedSprite::counterclockwise bool (false by default). Set to true to indicate sprites in the spritesheet are in counterclockwise order.
- Added CharacterPrototype::has_belt_immunity bool (false by default).
- Entities no longer require the order string be set when there's no item-to-place them.
- Added EntityPrototype::remove_decoratives. "true", "false", or "automatic". Defaults to "automatic".
- Added TurretPrototype::attack_target_mask and ignore_target_mask. ( more )
- Changed roboport tooltip to not show robot recharge rate when the roboport has no charging slots. ( more )

### Scripting

- Added LuaRecipePrototype::unlock_results read.

## 0.18.32

Date: 16.06.2020

### Graphics

- New beacon graphics.

### Features

- Changed fluid mixing to a simpler version that only checks when manually building most things.
- Added a flush fluids button to the pipe, underground pipe, and storage tank entity GUIs.

### Gui

- Show only unlocked items in filter selection (inventory and quickbar) and logistic/trash requests. Other selections like signal selection/upgrade selection are not affected. New interface settings (off by default) bypasses this and allows the player to see all items as before.
- When selecting an element from a slot that has already value, the selected value is now going to be highlighted with the related tab (if applicable) selected.

### Bugfixes

- Fixed a few weird pixels in heat exchanger East sprites. ( more )
- Fixed player mining animation had the backpack affected by the color mask. ( more )
- Fixed mining drill status after disconnecting it from logistic network. ( more )
- Fixed massive script time usage in Wave defense scenario after configuration changes. ( more )
- Fixed that infinity GUI filters didn't list all items.
- Fixed issue with upgrading ghost of assembler with pipes. ( more )
- Fixed new electric mining drill was missing integration layer. ( more )
- Fixed crash when unit group is destroyed while its goto behavior is being updated. ( more )

### Modding

- Changed beacon graphics definitions. Graphics are now defined in graphics_set prototype property. If graphics_set is not defined, old animation and base_picture properties will be loaded instead for limited backwards compatibility.

### Scripting

- Added LuaFluidBox::flush().
- Added LuaPlayer::auto_sort_main_inventory read.

## 0.18.31

Date: 10.06.2020

### Graphics

- New electric mining drill graphics.
- Tweaked electric mining drill icon to be a bit more colorful.

### Minor Features

- Hovering over the circuit network id in the entity circuit control window will now show a tooltip with the circuit network contents.
- Added experimental Color Filters graphics option to attempt to improve accessibility for color-blind players.
- The debug setting "show-time-usage" now 'line wraps' if it doesn't fit on screen vertically.

### Bugfixes

- Fixed crash when merging force that contained unit groups. ( more )
- Fixed character preview being empty when the character is in a vehicle.
- Fixed script error when trying to load old PvP save games. ( more )
- Fixed setting vehicle driver/passenger to an offline player would crash the game. ( more )
- Fixed 4th parameter of noise.terrace function was parsed as literal number but was used as noise program register index. ( more )
- Fixed an issue with modded entities having an electric output flow limit of 0. ( more )
- Fixed that furnace recipe auto-selection didn't work correctly with temperature ranges. ( more )
- Fixed that LuaUnitGroup could be used while in an invalid destroyed state.
- Fixed button for selecting signal or number would not switch from number to signal with left click. ( more )

### Modding

- Changed mining drill graphics definitions. Graphics are now defined using working visualizations contained in graphics_set and wet_mining_graphics_set prototype properties. If graphics_set is not defined, old animations property will be loaded instead for limited backwards compatibility, but other old graphics properties will be ignored.
- Mods can now be loaded from directories with the name of the mod but no version number.
- Added color_filters to utility-constants.
- Input fluid box with connection set to output or input-output will not have volume forced down by recipe fluid ingredient amount.

### Scripting

- Added LuaSurface::show_clouds read/write.
- Added LuaPlayer::stashed_controller_type read.
- Added LuaBootstrap::register_on_entity_destroyed().
- Added on_entity_destroyed event fired after an entity registered with LuaBootstrap::register_on_entity_destroyed() is destroyed.

## 0.18.30

Date: 03.06.2020

### Graphics

- Improved 8px versions of circuits so they look better on belts when zooming out.
- Improved 8px versions of inserters so they retain their color better.
- Tweaked Steel plate and Plastic bar icons to improve contrast between them.

### Changes

- Constant combinator and infinity chest filters can now be confirmed using Enter. ( more )

### Bugfixes

- Made grey virtual signal a bit darker to have more contrast with white virtual signal. ( more )
- Fixed building entity seemingly colliding with rolling stock ghost would delete the ghost. ( more )
- Fixed Tutorial campaign level 05 had non-translated train stop names. ( more )
- Fixed tiny maps hanging in PvP. ( more )
- Fixed Wave defense bonuses being lost when technology effects were reset. ( more )
- Fixed progression block in Tutorial level 01 if you don't close the furnace GUI while smelting the iron plate. ( more )
- Fixed redundant title in modded Container gui. ( more )
- Fixed changelog gui not reacting properly to window resize. ( more )
- Fixed premature goal completed notifications in Tutorial level 03. ( more )
- Fixed transport belt madness script error when trying to handle highlight-box entities. ( more )
- Fixed tightspot output chest deleting items when starting the level. ( more )
- Fixed tutorial level 01 start cutscene could be zoomed with the scroll wheel causing glitchy rendering. ( more )
- Fixed can_insert logic related to ammo and guns on the character entity. ( more )
- Fixed crash when clearing infinity pipe filter. ( more )

### Modding

- Added 'tank_count' to fluid wagon prototype. Allowed values are 1, 2 or 3. Default value is 3. ( more )

### Scripting

- Added start_position and start_zoom to cutscene controller initialisation.
- Made final_transition_time of cutscene controller optional. If not given, the cutscene won't loop back to the start position.

## 0.18.29

Date: 01.06.2020

### Graphics

- Reworked Engine unit icon.
- Tweaked the color of Sulfur icon.

### Changes

- Updates to mini-tutorials.
- New descriptions for mini-tutorial list.

### Features

- Added support to manually set several paths through the config.ini [path] file. 'saves', 'scenarios', 'mods', 'archive', and 'script-output'

### Bugfixes

- Fixed choose-elem-button filters not being respected when clicking the button with an item in hand.

### Scripting

- Added LuaEntityPrototype::grid_prototype read.

## 0.18.28

Date: 28.05.2020

### Gui

- Minor visual changes and fixes to achievement and tutorial related guis.

### Bugfixes

- Fixed that changing script areas and positions through the map editor in multiplayer as the client didn't work correctly. ( more )
- Fixed a crash when clearing logistic requests. ( more )
- Fixed some styles being defined twice in style.lua. ( more )
- Fixed follower robot count alert not showing correctly. ( more )
- Fixed container gui not showing logistics filters properly in large containers. ( more )
- Fixed wrong open/close sound for chemical plant. ( more )

### Modding

- Added support to play a sound when opening dropdowns through opened_sound.
- Improved performance by up to 2.5x when the game needs to iterate Lua tables on the C++ side.
- Improved save/load performance of mod script data.

### Scripting

- Lua functions are now explicitly disallowed in the script 'global' table.
- Added LuaSurface::generate_with_lab_tiles read/write
- Added LuaEntity::mine().

## 0.18.27

Date: 26.05.2020

### Graphics

- New high resolution icons for all items.
- New sprites for some equipment grid items.

### Gui

- Logistic chests have a different layout.
- Visual improvements to the equipment grid.
- Minor visual improvements to most of the game GUIs.
- Minor layout changes to GUI of Combinators, Programmable speaker, Circuit and logistic connection windows, Rocket silo.
- Added a close button to most game windows.

### Sounds

- New sounds for GUI interactions.
- New sounds for game interactions, such as pipette, rotate entity, build ghost, mine ghost, switching gun.
- Updating working sounds for many entities, such as substation, roboport, combinator.
- New working sound for rocket silo.
- New sound for night vision equipment, discharge defense equipment.
- New tile build sounds for landfill, concrete, stone bricks and refined concrete.

### Changes

- Increased logistic filter count for requester and buffer chests from 12 to 30.

### Scripting

- Changed script.raise_event() to only allow mod-created events and specific game events.
- Changed script.raise_event() to validate all required fields are provided for the given event being raised.
- Added event filters for script raised revive, destroy, and created events.
- Changed event erroring so errors during raise_event are properly blamed on the mod erroring.
- Changed raise_event ordering to match standard event ordering.
- All game events that support filters now filter correctly regardless of how they're raised (raise_event or actual game event).

## 0.18.26

Date: 21.05.2020

### Changes

- Crafting machines will now refund item ingredients when crafting is cancelled before finishing.
- Disallowed saving over autosave files or making saves that begin with '_autosave'.

### Bugfixes

- Fix tutorial description only mentioning 3 levels instead of the full 5. ( more )

### Modding

- Changed default value of return_ingredients_on_change property of furnaces, assembling machines and rocket silo to 'true'.
- Added script_raised_set_tiles.
- Added by_player to LuaEntity::copy_settings()
- Added by_player to LuaEquipmentGrid::take, take_all, clear, and put.

## 0.18.25

Date: 19.05.2020

### Features

- Added new tutorial campaign levels 04 and 05. ( https://www.factorio.com/blog/post/fff-347 )

### Changes

- Added a search bar to the mod settings GUI.

### Bugfixes

- Fixed a crash when building entity ghosts that immediately get invalidated through script.
- Fixed that the choose-elem-button elem_type "signal" didn't show special signals. ( more )
- Fixed that furnaces required module slots to be effected by beacons. ( more )
- Fixed that some select-a-thing GUIs didn't have search bars. ( more )
- Fixed that LuaEntity::revive({raise_revive=false}) would still raise the revive event.
- Fixed a crash when trying to iterate game.forces with the maximum number of forces created. ( more )
- Fixed a desync related to fast-replacing modded beacons. ( more )
- Fixed performance issue with initializing huge Lua arrays, that could cause loading of some modded saves take forever. ( more )

### Modding

- Added item prototype flag "draw-logistic-overlay".
- Added support to play a sound when a robot deconstructs something through utility-constants "deconstruct_robot".

### Scripting

- Added on_force_reset event called when LuaForce::reset() is run.
- Added remove_colliding_entities and remove_colliding_decoratives parameters to LuaSurface::set_tiles().
- Added LuaSurface::get_script_area, edit_script_area, add_script_area, remove_script_area, get_script_position, edit_script_position, add_script_position, remove_script_position.
- Added 'elem_filters' onto choose-elem-button LuaGuiElements to control what options appear in the picker GUI.
- Added 'crafting-category' filter to EntityPrototypeFilters.
- Added 'has-ingredient-fluid', 'has-ingredient-item', 'has-product-fluid', 'has-product-item' filters to RecipePrototypeFilters which can accept a nested set of FluidPrototypeFilters or ItemPrototypeFilters.
- Added 'place-result', 'burnt-result', 'place-as-tile', 'placed-as-equipment-result' filters to EntityPrototypeFilters which can each accept a nested set filters.
- Added 'name' filter to EntityPrototypeFilters, FluidPrototypeFilters, and ItemPrototypeFilters which accepts either a single name or a list of names to accept, similar to LuaSurface::find_entities_filtered.

## 0.18.24

Date: 12.05.2020

### Bugfixes

- Fixed version 0.18.23

## 0.18.23

Date: 12.05.2020

### Graphics

- Added player footprints and footstep visual effects.
- Added car and tank dust and particle trail visual effects.

### Changes

- Construction robots throw cliff explosives from afar the same as players do, instead of dropping them at the cliff.
- Changed rail segment visualisation colors to be more different from rail signal colors (red/green).
- Clicking a GUI now brings it to the front. Most noticeable when using the map editor or debug GUIs where they overlap.

### Bugfixes

- Fixed that Fast splitters were missing a piece visually in East rotation top_patch ( more )
- Fixed that inserters could insert modules for recipes into module slots in some rare cases. ( more )
- Fixed that robots blowing up cliffs was different than manually blowing up cliffs. ( more )
- Fixed limiting cargo wagon to 0 slots would break progress visualization for full cargo and empty cargo train conditions. ( more )
- Fixed teleporting player between surfaces while the player was in a map view would not invalidate tile renderer cache. ( more )
- Fixed that the "use different settings per save" setting didn't work for single player games. ( more )
- Fixed crash due to use-after-delete when single unit builds a base in position that does not collide with the unit. ( more )

### Modding

- Added the Prototypes GUI (ctrl + shift + E).
- Added the Prototype Explorer GUI (mouse over most anything + ctrl + shift + F).
- Added support to play different sounds for entity ghosts depending on the size of the entity in the ghost through build_sound (for small), medium_build_sound and large_build_sound on the entity ghost prototype.
- Added support to play a sound when switching weapons defined through utility-sounds 'switch_gun'.
- Added support to play a sound when picking up items (F key) through utility-sounds 'picked_up_item'.
- Added optional 'turn_speed' to projectile prototypes.

### Scripting

- Added "include_fuel" field to LuaItemStack::create_blueprint.
- Changed LuaSurface::create_entity so it places resource entities to center of a tile as map generator would. This can be overridden by optional snap_to_tile_center parameter. ( more )

## 0.18.22

Date: 30.04.2020

### Graphics

- Added shell particle effect for the artillery shooting.
- Added tinted scorch marks for explosion effects. Explosions on different tile types will result in scorch marks of different colors.

### Changes

- Pressing escape/close GUI when a search field is focused only closes the search field instead of the entire GUI.
- Updated GUI styles for PvP configuration GUI.
- Unit groups will determine their collision mask based on the collision masks of their members. ( more )

### Bugfixes

- Fixed landfill spawning under player when building landfill elsewhere. ( more )
- Fixed a crash when a train recalculating path during movement is unable to reserve rail signal within movement distance. ( more )
- Fixed production statistics corruption when recipe returns some but not all catalyst. ( more )
- Fixed a pathfinding crash related to changing tiles in a way that affected neighbouring tiles' transitions. ( more )
- Fixed that malformed data in data.raw wouldn't show the minimal-mode failure GUI. ( more )

### Modding

- Fixed that writing to mod settings would silently ignore bad values.
- Added "allowed_effects" support to the lab.
- Added "creation_distance_orientation", "use_source_position", "height" and "vertical_speed" to particle creation parameters (related to shooting effect shell particles).
- Added "scorch_mark_color" to TilePrototype.
- Added util.remove_tile_references for easier compatibility maintenance with future game updates when removing base game tiles.
- Removed migration for CustomInputPrototype consuming types that were removed in 0.15.24.

## 0.18.21

Date: 24.04.2020

### Bugfixes

- Fixed that the mod settings GUI was only showing hidden settings. ( more )
- Fixed crash in mod updater. ( more )

## 0.18.20

Date: 24.04.2020

### Features

- Added new environmental trigger effects for grenade, artillery and nuke explosions. ( https://www.factorio.com/blog/post/fff-343 )
- Added 3 level 'First steps' tutorial Campaign. ( https://www.factorio.com/blog/post/fff-342 )
- Mini-tutorial improvements.

### Changes

- Moved Compilatron and Compilatron speech-bubble entities from demo to base game files.
- Removed Introduction Campaign.
- Removed Compilatron chest, Compilatron roboport, Compilatron logistic chest.
- Removed Tutorial/Campaign Lualib (base/lualib).
- Removed other campaign-only prototypes, such as styles, sprites, sounds.

### Bugfixes

- Fixed that thumbnails wouldn't show in the update-mods tab of the mods GUI. ( more )
- Fixed that LuaSurface::spill_item_stacks return value didn't work correctly. ( more )
- Fixed that the research progress of the current tier showed for next queued tier in the technology GUI. ( more )
- Fixed that the game didn't validate modded rail-planner item type values and would crash in some cases. ( more )
- Fixed that modded units with consider-tile-transitions in their collision mask would cause the pathfinder to crash. ( more )

### Modding

- Empty layers in sprite or animation definition will yield an error now. ( more )
- Added support for playing a sound when using smart-pipette.
- Added support for playing activate/deactivate sounds for night vision.
- Added support for playing a sound while an resource-style is being mined through mining_sound.
- Added mod-setting value "hidden" to hide mod settings from the GUI.
- Added 'invoke-tile-trigger' and 'destroy-decoratives' trigger effects.
- Added 'rotate-offsets' to the create-particle trigger effect.
- Added 'trigger_effect' to tiles. It is called with the 'invoke-tile-trigger' trigger effect.
- Added 'trigger_effect' to decoratives. It is called when the decorative is destroyed with the 'destroy-decorative' trigger effect.

### Scripting

- Added on_pre_script_inventory_resized and on_script_inventory_resized events.
- Added 'allow_paths_through_own_entities' and 'no_break' path finding flags.
- Added LuaModSettingPrototype::hidden read.
- Added 'to_be_deconstructed' to the options for LuaSurface::find_entities_filtered. ( more )
- Added LuaGuiElement::badge_text read/write.

## 0.18.19

Date: 20.04.2020

### Bugfixes

- Fixed a crash when loading saves from 0.18.12 and older while re-spawning and having personal logistics researched. ( more )
- Fixed offshore pump selection box to match the new graphics. ( more )
- Fixed possible performance issue related to animated trees in OpenGL rendering backend. ( more )
- Fixed opening the character GUI through hotkey when the logistic tab isn't visible. ( more )
- Fixed that curved rail ghosts selection didn't work quite right. ( more )
- Fixed that the offshore pump would play sounds even when it wasn't doing anything. ( more )
- Fixed wrong Lua docs for LuaCommandProcessor::add_command. ( more )
- Fixed a desync when personal logistics is researched while a player is disconnected from the server with personal logistics disabled. ( more )
- Fixed a crash when moving armors around in other players inventories in multiplayer. ( more )
- Fixed a regression issue with the select-a-signal GUI related to group ordering. ( more )
- Fixed that trying to load a save created from a scenario in a now disabled/removed mod would crash the game. ( more )
- Fixed a crash when trying to join games through Steam when the Steam API fails to initialize.
- Fixed that the character corpse wasn't included in the post-player-died event 'corpses' parameter. ( more )
- Fixed that trains pathfinder could create non contiguous path in case of single segment cycle with a single train stop. ( more )

### Modding

- Added warning for empty layers in sprite or animation definition. In next release, this will become an error. ( more )
- Added a check to make sure placeable_by.count isn't larger than the placeable_by.item.stack_size. ( more )
- Added support to play sounds when left clicking radio buttons and checkboxes.
- Added ParticlePrototype::fade_away_duration and vertical_acceleration.
- Rolling stock entities can no longer have next_upgrade set.
- Added support for rotated_sound on entity prototypes.

### Scripting

- Fixed that LuaEntityPrototype::fluidbox_prototypes didn't include fluid energy source fluidbox prototypes.
- Added LuaEntity::productivity_bonus, pollution_bonus, speed_bonus, and consumption_bonus read.
- Added LuaGameScript::create_inventory() and get_script_inventories().
- Added LuaInventory::destroy() and resize().
- Added LuaInventory::mod_owner read.
- Added LuaEntityPrototype::adjacent_tile_collision_box, adjacent_tile_collision_mask, adjacent_tile_collision_test, center_collision_mask read to access new offshore pump prototype properties.
- Added "final-health" to the entity-damaged event.
- Added "final-health" to the entity-damaged event filter.
- Added LuaGameScript::max_force_distraction_distance, max_force_distraction_chunk_distance, max_electric_pole_supply_area_distance, max_electric_pole_connection_distance, max_beacon_supply_area_distance, max_gate_activation_distance, max_inserter_reach_distance, max_pipe_to_ground_distance, max_underground_belt_distance read.
- Added LuaEntity::deplete().

## 0.18.18

Date: 08.04.2020

### Changes

- Adjusted steam engine and turbine collision boxes so player can walk between two steam engines.
- Roboports allow exporting both logistics and robot stats at the same time. ( more )

### Graphics

- Added offshore pump remnants.
- Added new dying effects for biters, spitters, worms, and spawners.

### Gui

- Added confirmation box for deleting blueprint book.

### Sounds

- New or updated sound effects include:
- Transport belts - new concept for these sounds.
- Turrets rotation sounds and fold/unfold.
- Weapons improved and made more powerful, e.g. submachine gun, shotgun, gun turret, vehicle machine gun, Laser and electric beam.
- Particles: Water splashes, Tree debris.
- Various mix level tweaks including the train, enemies.
- Attenuations (audible distance) adjusted for entities such as Pipe, Substation and Offshore Pump.
- New sound when walking over ore patches.
- Default Sound Settings Updated:
- Music, Game Effects and Walking sound lowered, Environment sounds and Master Level raised.
- Zoom audible distance and volume levels adjusted.
- Maximum Environment Sounds increased (edited).

### Bugfixes

- Fixed mining entity with randomized mining result amount would never return the largest defined amount. ( more )
- Fixed crash when loading replay. ( more )
- Fixed reading LuaPlayer::entity_copy_source when the player is dead. ( more )
- Fixed that upgrading and delivering modules at the same time didn't work right. ( more )
- Fixed a crash when closing the game while some GUIs are shown. ( more )
- Fixed crash when setting max_group_gathering_time and min_group_gathering_time to the same value. ( more )
- Fixed discharge defense equipment had the wrong sprite in the equipment grid. ( more )
- Fixed that artillery wagons wouldn't show out of ammo icons. ( more )
- Fixed that modded cargo wagon colors wouldn't copy correctly through blueprints. ( more )
- Fixed furnaces with recipes using fluid ingredients could cause crash. ( more )
- Fixed a crash when removing a player that has modded associated character entities. ( more )

### Modding

- Furnaces now ignore off_when_no_fluid_recipe property of their fluid box definition. Fluid boxes will not be disabled based on enabled recipes. ( more )
- Changed colored concrete tiles to be non-mineable.

### Scripting

- Added LuaEquipmentPrototype::automatic.
- Added "include_entities", "include_trains", "include_station_names", and "include_modules" fields to LuaItemStack::create_blueprint.
- Added LuaRoboportControlBehaviour::read_logistics and read_robot_stats
- Removed LuaRoboportControlBehaviour::mode_of_operations

## 0.18.17

Date: 27.03.2020

### Bugfixes

- Fixed Map Generator GUI becoming larger than the screen. ( more )
- Fixed Blueprint Setup GUI becoming larger than the screen. ( more )
- Fixed number pad Enter would be ignored by personal logistic request setup GUI if it was bound to in-game action. ( more )

## 0.18.16

Date: 25.03.2020

### Graphics

- New water splash effects using water particles instead of an animation.
- New animations for leaf particles.

### Bugfixes

- Fixed the tank not being properly centered to its bounding box (graphical issue).
- Fixed GUI windows not drawing properly when they can't fit the screen width. ( more )
- Fixed glowing Heat pipe ending sprites. ( more )
- Fixed some character bonuses in bonus GUI not being printed correctly. ( more )
- Fixed character GUI player color sliders not changing chat colors ( more )
- Fixed that hotkeys wouldn't work while using the character logistics GUI in some cases. ( more )
- Fixed a desync related to unit speed changing while part of a unit group. ( more )
- Fixed some Trigger Effects not showing correct repeat count in tooltips. ( more )

### Scripting

- Added LuaEntity::effective_speed
- Added LuaControl::is_flashlight_enabled
- The 'on_ai_command_completed' event will now fire for distraction commands.
- Added 'was_distracted' to the 'on_ai_command_completed' event. If true, it means the completed command was a distraction command.

## 0.18.15

Date: 20.03.2020

### Changes

- ENTER key can now be used to confirm the small "Set request" pop-up windows.

### Bugfixes

- Fixed that defines.gui_type was missing some values. ( more )
- Fixed tabs not changing correctly in the item select gui for train circuit/item/fluid conditions. ( more )
- Fixed that deleting blueprints didn't work in some cases. ( more )
- Fixed a crash related to fast-replacing character entities through mods. ( more )
- Fixed that the "watch your step" achievement wouldn't show the achievement popup. ( more )
- Fixed script error when starting the mini-tutorials. ( more )
- Possibly fixed setting up heavily edited blueprints could drop players in multiplayer. ( more )
- Fixed that the graph in statistics GUI wouldn't show some data series if the search was being used. ( more )

### Scripting

- Serpent now uses 0 instead of nil as a placeholder in case of cyclic references. This will help prevent some specific desyncs with custom scenario or mod scripts.

## 0.18.14

Date: 18.03.2020

### Gui

- The production statistics and electric network GUIs now have a new look.
- The kills GUI (K keyboard shortcut) has been removed. Kills statistics are now accessible as a tab in the production statistics GUI.

### Bugfixes

- Fixed an issue with nested items in items. ( more )
- Fixed Character GUI missing logistics tab due to missing technology migration. ( more )
- Fixed Character GUI recipes constantly scrolling up when crafting or when inventory changes. ( more )
- Fixed that simple mouse click on double slider button would not set a slider as active. ( more )
- Fixed that tabbing out of empty high value textfield of double slider would reset it to 0. ( more )

### Scripting

- Removed the defines.gui_type.kills value from defines.gui_type.

## 0.18.13

Date: 17.03.2020

### Gui

- The character GUI now has a new look.
- Personal logistics has been moved to a separate tab. Logistic requests and auto trash have been merged into one panel.
- Using quick inventory transfers in the player inventory of the character gui will transfer the items either to weapons and armor slots or to trash slots depending on the selected tab, regardless of item type.
- Updated the look of filter, item and circuit signal selection GUIs.

### Changes

- Personal logistics are now unlocked by a single research. This unlocks personal logistic requests and auto trash(unlimited count), plus 30 character trash slots.
- Removed the restriction of not allowing to have two identical blueprints in the blueprint library or blueprint book.
- Allowed to delete blueprint/books/upgrade planners/deconstruction planners also when opened in other inventory.
- Removed the utility slots (to create blueprint, book etc) from blueprint library as it is now available directly through quick tools menu.
- Allowed to edit blueprints in the blueprint library the same way as when it is an item.
- Allowed to export blueprint books in blueprint library (it was only possible in inventory before).
- Allowed to choose whether train fuel should be included in a blueprint.

### Bugfixes

- Fixed that 3rd last row of 4th sheet of gun turret shooting had duplicate frame. ( more )
- Fixed desync when changing recipe that was outputting large amount of fluid per crafting cycle to recipe that outputs low amount of fluid. ( more )
- Fixed sprite button would not respect draw_shadow_under_picture style property. ( more )

### Modding

- Added main_menu_background_image_location to utility constants.

### Scripting

- Removed LuaStyle::extra_padding_when_activated read/write.
- Added LuaStyle::extra_top_padding_when_activated, extra_bottom_padding_when_activated, extra_left_padding_when_activated and extra_right_padding_when_activated read/write.

## 0.18.12

Date: 10.03.2020

### Bugfixes

- Fixed that some Lua events related to inventories would always report invalid. ( more )

## 0.18.11

Date: 10.03.2020

### Graphics

- Fixed player character shadow didn't animate in idle state when not facing north.

### Bugfixes

- Fixed that LuaEntity::splitter_filter would reject a LuaItemPrototype. ( more )
- Fixed smart entity collision mode in tile editor did not work with offshore pump. ( more )
- Fixed that modded shortcuts that spawned items not visible in the blueprint library didn't work. ( more )
- Fixed that technology tooltips didn't show debug tooltip data the same as other tooltips. ( more )
- Fixed that crafting machines would report as supporting backer names through the Lua API. ( more )
- Fixed that un-researched recipes couldn't be used while in the map editor. ( more )
- Fixed that the removed-content GUI didn't include some translations. ( more )
- Fixed a desync related to invalid rail signal requested to be closed by circuit network. ( more )

### Modding

- Added InserterPrototype::chases_belt_items. ( more )

### Scripting

- Added LuaEntityPrototype::inserter_chases_belt_items read.
- Added surface to the selected-area events.
- Changed LuaSurface::spill_item_stack() to return the created entities if any.

## 0.18.10

Date: 03.03.2020

### Graphics

- New offshore pump graphics.

### Changes

- Removed the sound effect from the console-only electric-energy-interface.
- Item localised name takes priority over place-result localised name when showing item's tooltip. ( more )
- Offshore pump is now buildable on ground tile adjacent to water instead of water tile adjacent to ground.

### Bugfixes

- Fixed that the map generator GUI didn't reset to the correct defaults when changing presets. ( more )
- Fixed blueprint window sizing for wide blueprints.
- Fixed some cases of not considering dark background icon when drawing alt mode overlay. ( more )
- Fixed that burner generator idle_animation and animation could have different frame counts.
- Fixed icons with overlays were drawn incorrectly when used in sprite widget. ( more )
- Fixed crash when loading map after removing fluid recipes with indexes. ( more )
- Fixed spitters would not break from attacking an obstacle when the obstacle moved away. ( more )

### Modding

- Added Instrument Mode to support mod development tools.
- Added optional burner generator prototype properties always_draw_idle_animation, performance_to_sound_speedup and min_perceived_performance.
- Added optional offshore pump prototype properties min_perceived_performance, adjacent_tile_collision_box, adjacent_tile_collision_mask and center_collision_mask.
- Changed offshore pump graphics definition. Old definition will still be accepted, but is deprecated.

### Scripting

- Added optional parameters daytime and water_tick to LuaGameScript::take_screenshot() function.

## 0.18.9

Date: 25.02.2020

### Features

- Added Rocket rush scenario. ( https://factorio.com/blog/post/fff-335 )

### Changes

- Changed Team production team joining system and cleaned up the map sets.
- Changed Wave defense bounty system and refactored unit spawning logic.
- Changed fire sticker to deal damage only once per 10 ticks.

### Graphics

- Added big scorch mark which is now used by atomic rocket and nuclear reactor meltdown.

### Bugfixes

- Fixed that fluid energy source effectivity was not shown in the tooltip. ( more )
- Fixed that the default column ordering in the update-mods GUI didn't match the visual ordering. ( more )
- Fixed that train could accelerate for one tick into wrong direction when train stop is disabled. ( more )
- Fixed that minimap would not allow setting temporary train stop when train would have to change movement direction. ( more )
- Fixed damage value in sticker tooltip was 60 times too small.
- Fixed icons with overlays were drawn incorrectly when used in rich text. ( more )
- Fixed PvP error when DEFCON was active alongside normal labs. ( more )
- Fixed that modded recipes with no products or no ingredients still showed those sections in the recipe tooltip. ( more )
- Fixed that modded burner generator equipment didn't show pollution in the tooltip. ( more )
- Fixed teleporting or changing the force of an entity with a control behavior that was connected to the logistic network. ( more )
- Reverted optimisation that caused inserters picking up items from belts to be slower.

### Modding

- Added support to filter on-damaged trigger effects through the trigger prototype definition.
- Added secondary_draw_order property to simple-entity prototypes.
- Added StickerPrototype::damage_interval, defaults to 1.

### Gui

- Updated the window of creating/editing blueprint.

### Scripting

- Added LuaTile::surface read.
- Added event filtering support to on_sector_scanned and on_entity_cloned.
- Added "original-damage-amount", "final-damage-amount" and "damage-type" filters to the on_entity_damaged event filters.
- Added LuaGameScript::is_valid_sprite_path().
- Removed the required argument from LuaEnity::to_be_deconstructed() because it did nothing.

## 0.18.8

Date: 18.02.2020

### Bugfixes

- Fixed that setting infinity filters through script didn't update the GUI. ( more )
- Fixed that dedicated server authentication didn't work when using the token option. ( more )

## 0.18.7

Date: 18.02.2020

### Graphics

- New visuals for poison capsule effect.
- New dying effect and remnants for flying robots.

### Sounds

- Entity destroyed alert - Sound softened and lowered in volume.
- Weapon sounds (WIP) - new Pistol, Submachine gun, Gun turret, Laser turret.
- Logistic chests open sound (WIP).
- Poison capsule cloud (WIP).

### Bugfixes

- Fixed that reordering heat buffers during the same tick a different heat buffer was built would leave the heat buffer state corrupted. ( more )
- Fixed that entity sounds with probabilities would loop forever once they started playing. ( more )
- Fixed rocket silo tooltip did not include contents of the rocket result inventory. ( more )
- Fixed that styles were applied to wrong slot in a filtered train view. ( more )
- Fixed that server authentication would fail if both the token and username and password were provided. ( more )
- Fixed that changing inserter pickup/dropoff through mods didn't work correctly. ( more )
- Fixed that combat robots had their fire resistance overwritten. ( more )
- Fixed that rolling stocks were not pulled correctly when train was moving through curved rails. ( more )
- Fixed that LuaEntityPrototype::burner_prototype didn't work for the burner-generator entity type. ( more )
- Fixed janky construction robot flying animation during repair work. ( more )

### Scripting

- Added optional LuaItemStack::build_blueprint raise_built.
- Added LuaInventory::find_empty_stack(), count_empty_stacks(), and get_insertable_count().
- Added LuaEntityPrototype::heat_energy_source_prototype, fluid_energy_source_prototype, and void_energy_source_prototype read.
- Added LuaGameScript::encode_string() and decode_string().
- Added on_player_set_quick_bar_slot.
- Added on_pre_player_toggled_map_editor.
- Removed LuaPlayer::name write. ( more )
- Removed core lualib util.encode() and util.decode().

## 0.18.6

Date: 11.02.2020

### Bugfixes

- Fixed infinite loop in renderer when trying to render water reflections created by off-screen entities under some circumstances. ( more )

## 0.18.5

Date: 11.02.2020

### Bugfixes

- Fixed a crash related to multiple blocks reserved for different trains but later merged by placing a rail. ( more )
- Fixed that construction robots were missing their working animation. ( more )
- Fixed circuit network debug visualization text overlap. ( more )
- Fixed the circuit network tooltip backgrounds didn't highlight correctly. ( more )
- Fixed that script.active_mods wouldn't be accurate when loading save files in some cases. ( more )
- Fixed that the sync-mods-with-save feature would try to download mods it didn't need to in some cases. ( more )
- Fixed that trains pathfinder could create non contiguous path in case of single segment cycle with a junction. ( more )
- Fixed possible crash when units were attacking rails with train on them. ( more )
- Fixed pump would consume energy and play animation when it tried to transfer very small amount of fluid but failed to do so. ( more )
- Fixed creating fire entity by trigger effect invoked by a particle would crash the game.
- Fixed overriding LuaSurface::brightness_visual_weight would cause light map to appear in map view. ( more )

### Scripting

- Building entities with from items with 0 health will set the entity to 1 health instead of 0. ( more )
- Added LuaGameScript::reset_time_played() which will reset the 'Time played' to 0.

## 0.18.4

Date: 06.02.2020

### Balancing

- Wave defense difficulty will scale with online player count.
- Wave defense hard difficulty will give 50% less bounty on each kill.

### Sounds

- New sound for small explosion.
- Combat robots now have their own explosion sound.
- Shotgun has more variety so it sounds less repetitive.
- Vehicle impacting wooden objects (e.g chests) now sounds subtly different to crashing into trees.
- A few minor volume level changes including lowering the offshore pump and electric furnace.

### Bugfixes

- Fixed a crash when saving fails due to mod issues. ( more )
- Fixed a crash that would happen when the player entered a vehicle when some biters were aggroed at them. ( more )
- Fixed that cargo wagons built while a train is moving didn't animate the doors correctly. ( more )
- Fixed an error when using modded night vision defined in zip files. ( more )
- Fixed a performance issue with assembling machine result slot tooltips. ( more )
- Fixed that items marked with the mod-openable flag couldn't be opened from the quickbar in some cases. ( more )
- Fixed that train could fail with chain signal sequence escape maneuver when path goes multiple times through a rail segment.
- Possibly fixed seam on terrain at certain position and zoom level. ( more )
- Fixed that sometimes wave defense would trigger victory before killing all spawners. ( more )

### Scripting

- Fixed that writing to LuaForce::stack_inserter_capacity_bonus was limited to 200 instead of 254.

### Modding

- Changed definitions of map colors of beacons, pipes, heat pipes, roboports and steam engines, so they can be overridden by friendly_map_color. ( more )
- Added ParticlePrototype::ended_on_ground_trigger_effect.
- Added fuel burnt results to the item tooltip.
- Loader remnants will pick rotation the same way as underground belts do. ( more )

## 0.18.3

Date: 30.01.2020

### Graphics

- Applied LUT color correction to new explosions.

### Sounds

- Transport belts - high frequencies reduced.
- Train - pitch scaling reduced and sound levels remixed (Work in Progress).
- Inserters lowered in level slightly (Work in Progress).
- Compilatron muted as it was too annoying.
- Removed scrollbar GUI click sound.

### Changes

- Overwriting a save file will show a confirmation if the selected save has more playtime on it than what you are about to save. ( more )

### Bugfixes

- Fixed tile rendering would break at extremely low zoom. ( more )
- Fixed dragging train schedules in the train GUI. ( more )
- Fixed a crash when migrating loader entities in blueprints. ( more )
- Fixed fast entity split to burner inserters. ( more )
- Fixed that the pump could never reach its pumping speed of 12000/s. ( more )( more )
- Fixed logistic and combat robots were missing dying explosion effect.
- Fixed migration of 1x1 loaders from pre-0.18 saves. It still might result in loss of items on transport lines that start on the migrated loaders.

## 0.18.2

Date: 28.01.2020

### Graphics

- Improved map colors by adding specific colors to beacons, pipes, heat pipes, roboports and steam engines.

### Sounds

- New or updated sound effects include:
- Pump, pumpjack, boiler, heat pipe, offshore pump, substation.
- Logistic and construction robots, roboport.
- Train.
- Rocket takeoff sequence.
- Car and tank (pitch scaling adjusted to sound more natural).
- All transport belts, splitters, inserters, assembling machines, power switch.
- Added some UI sounds that were missing.
- Shotgun, small explosions.
- Entity destroyed alert.
- New sound tech includes:
- Listener position set to centre of screen by default. This will allow you to hear what you see even when in map mode.
- The ability to turn off the Doppler effect in Lua, used for the Substation so far.
- environment-audible-distance setting increased to 30 so you can hear entities a bit further away.
- zoom-volume-coefficient changed so you can hear more of the world when you zoom out. This will help with combat and give a greater sense of the overall factory.

### Bugfixes

- Fixed that pressing escape in some log-in screens lead to blank screen or incorrect states. ( more )
- Fixed enemy walls should not render as connected to ghosts, since enemy ghosts are not visible. ( more )
- Fixed undo on self-looped combinator ghosts not restoring wires. ( more )
- Fixed achievement cards not showing description when descriptions are turned off in interface settings.
- Fixed that inserters from 0.17 save files could end up teleporting items into/from trains. ( more )
- Fixed that the sync mods with save GUI wouldn't size correctly. ( more )
- Fixed that thrown capsules could end up broken forever if thrown at exactly the right tick. ( more )
- Fixed crash when using "create-entity" trigger effect item to create an artillery flare. ( more )
- Fixed map view night LUT. ( more )
- Fixed a crash that would sometimes happen when a biter, who was in previous versions of the game aggroed by a player in a car or tank, was aggroed again. ( more )
- Fixed crash when joining a game through Steam without having previously logged in.

### Modding

- Migrating loaders between loader and loader-1x1 will maintain the loader type (input/output). ( more )

### Scripting

- Added LuaSurface::create_particle().
- Added LuaEntityPrototype::inserter_pickup_position and inserter_drop_position read.

## 0.18.1

Date: 23.01.2020

### Changes

- Train stop at train's starting segment exit is no longer counted into penalty. ( more )
- Inventory transfers mini-tutorial has been updated to feature the quickbar.
- Split the map editor sub-menu into more options so it's more clear when scenarios are copied and when they are edited directly.

### Bugfixes

- Fixed replay gui covering tooltips. ( more )
- Fixed tooltips in statistics window not showing force modifiers. ( more )
- Fixed electric mining drill was missing dying explosion. ( more )
- Fixed when using OpenGL backed turret range overlay was rendered incorrectly when zoomed in. ( more )
- Fixed a crash when using script.get_event_order during control.lua init. ( more )
- Fixed that LuaForce::reset_technology_effects() could change the enabled/visible when disabled state. ( more )
- Fixed wrong lua docs about what event(s) could be filtered. ( more )
- Fixed a wrong error message related to multiplayer and migration scripts. ( more )
- Fixed crash when rail with temporary train stop is removed. ( more )
- Fixed crash if you attempted to ping a train wagon immediately after placing it on a multiplayer server with high latency. ( more )
- Fixed that clicking the drop-down widget in the map editor script section would stop the mouse from working. ( more )
- Fixed nightvision effect was applied to zoomed-to-world view sometimes. ( more )
- Fixed that enemies would attack rails. ( more )

### Modding

- Changed default value of LoaderPrototype::structure_render_layer from "transport-belt-circuit-connector" to "object", in order to be consistent with other on-belt structure sprites. ( more )

### Scripting

- Added LuaEntity::get_damage_to_be_taken().
- Added LuaSurface::brightness_visual_weights to add back ability to control darkness of the night runtime per-surface. ( more )

## 0.18.0

Date: 21.01.2020

### Features

- Steam users can now log in automatically through Steam without needing their Factorio account password.
- Steam users without a Factorio account can create one by providing only a username.
- Reworked main menu structure.
- Added a "Continue" button which quickly loads the latest save game.
- Added a "New Game" GUI that shows all the ways to play the game
- Added a setting to the map editor to show/hide the extra entity settings.
- Added a map editor GUI to edit force data modifiers.
- Added a PvP team option to create a moat around the starting area.

### Graphics

- Added animation to water.
- Added animation to trees.
- Added LUTs and color corrected the game sprites.
- Added sliders to the graphics settings to adjust brightness, contrast, and saturation.
- Added on damaged effects for most entities.
- Added specific dying explosions for most entities.

### Sounds

- New or updated sound effects include:
- Nuclear reactor, chemical plant, furnace, fire, burner mining drill.
- Tank.
- Mining by hand, chopping wood
- Roboport door, Combat robots
- Player footsteps.
- Biter and Spitter footsteps.
- Worm breathing, Spitters and Biters, idling and attacking.
- New sound features include:
- The ability to fade out sounds instead of a sudden stop, e.g. for the furnace.
- Varying the pitch of sounds to a min/max level, to add more variety.
- A 'Random, no repeat' feature to reduce repetition, especially on sounds that happen frequently, such as player steps.
- The sound for the game has also been rebalanced to highlight certain sounds and make others fade into the distance.
- The default sound settings have also been updated to improve this mix.

### Optimizations

- Optimized particle logic.
- Improved performance when side-loading transport belts.
- Improved performance of inserters interacting with assembling machines and furnaces.
- Improved performance of inserters when the circuit network turns them off.
- Improved performance of mining drills and inserters in general.
- Improved performance of burner entities.
- Improved performance polluting entities.
- Improved performance of smoke producing entities.
- Improved performance logistic and construction robot performance when they're flying towards their target.
- Improved performance of furnaces and assembling machines that use fluids.
- Improved heat pipe performance by 3x.
- Improved item request proxy performance by turning them off in 99%+ of the cases.
- Improved locomotive, cargo wagon, and fluid wagon performance by turning them off in 99%+ of the cases.
- Electric networks, fluids, and heat pipes are updated in parallel if you have enough cores.
- Improved script rendering performance for text and lines.
- Improved performance of rotated bounding boxes.

### Bugfixes

- Fixed the recipe tooltip showing negative values for some complex recipes.  ( more )
- Fixed graphical glitch when GUI element with blurred background got out of bounds of the screen. ( more )
- Fixed hard coded English string in NPE. ( more )
- Fixed potential crash in NPE when Compilatron is pointing at something that gets deleted. ( more )
- Fixed issue where sometimes you couldn't move to the second area in NPE. ( more )
- Fixed issue where Compilatron would sometimes tell you to build more boilers when that was not the problem. ( more )
- Fixed issue where Compilatron's speech bubbles could block you from interacting with the world behind him. ( more )
- Fixed items with excessively long names squashing the count label in the recipe tooltips. ( more )
- Fixed accumulator charge text in statistics bouncing around because of inconsistent number of digits. ( more )
- Fixed train path finding penalty when there are 2 or more trains in block. ( more )
- Fixed a crash when creating trains during the player moved event that was caused by the player getting ejected from a vehicle because the vehicle died. ( more )
- Fixed a crash when removing mods that had custom GUI elements. ( more )
- Fixed a crash when using Lua event filters when the thing to be filtered becomes invalid. ( more )
- Fixed that some turret sounds could be heard on other surfaces. ( more )
- Fixed that the tooltip for the generator would not show its efficiency correctly. ( more )
- Fixed a crash related to building tiles in multiplayer with some mods. ( more )
- Fixed that turrets would sometimes fail to attack things that are in range. ( more )
- Fixed follower robot lifetime tooltip property not taking into account following_robots_lifetime_modifier. ( more )
- Fixed cliffs sometimes getting marked for deconstruction when they shouldn't have been. ( more )
- Fixed inconsistent rounding in the statistics window. ( more )
- Fixed a desync when setting .active=false on beacons through script. ( more )
- The map will be re-charted when the mod configuration changes. ( more )
- Fixed inserters sometimes not being highlighted when selecting a large modded vehicle. ( more )
- Fixed a crash when entity grid would destroy itself during update. ( more )
- Fixed a crash with rich text tags and dynamic images. ( more )
- Fixed setting the held stack of an inserter didn't update the inserter state correctly. ( more )
- Fixed tooltip alignment in some specific cases. ( more )
- Fixed a crash when lua removes pipe-to-ground between entity revive and deferred pipe connection fix. ( more )
- Fixed a crash when setting infinity chest filters to legacy items. ( more )
- Fixed that splitters could be set to have invalid bounding boxes that would lead to corrupt saves. ( more )
- Fixed word wrapping of rich text containing tag that doesn't fit given width would duplicate the tag on multiple lines. ( more )
- Fixed if migrating old achievement data to Steam Cloud failed, the old file would not be deleted resulting in the same error on every startup. ( more )
- Fixed train pathfinding penalty for circuit network closed rail signal was not applied in some cases. ( more )
- Fixed a crash when mods would define construction robots without some sprites. ( more )
- Fixed that trying to do 0 damage would still trigger the entity-damaged event. ( more )
- Fixed a save corruption issue related to modded loaders with different belt_distance values. ( more )
- Fixed that train would forget amount of ticks waiting at signal when doing repath. ( more )
- Fixed that train pathfinder was not counting penalty of last segment length in path cost. ( more )
- Fixed PvP error on configuration changed. ( more )
- Fixed pump tooltip showing double pumped amount when pumping to fluid wagon. ( more )
- Fixed manual ghost revive of a loader in unload mode would not work in visually matching direction. ( more )
- Fixed calling LuaEntity::order_deconstruction() on item-request-proxy would corrupt the game state leading to crash. ( more )
- Landfill can be placed over shallow water.
- Fixed that LuaEntity::color wouldn't accept "nil" to reset the color. ( more )
- Fixed that train pathfinder was not counting penalty of opposite train stop at last segment.
- Fixed that train pathfinder was counting penalty of whole starting segment instead of only part in front of locomotive. ( more )
- Fixed that train pathfinder would return single segment path even if there are shorter, multi segment ones. ( more )
- Fixed technology screen not showing modifier tooltips when tooltip descriptions are disabled. ( more )
- Fixed belt tooltips sometimes showing their speed in exponent format. ( more )

### Modding

- Added UnitPrototype::light.
- Removed the "particle" prototype type.
- Added the "optimized-particle" prototype type.
- Added the "burner-generator" prototype type.
- Removed GeneratorPrototype::burner.
- Added the "pass_through_mouse" option to speech bubble styles. This lets mouse interactions fall through to interact with the world behind.
- Added optional "radius_color" property to capsule prototype.
- Removed EntityPrototype::emissions_per_tick, it is replaced by emissions_per_second.
- Removed EnergySourcePrototype::emissions_per_second_per_watt and emissions, they are replaced by emissions_per_minute.
- Removed TilePrototype::ageing, it is replaced by pollution_absorption_per_second.
- Removed ItemPrototype::stackable, primary_place_result_item and can_be_mod_opened, they were replaced by ItemPrototypeFlags "not-stackable", "primary-place-result" and "mod-openable".
- Added "probability" to trigger items and trigger effect items.
- Added "script" trigger effect item. It will call the "on_script_trigger_effect" when triggered.
- Added AttackParameters::rotate_penalty and AttackParameters::health_penalty.
- Added generic support for rendering radius visualisations on entities through radius_visualisation_specification.
- Changed construction robots and logistic robots sprites to be optional.
- Changed the loader prototype type so it has a fixed belt_distance of 0.5.
- Added the prototype type "loader-1x1" that has a fixed belt_distance of 0.
- Changed render layer of belt structures (underground belt, splitter, circuit connector) to object layer. They now have special sorting logic, so they are not rendered over player or cars.
- Horizontal directions of splitter sprites were separated to two sprites (for purposes of the special sorting logic).
- Added AttackParameters::ammo_categories.
- Added optional artillery projectile property "rotatable".
- Scenarios can now contain a description.json file. In the file "order" determines the sorting in the New Game gui; "multiplayer-compatible" determines weather the scenario is shown for multiplayer games.
- Added "multiplayer-compatible" to description.json file of campaigns also.

### Scripting

- Added on_unit_group_finished_gathering and on_build_base_arrived events.
- Added LuaRendering::bring_to_front().
- Changed LuaGameScript::particle_prototypes to reference the optimized-particle type.
- Added LuaGuiElement::scroll_to_item() function.
- Renamed LuaInventory::hasbar(), getbar() and setbar() to supports_bar(), get_bar() and set_bar().
- Added LuaEquipmentPrototype::attack_parameters read.
- Added on_script_trigger_effect event.
- Set lower limit of zoom parameter of LuaGameScript::take_screenshot to be 0.0315 (1 pixel per tile) instead of allowing any value greater than 0.
- Added LuaPlayer::get_infinity_inventory_filter(), set_infinity_inventory_filter() functions.
- Added LuaPlayer::remove_unfiltered_items, infinity_inventory_filters read/write.
- Added LuaSurface::get_entities_with_force().
- Added optional "dealer" parameter to LuaEntity::damage().
- Added "force" filters to the on_built_entity and on_robot_built_entity event filters.
- LuaSurface::min_brightness doesn't have any effect on rendering as brightness of night depends only on color LUT of night.

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
