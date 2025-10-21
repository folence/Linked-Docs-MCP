---
title: Version history/0.12.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.12.0
scraped_at: 2025-10-21 15:47:00
tags: [web, documentation]
---

# Version history/0.12.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.12.0](https://wiki.factorio.com/Version_history/0.12.0)

## 0.12.35

### Bug Fixes

- Fixed the missing title in character logistics window.

## 0.12.34

### Changes

- Polished/Updated the New hope campaign maps
- LuaGameScript::server_save silently does nothing if used on a single player game instead of giving an error.

### Bug Fixes

- Fixed the fuel inventory of the car in the New Hope campaign missions. ( more )
- Fixed crash when exiting from an error during the on_robot_built_entity event. ( more )
- Fixed crash when removing and re*creating forces. ( more )
- Fixed crash after changing the type of a style currently applied to a custom GUI element when loading a save. ( more )
- Fixed crash when calling LuaPlayer::teleport on a disconnected player. ( more )
- Fixed crash after running LuaGameScript::server_save from a mod. ( more )
- Fixed crash when changing the force of an offline player with personal roboport equipment. ( more )
- Fixed crash when trying to merge a force into its self. ( more )
- Fixed underground belt position in blueprint preview. ( more )
- Fixed map transfer speed dropping to zero ( more )
- Fixed logistic description counts with the same counts getting displayed in random order ( more )

## 0.12.33

### Bug Fixes

- Fixed tiles in blueprints. ( more )
- Fixed the duplicated message on load error in multiplayer. ( more )
- Fluid values are rounded to the closest value instead of rounding down when transmitted to circuit network. ( more )
- Fixed that switching brush shape in the map editor didn't update the selected icon highlight. ( more )
- Fixed that label/check box padding was applied twice, moving the rendered text to be out of place. ( more )
- Fixed that map (chart) wasn't properly updated when existing map was edited in the map editor. ( more )
- Fixed crash when the character would die from mining something. ( more )
- Fixed crash when robot can't find charging spot when stationing. ( more )
- Fixed crash in multiplayer that could happen when 2 people are editing the same train schedule. ( more )
- Unified the electric network statistics production/consumption values to be average of the shown timeframe. ( more )
- Solved small numerical text box editing issue. ( more )

### Scripting

- Added LuaStyle::cell_padding/horizontal_spacing/vertical_spacing.

## 0.12.32

### Bug Fixes

- Fixed loading of electric network of pre 0.12 saves.
- Fixed blueprint building. Blueprints are migrated as long as you load the version 0.12.30 or earlier, existing blueprints might be off if you resaved in 0.12.31 already.

### Scripting

- Lua interface to create blueprint now expects the entity positions to be relative to center exactly, so in rail*less blueprints, the position 0.0 translates to center of the tile

when the blueprint is built.

## 0.12.31

### Bug Fixes

- Fixed crash when script errors occurs while loading game while in game. ( more )
- Fixed that attempting to connect to Factorio 0.12.30 with an old client wouldn't produce the correct error message. ( more )
- Fixed that modded roboports with no charging slots were still considering as charging candidates. ( more )
- Fixed that item icon variant for dark background was not used when showing cargo of logistic robots. ( more )
- Fixed crash with "Unblock sendto failed: The operation completed successfully." ( more )
- Human readable error notice when multiplayer connection wasn't successful. ( more )
- Fixed that headless server wouldn't save the map after Control*C. ( more )
- Fixed that attacking biters with a mining tool wouldn't aggro them.
- Improved map download speed when connecting to multiplayer game. ( more )
- Fixed that assigning units to a unit group of a different force would corrupt the save. ( more )
- Fixed crash when using can_insert on the quickbar from the Lua API.
- Fixed tight spot scenario crash. ( more )
- Fixed sort order for recipes in the recipe display.
- Fixed incorrect error message, when setting the number of filters on an inserter ( more ).
- Fixed flame from refineries that are marked for deconstruction was frozen in mid air. ( more )
- Fixed incorrect error message, when setting the number of filters on an inserter. ( more )
- Fixed flame from refineries that are marked for deconstruction was frozen in mid air. ( more )
- Fixed that odd sized blueprints were shifted when rotated. ( more )
- Fixed crash when clearing modded blueprint that doesn't need item to be cleared. ( more )
- Fixed crash in arithmetic combinator when calculating *2147483648/*1. ( more )
- Fixed crash when assigning a character as a passenger of a vehicle when that character already is a passenger of another vehicle. ( more )
- Fixed dealing damage could sometimes corrupt game state and saves. ( more )
- Fixed modded save could not be loaded when a modded inserter gained abilities of smart inserter. ( more )
- Fixed unknown*key message on the third level of first*steps. ( more )
- Fixed cursor*split transfer (right click) not working when putting items into assembling machine stacks over normal stack size. ( more )
- Fixed remote.call() from within the same mod. ( more )
- Fixed inconsistent inserter behaviour when inserting into a splitter from the side. ( more )
- Fixed train trying to turn around on a single rail. ( more )
- Fixed internal electric network problems when mod specified irregular number as supply reach of power pole. ( more )
- Fixed crash when Lua script appears in specific state in multiplayer. ( more )
- Fixed another crash than can happen when train destroys itself. ( more )
- Fixed rare multiplayer crash "server is missing in the crcs". ( more )
- Fixed several GUI problems on high DPI displays ( more )

### Optimizations

- Improved performance when using landmines. ( more )

### Scripting

- LuaUnitGroup::add_member now requires that the new member's force be the same as the UnitGroup's.
- Added LuaUnitGroup::force read*only attribute.

## 0.12.30

### Changes

- Mod checksums are calculated when the game starts and are compared with other peers when joining a multiplayer game. This is to ensure everyone has exactly the same mod in order to prevent desyncs caused by local changes made to mod files.

### Bug Fixes

- Fixed strange outer corner rendering for terrains with the same layer. ( more )
- Fixed Factorio timing out of a multiplayer game when closed by pressing the X button. ( more )
- Building things after quitting a multiplayer game is no longer possible and no longer crashes the game. ( more )
- Fixed memory leak with special signals in the circuit network.
- Fixed crash when killing the player in on_built_entity. ( more )
- Fixed crash when making blueprints of ghosts with some now*invalid circuit connections to other ghosts. ( more )
- Fixed player's shooting target not updating properly when the target's force became friendly ( more )
- Fixed the documentation of CircuitCondition ( more )
- Fixed that the ignore_planner field of Command would expect an integer instead of a Boolean. ( more )
- Starting value of progress bar is now properly set based on the input. ( more )
- Fixed crash when destroying entity with empty corpse string. ( more )
- Fixed mining drills getting stuck when built pointing at rails and then rotated. ( more )
- Fixed remote.call() within the same mod passing invalid data. ( more )
- Fixed the typo in the error "multiplayer.cannot*load*downloaded*map", the cause of the error wasn't displayed because of it. ( more )
- Fixed that the server could get desynced and in a state where he has no one to download from. ( more )
- Fixed that the train tooltip was showing the current station as the next one when in the station. ( more )
- Fixed crash when a Lua function was used as a value in a table in data.raw. ( more )
- Fixed the tooltip of the inventory limit feature to "Limit the inventory part to be filled by machines.", so it is clear, it limits only input, but not output.
- Fixed that cancelling a recipe in the crafting queue would reset the crafting timer unnecessarily. ( more )
- Fixed crash when a force other than player, enemy or neutral was used in autoplace specification. ( more )
- Fixed crash when a network interface is deactivated during multiplayer game. ( more )
- Fixed white bar on top of the screen was sometimes present in fullscreen on OS X. ( more )
- Unified the processing of savegame name in **load*game **start*server and **mp*load*game. It can all be supplied with or without the .zip
- Fixed that collision with point wasn't working properly for curved rail. ( more )

### Modding

- Added LuaEntity::unit_group read*only attribute
- Proper error message when subgroup specified by empty string. ( more )
- Fixed projectiles with negative acceleration would turn around, fly back and break the game. ( more )

## 0.12.29

### Changes

- When the game starts with the base mod disabled, it asks you, if you want to enable it.

### Bug Fixes

- Fixed construction robot crash. ( more )
- Fixed that multiplayer progress bar windows were blocked by currently opened window. ( more )
- Fixed another inconsistency with zero signals in combinators ( more )
- Fixed crash when Steam API initialization failed. ( more )
- Fixed random crashes when mining/closing and autosave happens at the same tick.

## 0.12.28

### Changes

- Added **port to specify which network port the game should use, when hosting with **start*server or **mp*load*game. This overrides the port specified in the config file.

### Bug Fixes

- Explosion sounds are now not deafeningly loud, when multiple things explode at once.
- Fixed LuaForce::clear_chart() would crash game if called while chart was refreshing. ( more )
- Fixed crash when refreshing chart while Direct3D device is lost. ( more )
- Fixed **config option not complaining about nonexistent file. ( more )
- Fixed crash when clicking on electric pole that was still in latency state ( more )
- Fixed freeze of server with more than 255 different players in the savegame.
- Fixed crash when exiting the map editor while holding power armor on the cursor. ( more )
- Fixed map exchange string not using segmentation or water size correctly. ( more )
- Fixed Lua game_view_settings::showentityinfo read/write issues. ( more )
- Fixed fog*of*war does not work correctly in New Hope level 1. ( more )
- Fixed inconsistent Offshore Pump collision when building. ( more )
- Fixed desync reports were not generated. ( more )
- Fixed that non destructible entities get attacked, so biters could get stuck while trying to attack rails under train. ( more )
- Control settings window is now scrollable when it can't fit the window. ( more )
- Fixed Factorio hanging on exit on Linux after copying or pasting ( more ).

## 0.12.27

### Changes

- The area of 400X400 tiles is explored when the game starts.

### Bug Fixes

- Fixed that merging two electric network didn't merge the statistics. ( more )
- Fixed the cyclic/overlapping win/lost sound sample when the game is finished in multiplayer. ( more )
- Fixed that extra pipe covers could be drawn on top of connected pipes. ( more )
- Fixed misaligned turrets in the 4. New hope mission. ( more )
- Fixed some inconsistencies related to zero*signals in circuit networks. ( more )
- Fixed inconsistency between the way inserters and logistic robots picked items from inventories. Logistic robots now prefer items at the end of the inventory and ignore inventory limit. ( more )
- Fixed LuaForce::clear_chart() would crash game. ( more )
- The report of different mods when trying to connect to multiplayer game is now scrollable when needed. ( more )
- Fixed Cargo Wagon Inserter input output inconsistency. ( more )
- Fixed the mod difference reporting when connecting to multiplayer game. ( more )
- Found workaround for issue in Visual C++ math library that was causing crashes on unpatched Windows 7. Service Pack 1 for Windows 7 is no longer required.
- Fixed that placing a rotated blueprint containing a splitter was not possible in some cases ( more ).
- Fixed crash after revive by player port when personal roboport is equipped ( more ).
- Optimized the map bitmap refresh logic 16 times. (the freeze after loading a game or resizing window while playing big saves).
- Fixed that the "you joined a paused game" message would display on all peers, rather than just the peer who just joined ( more ).
- Fixed slow sprite loading on Direct3D ( more ).
- Fixed the documentation of LuaGameScript::show_message_dialog ( more ).
- Fixed the order of parameters of some functions in the documentation ( more ).
- Fixed that the research screen would pre*select Automation even though it was disabled ( more ).
- Fixed rare crash that could happen when assembling machine recipe was reset the same tick as autosave started. ( more )
- Fixed the laser/discharge defense names in the set filter dialog. ( more )
- Better error when wrong bounding box definition is given. ( more )
- Creating message dialog with non existent image doesn't crash the game anymore. ( more )
- Localization errors will no longer stop the game, the result string will just contain the error. ( more )
- Fixed that the stone wall research was disabled in the New hope campaign level 4, so gates weren't researchable. ( more )
- The starting value of text property of textfield is properly set based on the input. ( more )
- Fixed map exchange string problems with mods ( more ).
- Fixed freezes on exit with recent NVidia drivers on Gentoo and Arch Linux ( more )
- Proper notification when quick bar slot can't be selected as there is no place to put the item in the cursor.
- Fixed crash on Linux after running xrandr **off ( more ).
- Fixed Rocket Silo GUI skipping 53%. ( more )
- Another attempt at fixing X11 copy/paste ( more ).
- Better message when the server leaves a multiplayer game ( more ).
- Fixed the bad values of defines.furnace_source, defines.furnace_result and added missing defines.furnace_modules. ( more )
- Fixed that modded saves could get unloadable without mods when they have entities removed in the loading transitions that were in more than one network.
- Fixed that it was possible to have unlimited range with melee weapon after running out of ammo. ( more )
- Fixed that LuaPlayer::remove_item didn't remove from cursor stack when the player was using god controller. This also fixes the bug in the tight spot scenario. ( more )
- Fixed black screen after UAC popped up in main menu ( more )

### Scripting

- Documented extra unit group status return values. ( more )

### Modding

- Added action_range to mining tool prototype (with the default of 1.5).

## 0.12.26

### Bug Fixes

- Fixed the corrupted level 2 of the New hope campaign, that was producing corrupted saves. If you are already playing this level, you have to start it over, I'm sorry for the trouble.
- Fixed the performance issue in the same level after train transport is researched.
- Fixed that the game reported the error to be related to overlay always when it crashed.
- Fixed rare crash related to splitting item in entity that is just about to be destroyed. ( more )
- Sending random packets to Factorio port can still crash the server eventually, the probability will just be lower. ( more )
- Running biters over with a car or tank will make them aggressive in peaceful mode ( more ).

## 0.12.25

### Bug Fixes

- Fixed quickbar selection handling when accepting blueprint with item in cursor. ( more )
- Train stations in the new hope level 2 had neutral force, so they weren't selectable as part of the schedule. ( more )
- Fixed that wall Graphics variations were not randomized when built by robots. ( more )
- Fixed that rail signals were not visible under remnants. They are drawn above now. ( more )
- Fixed that the multiplayer menu would allow one to resume the game as the game was already being disconnected, which would inevitably lead to a crash ( more ).
- Possible fix of rare Lua garbage collector error. Report: more Fix: more
- Fixed Combinator special signals not summing the inputs correctly(again). ( more )
- Fixed green circuit network signals icons in power pole tooltip.
- Fixed that multiplayer*specific options were available in the demo build of Factorio (such as **start*server) ( more ).
- Fixed crash when using screens connected to both AMD and Intel Graphics cards ( more ).
- Fixed very rare chance of a bug when window is closed at the same moment when autosave starts.
- Fixed two sources of rounding errors related to research. ( more )
- Fixed that replaying multiplayer game ended once any player died. ( more )
- Fixed the ungraceful error message when version/mods don't match in multiplayer. ( more )
- Fixed game not restarting when mods were changed ( more ).
- Fixed headless server not working with the Steam version ( more ).
- Fixed that destroying a chain signal in the same tick as it was created crashed the game ( more ).
- Fixed fullscreen issues on multimonitor configurations ( more ).
- Fixed crash when canceling crafting of a recipe who's ingredients have changed in the meantime ( more ).
- Fixed update of stand*alone ZIP package should not require elevated rights on Windows ( more ).
- Fixed specific crash in replay viewing. ( more )
- Fixed game ignoring local changes in config when using Steam Cloud.
- Fixed double key in smart inserter definition, causing it to be slower than fast inserter. ( more )

## 0.12.24

### Changes

- Updated sountrack.

### Bug Fixes

- Fixed corrupted player*data.json message on startup.
- Fixed unnecessary game restart when no mods were changed.
- Fixed crash due to electric network migration during load of some more complex games. ( more )
- Fixed very long belt lines would crash game ( more )

## 0.12.23

### Changes

- Scenario pack was moved to the base game package.

### Bug Fixes

- Any changes in the mods settings will automatically trigger the game to be restarted. ( more )
- The alerts are disabled when player or combat robots get hurt/destroyed. (It was especially annoying in multiplayer).
- Underground belt connection visualization in the "to build preview" wasn't proper. ( more )
- Fixed that picked up item event wasn't fired when picking items from the belt. ( more )
- Fixed that technology list and preview weren't updated when technology was researched in multiplayer. ( more )
- Fixed a crash after merging forces when the destroyed force's labs were researching ( more ).
- Fixed that it looked like it was possible to repair a tree in multiplayer. ( more )
- Fixed that the max health instead of current health was used for crash calculations. ( more )
- Fixed that the game could desync when someone joined while someone else was shooting.
- Fixed that trains were Signaling No Path after update ( more ).
- Fixed that accumulators kept their energy when destroyed and rebuilt by robots. ( more )
- Fixed the occasional 1pixel gap between vertical steam engine and a pipe.
- Fixed beacon would not re*activate when its deconstruction order was canceled.
- Fixed various desynchronizations in multiplayer caused by beacon. ( more )
- Fixed Combinator "each" special signal not summing the inputs correctly ( more )
- Fixed players in multiplayer game would not see progress of new player downloading a map in server/client configuration.
- Fixed crash when checksum error was detected while connecting to multiplayer game. ( more )
- Fixed that the full mod change info for recipes wouldn't display if only the counts were modified on the recipe. ( more )
- Fixed crash when car collided with decorative entity in object layer. ( more )

### Scripting

- Fixed that game.load (inner load) crashed the game in multiplayer. It still causes disconnect though.
- Removed the screen2realposition and real2screenposition methods from Lua API.

### Sound

- Extended the soundtrack.

## 0.12.22

### Bug Fixes

- Fixed that save is not loadable when mod changes type of entity. ( more )
- Fixed that enemy train stops were visible in the rename station GUI. ( more )
- Fixed freeze when there is no place to put character when he exits the vehicle and there is no exit point. ( more )
- Fixed internally inconsistent data state after cancelling deconstruction from script in a certain way. ( more )
- Fixed that map/minimap wasn't updated when settiles was used. ( more )
- Fixed the Graphics inconsistencies related to belt versus inserter drawing. ( more )
- Files starting with dot are ignored when opening locale files to ignore garbage files that mac is leaving around. ( more )
- Fixed the line trigger target specification. ( more )
- Fixed that neutral entities were shown red on the map. (Applies mainly in the campaign)
- Fixed sorting of item groups in the crafting window.

## 0.12.21

### Changes

- Dropped support for OS X 10.6 Snow Leopard.

### Bug Fixes

- Fixed random crash with "Trying to make chunk at unreasonable position" ( more )
- Fixed crash when calling the set_tiles with non existent terrain parameter. ( more )
- Fixed that label could go out of the window in other settings. ( more )
- Fixed that the energy progress bar was missing on personal roboport equipment. ( more )
- Cannon shells will not have plural in the item name to be consistent with other items. more )
- Fixed slight direction bias with the flamethrower ( more ).
- Fixed items in logistic GUI sometimes disappearing or reappearing.( more )
- Fixed copy&paste on Linux, again ( more ).
- Fixed controls settings GUI bad alignment in some situations( more ).
- Fixed the scripting error in the 3rd level of the transport belt madness.
- Fixed various scripting errors in the tight*spot scenario.
- Fixed that enemy train stations were selectable when setting train destination. ( more )
- Fixed crash that could happen when logistic networks are disconnected. ( more )
- Fixed invalid GUI pointing messages (visible namely in the first demo level).
- Fixed that entities could overlap wrongly in blueprint preview. ( more )
- Fixed that roboport sound continued even when it was out of power.
- Fixed that train could crash a gate by accelerating too fast. ( more )
- Fixed construction robots would lose their charging destination when roboport is activated/deactivated ( more )
- Fixed that entities marked for deconstruction would be instead rebuilt if they were destroyed before the actual deconstruction ( more ).
- Fixed undefined behaviour (crashes) when manually (from script) deactivated entity was killed and rebuilt by construction robot. ( more )
- Fixed the scripting bug in the first tutorial level. ( more )

### Scripting

- Fixed the defines.circuitconditionindex.inserter_logistic value (should be 2 not 1).
- Fixed crash when accessing item on the ground inserted into belt. ( more )
- When attacking a player in a tank, the tank will be attacked instead of the player directly ( more )

### Modding

- Better error message when specifying list of filenames instead of one in rotated sprite. ( more )

## 0.12.20

### Bug Fixes

- Fixed crash when attempting to set font color on styles that don't support it. ( more )
- Fixed Lua stack overflow when data.raw got too big ( more ).
- Fixed units sometimes getting stuck at the end of their paths ( more ).
- Fixed clicking on mod GUI in replay would crash the game ( more ).
- Fixed inventory slots with filters did not have hover and click style ( more ).
- Fixed the inconstancy between personal/normal roboport power consumption description. ( more )
- The right part of the research window is also scrollable when it doesn't fit the screen. ( more )
- Fixed that the west/east rotation Graphics of chemical was reversed. ( more )
- Fixed crash when merging a force with disconnected player ( more )
- Fixed Production/Electric network statistics windows resetting position every few seconds. ( more )
- Fixed the preview drawing boxes of some entities.
- Fixed chain signal not preventing crash when a train passed twice through one block ( more ).
- Fixed crash when loading a game saved by the server with only one player that is currently disconnected.

### Modding

- Technology prototypes now have optional integer property "icon_size". Default value for non*base mods is 64 (and 128 for base mod).

## 0.12.19

### Bug Fixes

- Fixed Optics technology icon was corrupted sometimes on OSX. ( more )
- Fixed crash in GroupBehavior ( more ).
- Ingame changelog only shows changes since the last stable release.
- Fixed beam weapon and turret issues ( more ).
- Fixed rocket silo inserters sometimes getting stuck ( more ).
- Fixed ghost trains appearing on minimap.
- Fixed manual crafting bug that could be exploited to get resources ( more ).

## 0.12.18

### Bug Fixes

- Fixed replay of a game created from another replay would crash the game. ( more )
- Fixed that rotating an unpaired underground transport belt wouldn't make its items go back ( more ).
- Fixed construction robots sometimes not picking up an underground transport belt whilst deconstructing it if it contains items ( more ).
- Fixed all personal construction robots could get stuck waiting for trees to be gathered ( more ).
- Fixed crash caused by allowing mods to order units to attack a disconnected player's character ( more ).
- Fixed rare crash with construction robot. ( more )
- Fixed the info about the energy consumption of personal roboport, to show the maximum consumption as other machines.
- Inventories with limit (chests) can get scroll bars when they are too big as well. ( more )
- Fixed, that the train could get stuck when it has to accelerate to get to station that is very close. ( more )
- Fixed map exchange strings not being accepted when the quote sequence contains spaces ( more )
- Fixed locomotive not centered on rails. ( more )
- Fixed train lights were further away than they should be. ( more )
- Fixed spitters freezing in some cases ( more ).
- Fixed crash when trying to load replay from save that doesn't contain level*init.dat ( more ).
- Fixed incorrect default request amounts for shield and battery equipment due to typo ( more ).
- Fixed save with modded roboport could become unloadable without the mod ( more ).
- Fixed beam animations for modded weapons ( more ).
- Fixed that reconnecting train in special case lead to corruption of the rail state. ( more )

### Changes

- Improved formatting of map exchange string.

### Scripting

- Reading or writing LuaPlayer::character will now fail if the LuaPlayer isn't connected (see LuaPlayer::connected).
- Lua API documentation is included in release packages (directory doc*html)

## 0.12.17

### Graphics

- New technology Icons!
- New item group icons.
- Updated the icons of rocket silo, beacon, sulfur, armors, stone brick and radar.

### Bug Fixes

- Fixed that assembling machines/furnaces could get stuck after changing mod configuration that affects their recipe. ( more )
- Fixed that the window title was "Allegro" on mac os. ( more )
- Fixed crash on exit with Steam overlay. ( more )
- Fixed displaying of update unavailable message with disabled experimental updates.
- Added workaround for problem with AMD drivers that could cause missing or corrupted textures on some systems. ( more )
- Fixed that making a blueprint of a ghost was not saving circuit connections.
- Fixed occasional crash during update after UAC dialog pops*up. ( more )
- Fixed that the value of the checkbox in tips and tricks wasn't set up properly.( more )
- Fixed that rocket silo electric energy drain was applied twice. ( more )
- Fixed chain signals getting stuck on red ( more )
- Fixed crash while rotating locomotives that crashed into something ( more )
- Fixed an issue causing desync. ( more )
- Fixed crash when loading save with Lua tables that are nested more than expected. ( more )

### Scripting

- Added global log method that can be used to debug script problems.
- Added LuaFluidPrototype::localised_name property.
- Fixed that LuaInventory::insert didn't follow the slot restrictions. ( more )

## 0.12.16

### Bug Fixes

- Fixed chain signal state propagation ( more ).
- Added "markers" that will be recognized by nVidia and AMD drivers as hints to run Factorio on high performance GPU if switchable Graphics technology is present. ( more )
- Improved burner inserter's fuel searching logic; it will now search both transport belt lines for fuel ( more ).
- Fixed crash when building locomotive on the junction. ( more )
- Fixed crash when the first lab is built by construction robots. ( more )
- Fixed crash related to train stopping for auto control. ( more )
- Removed the limit of 800 pixels height of the recipe GUI. ( more )
- Fixed problems with too big character windows with too big inventory (modded) on screens that can't hold it, by making it scrollable.
- Fixed problem with night vision effect on some PC configurations. ( more )

## 0.12.15

### Bug Fixes

- Fixed that it wasn't possible to execute UI actions while the game was stopped (research, tips and tricks etc.)
- Fix of fix of loading of game containing Lua objects.

## 0.12.14

### Graphics

- Added new smoke Graphics

### Bug Fixes

- Fixed loading of game containing duplicate Lua tables. ( more )
- Fixed flickering light intensity at the edge of the screen when moving.
- Fixed crash when pasting from empty clipboard into console on OS X.
- Fixed crash when reviving train stop that was connected to rail while destroyed while the rail no longer exists.
- Some UI actions made while the game was being saved were actually not executed although it looked like it. ( more )

## 0.12.13

### Bug Fixes

- Fixed that blueprint gates were colliding with ghost gates with same type and direction. ( more )
- Fixed that LuaEntity::clear_request_slot and set_request_slot wouldn't update the logistics GUI if it happened to be opened at the same time. This time it's fixed for logistic chests as well. ( more )
- Fixed crash when trying to open car GUIs in the map editor. ( more )
- Fixed the desync issues related to converting floating point numbers to string in Lua. ( more ) Note: until 0.13 other special values like nan, inf etc. are not solved properly, so they shouldn't be used.
- Fixed crash when loading a savegame with self recursive table elements. ( more )
- Fixed that furnaces deactivated improperly when switching products. ( more )
- Fixed crashes on Linux (when download failed, after Lua error, ...)

## 0.12.12

### Bug Fixes

- Fixed another solar panel counting error. ( more )
- Fixed that locale values in zip packages weren't loaded. ( more )
- Fixed pushing of compound localized strings into Lua. ( more )
- Tweaked train path finding values for trains waiting on signals ( more ).

### Scripting

- game.get_localised_entity_name is replaced by LuaEntityPrototype::localised_name read property. The same for technology and item.

## 0.12.11

### Features

- Added **no*auto*pause: When running as a server, **no*auto*pause will prevent stopping the game when no players are connected.

### Optimizations

- Optimised the particle performance. Helps during heavy fights.

### Changes

- Showing the log file location when the game crashes, so it is easier to find when reporting the bug.
- The "graphics.force*opengl" option default value is true when AMD Graphics card is present.

### Bug Fixes

- Fixed that multiple electric networks connected to a solar panel could be exploited to generate more energy. ( more ) The energy of the solar panel is now fractioned between all the networks it is connected to.
- Fixed character entities disconnected from players not working correctly when in vehicles. ( more )
- Fixed small*pump and offshore*pump not saving/restoring circuit conditions in LuaItemStack::get_blueprint_entities/set_blueprint_entities. ( more )
- Fixed threading issue when loading games. ( more )
- Fixed OS X Finder argument crashing the game on startup ( more ).
- Burner inserter now grabs fuel for itself even if the target doesn't need it.
- Fixed active sound playing on machines without power ( more ).
- Fixed empty unit groups crashing the game ( more ).
- Fixed crash when building locomotives in latency hiding.
- Fixed cannot load save with modded rails when a rail mod is disabled (will work only on 0.12.11+ saves) ( more ).
- Fixed crash when setting filters in the tank/car while riding in them. ( more )
- Fixed crash when migrating/removing entities marked for deconstruction. ( more )
- Removed one possible logical deadlock in the tutorial. ( more )
- Fixed that remove_item didn't remove from player ammo, gun, tool and armor slots. ( more )

### Scripting

- Changed LuaSurface::set_multi_command signature. Now the function takes a table with following keys: command(required), unit_count(required), force(optional), unit_search_distance(optional) This solves issue with not finding any enemies to attack: more
- Removed game.on_save function. There should be no need for it and it was causing too many problems.
- Lua on_load function is not called when saving the game anymore. It is called only on actual load now.
- Lua API calls on_load , on_init , on_configuration_changed , on_event and generate_event_name have been moved to a new namespace called script (so from now use script.on_load (...)). This will break many mods! The callback registered in on_load function doesn't have access to the game API. This is to avoid common desyncs. The on_init and on_configuration_changed still retain the access to the game API.
- on_configuration_changed is fired when the map version changes, a mod version changes, a mod is added, or a mod is removed and passes "data": Pushes old_version="x.x.x", new_version="x.x.x" when loading map versions other than the current version When a mod version is changed it appears as a table of mod Changes {["Mod name"] = {old_version="x.x.x", new_version="x.x.x"}, ...} When a mod is added it appears as: ["Mod name"] = {old_version=nil, new_version="x.x.x"} When a mod is removed it appears as: ["Mod name"] = {old_version="x.x.x", new_version=nil}
- Changed LuaGameScript::makefile to LuaGameScript:: write_file and added an optional third parameter bool to append.

### Modding

- Replaced entity type "rail" with types "straight*rail" and "curved*rail". Property "bending_type" is optional for rail entities, but is still mandatory for rail remnants.

## 0.12.10

### Changes

- Script created beam entities will now destroy themselves when the source or target entity becomes invalid.

### Bug Fixes

- Fixed crash when research completed in the same tick as inserting equipment into power armor. ( more )
- Fixed hand not refilling with repair packs after a repair pack was consumed ( more ).
- Fixed small pump not saving its condition in a blueprint ( more ).
- Fixed rocket silo GUI bug. ( more )
- Fixed "failed to create display" error on systems with multiple Graphics devices ( more ).
- Fixed the blinking problem in the multiplayer. ( more )
- Fixed units disappearing when they shouldn't ( more ).

## 0.12.9

### Features

- Added reset button to the control settings dialog. It will set the controls back to the default.

### Graphics

- Destroyer electric beams now use soft additive blend mode.

### Changes

- Added **load*game: Will automatically load a save after initializing Factorio and go straight to the game, skipping main menu.
- Moved MP / autosave information dialogues to the top half (better visibility of what is happening in the game) and added screen fading.
- Implemented time*to*live for deconstruction order, if an order is not assigned for 1 hour, it is removed.
- game.print_entity_statistics() has been moved to player.print_entity_statistics(). ( more )
- Updated the tips and tricks pictures. (+added copy paste)
- Smoothed map scrolling speed on different zoom levels.
- Added Resume button to multiplayer game menu.

### Optimizations

- Dramatic speedup of loading packages (mods) from the zip files. It is recommended to used only zipped mods from now on, as on non ssd discs, it might even speed up the startup time.
- Added FPS limiter to main menu screen.

### Bug Fixes

- Fixed the shotgun shooting. ( more )
- Fixed the game could get stuck during start on systems with multiple display adapters.
- Fixed train GUI closing immediately after opening in multiplayer when the player is riding on the train.
- Fixed train GUI not containing the wait time slider until a station was explicitly selected ( more ).
- Fixed production GUI jumping to undesirable places when resized ( more ).
- Construction robots will be transferred to appropriate network when a logistic network splits ( more ).
- Fixed crash when auto*re*filling ammo in tanks/cars ( more ).
- Fixed wait slider in train GUI editing after deleting a station ( more ).
- Fixed that negative emissions of power source (air filtering mod) could result into negative evolution factor.
- Fixed the game could hang when writing a message to log ( more ).
- Fixed next save not being selected properly after clicking the Delete Save button ( more ).
- Fixed module icons not showing in alt*view on rocket silos ( more ).
- Fixed mining progress bar staying on screen when not mining in certain situations ( more ).
- Fixed crash when loading 0.10 or older saves ( more ).
- Fixed crash when loading pre*12.7 scenarios with redefined spawn location ( more ).
- Fixed trains sometimes stopping on signals they reserved.
- Fixed personal roboport taking forever to deconstruct when there are a lot of deconstruction orders.
- Fixed a crash where the Lua stack would overflow and corrupt Factorio memory ( more ).
- Fixed crash when using player.inventory.clear(). ( more )
- Fixed that **create wouldn't create a control.Lua, causing the victory dialog not being shown after launching the rocket, or creating new players without giving them the initial inventory ( more ).
- Player <> entity transfer now ignores modules only when the entity has module inventory.
- Fixed beacons affected steel furnaces ( more ).
- Fixed car starting sound playing when opening it's GUI.
- Fixed crash when fast replacing a beacon (modded game only) ( more ).
- Fixed train station names appearing on minimap with certain GUI scale settings.
- Fixed crash when zooming in the map all the way with the keyboard ( more ).
- Fixed that LuaEntity::clear_request_slot and set_request_slot wouldn't update the logistics GUI if it happened to be opened at the same time ( more ).
- Fixed width of some progress bars did not respect UI scale configuration ( more ).

### Modding

- Fixed projectiles with direction_only = false didn't respect direction_deviation configuration.
- Fixed entity dying explosion with "rotated = true" caused crash ( more ).

### Scripting

- Added LuaEntity::get_connected_rail. It takes a table with rail_direction (0 front, 1 back) and rail_connection_direction (0 left, 1 straight, 2 right) and returns a new rail (or nil) following that specification from the given rail entity.
- LuaTrain::front_rail, LuaTrain::back_rail, LuaTrain::rail_direction_from_front_rail and LuaTrain::rail_direction_from_back_rail None of the methods takes any parameters.
- LuaEntity::get_output_inventory now returns nil when the inventory doesn't exist (doesn't raise an exception as before).

## 0.12.8

### Graphics

- New Graphics of the steel furnaces.

### Bug Fixes

- Fixed that it was possible to spawn inside an entity in multiplayer.
- Fixed that the amount of slots shown in the right panel didn't depend on its with. (Which is indirectly dependent on resolution and UI scale.) ( more )
- Fixed desync issue related to mod event registration and saving/loading.
- Fixed enemy units getting stuck on transport belts ( more ).
- Fixed a crash caused by icon = "" in a prototype definition ( more ).
- Fixed a crash related to assembling machine not being re*setup when recipe changes due to mod changes. ( more )
- Fixed LuaItemStack::set_blueprint_entities(nil) erasing tiles in blueprints.
- Fixed crash when fast*transferring ammo while in vehicles. ( more )
- Fixed trains stopping on green signals ( more ).
- Fixed crash when changing the force of a player who is currently not connected.
- Fixed another problem with the missing maximise button after fullscreen. ( more )
- Fixed desync problem related to duplicate order string in inventory groups leading to non*deterministic inventory sorting. ( more )
- Fixed putting a blueprint on transport belt could corrupt game save ( more ).
- Fixed CTD that could happen when removing focused widget (rarely). ( more )
- Fixed that the tank tower rotation center wasn't aligned with the visible rotation center. ( more )
- Fixed wrong coordination of the tank cannon direction and shooting direction when aiming on near the tank. ( more )

### Scripting

- Beams can now be created via create_entity. You need to specify source/source_position and target/target_position, you can also specify duration (ticks), max_length and source_offset (vector). Position of the created entity does not matter.
- Added LuaItemStack::set_blueprint_tiles/get_blueprint_tiles * the counterpart to get/set_blueprint_entities.
- LuaEntity::insert/remove_item and LuaInventory::insert/remove now return counts of inserted/removed items.
- Added LuaTrain::insert, remove_item, get_contents, clear_items_inside, get_item_count methods which interact on the cargo wagons of the train.
- Added LuaItemStack::cost_to_build * the cost in items to build a given blueprint.

### Modding

- The minimal energy_required for a recipe is 0.001 to avoid wrong behavior with values close to 0.

## 0.12.7

### Changes

- Added 5th level of character logistic slots research.
- New command line options for the headless server: **disallow*commands and **peer*to*peer
- Entries in the mod list GUI are highlighted in red only when enabled and invalid at the same time.
- Added natural case*insensitive string ordering for the mod list GUI.
- There is now only one spawn position per each force and per each surface. This means that only one spawn position can be defined in the map editor as it currently supports only the default surface and the "player" force.
- Added force*opengl value in config (under Graphics). When set to true, it forces to use opengl on windows instead of D3D.
- Map scrolling speed now changes with zoom level.

### Bug Fixes

- Inserters take items from correct line when the input transport belt is rotated ( more ).
- Solved the "A blocking operation was interrupted by a call to WSACancelBlockingCall" error (hopefully as we can't reproduce it). ( more )
- Scrolling using the scroll wheel now works much more predictably (not only when the cursor is over scroll bar or the root scrollable element). ( more )
- Fixed crash when a script attempted to access a previously*destroyed GUI element ( more ).
- Fixed that the Graphics.max*texture*size property in the config was removed after Factorio restart.
- Fixed the tree bounding boxes.
- Another attempt to fix map transfer problems.
- Fixed disappearing fonts. ( more )
- Fixed destroying a rail under a train would corrupt future save files. Rail can't be destroyed or die if a train is on it. ( more )
- Robots can charge from closer roboport when heading to distant roboport for stationing (2.0) ( more )
- Fixed problems with IPv6 on linux when only IPv4 is enabled in kernel. ( more )
- Fixed crash when loading save with modded personal roboport in vanilla game.
- Fixed opening power armour inside a chest with latency hiding enabled crashing the game ( more ).
- Fixed that distractor robots slowly drifted east.
- Fixed that that the high overload factor in assembling machines (the effect, that they allow to store more items when they are working very fast) wasn't taken in to consideration when calculating the slot limit. ( more )
- Fixed desync issue related to inventory sorting and blueprints. ( more )
- Fixed that amount_max in recipe specification actually worked as amount_max *1. ( more )
- Fixed that mining tiles did actually create mining particles+sound on the lastly mined entity.
- Fixed that the maximize button was disabled when Full screen was turned of in the settings. ( more )
- Fixed accessing the game menu was not possible when some other player paused the game in MP ( more ).
- Fixed a graphical bug where the boiler would still glow after running out of water ( more ).
- Fixed mergable items (repair packs, bullet magazines, ...) could sometimes confuse personal robots.
- Fixed the inserter sound related crashes. ( more )
- Blind fix of some of the transport belt gap issues. ( more )

### Scripting

- The LuaEntity::logistic_network now returns also primary logistic network of other entities than roboport. (Inserter, Character, logistic chests)
- Placing stone or concrete floors will now remove most of the bushes ( more ).
- Fixed crash on exit when config file can't be written ( more ).
- Fixed player changing direction when the game is paused ( more ).
- LuaEntity::belt_to_ground_type also works on a ghost.
- Increased precision of floating point in save files to prevent some desyncs in multiplayer ( more ).
- Added LuaEntity::revive() * usable on ghost entities to revive them back to normal.
- Fixed that that the resource amount while creating the entity accepted non*positive values. ( more )
- Added LuaForce::set_spawn_position(surface, position) and LuaForce::get_spawn_position(surface)
- Fixed that the event queue was never cleared when scripting error occurs while processing it. This lead to processing the same event every update once the game was stopped when error happened. ( more )
- Fixed inserting or removing items from player's inventory through LuaInventory object didn't update logistic supply properly. ( more )

## 0.12.6

### Changes

- Smaller breaks between ambient music tracks, some volume tweaks and moved a few tracks to the interlude category.
- Ambient settings can be controlled from the config file. By using: sound.ambient_music_pause_mean_seconds (default 60), sound.ambient_music_pause_variance_seconds (default 30) and ambient_music_mode: possible values are main*tracks*only, interleave*main*tracks*with*interludes, randomize*all (default is interleave)

### Bug Fixes

- Fixed setting circuit conditions desyncing/crashing multiplayer games. ( more )
- Fixed reading logistic_network from entities that didn't have logistic networks returning unknown results. ( more )
- Fixed that opening the Save Game menu after the last used saved was deleted would terminate Factorio ( more ).
- Fixed the behaviour of item on ground, that was created using script to contain many items. The inserter takes only the amount it can hold, and the stack stays there if it contains more ( more )
- Fixed destroying rail with gate would corrupt save file. ( more )
- Fixed two different problems related to loading map with different mod set. ( more )
- Fixed game freeze after desync happens for multiple players in server client mode.
- Fixed bug with ambient occasionally taking too long.
- The rotation of cargo wagon player is riding doesn't affect the riding direction. (While it still affects it while being in locomotive). ( more )

### Changes

- Smaller breaks between ambient music tracks, some volume tweaks and moved a few tracks to the interlude category.
- Ambient settings can be controlled from the config file. By using: sound.ambient_music_pause_mean_seconds (default 30), sound.ambient_music_pause_variance_seconds (default 30) and ambient_music_mode: possible values are main*tracks*only, interleave*main*tracks*with*interludes, randomize*all (default is interleave)
- Fixed a performance problem in the pathfinder that would cause complete lack of enemy attacks in certain situations ( more ).

### Scripting

- Added LuaItemPrototype::module_effects read.
- LuaSurface::spill_item_stack will now additionally accept LuaItemStack objects as the stack to drop.

### Modding

- Lab's researching speed is now independent of it's power consumption and can be changed using "researching_speed". ( more )

## 0.12.5

### Features

- The armor window opening is included in the latency hiding.
- Multiplayer broadcast (heartbeats) is done via a single message when not using peer2peer.
- Added some new ambient sounds (wind, slow tunes).
- Combinators blinking emit light.

### Changes

- Pasting newlines and tabs into Factorio console now no longer strips them. Instead they are replaced by spaces.
- Continuous zoom is much slower in the chart mode. Only applicable when the zoom is setup to keys rather then scroll wheel. ( more )
- Changed open/save dialog and the rail station list to use case insensitive natural ordering.
- Inserter stack size bonus is added to the assembling machine stack limit, to avoid inserters being stuck in certain situations. ( more )
- Robots can charge from closer roboport when heading to distant roboport for stationing. ( more )

### Optimizations

- Further Optimizations in size of the Multiplayer heartbeat (message sent every tick).

### Bug Fixes

- Fixed that editing tiles in the map editor on the edge of currently generated map could result in a corrupted scenario.
- Fixed potential stability problems when fast*replacing roboports (mod related).
- Fixed non*deterministic armor sorting which could cause desyncs. ( more )
- Fixed crash related to changing recipe prototypes used by entities in inactive chunks. ( more )
- Fixed circuit network contents sometimes being reset when removing connections or merging networks. ( more )
- Fixed crash when Ctrl*clicking items to the player's main inventory when no character is attached ( more ).
- LatencyState is suspended when player is killed (and waiting for respawn) in the Multiplayer.
- Fixed crash after finishing the game in MP with headless server ( more ).
- Fixed crash related to displaying alerts from other surfaces ( more ).
- Continuous zoom speed is independent of the game speed ( more ).
- Fixed that it was possible to stack blueprints by inserting them into an assembling machine ( more ).
- Fixed enemy expansion chunks not being updated properly ( more ).
- Fixed trains changing state unnecessarily when reserving a signal when arriving to a station ( more ).
- Fixed smart inserter not waking up when its filter was set from a script ( more ).
- Fixed signal placement problems with diagonal rails ( more more ).
- Fixed last wagon of long train did not wake up inserter at its end ( more ).
- Additional fix of the puff smoke appearing on different surface. ( more )
- Fixed portions of previous surface visible after respawn when the player died on a different surface than is their spawn surface ( more ).
- Fixed internal roboport connection inconsistency that could happen when migrating from 0.11 version. ( more )
- Fixed train still having path while being in NO_SCHEDULE state ( more ).
- Fixed disconnecting roboport from roboport network caused all construction robots in the network to cancel orders ( more ).
- Fixed that the game could crash when some mod tried to modify the GUI in the on_save event. The game now disallows these kind of modifications while processing the on_save event. ( more )
- Fixed crash when changing recipes (mod related). ( more )
- Fixed solar energy source was not included in electric demand satisfaction. ( more )
- Finishing research should no longer interrupt GUI when "Singleplayer game stops when research is completed" is turned off ( more ).
- Fixed Underground Belts Graphics not tiling correctly.
- Fixed recipes not displaying in the correct sort order when adding and removing mods from an existing game.
- Fixed pathfinding penalty for trains with 1 stop in their schedule ( more ).
- Fixed electric furnace still glowing with no power. ( more )
- Fix of loading a map that contains mod with tiles, while the mod is no longer present.
- Fixed that it was not possible to use fast*replace when player was very close to the building. ( more )
- Right side selection info GUI has fixed size. Description and text properties properly wrap. ( more )

### Scripting

- LuaForce::chart now creates a new chart if one doesn't exist yet, instead of erroring out ( more ).
- Items now have a new optional attribute "stackable": When set to false, assembling machines won't be allowed to create stacks of the item. Currently only used with blueprints, to fix the "crafting machine stacks blueprints" bug.
- Added LuaEntity::rocket_parts read/write, usable on Rocket Silo.
- Added LuaEntity::launch_rocket(), usable on Rocket Silo.
- Added LuaLogisticNetwork * an interface to logistic networks.
- Added LuaLogisticCell * an interface to logistic cells (roboport/player logistic information).
- Added LuaTransportLine::get_contents().
- Added LuaPlayer::connected read * true/false if the player is currently connected to the game.
- Added LuaForce::kill_counts read, set_kill_count/get_kill_count methods to access and manipulate kill counts per force.
- Constant combinators now export their wire connections in LuaItemStack::get_blueprint_entities. ( more )
- Added Prototype::order/group/subgroup read + LuaTechnology::order read.
- Added LuaRecipe::force read * the force that owns recipe reference.
- Added LuaEntity::chain_signal_state read * the chain state of chain signals.
- Added LuaEntity::speed read/write * the speed of a car/tank.

## 0.12.4

### Features

- Simple mechanism for multiplayer relaying via the server.

### Changes

- Renamed "multisampling" to "multisampling*level" in the config file. This will reset everyone's multisampling setting to 0.
- Construction robots take things primary from the main inventory, then quickbar.
- Reverted the order of inserter slot selection. ( more )
- Added Alt*mode (showing entity info) to the latency hiding.
- Trains now try to recalculate their path, when waiting over 5 seconds on a signal (only if needed). The recalculation is forced when waiting over 30 seconds.
- Construction robots will check if their target is still in the network area when they return to personal roboport for charging.( more )
- Tweaked the stuck resolve mechanism. This should solve the more

### Bug Fixes

- Less annoying glitches when running and shooting in multiplayer with latency hiding.
- Fixed that the loot wasn't always properly put on transport belts. ( more )
- Fixed force building specific blueprints. ( more )
- Fixed setting player character to other player's character crashing the game. ( more )
- Fixed failed **apply*update returning success even when it failed ( more ).
- Fixed the latency hiding inconsistency in the entity transfer action, entity rotation, blueprint selection deconstruction selection and others.( more )
- Fixed ghost inserter arrows being displayed incorrectly ( more ).
- Zooming works comfortably also when mapped on buttons, as holding the button continuously zooms in/out instead of doing just one small zoom step.( more )
- Proper direction filtering (8 way versus 4 way) when building ghosts from script. The direction is now dependent on the ghost inner entity limitation.( more )
- Fixed that the new lamp entity was off*center. ( more )
- Fixed behemoth biter resistance specification. ( more )
- Fixed that the game could crash when connecting train in a junction. ( more )
- Fixed construction robots could cause desync when they used up all repair packs.
- Rocket silo behaves correctly when out of electricity. ( more )
- Fixed tank cannon shell tooltips. ( more )
- Fixed error message on campaign mission 4 ( more )
- Fixed crash when exiting the game in the map editor with the menu open.
- Fixed trains not alarming inserters when switched to manual mode when already stopped. ( more )
- Fixed connection failures on windows without IPv6 enabled ( more )
- Solved stuttering while building when max_expansion_distance was set to high values by a mod. ( more )
- Fixed robots getting stuck when trying to store damaged items. ( more )
- Fixed that lot of output in the output console could slow down the game a lot. ( more )
- Fixed that damage to be taken wasn't cleared when entity was rebuild by robots, so the entity was partially unkillable.
- Fixed that train stop rebuilt by robots wasn't working properly. ( more )
- Fixed crashes with invalid locale on Linux
- Fixed that Save scenario + Save as wasn't translatable. ( more )
- Changed the default style of custom text field to have not only minimal_width but also maximal_width 150. So all of the text-fields will not get larger on load, until the maximal_width is specified to be larger. ( more )
- Fixed that replay didn't work on the campaign levels. ( more )
- Fixed determinism issue in logistic network causing desync. ( more )
- Two trains never collide as long as they don't share a train block, this solves some problematic situations, where the end of the train collided with different track a little, while it was technically on different block already. ( more )
- Fixed copy&pasting filters between cars ( more ).
- Fixed crash in replay of game which was save and then loaded ( more )
- Fixed problems with RTL scripts ... again ( more )
- Fixed the crash when radar was created on a surface that didn't have chart initialized on the surface for the specific force.( more )

### Scripting

- Fixed that inserter didn't return drop_position.
- Fixed crash when calling set_command on empty unit groups ( more ).

## 0.12.3

### Features

- Circuit wire building and repairing is incorporated in the latency hiding logic.

### Changes

- Cars of your own force always render their tags on the map.
- Multisampling not officially supported from now on.

```
It can still be manually specified in the config, but not in the graphic settings GUI.
 The main reason is the trouble with tiling which doesn't really have a simple fix.
```

- Changed the console spam*prevention mechanic to check all messages for the last second instead of just the last entered one.

### Bug Fixes

- Fixed the Invalid Transport Line Index error. ( more )
- Fixed signal selection window not displaying correctly when "Use item groups" is disabled. ( more )
- Fixed broken accumulator input flow limitation. ( more )
- Fixed trains viewing other trains with schedules with only 1 valid stop as not stopped ( more ).
- Fixed trains sometimes not recalculating their path when a new path opens up.
- Fixed shotgun damaging objects behind player. ( more )
- Fixed trains not being counted properly, when entering a block multiple times without leaving ( more ).
- Fixed copy&paste on Linux ( more )
- Fixed desync when trying to open an enemy structure ( more )
- Fixed changing forces of damaged entities could corrupt subsequent game saves. ( more )
- Fixed crash when clicking inventory item while dragging wire in latency hiding mode. ( more )
- Fixed that the smoke effect when building something always showed on the viewer surface. ( more )
- Fixed crash related to alerts on multiple surfaces. ( more )
- Fixed copy*paste for cars/tanks. ( more )
- Fixed single locomotives not rendering on the chart view.
- Fixed the non standard number format of big numbers in the research tooltip GUI. ( more )
- Fixed crash after finishing the game in multiplayer ( more ).
- Fixed construction robots got stuck when trying to take items from logistic trash slots ( more ).
- Fixed productivity bonus being lost with very high productivity values ( more )
- Fixed that script errors didn't stop the game, and it was possible to possible the game by pressing SEC.
- Fixed that non*default mods were not loaded during the first start of Factorio after mod*list.json was deleted.
- Fixed that inserter was always preferring the Left side when picking up from the underground belt. ( more )
- Fixed robots from personal roboport would keep transferring items from chest which was ordered for deconstruction

```
even after the chest gets out of the personal robot range. (more)
```

### Scripting

- Implemented remove_item() for all entities that have items.
- Added LuaEntityPrototype::autoplace_specification read.

## 0.12.2

### Features

- Enabled swapping held blueprints with other blueprints directly.
- Force*building blueprints will mark any colliding trees for deconstruction.
- Added filters to car and tank main inventories.

### Changes

- Inserters will never take more than the maximum stack size of the item.
- Way more relaxed timeouts for dropping peers during map uploads ( more ).

### Bug Fixes

- Factorio with RTL languages no longer crashes on startup because of reversed font path.
- Fixed crash when removing mods that added/changed recipes ( more ).
- Disabled repairing of combat robots ( more ).
- **start*server and **create now accept filenames with dots in them ( more ).
- Combinators will no longer turn off when no wires are connected ( more ).
- Shift + click will move items into logistic trash slots only in character GUI ( more ).
- Fixed circuit network crash when removing mods that changed the inserter ( more ).
- Fixed crashes related to migrating entities ( more ).
- Inserters and logistic robots no longer extract from enemy chests ( more ).
- Fixed health bar display on large entities like the rocket silo ( more )
- Fixed crash when loading some maps that were migrated from early*0.11 versions ( more ).
- Inserters now correctly pick up items from splitters ( more , more more]).
- Picking up items from curved belts picks up from the correct line ( more ).
- Fixed that electric pole/roboport radius visualization were off*centered in low Graphics mode.
- Fixed that turrets had too small remnants.
- Fixed bug when removing roboports during load migration ( more ).
- Empty autoplace tag in mod entity specification doesn't place entity at all ( more ).
- Fixed blueprints or armors getting erased when inserters move them.

```
Fixed "Attempt to clone non empty blueprint" and "Attempt to clone armor with equipment grid" when inserters move them.
 (more)
```

- Character doesn't get moved by neighbour transport belt after game load.
- Crafting entity tooltips show contents in order and now also show fluids ( more )
- Fixed missing belt activation in specific situation ( more )
- Fixed modded spitters could spit very far from their location when trying to destroy a tree ( more ).
- Map editor wire editing works again.
- Fixed beacons stopping working when the modules where removed and re*inserted ( more ).
- Fixed power armor GUI tooltips not showing sometimes.
- Fixed v*sync causing framerate to go bellow 60 when Windows Aero theme is enabled ( more ).
- Flame*thrower sounds volume is dependent on the distance of the player now. ( more )
- Tank can turn around without moving forward again. ( more )
- Fixed tile building/removal sometimes removing buildings or killing the player.
- Fixed tile building/removal sometimes creating or removing water.
- Fixed tile removal ignoring changes made in map editor.
- Fixed crashes when mining path tiles while map is generated.

### Scripting

- get_surface never returns invalid surface.

## 0.12.1

### Features

- Burner inserters start with enough energy to pick up 1 item and fuel them selfs.

### Changes

- Train station names use natural string comparing (station "Iron 10" comes after "Iron 9", not after "Iron 1").
- New command*line parameter: **latency*ms. Allows to set server latency in milliseconds rather than ticks
- You can copy paste circuit network conditions between Inserter, Lamp, Pump and Offshore Pump.
- The delete button in Load Game or Save Game dialogues now asks for confirmation before deleting
- Locomotive on schedule can't be rotated while moving anymore.
- Changed fast inventory transfer from the main player inventory so ctrl+clicking empty slots doesn't move items to the logistic trash slots.
- Changed Assembling machine's auto*insertion behaviour when using speed module effects. Faster speed with fast recipes will insert more items sooner.

### Bug Fixes

- Very rough support for RTL languages, the texts are no longer rendered backwards (but the GUI still is and multiline text will cause problems).
- Fixed Rocket Silo rocket inventory tool tip sticking around when it shouldn't ( more ).
- Fixed furnaces rendering light when inactive ( more ).
- Fixed transport belt to ground in blueprints when rotating crashing the game ( more ).
- Fixed LuaSurface::can_place_entity checks for rails ( more ).
- Fixed inserters putting items only on left line of underground belts. ( more )
- Fixed ghost building concrete/stone not updating charting ( more ).
- Fixed ghost building concrete/stone distance being restricted ( more ).
- Fixed crash when leaving vehicle while on a transport belt entity ( more ).
- Fixed charging from primary and secondary energy sources (aka shield insta charge) ( more , more ).
- Fixed crash when trying to set filter on vehicle ammo inventories ( more ).
- Fixed mining concrete/tiles sometimes making water where it shouldn't be ( more ).
- Fixed character*logistic*trash*slots*2 technology prerequisite ( more ).
- Fixed crash when calling game.player.surface.set_multi_command ( more )
- Fixed electric wire rendering on low Graphics quality settings ( more ).
- Fixed unable to load 0.11 savegames with active combat robots ( more ).
- Fixed robots building paths over existing paths not mining the existing paths first ( more ).
- Fixed personal robots would sometimes follow player instead of stationing when they use up all material for terrain building.
- Fixed splitters/transport belts still running when marked for deconstruction ( more ).
- Fixed death after launching the rocket not ending the game in single player ( more ).
- Fixed crash when disconnecting character from player while crafting ( more ).
- Fixed inserters sometimes not loading Rocket Silo after launch ( more ).
- Fixed circuit network sometimes showing items with no number.
- Fixed crash when the game attempted to play a sound in headless mode ( more )
- Fixed incorrect gun turret health ( more )
- Copy pasting now works for Small pumps and Offshore Pumps.
- Fixed crash when loading single*player save in multiplayer without "Allow commands" checked ( more ).
- Fixed not being able to set the UI scale back to normal after accidentally setting it to 200% ( more ).
- Fixed locomotive lights and vehicle indicators being rendered across different surfaces ( more ).
- Fixed not being able to fast*transfer stone bricks and concrete into entities.
- Fixed splitters giving priority to one input belt ( more ).
- Fixed actions during saves strangeness ( more ).
- Fixed logistic inconsistency when removing mods that added logistic/construction robots ( more ).
- Fixed crash when removing mods that added biter spawners ( more ).
- Fixed crash related to changing forces on units ( more ).
- Fixed assembling machines going to sleep when their fluid output had fluid but the ingredient slot didn't have enough item ingredients.
- Fixed crash when trying to read LuaSurface from disconnected player through mods ( more ).
- Fixed train going into automatic mode when hitting something (again) ( more ).
- Fixed laser turrets cause other electric machines to drain more power from accumulators than they should. ( more ).
- Fixed crashes when connecting to MP game on older Ubuntu (and possibly other distributions; more )
- Fixed crash when projectile with default maximum range doesn't hit anything and flies forever ( more ).

### Scripting

- LuaSurface::set_multi_command now takes an optional third argument specifying the force to send the command to. Default is the enemy force
- Default mods are always enabled if mod*list.json is lost (even when enable new mods option is disabled).
- LuaSurface can be invalid when read from LuaPlayer and Player entity if the player is disconnected from the game (MP disconnect) * use LuaSurface.valid to check.

```
Note: LuaSurface currently never switches between valid and not valid so the check only has to be done when it's first read from the LuaPlayer.
```

- Changed default maximum range of projectiles from 10^308 to 1000.

## 0.12.0

### Features

- The game is now finished by launching the rocket with satellite.
- Added chain signals, they can be used to make more complicated junctions and stations without deadlocks.
- Added personal roboport as modular armor equipment. Once it is active, it uses the materials and robots in the players inventory. It supports all the tasks construction robots can do like building blueprints, repairing structures, deconstruction etc.
- Added logistic trash fields to the character GUI. They supply items into the logistic system in the same way active provider chests do.
- Added combinators (Arithmetic Combinator, Decider Combinator and Constant combinator). These allow more advanced manipulation with the circuit network logic ( more )
- The Lamp, Storage Tank, Small Pump and Offshore Pump can be connected to the circuit network.
- Multiplayer latency hiding (gives impression that some common tasks are performed immediately) Applies to character movement, mining buildings, building, fast replacing, opening guis, etc.
- Stone brick can be used to build stone path. (30% walking speed increase).
- Concrete can be created. The concrete can be used to build concrete floors (40% walking speed increase).
- Terrain modifies vehicle friction force (sand: 1.8, grass: 1.6, dirt: 1.4, stone path: 1.1, concrete: 0.8).
- Trees degenerate slowly when there high pollution levels.
- Lab research is now continuous. Science packs have progress bars of usage. This means that 20 labs doing research with 10 units will still be faster than 10 labs and the science packs aren't wasted.
- Assembling machine input slot can contain more than the usual stack size when the recipe requirement demands it (3 X recipe demand). Example: The rocket silo requires 1000 steel, while the stack size is 100, but the input stack can hold enough.
- Added / updated sounds for biters, spitters, worm, spawner, flamethrower, tank, lasers, etc.
- New ambient soundtrack added. Added mechanism that prevents playing track that was played recently. The ambient player alternates between neutral wind/environment sounds and soundtrack songs.
- Mousing over a train will show you its current path and blocks it can't enter.
- Locomotives now show the contents of attached cargo wagons in their tooltip.
- Trees regenerate health slowly.
- Added support for transferring contents/settings when fast*replacing all entity types.
- Added modules to the alt*view for entities that support modules.
- Factorio can run as a dedicated server without Graphics ( more ).
- Basic PvP: New forces can now be created and merged back together; a cease*fire can be agreed upon between forces
- IPv6 support for multiplayer.
- DNS names can be used when connecting to multiplayer game.
- Enabled mining trees/ghosts while holding blueprints to be built.
- Added explosive cannon shells.
- Building blueprints over existing ghosts restores the ghost time to live to full.

### Changes

- Disabled loading of saves before 0.9.0 version (You can use 0.9.8 to load older saves and re*save them).
- Removed rocket defense entity.
- Items on transport belts don't go off the belt at the end, so the transport belt has to go directly in front of the required inserter.
- Reduced number of rendered Roboport connections.
- The trade in the marketplace only happens if the player can accept the trade items.
- Inserters can now extract from Roboports and Beacons.
- Inserters now take items from right behind them, not from the center of the pickup target entity.
- Copy entity settings mechanism now remembers only the last entity copied from. Also mechanism allows copy/paste across different entities of the same type (i.e. assembling machine 1 *> assembling machine 2) and from assembling machines to requester chests (sets filters to 2 x requirements of the assembling machine).
- Trees have generally smaller bounding boxes, so it is easier to walk through forest.
- Power armor modules generate and consume 100 times more power in order to be able to charge construction robots.
- The construction robots don't build gate in the gap between the rolling stock vehicles. They wait for the train to get away.
- Player's logistic filters are now remembered after respawn in multiplayer
- All turrets are now 2x2 (incorrectly stated as 4x4); laser turrets are 4x more expensive and powerful, gun turrets are 2x more expensive
- Roboport tooltip now shows correct numbers of construction and logistic robots separately.
- When a train loses a path and cannot find a new one, it stops immediately. This prevents it from riding into parts of the rail network, from where it can't find a path.
- Improvements to circuit network wire connection. You can connect multiple wires of the same color to the same entity.
- The autosave dialog no longer cancels an active blueprint or deconstruction planner selection if the mouse button is still held after the autosave finishes
- Number of autosave slots is now configurable through config.ini (no GUI).

### Optimizations

- Overall optimization of train + belt heavy factories is roughly 66% compared to 0.11, this means that the game runs 3 times faster.
- Optimised the transport belt movement.
- Optimised the rotated bounding box collisions checks (trains).
- Optimised the smoke update.
- Optimised the solar panel, all the solar panel input is merged, so the count doesn't matter.
- Optimised the accumulators by merging then into groups, where typical factory has 1 group per network.
- Optimised the land mine activation mechanism.
- Smaller multiplayer heartbeat packet size.
- Optimised adding/removing of roboport, robots keep their tasks if they can.
- Path finder will terminate when search is too long. This avoids save explosions (see more ).
- Optimised rendering for large logistic networks.
- Fixed that the Graphics were saved twice in the RAM memory.

### Graphics

- New Graphics of the combat robots.
- New Graphics of the laser/gun turrets, their color is now player/force dependent.
- New Graphics of muzzle flash for player, car, tank and turrets.
- New tree  Graphics. Trees have 4 levels of leaves and the leafs are color-able.
- Trees emit leaves (based on the tree color) when being mined and destroyed.
- Trees emit branches when mined or destroyed.
- Storage tank has a small window showing the liquid inside.
- Combat robots attack beam ( more )
- New GUI icons: Weapons, ammo, status icons such as out*of*ammo or out*of*electricity

### Bug Fixes

- Fixed wrong item count in the logistic system when handling partially*filled magazines, repair packs or other items with durability
- Fixed the choppy (not smooth) movement when using the exoskeleton equipment.
- item*description localization now displays correctly when previewing recipes.
- entity*description localization now displays on entities.
- Proper blueprint centering. It is based on the included entities rather then the selection rectangle when the blueprint is created.
- Very big entities no longer disappear at the edge of the screen
- When putting things on ground, the first item was never put exactly under the cursor even when the place was empty.
- Fixed that it wasn't possible to swap stacks of the same items with different health.
- Fixed strange behavior of tank/car entering sound.
- Fixed LuaFluidBox crashing the game when attempting to read fluid from an entity that previously had fluidboxes.
- Car / Tank ammo inventory is refilled from the trunk / player inventory when exhausted.
- Fixed writing invalid LuaEntity::selected_gun_index crashing the game.
- Fixed the power armor battery level indicator getting drawn on top of everything else ( more ).
- Fixed that following robots created through trigger crashed the game.
- Fixed the train pathfinding issue when the train crashes to something while stopping for signal or station in front of a junction.
- Fixed that crashing to something while in manual mode in train could switch it to automatic mode.
- Fixed crashing when setting modded GUI styles in Multiplayer.
- Fixed crash when trying to read LuaPlayer::opened on a dead player.
- Fixed crash when canceling deconstruction of a logistic container that was marked for deconstruction after the logistic network it was in lost power and then regained power ( more ).
- Fixed LuaSurface::can_place_entity returning true when checking item*on*ground against item*on*ground ( more ).
- Turrets can now be modded to use shotgun (and other not guided) ammo.
- Fixed research window appearing behind the selection/minimap pane when shown from research completion ( more ).
- Fix inability to bind some OEM keys on Windows. Added the ability to bind more keys including multimedia keys. ( more )
- Fixed marking a ton of entities for deconstruction outside the construction range of roboports slowing down normal deconstruction rates.
- Fixed crash when removing electric poles from electric networks or circuit networks with large amounts of poles ( more ).
- Fixed video*memory*usage option on Windows. It is possible to run Factorio on configurations with low VRAM (less then 512MB). Other platforms don't have this issue.
- Fixed that control*clicking entire inventory into a machine installed modules.
- Fixed another instance of the "Trying to make chunk at unreasonable position" bug ( more ).
- Requester chests no longer request more than they can store. E.g. if a requester chest only has one free slot and the requester slider is set to request 20000 iron ore, the chest will only request one stack from the network ( more )
- Console no longer loses focus after an autosave ( more )
- Fixed wrong highlight when crafting ammo in vehicles ( more )

### Modding

- Ambient sounds are specified as prototypes so they can be extended and modified by mods.

### Scripting

- Changed all the identifiers/methods/events/parameters. Underscores are used as word delimiter (findentities *> find_entities).
- Changed glob to global.
- New object LuaSurface, accessible from player/entity as read property surface.
- Some commands moved from LuaGame to LuaSurface: get_pollution, can_place_entity, find_entity, find_entities, find_entities_filtered, find_non_colliding_position, find_enemy_units, find_nearest_enemy, set_multi_command, create_entity, create_unit_group, build_enemy_base, get_tile, get_tileproperties, set_tiles, pollute, get_chunks, is_chunk_generated
- Added LuaGame::local_player console command: when entered through the console it will reference the local player doing the console command. Only works when run through the console.
- Added LuaFluidPrototype * similar to LuaItemPrototype but for fluids.
- math.random can now accept negative values for ranges eg x + math.random(*10, 10)
- Added LuaRecipe::hidden and energy read.
- New object LuaGroup, accessible from LuaEntityPrototype as read property group/subgroup. LuaGroup contains: name, type, inventory_order, group, subgroups
- Added several new options to LuaEntityPrototype: mineable_properties, items_to_place_this, collision_box, selection_box, order, group, subgroup, healing_per_tick, emissions_per_tick, corpses, selectable_in_game, weight, resistances, fast_replaceable_group, loot, repair_speed_modifier
- LuaItemPrototype::group now returns the new LuaGroup object.
- Added LuaEntity::is_crafting() * returns true/false if the assembling machine or furnace is currently crafting a recipe.
- Added LuaEntity::crafting_progress/bonus_progress * a percent of 1: the current crafting progress or bonus progress.
- Added the ability to compare LuaObjects using "==" as in: "if game.player == game.players[1]" for all LuaObjects.
- Removed all LuaObject::equals(): the == operator can be used in its place.
- Added new blend modes for sprites using "blend_mode" property. Possible values: "normal", "additive", "multiplicative".
- Added on_player_driving_changed_state event * passes the player_index who's driving state changed.
- Added LuaEntity::belt_to_ground_type * returns the type "input"/"output" of the transport*belt*to*ground.
- Added several methods for manipulating gates: is_opened, is_opening, is_closed, is_closing, request_to_open, request_to_close.
- Changed LuaEntity::neighbours:

```
For electric poles: the wire connections: {copper={}, red={}, green={}}
 For transport*belt*to*ground: the input/output entity it's connected to (or none)
 For entities with fluid * the entities the fluid connections connect to indexed by the fluid connection
```

- #entity.fluidbox can now be read from any entity and will return the number of fluidboxes the entity has (0 for non*fluid handling entities).
- Added the ability to specify map colors for all entities: map_color, friendly_map_color, and enemy_map_color
- Added the ability to disable drawing the station name for train*stop type entities: chart_name = "false" in the prototype.
- LuaEntity::backer_name can now be read/written for all entities that support backer names (furnace, assembling machine, lab, locomotive, radar, roboport, trainstop).
- LuaEntity::recipe can now be set to nil to remove the recipe from an assembling machine.
- Added LuaItemPrototype default_request_amount, resistances, item_to_clear.
- Added LuaChart::chart_all (charts all the generated parts of the map).
- Expanded LuaEntity::get_item_count and LuaEntity::clear to work with all transport belt entities.
- New object LuaTransportLine, accessible from entity as read method get_transport_line(index) * an interface to the items on transport belts.
- Added LuaSurface::count_entities_filtered * the same as find_entities_filtered but simply returns a count. The benefits being: it's much faster than find_entities_filtered when the entity references aren't desired.
- Added LuaForce::enable_research() * enables research for the force if it was disabled.
- Added LuaSurface::spill_item_stack() * takes a item_stack and position and drops the items on the ground item bomb style.
- Changed LuaEntity::stack, LuaEntity::held_stack and LuaPlayer::cursor_stack to return LuaItemStack objects.
- Changed LuaItemStack to allow reading any inventory slot even when the item in the slot is invalid. LuaItemStack::valid_for_read should be used before accessing the normal properties/methods for a given LuaItemStack.
- Removed LuaEntity::clear_circuit_condition() * LuaEntity::set_circuit_condition(index, nil) can be used instead.
- Added "force" option to LuaSurface::find_entities_filtered/count_entities_filtered.
- ItemStack counts can be excluded and defaults to 1, ItemStacks can be strings and default to a full stack.
- Added LuaItemStack::count write support.
- Added LuaItemStack::can_set_stack(), set_stack(), clear() * write support to a specific item stack.
- Removed LuaEntity::stack, held_stack write support * LuaItemStack::set_stack() can be used.
- Removed LuaPlayer::cursor_stack write support * LuaItemStack::set_stack() can be used.
- Added LuaTrain::cargo_wagons read * returns only the cargo wagons for the given train.
- Added LuaEntity::remove_market_item * takes an index to remove from a Market entity offer list.
- Added LuaEntity::get_market_items * returns a table of offers the Market entity offers.
- Added LuaForce::research_progress read/write * a percent of 1 * the current research progress (0 if no research).
- Added LuaEntityPrototype::turret_range read * the range of a given turret entity prototype.
- Added player_index to the on_put_item event.
- Added ghosts from manual building and blueprints to the on_built_entity event.
- Added LuaPlayer::enable_flashlight() * counterpart to disable_flashlight().
- Replaced LuaGameScript::kill_all_enemies() by LuaForce::kill_all_units().
- Changed on_researched events to return the relayed LuaTechnology object.
- Added LuaTechnology::force read * the LuaForce the technology belongs to.
- Added LuaGame::create_surface * takes a string name and optionally a table of map gen settings and creates a new surface.
- Changed LuaPlayer::teleport to allow optionally a surface name, index or object to teleport the player to. The surface must exist.
- Added LuaSurface::request_to_generate_chunks * takes a position and radius and requests to generate those chunks * will not generate chunks outside the map bounds.
- Added LuaSurface::map_gen_settings * the current map gen settings for the surface.
- Added LuaGame::server_save * in a multiplayer game with a server, this will make the server save the game. Only works with a headless server, i.e. one launched through the **start*server option.
- Added LuaGuiElement::parent read * the parent of the LuaGuiElement if any else nil.
- Added LuaPlayer::index read * the numeric index of the LuaPlayer object.

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
