---
title: Version history/0.15.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.15.0
scraped_at: 2025-10-21 15:46:59
tags: [web, documentation]
---

# Version history/0.15.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.15.0](https://wiki.factorio.com/Version_history/0.15.0)

## 0.15.40

Date: 29. 11. 2017

### Locale

- Fixed Chinese translations.

## 0.15.39

Date: 27. 11. 2017

### Bugfixes

- Fixed corrupted Windows release. ( more )

## 0.15.38

Date: 24. 11. 2017

### Features

- Added Razer Chroma and Razer Chroma Link support ( https://www.razerzone.com/chroma )

## 0.15.37

Date: 17. 10. 2017

### Bugfixes

- Fixed false positives in detection of crashes caused by incompatible version of RivaTuner Statistics Server.

## 0.15.36

Date: 10. 10. 2017

### Bugfixes

- Fixed a bug in the fix of electric network from 0.15.35.
- Fixed a crash when deleting chunks in specific cases. ( more )
- Fixed a crash when coupling/decoupling trains through the Lua API.
- Fixed crash when unknown program arguments were passed. ( more )

## 0.15.35

Date: 28. 09. 2017

### Bugfixes

- Fixed that after a player reconnected after a desync, while blueprints were uploaded, the game would crash. ( more )
- Fixed that in certain scenarios, the blueprint library wouldn't synchronise. ( more )
- Fixed that the server would sometimes quit if a player tried to connect after another player tried to connect unsuccessfully. ( more )
- Fixed a rare desync related to electric sub networks.
- Fixed archaic (from 0.12) migration that was supposed to fix rollingStockCounts on rails and it broke it instead.
- Fixed possible desync when rotating pipe to ground. ( more )
- Fixed a rare possibility of internal electric network crash when loading game. ( more )
- Handle network errors (caused by LavasoftTcpService64.dll corrupting Winsock) gracefully. ( more )

### Scripting

- Fixed changing force of underground belt entity would cause desync. ( more )

## 0.15.34

Date: 23. 08. 2017

### Bugfixes

- Fixed that after a player reconnected after a desync, their blueprints would no longer upload. ( more )
- Fixed that it was possible to modify other players' blueprint libraries. ( more )
- Fixed a crash when loading a save that was transferring blueprints to a now offline player. ( more )
- Fixed that the blueprint library would remove duplicate blueprints even though they were in different books. ( more )
- Fixed game freezing when clicking the decrease replay speed button. ( more )
- Disabled possibility to open invalid save/replay by enter key or double click.
- Fixed rare crash when being disconnected from multiplayer. ( more )
- Fixed creating map from scenario would copy also system and hidden files from scenario folder. ( more )
- Fixed threading issue causing random server crashes. ( more )
- Fixed that if the server was launched with --start-server-load-scenario , the /save command with no name would cause the server to hang. ( more )
- Fixed --start-server-load-scenario would ignore --map-gen-settings , --map-settings and --preset options. ( more )
- Fixed disabling shaders would cause crashes. ( more )

## 0.15.33

Date: 09. 08. 2017

### Changes

- Mod name in mod info pane will no longer be localised. ( more )
- Optional mod dependencies now show as orange when invalid. ( more )

### Bugfixes

- Fixed crash when trying to load replay that is not compatible with current version.
- Fixed ghosts might emit light. ( more )
- Fixed removing land mines didn't make any sound. ( more )
- Fixed creating window larger than screen. ( more )
- Improved performance of rendering uranium ore. ( more )

### Modding

- Bonus UI now shows additional force modifiers ( more )
- simple-entity-with-owner (and simple-entity-with-force) now supports apply_runtime_tint in sprite definition.

### Scripting

- simple-entity-with-owner exposes color property through LuaEntity::color . Set it to {r=0, g=0, b=0, a=0} to use color of entity's force.
- Fixed LuaEntityPrototype::distribution_effectivity would return value of supply_area_distance instead. ( more )

## 0.15.32

Date: 02. 08. 2017

### Bugfixes

- Fixed compatibility problem with several antivirus programs. ( more )
- Fixed seed in map-gen-settings.json would be ignored when creating map on headless server. ( more )
- Fixed that connecting to a multiplayer game with a large blueprint library might be difficult. ( more )
- Fixed that using capsules would open an Entity's GUI when clicked. ( more )
- Fixed that --window-size =maximized wouldn't work on Linux. ( more )
- Fixed that changing reactor consumption(production) values through a mod didn't update its production until rebuilt. ( more )
- Fixed that blueprints would sometimes stop transferring.
- Fixed crash when opening item/container and at the same time the controller is set to some that doesn't have inventory. ( more )
- Fixed 3 possible crashes related to getting malformed network packet over the network.
- Maybe fixed a biter path cache-related crash. ( more )
- Fixed that bad_alloc and similar low level errors were caught internally, so we couldn't get proper stack trace of those.
- Limited the size of a train chart tag when the map is zoomed in. ( more )
- Possible rare crash fix related to building rails and viewing preview of entities right after that. ( more )
- Limited technology cost multiplier to maximum of 1000. ( more )

### Scripting

- The log method also specifies the mod that wrote that, not only script file.
- Added LuaEntityPrototype::distribution_effectivity read.
- Added LuaEntityPrototype::time_to_live read.
- Added LuaControl::following_robots read.
- Added LuaPlayer::pipette_entity() .
- Added LuaEntity::can_be_destroyed() .
- Added script_raised_destroy reserved event ID.
- Added script_raised_built reserved event ID.
- Added script_raised_revive reserved event ID.
- Changed LuaEntity::time_to_live to also work for combat robots.
- Changed LuaEntityPrototype::fluid_capacity read to also work on fluid-wagon.
- Changed LuaEntityPrototype::turret_range read returns nil instead of error if not turret.
- Changed LuaEntity::train to return nil if entity is not rolling stock.
- Added LuaEntityPrototype::explosion_beam read.
- Added LuaEntityPrototype::explosion_rotate read.

## 0.15.31

Date: 25. 07. 2017

### Minor Features

- Train stop text angle is now configurable in the graphics settings. Default value is 30 degrees.

### Bugfixes

- Fixed that resizing the game window was very slow on Linux. ( more )
- Fixed rendering of turret ranges on map. ( more )
- Fixed "Disable listed mods" in minimal mode would disable all mods including Base if mod-list.json didn't exist. ( more )
- Fixed that pressing escape in the "mods error" GUI would close it and leave the game in a broken state. ( more )
- Fixed possible crash when loading game. ( more )
- Car and Tank now make a sound when deconstructed. ( more )
- Fixed that using the color command with no arguments would set your color to black.
- Fixed a crash when deleting a blueprint book while the label is being edited in the blueprint library. ( more )
- Fixed crash when closing the game in the Generate Map GUI. ( more )
- Fixed that the generate map GUI would show incorrect values for some of the enemy expansion settings in some cases. ( more )
- Fixed that some blueprints would always have to be reuploaded after connecting to a server, even if they weren't changed. ( more )
- Fixed that the map seed field wouldn't be used when given in a map-gen-settings.json file through the command line. ( more )
- Fixed that missing controls in "autoplace_controls" for map gen settings would get filled with default values instead of disabling unlisted controls.
- Fixed that blueprints would stop transferring if the game was loaded from a map that included some transfers in progress. ( more )
- Fixed missing font for Thai language.
- Changed the hazard concrete/concrete tile transition so it behaves predictively.

### Modding

- Fixed layered icons would render incorrectly in some cases. ( more )

### Scripting

- Fixed a crash when using LuaPlayer::disable_all_prototypes() and opening the technology GUI. ( more )
- Fixed that research bonus could be set to negative. ( more )
- Fixed that items in the character trash slots would get lost on reducing inventory size instead of spilling the items on the ground. ( more )
- Fixed validation for pickup_position and drop_position. ( more )
- Exposed internal buffer of fluid turret to Lua as its last fluidbox.
- Added LuaEntityPrototype::fluid_capacity read.

## 0.15.30

Date: 14. 07. 2017

### Bugfixes

- Fixed crash related to empty player blueprint shelf. ( more )
- Fixed crash related to handling focused state of widgets.
- Fixed possible crash when using font with size 0. ( more )
- Fixed focus error preventing to access GUI when the game is paused in multiplayer.
- Fixed a crash when the map can't be saved to disk due to permission errors when joining MP games. ( more )

### Modding

- Added optional "hide_resistances" to entity prototype to control whether resistances should be hidden in description for friendly forces. Default is true.

## 0.15.29

Date: 13. 07. 2017

### Changes

- Underground pipes will no longer connect if there is candidate ghost underground pipe between them.
- Command line option --window-size can be also used to start the game in maximized mode when used as --window-size =maximized
- The library no longer shows unavailable blueprints of off-line players, since there is nothing that can be done with them.

### Bugfixes

- Fixed that the edit field of a blueprint book in the shared pane would get reset every time crafting finished. ( more )
- Fixed that setting visibility to false on modded GUI elements while a text field had focus would keep blocking normal input. ( more )
- Fixed a performance problem when having the blueprint library GUI open while robots add/remove large amounts of items from the character. ( more )
- Fixed that walls and pipes built from blueprints could mark trees/rocks for deconstruction by mistake in some instances. ( more )
- Fixed entities with force color (turrets, gates, ...) would be drawn black in blueprint preview.
- Fixed false positive in game state corruption detection logic. ( more )
- Fixed pipette tool would pick diagonal rail with wrong direction. ( more )
- Fixed migrating save from level 4 of New Hope campaign would disable Plane recipe. ( more )
- Fixed that the blueprint library wouldn't close when Q is pressed and bound to the Close Window action. ( more )
- Fixed that blueprints would stop transferring if the game was saved whilst some transfers were in progress and then reloaded from this save. ( more )
- Fixed error with modal focus related to having blueprint error message and removed content message at the same time.
- Fixed server wouldn't close and delete a temporary save file made for a client that disconnected before the server finished saving. ( more )
- Fixed that standing on belts facing each other between two chunks would cause the player actions to run at double speed.
- Fixed that in an artificial test-case, two blueprints couldn't in the library at the same time. ( more )
- The Pipette tool will now copy the rotations of vehicles and trains. ( more )
- Fixed that making blueprints of ghost tiles on top of real tiles would have seemingly "random" results in the blueprint. ( more )
- Possible fix of the double "Communication with server failed" error. ( more )
- Fixed entities to be built wouldn't get rendered in some places when hovering over transparent GUI elements in the map editor. ( more )

### Modding

- Added optional "render_not_in_network_icon" for logistic container prototypes defaulting to true.
- Fixed empty sprite path would cause game to crash instead of entering minimal mode. ( more )

### Scripting

- Added LuaItemStack::swap_stack() .
- Added on_player_removed event.

## 0.15.28

Date: 06. 07. 2017

### Balancing

- Reduced time needed for an unit of Automation 2 research from 15 to 5 seconds to compensate for previous change of science packs requirements.

### Minor Features

- Added --window-size launch option. For example --window-size =1680x1050 ( more )
- Damaging a tree with impact or physical damage generates some leaves.
- Warning icon for logistic chests that are not in a reach of roboport.
- Train stop names are rendered at 45 degrees to better show names.

### Bugfixes

- Fixed that ghosts would stay over entities after deconstruction was canceled. ( more )
- Fixed that the controls menu wouldn't use a fixed common width between controls sections.
- Inserter researches now require equal ratios of science pack types.
- Fixed that transferring blueprints from the library could make the headless server crash. ( more )
- Fixed that blueprints could be duplicated when moving to a new version. ( more )
- Fixed progress bar not showing in the entity info panel if the text was too long. ( more )
- Fixed (at least one of the cases) of crashes related to not being able to connect to auth server while joining game. ( more )
- Fixed, possible crash related to changed bounding box of entity by a mod. When the mod is removed (added) the corner of the entity can occupy chunk that doesn't exist yet which would cause a loading error. ( more )
- Fixed that mining sounds and the leaves effect weren't present when mining tree from a car. ( more )
- Fixed possible crash when removing modded rails during save migration. ( more )

### Modding

- Mod hotkeys are arranged per-mod.
- Disallowed defining different rail categories for this moment as having more than one will never work properly until we spent some non-trivial time with that, which is not a priority now.

### Scripting

- Fixed that item-with-inventory filters wouldn't be preserved when cloned through the Lua API. ( more )

## 0.15.27

Date: 03. 07. 2017

### Balancing

- Speed and efficiency module 3 technology now requires high tech science packs instead of production science packs, so that working towards power armor mk2 does not require production science packs. This makes the branching between high tech and production science packs more meaningful.
- All researches now require equal ratios of science pack types. This reduces the cost of some researches.

### Bugfixes

- Fixed manually inserting items into the blueprint book would disconnect you in multiplayer. ( more )
- Fixed a crash when clicking an alert the same tick the game is loaded. ( more )
- Fixed a crash when saving screenshot failed. ( more )
- Fixed that trains could stop in the middle of chain signal blocks in some specific setups causing deadlocks. ( more )
- Fixed that large drop-down widgets would render off the bottom of the screen in some cases. ( more )

### Modding

- Added "render_layer" property to car prototype definition.

### Scripting

- Fixed that calling LuaForce::chart (...) would try to chart chunks outside the map limits. ( more )
- Fixed that LuaPlayer::unlock_achievement() would keep showing the notification after the achievement was unlocked. ( more )
- Fixed that LuaItemStack::create_blueprint didn't behave the same way as normal blueprint creation in regards to ghost tiles. ( more )
- Fixed that LuaEntity::selected_gun_index write was 0-based. ( more )
- Fixed that mods could do remote calls outside of events when the game isn't in a valid state. ( more )
- Fixed that a time_before_removed of 0 on a corpse entity could crash the game in some instances. ( more )

## 0.15.26

Date: 30. 06. 2017

### Bugfixes

- Fixed a crash when rendering modded pumps in some instances. ( more )
- Fixed that biters building new bases could cause a player standing in the way to be destroyed instead of killed. ( more )
- Fixed that the auto-cursor-refill wouldn't refill if the cursor started with 1 item. ( more )
- Fixed crash related to removing power switch connected to electric pole in a blueprint.
- Fixed crash related to building electric pole that is connected to closed power switch by blueprint. ( more )
- Fixed that the player would respawn at {0,0} in the campaign levels. ( more )

### Modding

- The God controller properties can now be set through the prototype system.

### Scripting

- Fixed that using math.random in control.lua before the file was fully parsed was not deterministic. ( more )
- Fixed that create_entity{variation=...} was 0-based. ( more )

## 0.15.25

Date: 29. 06. 2017

### Bugfixes

- Fixed that energy shields would charge faster than normal when the generators couldn't provide full power and there was a battery with available energy in the grid. ( more )
- Fixed crash when making blueprint from power switch ghost.
- Fixed a desync when loading save files from different game versions. ( more )
- Fixed that the map gen presets list box wouldn't respond to mouse clicks. ( more )

## 0.15.24

Date: 29. 06. 2017

### Minor Features

- Power switch connections are stored in the blueprint.

### Changes

- The F1-F12 debug hotkeys can now be reassigned.
- Disabled pumps don't block other pumps from connecting to fluid wagon anymore. ( more )
- Pump can connect to fluid tank that is slightly rotated, but only to tanks that are standing on straight rails.
- Blueprints in the library no longer transfer automatically when a player joins. Instead, they are transferred on-demand.
- Admins are allowed to modify other players' blueprints in the library, including deleting them.
- Changed default key binding for toggle filters on macOS to Command + Right Click ( more )

### Bugfixes

- Fixed Info boxes sometimes going to the center of the screen on scale change or display size change. ( more )
- Fixed the direction of underground belts/pipes wouldn't get detected correctly when using the pipette tool in some cases. ( more )
- Fixed that accumulators had two energy bars and one of these was showing incorrect value. ( more )
- Fixed that Copy paste couldn't be used in the numeric edit box.
- Fixed that the recipe tooltip would resize/change every time something was crafted. ( more )
- Fixed burner inserter reading signal pulses twice ( more )
- Fixed electric buffer error that could happen when updating save to newer factorio version or changing mods. ( more )
- Fixed that failing to mine an entity wouldn't try to transfer all items in the entity. ( more )
- Fixed locomotive could snap to train stop after it was attached to an existing train. ( more )
- Fixed that the item counts when making blueprints or deconstructing things would render off-screen. ( more )
- Fixed impossible research tasks in team production challenge. ( more )
- Fixed that the blueprint library GUI wouldn't restore scrollbar position when moving in or out of a book. ( more )
- Fixed that setting inserter filters wouldn't update the last-user. ( more )
- Fixed that fluid would not flow through circuit network disabled mining drills. ( more )
- Fixed a crash when exiting multiplayer due to a script error while hosting a public game locally. ( more )
- Fixed pump would not connect to last tile of a train in some cases. ( more )

### Modding

- Changed the format for localised mod name and description.
- Fixed that assembling machines using the heat energy source type would go inactive when out of power and stay inactive. ( more )
- Limited map gen presets pollution diffusion and dissipation rate values to prevent never-ending pollution bloating map sizes by mistake. ( more )
- Removed CustomInputPrototype consuming types "all" and "script-only".
- entity-with-owner now supports variation in blueprints.

### Scripting

- Fixed that marking an entity for deconstruction through script wouldn't fire the event. ( more )
- Fixed that level based research wouldn't fire the research-finished event in some cases. ( more )
- Fixed that several of the drop-down related methods for LuaGuiElement were 0-based.
- Added a global Lua function "table_size" which will quickly compute the number of values in any lua table (not to be confused with the # operator).
- Added LuaGuiElement::remove_item for drop-down type elements.
- Added LuaSurface::clear_pollution() .
- Added events on_console_chat and on_console_command.
- Added LuaEntityPrototype::production read.
- Added LuaControl::mine_tile() .

## 0.15.23

Date: 22. 06. 2017

### Changes

- Reverted change that made Inserters no longer drop what they are holding when disabled by the circuit network. ( more )

### Bugfixes

- Fixed that the UI scale option wouldn't apply until restarting the game in some cases. ( more )
- Fixed that number-input fields would also block letters/other keys. ( more )
- Fixed that tile filters in the deconstruction planner wouldn't get used in some cases when entity filters were also defined. ( more )
- Fixed curved rail ghosts wouldn't mark trees/rocks when force-built. ( more )
- Fixed construction robots could stop doing their jobs when roboport was destroyed or unpowered. ( more )
- Fixed long strings in the right description pane. ( more )

### Modding

- Fixed that some mod mods would falsely be detected as removed and have GUI elements they added removed on load. ( more )

### Scripting

- Fixed that teleporting entity ghosts didn't work correctly. ( more )

## 0.15.22

Date: 21. 06. 2017

### Changes

- Blueprints in the blueprint library are sorted using case-insensitive natural compare. E.g. the sorting order now is "1", "2", "10", instead of the previous "1", "10", "2".
- Inserters will no longer drop what they are holding when disabled by the circuit network. ( more )
- The deconstruction planner filter now treats any entity filter as also matching entity ghosts of that type.
- Multiplayer creation GUI now remembers game name. ( more )

### Balancing

- Explosive Mine now only does damage to enemy units and structures. Sounds:
- Added missing vehicle collision sounds (pipes, solar panels, etc...)
- Reduced volume of ore mining and tree chopping.

### Bugfixes

- Toggling fullscreen via options or Alt-Enter now keeps window on the same monitor. ( more )
- Fixed that in long recharging queues some robots would never get a chance to recharge. ( more )
- Fixed that it wasn't possible to click and drag blueprints into an empty blueprint book. ( more )
- Fixed that deconstruction/blueprinting selection would be canceled if the selection ended on one of the always-visible GUIs. ( more )
- Fixed the productivity bar in the furnace GUI wouldn't show in some instances. ( more )
- Fixed exiting a multiplayer game hosted through the in-game multiplayer option. ( more )
- Fixed that tile ghosts would always get selected over real entities. ( more )
- Fixed that the heat-connection icon was not visible on entities other than boiler and reactor. (related to modding)
- Fixed that furnace with heat source couldn't be rotated before placing it.
- Fixed the gui of furnace using heat as energy source.
- Fix PvP Gui script error. ( more )
- Fix that clearing items in Transport belt madness didn't give the items back. ( more )
- Fixed that rails marked for deconstruction wouldn't allow canceling deconstruction while a train was on  them. ( more )
- Fixed that biters would change orientation rapidly when they were near a player whom they couldn't attack. ( more )
- Fixed that Rocket Silo would continue crafting for 1 tick after completing a rocket. ( more )
- Fixed that lot of other keys that can be used to write characters in the edit box (or console) were not blocked from affecting the game if they are assigned to do a game action. Having text box active now means that all of the keys are blocked from affecting the game.
- Fixed (hopefully), that the stretching of bounding boxes of walls to touch their neighbours was not taking into account when  marking things in the way for the blueprint. ( more )
- Fixed that the description pane would change width depending on the content. It should now never change width. ( more )
- Fixed that the shooting-target would render as valid to shoot with rockets when it actually wasn't. ( more )
- Fixed that programmable speakers would get wrong instruments after importing pre-0.15.19 blueprint string. ( more )
- Fixed that maximized Factorio window had thin border around it. ( more )
- Fixed that vanilla and modded version of achievements could be mixed up. ( more )
- Fixed that inserters would try to insert items into other non-burner inserters. ( more )
- Fixed that fast-transferring modules into the rocket silo would put them into the module slots and the rocket at the same time. ( more )
- Fixed that the "rocket launched without satellite" message couldn't be dismissed in some cases. ( more )
- Fixed the mining drill GUI wouldn't show mining progress when it had a large number of modded module slots. ( more )
- Fixed fast-replacing an assembling machine with overloaded ingredients would spill the items. ( more )
- Fixed many ingredients or products in recipes would break the assembling machine GUI. ( more )
- Fixed wrong values when using /config set allowed-commands with invalid values would crash the game. ( more )

### Modding

- Fixed that giving rolling stock entities invalid collision masks would crash the game. ( more )
- Mod title and description can now be localised.
- Fixed a crash when mods use reset technologies during the technology researched event. ( more )
- Fixed that modded GUI elements wouldn't get removed in some cases when the mod was removed. ( more )
- Fixed source_effects applying effects to the source by the target instead of to the source by the source. ( more )

### Scripting

- Fixed setting robot.energy for logistic/construction robots wouldn't account for the robot battery upgrade. ( more )
- Fixed that setting LuaBurner::currently_burning didn't accept LuaItemPrototype as the docs said. ( more )
- Added LuaEntityPrototype::count_as_rock_for_filtered_deconstruction read.
- Added LuaEntityPrototype::filter_count read.
- Added LuaEntity::spawner /units read.

## 0.15.21

Date: 15. 06. 2017

### Bugfixes

- Fixed that the server would crash if someone tried to connect when there were no blueprints being transferred. ( more )

## 0.15.20

Date: 14. 06. 2017

### Changes

- Transports belt entities show belt speed in the tooltip and entity description.
- Reduced fluid wagon air resistance from 0.05 to 0.01
- Scenario names are now localised.

### Bugfixes

- Fixed login details getting lost (hopefully). ( more )
- Fixed a crash that would happen if the game exited due to a script error that happened immediately after deleting a force. ( more )
- Fixed int mod settings would show incorrect values in the GUI. ( more )
- Fixed gun sounds would continue when switching weapons while firing. ( more )
- Fixed a performance issue caused by spawners being active all the time in peaceful mode. ( more )
- Fixed a crash when removing train stops next to other train stops and then building locomotives. ( more )
- Fixed a rare desync related to opening your player inventory. ( more )
- Fixed a crash when teleporting/setting the force of a offline roboport. ( more )
- Fixed inserters with custom pickup/drop locations from mods would retain the custom data when the mods were removed. ( more )
- Fixed a crash when deleting blueprint records from the blueprint library while another player is viewing the record tooltip. ( more )
- Fixed that some clients wouldn't be able to connect to a server when blueprints were being uploaded. ( more )
- Fixed that Factorio wouldn't start when run from an NFS partition. ( more )
- Fixed crash on macOS older than 10.9 ( more )

### Modding

- Removed unused "energy consumption" from the roboport equipment. ( more )

### Scripting

- Fixed that setting researched = true on level-based research in progress wouldn't update the research level displayed. ( more )
- Fixed that game.write_file would cause desyncs if it failed due to file permission issues. ( more )
- Fixed a crash related to the train changed state event. ( more )
- Added events on_player_setup_blueprint, on_player_deconstructed_area, and on_player_configured_blueprint.
- Added LuaEntity::secondary_bounding_box read.
- Added LuaForce::worker_robots_battery_modifier read/write.
- Added LuaGuiElement::enabled read/write.

## 0.15.19

Date: 08. 06. 2017

### Changes

- Added alarm sounds to programmable speaker.
- Fullscreen is on by default.
- Locomotive snaps to a train stop when placing the first locomotive next to the train stop.
- Changed automation and fluid wagon research so it doesn't have multiples of science packs per unit. ( more )
- --start-server-load-scenario can load scenarios provided by a mod. For example, --start-server-load-scenario base/wave-defense will load the wave-defense scenario from the base mod.

### Graphics

- Changed the icon of the automation research, so it is not confused with the logistics research.

### Bugfixes

- Fixed that destroyed transport belt could leave zombified items in nearby tile ( more )
- Fixed inserter zombification at rail junctions ( more )
- Fixed visual seams on map/minimap ( more )
- Fixed that gate over rail could be rotated
- Fixed GUI size problems with the logistic networks GUI. ( more )
- Fixed that the headless server didn't close when it failed. (Most typically because of script error) ( more )
- Fixed misaligned force color mask on capsule projectiles. ( more )
- Fixed crash when changing player's controller, when player was controlling a vehicle with god controller. ( more )
- Fixed a crash caused by manually deactivated units. ( more )
- Fixed that exporting blueprints wouldn't respect the current filter options in the setup GUI. ( more )
- Fixed that selection-by-typing in list boxes would also trigger normal game actions. ( more )
- Fixed that adding stops to a train could change the current station. ( more )
- Fixed that the search text didn't reset after leaving the browse-mods GUI. ( more )
- Fixed that the mods-load-error GUI could end up too large to fit on screen. ( more )
- Fixed a crash when interacting with the "save/quit/reconnect" window after losing connection with a server. ( more )
- Fixed crashes when locking bitmap fails. ( more )
- Fixed rail preview was rendered under entities. ( more )
- Fixed message box in main menu  being not clickable ( more )
- Fixed trains stuttering on extremely short paths. ( more )
- Fixed flamethrower stream would destroy trees directly. ( more )
- Fixed that some information was missing from generator entities. ( more )
- Fixed that Factorio would hang on Linux after trying to paste a string when the clipboard was empty. ( more )
- Fixed generating unwinnable research tasks in team production scenario. ( more )
- Fixed that clicking escape while connecting to the game could lead to weird situations as the normal menu was opened. Pressing escape while connecting will abort the connection instead. ( more )
- Fixed the productivity bar in the mining drill wouldn't show in some cases. ( more )
- Fixed that the blueprint book gui didn't stretch vertically when possible. ( more )
- Fixed inconsistent hovered font color on buttons and dropdowns. ( more )
- Fixed train stuttering with only disabled stations in their schedule ( more )
- Fixed that you could disconnect wires at any distance. ( more )
- Fixed the icon used when rendering coal being held by construction robots. ( more )
- Fixed headless server on macOS getting stuck when in background ( more )
- Fixed that attempting to edit a blueprint label for the second time would show the original label before any edits were made. ( more )
- Fixed that --start-server-load-scenario wouldn't give an error when the specified scenario couldn't be found. ( more )
- Fixed that robots would leave items on the ground when building ghosts in some cases. ( more )
- Fixed train GUI size problems when the fuel tab is removed due to it going out of reach. ( more )
- Fixed that blacklisting tile ghosts in the deconstruction planner didn't work. ( more )

### Modding

- Fixed that the fluid wagon wouldn't show the equipment grid when one was added through mods. ( more )
- Fixed loading the item-with-tags item type. ( more )

### Scripting

- Fixed set_command with an empty list of commands would crash the game. ( more )
- Fixed LuaRandomGenerator docs. ( more )
- Added LuaTechnology::level write support for level-based technology. ( more )

## 0.15.18

Date: 01. 06. 2017

### Bugfixes

- Fixed that wire connections were not preserved in tightspot campaign. ( more )
- Fixed various crashes on macOS related to logistic counts. ( more )

### Modding

- Changed default value of "allow_custom_vectors" in inserter prototype to true, vanilla inserters set it to false explicitly.

## 0.15.17

Date: 01. 06. 2017

### Graphics

- Inserters in high resolution; normal resolution inserters are unchanged.

### Bugfixes

- Fixed some inconsistencies in programmable speaker gui ( more )
- Fixed that headless mode wiped out controls section of config file ( more )
- Fixed that detached roboports (e.g. after blackout) would not reset circuit network readings on number of robots ( more )
- Fixed that active blueprint/deconstruction-planner selection did not reset when switching between game and map ( more )
- Fixed AltGr behavior with special characters ( more )
- Fixed that mining bar would steal mouse focus ( more )
- Fixed the /evolution command would underflow when showing negative pollution values. ( more )
- Fixed crash when mod-list failed to save when exiting the game. ( more )
- Fixed game would not save at all if generating preview picture failed. ( more )
- Fixed desync related to driving vehicles. ( more )
- Fixed unnecessary quotes in programmable speaker note translations ( more )
- Fixed that the bonus GUI wouldn't fit on screen with a large amount of modded content. ( more )
- Fixed crash when closing public server. ( more )
- Fixed that filter inserters lost their filter in tightspot campaign. ( more )
- Fixed empty space would be rendered if glyph was missing in current font. ( more )
- Fixed that resizing the game window while catching up after joining a multiplayer game would leave the map blank. ( more )
- Fixed issue and desync when disconnecting one wire color of an entity connected to 2 wire colors. ( more )
- Fixed a multiplayer crash that would happen when a player left whilst uploading their blueprint library and then rejoined the same server. ( more )
- Fixed another issue that prevented spawners from spawning. ( more )
- Fixed game would fail to load if max-texture-size was too low. ( more )

### Modding

- Moved the "mod-settings.json" file so it now resides in the "mods" subfolder allowing it to work with the mod-directory command line option.
- Added support for virtual-signal migrations.
- Inserters now require the inserter prototype property "allow_custom_vectors" to be true before they allow setting custom pickup/drop locations.
- Font paths were moved from locale cfg to locale info.json (see core/en/info.json).
- Changed default value of hand_length in inserter prototype to 0.75, to make inserter shadow look nicer.

### Scripting

- Fixed crash when teleporting character entities while in vehicles. ( more )
- Fixed that character.character_maximum_following_robot_count_bonus didn't work. ( more )
- Fixed that /help for lua commands wouldn't do parameter substitution correctly. ( more )
- Added LuaEntityPrototype::resource_categories , fluid, and pumping_speed read.
- Added LuaEntity::previous_recipe read.
- Added LuaEntityPrototype::stack /allow_custom_vectors read.
- Changed LuaEntityPrototype::speed to also work for rolling stocks.

## 0.15.16

Date: 27. 05. 2017

### Changes

- Temporarily reverted GUI interaction changes (some GUI elements responding only to left mouse button, buttons clicked on mouse up instead of mouse down) introduced in 0.15.13 and 0.15.14.

### Bugfixes

- Fixed the "back" button wouldn't work in the save-game GUI. ( more )
- Fixed the "cancel" button wouldn't work in the user-login GUI. ( more )
- Fixed that the map editor item/inventory buttons didn't work. ( more )
- Fixed beacons would "wobble" in blueprints. ( more )
- Fixed crashes related to clicking different buttons.
- As a one-time migration, enemy spawners will reset their absorbed pollution to zero when a save from a previous version of 0.15 is loaded. ( more ) This is to avoid an extreme temporary spike in difficulty that would happen after loading a save with many spawners that were affected by a bug in the previous versions.
- Fixed the market GUI didn't work. ( more )
- Fixed crash when pollution reaches unreasonably far chunk. ( more )
- Fixed power bars glitch in electric network statistics dialog. ( more )

### Scripting

- Fixed setting LuaGuiElement::elem_value would always expect the elem_type to be "item". ( more )

## 0.15.15

Date: 26. 05. 2017

### Bugfixes

- Fixed desync related to loading pre 0.15.14 save with beacons marked for deconstruction without resaving it first.
- Fixed that spawners would sometimes stop spawning units even when polluted. ( more )
- Fixed crash when changing assembling machine recipe. ( more )
- Fixed crash that would happen after clicking a button in the tech tree. ( more )

### Scripting

- Fixed crash when creating smoke entity through create-entity trigger effect. ( more )
- Added Entity::update_connections . It updates connection of loader and beacon to entities that might have been teleported out or in. The effect might include more things later on.

## 0.15.14

Date: 26.05.2017

### Optimisations

- Optimised beacon update times which helps especially when the power is not full and it fluctuates.

### Changes

- Added support for using username and password for proxy connections.
- Changed technology sorting. All of the science pack types affect the order, not just the most expensive one. ( more )
- Leading and trailing whitespace will be trimmed from host name or IP address entered to Direct Connect multiplayer dialog. ( more )
- Electric network info window shows all connected entities in the list and the graph even when they have 0 consumption/production. This means, that the count of entities connected to the network is shown even if they don't consume or produce.
- Electric poles that have 0 consumption as well as 0 production show empty electricity graph instead of full. ( more )

### Bugfixes

- Keypad enter is treated as regular enter ( more )
- All buttons apart the inventory/recipe/crafting queue and item selection slot react on mouse click instead of just mouse down.
- Fixed that mining drills would continue to insert into entities when moved far away. ( more )
- Fixed that right click and drag in the blueprint setup GUI didn't work to remove things from the blueprint. ( more )
- Fixed that blueprint icons couldn't be removed with right click. ( more )
- Fixed that right-clicking items in the crafting queue didn't work to cancel 5.
- Fixed window being created slightly offscreen on certain resolutions. ( more )
- Fixed that the edit field for a blueprint book would get reset when bots delivered items to the player. ( more )
- Fixed that inserter facing north was slower compared to other directions. ( more )
- Fixed that the solaris achievement ignored usage of steam-turbines. ( more )
- Fixed that setting logistic requests didn't work in the map editor. ( more )
- Fixed crash after dropping a blueprint into a book inside the blueprint library. ( more )
- Fixed loading blueprint library from before 0.15.4 might crash. ( more )
- Fixed a crash related to changing the rail system when signals get disconnected from blocks. ( more )
- Fixed that furnaces and assembling machines weren't rotatable with heat pipe connection. ( more )
- Fixed crash when using --load-game with an error in a mod. ( more )

### Modding

- Fixed reading LuaCommandProcessor::commands when one of the help keys was empty. ( more )
- Fixed that disabled mods could change the mod event order.

### Scripting

- Fixed changing force of lab ghost would cause desync.
- Added LuaCustomGuiElement type "text-box".

## 0.15.13

Date: 23. 05. 2017

### Changes

- Most of the gui elements now work only with left mouse button, so other buttons might be used without interfering with gui.

### Bugfixes

- Fixed that biters would sometimes try to attack indestructible entities. ( more )
- Fixed that clearing the blueprint label would make the GUI show the previous label. ( more )
- Fixed personal laser defense equipment shooting at player in vehicle would hit the player instead of the vehicle. ( more )
- Fixed that the edit label button on blueprint books in the library could get hidden behind the delete button. ( more )
- Fixed missing space after timestamp in server console output messages that didn't contain tag. ( more )
- Fixed that the blueprint library wouldn't update blueprints stored in books. ( more ) ( more )
- Fixed that reach-distance checks for curved rails only checked against one end of the rail. ( more )
- Fixed bonus GUI display values when the bonuses were negative. ( more )
- Fixed that the auto launch settings of rocket silo was not saved in blueprint. ( more )
- Fixed beta campaign level 02 would error for migrated save games. ( more )
- Fixed locked belts in demo campaign level 03. ( more )
- Localised programmable speaker notes and instruments. ( more )
- Fixed that mining drill window got repositioned to the center every time it switched to another resource. ( more )
- Fixed fluids/virtual signals in the blueprint library wouldn't migrate correctly between different modded saves. ( more )
- Before 0.14 the game didn't track online time of players, this caused that games transitioned from pre 0.14 could prevent players to get achievements until they spent enough of time in the game again. So for single player games, when transitioning to 0.15.13, the online time is reset to be full time of the map.
- Fixed that the bonus progress of assembling machine didn't reset when the recipe was changed by using copy paste. This could be exploited to get extra free product of expensive items. ( more )
- Fixed crash when loading modded saves that used the flamethrow-explosion entity type. ( more )
- Fixed performance problems when building rails related to large rail sections and chain signals. ( more )
- Fixed desync related to trains.
- Fixed blueprint library wouldn't use the Open Item GUI key binding. ( more )
- Fixed that errors in mod locale would only show in the log file instead of giving the standard mod-error GUI. ( more )
- Fixed that turret help view on map did show turrets from other surfaces. ( more )
- Fixed that silo script didn't validate items on configuration changes. ( more )
- Fixed that tightspot level 05 had incorrect recipes unlocked. ( more )
- Fixed that you could pipette items and break transport belt madness. ( more )
- Fixed that the game would crash when trying to load corrupt blueprint-storage.dat. ( more )
- Fixed that map was not updated correctly when tile editing ended up changing other tiles in different chunk. ( more )
- Fixed crash when loading modded saves that contained specific items without the mods. ( more )
- You can now open circuit network connectible entities while holding copper wire. ( more )
- Fixed crash when closing the game window in Browse Games/Play on LAN gui. ( more )
- Fixed that the bonus progress bar of furnace disappeared when the smelting was not currently in progress.
- Fixed that changing recipe in the furnace didn't reset the bonus progress bar. ( more )
- Fixed that selection box of rotated (and modded) storage tank wasn't respecting the rotation properly. ( more )

### Modding

- Electric energy sources now support effectivity.
- Fixed crash when mods add values to data.raw incorrectly. ( more )
- Fixed some entities using heat energy source types wouldn't connect to heat pipes correctly when rotated. ( more )
- Mod settings now shows the mod display name instead of the mod ID name (My Mod Name instead of my-mod-name).
- Changing mod startup settings will now fire the on_configuration_changed event when appropriate.

### Scripting

- Fixed crash when using game.take_screenshot and then deleting the surface. ( more )
- Fixed the old train ID wouldn't be included in some cases during the on_train_created event. ( more )
- Fixed crash when trying to register negative event ids. ( more )
- Fixed that force.reset_technology_effects() didn't preserve currently researched technology and saved technology progress. ( more )
- Fixed LuaEntity::neighbours return format to match the docs. ( more )
- Fixed LuaPlayer::mine_entity() would return false when successfully mining the given entity. ( more )
- Changed create_entity 'item-request-proxy' "modules" to take the same format as LuaEntity::item_requests . ( more )
- Changed LuaSurface::freeze_daytime() to freeze_daytime read/write.
- Removed LuaPlayer::cursor_position .
- Added LuaEntity::proxy_target read - the target an item-request-proxy is pointing at if any.
- Added LuaEntityPrototype/ LuaEquipmentPrototype::electric_energy_source_prototype read.
- Added LuaEntityPrototype::fluid_usage_per_tick , maximum_temperature read, target_temperature.
- Added LuaForce::get_saved_technology_progress() and set_saved_technology_progress().
- Added LuaFluidPrototype::gas_temperature read.

## 0.15.12

Date: 18. 05. 2017

### Changes

- Zooming with the mouse wheel in the map and zoom-to-world is less aggressive.
- Fast entity transfer by dragging (ctrl + clicking and dragging) will remember if you're trying to insert or extract items.
- Changed the deconstruction planner "trees only" filter to "trees/rocks only".
- Lab speed info in the description contains the researched speed bonus as well.
- Sprite quality defaults to High when at least 2.7 GB VRAM is detected (instead of 1.7 GB).
- Video memory usage defaults to All when at least 1.5 GB VRAM is detected (instead of 0.8 GB).

### Bugfixes

- The statistics window (electric/production/kills) will automatically move to avoid being partially offscreen. ( more )
- Fixed that keypad /*-+, enter and delete were not usable in the text boxes if assigned in the controls.
- Fixed that power poles could be built at any distance by exploiting click-and-drag. ( more )
- Fixed marking underground belt output for deconstruction wouldn't block input from pushing more items into the underground part. ( more )
- Fixed "Read Stopped Train" checkbox not showing the correct value. ( more )
- Fixed entities with a burner energy source would show the incorrect power consumption. ( more )
- Fixed that production achievements could not be obtained. ( more )
- Fixed that some achievements (raining bullets, logistic network embargo, maybe more) were not properly marked as gained. ( more )
- Show the productivity bonus on mining drills even when they have no other effects on them. ( more )
- Fixed some GUI shortcuts not working when colliding with other shortcuts. ( more )
- Fixed that electric network visualisation on chart showed electric poles from other surfaces. ( more )
- Fixed that non-ASCII input wasn't possible on Linux. ( more )
- Fixed error when loading a save containing a folder which contained only subfolders but no files. ( more )
- Fixed swinging axe as attack might spawn mining particles of a nearby tree or resource patch. ( more )
- Fixed that signals built by robots on places that didn't match the suggested direction didn't connect. This caused that some otherwise correct blueprints required manual intervention to fix the signals. ( more )
- Fixed handling of X11 focus events. ( more )
- Fixed trains wouldn't leave disabled stations when the next station in the schedule was the same station. ( more )
- Fixed train stops wouldn't import as string correctly. ( more )
- Fixed requester chests would render numbers larger than 2,147,483,647 as negative values. ( more )
- Fixed logging in with email in updater set your username to your email. ( more )

### Modding

- Fixed that electric boiler didn't work. ( more )
- Fixed int mod setting error display message didn't show the upper limit correctly. ( more )

### Scripting

- Fixed cloning blueprint books wouldn't copy the label/active index. ( more )
- Fixed that inoperable entities couldn't be rotated even when rotatable was true. ( more )
- Changed LuaItemStack::trees_only to trees_and_rocks_only.
- Added LuaEntity::loader_type write.
- Added LuaFlowStatistics::on_flow() .
- Fixed lua documentation for DeciderCombinatorParameters and CircuitCondition. ( more )
- Fixed passing invalid arguments to LuaGame::take_screenshot would cause desync. ( more )

## 0.15.11

Date: 16. 05. 2017

### Minor Features

- When a train is stopped at the train stop, a circuit network signal is sent with a unique number for that train. ( more )

### Changes

- Added headless server option --server-id to allow specifying custom path to the server ID file.
- Increased the minimum custom UI scale from 50% to 80% to avoid some scaling issues.
- The zoom level at which the map switches from 'map view' to 'world view' was increased.
- The first level of infinite researches is not needed for the tech maniac achievement anymore.
- The game will default to low sprite quality on computers with less than 2.5GB RAM. ( more )
- Tweaked the rocket launch gui. It doesn't show the result inventory slot when it is empty to avoid confusion when people put the satellite in it.
- Removed the zoom-to-world-outside-coverage debug option because it was causing issues. ( more )
- Added "create specialized sprite atlases" option to graphics settings. If checked, tile and shadow sprites won't be put into separated sprite atlases instead of the main one. This should give graphics driver more room to fit required sprites to graphics memory.
- Added "atlas texture size" option to graphics settings. Larger atlas texture can fit more sprites into single atlas which reduces CPU load when rendering. But smaller atlases are more likely to fit into VRAM and reduce GPU load when rendering.

### Bugfixes

- Fixed nuclear reactor and centrifuge were not placed into toolbelt automatically. ( more )
- Tweaked the way heat pipes work, mainly to make it work the same regardless order of build. ( more )
- Fixed that click-and-drag interaction logic didn't work for trains. ( more )
- Another attempt to fix the ranged-based research info in the technology icon.
- Fixed that not all items were cleared in the transport belt madness campaign. ( more )
- Fixed that browse games table was inconsistent after resizing. ( more )
- Achievements should no longer be unlocked when replaying a game. ( more )
- Updated supply challenge level requirements. ( more )
- Fixed fluids consumed/produced by boilers didn't show in the production stats. ( more )
- Fixed that pasting very large strings wouldn't work on Linux. ( more )
- Fixed naming convention of transport belt madness campaign levels. ( more )
- Fixed copy-paste with containers so they correctly copy the inventory size limit. ( more )
- Fixed the progress bars in the lab wouldn't show correctly in some cases. ( more )
- Achievements are no longer be unlocked when replaying a game. ( more )
- Achievements are no longer unlocked by playing multiplayer game in which the player spent less than 50% of time online.
- Fixed that the blueprint renaming text box would close every time crafting finished. ( more )
- core/backers.json is now included in the core data crc. This means that different content of this file will be properly detected when joining multiplayer game.
- Fixed that loader filters were not saved in the blueprint string. ( more )
- Gas color is now tinted with the fluids 'flow_color'. ( more )
- Fix wave defense crash when a silo died while nobody was connected. ( more )
- Fixed that the "confirm and download" button in the sync-mods-with-save wouldn't restart the game once all mods were downloaded. ( more )
- Fixed construction robots could get stuck trying to repair curved rail forever. ( more )
- Fixed that the technology cost tooltip description wouldn't scale correctly. ( more )
- Fixed that the /help command when run from the server console would always output the server commands list. ( more )
- Fixed strange behavior when a train has the same station in the list multiple times with no other valid station. ( more )
- Fixed crash related to dying with some GUI open. ( more )
- Fixed rail signals getting stuck reserved when mining/building rails in some setups. ( more )
- Fixed desync when pumps are setup to pump into the output of an assembling machine. ( more )
- Fixed the final level of formula based research would show the wrong name when researched.
- Fixed crash when maximizing the game with the achievements window open. ( more )
- Fixed switching weapons while firing in the tank would keep playing the previous weapon sound. ( more )
- The productivity value in the  miner description now contains also the researched bonus.
- Fixed insert sending a signal twice during fast replace. ( more )
- Fixed crash that would sometimes happen when a player left whilst some other player was in the process of joining. ( more )
- Fixed hazard concrete item description. ( more )
- Fixed that some of the slider in the new game settings weren't controllable by scrollbar.
- Fixed recipes with long names would extend out of the tooltip GUI. ( more )
- Fixed keyboard input would be blocked in tutorial, if console was opened when entering the tutorial. ( more )
- Fixed robots could deliver the wrong number of modules during roboport blackouts. ( more )
- Fixed that the game would freeze if there was no valid place to drop items on limited size maps. ( more )
- Fixed fire wouldn't pollute in some cases. ( more )
- Fixed that the delete-blueprint button would show when it wouldn't actually work. ( more )
- Fixed an error when resource scaling results in amounts too large to store in a resource entity. ( more )

### Modding

- Fixed generator power output was always based on heat capacity and default temperature of water. ( more )
- Fixed logistic and construction radius visualization sprites would ignore tint. ( more )

### Scripting

- Fixed setting technology::researched wouldn't research all levels of a formula based technology. ( more )
- Fixed it was possible to add gui element with same to the same parent name more than once. ( more )
- Fixed the custom camera widget wouldn't render the correct entities when switching the surface it was rendering for. ( more )
- Fixed LuaTrain::schedule would allow an invalid current schedule record. ( more )
- Added LuaEntityPrototype::mining_speed , mining_power, energy_usage, max_energy_usage, normal_resource_amount, infinite_depletion_resource_amount, attack_parameters read.
- Added LuaLampControlBehavior::color read.
- Added LuaRailSignalControlBehavior::red_signal , orange_signal, green_signal, close_signal, read_signal, circuit_condition read/write.
- Added LuaEntityPrototype::mineable_properties fluid_amount, required_fluid, mining_trigger, effectivity, consumption, friction_force, braking_force, tank_driving, rotation_speed, turret_rotation_speed, guns, speed, speed_multiplier_when_out_of_energy, max_payload_size, energy_per_move, energy_per_tick, max_energy, min_to_charge, max_to_charge properties, and building_grid_bit_shift.
- Added LuaBurner::fuel_category read.
- Added LuaBurnerPrototype.
- Added LuaControl::mine_entity() .
- Added LuaEntity::text read/write.
- Added read/write support for flying text color through LuaEntity::color .
- Added LuaTrain::get_fluid_count() , get_fluid_contents(), remove_fluid(), insert_fluid(), and clear_fluids_inside().
- Added LuaGameScript::check_prototype_translations() - a way to check if all expected prototypes have valid translations.
- Changed LuaEntityPrototype::mineable_properties "miningtime" -> "mining_time" and "miningparticle" -> "mining_particle".

## 0.15.10

Date: 10. 05. 2017

### Changes

- Added rail block debug visualization.
- Increased maximum wire distance of all circuit connectable entities from 7.5 to 9.
- Steam is now internally a separate fluid from hot water.
- Coal liquefaction recipe now requires steam instead of water.
- Terrain, shadow and smoke sprites are sorted into separate sprite atlases in attempt to optimize GPU memory access during rendering.

### Graphics

- Added burner mining drill in high resolution and replaced the normal resolution version.

### Bugfixes

- Fixed speed-module-3 recipe typo. ( more )
- Fixed downgrading underground belts by fast replace would not work for even if output piece was close enough. ( more )
- Fixed that robots trying to repair each other wouldn't work correctly. ( more )
- More understandable description current level of technologies that have multiple levels merged into one slot in the technology gui.
- Fixed crash that would happen when loading old modded saves in vanilla Factorio. ( more )
- Fixed that it wasn't possible to fast-transfer blueprints to other players. ( more )
- Fixed that hitting rocks with vehicles made no sound. ( more )
- Fixed blueprint preview icons scaling and size to be consistent across all places they're shown. ( more )
- Fixed that you couldn't delete blueprints from your trash slots. ( more )
- Fixed that storage tanks used 4 directions although visually only showed 2 so they would conflict in blueprints. ( more )
- Fixed crash when loading blueprint storage while also migrating save files. ( more )
- Fixed a useless error when locale isn't correct for a scenario. ( more )
- Fixed possible desync related to inserter circuit network stack size control.
- Fixed that multiple passengers in a train could result in erratic behavior when trying to drive. ( more )
- Fixed that manually inserting the satellite into the silo when auto-launch is enabled wouldn't launch the rocket. ( more )
- Fixed crash when killing yourself with your own weapon. ( more )
- Fixed F12 might freeze or crash the game. ( more )
- Fixed circuit network controlled rail signal sometimes not going red when building rails. ( more )
- Fixed crash when starting tutorial at the same tick as autosave starts. ( more )
- Fixed that it wasn't possible to scroll the active blueprint in a blueprint book if the scroll bar was visible. ( more )
- Fixed crash when exiting some modded games. ( more )
- Fixed that Factorio wouldn't keep file permissions when saving a map. ( more )
- Fixed that the blueprint library wouldn't remember the player filter after opening a book. ( more )
- Fixed that player names in the blueprint library weren't sorted. ( more )
- Fixed the blueprint book tooltips would flicker when your inventory changed. ( more )
- Fixed desync when catching up.
- Fixed desync when adding/removing blueprints to blueprint books in some cases. ( more )
- Fixed some crashes related to loading invalid combinator parameters. ( more )

### Modding

- The game will now detect when joining a multiplayer game if any mods you're using are broken such that joining the game could result in desynching.
- Fixed that exiting the mod settings GUI without changing anything would incorrectly think you changed settings in some cases. ( more )
- Fixed crash when loading mods control.lua produces an error. ( more )
- Added favourite server icon to utility sprites. ( more )
- Added a global table "mods" - a mapping of mod name to mod version available during the prototype loading stage.

### Scripting

- Fixed some missing Lua docs and added information about the settings stage to the data life cycle. ( more )
- Fixed crash when trying to create stickers on entities that don't support them. ( more )
- Fixed that LuaGuiElement::surface_index was using 0-based indexing. ( more )
- Fixed that LuaEntity::graphics_variation was using 0-based indexing. ( more )
- Fixed that LuaItemStack::active_index was using 0-based indexing. ( more )
- Fixed rendering of layered icons in custom GUI. ( more )
- Added "item" and "tags" to the robot built entity/tile events.
- Added LuaEquipment::burner read.
- Added LuaEntityPrototype::crafting_categories read.
- Added support for setting 'tags' and 'custom_description' when making items through Lua.
- Added LuaBurner::burnt_result_inventory read.
- Added LuaInserterControlBehavior stack size read/write.
- Added LuaTrainStopControlBehavior enable/disable conditions.
- Added LuaTransportBeltControlBehavior enable_disable, read_contents, read_contents_mode read/write.
- Added LuaTrain::id read.
- Added LuaEntityPrototype::supply_area_distance read.
- Added LuaEntityPrototype::max_wire_distance read.
- Added LuaEntityPrototype::max_circuit_wire_distance read.

## 0.15.9

Date: 05. 05. 2017

### Bugfixes

- Fixed crash when opening the train GUI while in the train.

## 0.15.8

Date: 05. 05. 2017

### Changes

- New Supply challenge map.
- Circuit network-based inserter stack size overrides now take effect immediately instead of waiting until the inserter has moved something.

### Bugfixes

- Show 0.7% in the uranium processing recipe instead of 0.0 for uranium 235. This generally works for any recipe that gives less than 1 of anything.
- Don't draw player names on the map that is not in range of player or radar on the zoomed in map.
- Fix some ores with negative values in Tight spot level 04. ( more )
- Fixed inserters couldn't insert fuel into locomotives. ( more )
- Fixed random inaccessible map area in Beta campaign level 04. ( more )
- Fixed various inserter GUI bugs. ( more )
- Fixed train station tutorial relied on specific train schedule state. ( more )

### Balancing

- Changed iron gear wheel price of fast and underground belt from 20->40 and 40->80 to even out the bigger length.
- Fix that biters would sometimes stop and go to sleep during an attack. ( more )

## 0.15.7

Date: 05. 05. 2017

### Balancing

- Changed production science pack recipe to require assembling machine 1 instead of pumpjack.
- Changed science pack 3 to require electric mining drill instead of assembling machine 1.
- Changed crafting times: Oil refinery 20->10 Pumpjack 10->5 Chemical plant 10->5 Lab 5->3 Roboport 15->10
- Reduced the mining time of the storage tank from 3 seconds to 1.5 seconds.
- Increased the mining time of the reactor from 0.5 seconds to 1.5 seconds.
- Increased the underground belt length (basic, fast, express) from 5,5,5 to  5,7,9.

### Changes

- When a connection is refused the username is included in the log message. ( more )
- Copying entity settings from a disconnected entity will no longer disconnect circuit wires. ( more )
- Trains in manual mode now have twice the penalty and trains in manual mode without a player in them have 2.5 times the penalty.
- Reactors produce used up fuel cell when it is completely consumed instead of at start. ( more )
- Reverted flamethrower turret liquid consumption change from 0.15.5. Instead of 30/s it will use 3/s.
- Flamethrower turret no longer shoots in its prepare state. ( more )
- /color command defaults alpha (the 4th parameter) to 255 (instead of 0) if not specified. ( more )
- Reduced default requester chest paste multiplier for nuclear reactor recipe to 1 and for centrifuge recipe to 2. ( more )
- Inserters will no longer take fuel from locomotives and instead will take the burnt result items if the locomotive fuel uses that system.

### Bugfixes

- Fixed that clicking locomotive from zoomed in map view would change color (and show fuel) for some other locomotive on the train ( more )
- Fixed that construction bots could repair vehicles from very far. ( more )
- Fixed that rocket silo or other GUIs would obscure finished-game dialog. ( more )
- Fixed that boiler could output a different fluid than its input. ( more )
- Fixed that the inserter would sometimes report bad values to the circuit network. ( more )
- Fixed pump recipe description having wrong pumping speed. ( more )
- Fixed wrong error message when loaded headless save file doesn't exist ( more )
- Fixed the "Input action fragment is missing" crash that would sometimes happen due to packet loss. ( more )
- Fixed crash when resizing the game window while having an assembling machine level 1 GUI open. ( more )
- Fixed alternative zoom controls would do nothing in map editor. ( more )
- Fixed some cargo wagon spritesheets were offset by 1 frame. ( more )
- Fixed that it was hard/not possible to select the character corpse over some entities. ( more )
- Fixed that the blueprint book GUI would scroll to the top after every click. ( more )
- Fixed crash when trying to disconnect non circuit connectible entities using Lua::Entity ::disconnect_neighbour. ( more )
- Fixed that calling Lua::Entity ::disconnect_neighbour would sometimes disconnect more wires than it should.
- Fixed mod settings corruption when removing mods that contained mod settings. Note: this will reset all mod settings. ( more )
- Fixed inconsistent selection of resource patches on the map. ( more )
- Fixed GUI sizing when resetting mod settings. ( more )
- Fixed that the blueprint book GUI would scroll to the top after every click. ( more )
- Fixed that dropping a blueprint onto a book icon in the library GUI would drop it in the top level instead. ( more )
- Fixed that the blueprint library would sometimes stop opening books. ( more )
- Fixed GUI scaling problems with the assembling machine GUI. ( more )
- Fixed desync related to the on_selected_entity_changed event. ( more )
- Fixed that the atomic bomb shooting speed cooldown didn't work. ( more )
- Fixed the constant combinator GUI when the constant combinator name was larger than the rest of the GUI. ( more )
- Fixed that the reactor didn't show fuel in the description. ( more )
- Fixed making blueprints of requester chests with "set requests" would copy the current requests into the blueprint. ( more )
- Fixed that deleting saves with the delete key key wouldn't maintain focus on the saves list. ( more )
- Fixed crash when mining rails while having the "show rail paths" debug option enabled. ( more )
- Fixed infinite loop when migrating entities from an unrelated type to a roboport type. ( more )
- Fixed that the technology multiplier didn't apply on infinite research. ( more )
- Fixed filtering server list for games with mods. ( more )
- Fixed mod version checking for automatic mod download. ( more )
- Fixed flamethrower turret would not shoot last single shot worth of liquid. ( more )
- Fixed crash when exiting server list ( more )
- Fixed "Right mouse button to open" in opened armor. ( more )
- Fixed that the blueprint library wouldn't use scroll bars for shared blueprint books. ( more )
- Fixed that resource patches in unexplored areas could be examined on the map.
- Fixed rail ghosts could not be placed over ghosts of enemy force. ( more )
- Fixed the sulfuric acid fluid icon. ( more )
- Fixed that /config set password wouldn't work. ( more )

### Modding

- Icons are now required to have correct size (which can be overridden by icon_size property). ( more )
- 32x32px for entity, fluid, item, item-group, recipe, technology, virtual-signal
- 128x128px for achievement, tutorial
- If icon path references base mod, technology icon is expected to be 128x128px and item-group icon 64x64px.
- In near future, we may remove default sizes and require icon_size to be always specified.
- It is no longer possible to teleport any rolling stock or train stop. ( more )
- Added the string mod setting prototype property "auto_trim" defaulting to false.

### Scripting

- Fixed LuaChunkIterator could become invalid and crash the game if used. ( more )
- Added LuaPlayer::mod_settings read - the runtime player mod settings for the given player.
- Added LuaEntity::temperature read/write - the temperature of entities that use the heat energy source type as well as reactors and heat pipes.
- Added LuaEntity::get_burnt_result_inventory .

## 0.15.6

Date: 02. 05. 2017

### Changes

- Increased roboport construction range to 55 (110x110 area) to make roboports able to build each other without interconnecting their logistic areas, and not break when there are obstacles like trees or rocks.

### Bugfixes

- Fixed centrifuge glowing for one frame each time inserter drops something. ( more )
- Fixed biters expansion was biased towards northern part of the map. ( more )
- Fixed blueprint preview splitter not bending nearby belts correctly. ( more )
- Fixed items on ground were not cleared in tightspot campaign. ( more )
- Fixed that mining drills wouldn't pull in enough acid to continue mining. ( more )
- Fixed that you could complete some advanced signal tutorial stages by blocking trains. ( more )
- Fixed that nuclear fuel reprocessing was used to calculate raw ingredient requirements. ( more )
- Fixed that you could input invalid value to PvP config. ( more )
- Fixed crash when changing force of turret ghost. ( more )
- Fixed inserters would grab items off belts and try to drop them onto rails after the train left. ( more )
- Fixed inserters would rest with their hand above the center of a splitter. ( more )
- Fixed desync caused by heat pipes. ( more )
- Fixed crash when trying to edit mod settings after joining a paused multiplayer game. ( more )
- Fixed removed decoratives were migrated as big-ship-wreck-grass instead of being deleted from map. ( more )
- Fixed input underground belt fast replace would also replace output piece even if input changed direction. ( more )
- Fixed combinators continuing to output signals when parameters are cleared or when disconnecting feedback wire. ( more )
- Fixed programmable speaker continuing to make sounds without a wire connected. ( more )
- Fixed that it wasn't possible to scroll with the mouse wheel in the mod settings GUI. ( more )
- Fixed updater would fail if Factorio was in folder with name containing non-English characters. ( more )

## 0.15.5

Date: 30. 04. 2017

### Bugfixes

- Fixed crash when setting character trash slots through script while having the character GUI opened. ( more )
- Fixed crash on joining a multiplayer game if the "use different mod settings per save" was disabled. ( more )
- Fixed blueprint with roboports wouldn't draw roboport connections. ( more )
- Fixed crash when building rails in specific setups while trains are reserving signals on the rails being changed. ( more )
- Fixed when changing graphical variation of a tree from script or in map editor. ( more )
- Fixed flamethrower turret was using 10x less fluid than it should.
- Fixed opening item GUI wasn't rebindable ( more )
- Fixed burner inserters would try to fuel themselves with fuel they couldn't use. ( more )
- Fixed crash when deleting chunks in some instances. ( more )
- Fixed one direction of hazard concrete had no walking sounds. ( more )
- Fixed rare crash when getting killed by the locomotive you had opened. ( more )
- Fixed that right clicking the map view buttons would change the option but not update the button. ( more )
- Fixed the generate-map settings wouldn't be saved when switching to the mod-settings through the generate map GUI. ( more )
- Fixed crash when interacting with the map view buttons in some cases. ( more )
- Fixed crash when mousing over entities in some rare cases. ( more )
- Fixed crash when trying to mine tiles from the zoomed-to-world view. ( more )
- Fixed crash when editing speaker parameters in the map editor. ( more )
- Fixed that train stops wouldn't show the correct name when changed remotely. ( more )
- Fixed crashes related to electric pole/accumulator removal when migrating saves from 0.14 into 0.15. ( more )
- Fixed rail signals built by robots would frequently lead to the signals not connecting properly. ( more )
- Fixed GUI layout problems in the rocket silo GUI when adding/removing productivity modules. ( more )
- Fixed items on belt flickering when occupying same position. ( more )

### Scripting

- Fixed module inventory insert() didn't work for assembling machines. ( more )

## 0.15.4

Date: 29. 04. 2017

### Changes

- Added /permissions reset to reset all permissions to default.
- Steam and water content of fluid wagons are now shown separately in locomotive tooltip.
- Removed the "minimum chunks between new bases" map generation setting because it wasn't doing anything.
- Re-added custom /color support through /color r g b a.
- PvP: Added a biter easing option to prevent excessively large bases close to team starting areas.

### Bugfixes

- Fixed crash when building rails while a train is currently reserving some of the signals. ( more )
- Fixed that you could set the inserter stack size over the researched maximum by sending negative numbers with the circuit network. ( more )
- Fixed combinators continuing to output signals after disconnecting the input. ( more )
- Fixed blueprint would reference force it was created on and crash in rendering if that force no longer existed. ( more )
- Fixed that names of books stored in the blueprint library wouldn't be preserved after save and load. ( more )
- Fixed supply scenario would sometimes show the next level button in error. ( more )
- Fixed the rocket silo wouldn't copy the "auto-launch" option in blueprints.
- Fixed Sulfuric Acid recipe using 10 times less water. ( more )
- Fixed that dropping blueprints into a book inside the library would sometimes drop the wrong blueprint. ( more )
- Fixed crash when changing mod settings runtime while in a multiplayer game. ( more )
- Fixed that opening the blueprint library after calling game.remove_offline_players() would crash the game. ( more )
- Fixed that --start-server wouldn't find the save file when given just a name without the .zip suffix. ( more )
- Fixed that it was possible to export a blueprint book into another blueprint book. ( more )
- Fixed that it was possible to have the same blueprint multiple times in the library. ( more )
- Fixed that it was possible to grab a blueprint from the library whilst also holding a deconstruction planner in hand. ( more )
- Fixed desync when moving mouse over areas outside of radar range in zoomed-to-world view. ( more )
- Fixed crash when leaving the technology price multiplier blank. ( more )
- Fixed crash when removing modded rails during save migration. ( more )
- Fixed lab without power would be still rendered as active. ( more )
- Fixed several instances of the "last user" field not getting updated. ( more )
- Fixed rocket silo would not increment its "products finished" count when finishing rocket. ( more )
- Fixed landmines would last forever when friendly fire was disabled. ( more )
- Fixed possible crash when closing Factorio during loading. ( more )

### Modding

- Blueprints/books/deconstruction item prototypes with the "hidden" flag will no longer show up in the blueprint library. ( more )
- Added missing lua docs index section for settings and fixed some wording. ( more )

### Scripting

- Fixed assigning invalid index to LuaEntity::graphics_variation would cause crash. ( more )
- Fixed setting LuaItemStack::blueprint_icons didn't work correctly. ( more )
- Fixed teleporting entity with rectangular bounding box would reset bounding box to north orientation and cause desync. ( more )
- Added LuaEntity::products_finished for crafting machines.

## 0.15.3

Date: 27. 04. 2017

### Changes

- Wave defense: Units won't spawn if there are more than 500 already on the map.
- Wave defense: Added a 'Unit bounty bonus' upgrade.
- Removed the ability to set /color using RGB values.
- Wave defense: Added Uranium to the map.
- "Disable all mods" option in mod load error dialog doesn't disable base mod anymore.
- Changed stack-split so "splitting" a stack of 1 still transfers the 1 item. ( more )
- Change submachine stack size to 5. ( more )
- Blueprints, blueprint books and deconstruction planners can be destroyed by clicking the trash can icon in their GUIs. Clearing a blueprint is still possible via the Shift+Right Click shortcut.

### Bugfixes

- Fixed the fluid usage description for the steam engine would flicker when holding the steam engine in the cursor. ( more )
- Fixed that assembling machines would think the fluid barreling/unbarreling recipes could be used to calculate base ingredients for recipes. ( more )
- Fixed performance problems when opening the blueprint library GUI when the map has a large number of players. ( more )
- Fixed crash related to connection attempts from players with mods with mod settings. ( more )
- Fixed getting "No map setting instance" error when loading faulty mod instead of actual error. ( more )
- Fixed entering tutorial would remove scenario control script from current game. ( more )
- Fixed crashes related to saves with migrated circuit network signals. ( more )
- Fixed numeric inputs would block all keys instead of just numbers. ( more )
- Fixed ore field amount stuck to cursor when in technology view. ( more )
- Fixed crashes related to migrated saves with circuit network signals. ( more )( more )
- Fixed that train station tutorial would not progress if you removed the train wait condition. ( more )
- Fixed crash when changing mod setting prototype types. ( more )
- Fixed the refinery flame would freeze when using the coal liquefaction recipe and the machine didn't have any coal. ( more )
- Fixed fluids would be counted incorrectly for production stats when a pumpjack was placed on an oil well with a modded extremely high yield. ( more )
- Fixed the trains GUI wouldn't scale correctly. ( more )
- Fixed you could select entities in the zoomed-to-world view outside radar coverage. ( more )
- Fixed prompt about disabled base mod would not show up. ( more )
- Fixed crash when train was destroyed while hovering over it in map view. ( more )
- Fixed that the team production starting lobby had some uranium ore. ( more )
- Fixed hovering over very large resource patch in map view would crash the game. ( more )
- Fixed the "don't mine resources if mining starts with non-resources" logic. ( more )
- Fixed crash when the preview picture can't be saved for a save file. ( more )
- Fixed crash when trying to filter opened other players quick bars. ( more )
- Fixed crash when setting resource minimal yield above the normal yield. ( more )
- Fixed the tab complete logic for the /mute-programmable-speaker command. ( more )
- Fixed that you could only build blueprints in the zoom-to-world by click and drag.
- Fixed script error in basic train tutorial. ( more )
- Removed redundant recipe unlock in trash slot technology. ( more )
- Fixed inserter stack size override sometimes being lost when importing a blueprint.
- Fixed crash that would occasionally happen after deleting a book from the blueprint library. ( more )
- Fixed fluid could flow into the heat exchangers output fluidbox. ( more )
- Fixed that inserters would try to put stuff into the rocket silo result inventory. ( more )
- Fixed some invalid map exchange strings would crash the game. ( more )
- Fixed train stop would not output content fluid wagons to circuit network. ( more )
- Fixed locomotive tooltip would not show contents of fluid wagons. ( more )

### Modding

- Prototype names are not allowed to contain the '.' character.

### Scripting

- Fixed typo in defines.shooting.shooting_selected (was "shooting_seleted"). ( more )
- Fixed type in defines.control_behavior.type.train_stop (was "train-stop"). ( more )
- Fixed the custom camera widget was using 0 based indexing for the surface_index parameter. ( more )
- Added missing control behavior types to defines (wall, mining_drill, programmable_speaker). ( more )
- Added LuaTrain::fluid_wagons read.

## 0.15.2

Date: 25. 04. 2017

### Changes

- Reduced wave defense biter power increase as more players join to reduce pathfinding performance drain. ( more )
- Tweaked the biter and uranium ore settings of the 'Rail world' preset.
- Changed mining drill fluidbox to allow fluid to flow to pipes without the use of pumps.
- Changed the "sync mods with save" button to support disabling mods a save file wasn't using.
- Computers with 2GB or more video memory and 8GB or more RAM will default graphics quality to high.
- Selecting high sprite quality in graphics options will show warning if computer doesn't have enough video memory.

### Bugfixes

- Fixed tightspot campaign debt calculation. ( more )
- Fixed basic train tutorial rail setting offset. ( more )
- Fixed story script copying of assembling machines without recipes. ( more )
- Fixed crash when cycling through empty blueprint book. ( more )
- Fixed crash when the wrong fuel type was put into a burner equipment. ( more )
- Fixed LuaFluidBox::get_capacity() didn't work when the fluidbox was empty. ( more )
- Fixed LuaFluidBox::get_capacity() used 0-based indexing. ( more )
- Fixed blueprints with circuit wires would crash in some instances.
- Fixed the map would render black if the game was resized immediately after loading a large save file.
- Fixed that the technology cost multiplier allowed a value of 0.
- Fixed crash when circuit connector sprites aren't defined for a given entity. ( more )
- Fixed crash when inactive mining drills are disconnected from the circuit network. ( more )
- Fixed that the programmable speaker wouldn't save settings correctly when exported as a string in blueprints. ( more )
- Fixed crash when the base mod is disabled and no other mod defines map-settings. ( more )
- Fixed fluids consumed in the mining drill for mining resources didn't get counted in fluid production statistics. ( more )
- Fixed crash after display reset when browse multiplayer GUI was opened. ( more )
- Fixed browse games GUI sorting. ( more )
- Fixed wave defense GUI error. ( more )
- Fixed transport belt walking sound being controlled by the wrong volume slider. ( more )
- Fixed exiting tutorial would mute game sounds. ( more )
- Fixed crash when hovering over train with invalid path. ( more )
- The "Kovarex enrichment process" is no longer usable with productivity modules. ( more )
- Fixed alternative zoom would cause crash when bound to keyboard instead of mouse. ( more )
- Fixed that train stop would output circuit network signals with train contents regardless of it's parameters.
- Fixed possible desync related to train stops connected to circuit network.
- Fixed the exchange string wouldn't get cleared when clicking the reset button in the generate map GUI. ( more )
- Fixed crash when executing commands ban/unban/bans in a single player game. ( more )
- Fixed that opening another player's blueprint book though the /open command would crash the game. ( more )
- Fixed possible desync related to constant combinator filters.
- Fixed tooltip delay option didn't work. ( more )
- Fixed that disconnecting of electric poles hid some of the electric network visualizations on the map. ( more )
- Fixed crash when closing window on splash screen. ( more )
- Fixed that steam wouldn't show up as steam in fluid wagons. ( more )
- Fixed inactivity wait condition didn't work properly with fluid wagon. ( more )
- Fixed name of train field in on_train_created event. ( more )
- Fixed the technology list scrollbar position reset after clicking any technology.
- Fixed that LuaFluidBox would ignore the temperature field when setting a new fluid. ( more )
- Fixed crash when using recipes in furnaces that don't produce the exact amount of output items as the furnace output slots. ( more )
- Fixed crash when loading some older save files in 0.15 related to modded recipes. ( more )
- Fixed crash due to "Construction robot is in invalid state". ( more )
- Fixed game hang when connecting train in a loop ( more )

## 0.15.1

Date: 24. 04. 2017

### Changes

- Reduced noise effect on zoom-to-world view.

### Bugfixes

- Fixed update error.
- Fixed Steam config loading error.
- Fixed headless not starting without server-settings.json ( more )
- Fixed the "reset" button in the generate map GUI wouldn't reset settings to the actual default values. ( more )
- Fixed that right clicking icon in the tag edit gui crashed the game. ( more )

## 0.15.0

Date: 24. 04. 2017

### Major Features

- Research overhaul. 4 new science packs: Military, Production, High-tech and space. Space science packs are generating by launching a rocket. Added infinite researches.
- Nuclear power.
- Blueprint library: Allows for keeping players blueprints between individual game saves and allows sharing blueprints in multiplayer games.
- Added infinite mining productivity research, each tier increases mining productivity by 2%.
- Added wagon for transporting fluids. One side of pump can connect to the fluid wagon, the other side has to be connected to something else.
- Mini tutorials. Small missions that explain some of the game mechanics. The current content is a testing sample and it only covers trains. Features:
- Map Interaction improvements: Selectable map overlays: logistics networks, pollution, electric network, turret range, etc. Train stations and trains can be opened by clicking them while in the map view. Zoom to the world view from the map. It only shows parts of the map covered by radar or other players though. Custom map markers can be added by the players.
- When dying in multiplayer you leave behind a body with your items that slowly degrades.
- Fuel type now affects vehicle acceleration and top speed.
- Added coal liquefaction oil processing recipe.
- Added Pipette Tool. Picks up items from your inventory used to build the currently selected entity. For resources it will select the fastest available resource extractor.
- New scenarios: PvP and Wave defense.

### Minor Features

- Added map-settings command line option when creating map, it can be used to specify a file with map settings to be  used instead of the defaults.
- Added preset command line option when creating map.
- Fast in game interactions like fast inserting into/from entity and copy paste can be done by dragging instead of having to click one at a time.
- Build-by-moving for electric poles now accounts for covering all unpowered entities on the way.
- Fast replacing input piece of underground belt will also fast replace output piece if possible.
- Added support for setting player color from the /color command using Lua syntax: {r=...g=...,b=...,a=...}
- Added warning for situation when robots don't have storage place to put items in the logistics network.
- Pumps show their direction in the detailed view.
- Belts and pipes show correct connections when building a blueprint.
- Technologies show the required science packs below the icons in the technology GUI list.
- Technologies are sorted by the science packs needed.
- Added /screenshot command - takes a screenshot of your current game screen.
- Added support for equipment grids in the map editor.
- The build rotation of each blueprint is remembered independently of the general item build rotation.
- Infinite resource minimal yield is calculated using the initial resource amount and the prototype minimum yield.
- Added optional filters to the deconstruction planner.
- Copying from assembling machines to filter inserters will set the filters to the ingredients of the assembling machine recipe.
- Combat robots and construction robots are maintained between sessions in multiplayer and when changing surfaces.
- Added reverse-rotate.
- Offshore pump and generator show pumping speed/fluid usage.
- Alternative select with blueprints (shift + select) skips the blueprint setup GUI.
- Mining rails is disabled if mining starts with trains or gates.
- Toggle fullscreen using Alt + Enter.
- Added "f"/"force" option to the /players command
- Added Logistic networks GUI containing a list of all networks and contents with search (opened by the L key).
- Added /open command - opens another players inventory if you're an admin.
- Added /alerts command - configures alerts for your player.
- Added /mute-programmable-speaker command - disables global sounds created by the Programmable Speaker entity.
- Added /seed command - prints the map seed.
- Added fluids to the production GUI.
- Added kill statistics GUI.
- Added enable/disable all mods button to the mod manager GUI.
- Added automatic barreling support for all fluids.
- Cargo wagons can have settings copied from any distance like Locomotives.
- Added the ability to auto-launch the rocket.
- Train stops can be colored like trains.
- Fish can be collected by robots.
- Extended map generator settings to include an advanced section.
- Added map generator presets.
- Show fog-of-war and radar radius when holding radar in cursor.
- Seed for map creation on the headless server can be specified via map-gen-settings.json
- Damaged items merge into one stack, the health of the stack will be the average of the items.
- Added server whitelist support -- see the /whitelist console command.
- Added /banlist command to operate on the banlist, in addition to the pre-existing /ban and /unban commands.
- Added "favourite" feature in public games list: Keep your favourite servers at the top of the list.
- Added /permissions command for managing permissions in a multiplayer game.
- Added ability to change individual inserter stack size bonuses through GUI or the circuit network.
- Added ability to export and import blueprints, blueprint books, and deconstruction planners as strings.
- Server console will print JOIN and LEAVE messages for players joining or leaving.
- Server console messages that aren't a part of the main log can be logged separately by running the server with the --console-log option.
- Translatable energy units and SI prefixes (eg. "100 ГВт").
- Furnaces and assembling machines show the amount of products finished.

### Graphics

- Added high graphics quality option. In this settings the following list of things will have double resolution: Car, Trains, Rails, Rail signals, Train stop, Transport belts, Underground belts, Splitters, Pipes, Steam engine, Assembling machines, Oil refinery, Chemical plant, Mining drill, Furnaces, Resources
- New ore graphics that makes the ore patches look less tiled.
- Tweaked the GUI graphics.
- Decreased the size of the recipe icons on assembling machine by 23%.

### Balancing

- Increased the rate at which resources grow with distance from the center by 50%.
- Crude oil balancing: Halved the resource amount on the map Increased the minimum yield from 10% to 20% Halved the rate of depletion. Doubled the starting yield. Fixed that the mechanics of increasing richness with distance from start wasn't working for crude oil.
- Increased module inventory size of Chemical plant and oil refinery from 2 to 3.
- Increased logistic slot/trash slot count from 5 per level to 6 per level.
- Removed processing unit from the modular armor and portable solar panel recipe.
- Increased the pump pumping speed 4 times.
- Reduced the plastic bar recipe requirement of petroleum gas 30 -> 20
- Reduced the electric engine recipe requirement of lubricant 20 -> 15
- Reduced the electric furnace recipe requirement of steel 15 -> 10
- Reduced the steel furnace recipe requirement of steel 8 -> 6
- Reduced the pumpjack recipe requirement of steel 10 -> 5
- Reduced crafting time: Engine unit + electric engine unit: 20 -> 10 Pumpjack 10 -> 8 Advanced circuit 8 -> 6 Processing unit 15 -> 10 Cracking recipes 5 -> 3
- Increased stack size of stone wall pipe and belts 50 -> 100
- Increased the maximum power production of steam engine from 510kW to 900kW
- Doubled the heat capacity of water from 0.1kJ per degree per liter to 0.2kJ.
- Increased the substation supply area (16X16 to 18X18) and wire reach (16 to 18). Combat Balancing:
- Player regains health at a much higher rate, but only after being out of combat for 10 seconds.
- Discharge defense equipment pushes back, stuns and damages nearby enemies when activated by the remote.
- Decreased the size of Discharge defense equipment from 3x3 to 2x2.
- Greatly increased the damage of Personal Laser Defense Equipment.
- Flamethrower gun has a minimum range of 3.
- The flames created on ground from the flamethrower significantly increase in duration and damage when more fuel is added to them by firing at the same spot.
- Increased fire resistance of biter bases.
- Increased the health of player non-combat buildings.
- Increased player health from 100 to 250.
- Increased collected amount and effectiveness of Fish.
- Increased the damage, range and health of biters worms.
- Decreased health and resistance of Behemoth biters.
- Doubled the stack size of all ammos.
- Tweaked the cost and crafting time of some ammos.
- Increased the damage of most player ammos. Greatly increased the damage and fire rate of Rockets and Cannon Shells.
- Increased the collision box of Cannon Shells.
- Increased Tank health and resistances.
- Added research for Tank Cannon Shells damage and shooting speed.
- Tweaked research bonuses and added more end-game research for military upgrades.
- Greatly increased the damage of Mines. They also stun nearby enemies when they explode.
- Added uranium rounds magazine and uranium cannon shells.
- Added flamethrower to the tank.
- Other minor changes.

### Optimisations

- Improved performance of mining drills in general and significantly improved performance when mining drills get backed up.
- Improved performance when tiles are changed due to migration/mod removal.
- Significantly improved GUI performance for inventories that required scroll bars.
- Improved GUI performance in general.
- Improved performance of radars scanning chunks.
- Improved map generation speed and generation algorithm.
- Improved game load performance when a large amount of mod data exists in the save.
- Optimized graph rendering in production statistics window.
- Improved regenerate entity performance.
- Improved network map transfer performance.
- Improved train performance when building/mining rail related entities.
- Optimized memory requirements for storing tiles under concrete.

### Circuit Network

- Significantly improved circuit network performance. Up to 25 times less CPU usage and 10% less memory usage.
- Added the Programmable Speaker: it shows alerts and plays sounds based on circuit network signals. It can be used to make simple songs.
- Train Stop can output the contents of the stopped train's cargo.
- Train Stop can be disabled using the circuit network. Trains will skip disabled Train Stops, allowing simple train control.
- Mining Drills can be turned on and off using the circuit network. They can also output the remaining expected resources.
- Pumpjacks can be turned on and off using the circuit network. They can also output the current oil mining rate.
- Added Modulo, Power, Left Bit Shift, Right Bit Shift, Bitwise AND, Bitwise OR and Bitwise XOR to the Arithmetic Combinator.
- Added >=, <=, != to the Decider Combinator and Circuit Conditions.

### Changes

- Configuration has been reset.
- Boilers are more powerful and bigger and have dedicated output for the steam. Default boilers output steam at the fixed temperature 165.
- Removed support of 32 bit systems.
- Removed alien artifacts and alien science packs from the game completely.
- Changed bounding box of burner mining drills and pumpjack, so it is possible to walk in between them.
- Disabled loading of saves before 0.12.0 version (You can use 0.12 to load older saves and re-save them).
- Changed "small pump" to "pump". Small pumps in old saves will be migrated but they will be misaligned and disconnected from pipes.
- Train station adds 2000 tiles penalty when path finding, so trains try to avoid stations not related to their path.
- The map seed is used to generate unique maps instead of just shifting the starting position.
- The "decorative" entity type has been deprecated and replaced with the prototype type "optimized-decorative".
- Multiplied all fluid amounts by 10.
- All default map editor actions are now on left click.
- Change fluidbox height and base level of boiler, steam engine and pump to improve fluid flow.
- When the active train stop is removed trains will immediately leave the station if they're waiting at the station.
- Changed the default comparison type for train conditions to "or".
- Fast replacing splitters maintains the splitter contents on the new splitter instead of returning it to the player.
- Research started/changed notifications are only shown when in multiplayer.
- Crafting is now paused when the results can't be given to the player instead of spilling them on the ground.
- Changed evolution from global to per force.
- Disabled mining of vehicles other players are driving.
- Decreased biter sounds volumes
- Laser turret projectiles move much faster
- Roboport construction area changed from 50 to 51 to allow roboports build/deconstruct each other even when there is a 1 tile gap between their logistic areas.
- Restart button now uses map generation settings from currently loaded save.
- New rocket silo GUI and visibility button for freeplay and sandbox scenarios.
- Unified internal name of the 'flame-thrower' to 'flamethrower'.
- Manual ghost building will mark trees/rocks for deconstruction similar to alt-building blueprints.
- Trains are now always visible on the map, not only on chunks observed by radars or players.
- Renamed "armor-making-2" to "heavy-armor".
- Renamed "armor-making-3" to "power-armor".
- Renamed "diesel-locomotive" to "locomotive".
- Increased blueprint book size to hold 1000 blueprints
- Blueprints, blueprint books and deconstruction planners are obtainable from the library GUI with no crafting cost.
- Added combinator working, wire hold and wire place sounds.
- Single player can be continued when you die.

### Modding

- Fast cropping of sprite boundaries - it's no longer necessary to delete crop-cache.dat when existing sprites are modified.
- Utility sprites are now defined fully in the core mod prototypes.
- Added support for burner type generator-equipment.
- Added "simple-entity-with-force" and "simple-entity-with-owner" entity types.
- Boiler has now dynamically specified energy source (as inserter and similar).
- Added support for mod settings: startup, runtime, and runtime-per-user.
- Added commandline option --check-unused-prototype-data
- Added a "nothing" technology modifier type with an "effect_key" property for script-based-effect research.
- Redundant technology prerequisites are logged when verbose logging is enabled.
- Changed technology prototype icon_size to default to 32 instead of 64.
- In any instance an icon isn't 32x32 the icon_size property must be set to the actual size of the (square) icon.
- Added the ability to have "friend" forces. Friend forces are given unrestricted access to buildings and won't be attacked.
- Changed container entities to not scale info icons by default + added the optional prototype property "scale_info_icons" to enable scaling.
- Added property "turret_base_has_direction" to turret entity types. Set it to true if you want to use turn_range property in turret attack_parameters. This property has to be true for any fluid-turret, because of pipe connections.
- Added support for different recipe and technology complexity definitions.
- Added "item-with-tags" item type that can store any basic arbitrary Lua data.
- Lamps, roboports, walls, rail signals, and accumulators now accept any signal type (item, fluid, virtual).
- "animation_speed" property of animation definitions has to be greater than 0.
- Renamed smoke-with-trigger "action_frequency" property to "action_cooldown".

### Scripting

- Added "by_script" to on_research_finished.
- Added "cause" to on_entity_died - the entity that did the killing if available.
- Added "recipe" to on_player_crafted_item.
- Added "rocket_silo" to the rocket launched event.
- Added 4th custom gui root position "goal", which is used in the objectives.
- Added column_alignments settings in table style.
- Added LuaBurner - readable off entities and equipment - the burner energy source for the entity.
- Added LuaCircuitNetwork::network_id read.
- Added LuaConstantCombinatorControlBehavior::signals_count read + set_signal and get_signal.
- Added LuaControl::shooting_state , repair_state, picking_state read/write.
- Added LuaCustomChartTag + LuaForce API to add/find them.
- Added LuaDecorativePrototype.
- Added LuaEntity::connect_rolling_stock and disconnect_rolling_stock methods.
- Added LuaEntity::get_logistic_point() .
- Added LuaEntity::graphics_variation read/write for simple entities and trees.
- Added LuaEntity::shooting_target read/write for turrets.
- Added LuaEntity::stickers read. The stickers attached to a given entity.
- Added LuaEntityPrototype::crafting_speed read.
- Added LuaEntityPrototype::drawing_box , sticker_box, flags, remains_when_mined, additional_pastable_entities, allow_copy_paste, shooting_cursor_size, created_smoke, created_effect, map_color, friendly_map_color, enemy_map_color, build_base_evolution_requirement read.
- Added LuaEntityPrototype::get_inventory_size() .
- Added LuaEntityPrototype::ingredient_count read.
- Added LuaEntityPrototype::module_inventory_size read.
- Added LuaEquipmentGrid::get_contents , shield, and max_shield.
- Added LuaFluidBox::owner read + get_capacity and get_connections methods.
- Added LuaForce::evolution_factor .
- Added LuaForce::is_chunk_visible() .
- Added LuaForce::set_friend /get_friend.
- Added LuaGui::children read.
- Added LuaGuiElement drop-down type.
- Added LuaGuiElement type "camera".
- Added LuaGuiElement type "choose-elem-button".
- Added LuaGuiElement::children read.
- Added LuaGuiElement::clear to remove all the contents of the element.
- Added LuaGuiElement::single_line and want_ellipsis for the CustomLabel type.
- Added LuaInventory::entity_owner , player_owner, and equipment_owner read.
- Added LuaItemPrototype fuel_category, burnt_result, fuel_acceleration_multiplier, fuel_top_speed_multiplier read.
- Added LuaLogisticNetwork::provider_points , empty_provider_points, requester_points, full_or_satisfied_requester_points, and storage_points read.
- Added LuaLogisticPoint - read access to logistic data about provider, storage, and requester points.
- Added LuaPlayer::add_alert , remove_alert, and get_alerts.
- Added LuaPlayer::mute_alert , unmute_alert, is_alert_muted, enable_alert, disable_alert, is_alert_enabled.
- Added LuaPlayer::opened write.
- Added LuaPlayer::opened_gui_type read.
- Added LuaRandomGenerator.
- Added LuaSurface::destroy_decoratives and LuaSurface::create_decoratives .
- Added LuaSurface::find_logistic_networks_by_construction_area (..).
- Added LuaSurface::get_trains() and LuaForce::get_trains() .
- Added LuaSurface::regenerate_decorative() .
- Added LuaTrain::has_path , path_end_rail, and path_end_stop read + recalculate_path().
- Added LuaTransportLine::operator [] and operator#.
- Added Mod gui script for easy consistent styling of mod buttons and frames within the game.
- Added mouse info to the gui clicked event.
- Added on_biter_base_built - fires when biters build bases during migration.
- Added on_entity_renamed - fires when an entity is renamed either by the player or through script.
- Added on_gui_selection_state_changed - fires when an item in a drop-down gui element is selected.
- Added on_market_item_purchased - fires when a player purchases something from a market entity.
- Added on_player_changed_force - fires when a players force is changed.
- Added on_player_dropped_item - fires when a player drops an item that results in an item-on-ground entity.
- Added on_player_mined_entity and on_robot_mined_entity events.
- Added on_runtime_mod_setting_changed event - fires when a player changes runtime mod settings.
- Added on_selected_entity_changed - fires when the selected entity for a player changes.
- Added on_surface_deleted, on_pre_surface_deleted, and on_surface_created events.
- Added on_train_created event.
- Added optional "surface" to LuaForce::chart_all() .
- Added optional fields "durability" and "ammo" when using SimpleItemStack definitions.
- Added optional parameter "return_item_request_proxy" to LuaEntity::revive . If true and revive creates item request proxy, the proxy will be returned as the third value.
- Added player_index to the entity settings pasted events.
- Added remote interface functions for the rocket silo gui: add_tracked_item, remove_tracked_item, get_tracked_items, update_gui
- Added remote interface to freeplay and sandbox scripts.
- Added support for full copying LuaItemStack in most places that take the SimpleItemStack type.
- Added support for LuaFlowStatistics read on electric poles.
- Added support for specifying the "max_range" of a projectile when created through create_entity.
- Added support for turret orientation read/write through LuaEntity::orientation .
- Added the ability for mods to register commands.
- Added the ability to read item_requests from item request proxy entities as well as ghosts.
- Added the ability to read reach distances off the player or character entity.
- Changed less_then to less_than in lua GUI progress bar style specification. ( more )
- Changed LuaEntity::item_requests to match the docs format.
- Changed LuaEntity::passenger to work with both character entities and players.
- Changed LuaEntityPrototype::underground_belt_distance to LuaEntityPrototype::max_underground_distance and changed it to work on both underground pipes and underground belts.
- Changed LuaForce::clear_chart() to take an optional surface to clear the chart for.
- Changed LuaSurface::create_entity {name="item-on-ground", stack=...} to accept the same format for item stacks as the rest of the Lua API.
- Changed the player built event to include the item name used to do the building if possible and include the tags from the "item-with-tags" item if possible.
- Changed LuaPlayer::clean_cursor to return true if the cursor is now empty.
- Expanded LuaStyle read/write property support.
- Fixed LuaSurface::spill_item_stack didn't interpret "enable_looted" parameter properly. ( more )
- LuaForce::reset() now resets everything about the force to the default state.
- Mod events are now fired by the mod dependency order instead of the mod name starting with the scenario script.
- Moved game.get_event_handler and game.raise_event to "script".
- Removed Lua.coroutine due to potential exploits.
- Removed LuaGameScript::evolution_factor .
- Removed LuaGameScript::save /load.
- Removed LuaPlayer::build_from_cursor + LuaPlayer::rotate_for_build as they aren't replay/MP safe.
- Removed LuaSurface::get_tileproperties .
- Removed LuaForce::item_resource_statistics and LuaForce::fluid_resource_statistics - they've been merged into the production versions.
- The goal and left gui element has default direction vertical.
- Utility sprites can be used in the sprite button.

### Bugfixes

- Fixed that setting LuaForce::ai_controllable to false wouldn't prevent pollution-based unit group formation. ( more )
- Fixed graphics settings UI scale would change just by opening the GUI. ( more )
- Fixed UAC prompt would cause error and application termination during sprite loading on Windows. ( more )
- Fixed map generation could in some instances not correctly generate entities.
- Fixed crash when regenerating entities that are disabled by map generator settings ( more )
- Attempt to fix an occasional crash when DNS lookup fails ( more )
- Fixed crash when ammo was consumed fully by script during shooting. ( more )
- The Equipment Grid GUI is now scaled with the rest of the UI. ( more )
- Fixed possible crash caused by improper primary display detection. ( more )
- Fixed occasional broadcast related crashes on OSX ( more )
- Fixed building train vehicle in a way, that it connects on both sides. ( more )
- Fixed entities with efficiency modules wouldn't consume the correct amount of energy in some cases. ( more )
- Fixed problems when clicking connect button in server list too fast ( more )
- Fixed crash when removing large-tiles from a tile prototype definition. ( more )
- Fixed crash when mod created exoskeleton equipment with zero energy consumption. ( more )
- Fixed electric pole would draw wires to invisible ghost of enemy force. ( more )
- Fixed crash when refreshing in the browse mods GUI in some instances. ( more )
- Fixed crash when clicking the same tick the map is loaded. ( more )
- Fixed LuaGameScript::get_event_handler not working. ( more )
- Fixed desync when demoting every player on a server. ( more )
- Fixed desync caused by incorrect sorting of items with inventories (blueprint books) in player's inventory. ( more )
- Fixed crash when respawning player who had any requests in personal logistic slots and was transfered to a force without logistic slots technology researched while waiting for respawn. ( more )
- Fixed LuaSurface::create_entity {fast_replace=true} would end up deleting items in some instances. ( more )
- Fixed extremely slow deleting of selection in text fields. ( more )
- Fixed save corruption when saving while character is in vehicle with equipment grid and roboport equipment while destructor bots are deployed.
- Fixed rail integrity error when train crashes into itself. ( more )
- Fixed virtual signals wouldn't be sorted correctly by subgroup. ( more )
- Fixed typing in the save-replay GUI could move your player around. ( more )
- Fixed that manually created unit groups wouldn't be automatically removed when all their members died. ( more )
- Fixed crash when trying to make an entity ghost of an invalid entity through script. ( more )
- Fixed rail signals not reconnect after removing rails in some setups. ( more )
- Fixed trains switched to manual mode wouldn't trigger inserters when they coasted to a stop. ( more )
- Fixed lot of entities on the same tile might cause stack overflow crash when saving the map. ( more )
- Underground belt connects only to underground belt of the same force.
- Fixed personal roboport ended search for nearby ghosts prematurely if a ghost found couldn't be built due to missing item. ( more )
- Fixed desync related to teleporting any entity with emissions-per-tick defined in the prototype. ( more )
- Fixed explicitly placed crafting orders were sometimes used to satisfy dependency of other crafting orders.

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
