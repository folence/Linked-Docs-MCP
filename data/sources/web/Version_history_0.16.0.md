---
title: Version history/0.16.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/0.16.0
scraped_at: 2025-10-21 15:46:57
tags: [web, documentation]
---

# Version history/0.16.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/0.16.0](https://wiki.factorio.com/Version_history/0.16.0)

## 0.16.51

Date: 15. 06. 2018

### Graphics

- Changed the battery item icon to be more consistent with the technology icon.

## 0.16.50

Date: 11. 06. 2018

### Bugfixes

- Fixed loading script data when a mod is disabled. ( more )
- Fixed that 0 time interval was shown as an empty string. ( more )

## 0.16.49

Date: 08. 06. 2018

### Bugfixes

- Fixed belts in blueprints weren't selectable in the blueprint GUI.
- Fixed bad mouse-point when holding blueprints with belts.
- Fixed wrong connectivity in underground belt fast replace. ( more )

## 0.16.48

Date: 07. 06. 2018

### Bugfixes

- Fixed changing filters in cars wouldn't wake up inserters. ( more )
- Fixed train driving directions when not accelerating while driving backwards. ( more )
- Fixed copy-pasting between surfaces would render incorrectly. ( more )
- Fixed that empty storage tanks had the sound of fluid. ( more )
- Circuit connection distance check fix. ( more )
- The logic that shows rail signal indicators now respects bounding box and collision box of the currently held signal. ( more )

### Modding

- Fixed allow_copy_paste only worked on the source entity. ( more )

## 0.16.47

Date: 31. 05. 2018

### Bugfixes

- Fixed wall related consistency check related to modded walls with altered collision boxes. ( more )
- Fixed inconsistent train direction when reversing in a train vehicle that is not a locomotive. ( more )
- Fixed that having more than 6 products didn't fit the ui, as it wasn't wrapped. ( more )
- The system data path is removed from the log when it's automatically uploaded by the crash reporter.
- IP addresses are no longer hashed in the log file. All IP addresses are removed from the log when it's automatically uploaded by the crash reporter.
- Fixed crash when placing an entity with title while backers list was emptied.

## 0.16.46

Date: 29. 05. 2018

### Bugfixes

- Another fix for setting PvP map dimensions to 0. ( more )
- Fixed possible desync related to circuit networks.
- Another possible fix for multi-GPU setups on Linux. ( more )
- Fixed that modded infinite inserter stack size research would wrap around instead of maxing out. ( more )
- Fixed scenarios with partial identical names didn't work correctly. ( more )
- Fixed splitter lane selection inconsistency when inserting into middle. (Now it is always right for both belts, splitters and underground belts.) ( more )
- Fixed LuaPlayer::build_from_cursor . ( more )
- Fixed a desync in replay that would happen if console commands were used during the play. ( more )
- Fixed desync when setting inserter filters while it's connected to the circuit network ( more )

## 0.16.45

Date: 22. 05. 2018

### Bugfixes

- Fixed infinite research multiplier was always 1. ( more )

## 0.16.44

Date: 22. 05. 2018

### Minor Features

- Added technology price multiplier PvP scenario config.

### Changes

- Underground belt marked for deconstruction no longer connects to other underground belts.

### Bugfixes

- Fixed some cases of fast replacement by underground belt. ( more )
- Fixed corrupted config.ini in Steam cloud would prevent the game from starting.
- Fixed that using "Save and play" feature in the freeplay could specify the official freeplay map to be always that one forever. ( more )
- Fixed underground belt connection overlay when hovering over another underground belt. ( more )
- Fixed a crash when mods define empty result items. ( more )
- Fixed a crash when switching games and joining quickly in the server browser.
- Fixed that clicking rail planner with no available path while recording replay invalidated all other actions of the replay. ( more )
- Fixed a crash that would happen after opening a library blueprint that contained only entities from a disabled mod. ( more )
- Fixed LuaEntityPrototype::braking_force return value. ( more )
- Fixed LuaPlayer::ticks_to_respawn would read in seconds. ( more )
- Fixed certain type of energy source migrations. ( more )
- Fixed rare possibility of crash when two trains crash into each other. ( more )
- Fixed a rare crash that occurs when train collides in a way, that its position is reserved back while approaching closed signal which caused path recalculation. ( more )
- Fixed PvP error when setting map height to 0. ( more )
- Fixed construction robot tutorial breaking when removing the radar from the storage chest. ( more )
- Fixed crash when adding train station to a train while the train is modified (added/removed rolling stock). ( more )
- Fixed that destroying part of a cliff with tile ghost under it destroyed the whole part of the cliff. ( more )
- Fixed browse games dialog problems with the active game not being updated while searching. ( more )

### Modding

- Added support to set ReactorPrototype::neighbour_collision_increase which controls how much a reactor extends when connected to other reactors.

### Scripting

- Allow technology_price_multiplier to be less than 1 by script/scenario only.
- Added support for localised strings in LuaGameScript::write_file .

## 0.16.43

Date: 14. 05. 2018

### Bugfixes

- Fixed that consistency check failed on ghost wall entity on top of wall entity marked for deconstruction. ( more )
- Fixed, that it was possible (through mod or script) to build ghost entity of belt/wall on top of existing belt/wall causing inconsistency later on. ( more )

## 0.16.42

Date: 11. 05. 2018

### Bugfixes

- Changed the searching logic, that searching every word separately is only done when the fuzzy search option is on. ( more )
- Fixed a desync when printing a Lua error to players with different installation paths. ( more )
- Rail signal connection merge optimisation (tens of seconds instead of tens of minutes on big maps).
- Fixed that rail signal migration didn't update the state of the signal controlled by the circuit network. ( more )
- Fixed decimals displaying in production statistics that caused the numbers to be too long. ( more )
- Fixed high CPU usage on the main menu. ( more )
- Fixed an issue when joining friends games through steam. ( more )
- Fixed, that it was possible (with the use of script/mod) to build belt/wall entity (not ghost) on top of other belt entity marked for deconstruction, which could cause a consistency check fail later on.
- Added train path finding penalty for train with no path equal to 1000 tiles. ( more )
- Fixed a crash when building modded rolling stock entities on diagonal rails. ( more )
- Fixed "header errors" when extracting factorio zip files with 7zip.

### Scripting

- Added LuaEntityPrototype::collision_mask_collides_with_tiles_only and collision_mask_considers_tile_transitions read.

## 0.16.41

Date: 03. 05. 2018

### Bugfixes

- Yet another rail signal connection fix.

## 0.16.40

Date: 02. 05. 2018

### Bugfixes

- Yet another rail signal connection fix.
- Fixed a crash when killing the character during the gun_inventory_changed event. ( more )
- Fixed that LuaPlayer::opened wouldn't return the opened equipment grid. ( more )
- Fixed LuaInventory::sort_and_merge() would break furnaces and assembling machines.
- Fixed crash when trying to migrate circuit connected entities. Any migrated entities will be disconnected. ( more )
- Fixed round input in team production challenge. ( more )
- Recipe item ingredients with a count of 0 are reported as an error instead of allowing inconsistent behaviour. ( more )
- Fixed missing reset of state of signal right next to removed rail. ( more )
- Fixed a crash that could happen in multiplayer over a poor connection. ( more )

### Modding

- Added ItemPrototype::fuel_glow_color , it colors the fuel glow of entities that use that item as fuel.

### Scripting

- Added on_player_trash_inventory_changed event.
- Changed LuaSurface::find_entities_filtered/find_tiles_filtered/count_entities_filtered to additionally accept a table of filters.

## 0.16.39

Date: 30. 04. 2018

### Bugfixes

- Fixed function of enter key in number input. ( more )
- Fixed consistency check and migration related to rail internal inconsistency. ( more )
- Fixed that rail signals weren't fast replaceable.
- Fixed that the headless server wouldn't be able to restart for a while if it was stopped with an RCON client connected. ( more )
- Fixed that selecting map without a preview in the save/load dialog disallowed to delete the save by the ingame delete button.
- Fixed wrong calculation of item insertion into splitter in some cases, which could indirectly cause inconsistency in behaviour. ( more )
- Localised zip opening/closing error messages + added reason or error code there.

## 0.16.38

Date: 26. 04. 2018

### Bugfixes

- Fixed drawing of icons with multiple layers. ( more )
- Fixed that changing force of a wall didn't update the connections, which could lead to a desync.
- Changed that walls and gates marked for deconstruction don't connect, which solves some desync related problems with walls/gates marked for deconstruction with walls/gates ghosts on top of it.
- Changed, that rail signals marked for deconstruction disconnect from the rails.
- Changed, that rail signals marked for deconstruction are not blocking blueprint placement of rail signals. These changes should make it reliable to mark rail setup for deconstruction and build blueprint right on top of it before it is deconstructed.
- Changed the logic of "toggle LUA console" key to only open and not close the console (exception are ` and F1-F12 keys). ( more )
- Fixed LuaEntity::splitter_output_priority read/write didn't work. ( more )
- Fixed malformed sprite path error would not trigger minimal mode when loading mods. ( more )

## 0.16.37

Date: 23. 04. 2018

### Changes

- Added an option to interface settings to allow the user to change the distance of tooltips from the mouse. ( more )

### Minor Features

- Added optional resolution and zoom parameters to the screenshot command.

### Bugfixes

- Fixed that right click didn't work in the market GUI. ( more )
- Fixed a modded crash related to fire flame smoke.
- Fixed ignored_by_interaction when creating modded custom GUI elements. ( more )
- Fixed noise program compilation bug that resulted in broken programs. ( more )
- Fixed light from lamps outside of screen was not rendered properly. ( more )
- Fixed the steam engines in New Hope level 4. ( more )
- Possible fix for a crash on Linux with a multi-GPU setup. ( more )
- Fixed graphics of battery indicator ( more )
- Boiler and heat exchanger will spawn medium remnants instead of small remnants when destroyed. ( more )
- Fixed that a well (offshore pump with water landfilled) was not rebuildable by construction robots. ( more )
- Fixed gates sometimes not detecting car being driven by god controller. ( more )
- Fixed that some of the achievements were obtainable even when player didn't spend more than 50% of time in the game. ( more )
- Fixed that character window was closed when doing fast transfer between armor slot and inventory. ( more )
- Fixed that modded inserters would some times get stuck. ( more )
- Fixed that Wave defense would error when played on a headless server. ( more )
- Improved system of key blocking now allows more key bindings to work correctly. ( more )
- Fixed underground pipe ghost would block underground connections of other forces. ( more )
- Added missing directions to util.oppositedirection. ( more )
- Fixed that the sound sliders went to 200% causing a lost of audio quality. ( more )
- Fixed save corruption when forces are merged while there is a rocket on the map. ( more )
- Fixed that LuaEntity::teleport could teleport ghost belts/rails.
- Fixed that LuaEntity::teleport of ghost walls could create wall and ghost wall on the same position which could cause desyncs.
- Fixed that LuaEntity::teleport didn't put entities that are supposed to be aligned to grid onto grid.
- Fixed wrong behavior of mining of a vehicle the player is in in multiplayer. ( more )
- Fixed crash on starting mod scenario in multiplayer for the first time. ( more )
- Fixed signal placeability in junction with different directions in different ways. ( more )
- Added electric energy consistency check to avoid one more corrupted save situation resulting from memory corruption. ( more )

### Scripting

- Added LuaTrain::killed_players read.
- Added LuaTrain::kill_count read.
- Added LuaInventory::is_quickbar() .
- Added LuaInventory::get_selected_index() .
- Added LuaFluidPrototype::fuel_value read.
- LuaEntity::teleport puts entity to correct location on the grid when it doesn't have the off-grid flag.

## 0.16.36

Date: 28. 03. 2018

### Bugfixes

- Fixed a crash when opening the graphics settings GUI on a single core CPU. ( more )
- Fixed that building a blueprint on top of existing assembling machines did not copy the rotation correctly. ( more )
- Fixed that entering rectangular vehicles didn't work correctly. ( more )
- Fixed that totals in production statistics were 0.33% off. ( more )
- Fixed a crash when loading blueprint storage data.
- Fixed that LuaGameScript::check_prototype_translations() would report custom-inputs as having no translation.

### Scripting

- Fixed a crash by changing LuaGameScript::merge_forces() so the force is merged at the end of the tick.
- Added on_forces_merged event.
- Added LuaEntity::armed read.
- Added LuaEntityPrototype::timeout read.
- Added on_land_mine_armed event.
- Added LuaPlayer::spectator read/write.
- Added LuaGameScript::enemy_has_vision_on_land_mines read/write.

## 0.16.35

Date: 24. 03. 2018

### Bugfixes

- Fixed shifting for half-belt drawn as part of loader. ( more )

### Modding

- Added recipe-prototype show_amount_in_title and always_show_products .

### Scripting

- Added Added LuaRecipePrototype::show_amount_in_title and always_show_products read.

## 0.16.34

Date: 22. 03. 2018

### Bugfixes

- Fixed that long description in achievement cards was cut off. The card will be larger in this case now. ( more )
- Fixed a crash when rendering stickers. ( more )

## 0.16.33

Date: 22. 03. 2018

### Features

- Added dropdown to the replay viewing control that allows to switch between the view of different players.

### Changes

- Updated map-gen-settings.example.json. ( more )

### Bugfixes

- Fixed, that when the server is slower then the client, the player input is stuck. ( more )
- Fixed that using rail by the rail planner stopped replay. ( more )
- Fixed that burner inserter didn't show fuel in the entity info. ( more )
- Fixed that blueprint manipulation was broken in replays. (even opening the gui crashed the game) ( more )
- Fixed PvP script error when 'DEFCON timer' was set too low. ( more )
- Fixed that ctrl-click to transfer modules into assembling machines didn't work correctly. ( more )
- Small improvement in mining logic when using rail planner. ( more )
- Fixed an issue with un-researching upgrade-based technologies. ( more )
- Fixed a layering issue related to the train stop visualization. ( more )
- Fixed that player joined/left game messages weren't visible in the replay.
- Fixed that health bar of other players weren't visible.
- Fixed a rare crash when joining multiplayer games on Mac.
- Fixed crash when player with debuff sticker disconnected from game and later reconnected.

### Modding

- Added recipe-prototype allow_intermediates.

### Scripting

- Added events and remote interface to PvP scenario.
- Added LuaRecipePrototype::allow_intermediates read.

## 0.16.32

Date: 20. 03. 2018

### Minor Features

- Added string import/export to PvP config.

### Changes

- Only item ingredients are automatically sorted in recipes.

### Bugfixes

- Fixed LuaEntity::get_merged_signals() would always require a parameter. ( more )
- Fixed a crash related to mod settings losing precision when being saved through JSON. ( more )

### Modding

- mod-settings.json is now mod-settings.dat - settings will be auto migrated.

## 0.16.31

Date: 19. 03. 2018

### Minor Features

- Added 'Max players', 'Neutral chests' and 'DEFCON mode' PvP options.
- Empty fuel slot tooltips show what fuel they accept.

### Changes

- Enemy mines are not completely invisible anymore in PvP scenarios.
- Land mines now also stun enemy players.
- Walls will extend towards cliffs same as they already do towards water. ( more )
- Blueprint building over entities of an enemy force is no longer ignorable(blue). ( more )
- Ingredients in recipes are automatically sorted. ( more )
- Changed it so when loading a multiplayer map in single player it auto-promotes you to an admin. ( more )

### Bugfixes

- One more transport belt unsquashing tweak. ( more )
- Changed LuaSurface::find_entity to also find entities with zero sized bounding boxes but with the given position. ( more )
- Fixed drawing icons with layers when layers didn't have same source size as main icon. ( more )
- Fixed another bug where tables were disabled at certain scroll positions. ( more )
- Fixed applying blueprints could rotate unrelated assembling machines. ( more )
- Fixed that the god controller wouldn't trigger the player_moved event. ( more )
- Fixed script error in logistic tutorial when player went outside of logistic area. ( more )
- Fixed a crash when calling factorio Lua API functions with the wrong number of parameters. ( more )
- Fixed that blueprint tooltip text wouldn't line wrap. ( more )
- Fixed that heat and electric energy sources would show prototype efficiency even when they didn't support it. ( more )
- Fixed wrong scroll pane size in a specific situation. ( more )
- Fixed a crash when resetting technology effects while the technology GUI is open. ( more )
- Fixed crash with high-speed short trains crashing into something. ( more )
- Fixed that multi-line descriptions for multiplayer games would break the config.ini. ( more )
- Fixed creating cliffs through script or map editor didn't snap them to proper position. ( more )
- Fixed a crash related to biters in modded games. ( more )
- Fixed that several errors related to HTTP failure weren't localized. ( more )
- Fixed ghost rail-planner building would lock in the build rotation after being used once. ( more )
- Fixed that mod-associated character entities wouldn't be effected by force modifiers. ( more )
- Fixed that fast-transferring equipment into modded car equipment grids didn't work correctly. ( more )
- Partially fixed trains sending circuit networks signal to the wrong station. ( more )
- Fixed a crash when deleting 2 or more stations from a train within the same tick while the last station is selected in the GUI.
- Fixed another crash when saving fails when out of disk space.
- Fixed a crash when an open assembling machine with no recipe is mined while in the same tick another GUI is opened in multiplayer.
- Fixed a crash in multiplayer related to DNS failure.
- Fixed a crash when the game.take_screenshot() would fail.
- Fixed that switching between manual & automated mode was creeping forward by a bit every time when manual mode was re-activated.
- Fixed a crash when trying to set a mod setting value to 0.033333 repeating.
- Fixed that replay didn't check crc values.
- Fixed several problems related to replay saving.

### Modding

- Added Entity prototype flag "not-flammable", it prevents entities from catching fire.
- Stickers can by applied onto players now. Slowdown capsule has been changed to affect enemies only.
- Fixed some imprecisions in the Production/Electric statistics calculations.
- Added order_in_recipe into item-group, it defaults to the value of order property.
- Added item prototype flag "hide-from-fuel-tooltip".

### Scripting

- Removed LuaElectricEnergySourcePrototype::effectivity read since it didn't do anything.
- Added LuaGroup::order_in_recipe read.
- Added on_technology_effects_reset event.

## 0.16.30

Date: 12. 03. 2018

### Bugfixes

- Filters no longer disappear when inventory is downsized. ( more )
- Fixed free floating sprites would get corrupted on window resize with DirectX renderer when Low VRAM Mode was disabled. ( more )
- Fixed a crash related to resetting technology effects while a research was in progress/just finished.
- Fixed a desync related to mods calling math.random() during the data stage.

### Scripting

- Made it possible for the LuaFrame::align and LuaFrame::vertical_align to have effect on the align of the inner container.

## 0.16.29

Date: 12. 03. 2018

### Bugfixes

- Fixed that small numbers in recipe tooltips wouldn't render correctly. ( more )
- Fixed a bug where tables do not react under special conditions. ( more ), ( more )
- Fixed belt movement with squashed items and other gaps present. ( more )
- Fixed that splitter input priority was not that reliable. ( more )
- Fixed that fast replacing a circuit connected entity will sometimes double circuit network contents. ( more )
- Fixed the EULA GUI wouldn't wrap text. ( more )
- Fixed 'per second' suffix was not localised. ( more )
- Attempt to fix a problem that would prevent the Linux version from starting. ( more )
- Fixed that blueprints in the library would show empty component slots. ( more )
- Fixed that mining item entities when out of inventory space would move the item around. ( more )
- Fixed multiple desyncs related to walking near walls. ( more )
- Fixed that the "don't play sound for chat" option didn't work in multiplayer. ( more )
- Fixed some inconsistencies between damage bonus in item tooltip vs entity tooltip. ( more )
- Fixed that the players main inventory filters wouldn't persist through death. ( more )
- Fixed that pipes to ground didn't connect in blueprint preview the same way as pipes do. ( more )
- Fixed that some underground belts would not be correctly marked as ignorable(blue) when building blueprints.( more )
- Fixed enemy land mines would be highlighted when showing blueprint collisions. ( more )
- Fixed that walls would connect to ghosts from another force.
- Fixed rebinding build would cause artillery to fire multiple times per click in the map view.
- Fixed a crash when starting a headless server related to RCON.
- Fixed a crash when setting item stacks above their stack size through script.
- Fixed a crash when saving fails due to out of disk space.
- Fixed that vehicles and train stops wouldn't respect the "not-on-map" flag.
- Fixed that you couldn't move the map view while running the game at very high speeds.
- Fixed a crash when taking a large screenshot by script fails due to a lack of memory.
- Fixed a crash when canceling crafting after changing recipes through mods.
- Fixed a crash when merging forces through script while a recipe tooltip is visible.
- Fixed a crash when using the /open command and then opening an item in the players cursor.
- Fixed a crash when creating modded tree particles.
- Fixed a crash related to modded speaker entities.

### Modding

- Changed the maximum number of electric poles that can be connected to one entity from 255 to 65535.
- Added optional Electric pole prototype "draw_copper_wires" and "draw_circuit_wires".
- Added Entity prototype flag "not-rotatable".
- Fixed a crash when not defining a stream particle animation.

### Scripting

- Added LuaRCON to allow printing text to a calling RCON instance.
- Added LuaItemPrototype::fuel_emissions_multiplier read.
- Added LuaRecipePrototype::emissions_multiplier read.
- Added LuaFluidPrototype::emissions_multiplier read.

## 0.16.28

Date: 05. 03. 2018

### Minor Features

- Added a simple recipe price calculator to PvP production score.
- Item number in quickbar now shows over the "hand" when part of the stack is picked up. ( more )

### Bugfixes

- Fixed drawing endings of transport belts entering underground belt sideways. ( more )
- Fixed a bug with pumps not activating sometimes. ( more )
- Fixed roboport connections would be missing in some cases. ( more )
- Fixed a bug with pumps not activating sometimes. ( more )
- Fixed that biters in groups had too low tolerance for getting stuck. ( more )
- Fixed that you could set accumulator energy below 0. ( more )
- Fixed a crash in rail pathing when deleting signals. ( more )
- Fixed a crash when creating beam entities through script. ( more )
- Fixed old boilers in New Hope level 4. ( more )
- Fixed that changing the values in new game gui could move other gui elements. ( more )
- Changed order of drawing, so if sprite button uses caption, its text is over the picture. ( more )
- Fixed that the wire connection distance visualization didn't match the actual distance limits. ( more )
- Fixed a crash when trains are destroyed while the trains GUI is open. ( more )
- Fixed train stop indicators wouldn't render with larger blueprints. ( more )
- Fixed mod changing chest collision box could break PvP starting chest accessibility. ( more )
- Fixed that the Map editor wouldn't clear the cursor when the tool changes. ( more )
- Fixed a crash when destroying rails with trains on them. ( more )
- Fixed a crash when joining Steam games through the Steam interface.
- Fixed a crash related to adding equipment grid support to armor in existing games.
- Fixed several crashes related to GUI logic.
- Fixed a crash when loading pre 0.16 saves when in a vehicle as a god controller.
- Fixed a crash when teleporting offline players between surfaces.
- Fixed non-stackable items wouldn't enforce they aren't stackable.
- Fixed a crash when changing runtime mod settings while someone is joining a multiplayer game.
- Fixed a crash when a character or spawner dies in the map editor.
- Fixed a crash when hovering over blueprint book item in the map editor.
- Fixed a crash when right-clicking a blueprint to open it for editing in the map editor.
- Fixed a crash when putting blueprints into blueprint books in multiplayer.
- Fixed a crash when importing some blueprint strings.

### Scripting

- Added has_hidden_tile and collision_mask flags to LuaSurface::find_tiles_filtered and LuaSurface::count_tiles_filtered .
- Added LuaSurface::set_hidden_tile() .
- Added LuaGuiElement::ignored_by_interaction which prevents the elements from stealing mouse interaction with the parent elements. ( more )
- Added LuaSpriteButton::number which allows the number to be rendered in the standard way in the right-bottom corner of the sprite button.
- Added LuaSpriteButton::show_percent_for_small_numbers which, when set to true, forces the number to be shown as percent when smaller than 1.

### Modding

- Added ItemPrototype::fuel_emissions_multiplier which scales pollution generated when the fuel item is used.
- Added FluidPrototype::emissions_multiplier which scales pollution generated when when the fluid is consumed.
- Added RecipePrototype::emissions_multiplier which scales pollution generated by the entity using this recipe.
- Added support to set scroll_pane_style horizontal_scroll_bar_style and vertical_scroll_bar_style.

## 0.16.27

Date: 28. 02. 2018

### Minor Features

- Added refined concrete and refined hazard concrete.

### Changes

- The the name textfield in the rename train stop dialog gets automatically focused and the text is pre-selected.

### Bugfixes

- Fixed that dying would only put the first stack into the dead body. ( more )
- Fixed that infinite resources would always produce the same result when at minimal yield. ( more )
- Fixed how the switch event is processed. ( more )
- Fixed behaviour of the train station list-box when player inventory was big enough to be scrollable. ( more )
- Fixed that always_show_made_in didn't work for recipe tooltips in the technology GUI. ( more )
- Fixed a crash when migrating item types in some cases.
- Fixed movement of belt segment that has a lot of squashed items in it.
- Fixed a crash in the map editor when changing player armor.
- Fixed a crash related to mods destroying the player during player events.
- Fixed a crash when creating a Factorio account using the in-game option.

## 0.16.26

Date: 26. 02. 2018

### Features

- Added partial IME support for typing Chinese, Japanese and Korean text on Windows.

### Changes

- IPs are no longer directly logged.

### Bugfixes

- Fixed several belt compression problems.
- Fixed crash when rendering turret range visualization in camera widget.
- Fixed incorrect behaviour when a text box line wraps. ( more )
- Fixed achievement deletion dialog. ( more )
- Fixed choose-elem-button locking not persisting across saves. ( more )
- Fixed item creeping forward on belt sometimes. ( more )
- Fixed removal of tracked silo script items. ( more )
- Fixed a crash when using the Lua GUI element type "entity-preview". ( more )
- Fixed that "Expected resources" didn't always match what you actually got. ( more )
- Fixed that heavily modded saves with large amounts of tile types couldn't be loaded without the mods. ( more )
- Fixed that buffer chests could get items sent to them they weren't requesting. ( more )
- Fixed belts would stop animating after really long time. ( more )
- Fixed crash when vehicle with personal roboport was destroyed because of impact damage from its own movement. ( more )
- Fixed the help locale for the /toggle-rockets-sent-gui freeplay command. ( more )
- Fixed wrong scale of icons with non-standard icon_size in alt-mode. ( more )
- Fixed generator effectivity being applied twice when below 100%.
- Fixed a crash when failing to download a map in multiplayer.
- Fixed crashes related to Lua stack overflows.
- Fixed a crash related to changing the stack size of items when removing mods.
- Fixed a crash when researching logistic request slots.
- Fixed a crash related to the ending screen data in multiplayer.
- Fixed a crash when explosion entities where created during migration scripts.
- Fixed a crash when exiting the game while it's saving.
- Fixed a crash when loading a map file fails.
- Fixed a crash related to modded burner generator equipment in multiplayer.
- Fixed labels could render outside of their defined area.
- Fixed a crash when placing assembling machine blueprints over ghosts.
- Fixed a crash when clicking quickly while joining multiplayer games.
- Fixed a crash when saving the game fails.
- Fixed a crash when deleting chunks with cliffs on them.
- Fixed a crash when trying to set player inventory filters in the map editor.
- Fixed several GUI related crashes related to multiplayer latency.
- Fixed a crash when hosting LAN-enabled multiplayer games in some instances.

### Modding

- Added GeneratorPrototype::scale_fluid_usage which scales the generator's fluid usage to its maximum power output. Default is false.
- Generator will now produce pollution if emissions is specified on the energy source.

### Scripting

- Added LuaGameScript::is_multiplayer() .

## 0.16.25

Date: 19. 02. 2018

### Changes

- Inserters, mining drills, and belt sideloading can now squash items on belt even when the gap isn't big enough. The squashed gap is extended to normal size once the front of the belt starts to move again. This means, that inserter, mining drills and side loading can produce fully compressed belts without the usage of splitters.

### Minor Features

- Improved behavior of mode switches in deconstruction planner. ( more )

### Bugfixes

- Fixed crash when train was leaving station that was disabled by circuit network or destroyed. ( more )
- Fixed search box losing focus inconveniently in mods gui. ( more )
- Fixed client crash when server exits while player has the save game dialog open. ( more )
- Removing components of a blueprint no longer resizes the window. ( more )
- Fixed performance issue when running out of storage while big deconstruction is in progress.
- Fixed scrollbar buttons that would ignore mouse up event. ( more )
- Fixed that after changing some control settings, the quickbar wouldn't react to them until the game was reloaded. ( more )

### Scripting

- Added LuaControl::is_player()

## 0.16.24

Date: 15. 02. 2018

### Minor Features

- When the game crashes, the crash log is uploaded to us. You can opt out by disabling it in the options menu.
- Player chat color when set through '/color r g b a' command will be brightened. ( more )

### Bugfixes

- Fixed that LuaEntity::get_merged_signals() would return wrong value if no wires were connected. ( more )
- Fixed flamethrower turret could get stuck in deactivated state when fluid type in its pipe changed. ( more )
- Fixed energy consumption of laser turret in recipe tooltip. ( more )
- Fixed that specifying a shift for a storage tank's fluid_background would shift it incorrectly. ( more )
- Fixed that ctrl-arrow/backspace/delete worked in the console but not in other text boxes. ( more )
- Fixed that you could define a fluidbox height of 0. ( more )
- Fixed trains "twitching" under certain circumstances. ( more )
- Fixed wrong hairy dead tree graphics positioning. ( more )
- Fixed that ping-pong DNS lookup failure would shut down running multiplayer games. ( more )
- Fixed LuaInventory::getbar /setbar used zero-based indexing. ( more )
- Fixed incorrect electric network connection rendering on the map. ( more )
- Fixed train would reset its "waiting on signal" penalty when recalculating path due to waiting too long. ( more )

### Scripting

- Added script.on_nth_tick(n, function).
- Added LuaSurface::can_place_entity (...) optional parameter "build_check_type" and "forced".

## 0.16.23

Date: 12. 02. 2018

### Changes

- Lamps stagger again during day/night transition. They also turn on much sooner and turn off much later.
- The deconstruction planner "trees/rocks only" option can be inverted using the whitelist/blacklist toggle.
- The Rocket silo entity info now shows 'Rocket parts: 50/100'.
- Removed 'starting inventory' PvP option, as starting chests are a more proper solution.
- Added 'required satellites sent' option to space race PvP game mode

### Bugfixes

- Fixed snapping locomotive to station sometimes not working. ( more )
- Fixed modded loaders with different dimensions crashing when destroyed. ( more )
- Fixed that module effects would go negative when adding too many beacon effects together. ( more )
- Fixed that changing an assembling machine recipe by copy-paste would delete the in-progress recipe items. ( more )
- Fixed that directly replacing modules didn't work correctly. ( more )
- Fixed that changing train stop names wouldn't update the last-user. ( more )
- Fixed that the logistic count tooltip wouldn't show correctly for negative values. ( more )
- Fixed that changing the stack size of the satellite through mods could make it impossible to win. ( more )
- Fixed circuit controlled stack override sometimes being incorrect. ( more )
- Fixed that mods could specify invalid categories, for a few classes of modded item. ( more )
- Fixed pipette tool orientation of curved tracks. ( more )
- Fixed that beacons would ignore the allowed effects on an entity. ( more )
- Fixed that rail ghosts weren't placeable on top of enemy force's land mines, thus revealing the location of the mines. ( more )
- Fixed Lua module limitations array being a map of strings to numbers, instead of an array.  ( more )
- Fixed that the market GUI wouldn't use a scroll bar even when the offers didn't fit in the window. ( more )
- Fixed worker robot speed in PvP scenario. ( more )
- Fixed that the blueprint preview in the blueprint library was smaller than the blueprint view you get after opening a blueprint item. ( more )
- Fixed that the technology search would be broken by disabled technologies in some cases. ( more )
- Fixed that mods changing stack sizes would break the inventory transfers tutorial. ( more )
- Power switch copper wire connections are now saved in the ghost when destroyed and restored when rebuilt. ( more )
- Fixed LuaSurface::regenerate_decoratives() would generate much more decoratives than normal map generator run. ( more )
- Fixed clicking the label in sort-able tables wouldn't effect sorting. ( more )
- Fixed that recipe tooltip labels would render outside of the tooltip area in some cases. ( more )
- Fixed clamp_position=true on artillery shells would negate artillery range bonus. ( more )
- Fixed item icon would not be rescaled to normal size if icon_size not 32. ( more )

### Modding

- Added "friend" and "not-friend" force trigger modifiers.
- Added optional night vision equipment prototype "darkness_to_turn_on".

### Scripting

- Added LuaGameScript::ammo_category_prototypes read.
- Added LuaEntity::get_merged_signals() .

## 0.16.22

Date: 02. 02. 2018

### Bugfixes

- Fixed a crash when loading saves with modded camera GUI elements. ( more )
- Changed the "load save in map editor" to "convert save to Scenario" to support locale and custom scripts. ( more )
- Another attempt to fix crashes on OS X Mavericks (version 10.9). ( more )
- Fixed that some mod settings would always detect as different than the server when trying to join. ( more )
- Fixed that turrets that died and where rebuilt couldn't be mined. ( more )

### Modding

- Added optional RecipePrototype::allow_as_intermediate to disable a recipe being used as an intermediate when hand crafting.
- Added PlayerPrototype::enter_vehicle_distance .

### Scripting

- Added LuaRecipePrototype::allow_as_intermediate read.
- A player changing the active index in a blueprint book in the cursor will now fire the player_cursor_stack_changed event.
- Added LuaEntityPrototype read properties: running_speed, maximum_corner_sliding_distance, build_distance, drop_item_distance, reach_distance, reach_resource_distance, item_pickup_distance, loot_pickup_distance, enter_vehicle_distance, ticks_to_keep_gun, ticks_to_keep_aiming_direction, ticks_to_stay_in_combat, respawn_time, damage_hit_tint, character_corpse.

## 0.16.21

Date: 01. 02. 2018

### Minor Features

- Added support to load save files directly in the map editor.
- Added "Save and play" button to map editor, to allow quick iteration.
- Added levels in campaigns to level editor "open" menu.

### Changes

- Requesters requesting from buffer chests (which includes players) have higher priority than other requesters.
- Player death messages will be printed to all forces they are friends with.
- Player death messages include the player tag. Gui:
- The left/right switch used in locomotive and splitter can be also switched by clicking the label buttons.

### Bugfixes

- Fixed teleporting pumps would crash the game. ( more )
- Fixed dragging in the map preview and technology GUI didn't work correctly. ( more )
- Fixed walls wouldn't connect correctly when built through script in some cases. ( more )
- Fixed that the equipment grid was too small when using extra-low graphics quality. ( more )
- Fixed inserters could get stuck trying to pick up items off the ground in some cases. ( more )
- Fixed issues related to splitter priorities. ( more )
- Fixed that the "recursive technology prerequisites detected" error message wouldn't print the dependency cycle properly. ( more )
- Fixed (and hopefully generally improved) the splitter GUI so invalid states are not possible. ( more )
- Fixed that biters would not be able to path find close to cliffs. ( more )
- Fixed mod control settings would be wiped out when game entered minimal mod due to mod error on start up. ( more )
- Fixed that the tips-and-tricks GUI would open when running a replay. ( more )
- Fixed that the blueprint setup GUI wouldn't show in some situations. ( more )
- Fixed that the asynchronous saving process could freeze in headless mode. ( more )
- Fixed crash in PvP when distance between starting areas was too low. ( more )
- Fixed small locale error in resource entity info. ( more )
- Fixed crash when player deletes blueprint book from their library while other player has the book opened. ( more )
- Fixed that custom scroll panes didn't respect vertical scroll policy correctly. ( more )
- Fixed a crash in the technology GUI when using LuaForce::disable_all_prototypes() . ( more )
- Adjusted collision boxes of decals to reduce chance a decal will be generated in position colliding with water. ( more )
- Fixed that the recipe tooltip "made in" wouldn't show every possible machine when there was a lot of them. ( more )
- Fixed ghost of lamp would not connect to logistic network when revived. ( more )
- Fixed that the command line --map2scenario option wouldn't convert scenario-created saves correctly. ( more )
- Fixed handling of mouse bindings in map view. ( more )
- Fixed that you could get stuck after using cliff explosives. ( more )
- Fixed biters getting stuck next to a wall in some situations. ( more )

### Modding

- Added optional create_ghost_on_death for entities with health that normally make ghosts on dying.
- Added optional always_show_made_in to recipe prototypes.

### Scripting

- Added last_research to the on_research_started event.
- Added LuaEntityPrototype::energy_per_hit_point read.
- Added LuaEntityPrototype::create_ghost_on_death read.
- Added CustomMinimap GUI element type.
- Added CustomEntityPreview GUI element type.
- Added LuaInventory::sort_and_merge() .
- Added an optional "invert" option to LuaSurface::find /count entities filtered.
- Added LuaForce::enable_all_prototypes() .
- Added LuaRecipePrototype::always_show_made_in read.
- Added LuaControl::get_main_inventory() .
- Added LuaGuiElement::column_count read.
- Changed util.merge to always deepcopy nested tables. ( more )
- Changed events so they won't fire until every mod has had on_init ran.

## 0.16.20

Date: 26. 01. 2018

### Bugfixes

- Fixed another compression problem on belts related to splitters.
- Fixed that the cancel craft, import blueprint and blueprint book buttons didn't work.
- Fixed biter related desyncs. ( more )
- Fixed possible desync related to logistic network.

### Modding

- Renamed render_layers: ground_patch, ground_patch_higher, ground_patch_higher2, and air-entity-info-con to ground-patch, ground-patch-higher, ground-patch-higher2, and air-entity-info-icon.

## 0.16.19

Date: 25. 01. 2018

### Minor Features

- Added PvP options: Disband team on loss, team area artillery and give artillery remote.

### Bugfixes

- Fixed that the game allowed mining speed modifier less than -1, which resulted in negative mining speeds. ( more )
- Fixed that fast-replacing power poles while running would just delete them. ( more )
- Fixed that you couldn't exit vehicles with large collision boxes. ( more )
- Fixed that LuaPlayer::can_insert and LuaPlayer::insert didn't agree. ( more )
- Fixed game state corruption related to ordering deconstruction of entities with enabled connection to logistic network. ( more )
- Fixed that teleporting roboports when robots where charging would lead to corrupt saves. ( more )
- Fixed that toggle-console wouldn't work with modifier keys. ( more )
- Fixed graphical artifacts in terrain when zoomed out. ( more )
- Fixed that LuaForce::disable /enable research wouldn't update the GUI correctly. ( more )
- Fixed that pumps would ignore fluidbox filter. ( more )
- Fixed crash caused by non-ASCII characters in name of custom scenario. ( more )
- Fixed that idle biters would ignore the player when approached. ( more )

### Modding

- Added support for setting icon_size per icon layer.

### Scripting

- Added LuaGameScript::default_map_gen_settings read.
- Added LuaSurface::get_random_chunk() .

## 0.16.18

Date: 23. 01. 2018

### Bugfixes

- Fixed searching for recipes could add the "no recipe available" message multiple times. ( more )
- Fixed a crash related to biters. ( more )
- Fixed that setting locked = true on choose-elem-buttons through the mod API would still let the button be cleared. ( more )
- Fixed logistic entity highlighting didn't work correctly in some cases. ( more )
- Fixed that the map editor could get stuck if you built out-of-map tiles directly in the center of the screen. ( more )
- Fixed Linux runtime requirements being dynamically linked. ( more )
- Fixed (hopefully) macOS crash on startup due to 10.9 compatibility fix. ( more )

## 0.16.17

Date: 22. 01. 2018

### Features

- Added filter to splitter.
- Added input and output priority to splitter.

### Minor Features

- Added a "clone group" button to the permissions GUI.
- Added PvP options: Spectator fog of war, starting chests, chest item multiplier, team areas turrets, automatic round time, and base exclusion time.

### Balancing

- Increased the stack size of roboport from 5 to 10.
- Decreased collision box of substation, radar and chemical plant so it is possible to walk between it and other entities.

### Bugfixes

- Fixed that rail chain signals didn't work with copy-paste. ( more )
- Fixed that double clicking the empty space in scroll bars on the load/save map GUIs would trigger the load/save. ( more )
- Fixed that walking near the edge of water could result in no footstep sounds. ( more )
- Fixed building belts over splitters marked for deconstruction while a ghost belt was under the splitter didn't work. ( more )
- Fixed that ghost solar panels would show as having energy. ( more )
- Fixed that the bonus GUI didn't show correct numbers for some bonuses. ( more )
- Fixed that a single water tile that separates two terrain types would become invisible. ( more )
- Added graphics option "Separate lower object atlas" to address performance issue when rendering lot of decoratives on some PCs. The option will put sprites drawn under shadows in a separate sprite atlas with mipmaps enabled. This should reduce GPU load, but slightly increase CPU load and VRAM usage. ( more )
- Added a command-line option --executable-path to allow launching Factorio through a custom ld.so on Linux. ( more )
- Fixed a crash when setting invalid prototype values for vehicle type entities through mods. ( more )
- Fixed that you couldn't attack nests with your pickaxe.
- Additional fix of the rail block visualization for high res. ( more )
- Fixed jittering when running against entities with connected bounding boxes (for example pipes). ( more )
- Fixed that entities with multiple items to build them wouldn't fire mod events in some cases. ( more )
- Fixed recipe tooltip with many raw materials showing incorrectly. ( more )
- Fixed invisible GUI when assembling machine with no recipe is opened. ( more )
- Fixed a crash on Linux that would happen after dragging a UI element outside the game window. ( more )
- Fixed inconvenient drag-placing of electric poles around large entities. ( more )
- Fixed un-setting controls wouldn't work correctly for key bindings with default modifiers. ( more )
- Fixed artillery projectile shadow was not aligned with artillery cannon shadow. ( more )
- Fixed line breaks in changelog with UI scale. ( more )
- Fixed that too many biters trying to return to a spawner could make all other biters inactive. ( more )
- Fixed robots deconstructing artillery turrets could lose ammo. ( more )
- Improved scroll behaviour in server list. ( more )
- Fixed possibility of receiving the previous rounds input items in Team production. ( more )
- Fixed that the game could create many enemy unit groups resulting in poor performance. ( more )
- Fixed pasting entity settings would not disable connection to logistic network. ( more )
- Fixed blueprint containing rocket silo could result in broken silo if placed before rocketry was researched. ( more )
- Fixed rail chain signal ghost would emit light. ( more )
- Fixed that blueprint strings wouldn't retain storage chest filters. ( more )
- Fixed passing LuaObjects through the remote interface wouldn't always work correctly. ( more )
- Fixed that LuaSurface::create_entity wouldn't work to create walls on top of ghost walls. ( more )
- Fixed that a furnace or assembling machine with > 100% productivity with a <= 1 tick crafting time recipe wouldn't work correctly. ( more )
- Fixed building blueprint rails on rails marked for deconstruction didn't work correctly in some cases. ( more )
- Fixed a migration issue related to logistic entities and inventory resizing. ( more )

### Modding

- Removed terrain_collision_box from fish prototype. To prevent fish with non-zero collision box from blocking offshore pump placement, default collision mask of fish has flag 'colliding-with-tiles-only'. ( more )
- Disabled recipes won't be cleared from an assembling machine ghost, if the assembling machine prototype has fixed_recipe set.
- Entity of type offshore pump can be rotated on ground if flag 'filter-directions' is not set. ( more )

### Scripting

- Changed the tile related events to include the old tiles and positions instead of just positions.
- Added on_pre_player_crafted_item and on_player_cancelled_crafting events.
- Added on_entity_damaged event.
- Added on_chunk_charted event.
- Added LuaEntity::splitter_filter , splitter_input_priority and splitter_output_priority read/write.
- Added ghost_name and ghost_type to LuaSurface::find /count entities filtered.
- Fixed recursive call in util.merge(). ( more )

## 0.16.16

Date: 10. 01. 2018

### Minor Features

- Items on the ground can be mined manually for precise control of what you pick up.
- Added 'duplicate starting entities' option to PvP.

### Changes

- Changed splitters so they work more intuitively. The left and right lane splitting is now completely independent. The decision whether item goes to left or right output is now independent of the item type.
- Hide cliff explosives in bonus GUI as they don't really receive any bonuses. ( more )
- Tweaked the balancing of the PvP production score.
- Changed size of offshore pump from 3x1 to 3x2 in order to prevent pump placement in overlapping positions. ( more )

### Optimisations

- Optimized drawing of artillery range visualization when many artilleries were in range of viewed area. ( more )

### Bugfixes

- Fixed that consecutive splitters could uncompress compressed belt. ( more )
- Fixed that loading from the game-over screen would result in a crash if loading failed. ( more )
- Fixed several settings copying issues when placing blueprints over existing entities related to multiplayer. ( more )
- Fixed machines disabled by circuit network sometimes staying disabled when they shouldn't. ( more )
- Fixed Linux users sometime crashing when relaunching the game. ( more )
- Fixed that blueprint library GUI would lose your filter when you view a blueprint. ( more )
- Fixed that biters would sometimes be deactivated when they shouldn't. ( more )
- Fixed that artillery would target forces marked with cease fire. ( more )
- Fixed a crash when using LuaTransportLine::remove_item() . ( more )
- Fixed that the beacon would show energy consumption twice. ( more )
- Fixed PvP production score calculation for hand crafting and launching satellites.
- Fixed jittering when walking into a straight water/land border. ( more )
- Attempt at fixing missing symbol on macOS 10.9 ( more )
- Fixed that turret range map and hover overlays didn't quite match. ( more )
- Fixed that RCON would only respond to the first command in a packet. ( more )
- Fixed PvP no rush restriction could be bypassed using a vehicle.
- Ensure that there is always at least a minimal lake in the starting area.
- Fixed script error if a removed modded item was sent in a rocket. ( more )
- Fixed that loading logistic heavy saves after changing mods would take 20+ minutes. ( more )
- Fixed a crash when mods would try to set item health values to negative amounts. ( more )
- Fixed requester chests could get stuck in some cases. ( more )
- Fixed that manually putting damaged items in the output slot of an assembling machine could lead to lost items. ( more )
- Fixed chunk edge cliff discontinuities due to ore patches. ( more )

### Scripting

- Added LuaEntity::cliff_orientation read.

## 0.16.15

Date: 05. 01. 2018

### Bugfixes

- Fixed that underground belts built by a blueprint would not respect the type of an existing belt. ( more )
- Fixed pump ghosts would always highlight attached rail, not just when selected.
- Fixed that logistic network requests would get into invalid state when migrated from save where player had more requests due mods. ( more )
- Improved number formating in electricity overview to make it less jumpy. ( more )
- Fixed logistic robots migration related to changing force of logistic robots while stationing. ( more )
- Fixed when sliding around entity, the character could be pushed to a position colliding with water and get stuck in the terrain. ( more )
- Reduced RAM usage by removing unnecessary memory buffers for textures when using OpenGL. ( more )

## 0.16.14

Date: 04. 01. 2018

### Minor Features

- Added 'allow spectators' option to PvP.

### Changes

- Changed rail world settings to have normal biters frequency.

### Bugfixes

- Fixed loading specific saves wouldn't migrate the character requests correctly to request from buffer chests. ( more )
- Fixed that migrating saves would make research impossible in the level 4 of New hope campaign. ( more )
- Fixed that inserters would try to put items into furnaces that could never fit. ( more )
- Fixed requester chests wouldn't keep up with the request amount demand in logistic heavy saves. ( more )
- Fixed that request chests weren't equally distributed when there were not enough robots.
- Fixed that migration to 0.16.8 which de-duplicated logistic requests wasn't doing so for offline players. This could cause crashes as the internal data structures take it as granted.
- Fixed that download progress bar in the sync save with mods wasn't being updated.
- Fixed that exiting the connection in progress (by pressing escape) soon enough could result in a screen without any menu.
- Fixed some PvP game modes being won by launching a rocket.
- Fixed config.ini would be purged when game decreases graphics settings when loading sprites throws an error. ( more )

## 0.16.13

Date: 03. 01. 2018

### Minor Features

- Added a time limit option to PvP game modes 'Production score' and 'Oil harvest'
- Added 'score per minute' to the PvP Production score GUI.

### Bugfixes

- Fixed a crash when blueprinting modded logistic storage chests. ( more )
- Fixed requester chests wouldn't work with specific combinations of storage, buffer, and provider chests. ( more )
- Fixed a crash with the command line map preview option. ( more )
- Fixed the world-icon for the cliff explosive didn't match the item icon. ( more )
- Fixed the progress indicator in the browse-mods GUI would update too quickly. ( more )
- Fixed changing the force of a robot waiting to charge would break the robot. ( more )
- Fixed that joining modded multiplayer games where the spawn area was deleted would error. ( more )
- Fixed that pasting text didn't work correctly in any text field. ( more )
- Fixed a crash related to tile transitions. ( more )
- Fixed logistic storage filters would be ignored in some specific cases. ( more )
- Fixed that side-loading underground belts could lead to them getting stuck. ( more )
- Fixed that modded storage chests would allow more than 1 filter when the extra filters weren't valid. ( more )
- Fixed that the map preview seed wouldn't get used when the generate map GUI had an exchange string entered. ( more )
- Added yet another migration fixing invalid state created between 0.16.8 and 0.16.11.
- Fixed that startup mod settings could be changed while in-game by clicking the label on checkboxes. ( more )
- Fixed that tooltip of disabled widgets didn't work.
- Added greyed-out look to disabled textfield and checkbox to make it more clear that it isn't editable.
- Fixed one of the curved rail segment visualizations wasn't aligned correctly. ( more )
- Fixed that the console could be opened in a paused game where it can't be interacted with.
- Fixed issues of console in combination with technology GUI in multiplayer. ( more )
- Fixed changelogs (including mod changelogs) not properly displaying the "All" subversion for a version x.y when there was no version x.y.0. ( more )
- Fixed horizontal scroll pane scroller. ( more )
- Fixed that changing value in GameViewSettings in the Lua script didn't update the gui until the game was reloaded.
- Fixed a crash when controller view is disabled. ( more )
- Fixed script error when destroying a chest in the supply scenario.
- Fixed PvP production score price calculation.

### Modding

- Entities without an item-to-place can still be deconstructed if they are minable.

### Scripting

- Added LuaPlayer::blueprint_to_setup read.
- Changed default value of 'expires' when creating ghost through LuaSurface::create_entity from 'true' to 'false'.
- Fixed invalid internal state + crashes when ghost without "expires = false" was created through the script when ghost time to live was 0. ( more )

## 0.16.12

Date: 31. 12. 2017

### Bugfixes

- Fixed that rail signal indicator didn't show two way signal placement in junctions even when the signal was placeable there.
- Fixed that the game would crash if the mouse was moved fast enough outside the game window while loading a map. ( more )
- Fixed crash related to logistic chests to be cancel-deconstructed.
- Fixed few cases where logistic requesters and buffers were not initialized correctly when built before the roboport.

## 0.16.11

Date: 30. 12. 2017

### Bugfixes

- Fixed yet another requester chest state migration error.
- Fixed that burner inserter didn't show the fuel icon when out of energy sometimes. ( more )
- Fixed that some specific pre 0.15 maps couldn't be loaded.

## 0.16.10

Date: 30. 12. 2017

### Bugfixes

- Fixed crash related to setting logistic requests by circuit network.
- Fixed requester chest state migration between different save versions.
- Fixed one of the problems of internal provider data corruption related to setting inventory bar limit.

## 0.16.9

Date: 29. 12. 2017

### Bugfixes

- Fixed that player didn't request from buffer chests.
- Fixed that some maps with modded selection-tool items failed to load.

## 0.16.8

Date: 29. 12. 2017

### Features

- Storage chests can be filtered.

### Minor Features

- Requester chests can now request stuff from buffer chests as was originally intended. Buffer chests are provided items only if all requester chests are satisfied for that specific item.
- Requester chests have a checkbox that specifies whether it should or shouldn't request things from buffer chests. It is off by default.

### Optimisations

- Optimized selecting robot tasks for requester chests.

### Balancing

- Changed fluid wagon capacity from 75k to 25k (Same as storage tank).
- Lowered fluid wagon weight from 3000 to 1000 (same as cargo wagon).
- Changed fluid wagon recipe so it requires just 1 storage tank instead of 3.
- Lowered barrel fluid capacity from 250 to 50. (So cargo wagon with barrels holds 20k and logistic robots are not too strong alternative to carrying fluids.)
- Decreased barreling crafting time from 1 second to 0.2 seconds.

### Bugfixes

- Fixed loading of achievements with steam version. ( more )
- Fixed train schedule resizing with very large player inventory. ( more )
- Fixed missing auto resizing of Lua GUI elements when caption changes. ( more )
- Fixed that it was possible to set duplicate logistic requests.
- Fixed missing entity counts when selecting area for blueprint on low graphics quality. ( more )
- Fixed calculation of basis noise when x<0 ( more )
- Fixed missing locale key in fluid wagon description. ( more )
- Fixed that the fluid wagon wouldn't show any GUI when it had an equipment grid. ( more )
- Fixed evolution command output in campaigns. ( more )
- Fixed shotgun shooting direction when aiming between the player and the nozzle. ( more )
- Fixed technology sorting. ( more )
- Fixed that the default list box font was called "default-list_box". ( more )
- Fixed that clicking "Generate" button in the generate map window while the exchange string field was enlarged moved the button around before the mouse up was registered. The exchange string field will now never shrink on focus lost.
- Fixed that setting LuaPlayer::opened to an empty item would crash the game. ( more )
- Fixed performance issues when hovering over huge resource patches in map or zoomed-to-world view. ( more )
- Fixed a desync when hosting multiplayer directly and building blueprints. ( more )
- Fixed a crash when calling specific LuaEntity properties. ( more )
- Fixed module effects weren't checked correctly for modded modules. ( more )
- Fixed a crash when teleporting roboports or logistic containers marked for deconstruction. ( more )
- Fixed roboports would show up twice in the logistic GUI. ( more )
- Fixed the background on the select-recipe GUI for the choose-elem-button didn't show correctly. ( more )
- Fixed changing transport belt speeds through mods on existing saves. ( more )
- Fixed a crash when setting filters on cargo wagons in multiplayer. ( more )
- Fixed a crash when trying to put blueprint books in blueprint books. ( more )
- Fixed that train could overshoot a station when the schedule was changed by the script.
- Fixed that heat pipes would incorrectly update their connections when teleported. ( more )
- Fixed the problem of flickering tooltips in a generic way (hopefully). ( more )
- Fixed that the table of games was focused (for keyboard control) even if the player focused the search bar manually. ( more )
- Fixed crash that can happen when train on its path to station that was deactivated finds path to different alternative station of the same name that leads in opposite direction to current train movement. ( more )

### Scripting

- The item-with-tags and selection-tool item types now support LuaItemStack::item_number .
- Added an optional player parameter to LuaEntity::order_deconstruction , cancel_deconstruction, LuaTile::cancel_deconstruction , LuaSurface::deconstruct_area , and LuaSurface::cancel_deconstruct_area .

## 0.16.7

Date: 21. 12. 2017

### Bugfixes

- Fixed that trains approaching train stop started breaking 2 times sooner when no signal was in front of the stop.
- Fixed order of controls in the control settings GUI. ( more )
- Fixed rail pumps becoming invalid after being teleported via Lua. ( more )
- Fixed that biter expansion chunks weren't being generated correctly. ( more )
- Fixed that rail signal ghost of different force (so invisible) was restricting rail placement.
- Fixed server crash when last player leaves the game while the server is saving. ( more )
- Fixed text cursor positioning inside a text box during scroll. ( more )
- Fixed an additional crash when trying to filter the main inventory in the god-controller in the train GUI. ( more )
- Fixed that blueprint strings wouldn't copy station names in blueprints. ( more )
- Fixed that blueprints would build partially in chunks not visible by radar from the zoomed-to-world view. ( more )
- Fixed a crash when canceling loading of specific save files. ( more )
- Fixed the programmable speaker GUI wouldn't update correctly. ( more )
- Fixed a bug where text in a text box disappeared after jumping to cursor that is off view.
- Fixed --apply-update not setting executable permissions ( more )
- Fixed that pasting assembler recipe to requester chest would request too few items for some recipes. ( more )
- Fixed crash when exiting the game while a recipe tooltip was open. ( more )
- Fixed positioning of progress bars in mod download dialogs. ( more )
- Fixed creation of overlapping wagons under certain circumstances. ( more )
- Fixed scrolling by caret in a text box that would cause lines to disappear.
- Fixed jittering when driving cars/tanks in some cases. ( more )
- Fixed that only the first blueprint book, blueprint, and deconstruction planner item type would show in the blueprint library. ( more )
- Fixed crash when recalculating connections between roboports. ( more )
- Fixed crash when exiting mod portal during a refresh. ( more )
- Fixed error in saving blueprinted inserters with overridden stack size. ( more )
- Entities waiting for modules can now be fast replaced. ( more )
- Fixed saving of New hope level 2. ( more )
- Fixed that the game would crash trying to load some old saves. ( more )
- Fixed train top speed calculation when not all locomotives used the same fuel type. ( more )
- Fixed roboports wouldn't provide the repair packs for other robots to use when loading saves from 0.15. ( more )
- Fixed a crash when removing modded tiles that had tile ghosts waiting to be built. ( more )
- Fixed a crash when loading saves without specific mods. ( more )
- Fixed that scenario errors would lead to getting stuck on the map preview screen if started through the map preview. ( more )
- Fixed multiple issues with enemy force interaction. ( more )

### Changes

- Removed the mechanics of 3 different fluid tanks in fluid wagon, and simplified it so the fluid wagon has just 1 fluid.
- Ghost belt entities don't connect to other (ghost/or non-ghost) belt entities if they don't have the same force. This prevents ghost belt of other force (invisible to the player) from changing the shape of the belt.
- Building a blueprint on top of existing assembling machines, refineries and chemical plants also copies the rotation, along with the recipe. ( more )

### Scripting

- Added direction, created_by_moving, and shift_build event parameters to on_put_item event.
- Replaced ScrollPane::dont_scroll_horizontally by horizontal_scroll_policy and vertical_scroll_policy.
- Added LuaGameScript::backer_names read.
- Added LuaStyle::want_ellipsis read/write.

### Minor Features

- Added /version command.

## 0.16.6

Date: 18. 12. 2017

### Bugfixes

- Fixed a crash when trying to filter the main inventory in the god-controller. ( more )
- Fixed various crashes caused by mining or otherwise changing power poles. ( more )
- Fixed a desync when using bad values in the /color command. ( more )
- Better handling of the case where we mine our own car but our inventory's full. ( more )
- Fixed placing blueprint over existing Rail Signals does not build wires. ( more )
- Reverted "Number of entities in hand when previewing the entity to be built is now aligned to the entity." It proved to create too big problems with readability while building and running.
- Fixed that rolling stocks in cursor had no icon when there was no valid location for them.

### Scripting

- Fixed that TextBox was not re-layouting text when size was changed through styles.

## 0.16.5

Date: 17. 12. 2017

### Bugfixes

- Fixed boilers outputting water in New hope campaign levels. ( more )
- Fixed slow saving of New hope level 2. ( more )
- Fixed that blueprint books couldn't be built from the zoomed-to-world view. ( more )
- Fixed a crash when loading saves with modded blueprint entities migrated multiple times. ( more )
- Fixed a crash when importing blueprints with circuit connections when a mod had made the entities not circuit connectable. ( more )
- Fixed that forced ghost building (shift + click) didn't work correctly.
- Fixed destroying an entity powered from two electric networks would corrupt future saves. ( more )
- Fixed zooming in on uncharted map areas would reveal tiles on uncharted chunks. ( more )
- Fixed beacon would not highlight labs that are in range of its effects. ( more )
- Fixed disappearing sprites with Low VRAM Mode option enabled. ( more )
- Fixed glitch in one of the stone path transition sprites. ( more )
- Adjusted default graphics options to reflect increased memory requirements for high resolution sprites due to more sprites being converted to high resolution in 0.16.
- Improved very poor performance with video memory usage set to low. ( more )

### Modding

- Fixed circuit connector would not be visible on entities with more than one picture layer. Now the connector will render as 10th layer. ( more )
- Fixed icon_size scaled also icon's dark background in alt mode. ( more )

## 0.16.4

Date: 16. 12. 2017

### Bugfixes

- Fixed progress bar in automatic updates GUI. ( more )
- Fixed crash caused by mouse drag in an empty schedule in Locomotive GUI. ( more )
- Belt rendering fix. ( more )
- Fixed the mining speed for drills would show 1 higher than it actually was. ( more )
- Fixed issue with changelogs in mods. ( more )
- Fixed that the server could crash if it received invalid data. ( more )
- Fixed crash on startup when texture compression was enabled. ( more )
- Fixed that roboport connections wouldn't render as cleanly as 0.15. ( more )
- Fixed that using the /ban command with no parameters would crash the game. ( more )
- Fixed browse mods/games, so the vertical progress bars always keep space for the scroller, so the window doesn't change size when data is loaded, or searching minimizes the result to just a page or less.
- Fixed the game would not enter minimal mode if there was an error in migration script. ( more )
- Fixed the delete-achievements tooltip wouldn't be removed. ( more )
- Fixed the use-recipe-groups config option was ignored in the select-signal GUI. ( more )

### Scripting

- Fixed that LuaPlayer::admin write didn't work. ( more )
- Added 2 optional parameters to LuaSurface::create_entity when creating resource entities: enable_tree_removal and enable_cliff_removal.
- Changed burner prototypes to support fuel_category or fuel_categories + changed the Lua API to match.

## 0.16.3

Date: 15. 12. 2017

### Changes

- When mining normal entities ghost entity selection is disabled until the mining key is released.

### Optimisations

- Train stop penalty is applied when exiting the block with it instead of entering which should prevent searching for long paths just before destination train stop.

### Bugfixes

- Fixed changelog GUI displaying no version when launching the game ( more )
- Fixed crashes and desyncs related to circuit controlled lamps in more electric networks. ( more )
- Fixed advanced rail tutorial no path error. ( more )
- Fixed inventory transfer tutorial furnaces couldn't smelt ore. ( more )
- Fixed unknown locale key in train station tutorial. ( more )
- Fixed new hope level-02 script error. ( more )
- Fixed that the player would die when mining an enclosed vehicle while driving it. ( more )
- Fixed achievement progress bars rendering that caused misalignment of tracked achievements. ( more )
- Fixed that achievement title was sometimes not visible.
- Fixed spacing of effect icons in technology detail. ( more )
- Fixed that the player could teleport over things to get into a vehicle. ( more )
- Fixed the achievement progress bars rendering.
- Fixed that achievements not obtainable with peaceful mode were obtainable with enemy settings lower then default. ( more )
- Fixed that exiting the car whilst shooting could lead to a crash. ( more )
- Fixed that you could not submit a console message if you mapped it to ENTER. ( https://redd.it/7jjlzb )
- Fixed that the value of "bottom" of vertical align was not parsed properly. ( more )
- Fixed crash related to scenario message dialog.
- Fixed very low performance of drawing decoratives on medium or lower video memory usage setting. ( more )
- Fixed that window to select signal wasn't working when sub-groups were enabled but groups disabled. ( more )
- Fixed that LuaGame::take_screenshot would ignore the given surface. ( more )
- Fixed the tank being hurt by its own flamethrower. ( more )
- Fixed updater not properly setting permission bits ( more )
- Fixed that hazard concrete didn't have a walking sound in one rotation. ( more )
- Fixed force-building blueprint rails would build multiple rails on the same location. ( more )
- Fixed that you could copy-paste enemy structure settings. ( more )
- Fixed that double clicking the scroll bar in the save-game GUI would save the game. ( more )
- Fixed that exiting the car with a passenger would leave the car driving in some cases. ( more )
- Fixed that the read stopped train output signal wouldn't show unless the enable/disable checkbox was checked. ( more )
- Fixed amount in resource entity tooltip might be displayed as negative number. ( more )
- Attempted to fix hangs or crashes when using single channel textures for alpha masks on some PCs. ( more )
- Fixed that the deconstruction marker on diagonal rails was off-center.
- Fixed wrong order of buttons in Direct connection password dialogue. ( more )
- Reactor pipes now render correctly, without rotation. ( more )
- Browse games GUI now shows active filter text after reopening the GUI. ( more )
- Fixed incorrect number of rails being used when building with rail planner. ( more )
- Fixed printing of errors in Browse games GUI. ( more )

### Modding

- Fixed JSON parser did not fail on comma at the end of list or dictionary. ( more )

## 0.16.2

Date: 14. 12. 2017

### Bugfixes

- Fixed a crash when using the "flow" custom GUI element type in a mod. ( more )
- Fixed a crash when migrating energy sources from mods. ( more )
- Fixed a crash when a request to mod portal timeouts. ( more )
- Fixed that burner inserters wouldn't fuel burner furnaces in some cases. ( more )
- Fixed blueprint labels wouldn't render in the world. ( more )
- Fixed building entities very quickly could duplicate them in some cases. ( more )
- Fixed a crash when clicking refresh in Browse mods dialog. ( more )
- Fixed a crash when fast-replacing electric poles. ( more )
- Fixed a crash when trying to load mods in zipped format. ( more )
- Fixed a crash when loading saves where the character was in a vehicle which is being removed due to mod removal. ( more )
- Fixed that right click didn't work in the production/electric stats GUIs. ( more )
- Fixed a crash when migrating specific simple-entities to 0.16. ( more )
- Fixed lamp energy info in sidebar and in the Lua interface.
- Fixed that the logistic network embargo achievement didn't disallow the buffer chest.
- Fixed that fast-replace building ghost underground belts and pipes wouldn't rotate the direction correctly.
- Changed (hopefully improved) the heuristic that decides which rail path should be selected for manual rail building.
- Attempt at fixing game not working on macOS 10.12 and older. ( more )

### Modding

- Fixed the game did not check type of units defined in result_units of unit-spawner. ( more )

## 0.16.1

Date: 13. 12. 2017

### Bugfixes

- Changed requirement for parallel loading of high quality sprites to 12 GB of RAM to prevent chance of running out of memory on startup. ( more )
- Fixed that saves with modded progress bar GUI elements couldn't be loaded in 0.16. ( more )
- Fixed crash when loading crop cache from previous game version. ( more )
- Fixed that LuaRemote::call() wouldn't copy string values/keys correctly. ( more )
- Fixed updater would re-launch the game with deprecated --autoupdate-finished parameter.
- Fixed that scroll pane created unnecessary horizontal scroller when squashed vertically (MapPreview, blueprints, probably more) ( more )
- Fixed that the Linux binary was corrupt and wouldn't start. ( more )
- Fixed error checking when compiling GLSL shaders. ( more )
- Fixed artillery would still show as being able to shoot when on enemy forces. ( more )
- Fixed the programmable speaker GUI wouldn't show settings correctly when opened. ( more )
- Fixed graphics of achievements. ( more )

## 0.16.0

Date: 13. 12. 2017

### Major Features

- Added logistic buffer chest. It can request items that are still available to the logistic system.
- Added the artillery wagon and artillery turret which will automatically shoot biter nests and worms.
- Added cliffs. ( more )

### Features

- Train block visualisation.
- Building entities over identical ghosts will revive them. When building a different entity on top of a ghost, settings from the ghost will be copied if possible.
- Train schedules and wait conditions can be rearranged by clicking and dragging.
- New mini-tutorials: Construction robots.
- Belts, underground belts and splitters can now fast replace each other.
- Roboports now provide the repair packs they have for other robots to use.
- Logistic request tooltips now show the count of items in the requester, on the way, and in the network.
- The players main inventory can now be filtered.
- New terrains and new terrain generation.
- All terrains, including stone path and concrete, have transitions with water.
- Map generation dialog now contains a preview of the map.

### Minor Features

- Ctrl-delete now deletes whole word in a text field instead of a single character. ( more )
- Placing output underground belt as ghost properly retains its type as output underground belt. Also underground belts now respect nearby ghosts and become output if there is input ghost nearby. Underground belt and pipe ghosts when hovered show outline of where they will connect ( more )
- Headless server will automatically save the game when the last player leaves and auto-pause starts.
- Added support to disable debug settings for non-admin players in multiplayer through the /config command.
- Dropping items on belts manually (Z) won't spill items if they won't fit on the belt.
- Trees can now be configured in the generate-map GUI.
- Hotkeys can be un-bound by right clicking.
- Rail chain signals can be read by the circuit network.
- Small electric poles and medium electric poles can be fast-replaced with each other.
- In multiplayer players can now ride as passengers in cars/tanks.
- Electric poles and power switches can be opened from the zoomed-to-world view.
- Terrain can be configured in the generate map GUI.
- When holding an offshore pump, all valid build positions will be highlighted.
- After desynching in multiplayer, the game will not automatically connect back, instead a dialog with more information will be shown.
- All map visualisations work also when in zoomed in map mode, where normal view and map view is combined based on radar/player coverage.

### Graphics

- More entities in high resolution: laboratory, radar, worker robots (construction and logistic), combat robots (defender, distractor and destroyer), combinators, electric & circuit wires, pumpjack, storage tank, player, solar panel, lamp, roboport, tank.
- All terrain now supports high resolution.
- Blueprint previews and ghost entities now have their walls, pipes and belts connected.
- New alert icons.

### Balancing

- Removed Assembling machine 1 from the production science pack.
- Changed nuclear reactor stack size to 10.
- Moved cluster grenade recipe to military 4 research.
- Changed uranium ammo prerequisite from military 3 to military 4.
- Explosives now produce 2 per craft.
- Slightly adjusted some recipe craft times to better reflect their ingredient count.
- Changed the terrain building size limit to be based off the player reach.
- Biters scale less with distance and there are generally less biters.
- Resources are much more spread apart. To compensate, patches are larger. Since it's easier to mine, the amount of resources on the map is 3 times less.
- Resources scale slightly less over distance.
- No uranium as a starting resource also no uranium is ever generated near the starting area, you need to go look for it.
- There is 1.49 times more iron on the map to compensate for the extra iron required in a typical game.

### Changes

- Disabled loading of saves before 0.13.0 version (You can use 0.13 to load older saves and re-save them).
- Train doesn't need to come to a full stop when manually changing train destination or switching from manual to automated mode.
- Removed the "shift" value from map generation settings as it wasn't needed anymore.
- Creating blueprints and using deconstruction planner in zoom-to-world map mode now skip entities covered by fog of war. ( more )
- Changed the default autosave interval settings from 2 to 5 minutes.
- It is possible to open/close and interact with the chat console when the map is being saved or server loosing connection dialog is active.
- The game uses only the cloud version of player-data and achievements on steam to avoid problems with resets.
- Increased the limit of recipe categories from 255 to 65535.
- New blueprint no longer includes entities marked for deconstruction.
- Enable Map Exchange String for sandbox games
- Copy Paste from assembler to requester chest now scales with assembler speed and recipe crafting time.
- Blueprints never show the number 1 when held in cursor.
- Robots in the air from personal roboport now count towards logistics requests for that robot type ( more )
- Added /server-save command that does the same thing as lua server_save, but doesn't disable achievements. ( more )
- Gamesave names in the load game dialog that are too long to fit the gui now show in a tooltip in full. ( more )
- Removed the option to turn off the item groups and sub groups from the GUi. It can still be done through the config file or lua commands.
- Added separate control option for placing tags on the map, so by default map scroll is left click, and place tag is right click.
- Allow easier dragging of underground pipes and belts when not moving in a perfect straight line.
- The Arithmetic Combinator can now use a constant as the first parameter, not only the second. So you can do operations like 2^SIGNAL. ( more )
- When building blueprints, any already existing building of the same entity type will have their settings updated instead of showing red. ( more )
- The options menu has been organized better. Some options were moved to a new "Interface" settings menu.
- Updater proxy settings were removed from the options menu. They can still be accessed through the ini file.
- Exchange strings are now compressed before being converted into base64.
- Improved GUI search.
- Added /delete-blueprint-library *player* command to remove blueprints of players from the game.
- The map view will attempt to treat very short clicks as clicks instead of drags to make it easier to click things.
- The explosive cannon shells now target the ground where you shoot.
- Transition from terrain to water is no longer buildable, meaning entities can no longer be built partially on the water.
- Resources will have much less trees on them near the player starting area.
- Tanks no longer take miniscule amounts of damage from hitting trees.
- Previously, building while running at very high speed would create gaps. These are automatically filled now.
- Locomotive will show train ID in its tooltip. The ID can be used in circuit network conditions. ( more )
- When two trains are being merged, the decision which schedule should be used for the merged train has been changed from bigger schedule to schedule that has latest change. ( more )
- Number of entities in hand when previewing the entity to be built is now aligned to the entity.
- Added sliding when the player character collides with water or entities with rotated bounding box.
- Improved drawing of turret radii in blueprint. Many overlapping radii no longer covers terrain completely.
- External blueprint library is no longer merged with blueprint library in save. Instead, in-save library is always overwritten by the external one.

### Bugfixes

- Fixed that train arriving to station could give astronomically big penalty causing trains to go through weird places. ( more )
- Fixed that fluid wagon pumps would sometimes not connect properly ( more )
- Fixed that module icons in blueprint previews wouldn't render correctly in some cases. ( more )
- Fixed long mod manager preview labels would extend out of the frame.
- Fixed that the ~ key couldn't be used to close the console.
- Fixed that the mining progress was reset when mining selection is lost while mining button pressed. ( more )
- Catalysts in recipes are automatically recognized and not counted towards production/consumption statistics. ( more )
- Fixed that ghost rail signal emitted light.
- Fixed that different icon sizes were not scaled properly when drawn in the alt-info mode. ( more )
- Fixed latency sound effects in multiplayer latency hiding would sometimes play too many times.
- Fixed that errors in fonts would give useless errors. ( more )
- Fixed problems related to trains crashing rarely. ( more )
- Disabled possibility to attempt opening invalid save/replay by double click or enter.
- UTF-8 BOM in JSON, INI and LUA files will be ignored instead of causing parsing error. ( more )
- Fixed that clearing all blueprint icons would cause the entire blueprint to be cleared without a warning. ( more )
- Conflicts of multi-modifier hotkeys are now resolved correctly. ( more )
- Fixed sprite rendering at large distances from 0,0. ( more )
- Interacting with a filter slide bar requesting amount over capacity of a full requester won't dispatch robots anymore.
- Fixed restart after the second update in a row crashed the game due to duplicated launch parameter (Linux/macOS). ( more )
- Fixed that "asdf" and "as df" were considered the same when listed in the stop selection. ( more )
- Buildable item counts in inventory in Sandbox mode now update properly with resource changes. ( more )
- Fixed that map width/height accepted value of 0. ( more )
- Fixed crash when loading Vorbis Ogg files with metadata. ( more )
- Fixed that the manual rail building ended up one tile before the cursor. ( more )
- Assembling machine can now output product with amount over stack size. ( more )
- Fixed entity description for resources that require fluids. ( more )
- Possible fix of the problem that map download blocks all other communication and client is disconnected when downloading. ( more )
- Fixed that the game could crash when catching up when processing queued gui actions. ( more )
- Fixed a rare case, when the paused dialog stayed active when reconnecting game after drop. ( more )
- Fixed colored lights would lose their color when nightvision was on. ( more )
- Fixed very bad performance when previewing blueprint with one big connected circuit network. ( more )
- Fixed that an attacking group of biters would sometimes get stuck in a cyclic back-and-forth walking pattern. ( more )
- Fixed that in certain scenarios, the blueprint library wouldn't synchronise. ( more )
- Trains now recalculate next station correctly when more stations are en/disabled at the same tick. ( more )
- Fixed that the server would sometimes quit if a player tried to connect after another player tried to connect unsuccessfully. ( more )
- Fixed when updater requested administrator rights, updated Factorio would be started in elevated mode too. ( more )
- Fixed steam "leaking" outside of storage tank window on high sprite quality setting. ( more )
- Programmable speakers with "Global playback" active won't play for players in a different force.
- Beam weapon now shows correct damage when modded into dealing damage more times during its duration. ( more )
- Fixed that large entities wouldn't render correctly on the map. ( more )
- Fixed that the mining drill wouldn't show the speed bonus in the same format as assembling machines. ( more )
- Fixed the entity icons for combat robots didn't match the item icons. ( more )
- Train can't block its own path anymore. ( more )
- Fixed circuit wire connections wouldn't render correctly in rotated blueprints in some cases. ( more )
- Fixed that changing the system time forwards would cause Factorio to freeze.
- Fixed a crash when changing large circuit networks. ( more )
- Fixed closing window right after it was created would hang the process. ( more )
- Fixed it was possible to open entity GUIs from zoom-to-world when holding some items in cursor. ( more )
- Fixed that negative a productivity bonus would show in entity GUIs and create negative progress bars. ( more )
- Fixed that when biters were attacked but couldn't find a path to the attacker, they would stoically accept their fate. ( more )
- Fixed that the multiplayer-waiting icon wouldn't render in the map view. ( more )
- Fixed global achievement progress was multiplied by number of player in multiplayer game. ( more )
- Fixed that passing a LuaObject instead of a plain Lua table to LuaBootstrap::raise_event would crash the game. ( more )
- Fixed setting active=false then true on a beacon wouldn't update the beacon correctly. ( more )
- Possible fix of a crash when a player leaves when a blueprint is being transferred. ( more )
- Fixed that the rocket silo would get stuck if it died and was re-built by robots while launching the rocket.
- Fixed transport belt circuit connector would draw over splitter in front of it. ( more )
- Fixed that it was still possible to get some achievements in a replay. ( more )
- Fixed that circular references passed through the Lua remote interface would crash the game. ( more )
- Fixed missing personal robot recharging animation when character was in a vehicle. ( more )
- Fixed that vertical size of progress bar wasn't respecting the gui scale.
- Fixed that the number drawn next to cursor when item is held was differently positioned compared to how it is in the inventory.
- Fixed texture compression would not be disabled when d3dx9.dll is not installed, corrupting sprites that were expected to be compressed.

### Optimisations

- Improved performance of transport belts about x5 times. ( more )
- Added prefetching of the next entity in the update loop improving overall update performance by approx. 10 %.
- Improved performance of Item manipulation (4% effect on the overall performance).
- Improved performance of crafting machine (furnace/assembling machine) (2% effect on the overall performance).
- Improved performance of electric network transfer more than twice. (10% effect on the overall performance).
- Improved performance of smoke greatly. (2.5% and more effect on big factories).
- Improved performance when building rail blocks with many segments.
- Improved performance of logistic provider and requester chests.
- Improved performance of blueprint previews (the GUI and holding it in the world).
- Improved game startup time when a sufficiently powerful computer is detected.

### Modding

- Train path finding penalty values are now in utility-constants, to make it viewable and moddable.
- Fixed storage tank with non-square collision box would not align to tiles in all rotations properly. ( more )
- Fixed belt-immunity equipment so it now works on cars.
- Fixed that the radius property for the area trigger effect was called perimeter.
- Fixed that crafting machine with non-square bounding box was not rotatable. ( more )
- Removed default values for icon_size, so icon_size is now required property. ( more )
- Updated the serpent library to version 0.30.
- Changed the "item that builds this" list for entities so it's sorted first by ItemPrototype::primary_place_result_item and then by normal item prototype sort order.
- Changed default value of InserterPrototype::allow_custom_vectors to false.
- Changed "Nothing" technology effect "effect_key" to "effect_description" and changed it to accept localised strings.
- Changed rocket silo prototype "result_items" to be defined in the item as either "rocket_launch_product" or "rocket_launch_products".
- Changed the string mod setting type so it will attempt to localise items in the dropdown using "string-mod-setting.mod-name-setting-name-dropdown-item".
- Changed technology modifier icons so they can be defined per-modifier-type instead of always using the red "+" icon.
- Changed LuaObject::destroy() so it won't error if called on invalid objects.
- Changed mod settings so the game will remember settings from removed mods should they be re-added in the future.
- Changed how TilePrototype::transition_merges_with_tile works. See ( more ) for more details.
- Scenarios can contain folders with arbitrary names.
- Added 'single_line' and 'want_ellipsis' to Label style specification.
- Added force bonus for following robot time to live.
- Added force bonus for research productivity.
- Added ability to import and export item-with-tags to/from strings.
- Added support for fast-replacing character entities.
- Added CombatRobotPrototype::light .
- Added TurretPrototype::alert_when_attacking .
- Added optional 'respawn_time' (in seconds) to the character entity.
- Added "hide-from-bonus-gui" entity and item prototype flags.
- Added support for mods to disable custom-input prototypes of other mods.
- Added support for mods to show changelogs (following the same format as the core game changelog).
- Added MapGenSettings support to fully define which autoplace definitions are used for a given surface.
- Added AutoplaceSpecification::default_enabled - if a given autoplace specification should be enabled without being explicitly enabled in map gen settings.
- Added allowed_effects support to the mining drill.
- Added optional "has_belt_immunity" property to the unit and car prototype.
- Added optional "hidden" prototype property to the achievement prototype.
- Added support to link custom-input prototypes directly to game controls instead of having them act as their own control.
- Added a new entity type "infinity-container" that can automatically add/remove items from itself; useful for scenarios and modding.
- Added support for incompatible dependencies.
- Added an entity prototype flag "hide-alt-info" to never show alt-info for a given entity.
- Added distance bonus support to the mining tool item type.
- Added InserterPrototype::draw_held_item .
- Added FluidPrototype::fuel_value and Generator::burns_fluid .
- Added mod-developer support to runtime change autoplace specifications enabled through the command line option --enable-runtime-autoplace-modification using F2 in-game.
- simple-entity, simple-entity-with-owner and simple-entity-with-force can now define 'animations' instead of 'picture' or 'pictures'.

### Scripting

- Fixed that LuaSurface::get_trains() didn't work for trains without locomotives. ( more )
- Fixed that reversing technology effects in different orders than they where researched could lead to a non-zero number. ( more )
- Fixed surface_index was off by 1 for on_player_built_tile and on_player_mined_tile events.
- Fixed possible desync when teleporting underground belt ghosts and pipe to ground ghosts.
- Changed the robot_built and player_built events to pass the item stack used to do the building instead of the item name and tags.
- Changed "on_preplayer_mined_item" to "on_pre_player_mined_item".
- Changed LuaEntity::recipe to LuaEntity::get_recipe() and LuaEntity::set_recipe() .
- Changed LuaSurface::regenerate_decorative /regenerate_entity to accept zero arguments and regenerate everything.
- Changed the root custom gui containers (top, left, center, goal) to have the corresponding name.
- Changed the event data from script.raise_event will contain mod_name, the name of the mod that raised it.
- Changed LuaFluidBox fluid from {type="...", amount=...} to {name="...", amount=...}
- Changed name of colspan parameter of table to column_count.
- Changed LuaItemPrototype::group_filters and sub_group_filters to item_group_filters and item_subgroup_filters to match the prototype values.
- LuaEntity::set_recipe() returns the items removed from the entity as a result of setting the new recipe (if any).
- Moved Mod-gui button flow to gui.top.
- Removed LuaEntity::passenger read/write.
- Added style::width /height to set maximal/minimal value at the same time.
- Added style::align to set the align of inner elements.
- Added style::stretchable / squashable.
- Added LuaEntity::get_driver() , set_driver(), get_passenger(), and set_passenger().
- Added LuaGuiElement::hovered_sprite and clicked_sprite read/write methods for the SpriteButton.
- Added support to change daytime length and brightness on a per-surface basis.
- Added GameViewSettings show_rail_block_visualisation property that forces the visualisation to be always on.
- Added LuaItemStack::export_stack and LuaItemStack::import_stack to export/import supported items to/from strings.
- Added LuaEntity::tree_color_index read/write access and LuaEntityPrototype::tree_color_count read access.
- Added LuaEntity::selection_box and secondary_selection_box read.
- Added LuaBootstrap::mod_name read.
- Added LuaControl::in_combat read.
- Added LuaTile::order_deconstruction() and cancel_deconstruction().
- Added optional cause and force to LuaEntity::die() .
- Added on_player_used_capsule event.
- Added on_player_promoted and on_player_demoted events.
- Added on_player_changed_position event.
- Added LuaEntityPrototype::alert_when_attacking read and LuaEntityPrototype::alert_when_damaged read.
- Added LuaEntity::power_switch_state read/write.
- Added on_combat_robot_expired event.
- Added LuaEntity::relative_turret_orientation read/write for vehicles with turrets.
- Added LuaEntityPrototype::color read.
- Added LuaTrain::passengers .
- Added LuaEntityPrototype::collision_mask_collides_with_self read.
- Added "fluid", and "recipe" type to the choose-elem-button custom GUI element.
- Added LuaGuiElement::locked read/write - when true the given choose-elem-button can only be changed through script.
- Added an optional parameter to LuaSurface::drop_item_stack to mark dropped items for deconstruction.
- Added LuaForce::cancel_charting (...).
- Added LuaSurface::force_generate_chunk_requests() .
- Added support for setting a LuaGuiElement as the opened GUI for a player causing it to close with the normal close-GUI methods.
- Added on_gui_opened and on_gui_closed events.
- Added on_player_muted/unmuted and on_player_cheat_mode_enabled/disabled events.
- Added LuaItemStack read properties to tell if a given item is some specific item type.
- Added LuaAutoplaceControlPrototype, LuaNoiseLayerPrototype, LuaModSettingPrototype, and LuaCustomInputPrototype.
- Added LuaGameScript autoplace_control_prototypes, noise_layer_prototypes, mod_setting_prototypes, and custom_input_prototypes read.
- Added LuaForce::reset_evolution() .
- Added LuaSurface::create_trivial_smoke() .
- Added LuaPlayer::enable_recipe_groups() and enable_recipe_subgroups().
- Added LuaItemStack::rocket_launch_products read.
- Added on_mod_item_opened event.
- Added LuaItemPrototype::can_be_mod_opened read.
- Added the item stack index as a second return value to LuaInventory::find_item_stack .
- Added LuaItemStack::transfer_stack() .
- Added LuaGuiElement type "slider".
- Added on_gui_value_changed event - fired when a slider value changes.
- Added optional color field as a second parameter to the 4 print functions.
- Added support to change LuaSurface::map_gen_settings runtime.
- Added LuaEntityPrototype::allowed_effects read.
- Added LuaEntity::effects read.
- Added LuaPlayer::can_place_entity() , can_build_from_cursor(), and build_from_cursor().
- Added LuaSurface::play_sound() .
- Added LuaForce::play_sound() .
- Added LuaGameScript::play_sound() and is_valid_sound_path().
- Added LuaPlayer::play_sound() .
- Added support to teleport train stops, rail signals, walls, gates, and entities with fluidboxes.
- Added LuaEntity::rotate() .
- Added LuaEntity::get_infinity_filter() and set_infinity_filter().
- Added LuaEntity::infinity_filters and remove_unfiltered_items read/write.
- Added LuaEntityPrototype::rocket_parts_required read.
- Added LuaEntityPrototype::fixed_recipe read.
- Added LuaGameScript::kick_player() , ban_player(), unban_player(), purge_player(), mute_player(), and unmute_player().
- Added LuaPlayer::admin write support.
- Added LuaGuiElement::focus() .
- Added on_character_corpse_expired event.
- Added on_pre_ghost_deconstructed event.
- Added on_player_pipette event.
- Added LuaEntity::character_corpse_player_index , character_corpse_tick_of_death, and character_corpse_death_cause read/write.
- Added LuaSurface::get_tile_properties() .
- Added LuaSurface::can_fast_replace() .
- Added support for player associated characters - characters that get logged off/on with a given player but aren't directly controlled by the player.
- Added LuaEntity::associated_player read/write.
- Added LuaPlayer::get_associated_characters() , associate_character(), and disassociate_character().
- Added LuaPlayer::ticks_to_respawn read/write.
- Added old_state to the on_train_changed_state event.
- Added LuaRecipe::catalysts read.
- Added LuaRecipe::hide_from_flow_stats read/write.
- Added LuaRecipePrototype::hidden_from_flow_stats read.
- Added LuaEntity::tick_of_last_attack and tick_of_last_damage read for the character entity.
- Added LuaLogisticNetwork::passive_provider_points and active_provider_points read.
- Added LuaPlayer::display_resolution read.
- Added on_player_display_resolution_changed event.
- Added LuaPlayer::display_scale read.
- Added on_player_display_scale_changed event.
- Added LuaTrain::weight and riding_state read.
- Added LuaEntity::products_finished write.
- Added optional surface to game.take_screenshot(...).
- Added LuaEntityPrototype::construction_range and logistics_range read.
- Added LuaGuiElement::index read.
- Added LuaForce::max_successful_attempts_per_tick_per_construction_queue and max_failed_attempts_per_tick_per_construction_queue read/write + technology modifiers.
- Added LuaGuiElement::mouse_button_filter read/write for buttons and sprite-buttons.
- Added LuaSurface::find_tiles_filtered() and count_tiles_filtered().
- Added LuaEntity::get_train_stop_trains() .
- Added LuaLogisticNetwork::force read.
- Added LuaItemStack::item_number read - the unique ID of the item if it has one.

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
