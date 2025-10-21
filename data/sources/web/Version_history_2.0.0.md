---
title: Version history/2.0.0 - Factorio Wiki
source: https://wiki.factorio.com/Version_history/2.0.0
scraped_at: 2025-10-21 14:29:19
tags: [web, documentation]
---

# Version history/2.0.0 - Factorio Wiki

**Source:** [https://wiki.factorio.com/Version_history/2.0.0](https://wiki.factorio.com/Version_history/2.0.0)

## 2.0.71

Date: 16.10.2025

### Bugfixes

- Fixed asteroid collector navmesh would in rare cases be stuck computing forever. ( more )
- Fixed crash on Intel Macs with Intel Iris Plus Graphics by disabling GPU timings for those cards.
- Fixed freeze with unknown cause when placing rails. ( more )

## 2.0.70

Date: 13.10.2025

### Bugfixes

- Fixed scripted technology trigger was unable to load layered icons. ( more )
- Fixed tips and tricks item was unable to load layered icons.
- Fixed stomper stomp sound playing way too many times when dying by stomping in a mine field. ( more )
- Fixed electric turret was suggesting it is possible to read ammo. ( more )
- Fixed a crash when artillery turret didn't have rotating_sound defined even though it's optional. ( more )
- Fixed startup crashes on some Intel Macbook Pros. ( more )
- Fixed that changing player's character could cause equipment related events to not fire. ( more )
- Fixed upgrading programmable speaker would clear settings. ( more )
- Fixed that LuaPlayer::can_build_from_cursor would play the not-allowed sound when out of reach. ( more )
- Fixed that on_chart_tag_modified was not called when name/icon was modified by script. ( more )
- Fixed a crash when a surface is deleted while viewing a ping tooltip for that surface. ( more )
- Fixed some OpenGL lighting issues when light occlusion was enabled.
- Fixed color saturation problems on some Intel Macs. ( more )
- Fixed crashes on Intel Macs with AMD GPUs by disabling GPU timings for those cards.
- Fixed a crash when robots try to charge at a roboport that only supports charging when using quality. ( more )

### Modding

- Added CargoStationParameters::is_input_station and ::is_output_station to mainly clarify tooltips. ( more )

## 2.0.69

Date: 29.09.2025

### Bugfixes

- Fixed some combinations of surface properties would cause robots to consume NaN amount of energy. ( more )
- Fixed upgrading underground belts in a blueprint would not preserve underground belt type. ( more )
- Fixed that upgrading fuel in blueprints could result in invalid fuel requests. ( more )
- Fixed that super-force-building would not generate a player-rotated event. ( more )
- Fixed a crash when script checks if a space platform can leave when it was not yet built. ( more )
- Fixed a crash when a modded character entity without a character corpse defined dies. ( more )
- Fixed custom tooltip fields were not showing for modded recipes. ( more )
- Fixed some gui widgets were not selectable when inside of a long table that is scrolled to only show last row. ( more )
- Fixed proxy container interaction with agricultural tower. ( more )
- Fixed spoil products of recipe products were not listed as possible recipe trash. ( more )
- Fixed LuaRendering rich text in game render mode being drawn above fog of war. ( more )
- Fixed (super)forcing entity requiring tile would sometimes not trigger deconstruction of an obstacle despite said obstacle blocking revival of autofilled tileghost. ( more )

### Modding

- Added MiningDrillPrototype::resource_searching_offset.
- Added "scripted" technology trigger.
- Added FluidWagonPrototype::connection_category.

### Scripting

- Added on_player_dropped_item_into_entity event.
- Added LuaItemCommon::entity_logistics_enabled and entity_enable_logistics_while_moving read/write.
- Added LuaItemCommon::entity_driver_is_gunner, entity_auto_target_without_gunner and entity_auto_target_with_gunner read/write.
- Added maximum_quality_jump utility constant.
- Added LuaEntity::mining_area read.
- Added LuaForce::script_trigger_research().

## 2.0.68

Date: 23.09.2025

### Graphics

- Made Metal the default graphics rendering API for Macs.
- Deprecated OpenGL support on Macs. It will still exist for older versions of macOS, but may not receive future updates.
- Removed Graphics backend user setting.

### Bugfixes

- Fixed a crash with some menu simulations and mods. ( more )
- Fixed a crash when entities are removed while their GUI is being interacted with. ( more )
- Fixed a crash after migrating a frozen assembling machine fluidbox that has fluid contents. ( more )
- Fixed undo actions for removed entities would not keep underground belt type. ( more )
- Fixed LuaSplitterControlBehavior was missing fields from LuaControlBehavior. ( more )

## 2.0.67

Date: 22.09.2025

### Minor Features

- Partially fulfilled wait conditions use different background color to indicate progress.
- Splitters can be connected to circuit network.

### Changes

- Added absorbed pollutant name to tile description in Factoriopedia.
- Changed manual mining when the inventory is full to not drop the mined result on the ground.
- Improved the mod API search to find union literals, define leaf nodes, and more.

### Graphics

- Fixed Metal graphics backend throttling the FPS when the display refresh rate isn't a multiple of 60 Hz. ( more )

### Bugfixes

- Fixed LuaSegmentedUnit::acceleration calculations in some situations. ( more )
- Fixed combinator's red and green wires would overlap when built vertically. ( more )
- Fixed a crash when tile-effect texture filename is invalid. ( more )
- Fixed that hiding an autoplace control did not remove it from the map generator GUI.
- Fixed multisample noise operation not working properly for LuaSurface.calculate_tile_properties(). ( more )
- Fixed technology slots drawing ingredients when research trigger is also specified. ( more )
- Fixed rail support drawing box in GUI widgets.
- Fixed a consistency issue when copying settings between loaders in some cases. ( more )
- Fixed demolisher kills being counted twice in the kill statistics. ( more )
- Fixed a crash when writing LuaStyle::clicked_font_color on labels. ( more )
- Fixed UI scaling and alignment issues when the window content scale is changed during loading. ( more )
- Fixed a crash when migrating agricultural towers. ( more )
- Fixed a crash when showing modded technology effects. ( more )
- Fixed that fluid could pass through frozen machines. ( more )
- Fixed copying train stop settings would send trains to a train stop in some cases. ( more )
- Fixed a charting issue with pentapods. ( more )
- Fixed thruster tooltip was not showing quality indicator on the thrust line. ( more )
- Fixed a desync when a car or spidertron with toolbelt equipment is destroyed. ( more )
- Fixed that fast replacing a train stop could fail to preserve train stop limit. ( more )
- Fixed heat flow between heat pipes that have different default temperature. ( more )
- Fixed that the too-many-trees achievement check was backwards. ( more )
- Fixed that resource entities were not protected from tile removal even if set that they should be. ( more )
- Fixed a crash when minimap GUI elements would try to view deleted surfaces. ( more )
- Fixed biters could be distracted when told not to be distracted in some cases. ( more )
- Fixed selector combinator's update interval was not covered by blueprint parametrisation. ( more )
- Fixed some alert icons were using wrong colors. ( more )
- Fixed that blueprint parametrisation could cause splitter filter to be cleared causing mode of operation to change. ( more )
- Fixed a crash when selecting an underground belt without an underground_sprite.
- Fixed issue with selector combinator random interval and formulas is gui. ( more )
- Fixed that LuaPlayer::can_build_from_cursor() did not check build distance. ( more )
- Fixed a style issue with labels in buttons when changing the enabled state of the button. ( more )
- Fixed a crash when editing decider combinator constants in some cases. ( more )
- Fixed a crash when editing interrupts on space platforms. ( more )
- Fixed a crash when migrating linked containers. ( more )
- Fixed a crash when teleporting or changing the direction of asteroid collectors. ( more )
- Fixed entities with tile_buildability_rules crashing the game when rotated to non-cardinal direction.
- Fixed sound of a machine with its GUI opened not fading out on game pause. ( more )
- Fixed that custom inputs would not fire if there were game GUI controls with the same key bindings. ( more )
- Fixed that disabled trigger technologies were still researchable. ( more )
- Fixed a crash and the back button in map generator GUI when map width or height were out of range. ( more )
- Fixed that remote view dragging wasn't cancelled when the game was paused. ( more )
- Fixed that rail signals did not rotate automatically to a valid direction in forced and super-forced build modes when they collided with tiles. ( more )
- Fixed that tips and tricks simulations could show the "game finished" screen when mods didn't rewind them to the beginning. ( more )
- Robots with construction task of elevated entity will not queue more tasks - fixes some cases of some jobs never getting done. ( more )
- Fixed cancelling deconstruction of entity colliding with both an entity ghost and a tile ghost supporting said entity ghost sometimes crashing. ( more )
- Fixed undoing after manually mining tile that had cover ghost tile on it would not restored said cover tile ghost. ( more )
- Fixed the surfaces list in remote view not scrolling when using the "Select next/previous surface" hotkeys. ( more )
- Fixed that blueprint book LuaRecords in a preview state could not be read. ( more )
- Fixed that players could enter vehicles marked for deconstruction. ( more )
- Fixed selection tool could select tile ghosts when it was not configured for selecting tiles. ( more )
- Fixed that car light animation with apply_runtime_tint enabled was always black. ( more )
- Fixed personal laser equipment was not showing under ammo category in facotriopedia. ( more )

### Modding

- Removed "research-progress" product type from RecipePrototype.
- Added RobotWithLogisticInterfacePrototype::max_payload_size_after_bonus.
- Added FusionGeneratorPrototype::burns_fluid.
- Added FusionGeneratorPrototype::effectivity.
- Changed Generator and FusionGenenerator tooltips to not show temperatures when in burns_fluid mode.
- Added support for heating_energy to FusionGeneratorPrototype and ThrusterPrototype.
- Added recipe_icon_scale chart utility constant.
- Added LightningPrototype::attractor_hit_effect.
- Added RoboportPrototype::render_recharge_icon.
- Changed CargoWagonPrototype to use EntityPrototype::icon_draw_specification when drawing cargo wagon content.
- Changed DisplayPanelPrototype to use render_layer from icon_draw_specification when drawing icon.
- Added __TECHNOLOGY__ and __RECIPE__ built-in locale parameters.

### Scripting

- Added LuaPlayer::get_recipe_notifications().
- Added LuaPlayer::swap_characters().
- Added flip_horizontal and flip_vertical parameters to LuaPlayer::build_from_cursor().
- Added skip_fog_of_war to LuaPlayer::can_build_from_cursor().
- Added LuaCustomChartTag::position and surface write.
- Added LuaFluidBox::get_fluid_segment_extent_bounding_box().
- Added LuaItemPrototype::get_module_effects().
- Added LuaInventory::get_item_count_filtered().
- Added LuaInventory::get_item_quality_counts().
- Added LuaLogisticNetwork::custom_name read/write.
- Added LuaRecord::export_record().
- Added LuaRecord::get_selected_record().
- Added LuaEntity::transitional_request_target read.
- Added LuaEntity::rail_length read.
- Added LuaEntity::get_movement() and set_movement().
- Added LuaHelpers::multilingual_to_lower().
- Added LuaEntityPrototype::get_attraction_range_elongation() and get_energy_distribution_efficiency().
- Added LuaEntityPrototype::fluid_buffer_size, activation_buffer_ratio and fluid_buffer_input_flow read.
- Added LuaEntityPrototype::spider_engine read.
- Added LuaEntityPrototype::range_from_player, combat_robot_friction, destroy_action and follows_player read.
- Added LuaEntityPrototype::strike_effect, attractor_hit_effect, damage and energy read.
- Added LuaEntityPrototype::support_range read.
- Added LuaGuiElement::icon_selector read.
- Added LuaItemCommon::entity_logistic_sections and entity_request_from_buffers read/write.
- Added custom_tooltip_fields reads to all LuaPrototypes that support it.
- Added on_cargo_pod_started_ascending event.
- Added previous_target and previous_quality to on_marked_for_upgrade event.
- Added in_gui to custom input events.
- Added LuaSplitterControlBehavior.
- Added surface_index to all UndoRedoActions.
- Changed LuaSpacePlatform::destroy_asteroid_chunks() to return the number of destroyed chunks.
- Changed LuaEntity::color read/write to also work for character corpses.

## 2.0.66

Date: 02.09.2025

### Minor Features

- Windows executables now undergo code signing.

### Changes

- Reverted belt building changes from 2.0.61.

### Bugfixes

- Fixed that blueprints made from ghosts would not be included in the on_player_setup_blueprint event. ( more )
- Fixed a consistency issue when rotated entities are moved by belts. ( more )
- Fixed modded mining drills with filters would not keep filters when upgrading. ( more )
- Fixed that the time usage entry for "Multiplayer UPS" did not work. ( more )
- Fixed a crash when changing research state during the configuration changed event. ( more )
- Fixed that deconstruction planner was ignoring quality of items on ground. ( more )
- Fixed captive biter spawners would not get damaged while not producing if friendly fire was disabled. ( more )
- Fixed that reading roboport logistic requests in networks with buffer chests did not behave correctly. ( more )
- Fixed remembered zoom levels when going back and forth in the browse history.
- Fixed a crash when saving after parametrising a blueprint that caused filters to merge in some cases. ( more )
- Fixed train stops with priority above 90 would get priority clamped to 90 inside of a blueprint. ( more )
- Fixed util.mul_shift not accepting struct. ( more )

### Modding

- Added color mod setting "forced_value".
- InserterPrototype::pickup_position and insert_position are no longer checked for being too close to tile edge.

### Scripting

- Added an "overflow" inventory option to LuaEntity::revive and silent_revive.
- Added LuaEntityPrototype::icons_positioning and icon_draw_specification read.
- Added LuaRenderObject::dash_offset read/write.
- Added tile_condition to LuaItemPrototype::place_as_tile_result.
- Changed LuaAchievementPrototype::to_kill and module to returns arrays of LuaPrototypes instead of arrays of strings.
- Added LuaRecord::is_preview read.
- Added LuaGameScript::allow_debug_settings read/write.

## 2.0.65

Date: 22.08.2025

### Bugfixes

- Fixed that freezing and thawing underground belts would move items slightly. ( more )
- Fixed super-forcing gates and walls would sometimes cause deconstruction of adjacent curved rail ghosts( more )
- Fixed that opening rich text in map view could send a click action to opened GUIs. ( more )
- Fixed that switching between normal and remote view would close the blueprint setup GUI. ( more )
- Fixed a crash with running replay headless when game wants to show notifications. ( more )
- Fixed selector combinator wire connector shadow position. ( more )
- Fixed that some entities did not draw fluid box connection pipes. ( more )
- Fixed that the home key did not work in the manage mods GUI. ( more )
- Fixed that the undo item was not yet in the player queue during the entity built event. ( more )
- Fixed a crash when a mod puts item request proxies into the player undo queue. ( more )
- Fixed that several entity types would not account for drain in their energy buffer. ( more )
- Fixed stomper corpses graphics. ( more )
- Fixed that cloning some entities while they contained spoilage would result in the clone getting stuck. ( more )
- Fixed LuaEntity::display_panel_icon was not accounting for nil. ( more )
- Fixed that migrating entities with quality would not preserve the quality. ( more )

### Modding

- Heat energy sources support pollution.
- Omitting required_tiles in a tile_buildability_rules's item now default to "all" (instead of "none" which was making the entities unbuildable) ( more )
- Added EntityPrototype::draw_stateless_visualisations_in_ghost.
- Added LoaderPrototype::respect_insert_limits.

### Scripting

- Changed LuaParticlePrototype::render_layer, render_layer_when_on_ground and LuaTrivialSmokePrototype::render_layer to be strings instead of integers.

## 2.0.64

Date: 12.08.2025

### Minor Features

- Heat interface can now heat entities and tiles.

### Changes

- Changed the blueprint setup GUI description field to include the icon picker. ( more )

### Bugfixes

- Fixed that belts in the blueprint GUI did not animate. ( more )
- Fixed a crash when a beam attack trigger destroys the turret firing it. ( more )
- Fixed a crash when pressing end, home, page up or page down key while the alerts GUI was focused. ( more )
- Fixed a crash when loading a save file with furnaces that are crafting a recipe with custom fluidbox indexes set. ( more )
- Fixed that the on_research events pushed the player index using the wrong name. ( more )
- Fixed that train route highlighting didn't work when riding in non-locomotives. ( more )
- Fixed that the remote view minimap always focused on the physical player position when in remote view. ( more )
- Fixed a crash when cloning moving trains in some situations. ( more )

### Scripting

- Added LuaItemCommon::blueprint_description read/write.
- Added LuaRecord::blueprint_description read/write.
- Added LuaControl::render_position read.
- Added LuaControl::flight_height read.
- Added LuaControl::is_flying read.
- Added LuaEntity::created_by_corpse read.
- Added heat pipe to LuaEntity::neighbours read.
- Added LuaEntity::heat_neighbours read.
- Added LuaPlanet::get_space_platforms().
- Added LuaEntity::priority_targets read.

## 2.0.63

Date: 04.08.2025

### Bugfixes

- Fixed that --dump-icon-sprites would shift icons south-east by one pixel. ( more )
- Fixed boilers consuming hot input fluid would not produce enough steam. ( more )
- Fixed spider unit graphic layers with 'apply_runtime_tint' would not use the force color. ( more )
- Fixed that drag building with smart belt building disabled would remove belts in some cases. ( more )
- Fixed that space platform construction requests would not request more repair packs after running out. ( more )
- Fixed a crash when rendering latency players in some cases. ( more )

## 2.0.62

Date: 31.07.2025

### Bugfixes

- Fixed a crash when furnace that is crafting is cloned.

## 2.0.61

Date: 30.07.2025

### Changes

- When dragging belts, going forward and back will remove the extra belts built.
- When using smart belt building to make a turn, the player can decide to change the direction after the turn by dragging in the opposite direction.
- Don't change gamepad selection center when the character starts flying in mech armor. ( more )
- Improved the GUI responsiveness in the display panel. ( more )

### Graphics

- Fixed that playing in fullscreen with the Metal graphics backend could look blurry if "Render in native screen resolution" was off.
- Changed "Render in native screen resolution" graphics setting to no longer require a game restart.

### Bugfixes

- Fixed minimap bobbing up and down when the character is in mech armor.
- Fixed that spidertrons built from script did not default to request-from-buffers. ( more )
- Fixed that overlapping tile ghosts would not draw on the map. ( more )
- Fixed that the game would attempt to load Mac specific filesystem files. ( more )
- Fixed a crash related to underground belts when super force building. ( more )
- Fixed pentapod leg mount positions  when the body is rotated.
- Fixed pentapod orientations getting incorrectly warped.
- Fixed that cloning rockets with attached cargo pods did not work correctly. ( more )
- Fixed that removing territory noise expressions made saves which used them not loadable.
- Fixed research completed sound playing for all forces.
- Fixed that furnaces could keep using a recipe they should not be able to use after a migration.
- Fixed that furnaces were not considering recipe with no ingredients as not craftable.
- Fixed a crash when inserter tries to insert item into a furnace which is currently crafting a recipe with no item ingredients. ( more )
- Fixed a crash when using send_udp fails. ( more )
- Fixed that rail ramp ghosts would block ground rail ghost construction. ( more )
- Fixed on-screen-keyboard opening on top of the search field in the technology GUI.
- Fixed graphics rendering unpausing while still minimized on macOS in some special circumstances. ( more )
- Fixed crash if a simulation gets paused.
- Fixed a crash if a player using the editor equips an equipment with a burner component.
- Fixed that a player using the editor could not activate electric discharge equipment and other manually-activated equipment.
- Fixed that resetting control settings wouldn't update control tooltips. ( more )
- Fixed that cliff bounding boxes could be defined in an invalid way. ( more )
- Fixed that inventory filters were ignored when in the train fuel GUI. ( more )
- Fixed loaders could get stuck when taking from asteroid collectors when one lane of a belt was blocked. ( more )
- Fixed that inserters could get stuck inserting items into rogue spawners when picking from belts. ( more )
- Fixed a crash when attempting to render a linked fluidbox connection.
- Fixed frozen pumpjack could not match frozen sprite. ( more )

### Modding

- Added demolisher and territory API.
- Added RecipePrototype::hide_from_bonus_gui.
- Moved LuaPlayer::can_place_entity to LuaControl::can_place_entity so that it can be called on character entities. ( more )
- Changed pentapods to prioritize using the torso base sprite to control rotations, or if no base sprite is defined, the head sprite is used.
- Added ability for SpiderVehicles to rotate their legs like pentapods when provided with a base sprite that has rotation frames. ( more )
- Added LuaPlayer::set_zoom_limits() to set zoom limits for any controller type. ( more )
- Added SpaceLocationPrototype::starmap_icon_orientation.

### Scripting

- Added LuaForce::get_chunk_chart(surface, position).
- Added LuaEntity::apply_upgrade().
- Added LuaEntity::pumped_last_tick read.
- Added LuaEntityPrototype::tile_buildability_rules read.
- Added agricultural tower events: on_tower_planted_seed, on_tower_pre_mined_plant, and on_tower_mined_plant.
- Changed LuaEntity::copy_color_from_train_stop and vehicle_automatic_targeting_parameters to work on ghosts.
- Added LuaEntity::register_tree().
- Added register_plant to LuaSurface::create_entity.

## 2.0.60

Date: 10.07.2025

### Changes

- Moved the ammo turret request-slot closer to the turret center visually. ( more )

### Bugfixes

- Fixed a crash when removing transport belts or walls with wires in blueprints.
- Fixed that the show-train-signals debug option didn't render correctly for elevated signals. ( more )
- Fixed that changing a trains group would not always refresh interrupt names in the GUI. ( more )

## 2.0.59

Date: 09.07.2025

### Changes

- Remastered and remixed music.
- More icons in factoriopedia made unique.

### Optimizations

- Improved performance when holding blueprints.

### Graphics

- Improved frame rate stability of Metal graphics backend
- Improved rendering performance of busy scenes of Metal graphics backend

### Bugfixes

- Fixed that teleporting a car to another surface would invalidate lua references to non-player characters in it. ( more )
- Fixed that LuaSurface::create_entity() using the 'item' parameter did not work for vehicle equipment grids. ( more )
- Fixed that choose-elem-button with id-with-quality didn't respect prototype filters. ( more )
- Fixed that LuaFlowStatistics::[input, output, storage]_counts read didn't merge qualities. ( more )
- Fixed that some entities would collide with nearby tiles when they shouldn't. ( more )
- Fixed that mod-defined fonts did not apply correctly when first starting the game. ( more )
- Fixed a crash when using LuaItemStack::deconstruct_area() in some cases. ( more )
- Fixed electric mining drills were able to stack items when at high mining productivity. ( more )
- Fixed a disconnect when viewing tips and tricks in multiplayer. ( more )
- Fixed quickbar selection getting stuck when trying to pick a blueprint book from the blueprint library that didn't finish downloading. ( more )
- Fixed blueprint book download progress drawing sometimes being broken.
- Fixed that large values given for LuaSurface::find_entities_filtered(radius) would crash the game. ( more )
- Fixed that equipment ghosts couldn't be added to armor when not worn. ( more )
- Fixed that you could place or take blueprint items from chests in remote view. ( more )
- Fixed that you couldn't open reactors with a void energy source. ( more )
- Fixed that the sync mods confirmation did not have the draggable texture. ( more )
- Fixed that LuaSurface::create_entity() did not work correctly with quality. ( more )
- Fixed that remote fast transfer of modules could downgrade modules with higher quality. ( more )
- Fixed that remote driving didn't raise on_player_driving_changed_state event when entering a vehicle. ( more )
- Fixed beacons with supply area distance of 0 not showing radius visualisation. ( more )
- Fixed Game Mode not enabling on macOS 26
- Fixed that space location wouldn't read starmap_icons if starmap_icon didn't exist. ( more )
- Fixed mipmaps for fulgoran ruin vault icon. ( more )
- Fixed that flush-fluid would not flush fluid from fluid energy sources. ( more )
- Fixed collected asteroid chunks were not showing in item production statistics. ( more )
- Fixed a crash when navigating planets while Factoriopedia was open. ( more )
- Fixed that asteroid collectors didn't draw radius visualisation for ghosts when holding it in cursor. ( more )

### Modding

- Added InserterPrototype::uses_inserter_stack_size_bonus.
- Added Prototype::custom_tooltip_fields.
- Renamed "aquilo-4-hero" ambient-sound to "aquilo-3-hero", corresponding audio file was renamed as well.

### Scripting

- Added LuaPlayer::pipette. LuaPlayer::pipette_entity is deprecated and should not be used.
- Added ConfigurationChangedData::migrations.
- Added "item-open", "item-close", "item-pick", "item-drop" and "item-move" SoundPath types. ( more )
- Removed LuaTilePrototype::placeable_by. Use LuaTilePrototype::items_to_place_this instead.
- Added LuaEquipmentGrid::itemstack_owner read.
- Added LuaEntity::display_panel_text, display_panel_icon, display_panel_always_show and display_panel_show_in_chart read/write.
- Added LuaHelpers::send_udp and recv_udp. Added on_udp_packet_received.

## 2.0.58

Date: 23.06.2025

### Bugfixes

- Fixed LuaForce::get_logistic_group was not working with constant combinators. ( more )
- Fixed a crash when item spoils in furnace source inventory while recipe was not yet selected.
- Fixed music not playing on surfaces without a planet associated with them. ( more )
- Fixed that enabling user mods would not auto enable built in required mods. ( more )
- Fixed that inventory migrations could cause chests to send wrong item counts. ( more )
- Fixed logistic filter merging during parametrisation would incorrectly sum values. ( more )
- Fixed a crash when loading a save file when asteroid collector arms count and asteroid collector arms capacity were changed at the same time.
- Fixed cursor transfer could insert items beyond inventory weight limit. ( more )
- Fixed set constant gui would was not focusing upon opening. ( more )
- Fixed that some items that did not require recycling recipe had a recycling recipe. ( more )
- Fixed a crash when querying members of logistic group while one of them is a detached character. ( more )
- Fixed a crash when entering huge numbers into electric energy interface. ( more )

### Modding

- Added the "mod-data" prototype type.
- Added CraftingMachinePrototype::crafting_speed_quality_multiplier, module_slots_quality_bonus and energy_usage_quality_multiplier.

### Scripting

- Added LuaEntityPrototype::neighbour_connectable read.

## 2.0.57

Date: 19.06.2025

## 2.0.56

Date: 19.06.2025

### Minor Features

- Added ability to undo rotating or flipping an entity. ( more )

### Changes

- Changed how captive spawners work to always allow spoilage into the trash slots. ( more )

### Bugfixes

- Fixed that modded choose-elem-buttons didn't respect filters. ( more )
- Changed the sync mods with GUI "Sync startup settings" and "Load save after sync" so their value is always used. ( more )
- Fixed a crash when saving the game while using the spectator controller while a GUI is open. ( more )
- Fixed that remote controllers could still open GUIs of entity ghosts that had operable set to false. ( more )
- Agricultural tower planting now respects plant's tile buildability rules. ( more )
- Fix buffer chests having their contents counted twice for 'missing requests' circuit read. ( more )
- Fixed ghost overbuilding vehicle ghost would not set inventory filters. ( more )
- Fixed using selection tools would sometimes incorrectly ignore tile ghosts. ( more )
- Fixed cancelling deconstruction of a tile would not remove a tile ghost of the same tile on the same position. ( more )
- Fixed that modded crafting machines with large amounts of fluidboxes could freeze the game. ( more )
- Fixed shooter was doing ammo refill every shot causing reload time on modded ammo to not work. ( more )
- Fixed that some widgets would click-through when trying to open Factoriopedia. ( more )
- Fixed car crashing into a rock at the beginning of campaign level 5.
- Fixed that integration_patch for characters did not render for the local player. ( more )
- Fixed a crash when migrating cargo bays in some cases. ( more )
- Fixed that repair orders would not queue robots correctly. ( more )
- Fixed that changing the link ID on a linked container wouldn't alarm sleeping inserters. ( more )
- Fixed that loaders were unable to drop full belt stacks if that required merging items from multiple inventory slots. ( more )
- Fixed editor not instantly reviving tile ghosts from blueprints when overbuilt over preexisting tile ghosts. ( more )
- Fixed rectangular crafting machine sometimes rising rotate event even when it wasn't successfully rotated. ( more )
- Fixed force building entities over required foundation marked for deconstruction would result in both decon. proxy and tileghost.
- Fixed tiles being thawed or frozen would cause cancelling of deconstruction. ( more )
- Fixed controls GUI in controller input method not updating the icons for the controls when the icons dropdown is changed. ( more )
- Fixed that the amount of VRAM on the Steam Deck was not being detected correctly, leading to the erroneous activation of VRAM-saving measures. ( more )
- Fixed a crash when fast replacing furnaces when old furnace had empty item product stack and new furnace has fluid output. ( more )
- Fixed LuaItemStack::transfer_stack was incorrectly reporting success when performing unlimited transfers. ( more )
- Fixed a crash when trying to custom launch rockets to space platforms. ( more )
- Fixed a crash when copying vehicle equipment grids from blueprints. ( more )
- Fixed a desync related to circuit network and removing entities. ( more )
- Fixed that regular mining drills weren't able to output full belts when belt stack size was researched. ( more )
- Improved the expand/collapse icon for the crafting queue. ( more )
- Fixed that opening rich text Factoriopedia shortcuts while in remote view did not work. ( more )
- Fixed that Vulcanus chimneys were grouped with Nauvis big rocks in the deconstruction planner. ( more )
- Fixed that base quality did not show in crafting machines. ( more )
- Fixed that players landing on the same planet at the same time would squash each other. ( more )
- Fixed a malformed icon. ( more )
- Fixed that buffered fluidboxes would not flow fluid through their directional connections. ( more )
- Fixed that fluidboxes in the vicinity of a removed fluidbox could disconnect from otherwise valid neighbors in some situations. ( more )
- Fixed that roboport antenna was rotating while in preview. ( more )
- Fixed promethium science pack was missing a description. ( more )

### Modding

- Added `with_filters`, `with_weight_limit` and `with_custom_stack_size` options to ContainerPrototype::inventory_type and LinkedContainerPrototype::inventory_type.
- Added LoaderPrototype::wait_for_full_stack.
- Added QualityPrototype::default_multiplier, inserter_speed_multiplier, fluid_wagon_capacity_multiplier, inventory_size_multiplier, lab_research_speed_multiplier, crafting_machine_speed_multiplier, crafting_machine_energy_usage_multiplier, logistic_cell_charging_energy_multiplier, tool_durability_multiplier, accumulator_capacity_multiplier, flying_robot_max_energy_multiplier, range_multiplier, asteroid_collector_collection_radius_bonus, equipment_grid_width_bonus, equipment_grid_height_bonus, electric_pole_wire_reach_bonus, electric_pole_supply_area_distance_bonus, beacon_supply_area_distance_bonus, logistic_cell_charging_station_count_bonus, beacon_module_slots_bonus, crafting_machine_module_slots_bonus, mining_drill_module_slots_bonus, mining_drill_mining_radius_bonus and lab_module_slots_bonus.
- Added `quality_selector_dropdown_threshold` utility constant.
- Added CraftingMachinePrototype::quality_affects_energy_usage.
- Added MiningDrillPrototype::quality_affects_mining_radius.
- Added BeaconPrototype::quality_affects_supply_area_distance.
- Added CraftingMachinePrototype::quality_affects_module_slots, LabPrototype::quality_affects_module_slots, MiningDrillPrototype::quality_affects_module_slots and BeaconPrototype::quality_affects_module_slots.
- Added CharacterPrototype::crafting_speed.

### Scripting

- Added LuaAsteroidChunkPrototype::dying_trigger_effect read.
- Added LuaItemPrototype::send_to_orbit_mode read.
- Added LuaEntityPrototype::captured_spawner_entity read.
- Added LuaEntityPrototype::min_performance read.
- Added LuaEntityPrototype::max_performance read.
- Added target_filter to ammo type read.
- Added LuaInventory::weight and max_weight read.
- Added LuaEntity::pickup_from_left_lane and pickup_from_right_lane read/write for inserters.
- Added ghost_mode to LuaGuiElement::anchor.
- Added LuaPlayer::exit_remote_view().
- Added "blink_interval" and "render_mode" parameters to LuaRendering functions.
- Added LuaRenderObject::blink_interval and render_mode read/write.
- Added several LuaEntityPrototype reads for asteroid collector prototypes and entity with health prototypes.
- Added several LuaItemPrototype reads for starter pack prototypes.
- Added LuaForce::get_logistic_groups(), get_logistic_group(), create_logistic_group(), and delete_logistic_group().
- Added on_research_queued.
- Added player to on_research_moved and on on_research_cancelled.
- Added fusion reactor properties to LuaEntityPrototype.
- Added LuaSurface get_default_cover_tile() and set_default_cover_tile().
- Added CustomInputEvent::element to get the LuaGuiElement under the cursor when the custom input was activated.
- Changed LuaInventory::set_bar to allow passing nil as well.
- Added LuaPrototypes::utility_constants read.
- Added LuaEntityPrototype::get_fluid_capacity().
- Added force to LuaEntityDiedEventFilter.
- Added LuaSpacePlatform::hidden read/write.
- LuaGuiElement::locked can be set during add().
- Added LuaEntity::inventory_supports_bar(), get_inventory_bar(), set_inventory_bar(), inventory_supports_filters(), is_inventory_filtered(), can_set_inventory_filter(), get_inventory_filter(), and set_inventory_filter().

## 2.0.55

Date: 02.06.2025

### Bugfixes

- Fixed a crash when game was saved in complete mode (for desync, benchmark or heavy mode) that could happen after a save file was loaded from an older version requiring transport line groups to be reconstructed while there were also blueprints with transport belts present in the save.
- Fixed vehicle ammo refill was not working. ( more )
- Fixed splitter gui was not updated in some cases. ( more )
- Fixed heat pipe connections did not flip. ( more )
- Fixed blueprint tile building sometimes not allowing partial builds ( more )
- Fixed some issues around setting driving for a vehicle on different surface via scripts ( more )

### Modding

- Added `helpers` to settings and prototype stages.

### Scripting

- Added LuaHelpers::game_version read.
- Added LuaHelpers::compare_versions().

## 2.0.54

Date: 30.05.2025

### Bugfixes

- Fixed script could rotate inserters into diagonal directions. ( more )
- Fixed turret cooldown not accounting for StartingAttack phase length, making effective turret cooldowns longer. Fixes Railgun turret showing incorrect shooting speed. ( more )Fixes Railgun upgrades not being correct. ( more )Adjusted railgun cooldown to maintain previous shooting speed. Effective technology bonus increased slightly.
- Fixed asteroid collector not drawing arms and radius when offscreen. ( more )
- Fixed a crash due to item request proxy inconsistency.

## 2.0.53

Date: 30.05.2025

### Bugfixes

- Improved collection of asteroid chunks on space platforms with fluctuating speed. ( more )
- Fixed that you couldn't immediately clear the cursor if the inventory "hand" was on a filtered slot and you held a different item. Hand will now move to a new slot when swapping it. ( more )
- Fixed that ghost-building upgrading of an entity with module requests would clear the module requests. ( more )
- Fixed that did on_player_driving_changed_state not run when cargo pods landed. ( more )
- Fixed that recipe with quality tooltip didn't work for modded GUIs. ( more )
- Fixed math2d.vector.to_orientation() not enforcing range [0, 1) for the return value. ( more )
- Fixed spoilable category not showing in Factoriopedia when the item spoiled into nothing. ( more )
- Fixed a crash when reading LuaStyle::horizontal_spacing and vertical_spacing of a table which didn't have these values set. ( more )
- Fixed LuaEntityPrototype::get_inventory_size() returning nil for rocket_silo_rocket and rocket_silo_trash inventories. ( more )
- Fixed that AnimationSheet::repeat_count wasn't handled correctly and could crash the game. ( more )
- Fixed that internal console textfield scrollbar moved to the beginning and back after every key press if the message was too long.
- Fixed LuaGameScript::take_technology_screenshot was not processing selected_technology. ( more )
- Fixed that item insertion requests didn't work well with spidertron's sorted inventory. ( more )
- Fixed storage tank was not showing fluid content through window when frozen. ( more )
- Fixed wait condition "any planet import zero" was ignoring negative filters when deciding which items would be requested. ( more )
- Fixed any filter was showing in copy-paste filters tip. ( more )
- Fixed a crash when replacing a buffered fluidbox with an unbuffered fluidbox. ( more )
- Fixed missing localisation for nuclear explosion effects. ( more )

### Modding

- Added utility constants logistic_slots_per_row, crafting_queue_slots_per_row, blueprint_big_slots_per_row, blueprint_small_slots_per_row, and trash_inventory_width.
- Added LandMinePrototype::trigger_interval.
- Added SolarPanelEquipmentPrototype::performance_at_day, performance_at_night and solar_coefficient_property.

### Scripting

- Changed LuaEntity::set_passenger() to work with cargo pods.
- Changed LuaLogisticSection::set_slot() to return the existing conflicting slot (if one exists) instead of erroring.

## 2.0.52

Date: 23.05.2025

### Minor Features

- Added --run-replay command line option.

### Bugfixes

- Fixed that character armor animations did not play correctly. ( more )
- Fixed that beacons would not respect the allowed module categories of the affected machine. ( more )
- Fixed a crash when using --dump-prototype-locale with some mods. ( more )
- Fixed that eggs could spoil while traveling over open space and result in stuck biters. ( more )
- Fixed that red wire shadows on selector combinators did not render correctly in the east orientation. ( more )
- Fixed that asteroids would block placing blueprints. ( more )
- Fixed that the galaxy of fame button would not show when in multiplayer. ( more )
- Fixed ghost rotated overbuild over real entity would not generate events. ( more )
- Fixed super-forcing gates and walls would sometimes cause deconstruction of adjacent curved rails ( https://forums.factorio.com/122374 and https://forums.factorio.com/116779 )
- Fixed other forces' ghosts with tile buildability rules colliding with a tile ghost on platform being removed on tile ghost build. not revive.
- Fixed blueprints not building cover tiles when foundation tile build failed on the same position ( more )
- Fixed that rocket silos disabled by script would still try to fulfil space platform requests. ( more )
- Fixed a broken menu simulation. ( more )
- Fixed that destroying a character entity while it was in a space platform would crash the game. ( more )
- Fixed a crash when trying to render corpses without graphics defined. ( more )
- Fixed an issue with choose-elem-button highlighting when disabling/enabling widgets. ( more )
- Fixed a rendering issue with tables when removing all child widgets at once. ( more )
- Fixed that changing recipes in ghost assemblers would always clear requested modules. ( more )
- Fixed researched and disabled technologies being shown in the technology tree and considered as "not researched" for prerequisites checks. ( more )
- Fixed that railguns didn't show the maximum energy consumption correctly. ( more )
- Fixed that valves would play a working sound when no fluid is flowing.
- Fixed that LuaEntity::launch_rocket() did not work with some parameter combinations. ( more )
- Fixed consistency issue with locomotive's fuel inventory if it has non fuel items in it.
- Fixed several issues of factoriopedia entries being in the wrong order. ( more )
- Fixed that the blueprint GUI could think there were pending changes when there weren't. ( more )

### Modding

- Added ItemPrototype::moved_to_hub_when_building.

### Scripting

- Added LuaSchedule::get_inside_interrupt()/set_inside_interrupt().
- Added `quality` to on_script_trigger_effect event when item spoils to script trigger.

## 2.0.51

Date: 19.05.2025

### Minor Features

- Spidertron remote tooltips show a camera view of the selected spiders.

### Bugfixes

- Fixed spidertron remote not showing the color of the selected spiders. ( more )
- Fixed a crash when player uses editor and views surface through remote view and presses shift+right click. ( more )
- Fixed that inactive crafting machines were not clearing animation state when freezing.

### Scripting

- Added LuaSurface::spill_inventory.

## 2.0.50

Date: 16.05.2025

### Bugfixes

- Fixed super forced building across underground belts not working for some directions. ( more )
- Fixed that landing at modded planets could cause the game to get stuck waiting for a landing position. ( more )
- Fixed that instant upgrading modules was not instant. ( more )
- Fixed that inserters could get stuck when captured spawners would revert and be re-captured. ( more )
- Fixed that when parametrising something without quality (fluid for example), confirming with shortcut didn't allow to keep the parameter. ( more )
- Fixed that demolishers would fall asleep while mostly outside of their territory and would not respond to taking damage. ( more )
- Fixed a rare, failing demolisher-related consistency check. ( more )
- Fixed that deleting all achievements in a modded game also deleted Steam achievements. ( more )
- Fixed a crash when a vehicle with roboport equipment was marked for deconstruction. ( more )
- Fixed entity ghost colliding colliding with other force's entity marked for deconstruction sometimes causing a crash ( more )
- Fixed a crash when attempting to run RCON commands in single player before the first tick has run. ( more )
- Fixed that fast-replacing furnaces did not put result items into the correct slots. ( more )
- Fixed that you could un-toggle all of the time buttons in the production statistics GUI. ( more )
- Fixed that finishing a map drag and closing remote view on the same frame would cause remote view to become "stuck" at an offset. ( more )
- Fixed that toggling rocket silo space platform requests did not set the last user. ( more )
- Fixed that some space-age recipes using spoiling could be paused indefinitely. ( more )
- Fixed that text field rendering did not work correctly when when changing the text value in some cases. ( more )
- Fixed that belt dragging over belt undergound gap changed direction in the process, effectively making one part of the drag in the opposite direction.
- Fixed a crash in map generation when offset_x/y was infinite by adding stronger noise expression argument validation.
- Fixed that disabling a text field widget didn't disable the rich text icon selector. ( more )

### Balancing

- Fuel acceleration bonus and equipment speed bonuses now apply quarter of compound bonus rate to turning rate of tank-driving cars (e.g. tank)

### Scripting

- Added LuaEntity::set_inventory_size_override/get_inventory_size_override methods with support for container and cargo-wagon.
- Added LuaEntity::crane_end_position_3d read for getting current ending position of agricultural crane. ( more )

## 2.0.49

Date: 12.05.2025

### Bugfixes

- Fixed a crash when calling LuaEntity::launch_rocket() with no character.
- Fixed a crash related to logistic filters that should not have import from configured but kept having one due to missing migration. ( more )
- Fixed it was possible to set "solar" usage priority for electric energy source of entities that are not a solar panel.
- Fixed multioctave noise allowing negative and infinite octaves which caused the game to freeze in map generation on ARM systems. ( more )
- Fixed "Any request zero" wait condition triggering when building last item on a space platform. ( more )

### Modding

- Added AgriculturalTowerPrototype::randomize_planting_tile.
- Added RecipePrototype::additional_categories.

### Scripting

- Added LuaEntity::owned_plants read.
- Added LuaEntityPrototype::launch_to_space_platforms read.

## 2.0.48

Date: 12.05.2025

### Minor Features

- Show existing turrets' radius when holding a turret to be built. ( more )
- Smart underground belt building now considers splitter to be an obstacle if there was something connected to the lane already.

### Bugfixes

- Fixed a crash when trying to render screenshots of entities marked for upgrade in multiplayer latency. ( more )
- Fixed that negative quality effects did not show correctly in tootips. ( more )
- Fixed a crash opening the train GUI in spectator controller. ( more )
- Fixed that changing recipes in ghost assembling machines didn't remove invalid item requests. ( more )
- Fixed that construction robots dispatch for item requests was too slow in networks with many unfulfillable requests. ( more )
- Fixed the browse arrows in the remote view changing position when opening the train GUI. ( more )
- Fixed listbox items with remarks would have their text cut off unnecessarily. ( more )
- Fixed renaming the last train stop on a surface would rename all global uses of the name in interrupts. ( more )
- Fixed extra padding above the ghost cursor selection GUI. ( more )
- Killed landmines now explode. ( more )
- Fixed that manually launched rockets could be sent to platforms mid-flight in some cases. ( more )
- Fixed that ghost upgrading entities in remote view would play a failure sound if the entity supported rotation but was not currently rotatable. ( more )
- Fixed that multiplayer networking would fail if there were too many mods in the mods directory on Linux. ( more )
- Fixed that renaming all stops would change the color of all stops with that name. ( more )
- Fixed that a long 'Enable train limit' translation would make the train stop GUI expand. ( more )
- Fixed textbox overlap in logistic network GUI. ( more )
- Fixed a recursive table in data would cause a crash. ( more )
- Fixed a crash when script requested printing a localised string that has recursion loop. ( more )
- Fixed inserter rotation and extension speed would ignore quality level of normal quality. ( more )
- Fixed belt gap traversing bug related to overbuilding ghost undergrounds with real ones. ( more )
- Fixed missing train stop limit and priority blueprint parametrisation context captions translations. ( more )
- Fixed a crash when clicking on "Show only essential technologies" in technology GUI while a hidden technology is selected. ( more )
- Fixed high memory usage of asteroid collectors because they didn't remove invalid asteroid chunks from tracking when they were disabled. ( more )
- Fixed getting an extra warning message of missing underground even when its not needed. ( more )
- Fixed possible memory management error when initializing GPU device counters with Metal. ( more )
- Fixed texture initialization on low-memory Macs with the Metal graphics backend. ( more )
- Fixed that the default graphics settings for some Macs with Apple GPUs were too high. ( https://forums.factorio.com/128458 , https://forums.factorio.com/128653 )
- Fixed that transport belt ghost upgrading could generate unexpected undergrounds. ( more )
- Fixed that the blueprint parametrisation formula UI error handling didn't properly fill the variables resulting in false positive errors. ( more )
- Fixed that some map generator GUI headers didn't show. ( more )
- Fixed that it was not possible for scripts to set the player's zoom level at or below 1/32. ( more )
- Fixed that the Constant Combinator GUI had inconsistent default values. ( more )
- Fixed upgrade planner upgrading incorrect module slots when the entity was marked for downgrade. ( more )
- Added missing notification of "too far to connect" for smart belt dragging when the obstacle is exceeding the limit of the related undergrounds.
- Fixed that items in provider chests did not count as available when reading logistic network requests. ( more )
- Fixed a crash when setting active=false on logistic/construction robots. ( more )
- Changed pipette of fluid recipes to work the same as pipette of item recipes. ( more )
- Fixed solar panels on a script created surfaces were not affected by surface properties.
- Fixed an issue when changing constant combinator values in multiplayer. ( more )
- Fixed that locomotive fuel request couldn't be canceled outside of remote view. ( more )
- Fixed that building while in the trains GUI when entered from remote view would build physical items. ( more )
- Fixed that the fulgoran lightning attractor didn't show what items it would produce when mined. ( more )
- Fixed a crash when trying to parameterize infinity pipe filters. ( more )
- Fixed inserters could get stuck trying to insert into lab with some modded technologies active. ( more )
- Fixed smart belt building over a curve in reversed direction. ( more )
- Fixed various problems of smart belt building with no undergrounds in inventory over perpendicular belts. ( more )
- Fixed that offshore pump ghosts kept their fluid filters in cases where they weren't meant to. ( more )
- Fixed ghosts were not showing wire connection areas properly for combinators and power switches when connecting wires.
- Fixed LuaRadarControlBehavior was missing LuaControlBehavior fields.
- Fixed a crash when interacting with temporary stops in moving trains. ( more )
- Fixed a crash when defining a local noise expression as empty string and using it. ( more )
- Fixed a crash when migrating rolling stocks. ( more )
- Fixed wire shadow rendering ignoring surface shadow opacity. ( more )
- Fixed an issue with scrollable tooltips and label sizes. ( more )
- Fixed modded furnaces would not work with item and fluid recipes based on ingredients order.
- Fixed LuaForce::platforms read not being mapped by platform index as documented.
- Fixed a crash when ghost of train stop with custom color is upgraded.
- Fixed agricultural tower having insufficient electric buffer size when crane_energy_usage was larger than energy_usage.
- Fixed that a black line could appear between chunks at some zoom levels. ( more )

### Modding

- Added the "valve" entity type.
- Added SolarPanelPrototype::performance_at_day, performance_at_night and solar_coefficient_property.
- Added LightningProperties::lightning_multiplier_at_day, lightning_multiplier_at_night, multiplier_surface_property and lightning_warning_icon.
- Added AgriculturalTowerPrototype::accepted_seeds.

### Scripting

- Added LuaSpacePlatform::ejected_items read.
- Added LuaSpacePlatform::eject_item().
- Added LuaSpacePlatform::clear_ejected_items().
- Added LuaEntity::valve_threshold_override read/write.
- Added LuaEntityPrototype::valve_mode read, LuaEntityPrototype::valve_threshold read, and LuaEntityPrototype::get_valve_flow_rate(quality).
- Added drop_full_stack parameter to LuaSurface::spill_item_stack.
- Added character parameter to LuaEntity::launch_rocket.
- Added LuaSurface::set_pollution.
- Added defines.inventory.agricultural_tower_input and defines.inventory.agricultural_tower_output.
- Added defines.inventory.linked_container_main, asteroid_collector_output, crafter_input, crafter_output, crafter_modules, crafter_trash, lab_trash.
- Added LuaControl::get_inventory_name.
- Added LuaInventory::name read.
- Added LuaGuiElement::quality read/write for "sprite-button" type.
- Added LuaEntity::cargo_bay_connection_owner read.
- Added LuaEntity::use_transitional_requests read/write.
- Added LuaEntityPrototype::fluid_source_offset.
- Added LuaEntity::get_fluid_source_tile() and get_fluid_source_fluid().
- Added LuaSurface::pollution_statistics read.
- Added LuaSurface::global_electric_network_statistics read.
- Added LuaSurface::daytime_parameters read/write.
- Added LuaEntityPrototype::agricultural_tower_radius, crane_energy_usage and growth_area_radius read.
- Changed on_space_platform_changed_state event to run after all starter pack actions are done when applying it and LuaSpacePlatform::hub is set.

## 2.0.47

Date: 29.04.2025

### Bugfixes

- Fixed alert icons could persist after changing surfaces. ( more )
- Fixed upgrade planner slot tooltips not showing with the correct quality. ( more )
- Fixed that manually filed rocket silos wouldn't launch correctly when multiple platforms requested the same item. ( more )
- Fixed logistic group multiplier was not visible with long group names. ( more )
- Fixed asteroids not getting destroyed when they collided with the platform and had zero relative velocity while the platform was moving.

## 2.0.46

Date: 29.04.2025

### Minor Features

- Added Space Age expansion filter to the mod portal explore pane.
- Added "planets" and "character" tags to the mod portal explore pane.
- Mod portal search results and mod info will show whether they require the Space Age expansion.
- Added heading car driving option for keyboard input method. Pressing in a direction will make vehicles automatically turn and accelerate to that side of the screen.
- Cars and tanks will automatically snap to one of the 8 major directions if within a few degrees.

### Balancing

- Changed piercing ammo recipe to be cheaper.

### Changes

- Renamed controller vehicle driving modes from "relative" to "heading" and from "absolute" to "steering".
- Creating a rich text tag will move the text cursor to the end of the tag, not the beginning.
- New achievement limitations won't affect saves started before the version 2.0.45.
- Added a confirm dialog informing about which achievements will be disabled with the current map settings when starting a new game.
- Some achievements are also disabled when Gleba enemies are set to be lower.

### Graphics

- Improved visibility and looks of Fulgora cliffs.
- Added graphics for frozen stone path.
- Changed the north edge of all pipe graphics to include an arch to prevent tiling issues in specific cases.

### Bugfixes

- Fixed that space platform schedule wasn't properly affected by during blueprint parametrisation. ( more )
- Fixed that space platform name wasn't parametrisable by blueprint.
- Fixed a sound instance leak when closing machine GUIs with playing sound accents. ( more )
- Fixed burner spidertron would keep moving indefinitely after running out of fuel. ( more )
- Fixed that modifying the group schedule of trains would cause other trains in the group to switch to automatic mode. ( more )
- Fixed that rearranging infinity filters could cause buttons to edit the wrong filters. ( more )
- Fixed accumulator charge/discharge emission sprite being misaligned. ( more )
- Fixed a crash when clicking on a new tip popup while being dead. ( more )
- Fixed blood particle tint being ignored in Lua. ( more )
- Fixed Controller settings section in the Controls settings window not behaving correctly during search.
- Fixed deconstruction planner with tile filter would not mark for deconstruction hidden tiles matching filter if there is a non-matching tile marked for deconstruction covering them. ( more )
- When (super)force-building tiles, only foundation tiles will be autofilled and only for building cover tiles. ( more )
- Fixed that a decal covered by a tile would still play its walking sound. ( more )
- Fixed Undo after overbuilding existing entities with blueprint parametrised blueprint. ( more )
- Fixed a crash when preparing undo/redo camera for tiles which are on a deleted chunk. ( more )
- Fixed that quality tooltips showed the wrong value in crafting machines in modded cases. ( more )
- Fixed clicking a station label in the train GUI would not open map at the expected train stop. ( more )
- Fixed black lines on some entities when "alt-mode" is enabled when using Metal graphics backend.
- Fixed crash that could randomly occur when using Metal graphics backend.
- Fixed crash that could occur when using the Metal graphics backend with texture streaming enabled.
- Fixed missing achievement mentions for the new restrictions in map gen settings.
- Fixed that lower pollution absorption disabled some achievements (instead of the higher one).
- Fixed that Bioflux and Yumako would heal vehicles. ( more )
- Fixed a crash when fast-replacing a train stop ghost with mods listening to 'on_entity_color_changed' event. ( more )
- Fixed that creating a rich text tag by deleting a character would not move the text cursor from the middle of the tag. ( more )
- Fixed that drag building an underneathie would show a flying text whenever the cursor went over an obstacle.
- Fixed a crash when reordering empty filters in asteroid collector. ( more )
- Fixed a consistency crash when disconnecting rolling stock and modifying the train in the same tick through Lua. ( more )
- Fixed that undo when in the Map Editor and having instant-blueprint-building enabled didn't always work with elevated rails. ( more )
- Fixed that the missing-equipment message when copying spidertron equipment overlapped. ( more )
- Fixed that signal pipette did not work for fluids, and some other GUI elements. ( more )
- Fixed that the space platform hub full alert didn't persist in some situations. ( more )
- Fixed that reading orbital requests would generate negative signals in some cases. ( more )
- Fixed that modifying logistic requests in groups on planets would reset import-from. ( more )
- Fixed that linked belt fast-replace didn't change the direction. ( more )
- Fixed that changing the requested item in space platform hubs would only visually update the max amount. ( more )
- Fixed that the map view train shortcut info was shown when zoomed in even though it didn't apply when zoomed in. ( more )
- Fixed that changing quality in some select-GUIs would reset the count. ( more )
- Fixed that the recipe productivity locale was in space age instead of core. ( more )
- Fixed that deleting items through the map editor didn't clear request proxies. ( more )
- Fixed that instant tooltips could block the game-over screen. ( more )
- Fixed wrong position of inventory limit button for some inventory sizes. ( more )
- Fixed recipe tooltips not showing intermediate ingredients as craftable (orange) when those intermediate recipes create extra products. ( more )
- Fixed that recipes using result_is_always_fresh would start spoiling at the tick crafting started instead of the tick crafting finished. ( more )
- Fixed that pipette while in the train fuel tab would put a ghost item in the cursor. ( more )
- Fixed particles being updated twice when they moved to a new chunk. ( more )
- Fixed rich text chat tooltips not disappearing when opening the menu. ( more )
- Fixed rich text chat tooltips showing when hovering below the chat with chat messages with multiple lines.
- Fixed that trying to move the upper limit on double-slider GUI elements could sometimes change the lower limit even when nothing actually changed. ( more )
- Fixed that remote view could not interact with blueprint books in the character inventory. ( more )
- Fixed that you could order upgrade some entities through remote view that could never be upgraded. ( more )
- Fixed that the build preview and rolling stock final position did not match in some cases. ( more )
- Fixed that changing the minimum value of a logistic request through moving the maximum slider did not work correctly. ( more )
- Fixed that building trains would remove train ghosts on other rail elevations. ( more )
- Fixed that arriving platforms sent the wrong old state to on_space_platform_changed_state event. ( more )
- Fixed that indestructible entities on the space platform could consume asteroid damage before other entities on the same tile.
- Fixed asteroids sometimes getting destroyed when platform speed was negative.
- Fixed a crash when rendering a modded pipe that has multiple connections facing the same direction. ( more )
- Fixed a crash when robot orders are invalidated while finishing another order. ( more )
- Fixed a crash when some tile sprites end up with zero size due to scaling. ( more )
- Fixed a crash when a space platform in orbit is teleported to a distant connection by a script.
- Fixed a custom GUI layout issue. ( more )
- Fixed "<user> has paused the game" box sometimes appearing outside the screen when pausing the game.
- Fixed "<user> has paused the game" box moving outside the screen when opening the menu. ( more )
- Fixed shotgun damage tooltip not showing parenthesis. ( more )
- Fixed pinned achievement cards stretching when multiplayer infoboxes are present. ( more )
- Fixed achievement GUI progress not being updated after an achievement was completed. ( more )
- Fixed not being able to mute sound category by clicking its label. ( more )
- Fixed that robot upgrade jobs weren't evenly distributed. ( more )
- Fixed that deconstruction jobs didn't properly distribute tasks to closer robots. ( more )
- Fixed that locale pluralization did not work with SI-prefixed numbers.

### Modding

- Added CarPrototype::rotation_snap_angle
- Instead of "enemy-bases" autoplace control being hardcoded to be the one to affect achievements, achievements are now affected by any autoplace controls with the new property related_to_fight_achievements.
- Fluid boxes with diagonal connections now throw a prototype error.

### Scripting

- Added LuaEntity::item_request_proxy read as the recommended way to check for the presence of one.
- Added optional amount to LuaItemStack::transfer_stack().
- Added base_damage_modifiers and bonus_damage_modifiers when creating projectile types through LuaSurface::create_entity().
- Added LuaEntity::base_damage_modifiers and bonus_damage_modifiers read/write.
- Made LuaPlayer::zoom readable
- Added LuaPlayer::zoom_limits
- Added LuaTransportLine::total_segment_length.

## 2.0.45

Date: 14.04.2025

### Minor Features

- Equipment grid GUIs have improved click-and-drag support. In addition to installing equipment, you can now click and drag to pick up, transfer, and fast-replace equipment.

### Changes

- Improve relative vehicle driving with gamepad in multiplayer, especially when shooting.
- Included priority and train limit of train stop into blueprint parametrisation.
- Changed pipette to always select normal quality items when pipetting a tile. ( more )
- Changed the blueprint parametrisation logic related to quality. Before, whenever anything other than normal quality was used with parameters, the quality was always taken from the blueprint, and only the core id was parametrised. Now, this only happens when more than 1 quality with the same id is present instead.
- All parameters can potentially generate the stack size, crafting time, rocket capacity and ingredient count as long as they are mapped to id which is a recipe.
- When the blueprint is being parametrised and "Show all items in selection list" interface option is selected, all (even locked) recipes are presented. ( more )
- Changed rocket part recipe position in the signal selection to be next to the rocket silo instead of intermediates.
- Reduced volume and pitch of recycler loop and railgun turret shot sounds. ( more )

### Graphics

- Added Metal graphics backend for Apple devices.
- Added new particle effects for mining or destroying Gleba plants and fungi.

### Bugfixes

- Fixed that Factoriopedia would not fully respect the relative ordering between different object types. ( more )
- Fixed Spoilage from section is included in merged recipe/item entries of factoriopedia. ( more )
- Fixed that the achievements checks of map startup difficulty settings didn't check for pollution, expansion settings, starting area and trees.
- Fixed that module upgrades could not be cancelled with an upgrade planner. ( more )
- Fixed that installing modules with an upgrade planner or manually via fast-transfer wouldn't work if modules or module requests already existed in the entity. ( more )
- Fixed that module upgrades, installations, and removals via upgrade planner didn't work if the entity already had existing delivery or removal requests in another inventory.
- Fixed that upgrading or manually fast-replacing any entity would clear any pending item delivery or removal requests. ( more )
- Fixed that module upgrades used the original entity's "allowed effects" restrictions instead of the upgrade target's. ( more )
- Fixed that module upgrade requests could get cut short depending on the module inventory size of the original entity. ( more )
- Fixed copying from space platforms did not count and preview platform tiles. ( more )
- Fixed that pipette on resource entities would put the burner drill circuit signal in the cursor. ( more )
- Fixed that LuaSchedule::add_record() ignored created_by_interrupt. ( more )
- Fixed a crash when hovering blueprints pasted into chat. ( more )
- Fixed a crash when on_player_setup_blueprint errors. ( more )
- Fixed that the mod manager update table styling would break when mods were updating. ( more )
- Fixed inconsistent display of rich text icons in tooltips. ( more )
- Fixed rail variants can now be accessed with alt click in factoriopedia. ( more )
- Fixed that pressing alt while selecting blueprint contents confirmed the selection. ( more )
- Fixed that recipe item order changes would cause items to be removed in some cases. ( more )
- Fixed that building walls would remove unrelated ghosts in some cases. ( more )
- Fixed that CustomGuiSlider did not respect the discrete slider value when changing the minimum and maximum values. ( more )
- Fixed that the burner generator prototype type did not report its max consumption correctly. ( more )
- Fixed labs with drain multiplier taking too long to drain final fraction of science packs. ( more )
- Fixed that the invalidation of the achievement "Keeping your hands clean" wasn't properly saved on a headless server. ( more )
- Fixed issue with merging fluid/recipe where there are more result products. ( more )
- Fixed fluid box compound was not respecting max pipeline extent value of the original fluid boxes. ( more )
- Fixed that selecting rocket part during blueprint parametrisation created incompatibile station name. ( more )
- Fixed that it was possible to start another blueprint build while parametrisation was in progress. ( more )
- Fixed generator equipment item tooltip ignoring fuel consumption efficiency. ( more )
- Fixed constant combinators were clamping total values from logistic sections when they should wrap around. ( more )

### Modding

- Added MiningDrillPrototype::uses_force_mining_productivity_bonus.
- Added PumpPrototype::flow_scaling.

## 2.0.44

Date: 07.04.2025

### Minor Features

- Items manually inserted or removed from space platform dump inventory will always reset drop cooldown to two seconds. This should make manual interactions more responsive and intuitive. ( more )
- Added filter support to burner fuel inventories.
- Tall tooltips when attached to the right side of the screen can be scrolled (by default shift + scroll).

### Changes

- Atomic bomb now blasts planet-appropriate holes into the terrain of the planet if the terrain is floating on a fluid: Ammoniacal ocean for Aquilo, Lava for Vulcanus. It also destroys space platform tiles.
- The "Tags" map overlay setting now also toggles display panel tags. ( more )
- Decider combinator condition which contains parameter evaluated to nothing (non-existent ingredient) when building blueprint is deleted instead of kept empty. ( more )
- Lowered volume of cargo wagon and beacon open/close GUI sounds. ( more )
- Cargo landing pad does not draw inventory contents in alt mode.

### Gui

- Added equipment grid button to locomotive GUI and removed the popup window. ( more )

### Graphics

- Added some new Gleba decorative variants for Nerve roots.
- Improved water/land visibility on Gleba by masking decals over water, changing terrain and water colors, and adding a water edge foam effect.
- Added new recipe icons for molten metals from ore and reworked existing icons related to molten metals and lava. ( more )

### Bugfixes

- Fixed that modded miniature spidertrons could get stuck when something is built underneath their legs. ( more )
- Fixed locomotive GUI formatting for trains with many fuel slots. ( more )
- Fixed edit interrupt GUI closing the wait conditions and choose station windows spuriously. ( more )
- Fixed schedule GUI station buttons not updating correctly. ( more )
- Fixed a crash when removing modded cargo pods through mod removal. ( more )
- Fixed blueprint library small slots view had extra empty space. ( more )
- Fixed renaming all logistic points in a logistic group would delete the old group if the new group already existed. ( more )
- Fixed pretty print for LuaPlayer was showing wrong index. ( more )
- Fixed expected resources were rounded down in some cases. ( more )
- Fixed that the last-shown mod thumbnail would remain when the mod info pane was cleared. ( more )
- Fixed a crash when migrating some mods with assembling machines that have control behaviors. ( more )
- Fixed that pushing fluid away into a double-buffered fluidbox would push fluid into the internal buffer instead of the segment. ( more )
- Fixed display panel chart tags having different sprite layering than regular map tags. ( more )
- Fixed that the map editor extra-settings GUI did not work correctly for ghosts. ( more )
- Fixed that building underground belts and underground pipes would not show an error flying text. ( more )
- Fixed inserters would detach from valid pickup targets if they have no inventory. ( more )
- Fixed count of trains in group was not updating when adding other trains to group by copy settings. ( more )
- Fixed programmable speaker alerts would not update to show on map when alert was active. ( more )
- Fixed building preview of blueprint with locomotives could show them in wrong orientation when blueprint is rotated in some cases. ( more )
- Fixed that overbuilding train with parametrised blueprint didn't apply the parametrisation on the schedule of the existing train. ( more )
- Fixed in some cases a locomotive could be fueled even if the train was already on the way but not yet moving. ( more )
- Fixed that selecting parameter when only the base value is possible to change (the blueprint contains the item in other than normal quality), the select list actually offered quality selection and discarded it, instead of not even offering the quality selection. ( more )
- Fixed that blueprint parametrisation of combination of recipe + item didn't apply the recipe limitation based on crafting machine it appears in. ( more )
- Fixed that blueprint parameter item which was named but not configured to be parametrised became parametrised after export/import through blueprint string. ( more )
- Fixed that self-recycling recipes were generated for parameters.
- Fixed that pipetting parameter in cheat mode generated parameter item.
- Allowed setting blueprint parametetrisation ingredient of by pepetted parameter. ( more )
- Fixed that confirming icon selection in the save game dialog name editing confirmed the save dialog instead of the icon selection. ( more )
- Added info about not being able to set recipe based on surface condition when parametrising blueprint. ( more )
- Fixed assembler insertion margins were not correctly accounting for max inserter hand in some cases. ( more )
- Fixed that when number parameter had formula but disabled, it still counted that value as not needed to be filled when deciding what parametrisation window to show. ( more )
- Fixed wall corpses used wrong orientation when part of a thick wall. ( more )
- Fixed mods adding many planets would cause the map generator GUI to not layout nicely. ( more )
- Fixed that searching in inventories did not search quality names. ( more )
- Fixed a crash when setting resource_patch_search_radius to 0. ( more )
- Fixed GUI layout issues with relative GUIs when nesting widgets. ( more )
- Fixed the loading of inputs from config file when using a combination of controller triggers and the ALT keyboard modifier. ( more )
- Fixed latency hiding when dragging remote remote view with the cursor while the server is running more slowly than clients. ( more )
- Fixed Beacon transmission strength graph duplicate number on some scales. ( more )
- Fixed a crash when corpse animations aren't defined correctly. ( more )
- Fixed that the confirm hotkey did not confirm-resume when in the map editor. ( more )
- Fixed that combining negative logistic filters with positive ones did not work correctly. ( more )
- Fixed that LuaDefines::logistic_member_index was missing some values. ( more )
- Fixed that recipe hover highlights didn't work correctly when driving vehicles. ( more )
- Fixed that logistic section multipliers rounded differently in some places. ( more )
- Fixed that frozen rocket silos could block non-frozen silos from launching. ( more )
- Fixed that highlighting robots in the logistic networks GUI excluded requested robots. ( more )
- Fixed that remote view could not order removal of items from the assembling machine dump inventory. ( more )
- Fixed that smart belt dragging would not revive ghost underground belts at the end of a gap. ( more )

### Modding

- Added collision-layer out_of_map for out-of-map tiles.
- Decals now support draw_as_light and draw_as_glow.
- Decals can now be masked by water if their layer is above UtilityConstants::capture_water_mask_at_layer, the tile effect has a lightmap_alpha of less than 1, and the decal has opacity_over_water less than 1. This is currently requires Space Age as the effect is not supported on Switch.
- Added FusionReactorPrototype::target_temperature.
- Added RocketSiloPrototype::can_launch_without_landing_pads.

### Scripting

- Added support for fusion reactors to LuaEntityPrototype::target_temperature.
- Added label, preview_distance and always_visible fields to LuaPlayer::add_pin.
- The remote view controller now supports enabling and disabling flashlight.
- Added LuaControl::open_factoriopedia_gui(...).
- Added LuaControl::close_factoriopedia_gui().

## 2.0.43

Date: 26.03.2025

### Minor Features

- Added support for volume and speed activity matching for persistent working sounds.
- The swap-players command can now handle basic remote view and players in space platform hubs.

### Graphics

- Changed items to stop drawing health and spoilage bars when the player is zoomed too far out. ( more )

### Balancing

- Trees no longer take damage from spores nor absorb spores as a result of taking pollution damage.
- Gleba wetlands, lowlands, and water tiles now absorb 3 times as many spores as other tiles.

### Bugfixes

- Fixed a desync related to demolishers. ( more )
- Fixed total raw item icons clipping out of the recipe tooltip. ( more )
- Fixed unlimited building reach when train GUI was open from character view. ( more )
- Fixed vehicles with portable roboports not being able to insert/remove equipment from themselves. ( more )
- Fixed a potential stutter when stopping a variable music track. ( more )
- Fixed variable music track intermezzo not being played correctly for subsequent tracks.
- Fixed the collision and selection boxes for many of the Gleba tree/fungi.
- Fixed a performance issue with lightning on explored planets. ( more )
- Fixed tile auto-filling logic would sometimes ignore listed entities' (e.g. Asteroid collector's) buildability rules. ( more )
- Fixed that picking rocket parts signal by pipette picked the item version of the signal, which wasn't compatible with the recipe version of the signal.
- Fixed that inserters could get stuck inserting items if the item spoiled into one of the crafting machines current recipe ingredients. ( more )
- Fixed ghost (non-superforced) rotated fast replace of some fast replaceable entities that have rotation constrains after placement. ( more )
- Fixed cutting both tile ghosts and non-(tile ghost) entities would remove the tile ghosts, despite not include them in resulting BP. ( more )
- Fixed that remote equipment removal couldn't be cancelled. ( more )
- Fixed that Ctrl+Click on empty equipment grid slot in remote view behaved unexpectedly. ( more )
- Fixed production score script error when encountering recipe products of type "research-progress". ( more )
- Fixed that trees on Gleba were taking damage from and absorbing spores. ( more )
- Fixed that some tile types on Gleba were not absorbing spores.
- Fixed that the train control hint window was showing in remote view of other surfaces. ( more )
- Fixed that undoing a fast replace would not restore wires. ( more )
- Fixed a crash with rocket flying sound after a failed audio device switch.
- Fixed that it was possible to rotate blueprint with thrusters. ( more )
- Fixed custom minimap widget would not restore zoom after save-load, would ignore zoom given during creation and would change zoom incorrectly when writing to zoom. ( more )
- Fixed that canceling cliff deconstruction could break cliff deconstruction. ( more )
- Fixed that manually placing a real entity on a ghost didn't set item requests properly. ( more )
- Fixed a crash when drawing combinator with activity_led_sprites missing. ( more )
- Fixed rocket target GUI was showing platforms unsorted. ( more )
- Fixed platforms list not updating after platform was renamed. ( more )
- Fixed crash related to boilers when configured to output fluid with lower temperature than default temperature of output fluid. ( more )
- Fixed recipe raw for some gleba recipes would use some unexpected recipes to obtain spoilage. ( more )
- Fixed decider's output constant was not covered by parametrisation. ( more )
- Fixed display panel not updating rendered text after parametrisation. ( more )
- Fixed consistency issue related to importing blueprint strings where assembler is given a recipe it cannot craft. ( more )
- Fixed a crash when script tries to set deconstruction planner's entity filter to contain only quality condition. ( more )
- Fixed a crash on saving when blueprint was made out of a train that contains a non temporary rail target. ( more )
- Fixed util.rotate_position was working incorrectly. ( more )
- Fixed changing deconstruction planner entity and tile filters by script would not replace all filters. ( more )
- Fixed unit groups getting stuck while following a path, causing the units in the group to give up on their goal. ( more )
- Changed asteroid spawning to be consistent regardless of what other game things are happening. ( more )
- Fixed locomotive stop trigger being triggered repeatedly when hitting a disabled gate. ( more )
- Fixed a crash when trying to open the logistics GUI while dead. ( more )
- Fixed that galaxy of fame wasn't available when player died after winning the game. ( more )
- Fixed that changing enemy expansion settings didn't update the enemy expansion map. ( more )
- Fixed that choose elem button filters did not handle migrations at all. ( more )
- Fixed that turrets could get stuck shooting at the wrong location when target-leading fast targets. ( more )
- Fixed that entity quality conditions when rendering blueprints would render behind the entity. ( more )
- Fixed importing upgrade planner string would not preserve fuel mappers. ( more )
- Fixed potential crash when drawing an entity in the GUI at scale 0. ( more )
- Fixed module slots configured in upgrade planner would not preserve positions when exported to a string. ( more )
- Fixed various issues related to upgrade planner and Lua API. ( more )
- Fixed programmable speaker alert quality wasn't shown in the alert slot. ( more )
- Fixed it was not possible to use more than 6 recipe ingredients in blueprint parametrisation formulas. ( more )
- Fixed it was not possible to configure infinity cargo wagon infinity filters in some cases. ( more )
- Fixed that setting fluids on a FluidBox via Lua would give fluids to ghost entities, which would cause a consistency check failure. ( more )
- Fixed space platform schedule was not updating logical operator when changed by other players. ( more )
- Fixed manually changing upgrade target of entity was not covered by undo. ( more )
- Fixed freeplay description was changing to space age freeplay even if space-age mod was not enabled. ( more )
- Fixed some icons were not collected for galaxy of fame uploads. ( more )

### Modding

- Added AirbornePollutantPrototype::damages_trees.

## 2.0.42

Date: 19.03.2025

### Minor Features

- Added additional information to Landing pad, Platform Hub and Cargo bay in factoriopedia. ( more )

### Graphics

- Added more variations to small explosion to improve the visuals when many small entities explode at the same time (happens a lot when a space platform is hit by a larger asteroid).

### Bugfixes

- Fixed equipment grid ghost interaction for entities that move in some cases. ( more )
- Fixed a crash when named logistic sections are removed when entities are removed due to mod removal. ( more )
- Fixed that finite infinite levels would show wrong in the technology GUI in some cases. ( more )
- Fixed that display panel text wasn't parametrisable by blueprint parametrisation. ( more )
- Fixed that switching to remote view while shooting would keep shooting. ( more )
- Fixed consistency issue related to downgrading blueprints that contain assemblers that when downgraded can no longer craft the recipe. ( more )
- Fixed trains station tutorial would crash when adding a schedule record. ( more )
- Fixed that space platform hubs would not auto-trash items correctly. ( more )
- Fixed a crash when asteroid collector tried to mine an unminable asteroid chunk.
- Fixed migrating logistic containers into storage chest could leave them inconsistent. ( more )
- Fixed that fusion generators were highly sensitive to entity update order. ( more )
- Fixed that rockets might not launch if there were manual filled rockets and multiple platforms wanting the same items with at least 1 being full. ( more )
- Fixed a crash related to drag building ghost belts and script reviving entities. ( more )
- Fixed a crash when upgrade-reviving ghost entities that have gui open. ( more )
- Fixed a proxy container attached to mining drill module inventory would not wake up inserters when modules are inserted or removed. ( more )
- Fixed display panel text was not showing up on screenshots. ( more )
- Fixed selector combinator gui was showing input value in the output count signal slot. ( more )
- Fixed following robots lifetime modifier was not working with fractions. ( more )
- Fixed demolishers were unable to destroy open gates. ( more )
- Fixed spoil to trigger was not spawning correct amount of entities.
- Agricultural Tower soil fertility visualisations now renders "growable with different soil" even when acceptable tile is covered by deconstructible tile ( more )
- When placing growable tile, Agricultural tower growing spot is highlighted even in a case where tile is placeable as replacement of non-growable tile (e.g. overgrowth soil on landfilled apt wetland tile)
- Fixed a crash and some other zoom-related problems if the window size is exceptionally large. ( more )
- Fixed items on splitters were changing sides when rotating. ( more )
- Fixed decider combinator gui conditions highlighting. ( more )
- Fixed blueprints being able to rotate entites that are not rotatable based on their prototypes ( more )
- Fixed that blueprint building parametrisation gui didn't accept unit postfixes and formulas. ( more )
- Fixed that blueprint parametrisation number value edit didn't accept unit postfixes and formulas.
- Fixed wire distance checks when entity uses rotated selection boxes. ( more )
- Fixed deconstruction planner with quality entities selected would not show quality on the icon. ( more )
- Fixed modded technologies with finite amount of levels could fail to show levels info. ( more )
- Fixed that blueprint parametrisation was able to change number in a storage chest filter. ( more )
- Added more context to blueprint parameters in trains. ( more )
- Fixed changing space platform hub's inventory bar was not waking up input inserters. ( more )
- Fixed pipe connection sprites of some machines not working together with storage tanks and pumps. ( more )
- Fixed tooltip for recipe parameters to not show "made in". ( more )
- Fixed lamps with color set by control behavior would not use color for one tick after loading a save. ( more )
- Fixed cutscenes would reset player zoom level when finishing. ( more )
- Fixed some tooltip lines would clip outside the tooltip frame. ( more )
- Fixed that the character would keep mining when entering remote view. ( more )

### Modding

- Changed working_visualisations to enforce that the provided array is contiguous.
- Added FluidBoxPrototype::volume_reservation_fraction.
- Added ExplosionPrototype::delay and ExplosionPrototype::delay_deviation for adding an artificial delay to an explosion effect.
- Added ExplosionPrototype::explosion_effect which triggers after the delay has passed instead of when the explosion entity is created as with EntityPrototype::created_effect.
- Added TechnologyPrototype::show_levels_info.

### Scripting

- LuaEntity::infinity_inventory_filters and remove_unfiltered_items now support infinity-cargo-wagon.
- LuaControl::walking_state now reads and writes spider-vehicle walking state if the player is driving one.
- Added LuaEntity::cargo_pod_origin which stores which station entity the pod departed from. (Migrated existing pods from before this version do NOT retroactively gain this information)
- Added 'spoil-result' and 'plant-result' filter to ItemPrototypeFilters.

## 2.0.41

Date: 12.03.2025

### Bugfixes

- Fixed extra spidertron ghost being created when ghost-building spidertron snapped to existing spidertron ghost ( more )
- Fixed deconstruction planner would not respect deconstruction alternatives when they were inside of entity ghost. ( more )
- Fixed a desync when cancelling deconstruction of frozen underground belts or frozen splitters.
- Fixed a crash when trying to create a blueprint out of space platform hub which has wait condition with empty item field.

## 2.0.40

Date: 12.03.2025

### Bugfixes

- Fixed splash screen progress bar size not scaling with the UI.
- Fixed that the can't-reach wire sprite would get drawn under some entities. ( more )
- Fixed that the chart drag hotkey did not work. ( more )
- Fixed that pre-2.0 map exchange strings were able to disable cliffs on all planets. ( more )
- Fixed a crash when a tile cannot be placed due to a missing foundation with default not given. ( more )
- Fixed rail signal selection box when selection box is off-center. ( more )
- Fixed that beacon fast-replace would allow modules the beacon did not accept. ( more )
- Fixed that water cane had the wrong icon. ( more )
- Fixed that building vehicles with pre-configured equipment grids did not always work correctly. ( more )
- Fixed another bug related to smart underground belt building.
- Fixed some recipes would recycle to wrong items when playing with quality only. ( more )
- Fixed parametrisation into requests which would lead into duplicate requests wasn't handled. ( more )
- Fixed that personal lasers would be offset incorrectly while having a tesla gun equipped. ( more )
- Fixed a crash related to modded enemy behavior. ( more )
- Fixed ghosts of non-blueprintable entities being ghost-buildable in normal mode (e.g. in remote view). ( more )
- Fixed missing blueprint parametrisation number context for ticks waiting in station schedule condition. ( more )
- Fixed GPU-accelerated compressed mipmaps on Apple Silicon Macs. ( more )
- Fixed that the infinity cargo wagon showed in Factoriopedia. ( more )
- Fixed a graphics artifact when drawing ghost rocket silos. ( more )
- Fixed nauvis_uranium_processing menu simulation not loading properly in the demo. ( more )
- Fixed that some frozen rocket silos could get stuck. ( more )
- Fixed a crash when upgrading underground belts manually through remote view. ( more )

### Modding

- Added ElectricPolePrototype::rewire_neighbours_when_destroying.
- Moved the agricultural tower growth area radius to the prototype as growth_area_radius. ( more )

## 2.0.39

Date: 05.03.2025

### Changes

- Added extra info about the evaluation order and dependencies into the blueprint parametrisation UI.

### Bugfixes

- Fixed not being able to interact with GUI elements behind transparent parts of other windows. ( more )
- Fixed display panels not drawing text correctly at larger GUI scales. ( more )
- Fixed a crash related to placing cargo landing pads on space platforms. ( more )
- Fixed a crash when rendering thrusters without fire plumes defined. ( more )
- Fixed that fast-transfer of ghost modules did not work for out of reach entities. ( more )
- Fixed that trains with the same top in their schedule would not move between stops even if the one it is waiting at is disabled. ( more )
- Fixed decider combinator GUI signals tables getting squashed too much when there are a lot of conditions/outputs. ( more )
- Fixed intro sound not respecting music-muted and master-muted settings. ( more )
- Fixed graphical issue happening when lightning attractor's collection range boundary was touching larger range attractor's collection range boundary from the inside. ( more )
- Fixed incorrect lightning protection visualisation when surface lightning search range was larger than attractor's protection range.
- Fixed overbuilding ghost with module requests with physical entity of different quality would not retain the module requests. ( more )
- Fixed normal building underground belts and pipes in remote view would deconstruct rocks, trees and cliffs. ( more )
- Fixed normal building underground belts and pipes in remote view would have missing tiles autofilled. ( more )
- Fixed crash in latency when upgrading ghost of elevated rails to different quality ( https://forums.factorio.com/120345 , https://forums.factorio.com/124222 )
- Fixed crash when car would collide with 0 health entity in latency ( more )

## 2.0.38

Date: 04.03.2025

### Changes

- Space platform "request missing materials for construction" will no longer request items for entity ghosts which can't yet be built. ( more )This should help to prevent over filling of hubs while larger platforms are being built.
- Increased minimum sprite atlas size to 4096 even when sprite resolution is set to medium. ( more )

### Bugfixes

- Fixed a lua doc error with LuaSchedule::add_wait_condition(). ( more )
- Fixed a crash when changing the station in some wait conditions. ( more )
- Fixed that the mining dril status would be incorrect when out of resources and pointing at an entity to be deconstructed. ( more )
- Fixed that inserters would not show target full for space platform hubs. ( more )
- Fixed a crash when opening the changelog while trying to connect to a multiplayer game. ( more )
- Fixed that LuaSchedule::add_record() did not support rail_direction. ( more )
- Fixed that vehicle weapon tooltips did not show bonuses. ( more )
- Fixed achievement steamrolled can be earned while driving remotely. ( more )
- Fixed lab was not creating trash inventory of proper size when LabPrototype::trash_inventory_size was given. ( more )
- Fixed that the side menu buttons did not update when a player would change forces. ( more )
- Fixed that the filter selection GUI would get closed when a ghost buffer chest was built. ( more )
- Improved issue with fast moving bots sometime appearing on screen instead of flying in from off screen. ( more )
- Fixed issue which sometimes resulted in incorrect lightning protection visualisation for marginal setups ( more )
- Fixed cutting tiles marked for deconstruction could produce superfluous deconstructible tile proxies ( more )
- Fixed Steam achievements synchronisation issues. ( more )
- Fixed that having a camera widget on screen would cause issues with the rail plan finder. ( more )
- Fixed that resources with no minable products would not show a name when hovering in the map view.
- Fixed some almost transparent pixels in the car and production group icons. ( more )
- Fixed that researching a technology would cause the input fields in constant combinators and requester chests to lose focus. ( more )

### Modding

- Added the "infinity-cargo-wagon" entity type.
- Added the "proxy-container" entity type.
- Added SpiderVehicleGraphicsSet::default_color.
- Unified entity_renderer_search_box_limits to 6 from all sides due to reduced update rate optimization of robots.
- Reduced light_renderer_search_distance_limit to 20 to compensate for entity_renderer_search_box_limits change.

### Scripting

- Added LuaSchedule::get_records(), set_records(), clear_records(), get_interrupts(), set_interrupts(), clear_interrupts().
- Changed LuaSchedule::add_record() to purely add without any extra behavior.
- Changed LuaSchedule::add_record() to accept index saying where the record is added.
- Added LuaProxyContainerControlBehavior.
- Added defines.inventory.proxy_main.
- Added LuaEntity::proxy_target_entity and proxy_target_inventory.
- Added LuaEntity::get_cargo_bays().
- Added LuaPlayer::add_pin().
- Added LuaPrototypeBase::factoriopedia_description read.
- Added factoriopedia_alternative reads to all LuaPrototypes that support it.

## 2.0.37

Date: 26.02.2025

### Bugfixes

- Fixed that inserters could get stuck when interacting with trains if the train arrived at a station without physically moving. ( more )
- Fixed that LuaSchedule::add_wait_condition, remove_wait_condition, and change_wait_condition expected a table of arguments instead of direct arguments.

## 2.0.36

Date: 26.02.2025

### Minor Features

- Added an option to mute sound categories in sound settings. ( more )
- Added an option to control the volume of Programmable speaker sounds via circuit network. ( more )
- Added an option to stop playing sounds of Programmable speaker when input signal changes instead of waiting for the sounds to finish playing. ( more )
- Added an option for Programmable speaker to use Cyclic sounds. ( more )
- Decider combinator output constant can be changed.

### Changes

- Added missing open/close GUI sounds and fixed incorrect open/close GUI sounds for various entities. ( more )
- Changed the "Train stop names" checkbox in the blueprint ui to be always on by default.

### Graphics

- Updated space platform related icon like the hub, starter pack, icon for the surface and the tech icon.
- Used the new virtual signal icon for research also for the research icon in the production graphs.

### Optimizations

- Improved belt reader performance.

### Bugfixes

- Fixed that a small empty UI box was visible on the main menu. ( more )
- Fixed a crash when generating a variable track would encounter a filesystem error.
- Fixed sound accents could play when they shouldn't on switching between machine GUIs. ( more )
- Fixed a crash when changing some modded assembling machine recipes. ( more )
- Fixed a failing SegmentedUnit-related consistency check when loading some saves. ( more )
- Fixed that the building preview and actual build position could differ at some resolutions and zooms. ( more )
- Fixed a crash when trying to drop items onto game's title bar.
- Fixed LuaWireConnector was returning wrong values of the electric network index. ( more )
- Fixed that clicking on a station in train GUI created unexpected browse history entries. ( more )
- Fixed that traversing train GUI browse history entries didn't preserve centered locomotive.
- Fixed that going back in history to remote driving didn't change player surface. ( more )
- Fixed LuaSurface::calculate_tile_properties() not ignoring unknown variables. ( more )
- Restored signal-ghost virtual signal. ( more )
- Fixed decider combinator gui could show old input or output signals when fps < ups and last signals change happened at skipped frame.
- Fixed construction robots storing incorrect items in a filtered storage chest if their upgrade job was cancelled. ( more )
- Fixed that changing the volume of a Programmable speaker wouldn't update the volume of a playing sound with Surface playback mode.
- Fixed that changing playback mode of a Programmable speaker wouldn't affect currently playing sounds.
- Fixed that trivial smokes for player effect could cause new chunks to be generated when looking at the map. ( more )
- Fixed missing walking sounds for rails. ( more )
- Fixed that undo removal of tile ghosts did not set the last user. ( more )

### Modding

- Added optional ProgrammableSpeakerNote::cyclic_sound. ( more )

### Scripting

- Added optional 'stop_playing_sounds' parameter to LuaEntity::play_note().
- Added LuaSchedule.
- Added LuaSpacePlatform::get_schedule().
- Added LuaTrain::get_schedule().

## 2.0.35

Date: 20.02.2025

### Minor Features

- GUIs can now also be navigated with D-pad in controller input method.
- Added drag-to-reorder to pins.
- Added drag-to-reorder turret priorities.
- Added drag-to-reorder to infinity chest filters.
- Added drag-to-reorder to editor infinity filters.
- Added drag-to-reorder to deconstruction planner filters.
- Added drag-to-reorder to upgrade planner filters.
- Added drag-to-reorder to module upgrade settings inside upgrade planner destination UI.
- Added drag-to-reorder to inserter, loader, and asteroid collector filters.
- Furnaces can be connected to circuit network.
- Added fluid temperatures to Factoriopedia ingredients and products where relevant. ( more )
- Make drop item hotkey work the same way in GUI as it does in the game world.

### Changes

- Adjusted how walking and driving sounds attenuate with zoom level.
- Added missing walking sounds and fixed incorrect walking sounds for various decoratives.
- Linked fluidbox connections will no longer show a fluid icon.

### Bugfixes

- Fixed that reading localised strings through some methods did not work correctly. ( more )
- Fixed that unpowered inserters could pick up fish. ( more )
- Fixed that spoiled items in modded rocket silos couldn't be removed by inserters. ( more )
- Fixed that virtual items like green-wire or spidertron-remote are no longer showing recycling recipe. ( more )
- Fixed that deleting a surface with off-chunk segmented units could cause consistency checks to fail. ( more )
- Fixed a desync when deleting chart tags pinned by other players. ( more )
- Fixed consistency issues in deconstruction planner UI when toggling "Trees/rocks only" checkbox and tile mode dropdown.
- Fixed space platforms not updating last activity time when advancing schedule to the same planet. ( more )
- Fixed missing frames in fusion generator animation. ( more )
- Fixed a consistency issue when a mod adds fluid to a frozen fluid box. ( more )
- Fixed that LuaFluidBox functions would not work correctly with a frozen fluid box.
- Fixed that frozen fluid boxes would not show the fluid they contained.
- Fixed schedule GUI not updating temporary station status when interrupt triggers from a temporary station which is last in schedule. ( more )
- Fixed furnaces could report as being able to craft certain recipes when they had not enough item ingredient slots. ( more )
- Fixed assemblers could report as being able to craft certain recipes with custom fluidbox indexes when assembler had not enough fluidboxes.
- Fixed furnaces were able to craft recipes with more item products than size of furnace's products inventory.
- Added more detailed healing values for entities healing < 10/s. ( more )
- Fixed a crash when migrating assembler with control behavior into different entity type.
- Fixed that crafting machines with high speeds would not scale input fluid amounts. ( more )
- Fixed a crash in latency when character with exoskeletons moves onto ungenerated chunks.
- Fixed that items spoiling in cargo pods would not run spoil triggers. ( more )
- Fixed that entities upgraded on platforms would not fire the on_space_platform_built_entity event. ( more )
- Fixed that equipment in map editor armor did not work. ( more )
- Fixed consistency issue related to setting signals with with quality only. ( more )
- Fixed a consistency issue when underground belts with items are cloned. ( more )
- Fixed a consistency issue when robots deconstruct heat pipes keeping roboports from freezing. ( more )
- Fixed a crash when flipping an entity with linked fluidbox connections. ( more )
- Fixed a scaling performance issue related to blueprints with asteroid collector and thruster count on space platforms. ( more )
- Fixed that LuaRecord::contents did not accurately reflect the positions of the children.
- Fixed that canceling mod updates would not re-enable the "Update selected" button. ( more )
- Fixed a crash when placing ghost rail signal on top of existing rail signals that is marked to be upgraded. ( more )
- Fixed that copy-settings undo/redo action descriptions would use the wrong surface. ( more )
- Fixed that the map editor tile paint bucket tool did not highlight tiles correctly. ( more )
- Fixed that platform inactivity was not updated when sending cargo to planets. ( more )

### Modding

- Added FurnacePrototype::circuit_connector, circuit_connector_flipped, circuit_wire_max_distance, default_recipe_finished_signal, default_working_signal.
- Added AssemblingMachinePrototype::circuit_connector_flipped.
- Added AssemblingMachinePrototype::max_item_product_count.
- Added LoaderPrototype::adjustable_belt_stack_size.

### Scripting

- Added LuaFurnaceControlBehavior.
- Added LuaTransportLine::force_insert_at.
- Added LuaEntity::loader_belt_stack_size_override read/write.
- Added LuaEntityPrototype::loader_max_belt_stack_size read.
- Added LuaEntityPrototype::loader_adjustable_belt_stack_size read.
- Added on_cargo_pod_finished_descending and on_cargo_pod_delivered_cargo events.
- Added LuaRecord::contents_size read.
- Added CustomInputEvent::cursor_direction.
- Added on_singleplayer_init and on_multiplayer_init.
- Added defines.inventory.assembling_machine_trash and defines.inventory.furnace_trash.

## 2.0.34

Date: 06.02.2025

### Minor Features

- Extended the virtual signals, and unified/changed graphics of some of the existing ones.
- Added an ability to pin the selected resource patch directly from map view.

### Balancing

- Oil Refinery now collides with ice platform ( more )
- water-mud and water-shallow are now landfillable in vanilla (already landfillable in space age) ( more )

### Changes

- Added speed values to the description of demolishers. ( more )
- Drag building produces one merge undo action per the whole drag, instead of the individual undo actions for every entity built.

### Optimizations

- Cargo pod performance when launching from platforms to planets is roughly 687 times faster. ( more )
- Cargo pod performance when landing in cargo bays attached to landing pads is roughly 187 times faster.
- Improved cargo pod and rocket silo rocket performance when waiting in rocket silos by 100%.
- Improved inserter performance when removing items from space platform hubs.

### Bugfixes

- Fixed wrong behaviour in smart belt building over an obstacle with belts soon after the obstacle.
- Fixed smart belt building over an obstacle when there is perpendicular underground belt in the way.
- Fixed a crash when wrapping a rich text image in color tags and pressing backspace. ( more )
- Fixed that changing the force of a segment did not in fact change the force of the entire segmented unit. ( more )
- Fixed demolisher simulation in Factoriopedia.
- Fixed that roboport read-requests could output signals when they weren't actually being requested. ( more )
- Fixed missing link between vehicles and guns in Factoriopedia. ( more )
- Fixed that async saving would freeze the game. ( more )
- Fixed a crash when changing GUI scale with the production statistics open. ( more )
- Fixed textboxes not clearing mouse drag selection when something is typed. ( more )
- Fixed that issuing valid navigation commands to UnitGroups would sometimes fail or succeed immediately. ( more )
- Fixed that attack area commands issued to UnitGroups were not finding valid targets in the attack area. ( more )
- Fixed that super-forced building over belts ignored planned upgrade when adding underground belts. ( more )
- Fixed modifier icon in technology icons would cause the technology icons to draw smaller and off center. ( more )
- Fixed stack inserter not dropping held item that does not match filters when filters were enabled. ( more )
- Fixed yellow tinted rectangles around rail tracks and other sprites on Mac. ( more )
- Fixed Galaxy Of Fame upload timeout errors for bigger saves
- Fixed a crash with a working sound containing an empty main sound. ( more )
- Fixed the research completed sound being played multiple times when multiple researches finish on the same tick. ( more )
- Fixed "Send to orbit automatically" tooltip being incorrect when playing Space Age with mods. ( more )
- Fixed a space platform destination inconsistency when pasting space platform hub settings. ( more )
- Fixed Schedule interrupts not reading any-signal signal counts sent to train correctly. ( more )
- Fixed car orientation being lost when exporting and reimporting blueprint string. ( more )
- Fixed being able to remotely drive enemy vehicles ( more )
- Fixed unrotatable furnaces being rotated when overbuilt with a blueprint ( more )
- Fixed including any filter into deconstruction planner would make it ignore vehicle ghosts ( more )
- Fixed removing tile ghost would sometimes not remove supported entity ghost in the margins ( more )
- Fixed that deconstructing cargo bays connected to cargo landing pads could delete items. ( more )
- Fixed a desync when upgrading underground belts in some cases.
- Fixed a roboport network becoming overfilled with robots when a stationing robot went to a roboport which was being refilled by inserters and the network was full.
- Fixed that a robot didn't resume bobbing after unsuccessful stationing attempt.
- Fixed space platform's asteroid nav mesh could use wrong max tether value when after mods were changed. ( more )
- Fixed a consistency crash related to super force building and underground belts. ( more )
- Fixed that tile prototype's placeable_by.count was ignored when building manually ( more )
- Modified Railgun Turret projectile spawning location such that it would no longer unexpectedly destroy nearby friendly entities ( more )
- Fixed that character light rendering would be wrong when paused while in remote view. ( more )
- Fixed issue which allowed player to get tile ghost over tile of same type (leading to stuck robots) ( more )
- Fixed entities with protected_from_tile_building = false would block tile ghost revival ( https://forums.factorio.com/125189 and https://forums.factorio.com/126504 )
- Fixed overbuilding of storage chests with blueprint of different quality storage chest with filter set would result in unneeded deconstruction ( more )
- Fixed that space connections on the starmap would not use the shortest route if the route passed above the star. ( more )
- Fixed autofilled tile ghosts not raising on_built_entity triggers ( more )

### Scripting

- Added LuaRecord::preview_icons read/write.
- Added record to on_player_setup_blueprint and on_player_deconstructed_area. ( more )
- Added LuaEntity::create_cargo_pod().
- Added LuaEntity::cargo_hatches read.
- Added LuaEntity::cargo_pod_state read.
- Added LuaEntity::cargo_pod_destination read/write.
- Added LuaCargoHatch.
- Added Luaentity::attached_cargo_pod read.
- Added LuaEntity::rocket read.
- Added LuaSpacePlatform::can_leave_current_location().
- Added LuaSpacePlatform::distance read/write.
- Added LuaSpacePlatform::space_connection read/write.
- Changed LuaSpacePlatform::space_location to read/write.

## 2.0.33

Date: 28.01.2025

### Minor Features

- Show a warning in the blueprint library if it's using a lot of RAM.
- Show a warning in blueprint and blueprint book tooltips if they are using a lot of RAM.
- Added fluid contents to the pumpjack tooltip. ( more )

### Changes

- Added hatch count info to platform hub, landing pad and rocket silo.
- Reduced how much you can zoom out in god controller.
- Multiplayer selection rectangles will only show the player name if the player's character is not visible on-screen.
- Moved biter egg handling to be required by promethium science pack instead of quantum processors because that's when they are really needed.

### Graphics

- Fixed reflections on water being broken. ( more )
- Baked in shadows of decaying enemies to have them draw better when on transport belts, and also to save on VRAM. ( more )
- Tweaked some colours of recipes in biochambers so they're a bit easier to tell apart.
- Added destroyed graphics for crushers, and improved their graphics a little bit.
- Added destroyed graphics for space platform thrusters.
- Improved icons of cargo pod.
- Added icon for the technology effect of elevated rails.
- Removed unused spritesheets from the game data folder.

### Optimizations

- Demolishers are now no longer simulated when they are irrelevant to gameplay, and off-screen demolishers are now only partially simulated. ( more )

### Bugfixes

- Fixed that modded rocket silo ingredients that could spoil would not be inserted into the rocket silo crafting inventory. ( more )
- Fixed that some startup errors would cause the mod list to be set to "enable all". ( more )
- Fixed that a demolisher dying to a nuclear reactor meltdown didn't count as a player kill for statistics or achievements. ( more )
- Fixed scaled rich text was not rendered properly. ( more )
- Removed duplicated frame in the fusion generator animation. ( more )
- Fixed that the rail planner did not work on the edges of larger screens. ( more )
- Fixed that LuaPlayer::set_controller would erroneously toggle double-remote view, causing corrupted remote driving states. ( more )
- Fixed "Any planet import zero" wait condition not ignoring requests with zero amount. ( more )
- Fixed request satisfied item selection list showing all qualities. ( more )
- Fixed large amounts of unfulfilled requests blocking delivery of available items. ( more )
- Fixed that turbo splitters used slightly less energy than other splitters to not freeze. ( more )
- Fixed rocket silo tooltip was not aggregating similar items from rocket inventory. ( more )
- Fixed that you couldn't re-select the same item when opening the remote view ghost picker. ( more )
- Fixed that calling LuaGuiElement::remove_tab would not remove the tab content in some cases. ( more )
- Fixed that LuaGuiElement::selected_tab_index would not update when a tab was removed. ( more )
- Fixed that hovering asteroids in a space route in Factoriopedia with a controller didn't highlight the relevant line in the graph.
- Fixed lamps with 'always_on' set in the prototype would still show the checkbox in the lamp GUI. ( more )
- Fixed train stop GUI recentering when trains count goes to 0. ( more )
- Fixed surface list not updating platform position icons when passing a space location without stopping. ( more )
- Fixed assembling machine recipe tooltip not showing ingredients with quality. ( more )
- Fixed edit pin GUI clipping out of the screen at large GUI scales. ( more )
- Fixed mod info panes retaining scroll distance between selection. ( more )
- Fixed map generator GUI scrollpane clipping the resource richness sliders. ( more )
- Fixed spidertron preview zooming in and out in the spidertron UI while walking. ( more )
- Fixed that the cheat mode crafting GUI didn't show quality options at all times. ( more )
- Fixed that CLI arguments would not be preserved when restarting due to a mod load error. ( more )
- Fixed tight spot script crashing when in remote controller. ( more )
- Fixed LuaSimulation API crashing the game when used incorrectly. ( more )
- Fixed that space locations marked as hidden were visible in space platform schedule and platform creation GUI. ( more )
- Fixed that the game would close if a filename-related error was raised in the save game dialog with async saving enabled. ( more )
- Fixed that quitting from the server console while an async save was running would deadlock the server. ( more )
- Fixed that clicking "yes" in the crash dialog would not correctly terminate the Factorio process on Linux. ( more )
- Fixed that roboports marked for deconstruction still wanted to fulfill robot requests. ( more )
- Fixed that attacking biter bases directly or with artillery could award the "It stinks and they don't like it" achievement. ( more )
- Fixed that attacking pentapod bases directly or with artillery could award the "It stinks and they do like it" achievement. ( more )
- Fixed spitters could get stuck attacking trees and rocks blocking their path without dealing any damage to them. ( more )
- Fixed that module replacement logic on space platforms didn't keep the old module if the new module wasn't available. ( more )
- Fixed an issue with asteroid collectors reading content when qualities have level changed. ( more )
- Fixed that rocket turrets and railgun turrets had the wrong fast-replace groups. ( more )
- Fixed that players in cargo pods would activate gates. ( more )
- Fixed util.combine_icons calculated scale from icon_size incorrectly. ( more )
- Fixed that flying text was shown on all surfaces in some cases. ( more )
- Fixed 'speed' parameter of LuaPlayer::create_local_flying_text() not behaving as documented. ( more )
- Fixed quality of held tile item not being visible when showing placement preview. ( more )
- Fixed that technology GUI allowed opening console in multiplayer. ( more )
- Removed several unused sprites. ( more )
- Fixed that prototype defined lamp colors didn't work. ( more )
- Fixed that hidden surface properties would still show in tooltips. ( more )

### Modding

- Renamed WorkingSound::max_sounds_per_type to WorkingSound::max_sounds_per_prototype. The limit is now applied per prototype.
- Removed WorkingSound::apparent_volume.
- Removed WorkingSound::audible_distance_modifier, MainSound::audible_distance_modifier and SoundAccent::audible_distance_modifier. Sound::audible_distance_modifier is used instead.
- Removed PlaySoundTriggerEffectItem::volume_modifier and PlaySoundTriggerEffectItem::audible_distance_modifier.

### Scripting

- Added LuaEntityPrototype::get_pumping_speed. LuaEntityPrototype::pumping_speed is deprecated and should not be used.
- Added optional 'surface' parameter to LuaPlayer::create_local_flying_text().

## 2.0.32

Date: 20.01.2025

### Optimizations

- Improved performance when removing roboports in large active networks by 60%. ( more )

### Graphics

- Removed reflections from lava. Tile transitions to lava now use the foam channel instead to keep their appearance. ( more )

### Bugfixes

- Fixed rocket silo GUI not fitting on small screens. ( more )
- Fixed a crash when writing LuaItem::entity_filters. ( more )
- Fixed that blueprint preview rendering did not work correctly. ( more )
- Fixed a crash with positional GuiEffect sounds with aggregation when dedicated UI sound resources were exhausted. ( more )
- Fixed upgraded blueprint entities would have their flip reverted ( more )
- Fixed worm shooting at fast moving target sometimes created multiple acid puddles with single spit and even outside of its range. ( more )
- Fixed that labs could try to research trigger based technologies. ( more )
- Fixed LuaEntity::get_logistic_sections was not always working with entity ghosts. ( more )
- Fixed selector combinator was using wrong open and close sounds. ( more )
- Fixed remote item requests leaving a visual deconstruction/ghost mark when inserters interacted with the slot. ( more )
- Fixed issue related to rendering items on belts when a belt was also rendered through a camera widget. ( more )
- Fixed that assembler input slots could exceed stack limits. ( more )
- Fixed a crash in assembling machine GUI when the output was full and a recipe containing a research progress product was being crafted. ( more )
- Fixed shooting actions missing vibrations when playing with a controller.

### Scripting

- Added connection_category to LuaFluidboxPrototype::pipe_connections.

### Modding

- Added FluidStream::target_initial_position_only. It's used by worm acid spit.

## 2.0.31

Date: 16.01.2025

### Changes

- Disabled achievements "It stinks and they don't like it", "It stinks and they do like it", and "Get off my lawn" in peaceful mode and no enemies mode. ( more )
- Adding more effect info to yumako, mash, jellynut, jelly, bioflux and slowdown capsule tooltips.

### Bugfixes

- Fixed mouse cursor showing up when exiting Steam Big Picture in controller input method. ( more )
- Fixed belts under elevated rails were not being removed when building a pair of undergrounds. ( more )
- Fixed that inserters could grab items from belts that crafting machines no longer wanted. ( more )
- Fixed taking screenshot could crash in some cases. ( more )
- Fixed that select list background drawing was incorrect for the first row. ( more )
- Fixed that inventory rendering did not work correctly if part of it was off the left or right side of the screen. ( more )
- Fixed that reset technology effects would clear in-progress research triggers. ( more )
- Fixed that writing "nil" to storage_filter did not work correctly. ( more )
- Fixed that UI sounds would not play when dedicated UI sound resources were exhausted. ( more )
- Fixed display panel text and player names were not covered by onboard rocket/cargo pod flight cutscene. ( more )
- Fixed that upgrading pairs of underground belts could transform one end of the belt. ( more )
- Fixed visualisation of asteroid collector range sometimes being drawn wrong. ( more )
- Fixed upgrading a blueprint could fail to upgrade preview icons if the upgrade only changed quality. ( more )
- Fixed clicking space connections in factoriopedia would not update selected items. ( more )
- Fixed that on_equipment_removed did not fire for robots removing equipment. ( more )
- Fixed that some hidden items would show in Factoriopedia. ( more )
- Fixed that Sound::audible_distance_modifier and SoundPrototype::audible_distance_modifier would be effectively applied twice.
- Fixed pentapod eggs default import surface. ( more )
- Fixed that loading old save files created from a freeplay custom scenario would not load because of outdated scripts. ( more )
- Fixed trunk of a specific tree flickered when moving while zoomed out. ( more )
- Fixed "Open character logistics/info/crafting" hotkeys sometimes not closing the character gui. ( more )
- Fixed a desync related to cliffs and deleting multiple chunks in the same tick. ( more )
- Don't auto-focus blueprint parameter fields when using a controller. ( more )
- Fixed a crash when interacting with GUIs while auto-save runs. ( more )
- Fixed that the steam 'low steam remote storage' warning would show even if all steam remote storage options were disabled. ( more )
- Fixed that player.render_mode didn't report chart_zoomed_in for the remote controller. ( more )
- Fixed crash when clicking a shortcut rich text link in controller input method.
- Fixed BP of storage chest with filters would be incorectly overbuilt over non-storage logistic chests ( more )
- Fixed quality icon being shown twice in in-world icons for blacklist quality filter (without entity)
- Fixed a crash when building entities with linked pipe connections in multiplayer latency. ( more )
- Fixed that manually launching items to space platforms would wrongly say some combination of items wouldn't fit. ( more )
- Fixed that map rendering would wrongly show your player as on the map when paused. ( more )
- Fixed that going back in browse history didn't return to player location if the character was in space platform hub.
- Fixed an audible click at certain zoom levels when playing positional sounds with custom zoom attenuation and aggregation.
- Fixed offshore pump underwater patch was not rendered under water.
- Fixed issue where plants were not being destroyed when (super)force building entities that autofill tiles that collide with them ( more )
- Fixed loading of scenarios when entities were configured with difficulty settings. ( more )
- Fixed biters and pentapods getting frozen mid-attack. ( more )
- Fixed infinity container parametrization could set empty filters causing crash on saving.

### Scripting

- ItemPrototype::spoil_result and spoil_to_trigger_result can now be used at the same time.

## 2.0.30

Date: 10.01.2025

### Changes

- Changed map generated lightning attractors to always produce full-health items when mined. ( more )
- Reordered results of scrap recycling to make the recycler stack them on belts more efficiently. ( https://mods.factorio.com/mod/better-scrap-stacking ) ( more )

### Bugfixes

- Fixed that item request proxies would show bad "missing materials for construction" counts. ( more )
- Fixed a crash when creating a ghost assembling machine with a pre-set recipe through script. ( more )
- Fixed a multiplayer latency related crash when deleting surfaces. ( more )
- Fixed crash due to division by zero when line_length of sheet definition of SpriteVariations was 0. ( more )
- Fixed quality filter comparators did not dim at night. ( more )
- Fixed ammo turrets with target leading would undershoot ammo with range modifier. ( more )
- Fixed opening a train stop on another surface from a tag would show the wrong trains. ( more )
- Fixed only pings from last message in a given tick were being recognized. ( more )
- Fixed circuit condition signal selection title was "Set the filter" instead of "Select a signal". ( more )
- Fixed asteroid collector could fail to grab some chunks if there were no other chunks nearby. ( more )
- Fixed a crash when interacting with ghost assembling machines after migrating recipes. ( more )
- Fixed crash when using the same sprite as both decal and decorative. ( more )
- Fixed that cycling quality did not work while the mouse was over scrollable widgets. ( more )
- Fixed that logistic groups could get broken when mining and un-doing ghost logistic containers. ( more )
- Fixed long custom ending text would not fit in the victory screen. ( more )
- Fixed that hidden surfaces would show in the evolution command. ( more )
- Fixed a crash when hovering some widgets at very small resolutions. ( more )
- Fixed that orbital request weight tooltips wouldn't show any decimal values. ( more )
- Fixed a crash when quitting abnormally in multiplayer while the menu was visible. ( more )
- Fixed that labs would consume power for one tick when not working. ( more )
- Fixed that the mods GUI did not fit on small screens such as the Steam Deck. ( more )
- Fixed crash when frame count of animation layer definition using stripes didn't match frame count of previous layer. ( more )
- Fixed hovering cursor over undo button could change rail planner start location. ( more )
- Fixed missing Ў character in the game font. ( more )
- Fixed yet another issue with flow statistics. ( more )
- Fixed script rendering objects targeting an entity didn't draw at render position of the entity. ( more )
- Fixed issue of incorrect undo of deconstruction of multiple tile ghost with common dependent entity ghost ( more )
- Fixed macOS Game Mode not activating for the non-Steam version of the game.
- Fixed that items would end up in crafing machine trash slots when it wasn't desired. ( more )

### Scripting

- Added LuaEntity::inserter_spoil_priority read/write.

## 2.0.29

Date: 06.01.2025

### Minor Features

- Added smart pipette for items on the ground.

### Graphics

- Improved graphics of Recyclers.
- Added corpse graphics for Asteroid Collectors.

### Bugfixes

- Fixed a crash when mods define heat pipes with heating_radius of 0.
- Fixed that deleting a surface with global electric network would leak an electric network. ( more )
- Fixed blueprint could be configured with invalid set of grid size and absolute grid position. ( more )
- Fixed that the space map would not show when unlocking space-locations. ( more )
- Fixed map artifacts on space platforms when removing in-progress builds. ( more )
- Fixed that frozen radars still worked. ( more )
- Fixed that instant blueprint over-building would not auto fulfill item requests. ( more )
- Fixed that marking a space platform to be deleted while a starter pack is on the way would break the platform state. ( more )
- Fixed statistics would not include values from a newest sample that is still being created. ( more )
- Fixed an issue with memory management in some cases when rotating entities. ( more )
- Fixed a crash related to modded triggers on spider legs. ( more )
- Fixed that hidden mining drills would still show in "mined by" in resource tooltips. ( more )
- Fixed that the artillery wagon auto-targeting checkbox was not shown when the artillery had an equipment grid. ( more )
- Fixed LuaTransportLine::get_line_item_position would return incorrect positions. ( more )
- Fixed that writing to LuaPlayer::opened did not update the GUI in multiplayer. ( more )
- Fixed pumps were setting filter when given negative fluid signals. ( more )
- Fixed a crash related to merging forces and gui. ( more )
- Fixed trains could switch to manual when due to interrupts the schedule became empty. ( more )
- Fixed math expressions were not accepting numbers with positive exponent and + sign. ( more )
- Fixed a desync related to worker robots charging when force has worker robot battery bonus set.
- Fixed a crash when installing mods with almost-cyclic dependencies. ( more )
- Fixed that changing surface::localised_name did not update the surfaces list in remote view. ( more )
- Fixed that quality could add a supply area to an electric pole without one. ( more )
- Fixed that the LAN games browser would not show anything if the public-games filter was set to only show favorites. ( more )
- Fixed a crash related to cargo pods when loading older save files. ( more )
- Fixed bad rendering logic for space platform trash slots. ( more )
- Fixed that flying robots did not render quality indicators correctly. ( more )
- Fixed arithmetic combinator gui not refreshing circuit network selection when combinator parameters are changed externally. ( more )
- Fixed solar panels bonus description didn't display correctly. ( more )
- Fixed copy source was cleared when source entity was built from ghost or destroyed leaving ghost. ( more )
- Fixed that tesla turret chain bolts could damage protected biter spawners. ( more )
- Fixed that some actions would still be processed while the game was paused. ( more )
- Fixed a latency armor related crash. ( more )
- Fixed that some remote view GUI elements did not align correctly. ( more )
- Fixed that Factoriopedia would claim some recipes as exclusive to a given planet/location when they weren't. ( more )
- Fixed that the blueprint GUI didn't render vehicles correctly. ( more )
- Fixed that you could launch yourself to a platform in flight. ( more )
- Fixed that changing loader direction through script could cause transport lines to become inconsistent. ( more )
- Fixed that plants would show the wrong expected amount in deconstruction planner totals. ( more )
- Fixed that map pipeline rendering would show other forces pipes. ( more )
- Fixed that pipette over tiles would always override other actions bound to the same hotkey. ( more )
- Fixed that vehicles would get stuck as 'reserved by remote driver' if they died while being remote driven. ( more )
- Fixed inserters would keep using filters after migration when new prototypes disallowed usage of filters. ( more )

### Scripting

- Added LuaRecord::get_active_index.
- Added LuaEntityPrototype::science_pack_drain_rate_percent read.
- Added LuaEntityPrototype::get_fluid_usage_per_tick. LuaEntityPrototype::fluid_usage_per_tick is deprecated and should not be used.
- Added LuaEntityPrototype::get_max_power_output. LuaEntityPrototype::max_power_output is deprecated and should not be used.
- LuaEntity::combinator_description supports ghosts of combinators.
- Added LuaDefines::car_trash read. ( more )
- Added asteroid collector support to LuaEntity::get_filter, set_filter, and filter_slot_count.
- Added LuaPlayer::clear_recipe_notification().
- Changed LuaEntity::get_passenger() to give the character in cargo pods. ( more )
- Added LuaControl::hub read.
- Changed LuaEntity::cargo_pod read into LuaControl::cargo_pod read and made it work for players in cargo pods.
- Changed LuaEntity::get_logistic_point() and LuaEntity::get_logistic_sections() to work with ghosts.

### Modding

- Added CargoWagonPrototype::quality_affects_inventory_size.
- Added FluidWagonPrototype::quality_affects_capacity.

## 2.0.28

Date: 20.12.2024

### Optimizations

- Improved GUI performance when logistics status diode is part of the structure. ( more )

### Bugfixes

- Fixed a crash when units spawned by an enemy spawner are destroyed by script during created effect.

## 2.0.27

Date: 18.12.2024

### Changes

- Wrigglers will no longer proactively attack pollen emitters. However, they will still respond to artillery.
- Attack groups containing stompers or strafers will now contain fewer units.
- Large egg rafts will try to have at least one stomper or strafer spawned at a time.
- Small egg rafts no longer absorb pollution because they will never produce stompers or strafers.

### Graphics

- Aquilo icebergs have longer shadows to integrate with the world better.

### Bugfixes

- Fixed that the asteroid collectors circuit condition referred to inserters. ( more )
- Fixed that hidden planets still showed in the map preview GUI. ( more )
- Fixed a crash when loading new modded tips and tricks with a "dependencies met" trigger but no dependencies.
- Fixed a crash when interacting with modded equipment ghosts. ( more )
- Fixed that a robot wouldn't play a tile mined_sound when deconstructing it.
- Fixed that a robot would play a deconstruct sound regardless of whether the deconstruction succeeded or not. ( more )
- Fixed a consistency issue related to loading script rendered animations when animation is no longer available. ( more )
- Fixed a desync related to asteroid collectors and distant chunks optimization when asteroid collector is destroyed. ( more )
- Fixed a crash when opening an audio stream encounters a filesystem error. ( more )
- Fixed a performance issue when exiting the game while large modded entities exist. ( more )
- Fixed that the personal logistics area would render incorrectly when the game was paused. ( more )
- Fixed that quality science packs would show "100%" remaining. ( more )
- Fixed that the open-factoriopedia hotkey did not work in some cases. ( more )
- Fixed that fog of war was not rendered while dead. ( more )
- Fixed that opening the technology GUI while dragging the map would continue to drag the map. ( more )
- Fixed a crash when deleting a space platform which had cargo bays built in a specific order. ( more )

### Modding

- TipsAndTricksItem requires at least one dependency if it has a `dependencies-met` trigger.
- Added UnitAISettings::size_in_group and UnitAISettings::join_attacks.
- Added LuaAISettings::size_in_group and LuaAISettings::join_attacks.
- Added EnemySpawnerPrototype::max_count_of_owned_defensive_units and EnemySpawnerPrototype::max_defensive_friends_around_to_spawn.
- Added LuaEntityPrototype::max_count_of_owned_defensive_units and LuaEntityPrototype::max_defensive_friends_around_to_spawn.

### Scripting

- Added LuaSurface::ignore_surface_conditions.

## 2.0.26

Date: 16.12.2024

### Minor Features

- Re-added the sandbox scenario questionnaire.

### Changes

- Space age mods no longer count as "has mods" in the server browser. ( more )
- Removed default secondary keybinding for redo action on AZERTY keyboards as it collided with super force building while moving up. ( more )

### Optimizations

- Improved asteroid collector performance - we estimate it should be 5x - 15x faster when there are thousands of asteroid chunks on the map. ( more )
- Improved asteroid update performance by up to 20%.

### Bugfixes

- Fixed a crash at startup when mods would define fluid with no fuel value as a fluid energy source fuel. ( more )
- Fixed that LuaPlayer::opened did not work with equipment grids. ( more )
- Fixed some asteroid graphic variations were defined twice. ( more )
- Fixed that it was possible to click the update selected mods button while update data was being fetched. ( more )
- Fixed several edge cases where the mod explore results table selection would get out of sync with the mod info pane. ( more )
- Changed graphics setting turret-overdraw-scale-threshold to turret-overdraw-estimated-pixel-overdraw-threshold to fix artillery range overdraw performance. ( more )
- Fixed fulgorite pieces icon had empty mipmaps. ( more )
- Fixed that rocket silos would not launch quickly when there were platform requests that couldn't be satisfied. ( more )
- Fixed a crash when building terrain in remote view. ( more )
- Fixed that layered quality icons did not work correctly in recipe overlays. ( more )
- Fixed that "hidden in factoriopedia" technologies still showed in Factoriopedia. ( more )
- Fixed a crash when mods set ItemRequestProxy::active to false. ( more )
- Fixed incorrect space platform bounds and weight when space platform foundations were covered by other tiles.
- Fixed a crash when mining closed power switch. ( more )
- Fixed a performance issue when rendering radar minimap visualization. ( more )
- Fixed a crash when clicking give-item technology modifiers in the technology GUI. ( more )
- Fixed a crash when a recipe has a research-progress result. ( more )

### Scripting

- Added LuaEntity::minable_flag read/write. Write to LuaEntity::minable is now deprecated.
- Added LuaEntity::is_updatable read, disabled_by_script read/write, disabled_by_control_behavior read and disabled_by_recipe read.
- Added LuaEntity::is_freezable read and frozen read.

## 2.0.25

Date: 12.12.2024

### Minor Features

- Dragging and dropping a blueprint file into the game window will import the file contents as a blueprint string.
- Dragging and dropping text into the game window on X11 will import the text as a blueprint string.
- Factoriopedia now shows recycling recipes for each item.
- Cargo pod scheduling reworked to send larger and more spaced out deliveries. This should improve the frequency of trickling space science and material drops.

### Changes

- Inserters (especially ghost long handed ones) spawn in stretched to an appropriate distance.
- Reverted fix for god controller being able to zoom out to map view. ( more )
- Changed selector combinator circuit wire reach to be the same as wire reach of other combinators.

### Graphics

- Asteroid collector tentacles have less colourful rainbow effect on them.

### Bugfixes

- Fixed that victory condition didn't trigger when the platform was paused or didn't stop at solar system edge. ( more )
- Fixed a crash when copying logistic filters into blueprints. ( more )
- Fixed that Factoriopedia would close if a GUI behind it was changed. ( more )
- Fixed a crash when fast-replacing the platform hub. ( more )
- Fixed that the mod manager would not account for mods hidden by search when browsing dependencies. ( more )
- Fixed a crash on Mac when driving a car in multiplayer when the player has no character. ( more )
- Fixed a crash when drawing EntityButtons with entities with inverted selection boxes. ( more )
- Fixed that pumps would run endlessly if the input fluid was incompatible. ( more )
- Fixed station list could be sometimes sorted incorrectly. ( more )
- Fixed trashing logic would not run after cancelling deconstruction of entity. ( more )
- Fixed reverting technologies with recipe unlocks would lock recipe that is still unlocked by other technology. ( more )
- Fixed railgun turret would not draw out of power when ammo was inserted. ( more )
- Fixed that logistic network content tooltips didn't show nice numbers. ( more )
- Fixed blueprint export to string would create malformed blueprint if it contained decider combinator with empty conditions or empty output. ( more )
- Fixed consistency issue when power switch was destroyed leaving a ghost. ( more )
- Fixed inserters could in some cases interact with elevated cargo wagons. ( more )
- Fixed mods could specify an assembling machine with fixed quality without specifying fixed recipe. ( more )
- Fixed research was not correctly counted in total item production statistics. ( more )
- Fixed rocket silo control behavior would not update outputs when connecting wire. ( more )
- Fixed that fast-replacing crafting machines would not preserve the mirrored orientation of the original machine. ( more )
- Fixed that burner inserters would load too much fuel when fed by inserters. ( more )
- Fixed nuclear power achievement could be obtained without burning uranium fuel cell if it was consumed for crafting. ( more )
- Fixed that clicking the sort buttons in the save-map GUI would reset the save name field. ( more )
- Fixed demolisher in vulcanus crossing menu simulations would sometimes render health bar. ( more )
- Fixed a crash when opening the console while a platform tooltip was shown. ( more )
- Fixed that the cursor theme was not being respected when running on GNOME Wayland. ( more )
- Fixed loader was able to insert items into asteroid collector. ( more )
- Fixed flamethrower turret sound still playing after being deactivated or destroyed with its ghost created. ( more )
- Fixed cars and tanks would keep their speed through a ghost when dying. ( more )
- Fixed fluid parameters were not showing when selecting fluids for wait condition. ( more )
- Fixed gleba tree sprites still had blue line at their upper edge under some conditions. ( more )
- Fixed deconstruction planner would not mark rails for deconstruction if they were dependency of a rail support that was instantly removed. ( more )
- Fixed cargo pods with passenger would select landing spots using incorrect bounding box. ( more )
- Fixed blueprint parametrization would allow selecting hidden recipe that can be crafted. ( more )
- Fixed that writing invalid font names to custom GUI elements would crash the game to desktop. ( more )
- Fixed cryogenic science pack recipe was incorrectly considering entire fluoroketone input as a catalyst. ( more )
- Fixed fish breeding recipe was applying productivity to catalyst. ( more )
- Fixed a crash when trying to set infinity chest filter with non zero count but empty name. ( more )
- Fixed a crash when super force building blueprint with belts and external wires in latency. ( more )
- Fixed 'import from' option changing when setting requested item quality on platforms. ( more )
- Fixed that assemblers without fluid boxes were incorrectly considered rotatable. ( more )
- Fixed burner energy source would not report out of fuel when incompatible items were in the fuel inventory. ( more )
- Fixed that some damage tooltips were incorrect. ( more )
- Fixed that any tag being changed would refresh any active tag-edit GUI. ( more )
- Fixed many smaller GUIs still not supporting non-English search ( more )
- Fixed a desync related to cargo landing pads trash inventory when playing without Space Age.
- Fixed a crash when mods use fixed recipes with surface conditions in machines that don't have surface conditions. ( more )
- Fixed copying display panel would copy icon and text regardless of control behavior being active. ( more )
- Fixed nuclear reactor was heating tiles farther than it would heat entities. ( more )
- Fixed asteroid background rendering black lines when graphics driver forces anisotropic filtering. ( more )
- Fixed that "auto requests for space platforms" was not preserved in blueprint strings. ( more )
- Fixed that changing "send to orbit automatically" on rocket silos did not work when in ghost form. ( more )
- Fixed electric network statistics could show total value that was larger than expected caused by counting incomplete next sample. ( more )
- Fixed that importing save files in the map editor would crash the game. ( more )
- Fixed current research tooltip would show incorrect progress values. ( more )

### Modding

- UTF-8 encoding is now checked for all mod text files to ensure proper rendering. Mods with ANSI encoded text files will not load anymore. (Prompted by https://forums.factorio.com/120452 )
- Added InserterPrototype::starting_distance.
- Added minimum collision box restriction to cargo bays, cargo landing pads and space platform hubs. ( more )
- Burner inserter initial energy amount was changed to be defined on the burner energy source prototype.
- Changed UseEntityInEnergyProductionAchievementPrototype::consumed_condition into ItemIDFilter.
- ItemProductPrototype and FluidProductPrototype ignored_by_productivity defaults to value of ignored_by_stats.
- Added heating_radius to ReactorPrototype and HeatPipePrototype.

### Scripting

- Added LuaBurnerPrototype::initial_fuel and initial_fuel_percent read.
- Added LuaSpacePlatform::last_visited_space_location read.
- Added LuaSpacePlatform::paused read/write.

## 2.0.24

Date: 05.12.2024

### Minor Features

- Added "Nauvis Bus" and "Nauvis Power Up" menu simulations.
- Added camera views to Space platform tooltips.
- Added radar minimap visualization for roboports and cargo landing pads. ( more )

### Graphics

- Changed the Space crafting category icon to look like a cargo pod instead of rocket silo.
- Changed the Rocket part icon to look more like a part of the rocket.

### Balancing

- Land mines on space platforms now damage the space platform tiles in a radius.
- Changed rocket fuel from ammonia recipe to require the same amount of solid fuel as the main rocket fuel recipes to prevent a recycling loop. ( more )

### Changes

- Tweaked how entities are selected in remote view when using a gamepad. The entity directly under the crosshair is much more likely to be selected.

### Bugfixes

- Fixed a desync related to building rails with rail planner in latency. ( more )
- Fixed a crash when opening a planet with empty cliff generation settings in Factoriopedia. ( more )
- Fixed a crash when the last roboport is disconnected while searching in Logistic networks GUI. ( more )
- Fixed that items could be inserted into rocket inventory while the silo was in "automatic requests" mode. ( https://forums.factorio.com/118442 , https://forums.factorio.com/123172 )
- Fixed that downgrading an entity ghost didn't remove invalid item insertion requests. ( more )
- Fixed that robots could enter roboports marked for deconstruction. ( more )
- Fixed pipes and pipe shadow graphics on flipped biochamber. ( more )
- Fixed recycler showing greater than 300% productivity in the tooltip. ( more )
- Fixed crash when rendering thruster with ThrusterPrototype::plumes set to nil. ( more )
- Fixed that higher quality pumpjacks would produce less oil. ( more )
- Fixed that ghost building electric poles did not always space them correctly. ( more )
- Fixed rocket turrets not shooting spawners with capture robots. ( more )
- Fixed a crash when demolishers are killed as a direct result of attacking something. ( more )
- Fixed a crash when a robot tried to move in the same tick as it was deactivated by script. ( more )
- Fixed a crash when reordering time-based wait conditions in multiplayer. ( more )
- Fixed that a thruster deactivated by script still rendered the exhaust flames. ( more )
- Fixed that reading collision mask from LuaEntityPrototype could give incorrect collision mask when there were no layers. ( more )
- Fixed that players with open blueprint creation GUI were unable to open menu when the game was paused. ( more )
- Fixed parametrization of selector combinator would propose variables not relevant due to current mode. ( more )
- Fixed parametrization was not covering inserter, assembler and reactor signals. ( more )
- Fixed some recipes would give items of wrong quality when changing quality effect. ( more )
- Fixed a dying turret could be disabled by control behavior causing it not able to finish dead animation. ( more )
- Fixed a rare crash in CargoPod code when loading a Space Age save file with Space Age disabled. ( more )
- Fixed that LuaSurface::force_generate_chunk_requests() would not force all chunks correctly if generate_with_lab_tiles was true. ( more )
- Fixed a desync when changing force friends/ceasefire. ( more )
- Fixed that railguns could get stuck switching targets and not fire. ( more )
- Fixed trying to parametrize inserter stack size would clamp them to max stack size of neutral force. ( more )
- Fixed construction robots from the personal roboport being stuck in a loop when fulfilling delivery requests for construction robots. ( more )
- Fixed production-entity-list showing values for space age when only quality mod was enabled. ( more )
- Fixed a crash when mods cancel deconstruction of a rolling stock while it's being marked for deconstruction. ( more )
- Fixed that stack inserters could deadlock in some cases. ( more )
- Fixed that disabling Space Age mod removed Space Age achievements when playing a non-modded game. ( more )
- Fixed shortcut bar GUI clipping off screen in remote view. ( more )
- Fixed that Gleba generated cliffs when they were disabled. ( more )
- Fixed rapidly changing platform schedule would make it impossible to view that platform. ( more )
- Fixed Space platform tooltip flickering for 1 tick when another platform schedule/location changes. ( more )
- Fixed Space platform position indicator not updating in some cases. ( more )
- Fixed long logistic group name pushing delete button out of view. ( more )
- Fixed rocket silo in "automatic requests" mode not trashing spoiled items. ( more )
- Fixed assemblers with parameter recipe would not flip correctly. ( more )
- Fixed building rails in some cases could attempt to build them in wrong order causing a build attempt to be performed before a required support was built. ( more )
- Fixed bonus from research of character health is now showing in factoriopedia. ( more )
- Fixed that the pump would lose its filter when fast-replaced. ( more )
- Fixed setting generate_map in SimulationDefinition would not allow to have map generated in simulations. ( more )
- Fixed pipette of hazard concrete tiles would not set correct build direction. ( more )
- Fixed control settings menu sometimes growing in size when interacting with it. ( more )

### Modding

- Added support for Opus audio codec.
- Added FluidBox::mirrored_pipe_picture and mirrored_pipe_picture_frozen.
- Added CharacterArmorAnimation::mining_with_tool_particles_animation_positions.
- Underground fluid box connections with incompatible underground_collision_mask are allowed to connect as long as tiles between do not collide with any of them.

### Scripting

- Added LuaCustomEventPrototype::event_id read.
- Added LuaCustomInputPrototype::event_id read.
- Added LuaBootstrap::get_event_id.
- Unified parsing of event types into LuaEventType. Made it possible to specify custom events and custom inputs by providing prototype instance.
- Custom events and custom inputs defined by prototypes are given constants inside of defines.events.

## 2.0.23

Date: 28.11.2024

### Changes

- Added an error message when manually trying to launch a rocket to a full space platform.
- Changed space platforms to not delete items on the ground when deconstructing them. ( more )
- Added back a simple version of the Sandbox scenario. Improved the behavior of god controller.

### Optimizations

- Improved asteroid chunk creation and movement performance.
- Improved chart overlay performance in several cases.

### Bugfixes

- Fixed that clicking the "delete blueprint book" button in the same tick auto-save started as a multiplayer host would crash the game. ( more )
- Fixed that the display panel would lose its settings when fast-replaced. ( more )
- Fixed that the bonus GUI did not show recyclers benefiting from belt stack size research. ( more )
- Fixed that space platforms could get stuck waiting for rockets which became frozen. ( more )
- Fixed spidertron inventory sort interfering with item pickup requests. ( more )
- Fixed problems with incorrect setting of allowTipActivationFlag. ( more )
- Fixed robots attempting to enter a roboport which had all slots reserved for robots of a different type. ( more )
- Fixed trains and logistics map views would not preserve their settings. ( more )
- Fixed the tips and tricks window on small screens.
- Fixed on screen keyboard appearing when some tips and tricks were shown. ( more )
- Fixed renaming all trains stops wouldn't rename the stops in wait conditions or interrupts. ( more )
- Fixed that slow-moving asteroid chunks didn't collide with space platform tiles. ( more )
- Fixed a crash when the game tried to unlock Steam achievements in minimal mode.
- Fixed a crash when trying to open tips and tricks from chat. ( more )
- Fixed that cancelling entity upgrade didn't remove invalid requests. ( more )
- Fixed choppy fog animation in saves with 300+ hours of play time. ( more )
- Fixed a consistency issue when script inserts items at the back of a stopped transport belt. ( more )
- Fixed requested robots failing to cross a gap in the network. ( more )
- Fixed that space platform included thrusters marked for deconstruction in "can produce enough thrust" calculation. ( more )
- Fixed death messages for players with no username. ( more )
- Fixed stack inserters would not drop held items if they became incompatible due to filter change.
- Fixed Quick Panel Panels tab missing next/previous page labels. ( more )
- Fixed a crash when opening assembling machines with a fixed recipe in latency. ( more )
- Fixed that some recipes could not be crafted by god controller. ( more )

## 2.0.22

Date: 26.11.2024

### Minor Features

- Assemblers circuit allows to choose if items in crafting should be included by read contents.
- Asteroid collector circuit allow to choose if items held by hands should be included by read contents.

### Changes

- Jelly is no longer mined from Slipstack trees so it is less confusing where to get jelly from.
- Nightvision is less orange.
- Moved the "Any quality" option into the comparison dropdown.
- Disabled spoiling for items created in an infinity chest until the first time they are removed from said chest.
- Removed "Select previous technology" control which didn't work (replaced with the generic back/forward navigation in 2.0). ( more )

### Bugfixes

- Fixed that undo tooltips could show the wrong surface. ( more )
- Fixed quality selector not appearing in infinity chest GUI if qualities are not yet unlocked. ( more )
- Fixed quality selectors in unfocused windows reacting to quality cycling. Fixes quality cycling while selecting upgrade planner entity modules.
- Fixed selector combinator using the old quality dropdown UI.
- Fixed a desync when holding blueprints with spidertrons. ( more )
- Fixed "option" key name on macOS. ( more )
- Fixed modifier key order on macOS.
- Fixed that reaching inventory transfer limit didn't cancel additional item requests. ( more )
- Fixed performance issue when long transport line sequence is remerging while having active belt reader. ( more )
- Fixed "So Long and Thanks for all the Fish" achievement not triggering with Space Age enabled ( more )
- Fixed robots cancelling module upgrade requests if they didn't have enough storage for the old modules. ( more )
- Fixed that upgrading a rocket silo destroyed the second rocket if it was prepared. ( more )
- Fixed drawing of quality conditions in entity/blueprint preview in GUI. ( more )
- Fixed screenshot command crash when passing zoom of 0. ( more )
- Fixed it was not possible to copy settings between artillery wagons. ( more )
- Fixed another script issue in orbital logistics tips. ( more )
- Fixed that undoing a module upgrade didn't update the GUI. ( more )
- Fixed missing technology dependencies in quality technologies when playing base+quality. ( more )
- Fixed stack inserter would start dropping partial held stack when waking up by control behavior. ( more )
- Fixed an issue with obtaining achievements after loading a save file in some cases. ( more )
- Fixed construction robots not delivering items to an entity marked for upgrade. ( more )
- Fixed rocket silos requesting more items than their inventory size. ( more )
- Fixed flamethrower sound still playing after a tank is deactivated or destroyed with its ghost created. ( more )
- Fixed a crash when interacting with ghost tanks in some scenarios. ( more )
- Fixed persistent working sounds remaining silent after fading out on pause. ( more )
- Fixed that you could exit the rocket while landing on space platforms. ( more )
- Fixed a crash when your inventory was full and robots were trying to store items in your inventory. ( more )
- Fixed that infinite item resources would not produce if the yield went below 100%. ( more )
- Fixed that the automated insertion limit tooltip for artillery turrets was incorrect. ( more )
- Fixed cargo pod didn't have transparent background when landing on Fulgora. ( more )
- Fixed some light sprites rendered incorrectly when Occlude light sprites option was disabled. ( more )
- Fixed surface list being too tall when loading into a game in remote view. ( more )
- Fixed generic interrupt logic not replacing station names in wait conditions. ( more )
- Fixed that modded custom cameras would always show fog of war. ( more )
- Fixed a crash when pinning resource patch results that had been fully mined. ( more )

### Modding

- Corpses used by entities with health automatically use the collision box of the parent entity. ( more )
- Added LuaEntityPrototype::auto_setup_collision_box which defaults to true.

### Scripting

- Added LuaEntityPrototype::auto_setup_collision_box read.
- Events::on_cargo_pod_finished_ascending Lua event added.
- 'rocket-launched' achievement condition now triggered by cargo pod ascending instead of rocket.
- removed property 'player_index' from Events::on_rocket_launched data.
- Changed LuaLogisticPoint::targeted_items_deliver and targeted_items_pickup to include quality.
- Changed all instances of get_item_count to support quality.
- Changed LuaPlayer::get_quick_bar_slot to include quality.
- Changed LuaEquipmentGrid::get_contents() to include quality.
- Changed LuaEquipmentGrid::count() to support quality.
- Changed LuaEntity::storage_filter read to include quality.
- Added quality to selected_prototype during custom input events.
- Added GameViewSettings::show_surface_list property to control its vibility in the Remote View.

## 2.0.21

Date: 21.11.2024

### Minor Features

- Added drag-to-reorder to the research queue.
- Added "Occlude light sprites" graphics option to allow disabling 2.0 light rendering to improve performance. As a side effect, it disables also lava glow. ( more )
- Added "Additional terrain effects" graphics option to disable puddles and global terrain tint as alternative to increase performance on Gleba to disabling fog, clouds and animated water.

### Changes

- Replaced the "move forward" and "move backward" buttons on technologies in the research queue with a draggable handle.
- Allowed to set blueprint parameter to be ingredient of other parameter even when it doesn't exist in an assembling machine. ( more )
- Added a hidden sound setting to base the music selection on the character's physical location. ( more )
- Agriculutral Tower now respects allied ghosts blocking planting spots. ( more )
- volcanic-cracks-hot no longer coverable by foundation. ( more )
- Added consistency check for overlapping blueprint tiles not being both (non)-foundations. Any inconsistent tiles will be removed on load (analogous already happens when importing blueprint via string or setting blueprint tiles via lua).
- The slider and input field for the minimum payload in orbital logistic requests now enforce a minimum of 1 instead of 0. ( more )
- Added a delay before music switches when switching surfaces. ( more )
- Added hidden sound setting for controlling music transition stage durations.
- Improved performance of superforced blueprint preview that is autofilling-in tiles.

### Bugfixes

- Fixed double parameter selection in signal selection list.
- Fixed additional invalid state of collector navmesh. ( more )
- Fixed "Make it better" achievement not obtained when dropping modules in. ( more )
- Fixed dragging sliders with gamepad in free cursor mode.
- Fixed a sound instance leak related to sound priority. ( more )
- Fixed that selection tool highlighting would show incorrectly in chart view for 1 frame. ( more )
- Fixed a crash when destroying segmented units during the chunk generated event. ( more )
- Improved logic for choosing which schedule to keep if trains get connected ( more )
- Fixed a crash after deconstructing cargo bays with editor. ( more )
- Fixed tutorial missions 4 and 5 missing access to radars and repair packs. ( more )
- Fixed spidertrons shooting extra capture robot during tick of projectile creation. ( more )
- Fixed condition highlights in decider combinator GUI not always updating if a condition used the "Each" special signal.
- Fixed that energy sources would not update their buffer sizes when the prototype value would change. ( more )
- Fixed that asteroids would calculate damage to entities with resistances incorrectly. ( more )
- Fixed use of slow GPU timer query operation on macOS.
- Fixed that opening ghost power poles would leave the GUI in a broken state. ( more )
- Toggle menu (escape) leaves remote driving. ( more )
- Fixed that equipment ghost tooltips did not show quality. ( more )
- Fixed incorrect consistency check when trash not requested is used inside of a blueprint and mods are involved. ( more )
- Fixed that portable solar panels and power armor tooltips did not report the correct amount of power generation for the current surface. ( more )
- Fixed that changing Vulcanus map gen settings using the editor prevented ashlands trees from spawning. ( more )
- Fixed that paste-settings could happen when not desired in some situations. ( more )
- Fixed that mobile logistic networks could generate useless alerts in some situations. ( more )
- Fixed robots repeatedly failing to cross Aquilo lake due to high energy usage and being stuck in a loop. ( more )
- Fixed robots looking for a place to charge always picking roboports closer to their target which resulted in overcrowding. ( more )
- Fixed a crash when attempting (and failing) to connect trains parked at specific positions. ( more )
- Fixed a crash when removing a station from a train schedule while another train in the same group used the final stop as waypoint. ( more )
- Fixed that agricultural tower would show all nauvis tiles as unplantable. Nauvis grass, dirt and red desert are now specifically plantable for tree seeds and highlight as green. ( more )
- Fixed Space age map generation not respecting custom starting locations (apart from Nauvis). ( more )
- Fixed technology slot showing research progress for finished trigger technologies. ( more )
- Fixed that reloading specific technologies would leave the dead technology trigger pointer in the trigger processor. ( more )

### Modding

- Added distance_from_nearest_point_x and distance_from_nearest_point_y noise expressions.
- Moved SpiderVehiclePrototype::chunk_exploration_radius to VehiclePrototype.
- Removed limit of 64 unique PipeConnectionDefinitions's connection categories.
- Removed music_transition_* utility constants.
- Changed CraftItemTechnologyTrigger::item into ItemIDFilter. Removed item_quality.
- Changed ProduceAchievementPrototype::item_product into ItemIDFilter. Removed quality.
- Changed ProducePerHourAchievementPrototype::item_product into ItemIDFilter.

### Scripting

- Added optional build_check_type to LuaControl::teleport. ( more )
- Added LuaEntityPrototype::heating_energy read. ( more )
- Added LuaForce::circuit_network_enabled, cliff_deconstruction_enabled, mining_with_fluid, rail_support_on_deep_oil_ocean, rail_planner_allow_elevated_rails, vehicle_logistics read. ( more )

## 2.0.20

Date: 18.11.2024

### Minor Features

- Added gamepad stick sensitivity setting for map movement.
- Selecting a spidertron remote selection in the quickbar which is for a different planet than the current one will center on the planet.

### Bugfixes

- Fixed that selecting a quality comparison option when "any" quality was set did not work. ( more )
- Fixed it was possible to set inconsistent signals on a control behavior by using parametrized blueprint with a shared parameter. ( more )
- Fixed a crash when rotating entity that is destroyed inside of event handler.
- Fixed blueprint description label not showing in list view. ( more )
- Fixed fulgoran attractor marking for deconstruction. ( more )
- Fixed beacons deactivated by script loaded from a 1.1.x save file were not migrated properly. ( more )
- Fixed a crash when using modded equipment without items to build it in ghost form. ( more )
- Fixed inserter would not keep stack size signal through a blueprint string. ( more )
- Fixed that you could pick up items off the ground while flying in a rocket. ( more )
- Fixed inserter would not reevaluate enable condition when it was changed by blueprint parameters. ( more )
- Fixed orbital logistics tips&tricks script crash due to space platform hub gui having different layout. ( more )
- Fixed that recipe fuel tooltips did not respect the show-all-unlocked-items interface setting. ( more )
- Fixed asteroid collector set filters from circuit network would set wrong filters for one tick after items were removed and read content is active. ( more )
- Fixed a crash when lua orders entity deconstruction specifying undo item but not specifying a player. ( more )
- Fixed that two damaged construction robots trying to repair each other could get stuck in an infinite loop of trying to hug each other and overshooting. ( more )
- Fixed a crash when running under the Steam Runtime Environment on Linux in certain situations. ( more )
- Fixed quality increase of self-recycling recipes being reported incorrectly in production statistics. ( more )
- Improved super force building logic of belt related blueprints over existing belts. ( more )

## 2.0.19

Date: 15.11.2024

### Minor Features

- Added debug option 'always-show-lightning-protection'.

### Changes

- Changed captive biter spawner to inherit quality from the wild spawner instead of the capture robot. ( more )
- Spidertron selections saved into the quickbar will be darkened with a planet icon in the top when the selection leads to a different planet than the current one.

### Bugfixes

- Fixed mining fulgoran lightning rods would not show yield. ( more )
- Fixed blueprint external wires were not added when pasting blueprint over existing entities. ( more )
- Electric weapons damage infinite tiers start more expensive to naturally progress from the non-infinite tiers correctly. ( more )
- Fixed wrong locomotive could turn lights on when train has locomotives both ways and goes back. ( more )
- Fixed a crash when trying to cycle qualities in 2.0 base game. ( more )
- Fixed foundry was not able to reach declared speed of crafting holmium plates due to input fluid shortage. ( more )
- Fixed buildings constructed on space platform by space platform were not tracked by build statistics, research triggers nor achievements.
- Fixed pasting blueprint with constant combinator over constant combinator could create unnecesary copy settings undo actions. ( more )
- Fixed upgrading storage chests would not preserve storage filter. ( more )
- Fixed a crash when generating multiplayer maps while background simulations were enabled. ( more )
- Fixed selection tools and some spawnable items did not work correctly when chosen via remote ghost cursor gui. ( more )
- Fixed a crash when an item request proxy wanted to dispatch robots to insert items into invalid slots. ( more )
- Fixed tip of the rocket poking through air objects. ( more )
- Fixed rail planner in ghost mode would ignore existing ghost ramps and ghost supports proposing new supports that were not needed. ( more )

## 2.0.18

Date: 14.11.2024

### Changes

- Allowed negative multiplier of logistic (and constant combinator) groups. ( more )
- Updated shortcut icons and increased their size to 56px.
- Container sizes increase with quality.
- Reviving container ghosts no longer puts colliding items on the ground into the resulting container.
- Loading game for hosting now automatically offers the dialog whether the mods should be synced before continuing (as with normal game load).
- Bulk inserter doesn't default upgrade to Stack inserter as they are not functionally interchangeable. ( more )
- Demolisher health bars will always be visible for at least 1 tick after they take any damage, even if they fully regenerate the damage in the same tick.
- Default quality cycling shortcut simplified to alt+scroll.

### Bugfixes

- Fixed confusing blueprint parameter context tooltip for filter of storage chest. ( more )
- Fixed music not switching correctly when restarting level. ( more )
- Fixed that the production GUIs showed the graphs in 'All' when opened with saved precision. ( more )
- Fixed that the "load save after sync" checkbox did not work in the sync mods with save GUI. ( more )
- Fixed removing heatpipes from a blueprint could leave them visually connected to their neighbours. ( more )
- Fixed 'Dropping to planet' button being too wide and pushing the 'Cancel' button off the screen. ( more )
- Fixed 'Always show' label not being accurate to the behavior of only showing in "Alt-mode". ( more )
- Fixed 'Parameterised build' GUI clipping off screen when too long. ( more )
- Fixed robots failing to upgrade a container if it was the only source of the requested item. ( more )
- Fixed that reusing the same sprite for multiple effects crashed instead of showing the error message and an option to disable problematic mods. ( more )
- Fixed 'Galaxy of Fame' upload GUI clipping off screen on smaller resolutions. ( more )
- Fixed vertical alignment of Current Research icon. ( more )
- Fixed asteroid spawning being significantly reduced when a platform moved with paused thrust. ( more )
- Fixed that fluids could get erased during migrations. ( more )
- Fixed a crash when removing a roboport while robots in that network are deactivated by script. ( more )
- Fixed that choose-elem-button wouldn't show the select list GUI if clicked with an item that didn't pass the filters. ( more )
- Fixed that syncing mod while trying to host game didn't allow to continue the process after reloading the game. ( more )
- Fixed chunks not being covered by fog of war when remote-viewing an unvisited surface. ( more )
- Fixed all/any/individual request satisfied wait conditions ignoring maximum count of space platform requests. ( more )
- Fixed offshorepump tooltip flickering too much when pumping at full capacity. ( more )
- Disabled "Drive Remotely" button on driveable vehicles ghosts' GUIs. ( more )
- Fixed Cargo Landing Pad and Space Platform Hub GUI being clipped off screen on smaller resolutions. ( more )
- Fixed platform deletion and undelete platform buttons being clipped off the surface list. ( more )
- Fixed that tanks didn't preserve all of their settings when mined and rebuilt. ( more )
- Fixed that rebuilt tanks didn't have their inventory size bonus from equipment. ( more )
- Fixed script error in PvP when setting starting item count to 0. ( more )
- Fixed spectator players of dead teams showing on the map in PvP. ( more )
- Fixed that inserters could get stuck with specific combinations of spoilage and disabled by control behavior. ( more )
- Fixed that some pop-up GUIs would get closed when robots built the entity while the ghost GUI was open. ( more )
- Fixed that robots performing module upgrades left some modules on ground when upgrading mixed modules to one type. ( more )
- Fixed that space platforms could unload cargo while waiting for departure. ( more )
- Fixed clouds and smoke were moving in exactly opposite direction. ( more )
- Fixed that spidertrons would severely confuse demolishers. Demolishers will now retaliate against spidertrons. ( more )
- Fixed the confirmation button behaving inconsistently in the remote view ghost picker menu. ( more )
- Fixed Agricultural tower sometimes showing wrong status if its growing plants were destroyed externally.
- Fixed a crash when exporting a blueprint with asteroid collectors which had gaps in the filters list. ( more )
- Fixed Being able to super-force entity through technology gui. ( more )
- Fixed spoilage was not considered as more spoiled than any spoilable items. ( more )
- Fixed that highlighted robots in the logistic networks chart view didn't smoothly follow robots. ( more )

### Modding

- Changed base/space-age tile collision mask definitions so that they don't share references to the same tables.
- Added ItemPrototype::spoil_level.

### Scripting

- Fixed/reworked how setting tiles behaves vis-à-vis (double)hidden tiles (concerns LuaSurface::set_tiles, editor and placing of non-mineable tiles in-game) ( more )
- Added LuaEquipment::inventory_bonus read.
- Added LuaEquipmentGrid::inventory_bonus and LuaEquipmentGrid::movement_bonus read.
- Added LuaEquipmentPrototype::get_inventory_bonus().
- Fixed that LuaEntity::get_priority_target() would give invalid results for empty filters.
- Extended LuaEntity::splitter_filter, splitter_input_priority and splitter_output_priority to also work with lane splitters.

## 2.0.17

Date: 12.11.2024

### Changes

- Gleba evolution is smoother and more gradual.
- Small stomper pentapod moves more slowly (also decreases stomp DPS).
- Stomper pentapod vision range is reduced from 40 to 30.
- Medium and big wriggler pentapod health is increased.
- Streamlined quality selector to use separate buttons for each quality instead of a drop-down.
- Changed crafting machines to reset quality of the in-progress result when module effects change. ( more )
- Added inserter stack size override to be parametrised by blueprint. ( more )
- Added Vulcanus 8 music track.

### Bugfixes

- Fixed that the game would get into an invalid state if the backers.json file was manually edited in some ways. ( more )
- Fixed a crash with lightning when setting time to damage to 0 through mods. ( more )
- Fixed fast replacing a radar could cause radar network to break.
- Fixed that blueprint export/import to string did not work correctly for turret priorities with gaps. ( more )
- Fixed that some asteroids could appear stationary if their velocity was lower than minimum position increment. ( more )
- Fixed space platform autosaves being overwritten mid-journey when the platform changed its state. ( more )
- Fixed market offer not working with nothing modifier. ( more )
- Fixed rocket silo would start closing doors when next rocket was finished while lights blinking animation was already started. ( more )
- Fixed LuaTechnologyPrototype::essential returning incorrect value. ( more )
- Fixed that strafer pentapods couldn't attack a retreating target it was behind even when faster than the target. Attack range is increased but strafe distance is unchanged.
- Fixed more issues with blueprint reassigning changing the position of the entities or snapping values of the blueprint. ( more )
- Fixed wrap-around of asteroid rotation animation was not seamless. ( more )
- Fixed that Galaxy of Fame upload didn't clean its files. ( more )
- Fixed more crashes related to using formatting strings with floating-point numbers on Intel Macs running Sonoma.
- Fixed cancelling deconstruction via deconstruction player was not showing counts for canceled deconstructions. ( more )
- Fixed that galaxy of fame upload din't clean its files. ( more )
- Fixed that setting negative value in constant combinator create 2 entries for the number in the blueprint parametrisation, one with underflown value.
- Fixed that it wasn't possible to input negative numbers in blueprint parametrisation. ( more )
- Fixed offshore pump would present itself as water well pump even when it was not pumping water. ( more )
- Fixed crash when trying to search invalid UTF-8 string ( more )
- Fixed that hidden space locations would will show in descriptions. ( more )
- Fixed that fast-transferring modules would put them into the rocket silo rocket inventory. ( more )
- Fixed that switching surfaces while a platform hub GUI was open would leave the GUI open in some cases where it wasn't supposed to. ( more )
- Fixed that you could remove your armor and spill items through the quickbar. ( more )
- Fixed that modded attack_reaction could crash the game. ( more )
- Fixed a crash when using surface.clear() on vulcanus. ( more )
- Fixed that orbital request select window wasn't showing proper import from after chaning the group unless the whole window was closed and opened again. ( more )
- Fixed double set of parameters in factoriopedia. ( more )
- Fixed stack inserter would not wait for more items if spoil priority was set. ( more )
- Fixed loaders would freeze or unfreeze partially. ( more )
- Fixed arithmetic combinator gui would allow changing not relevant checkboxes in some cases. ( more )
- Fixed surface editor would not set surface properties when creating surfaces planet-alike. ( more )
- Fixed rail planner would remain active when changing surfaces. ( more )
- Fixed a crash when reviving power switch with multiple ghost copper cables connected to the same side. ( more )
- Fixed space platform hub gui would reset position when changing auto requests checkbox. ( more )
- Fixed that assembler with set recipe enabled would not keep direction if current recipe did not require direction. ( more )
- Fixed robot repair job assignmend ignoring repair packs stored in roboports when finding the closest source. ( more )
- Allowed increasing of request count by blueprint parameters to push the max request count. ( more )
- Fixed that corpses would block tiles from being deconstructed. ( more )
- Fixed that restarting to reload mods on macOS would leave behind unresponsive zombie windows. ( more )

### Modding

- Input loader supports filters.

### Scripting

- Added LuaControl::set_driving() ( more )

## 2.0.16

Date: 08.11.2024

### Minor Features

- Search is now case and accent insensitive for all official languages.

### Changes

- Changed tree seed default import location to Nauvis. ( more )
- Fluid mixing will prefer the fluid with more volume and discard the other.
- Updated SDL to version 2.30.9.

### Bugfixes

- Fixed a freeze when setting logistic/construction robots to active=false through script. ( more )
- Fixed that LuaEntity::vehicle did not work correctly for characters controlled by a player. ( more )
- Fixed rendering of glowing items on belts would not be batched properly. ( more )
- Fixed a crash when reading LuaEntity::robot_order_queue. ( more )
- Fixed that the permissions GUI could not be opened in multiplayer as not-the-host. ( more )
- Fixed some decorative entities like craters or chimneys not having a tall enough drawing box. ( more )
- Fixed that factoriopedia_description would not be used if the prototype didn't also have a regular description. ( more )
- Fixed a crash when space platforms are destroyed while specific entity GUIs are open. ( more )
- Fixed undoing a copy-settings could void assembler contents. ( more )
- Fixed tips not appearing in tutorials. ( more )
- Fixed wrong times symbol in a logistic request tooltip. ( more )
- Fixed that using pipette on GUI items did not consistently copy the quality. ( more )
- Fixed that using pipette on tile items in GUI always selected normal quality. ( more )
- Fixed that using pipette on entity items in GUI could select the wrong item if multiple items can build the same entity.
- Fixed visualisation issue around cursor attractor range enveloping an existing attractor ( more )
- Fixed tile replacement logic ignoring tile ghosts covered by tile ghosts
- Fixed stations getting skipped when using the 'Destination full' condition for interrupts. ( more )
- Fixed UI jank that widgets would snap to be centered on the cursor when dragged.
- Fixed selections using deconstruction planners etc. not getting cancelled when leaving remote view. ( more )
- Fixed that changing viewed surface would not abort wire drag. ( more )
- Fixed non-chart sprites sometimes being drawn into chart. ( more )
- Fixed upgrading cargo bays with incoming pods would leave them permanently reserved. ( more )
- Fixed a crash when changing tiles causes entities to die. ( more )
- Fixed that a music track could play on a wrong surface. ( more )
- Fixed bloom lightmap for fog was being rendered also when fog effect was not used.
- Fixed super force overbuilding entity with settings sometimes behaving incorrectly if overbuilt entity was marked for upgrade.
- Fixed fluid overextent warning would sometimes show on entities that would not help overcome the overextent. ( more )
- Fixed cars not having lightning endangerement alerts despite being vulnerable to lightnings ( more )
- Fixed a performance issue in the manage-mods GUI. ( more )
- Fixed a memory corruption issue when changing a character's force from one that did not have logistics to one that did. ( more )
- Fixed the Trash unrequested checkbox in the character logistic GUI expanding the GUI size. ( more )
- Fixed that LuaEntity::mirroring write did not work for ghosts. ( more )
- Fixed sounds of items inserted by robots being too loud. ( more )
- Fixed the Trash unrequested checkbox showing in chests which have no trash slots. ( more )
- Fixed a crash when switching audio devices when there were none initially.
- Fixed pin text rich text icon quality punching through GUIs. ( more )
- Fixed that LuaSurface::find_tiles_filtered() did not work with rotated bounding boxes. ( more )
- Fixed interrupt GUI targets list being squashed too much with lots of interrupt conditions. ( more )
- Fixed that heating towers couldn't consume items fast enough if the fuel value was low. ( more )
- Fixed a consistency issue when deconstructing the last roboport in a logistic network. ( more )
- Fixed fog was clipping through agricultural tower. ( more )
- Fixed that killed and rebuilt power switches would get stuck in the inoperable state. ( more )
- Fixed a performance issue with large inventory GUIs. ( more )
- Fixed that infinity chests didn't show hidden items. ( more )
- Fixed that programmable speaker alert text wasn't included in the blueprint parametrisation logic. ( more )
- Fixed that science pack descriptions in Factoriopedia didn't make any sense. ( more )
- Fixed muzzle flash of artillery wagon was offset when the wagon was on elevated rails. ( more )
- Fixed artillery wagon gun barrel was rendered under elevated rail fence.
- Fixed drawing linked fluidbox connections when they should be hidden.
- Fixed that manually-built trains were switched to automatic mode when a ghost attached to them was revived. ( more )
- Fixed that blueprints could be grabbed while having a ghost item in the cursor. ( more )
- Fixed an assembling machine could be set a fluid-only recipe with quality when set by circuit network. ( more )
- Fixed maximum request limit (autotrash threshold) not accepting math expressions. ( more )
- Fixed equipment requests not being cleared when the grid didn't have enough space. ( more )
- Fixed that asteroid collector control behavior "set filter" would affect status light while wire was disconnected. ( more )
- Fixed turbo splitter was missing description. ( more )

### Scripting

- Added hide_clouds and hide_fog parameters to LuaGameScript::take_screenshot. ( more )
- Added LuaEntity::get_logistic_sections(). Added LuaLogisticSections.

## 2.0.15

Date: 05.11.2024

### Minor Features

- Cars and tanks will auto-refuel. ( more )
- Relation between offshore pump and fluid tiles added to Factoriopedia.
- Statistic GUI precision is preserved across instances.
- Space platforms can be built with quality starter packs. ( more )

### Changes

- Increased spidertron walking sound volume.
- Using the "craft all" hotkey on free recipes queues 1 stack of the results. ( more )
- Changed the simulated mouse cursor appearance to match the system default on macOS.
- Added pollution value to heating tower.
- Show recycler output arrow in "Alt-mode". ( more )
- Display panels set to "Show in chart" with no icon now hide the default icon until hovered. ( more )
- Removed support for 8 bit audio depth.
- Added tooltip to "Spoiled priority" inserter setting to clarify behavior and limitations.

### Bugfixes

- Fixed IME Pad input not working on screens with visible simulations. ( more )
- Fixed that the browse-games GUI header labels were not clickable. ( more )
- Fixed that kills with chained effects did not count towards statistics or achievements. ( more )
- Extended the mute-programmable-speaker command to apply to sounds with both global and surface playback modes. ( more )
- Fixed a crash when a player got desynced from a multiplayer game while the Technology GUI was open.
- Fixed a crash when rendering display panel text after loading a save file. ( more )
- Fixed a crash when clicking on an orbital request slot with an invalid ghost item in cursor. ( more )
- Fixed a crash when rendering certain blueprints with pipe-to-grounds which visually connected to neighbours outside of the blueprint. ( more )
- Fixed cargo pod with satellite not despawning after launching to orbit. ( more )
- Fixed a crash when teleporting a crafting machine ghost with fluid connections. ( more )
- Fixed that space platforms would try to build/upgrade/deconstruct/repair other forces entities. ( more )
- Fixed that the production GUI title wouldn't update when viewing different planets. ( more )
- Fixed that starting territories on Vulcanus could be merged into one more frequently than expected. ( more )
- Fixed that platform requests satisfied wait conditions could be stuck when the platform had unfulfilled ghost item requests. ( more )
- Fixed that space platforms didn't fulfill remote item delivery requests if the target slot was already occupied with the same item. ( more )
- Fixed that negative movement speed stickers could cause player movement to get stuck in a near infinite loop. ( more )
- Fixed a crash when drawing spidertrons on the map if selected_minimap_representation wasn't defined. ( more )
- Fixed shattered planet achievements being incorrectly awarded when traveling backwards in a paused platform. ( more )
- Fixed that remote view while in the map editor did not ignore fog of war. ( more )
- Fixed a crash when using LuaEquipmentGrid::take_all() when the grid contained ghosts. ( more )
- Fixed that belt immunity equipment didn't use less power at higher qualities like it said it did. ( more )
- Fixed that several specific-item producing entities could not be specifically filtered in the deconstruction planner. ( https://forums.factorio.com/118089 , https://forums.factorio.com/118297 , https://forums.factorio.com/116477 )
- Fixed LuaEntity::max_health was returning incorrect values for entities with health affected by evolution factor. ( more )
- Fixed fast replacing loaders would not preserve filter mode. ( more )
- Fixed that heating towers and nuclear reactors were fast-replaceable with each other. ( more )
- Fixed rail curves making a blueprint's default snapping grid unnecessarily large. ( more )
- Removed long delay at start when no audio devices are found. ( more )
- Fixed that result_is_always_fresh was ignored for hand crafting. ( more )
- Maybe fixed crashes related to using formatting strings with floating-point numbers on Intel Macs running Sonoma.
- Fixed that removing cargo bays while the inventory limit was in place did not work correctly. ( more )
- Fixed that inserters could get stuck loading cargo wagons in some cases. ( more )
- Fixed spoiled items in filtered slots of inventory would not get ejected to unfiltered slots when sorting inventory. ( more )
- Fixed a crash when removing equipment that was in equipment ghosts. ( more )
- Fixed a crash when migrating a fluid box from one that joins with a fluid segment to one that does not.
- Fixed endlessly pending asteroid collector calculation when navigation was not changed ( more )
- Fixed modded spider vehicles being selectable with Spidertron Remote when selectable_in_game property was false.
- Fixed copying settings from inserter to assembler could raise error sound even when circuit conditions were changed. ( more )
- Fixed that some color signals were not given lamp color. ( more )
- Fixed that recipe parameter would not allow productivity effect. ( more )
- Fixed that new filters set by LuaLogisticSection::filters would not propagate to other sections under the same group. ( more )
- Fixed that sync-mods-with-save did not show load-save as an option. ( more )
- Fixed captive biter spawner was able to connect to logistic network. ( more )
- Fixed that clearing assembler recipe would not clear invalid item requests. ( more )
- Fixed a crash when trying to drag temporary schedule record for a constantly retriggering interrupt. ( more )
- Fixed asteroid collector description not listing minimum energy consumption. ( more )
- Fixed recycling time of recipes with default crafting time was twice as long. ( more )
- Fixed space platforms and cargo landing pads losing items when merging forces. ( more )
- Fixed that item pickup requests weren't invalidated after making an automatic trash request. ( more )
- Fixed environmental sounds needlessly reloading when entering/leaving remote view. ( more )
- Fixed rough ice thawing to volcanic tiles. ( more )

### Modding

- Changed territory noise expressions coordinate system from chunk-based to tile-based.
- Added option to surface.pollute() for recording the pollution change in statistics.
- Fixed on_entity_damaged.source not behaving according to the 2.0 specification.

### Scripting

- Added connection_type and linked_connection_id to LuaFluidboxPrototype::pipe_connections.

## 2.0.14

Date: 01.11.2024

### Changes

- Changed self-recycling recipe statistics to be ignored in production graph.
- Changed sprites with scale between 0.5 and 1 (exclusive) to apply downscaling to low resolution (affects base game biter sprites).
- Changed cargo landing pad mining time to 1.
- Moved the mods GUI search to be with the content it is searching.
- Added linear interpolation method (used by default now) for audio resampling when playback speed is changed. ( more )
- Added an option to disable animated ghosts to aid performance on integrated GPUs. ( more )
- Added a confirmation box when deleting space platforms.

### Bugfixes

- Fixed that having multiple key bindings could cause some keys to get stuck. ( more )
- Fixed that it wasn't possible to parametrised item filter to any quality. ( more )
- Fixed a crash when killing segmented units attached to a segmented controller. ( more )
- Fixed that tank logistic trash slots did not work correctly when using roboports in the tank. ( more )
- Fixed that shortcuts marked as not toggleable still allowed being toggled. ( more )
- Fixed that lua shortcuts ignored unavailable_until_unlocked. ( more )
- Fixed that teleporting certain entities would delete their fluid contents. ( more )
- Fixed that the reactor GUI temperature would flicker when the temperature was < 100 degrees. ( more )
- Fixed that some errors related to prototypes would report coming from the wrong prototype. ( more )
- Fixed that copying spider vehicle settings between spiders of different quality did not work correctly. ( more )
- Fixed that pumps would pull fluid from internal machine buffers instead of the connected fluid segment. ( more )
- Fixed that mods were able to create item stacks without quality which crashed the game. ( more )
- Fixed rocket silo requesting more items even if another rocket wasn't ready yet. ( more )
- Fixed incorrect lightning protection visualisation in some cases where shorter range attractor is close to longer ranged one ( more )
- Fixed vehicle sounds not playing in some menu simulations. ( more )
- Fixed a crash when reading repair state of a character not assigned to a player. ( more )
- Fixed asteroid collector navigation not generating in time when a straight platform edge is aligned with chunk border, which caused a crash. ( more )
- Fixed consistency issue when removing a turret that was connected to logistic network. ( more )
- Fixed a crash when prototype data changes and roboports are requesting specific robots. ( more )
- Fixed combinators could get stuck after cancelling deconstruction order. ( more )
- Fixed a crash when fast-replacing not-a-heat-interface entity with a heat interface. ( more )
- Fixed a crash when trying to recycle blueprint books with contents. ( more )
- Fixed being able to enter a frozen rocket.
- Fixed flames not updating on a frozen or deconstructed rocket silo.
- Fixed a crash when viewing players in the players GUI when they disconnect from the server.
- Fixed a crash when copy-pasting settings from an assembling machine to a logistic chest that did not support requests. ( more )
- Fixed that the space map GUI would not show until you had visited at least 1 other planet. ( more )
- Fixed loader energy source buffer size computation. ( more )
- Fixed that tesla turret and tesla gun chain lightning sometimes arced to friendly entities. ( more )
- Fixed that character_mining_speed_modifier was not handled in latency state.
- Fixed factoriopedia for space connections would highlight wrong graph series when hovering over slots of spawned asteroids. ( more )
- Fixed pinning other players did not work correctly. ( more )
- Fixed demolishers getting disturbed by vehicles and other non-building entities. ( more )
- Fixed "Get off my lawn" achievement not being awarded when building close to a demolisher. ( more )
- Fixed a crash when copy-pasting from cars with equipment grids to ghost-cars without equipment grids. ( more )
- Fixed a crash when showing logistic request tooltip immediately after joining a multiplayer game. ( more )
- Reverted a fix for train interrupts not being checked when passing a station without conditions ( more )because it crashed the game. ( more )

### Modding

- Combined four ghost tint definitions in UtilityConstants into UtilityConstants::ghost_shader_tint and added UtilityConstants::ghost_shaderless_tint.
- Added LoaderPrototype::per_lane_filters.

### Scripting

- Added LuaEntity::loader_filter_mode (read/write).

## 2.0.13

Date: 30.10.2024

### Minor Features

- Offshore pump speed increases with quality.

### Changes

- Curved rails cost 3 rail items to build.

### Bugfixes

- Fixed Remote View sometimes flickering to the wrong surface when using Next Surface/Previous Surface hotkeys.
- Fixed that the Surface List would react to the Home and End keys after it was clicked ( more )
- Improved diagonal character movement which should help slip between things easier. ( more )
- Fixed a crash when upgrading the inner entity of a ghost while the GUI was open. ( more )
- Fixed that joining LAN games without a username set would allow any characters for the username. ( more )
- Fixed that request from buffer chests was not preserved when changing the force of an entity. ( more )
- Fixed that flamethrower turret could be manually built to mix fluids. ( more )
- Fixed that half diagonal rails would cost only 1 rail item. ( more )
- Fixed pipe sound starting and stopping too abruptly. ( more )
- Fixed turret behaviour when it has more than 4 directions and the collision box is not affected by rotation.
- Fixed a crash when switching preferred audio output device while a variable music track is being generated. ( more )
- Fixed an issue with platform construction requests when copying settings onto the hub. ( more )
- Fixed a crash when saving related to construction robots and their work targets moving. ( more )
- Fixed that Continue host option didn't offer mod sync to the save to be hosted. ( more )
- Fixed Space platform requests would always be checked in the same order, leading to some requests being ignored. ( more )
- Fixed base game space science getting throughput limited due to limited hatches. ( more )
- Fixed defines.space_platform_state was missing value for paused. ( more )
- Fixed solar panel output multiplier flickering in tooltip. ( more )
- Fixed that deconstruction of a chest with full trash slots didn't dispatch enough robots. ( more )
- Fixed a crash caused by a player sending a space platform which was waiting for departure (not enough thrust) to a location which wasn't unlocked yet. ( more )
- Fixed that train interrupts were not checked when passing station without conditions. ( more )
- Fixed that the browse-games GUI 'dedicated server' and 'favorite' settings would get confused with each other. ( more )
- Fixed that capture-spawner research trigger reported incorrect type. ( more )
- Fixed production and electricity statistics would use wrong locale for ranges exceeding 99 hours. ( more )
- Fixed that exoskeleton legs would incorrectly consume more energy at higher qualities. ( more )
- Fixed that logistic filter upper count wasn't considered by the blueprint parametrisation. ( more )
- Fixed technology trigger info showing outside the tooltip. ( more )
- Fixed that Lua require didn't accept symbolic links. ( more )
- Fixed that migrating logistic cell charger count would corrupt loading. ( more )
- Fixed that cars/tanks would not preserve their settings correctly in blueprint strings. ( more )
- Fixed that fluids would be duplicated when fast-replacing machines. ( more )
- Fixed that the window could get stuck in an infinite loop of toggling fullscreen when changing displays on Linux. ( more )
- Fixed that the "make it better" achievement only worked with quality level 1 modules. ( more )
- Fixed asteroid collectors sometimes not generating navmesh properly around chunk borders and related instabilities. ( https://forums.factorio.com/117737 , https://forums.factorio.com/117276 )
- Fixed that opened console was rendered into the galaxy of fame output. ( more )
- Fixed that the focus search hotkey would not work in choose elem button GUIs if a mod GUI was marked as opened. ( more )
- Fixed that Intel Macs running macOS Big Sur or later logged the wrong version number.
- Fixed issue where entities at position where entities at the point where lightning attractor collection ranges touch were incorrectly considered endangered by lightning ( more )
- Fixed blue line at the edge of some sprites by clearing sprite atlas background to clear color. ( more )
- Fixed some cases of upgradeable overbuilds not upgrading ( more )
- Fixed that using Nauvis map gen settings for other planets made them generate only grass. ( more )
- Fixed that the select-recipe GUI did not work correctly if you re-bound the crafting hotkeys. ( more )
- Fixed a crash when editing a pin while the entity was referencing was removed. ( more )
- Fixed selector combinator could sometimes fail to select correct signal. ( https://forums.factorio.com/118412 , https://forums.factorio.com/116548 )
- Fixed that some technology triggers required crafting specific quality items. ( more )
- Fixed constant combinator activity lamp not updating state in certain cases. ( more )
- Fixed that custom sprite button's caption would be drawn under the sprite. ( more )
- Possibly fixed a crash on Intel Macs related to printing floats with 0 precision. ( more )
- Fixed layered icons in rich text were not scaled and rotated properly. ( more )
- Fixed that moisture and terrain type weren't migrated properly for 1.1 saves resulting in hard chunk edges.
- Fixed occasional crash occurring when super force deconstructing with filtered tiles only planner includes double tile ghosts and an entity ghost on one tile ( more )
- Fixed a crash when a space platform hub with 'Any request zero' wait condition was destroyed. ( more )
- Fixed that custom gui elem_tooltip did not work for some new types. ( more )
- Fixed big electric poles were not colliding with asteroid collectors. ( more )
- Fixed that LuaGameScript::show_message_dialog() could use the wrong player and freeze the game. ( more )

### Scripting

- Added LuaSpacePlatform::name write.
- Added player_won to the on_pre_scenario_finished event.
- LuaControl uses physical controller for item manipulations (LuaControl::insert, has_items_inside, get_item_count, remove_item, clear_items_inside)
- Added LuaPlayer::physical_controller_type read.
- Added LuaQualityPrototype::color read.

### Sounds

- Fulgora lightning sound remixed lower with volume variations.
- Fixed some explosions that were using the wrong size of explosion sound.
- Numerous sound mixes including new plant mining sounds mixed lower.
- Various menu simulation mixes improved.

## 2.0.12

Date: 28.10.2024

### Bugfixes

- Fixed rocket silos requesting more items than necessary. ( more )
- Fixed a crash when reading owner_location on simple item stacks. ( more )
- Fixed mini-tutorial scripts crashing or not granting items if player switched to remote view.
- Fixed that LuaControl::opened write did not work for several GUI types. ( more )
- Fixed that elevated rail entities would still work without owning space-age. ( more )
- Fixed that the admin "other player" GUI would open the other player's remote controller invenory instead of physical inventory. ( more )
- Fixed a crash related to quickbar interaction with any-quality spawnable items. ( more )
- Fixed a crash when building (faulty) blueprint with two hazard concrete tiles in one space ( https://forums.factorio.com/117108 and https://forums.factorio.com/117071 )
- Fixed game state GUIs being automatically closed when the game was paused. ( more )
- Fixed several possible errors related to smart belt building. ( https://forums.factorio.com/116660 , https://forums.factorio.com/117119 )
- Fixed that disconnecting and reconnecting while personal robots were working did not preserve their quality. ( more )
- Fixed that cargo pods dropped players to a random location which could make them stuck. ( https://forums.factorio.com/117461 and https://forums.factorio.com/117408 )
- Fixed that alert icons were rendered into the galaxy of fame.
- Fixed a desync related to space platform hubs reading content and repair packs merging due to inventory sorting.
- Fixed ribbon world preset having too many cliffs on Nauvis. ( more )
- Fixed that blueprint parametrisation value formula evaluation didn't work for negative numbers. ( more )
- Extended blueprint parametrisation to work on fluid recipe parameters.
- Fixed lua deconstruct_area crashing when deconstructing a ghost ( more )
- Fixed inserter status showing "Target full" when swinging towards a belt ( more )
- Fixed that drag building context was not carried properly between normal view and remote view. ( more )
- Fixed combat robots bobbing. ( more )
- Fixed a crash when defining a recipe that does not always produce an item. ( more )
- Fixed that filters of a ghost turret could get corrupted in latency when upgrading it with upgrade planner. ( more )
- Fixed that re-bound crafting keys did not work correctly. ( more )
- Fixed that chat icons didn't include layered icons. ( more )
- Fixed a crash when super-force-building electric poles in latency state. ( more )
- Fixed a debug visualization render crash when the given force no longer exists. ( more )
- Fixed visual noise caused by parameter recipes drawing as not researched. ( more )
- Fixed selector combinator's constant index was not covered by blueprint parameters. ( more )
- Fixed arithmetic combinator was not showing red and green inputs separately in tooltips. ( more )
- Fixed superforced overbuilding logistic and non-losistic chests did not transfer limits ( more )
- Fixed underground pipe in cursor would sometimes not rotate when rotation key pressed right after placement while playing in latency.
- Fixed loading save files with some entities on planets with lighting when those entities were removed.
- Fixed a crash in multiplayer if you were wearing armor and the force you were on was deleted.
- Fixed some of the quirks of drag building. Whenever there is nothing to build from in the cursor, the drag building logic is interrupted. ( more )
- Fixed that the mine-entity technology trigger did not work if the resource entity produced multiple or variable results. ( more )
- Fixed that asteroid collectors could get stuck if the inventory limiter was used. ( more )
- Fixed a missing value in the prototype explorer. ( more )
- Fixed that smoke-with-trigger could teleport to 0,0 on a map if it was previously following a specific entity. ( more )
- Fixed rail ramp health bar position. ( more )
- Fixed wait condition "station is full" and "station is not full" would report incorrect progress. ( more )
- Fixed crash related to blueprint parametrisation and drag building button being held and moved after the dialog appeared. ( more )
- Fixed lamp would keep using color when circuit wire was disconnected. ( more )
- Fixed copy settings undo could fail to restore control behavior settings if they were originally at default values. ( more )
- Fixed that the map editor couldn't set filters in some cases. ( more )
- Fixed that LuaRecord methods did not work correctly. ( more )
- Fixed crash when building parameterised blueprint with dependent ingridient used in another machine being a fluid. ( more )
- Fixed missing blueprint parametrisation logic for the loader. ( more )
- Fixed a crash when migrating blueprint library content in a save that had that blueprint GUI open. ( more )
- Fixed that items could be put into ghost inventories. ( more )
- Fixed playing too many sounds at once at the start of certain tips and tricks simulations. ( more )
- Fixed a crash when setting RoboportPrototype::charging_station_count_affected_by_quality to true. ( more )
- Fixed generic interrupt false positives with certain interrupt conditions. ( more )
- Fixed main-menu music mode not working correctly in-game. ( more )
- Fixed a crash when trying to open Technology GUI from Factoriopedia while the game was being saved. ( more )
- Fixed clipping that could occur in some variable music tracks. ( more )
- Fixed that set recipe on assembling machine circuit controls could buffer items indefinitely. ( more )
- Fixed inconsistency in belt power replace through corner when going backwards and forwards. ( more )
- Fixed a train consistency issue when interrupt triggers inside of another interrupt in certain cases. ( https://forums.factorio.com/116845 , https://forums.factorio.com/117585 , https://forums.factorio.com/117717 )
- Fixed space platform losing its paused state when it arrived to a planet drifting backwards. ( more )

### Modding

- Added LoaderPrototype::frozen_patch_in and frozen_patch_out.

## 2.0.11

Date: 25.10.2024

### Features

- Asteroid collector filters can be modified by blueprint parametrisation.
- Programmable speaker can be modified by blueprint parametrisation.
- When imported blueprint is placed, assembling machines will be configured with the recipe even when recipe is not yet researched.

### Changes

- Fulgora ruins now also drop iron sticks when mined so electric poles could be crafted without recyclers at the start.
- The "Custom minimum payload" slider for orbital logistics now offers more sensible values.
- Orbital logistics "Custom minimum payload" is now checked against largest possible payload before setting the filter.
- Cargo bays will show a warning icon when they are not connected to a Hub or Landing Pad.

### Optimizations

- Improved performance of technology GUI when viewing only essential technologies. ( more )

### Bugfixes

- Fixed a crash when construction robots attempt to deliver modules in the same tick the target entity is destroyed. ( more )
- Fixed that biter base menu simulation had more decoratives over the Wube logo than desired. ( more )
- Tips simulation fixed with minor changes to texts ( more more more )
- Fixed that the map editor couldn't change the spawn point of a force after it was set. ( more )
- Fixed that the game would hang when closing the load game menu if the number of mods in the mods directory was too large on Linux. ( more )
- Fixed incorrect pump speed reporting when pumping into a fluid wagon. ( more )
- Fixed that pumps could not pump into a fluid wagon at full speed. ( more )
- Fixed that inserters could get stuck if the crafting machine they're interacting with dies and is rebuilt. ( more )
- Fixed a performance issue with ghost building. ( more )
- Fixed achievement nucear-power to require building nuclear reactor. ( more )
- Fixed a possible exploit of using parametrised blueprint to set unlocked recipes in assemblers. ( more )
- Fixed that players in remote view were unable to open menu when the game was paused. ( more )
- Fixed turrets sometimes being marked for deconstruction and rebuild if trying to upgrade through overbuilding.
- Fixed position of car driven by local player would be delayed on minimap in multiplayer.
- Fixed a crash related to rocket silos when adding and removing mods. ( more )
- Fixed that zooming with buttons(keyboard or controller) would not zoom to pixel-perfect values.
- Fixed a crash when reading cursor record of a character not assigned to a player. ( more )
- Fixed that building with modded items did not work correctly in all cases. ( more )
- Fixed a crash when merging forces related to chart tags. ( more )
- Fixed that blueprinted containers would loose their settings when overbuilt over container without those settings ( more )
- Fixed a crash when setting roboport requests to a negative value. ( more )
- Fixed RecipePrototype::maximum_productivity was allowed to be negative. ( more )
- Fixed rail description would suggest toggle rail layer binding when elevated-rails mod was disabled. ( more )
- Fixed blueprints being able to produce two overlaying ghosts of tiles with the same placing item (like hazard-concrete-left/right)
- Fixed technology GUI not updating technology cost label if the technology didn't have any science packs. ( more )
- Fixed reading LuaTechnologyPrototype::research_trigger could throw an error. ( more )
- Fixed modules technology icon when quality mod is disabled. ( more )
- Fixed MapGeneratorGui would not enable reset to defaults button when changing technology price multiplier. ( more )
- Fixed PVP scenario not having starting area protection enabled when the last player of that force logged out. ( more )
- Fixed use-item-groups had no effects. ( more )
- Fixed a crash when trying to render a surface which doesn't exist in a simulation. ( more )
- Fixed crashes caused by calling missing library symbols on older macOS versions. ( more )

### Modding

- Added AssemblingMachinePrototype::disabled_when_recipe_not_researched.

### Scripting

- Added LuaEntity::insert_plan and LuaEntity::removal_plan read/write.
- Added removal_plan parameter to LuaSurface::create_entity for item request proxies.

## 2.0.10

Date: 23.10.2024

### Features

- Galaxy of fame. Offered when the game is finished. ( more )

### Changes

- Non-blocking saving setting is no longer synced over the Steam cloud.

### Minor Features

- Added flying text for more cases of unsuccessful resource mining.

### Bugfixes

- Fixed that blueprint book tooltips did not look correct when in the quickbar. ( more )
- Fixed that movement speed bonus equipment would show garbage values when low on energy. ( more )
- Fixed that some fluid-only recipes would allow quality modules. ( more )
- Fixed that the "kill with artillery" achievement did not work with artillery wagons. ( more )
- Fixed invalid package name in sprite path definition would result in OS error message dialog instead of loading into minimal mode. ( more )
- Fixed that continue host menu option didn't respect the port from the config. ( more )
- From now on, we wont save blueprint-storage to a file when it was not used yet. This might help preventing cloud storage file by a file representing empty blueprint storage. ( more )
- Fixed that the blueprint setup GUI would always confirm to discard changes even if nothing changed when the blueprint had a description. ( more )
- Leaked D3D device and swap chain in attempt to avoid AMD driver crash when closing the game. ( more )
- Fixed LogisticContainerControlBehavior exclusive mode could get out of sync from the ContainerControlBehavior it derives from. ( more )
- Fixed that the debug settings GUI could get stuck behind the normal game logic. ( more )
- Fixed that the elem_tooltip type of "signal" did not work correctly. ( more )
- Instead of aborting when SDL_DXGIGetOutputInfo call fails, the game will try to initialize D3D device using adapter 0. ( more )
- Fixed crashes when using LuaEntity fluid methods when the entity's fluidboxes were not part of a segment. ( more )
- Fixed that LuaEntity::insert_fluid would not work on the output FluidBoxes of a crafting machine.
- Fixed removal of transport belts under cursor which would be normally fast-replaeable while drag traversing underground gap by belt rebuilding. ( more )
- Fixed arithmetic combinator's first constant would not be proposed as parameter. ( more )
- Fixed that on_entity_logistic_slot_changed did not fire for constant combinators. ( more )
- Fixed a crash in the space platform hub GUI when the inventory size changes at the same time as the limit is changed. ( more )
- Fixed turbo underground belts simulation in factoriopedia. ( more )
- Fixed a crash when a segmented unit entity causes the entire segmented unit to die. ( more )
- Fixed a crash when a platform was traveling to the shattered planet using a temporary stop which expired. ( more )
- Fixed fluid conditions not showing fluid amounts. ( more )
- Fixed using a custom surface in PvP was preventing Space Age progression. ( more )
- Fixed a crash when switching preferred audio output device while a variable music track is playing. ( more )
- Fixed train stop GUI being too wide at some smaller resolutions. ( more )
- Fixed driven car being drawn on all surfaces in latency. ( more )
- Fixed dying enemy would not randomize direction of its dying animation.
- Fixed that failed achievement wasn't gettable again without restarting the game. ( more )
- Fixed a crash when defining planet prototypes that don't contain any resources. ( more )
- Fixed logistic section active state was not preserved in a blueprint string. ( more )
- Fixed a crash when showing some modded GUI tables. ( more )
- Fixed an issue where entity flagged as not mineable could be marked for deconstruction using undo.
- Fixed pumpjacks with low yield would show 0 output rate in the tooltip. ( more )
- Fixed Nauvis elevation dropdown missing in map generator GUI, causing incorrect previews from map exchange strings. ( more )
- Fixed that it wasn't possible to parametrise virtual signals and space locations contained in text. ( more )
- Fixed brightness and contrast sliders being reset to 0 when setting the text field to a negative value. ( more )
- Fixed that it wasn't possible to parametrise entities, virtual signals and space locations contained in text. ( more )

## 2.0.9

Date: 22.10.2024

### Changes

- Achievement logistic-network-embargo updated with different condition for base game and space age.

### Bugfixes

- Fixed a crash when viewing the production statistics GUI while switching surfaces. ( more )
- Fixed unstable global grid position when re-assigning blueprint. ( more )
- Fixed that individual segmented units parts were in the kill statistics.
- Fixed a crash when opening the technology GUI focused on disabled technology. ( more )
- Fixed migration of rails in blueprints in 1.1 version of blueprint library. ( more )
- Fixed a crash when trying to use unsupported audio depth. ( more )
- Fixed a crash when loading some blueprint library contents with mods changed. ( more )
- Fixed a crash when clicking "upgrades" in the wave defense scenario. ( more )
- Fixed Spidertrons receiving up to 8 times extra damage from explosives. ( more )
- Fixed that unpowered inserters could grab items.
- Fixed that some GUIs could be opened behind the technology GUI. ( more )
- Fixed crash in multiplayer when mining modded tree with less stump variants than alive tree variants.
- Fixed it was not possible to open loader gui for input loader. ( more )
- Fixed crash in mod manager in minimal mode when some text used space-age icon rich text tag.
- Fixed that changing surfaces with ghost equipment would not correctly request robots to deliver the equipment. ( more )
- Fixed build sound of huge ghost entities not being ghostly enough. ( more )
- Fixed a crash when item entity marked to be deconstructed is cancel deconstructed while being over belt. ( more )
- Fixed that the runtime server config GUI did not fit on some screen sizes. ( more )
- Fixed GUI effects volume set to zero not being applied on start if background simulations were turned off. ( more )
- Fixed a crash when setting cursor_ghost of a character not assigned to a player. ( more )
- Fixed a crash when reading opened GUIs of a character not assigned to a player. ( more )
- Fixed PvP Scenario unlocking all the trigger technologies. ( more )
- Fixed a crash when changing the force of cargo landing pads.
- Fixed tools items and ammo items could be refilled during cursor split interaction. ( more )
- Fixed that it was not possible to mark legacy rails for deconstruction using deconstruction planner configured for straight-rail. ( more )
- Fixed that the Fulgora starting island could have no breaks in the cliffs. ( more )
- Fixed that deconstruction planner would treat entities with deconstruction alternative as being normal quality.
- Fixed crash when running out of disk space when saving preview for a save file.
- Fixed that passive provider and active provider logistic points could have sections added through the Lua API. ( more )
- Fixed that space platform schedule changes didn't update last user of the space platform hub. ( more )
- Fixed a crash when enabling snap-to-grid when a blueprint had no contents. ( more )
- Fixed that filter inserter was visible in technology icon for fast inserters.
- Fixed that a buffered rocket would briefly render lights south of the rocket silo. ( more )
- Fixed commas and quality icons not allowed in save file names. ( more )
- Fixed crashes when viewing alerts for entities that then die. ( more )
- Fixed incorrect surface condition of a space platform hub. ( more )

## 2.0.8

Date: 21.10.2024

### Bugfixes

- Fixed a crash when changing decider combinator conditions or outputs in latency in some cases.
- Fixed a crash when sending a platform with no thrust to a planet and then removing the stop. ( more )
- Fixed a crash when robots try to station in a full roboport because their stack size changed.
- Fixed a crash in path finder when migrating 1.0 save files to 2.0.
- Fixed orbital drop slots not counting towards Item count wait condition.
- Fixed space platforms not respecting peaceful and no enemy modes.
- Fixed a crash when downloading multiple mods fails.
- Fixed a crash when clicking "play" while the map preview was running. ( more )
- Fixed a crash when drawing a spider leg with length 0. ( more )
- Fixed error in loading 1.1 version of blueprint library would prevent starting new map or loading a save. ( more )
- Fixed crashes around the Explore Mods GUI with intermittent network connectivity.
- Fixed a crash when viewing a single-product recipe with no main product in Factoriopedia.
- Fixed a crash when pathfinding with a rotated bounding box. ( more )

## 2.0.7

Date: 21.10.2024

### Major Features

- Added space platforms, which can request items to be delivered by rockets and used to deliver cargo between planets. ( Friday Facts #381 )
- Added new planet Vulcanus, a volcanic planet with new resources, structures, items, recipes and technologies focussed on metallurgy. ( Friday Facts #386 , Friday Facts #387 )
- Added new planet Gleba, a swampy planet with new resources, structures, items, recipes and technologies focussed on agriculture. ( Friday Facts #413 , Friday Facts #414 )
- Added new planet Fulgora, a stormy desert planet with new resources, structures, items, recipes and technologies focussed on elecromagnetism. ( Friday Facts #398 , Friday Facts #399 )
- Added new planet Aquilo, a freezing planet with new resources, structures, items, recipes and technologies focussed on cryogenics.
- Introduced quality, which is additional property of item, entities and equipment. ( Friday Facts #375 ) Most entities, equipment, modules and ammo have various kind of bonuses with higher quality.
- Added rail ramps, rail supports and elevated rails to build bridges. ( Friday Facts #378 )
- Added stack inserters (previous stack inserters are called bulk inserters now) which can load transport belts with layered stacks of items. ( Friday Facts #393 )
- New rail shapes, rail curves, 22.5 degree tracks.
- Added Train interrupts ( Friday Facts #389 , Friday Facts #395 ) Trains can have number of interrupts, each interrupt has conditions and set of stops. Whenever is the train leaving a station, the first interrupt with fulfilled condition is activated, which adds its stations as temporary items into the schedule.
- Added Train groups. ( Friday Facts #389 ) Train name is editable and trains with the same name are considered to be in the same group. Editing schedule of a train automatically updates schedules of all the trains in the same group.
- Added Logistic groups. ( Friday Facts #382 ) Logistic group is editable for logistic points (Requester chest, Roboport, Character, Spidertron, etc.). Editing the requests of a logistic point automatically updates requests of all the points in the same group.
- Added Factoriopedia. ( Friday Facts #397 ) It provides detailed information about different kind of objects. Alt clicking any relevant gui element or game entity opens the related page.
- Forced building will now automatically adds missing landfill or other other tiles based on context.
- Added super forced building mode. Ctrl + Shift + Build marks for deconstruction player's colliding entities and replaces ghosts and tiles. ( Friday Facts #383 )
- Added search to the remote view. It allows to do surface wide search for recipe production, resources and train stations and map tags. ( Friday Facts #400 )
- Blueprint parametrisation. Allows to make more generic bluprints, which are configured upon building. ( Friday Facts #392 )

### Features

- Rail planner is usable in the map (remote view). ( Friday Facts #403 )
- Added smart dragging of underground belts and pipes.
- Added a toggle to show pipelines on the map.
- Added the option to pin positions, entities, alerts or search results, and keep track of their location. ( Friday Facts #400 )
- Entity ghosts are now buildable on water if the landfill ghosts are already there.
- Added a third graph to the electric network overview to track the charges of accumulators over time. ( Friday Facts #408 )
- Added a new alert for construction and logistic robots that can't find free space in a roboport.
- Added a new alert for trains failing to pathfind to their target. ( Friday Facts #395 )
- Added a new alert for turrets running out of ammunition. It only sounds once right when the ammo is used up.
- Added fuel condition to the train schedule.
- Added condition to the train schedule to check whether a specific station is full or not.
- Added an option for a locomotive to update its color automatically based on the color of the target train stop. ( Friday Facts #389 )
- Smarter worker robot scheduling. Worker robots have task queue now which allows the planner to choose the robot that will be able to get to the destination fastest, even if it is doing something else at the moment.
- Robot requests in roboports.
- Added Flipping as a primary action to flip entities horizontally or vertically. Works on items in hand placed on the surface or ghosts. AssemblingMachines can now be mirrored by flipping them, allowing additional fluid box configurations. Bound to F (Horizontal) & V (Vertical) by default.
- Upgrade planner can install new modules into machines, this is done by leaving the source slot empty and setting up only the destination slot.
- Upgrade planner module upgrade/install can have machine filter and maximum count per machine specified.
- Upgrade planner now has dynamic size, similar to the blueprint library. The size is capped at 250 rows now.
- Added a way to create module/fuel requests in entities remotely by clicking with ghost item in hand. ( Friday Facts #380 )
- All turrets (except for artillery) can now be configured individually to prioritize certain types of enemies when looking for targets. ( Friday Facts #410 ) The priority settings can be copy-pasted between the different turret types and can be configured through the circuit network.
- Added latency hiding for cars (and tanks).
- Rocket silos continue producing parts for the next rocket while the current rocket is being launched. Completing another rocket soon enough skips closing and reopening the doors. ( Friday Facts #405 )
- Improved the way spidertrons are remotely controlled. Instead of spidertron remote being linked to single spidertron, it can be used to group select and command spidertrons like in your typical RTS game.
- Spidertrons can be entered remotely, so you can control them as if you were inside physically, so switching the map on/off doesn't distrubt the mode.
- Allowed opening and configuring entities through remote view. ( Friday Facts #380 )

### Ease of use

- Added green indicator (instead of yellow), when previewing underground belt/pipe on its maximal distance. ( Friday Facts #388 )

### Circuit Network

- Added selector combinator. It allows to select one of the signals, or the signal count from an input.
- Added editable description to combinator entities.
- Decider Combinators are now allowed to check multiple conditions and send multiple outputs per combinator.
- Arithmetic combinator now allows to select red and green networks for input signals and perform Each-Each operations.
- Signal pipetting.
- Added display panel. 1X1 entity which can show specified icon and/or text, possibly also on the map. It can be also controlled by the circuit network. ( Friday Facts #419 )
- Transport belt connected to a circuit network can now read contents of the whole segment instead of just the one tile. ( Friday Facts #405 )
- Roboports can read logistic network contents and requests. ( Friday Facts #428 )
- Roboports can output the number of roboports in the logistic network to the circuit network. ( Friday Facts #428 )
- Logistic Chests have an optional circuit condition to enable / disable their connection to the network. ( Friday Facts #428 )
- Rocket silo is connectable to circuit network, and allows to read its contents.
- Rocket silo circuit connection can read orbital requests.
- All turrets (including artillery) can now be connected to the circuit network to read their current ammo count and/or deactivate them. ( Friday Facts #410 )
- Assembling machines, chemical plants, oil refineries and centrifuges can now send the ingredient list of their recipes to the circuit network.
- Drag building electric poles will also drag circuit wires when starting from electric pole with already connected circuit wires.
- When electric pole is removed, it will rewire circuit wires similar to copper wires.
- Cut/copy pasting blueprint with external circuit wire connections will preserve these connections when the blueprint is built (if possible). ( Friday Facts #402 )
- Radar can now be connected to circuit network, allowing to wirelessly transmit a single channel of red and green signals on each planet/surface. ( Friday Facts #402 )
- Added a way to read nuclear reactor temperature through the circuit network. ( Friday Facts #428 )

### Minor Features

- Added "No enemies" setting that disables enemy unit spawning from enemy spawners, map gen, and items. Does not disable enemy spawners.
- Upgrade planner can upgrade fuel in blueprints (yet to be implemented for existing entities).
- Added cargo pods that move items from platforms to landing pads.
- Added a warning when a save game is too large to sync via the Steam cloud.
- Added PipeWire audio driver.
- Added a setting to select the preferred audio driver on Windows and Linux.
- Undo improvements. Undo actions older than 1 minute require confirmation +flying text notification of what was undone.
- Added redo.
- Allow undoing of module changes done via upgrade planner.
- Allow undoing of copy-pasting entity settings like assembler recipes or inserter filters. ( Friday Facts #412 )
- Allowed lamps color to be configured manually.
- Manual building in latency state now tracks used items.
- Manual building previews will now highlight ghosts that would be removed.
- Blueprints with entities and landfill are now one-click buildable over water.
- Added icons for tileable blueprints, like "Curve, Corner, T junction, X junction" and similar, in Virtual signals category.
- Evolution factors are now tracked individually for each surface.
- Pumps now can have a fluid filter. If present, only the specified fluid is taken from the pump's source.
- Electric poles are no longer limited to 5 copper connections to other electric poles.
- Removed some of the abstract items (red wire, green wire, discharge defense, artillery remote, spidertron remote) and replaced them with shortcut bar tools which can be used anytime for free. ( Friday Facts #379 ) These tools can still be placed into the quickbar if desired.
- The smart pipette can also pick terrain and using it on fluid select the offshore pump.
- The smart pipette can also pick items from crafting, logistic, select list, inventory and quickbar.
- Disabling train stop no longer sends ongoing trains away. Disabled train stop is now considered full and trains will not skip schedule records.
- Map tags can be moved. ( Friday Facts #388 )
- Map tags can be quickly copied using pipette. ( more )
- Map tags and pings can be placed while zoomed in to game view.
- Spidertrons can be damaged by cars and tanks, can be damaged by walking on fire, and can be slowed with slowdown capsules.
- Switching to the map editor using /editor now places the player at the position they were looking at in remote view. Switching out of the map editor returns the character to the position it was when entering. Added editor options to individually revert these changes to their previous behavior.
- Numerical textfields accepts values with postfix formats (10k instead of 10000 etc), simple math expressions, like 3*7+7k are also possible.
- Added logic to hide previews for buildable items if fast-transfer modifiers (default: Ctrl) are pressed. Doesn't apply to blueprints or when rail planner is active.
- Improved the AI of the worker flying robots when it comes to choosing roboport to recharge. It prefers roboports closer to its destination, so (for example) it won't get stuck over lakes forever.
- When you retrieve your corpse, the logistic requests will re-enable if they were enabled before death. (Related to the already existing behaviour, where the requests are disabled upon death, to avoid unwanted supply)
- Dedicated servers will stay paused until the first player is fully connected (if auto-pause is enabled).
- Added an option to auto-pause servers while any player is connecting (defaults to false).
- Added several new achievements both to the base game and space age.
- When renaming a train stop, it will try to copy its color from an existing stop with that name.
- Added control inputs (Ctrl/Shift + Arrow keys) to adjust blueprint grid alignment.
- Train stop can be given a priority, trains will prefer going to the train stop with higher priority and it will be easier for them to depart from such train stop. ( Friday Facts #395 )
- Allow copy-pasting of setting for trains and train stops while in chart view. ( Friday Facts #403 )
- Crafting machines can craft more than 1 recipe per tick if their speeds are fast enough.
- Improved the ultra-wide monitor experience by greatly increasing the maximum view distance based on the game window's dimensions.
- Added "sync-mods" command line option to sync mods with a given save file.
- Trains with non-empty schedule are automatically switched into automated mode upon completition.
- The spidertron inventory is automatically sorted.
- Added a browse history feature. Pressing ALT + arrow keys (or the arrow button on the right top of the window), can go back and forth through what was opened. ( Friday Facts #397 )
- Added 8 directional arrows to virtual signals. Also added red cross signal next to the checkmark.
- Added a super forced mode for deconstruction planner: when selecting area while holding Ctrl + Shift (by default) deconstructs everything (deconstructible and not filtered out), i.e. entities, tiles and hidden tiles
- Added a reverse mode for deconstruction planner: when selecting an area using right-click, the white-/blacklist setting for entity and tile filters will be reversed for this selection.
- Added a nondefault tile cover cache - last used cover tile is being saved per surface per force per tile id being covered. For most intents and purposes, those values act the same as default covers defined by covered tile prototype (for tiles without default cover defined).
- The storage filter of logistic storage chests can now be copy-pasted.

### Optimizations

- Added automatic splitting of repeated noise expressions into separate procedures which increased map generation speed.
- Improved C++ structure of noise expressions which reduced game start-up time and MapGenSettings compilation time.
- Improved worker robot performance, they are not updated every tick when moving or stationary anymore. ( Friday Facts #421 )
- Improved performance of idle roboports. ( Friday Facts #421 )
- Improved radar charting speed. ( Friday Facts #421 )
- Improved circuit network logic by making it fully multithreaded.
- Changed Spidertron walking strategy to deliberately alternate legs and be overall more efficient and performant.
- Changed train wait condition evaluation order to check 'cheap' conditions (e.g. wait time) before 'expensive' conditions (e.g. inventory) within a set of "and"-connected conditions.

### Graphics

- Changed night vision effect from grayscale to a more contrasty one.
- Added decay stages for enemies. (Biters, Spitters, Worms, Spawners)
- Reworked die animations, now they have more gore to transition into the decay stages better.
- Reworked fire animations, improved quality and increased resolution.
- Reworked rocket projectile animations
- Fixed copper and circuit wires appearing to sag below the perceived ground level.
- Fixed copper and circuit wire shadows projecting onto the ground incorrectly.

### Sounds

- Improved sounds of dying enemies.
- Added different sounds for manipulating different items in the inventory and opening different entities. ( Friday Facts #396 )
- Added different sounds for shooting different kind of targets.
- Added ambient sounds. ( Friday Facts #396 )
- Added semi-persistent ambient sounds.
- Added support for sound accents for entities' working_sound. These are short sounds which play at a specific moment in the entity's animation.
- Added support for multiple main sounds for entities' working_sound.
- Extended support for aggregation to most sounds.
- Added controls to skip current music track, go back to previous one and to pause/resume music.
- Added new music. ( Friday Facts #406 )
- Added variable music. ( Friday Facts #407 )

### Balancing

- Diminishing return of beacons effect ( Friday Facts #409 )
- Lowered Fluid pumping speed from 12 000 to 1 200.
- Altered the mining drill bounding box, so you can walk between mining drill and substation and such.
- Lowered stack size of ammo from 200 to 100.
- Increased fluid wagon capacity from 25000 to 50000 to make fluid wagons more compelling compared to the new pipe mechanics.
- Increased low density structure stack size from 10 to 50.
- Increased beacon stack size from 10 to 20.
- Rocket part takes 10 times less ingredients than before.
- Rocket silo requires 50 rocket parts to craft a rocket instead of 100.
- Biter spawner health grows with evolution, up to 10 times with maximum evolution.
- Increased health of bigger worms, and added a laser resistance to them.
- Removed the 15% explosion damage resistance from biter spawners.
- Doubled the damage of artillery.
- Nerfed personal laser defense damage output to 1/3 its previous output.
- Changed all module-3 recipe to require only 4 (instead of 5) module-2 ingredients.
- Greatly increased default tile pollution absorption.
- Increased rocket fuel stack size from 10 to 20.
- Decreased the crafting time of rocket ingredients.
- Decreased the crafting time of solid fuel.
- Increased damage and range of non-explosive cannon shells.
- Doubled the distractor robot health from 90 to 180 and life time from 45s to 90s.
- Increased destroyer robot base damage from 10 to 20 and range from 15 to 20.
- Increased damage of shotgun pellets from 5 to 8, and made shotgun projectiles spawn closer to the player.
- Increased battery capacity of construction robot from 1.5MJ to 3MJ.
- Rocket (ammo) no longer requires an electronic circuit to be crafted.
- Rocket and Explosive rocket projectiles accelerate twice as fast.
- Changed the rocket recipe to require only processing unit instead of rocket control unit. Rocket control unit was removed from the game.

### Changes

- Reworked the fluid system flow logic. ( Friday Facts #416 ) Contiguous sections of pipes and storage tanks are merged into segments. Each segment contains a single fluid, and throughput is proportional to how full a segment is.
- Removed Filter and Stack filter inserter, instead all inserters can use filters now.
- Character corpses no longer despawn.
- Merged zoom controls and removed functionality to zoom in without leaving chart view.
- Kovarex enrichment process is now unlocked by automation, logistic and chemical science pack only.
- Power armor equipment grid resized from 7x7 to 6x8 to be a bit more practical.
- Power switch and Programmable speaker stack size reduced from 50 to 10.
- Big and huge rock doesn't drop stone items when destroyed anymore.
- 1 Water will now produce 10 Steam in boilers/heat exchangers.
- Boilers will respect conservation of energy by considering heat capacity of input and output fluids.
- Improved high-DPI display support on Windows to match that of Retina displays on macOS.
- Removed the "fuzzy search" setting.
- Updated SDL to version 2.30.0.
- Smart belt building was slightly improved, so it makes the underground also when overbuilding belt gap with belts already present on both sides.
- Trains will not skip stations that do not have any valid stops, they will 'no path' instead.
- Trains with artillery wagons now need to wait for all cannons to be in fully their parked position before departing. When driving manually, keep holding accelerate to command the artillery to stop firing and assume their parked position.
- Improved Apple Retina display support throughout the game.
- Made manual UI scale setting visually consistent between Retina and non-Retina displays, and between native resolution rendering setting being enabled and disabled.
- Default control key for Map changed from M to Tab or M.
- Default control key for Next weapon changed from Tab to C.
- Default control key for Shoot selected changed from C to Shift+Space.
- Default control key for Toggle personal roboport changed from Alt + R to Alt + F.
- Added event-based technologies for unlocks related to the early game.
- Added event-based technologies to only allow to research the oil related and uranium related technologies after the related resource had been mined.
- Switching to map view switches to remote controller now, which allows to open and setup entities even when they are far away.
- Chunks under fog of war are covered even in normal view.
- Default train connect key is now J, train disconnect key is now K and vertical flip is now V.
- Allowed electric poles to be fast-replaced by moving.
- Allowed entity ghost-building over tile ghosts.
- Allowed landfill mining.
- Underground belts and pipes-to-ground connections can be blocked by certain tiles.
- Disabled loading of saves before 1.0.0 version (You can use 1.1 to load older saves and re-save them).
- Changed the /evolution command to respect the now Surface-based evolution tracking. Provide a Surface's name as parameter to get its evolution factor, or leave blank to get a full list.
- Locomotive fuel inventory is now accesible by inserters, so it can be unloaded automatically.
- Changed module limitations for recipes from item-based to effect-based. A module can't be placed into a machine if the current recipe doesn't support one of the effects.
- Changed "use item" (grenades, artillery remote, capsules) to its own control and changed the default to right mouse button.
- Improved heuristic of robots selecting roboports to charge/station.
- Changed selection logic of entity ghosts. They now behave as if they were real entities already.
- Car collisions impact on speed reworked (destroying obstacles now slows the car less than before).
- Added one more color to robot overview on the map (red = logistic robots targeted to me, to deliver or to trash).
- Launching space science pack into space no longer returns fish as there is now an other method to automate obtaining fish.
- Changed command-line map preview to match GUI map preview, including correct overlapping ore generation and cliffs.
- Changed --report-quantities option to report total entity count and resource amount in the selected area instead of approximate values.
- Removed --map-preview-scale, --slope-shading, --slope-shade-property and --noise-outputs command-line options.
- Ghost pipes are now connecting to other pipes.
- When train has no fuel, player can manually move the train slowly when it is manually controlled. ( Friday Facts #403 )
- Increased Big electric pole maximum wire reach from 30 to 32.
- Electric poles are always crafted from copper wire instead of copper plates.
- Removed sandbox scenario.
- Tweaked most of the tips trigger and skip trigger logic, added new tips. Added the ability to show animated UI related tips.
- MapTick is now 64 bit.
- Disabled the turret shooting alert by default.
- Remnants of destroyed player buildings do not disappear after a while any more.
- Increased the number of chunks generated around players based on the maximum view distance.
- Steam Cloud sync for blueprint library is enabled by default now, and library is saved to blueprint-storage-2.dat.
- Changed pipe to ground collision mask so player can walk on top of it.
- Using the pipette on an entity marked for upgrading now picks the result of the upgrade instead of the existing entity.
- Rotating (and flipping) already built entities is now allowed at any distance.

### Gui

- Added Players screen (accessible from the side menu), where each of the player can be inspected. ( Friday Facts #423 )
- Added click-and-drag to rearrange logistic requests within a section.
- Changed spidertron gui to have 3 panels instead of two when the flat character gui settings is selected (which is by default).
- The spidertron grid is opened by a button instead of a tab.
- Improved the tooltips of the graph, to actually explain what is the relationship of the two numbers displayed.
- Production and electric network graphs now highlight the corresponding line if an item's slot is hovered in the list below.
- Fixed technology graph UI not properly scaling with UI scale.
- Fixed heat exchanger glow sprite was drawn above the character sprite. ( more )
- Fixed a minor bug in the fluid movement calculation, which didn't take the volume of the container into considaration properly.
- Restructured all the circuit condition windows.
- Circuit and logistics condition windows can be opened at the same time.
- New logistic networks GUI. ( Friday Facts #405 )
- Added Arrow Up/Down keys support when searching in a listbox.
- The trains stop gui contains a list of trains on the way to this stop ( Friday Facts #403 ).
- Added option switch save game sorting by either name or last modified state.
- Added a notification of researched technology.
- Research widget has a tooltip which shows the research production graph for the last 10 minutes. ( Friday Facts #423 )
- Alert gui now allows specific selection of the problem we want to move to. ( Friday Facts #400 )
- Circuit conditions for trains now show precise progress in the GUI if it makes sense for the condition.
- Changed sorting of technologies in technology list to put infinite technologies at the back.
- The buttons for circuit and logistic control settings of entities are now always visible if the entity supports them.

### Modding

- Added global feature_flags in the settings and prototype stages.
- Added BeaconPrototype::allowed_module_categories, CraftingMachinePrototype::allowed_module_categories, LabPrototype::allowed_module_categories, MiningDrillPrototype::allowed_module_categories, and RecipePrototype::allowed_module_categories.
- Replaced the map generator water slider with an autoplace control prototype; water_level and segmentation_multiplier are now noise expressions.
- Removed pre-defined noise variables finite_water_level, wlc_elevation_offset, wlc_elevation_minimum, cliff_elevation_offset, terrace_elevation_offset, terrace_elevation_interval. Added cliff_elevation_0.
- Added EntityWithHealthPrototype::overkill_fraction.
- Removed AutoplacePeak specification format.
- Added AmmoItemPrototype::shoot_protected.
- Removed ItemPrototype::rocket_launch_product. Use rocket_launch_products instead.
- Moved FluidBoxManagerPrototype::off_when_no_fluid_recipe up to AssemblingMachinePrototype::fluid_boxes_off_when_no_fluid_recipe.
- Added delayed-active-trigger ActiveTrigger type.
- Added ability to attach a SmokeWithTrigger to a target entity and make it fade when the target entity is destroyed.
- Added time-based cooldowns to TriggerEffectWithCooldown.
- Removed ContainerPrototype::enable_inventory_bar.
- Added ContainerPrototype::inventory_type "normal".
- Added LinkedContainerPrototype::inventory_type "normal".
- Added ItemPrototype::send_to_orbit_mode.
- Renamed ItemPrototype::placed_as_equipment_result to place_as_equipment_result to match the runtime name.
- Removed BurnerEnergySource::fuel_category. Use BurnerEnergySource::fuel_categories instead.
- Removed slice, slice_x and slice_y from Sprite and RotatedSprite.
- Changed PipeToGround::pictures to use a standard Sprite4Way.
- Removed OffshorePumpPrototype::picture. Use OffshorePumpPrototype::graphics_set instead.
- Removed deprecated "compressed" SpriteFlag.
- Removed icon_mipmaps from various prototypes using icons. Mipmap count will be inferred from icon_size and actual dimensions of the source image.
- Added OffshorePumpPrototype::energy_source and energy_usage.
- Changed research unit ingredients to only be specified by a tuple.
- Changed recipe ingredients to only be specified by a table with named keys.
- Removed catalyst_amount from recipe ingredients and products.
- Added ignored_by_stats to recipe ingredients.
- Added ignored_by_stats and ignored_by_productivity to recipe products.
- Added 'R' (ronna) and 'Q' (quetta) SI prefixes.
- Removed 'K' from allowed SI prefixes - use 'k' instead.
- Renamed "effectivity-module" to "efficiency-module", including all items, recipes, and technologies.
- Renamed technology "advanced-electronics" to "advanced-circuit".
- Renamed technology "advanced-electronics-2" to "processing-unit".
- Renamed technology "optics" to "lamp".
- Reset technology effects is automatically run when technology unlocks change.
- Renamed boiler "heat-water-inside" mode to "heat-fluid-inside".
- Replaced TileSpriteLayoutVariant::tall with TileSpriteLayoutVariant::tile_height.
- Removed WorkingVisualisation::draw_as_sprite and WorkingVisualisation::draw_as_light. Use SpriteParameters::draw_as_light and draw_as_glow instead.
- Removed BeaconModuleVisualization::draw_as_sprite and BeaconModuleVisualization::draw_as_light.
- Removed AnimationElement::draw_as_sprite and AnimationElement::draw_as_light.
- Removed BeaconGraphicsSet::apply_module_tint_to_light.
- On prototypes of entities with circuit connector removed circuit_wire_connection_points and circuit_connector_sprites but added circuit_connector.
- Renamed InserterPrototype::stack to InserterPrototype::bulk.
- Changed "forward-then-backward" animation run mode to not repeat the first and the last frame when running backward.
- Determining whether a tile draws transitions over different tile takes into consideration also TilePrototype::layer_group now.
- Renamed TileRenderLayer "ground" to "ground-natural" and added "ground-artificial".
- Reduced number of layers in "zero" tile render layer group from 128 to 64. And "water" from 64 to 8.
- Removed TilePrototype::draw_in_water_layer.
- Changed tile graphics definition format for both main tile pictures and tile transitions. See TilePrototype documentation.
- Add more prototype properties for shaping Spidertron and spider unit legs and behaviors.
- Loader is now circuit connectable.
- Increased the limit of different "optimized-decorative" types from 255 to 65535.
- Removed EntityPrototype::drawing_box and replaced it with drawing_box_vertical_extension.
- Changed icon_size default to be always 64, which is also defined by defines.default_icon_size, for the case we ever wanted to change this.
- Changed icon drawing in GUIs to account for all layers when scaling them to fit a slot or a button.
- Added IconData::draw_background.
- Increased the limit of different tile types from 255 to 65535.
- Collision layers are now defined by prototypes. There is still limit of 55 layers but the layers themselves can have any name.
- Collision mask has a mandatory table "layers" which must specify layers as dictionary.
- Removed collision layers from "layer-13" to "layer-55".
- Changed prototypes from straight-rail to legacy-straight-rail and curved-rail to legacy-curved-rail
- New rail prototypes: straight-rail, curved-rail-a, curved-rail-b, half-diagonal-rail, rail-ramp, elevated-straight-rail, elevated-curved-rail-a, elevated-curved-rail-b, elevated-half-diagonal-rail.
- Added rail-support prototype.
- Changed way of defining rail prototype graphics: pictures are tied to direction of an entity they will be used by.
- Changed prototype data loading to enforce the correct types are used.
- Restricted prototype names to only contain alphanumeric characters, dashes and underscores.
- Added RailPrototype::ending_shifts to fine-tune render position of rail endings.
- Added RollingStockPrototype::transition_collision_mask and RollingStockPrototype::elevated_collision_mask.
- Changed rail planner prototype: it now takes list of rail entities it is allowed to place and optional support for use with elevated rails.
- Added EntityPrototypeFlag "building-direction-16-way".
- Reworked noise expression definition system.
- Added circuit connections to TurretPrototype and ArtilleryPrototype.
- Changed most entity graphics definitions to be optional.
- Changed various entity prototypes to only accept "energy_source" for the energy source, not "burner".
- Changed PumpPrototype::fluid_box into input_fluid_box and output_fluid_box.
- Changed TileEffectDefinition to allow for different effects.
- Changed "finish-the-game-achievement" achievement type to "complete-objective-achievement".
- Renamed until_second to within for various achievement prototypes.
- Renamed spidertron-remote prototype to rts-tool.
- Moved subgroup property from individual prototypes to PrototypeBase.
- Removed "axially_symmetrical" property from RotatedSprite and RotatedAnimation definitions.
- Removed the entity flag fast-replaceable-no-cross-type-while-moving and fast-replaceable-no-build-while-moving.
- Removed support for emissions_per_second from worker robots.
- Renamed track_coverage_during_build_by_moving to track_coverage_during_drag_building and changed the default to true
- Added optional tile_condition to the place_as_tile, which allows to specify explicit list of tiles it can be built over.
- Added vector_to_place_result (drop target) support to crafting machines.
- Changed default value of TilePrototype::check_collision_with_entities to true.
- The fluid generated by offshore pump is property of the tile instead of the pump.
- Replaced ModulePrototype::limitation and ModulePrototype::limitation_blacklist with RecipePrototype::allow_[effect-name] properties (e.g. RecipePrototype::allow_productivity). By default, all effects except productivity are allowed.
- Replaced ModulePrototype::limitation_message_key with RecipePrototype::allow_[effect-name]_message properties (e.g. RecipePrototype::allow_productivity_message). If not set, the game uses "item-limitation.[effect-name]-effect".
- Added ElectricPolePrototype::auto_connect_up_to_n_wires.
- Added RecipePrototype::hide_from_signal_gui.
- Replaced min_perceived_performance, performance_to_sound_speedup, min_animation_progress and max_animation_progress with perceived_performance table containing minimum, maximum and performance_to_activity_rate.
- Entity selection priority is no longer deduced from collision masks. Use property 'selection_priority' for that purpose.
- Several prototype types have been given new 'selection_priority' default values, documented in '__base__/prototypes/entities/entity_util.lua'.
- The prototype names of logistic chests have been changed to match their English display name. 'logistic-chest-requester' became 'requester-chest', etc. This applies to entities, items and recipes. Saves, exported blueprint/book/planner strings, and rich text tags in labels and destriptions will have their contents migrated automatically.
- Added RocketSiloPrototype::rocket_quick_relaunch_start_offset, specifying the starting position for rockets created with the new quick-launch feature. 0 is the regular starting position, 1 is the end of the rising animation.
- Added optional RocketSiloPrototype::rocket_parts_storage_cap, denoting when a silo is considered "full" for crafting rocket parts. Has to be at least rocket_parts_required, and defaults to that value.
- Reworked how PipeConnectionDefinitions are specified. Added 'connection_type'. Added ability to specify 'linked' connection_type. Renamed 'type' into 'flow_direction'. Added direction. 'position' now has to be inside of the entity. Added 'connection_category'. Added 'linked_connection_id'.
- Deprecated player-port prototype.
- Changed type of 'entity-unknown', 'tile-proxy', 'tree-dying-proxy', 'tree-proxy' from flying-text to entity-ghost.
- Removed the "flying-text" entity type. Use LuaPlayer::create_local_flying_text or LuaRendering::draw_text instead.
- Removed the "flame-thrower-explosion" entity type.
- Removed "smoke" entity prototype.
- Removed "particle" and "leaf-particle" entity prototypes.
- Removed "mining-tool" item prototype.
- Removed "noise-layer" prototypes. Places previously accepting them now take a 32-bit integer or a string which gets converted using CRC32.
- Removed SpiderEnginePrototype::military_target check. If a spider vehicle should be a military target, set EntityWithOwnerPrototype::is_military_target directly.
- Removed RecipePrototype::result and result_count. Use RecipePrototype::results instead.
- ProductPrototype now has a mandatory "type" field and does not accept simplified syntax for item products.
- Unified the way hidden property of all prototypes is specified, which is always a hidden bool instead of different kind of flags.
- Added MiningDrillPrototype::effect_receiver, CraftingMachinePrototype::effect_receiver and LabPrototype::effect_receiver.
- Removed MiningDrillPrototype::base_productivity, CraftinMachinePrototype::base_productivity and LabPrototype::base_productivity. They were moved into EffectReceiverPrototype::base_effect.
- Restructured SelectionToolPrototype: specific modes are described under select(required), alt_select(required), reverse_select(optional) and alt_reverse_select(optional) tables.
- Added airborne-pollutant prototype and changed various pollution related properties to support multiple pollution types.
- Rearranged BoilerPrototype's pictures.
- Added CorpsePrototype::expires, defaulting to 'true'. Denotes whether corpses of this type expire by default.
- Moved character guns inventory size to the prototype as guns_inventory_size defaulting to 3.
- Removed hr_version from all graphics definitions. The graphics are now always considered to be in high definition.
- Removed ability of ItemWithInventory to extend inventory.
- Removed ItemPrototype::default_request_amount and wire_count.
- Removed normal and expensive properties from TechnologyPrototype and RecipePrototype.
- Removed deprecated graphics definitions from TransportBeltConnectablePrototype, use belt_animation_set instead.
- Removed RocketSiloPrototype::rocket_result_inventory_size.
- Removed ConstantCombinatorPrototype::item_slot_count.
- Changed "combat-robot-count" achievement type to "combat-robot-count-achievement".
- Changed "ghost-time-to-live" modifier type to "create-ghost-on-entity-death" and changed the modifier from double to bool.
- Added EntityPrototype::icon_draw_specification, to control the scale and shift of alt-info icons for entities.
- Removed AmmoTurretPrototype::entity_info_icon_shift.
- Removed CraftingMachinePrototype::entity_info_icon_shift.
- Removed CraftingMachinePrototype::scale_entity_info_icon.
- Removed StorageTankPrototype::scale_entity_info_icon.
- Removed LinkedContainerPrototype::scale_info_icons.
- Removed ContainerPrototype::scale_info_icons.
- Removed RobotWithLogisticInterfacePrototype::cargo_centered.
- Removed utility constant pollution_color.
- Removed biter_ai_settings global variable. Instead, when requiring "biter-ai-settings.lua", assign the returned table to a local variable.
- Added BeamPrototype::graphics_set and moved graphics related properties there.
- Added CraftingMachinePrototype::graphics_set and moved graphics related properties there.
- Added AccumulatorPrototype::chargable_graphics and moved graphics related properties there.
- Added space-platform-hub, cargo-pod and cargo-bay prototypes.
- Added asteroid, asteroid-collector and thruster prototype.
- Added asteroid-chunk prototype.
- Added cargo-landing-pad prototype.
- Added procession and procession-layer-inheritance-group prototypes.
- Added space-platform-starter-pack, space-location, planet and space-connection prototypes.
- Added surface-property and surface prototypes.
- Added active-trigger and chain-active-trigger prototypes.
- Added quality prototype and various related prototype properties.
- Added spider-unit prototype.
- Added segment and segmented-unit prototypes.
- Added lightning-attractor prototype.
- Added lightning prototype.
- Added plant prototype.
- Added agricultural-tower prototype.
- Added selector-combinator and display-panel prototypes.
- Added fusion-generator and fusion-reactor prototypes.
- Added burner-usage prototype.
- Added temporary-container prototype.
- Added equipment-ghost prototype.
- Added impact-category, deliver-category and deliver-impact-combination prototypes.
- Added remote-controller prototype.
- Added stateless_visualisation_variations to DecorativePrototype, SimpleEntityPrototype, SimpleEntityWithOwnerPrototype and TreePrototype.
- Added stateless_visualisation to DecorativePrototype and EntityPrototype.
- Added RoboportPrototype::radar_range.
- Added ShortcutPrototype::unavailable_until_unlocked.
- Added MiningDrillPrototype::resource_drain_rate_percent and filter_count.
- Added MiningDrillPrototype::drops_full_belt_stacks.
- Added LoaderPrototype::max_belt_stack_size.
- Added InserterPrototype::max_belt_stack_size.
- Added InserterPrototype::grab_less_to_match_belt_stack and enter_drop_mode_if_held_stack_spoiled.
- Added BeaconPrototype::profile and beacon_counter.
- Added AmmoItemPrototype::ammo_category.
- Added LogisticContainerPrototype::trash_inventory_size.
- Added LabPrototype::trash_inventory_size.
- Added CarPrototype::auto_sort_inventory and trash_inventory_size.
- Added RocketSiloPrototpye::rocket_supply_inventory_size, logistic_trash_inventory_size, render_not_in_network_icon and cargo_station_parameters.
- Added TilePrototype::built_animations and related properties.
- Added TilePrototype::weight, max_health, dying_explosion, destroys_dropped_items and default_destroyed_dropped_item_trigger.
- Added ItemPrototype::weight, random_tint_color, has_random_tint, plant_result, destroyed_by_dropping_trigger and default_import_location.
- Added ItemPrototype::spoil_result, spoil_to_trigger_result and spoil_ticks.
- Added CliffPrototype::place_as_crater.
- Added TurretPrototype::graphics_set and other graphics related properties.
- Added TechnologyPrototype::research_trigger and allows_productivity.
- Added AmbientSound::planet and variable_sound.
- Added Prototype::factoriopedia_alternative and PrototypeBase::factoriopedia_description, hidden_in_factoriopedia and factoriopedia_simulation.
- Added RecipePrototype::preserve_products_in_machine_output, surface_conditions and maximum_productivity.
- Added VehiclePrototype::allow_remote_driving.
- Added MapSettings::asteroids.
- Added RollingStockPrototype::default_copy_color_from_train_stop.
- Added AmmoTurretPrototype::energy_source and energy_per_shot.
- Added RocketSiloRocketPrototype::cargo_pod_entity.
- Added EntityPrototype::ambient_sounds, tile_buildability_rules, impact_category, icons_positioning and surface_conditions.
- Added RadarPrototype::connects_to_other_radars, energy_fraction_to_connect and energy_fraction_to_disconnect.
- Added CustomInputPrototype::block_modifiers.
- Added ArmorPrototype::provides_flight, collision_box and related properties.
- Added CharacterPrototype::flying_bob_speed, grounded_landing_search_radius and flying_collision_mask.
- Added capture-robot prototype.
- Added EnemySpawnerPrototype::captured_spawner_entity and time_to_capture.
- Added EntityPrototype::heating_energy.
- Added frozen graphics to various entities.
- Added inventory-bonus-equipment prototype.
- Added lane-splitter prototype.
- Added new achievement prototypes: dont-kill-manually-achievement, dont-research-before-researching-achievement, change-surface-achievement, create-platform-achievement, deplete-resource-achievement, destroy-cliff-achievement, equip-armor-achievement, module-transfer-achievement, place-equipment-achievement, research-with-science-pack-achievement, shoot-achievement, space-connection-distance-traveled-achievement, use-item-achievement.
- Added FluidPrototype::visualization_color.
- Added PipeToGroundPrototype::visualization.
- Added "get-by-unit-number" entity prototype flag.
- Changed plural localisation format to use double underscores around parameter index.
- Added new prototype type "custom-event" to define custom events in the data stage. Custom events share the same namespace as custom inputs and built-in events for subscribing to and raising them.
- Added "grounded" sticker effect to temporarily disable mech armor flight
- Changed autoplace control-setting variable names in noise expressions to be shorter/less verbose.
- Added dynamic volume modifiers to sounds. These are applied when specific conditions in-game are met.
- Added non-linear modes for sound attenuation.
- Added an option to override default zoom level attenuation for individial sounds.
- Added darkness (time of day) threshold for sounds.
- Added Sound::advanced_volume_control which includes attenuation (distance based), fades (zoom level based) and darkness threshold.
- Added Sound::speed_smoothing_window_size to smooth out changes in playback speed.
- Added priority selection to sound aggregation.
- Added activity matching modifiers to further control activity to volume or speed matching of working_sound.
- Added Sound::priority. Sounds with higher priority can replace sounds with lower priority when all audio resources are used.
- Added SoundDefinition::min_volume and SoundDefinition::max_volume for automatic volume variation.

### Scripting

- Renamed `global` into `storage`.
- Added LuaBootstrap::feature_flags.
- Added LuaEntityPrototype::allowed_module_categories read.
- Added LuaRecipePrototype::allowed_module_categories read.
- Removed LuaConstantCombiantorControlBehavior::parameters read/write.
- Added LuaPlanet::associate_surface.
- Added on_space_platform_pre_mined, on_space_platform_mined_item, on_space_platform_mined_entity, on_space_platform_built_entity, on_space_platform_built_tile, and on_space_platform_mined_tile.
- Renamed on_built_entity and on_robot_built_entity parameter `created_entity` to `entity`.
- Removed LuaConstantCombinatorControlBehavior::signals_count, set_signal() and get_signal().
- Removed LuaGameScript::disable_tutorial_triggers().
- Added LuaGameScript::enable_tip_triggers_in_custom_scenarios().
- Added event on_player_used_spidertron_remote.
- Added LuaEntity::cargo_pod read.
- Added LuaHelpers class globally visible under `helpers` in control stage, including in `on_load`.
- Moved LuaGameScript::table_to_json, json_to_table, write_file, remove_path, direction_to_string, evaluate_expression, encode_string, decode_string, parse_map_exchange_string, check_prototype_translations, is_valid_sound_path, is_valid_sprite_path to LuaHelpers.
- Removed LuaGui::is_valid_sprite_path. Use LuaHelpers::is_valid_sprite_path instead.
- Removed LuaRendering::is_font_valid. Use LuaPrototypes::font instead.
- Removed LuaGameScript::active_mods. Use LuaBootstrap::active_mods instead.
- Added on_player_controller_changed event.
- Added LuaEntity::force_finish_ascending() and force_finish_descending() methods.
- Added LuaEntity::procession_tick read/write.
- Removed LuaPlayer::open_map, zoom_to_world, and close_map. LuaPlayer::set_controller with type 'remote' replaces these.
- Added LuaPlayer::centered_on read/write.
- Added LuaPrototypes globally visible under `prototypes` in control stage, including in `on_load`.
- Moved prototypes access from LuaGameScript::X_prototypes to LuaPrototypes::X.
- Moved filtered prototypes access from LuaGameScript::get_filtered_X_prototypes to LuaPrototypes::get_X_filtered.
- Moved LuaBootstrap::get_prototype_history to LuaPrototypes::get_history.
- Moved LuaGameScript::styles to LuaPrototypes::style.
- Moved LuaGameScript::map_gen_presets to LuaPrototypes::map_gen_preset.
- Moved LuaGameScript::named_noise_expressions to LuaPrototypes::named_noise_expression.
- Renamed LuaSettings::player to player_default.
- Changed Vectors to always be read from the game as the two-element array format instead of sometimes using x and y keys. This mostly affects properties of TriggerEffectItem. Writing a Vector to the game still accepts both formats.
- Removed util.online_players. Use game.connected_players instead.
- Removed LuaEntity::is_entity_with_force. Use LuaEntity::is_military_target instead.
- Added preserve_ghosts_and_corpses argument to LuaSurface::create_entity.
- Added cause argument to LuaSurface::create_entity.
- Added on_pre_scenario_finished event.
- Added optional gui_title to game.create_inventory().
- Changed on_entity_damaged.cause semantics
- Added on_entity_damaged.source
- Replaced dealer argument with source and cause arguments in LuaEntity::damage().
- Added LuaEntityPrototype::growth_grid_tile_size read.
- Added LuaEntityPrototype::harvest_emissions read.
- Added LuaSurfacePrototype::surface_properties read.
- Added max_radius and use_start_position_on_failure to LuaSurface::spill_item_stack.
- Changed LuaSurface::spill_item_stack to take a table of parameters.
- Lua functions inside of `global` will now throw an error when saving instead of being silently discarded.
- Renamed LuaEntityPrototype::stack to LuaEntityPrototype::bulk.
- Added LuaTechnology::successors and LuaTechnologyPrototype::successors read.
- Added LuaGameScript::technology_notifications_enabled (read/write).
- Removed LuaForce::get_saved_technology_progress() and set_saved_technology_progress(). Added LuaTechnology::saved_progress (read/write).
- Added LuaPlayer::locale read and on_player_locale_changed event.
- Moved LuaGameScript::request_train_path into LuaTrainManager::request_train_path.
- Removed LuaEntity::get_rail_segment_entity. Added LuaEntity::get_rail_segment_signal and get_rail_segment_stop.
- Added LuaEntity::get_item_insert_specification.
- Added LuaEntity::get_line_item_position, LuaTransportLine::get_line_item_position and LuaTransportLine::line_length.
- Added LuaTransportLine::get_detailed_contents.
- Added LuaEntity::fluids_count read, get_fluid() and set_fluid().
- Removed ability of reading FluidWagon's fluid storage or FluidTurret's internal buffer fluid storage using LuaFluidBox.
- Added new controller type (remote), which is to build space platforms, so it allows ghost building but not any physical manipulation.
- Added LuaPlayer::physical_surface, physical_surface_index, physical_vehicle and physical_position read.
- LuaInventory::get_contents() will now return an array of {name = name, count = count, quality = quality}.
- Changed market price items to be defined as {name = name, count = count, quality = quality }.
- Added 8 new directions into defines.direction. If mods are storing any direction values in their storage, they will need to migrate them by multiplying by 2.
- LuaEntity::rotate no longer takes "spill_items", "enable_looted" nor "force" parameter.
- Removed LuaEntity::get_upgrade_direction() method.
- Changed on_built_entity event. Instead of stack/item, it passes consumed_items - modifiable stack of items used for the building.
- LuaTile::to_be_deconstructed() and related events can be given a force. If not given, it checks if tile is to be deconstructed by any force.
- Moved LuaItemPrototype::mapper_count property to LuaItemCommon.
- Renamed LuaLogisticContainerControlBehavior::circuit_mode_of_operation into circuit_exclusive_mode_of_operation.
- Added LuaCustomEventPrototype type and LuaGameScript::custom_event_prototypes read for the custom event prototypes.
- Added on_achievement_gained event.
- Added on_undo_applied event.
- LuaBootstrap::raise_event()'s "event" parameter now also accepts event names as string as alternative to their numerical IDs. The event names are needed to raise custom events.
- LuaBootstrap::on_event()'s "event" parameter now accepts event names for built-in events too, in addition to for custom inputs and the new custom events.
- Added new attribute "icon_selector" to LuaGuiElement::add() for creating textfields and text-boxes with the icon selector button.
- Removed __self from the LuaObjects. Intended way of checking if an object is a lua object is to check type is userdata.
- Changed LuaForce::evolution_factor, evolution_factor_by_pollution, evolution_factor_by_time and evolution_factor_by_killing_spawners to get_* and set_* methods.
- Type of LuaObjects is now "userdata" instead of "table".
- Added defines.wire_connector_id.
- Added LuaEntity::get_wire_connector and LuaEntity::get_wire_connectors.
- Added LuaWireConnector.
- Added LuaRecipePrototype::hide_from_signal_gui.
- Removed LuaEntity::circuit_connected_entities, LuaEntity::circuit_connection_definitions and LuaEntity::copper_connection_definitions.
- Removed LuaEntity::neighbours support for electric poles and power switches.
- Removed LuaEntity::connect_neighbour and LuaEntity::disconnect_neighbour.
- LuaCircuitNetwork is now binding to WireConnectorID. Removed LuaCircuitNetwork::circuit_connector_id. Added LuaCircuitNetwork::wire_connector_id.
- LuaEntity::get_circuit_network and LuaControlBehavior::get_circuit_network now require exactly 1 parameter: wire_connector_id.
- Replaced LuaEntity::get_merged_signal with LuaEntity::get_signal and LuaEntity::get_merged_signals with LuaEntity::get_signals. They no longer take circuit_connector_id but wire_connector_id.
- Removed defines.circuit_connector_id.
- Electric pole created through LuaSurface::create_entity can be requested to not auto connect.
- Replaced LuaFlowStatistics::get_flow_count parameter "bool input" with "string category" to reflect the addition of the "storage" category.
- Added LuaFlowStatistics::set_storage_count() and get_storage_count() methods.
- Added LuaFlowStatistics::storage_counts read.
- Removed LuaForce::item_production_statistics, fluid_production_statistics, kill_count_statistics and entity_build_count_statistics reads.
- Added LuaForce::get_item_production_statistics(), get_fluid_production_statistics(), get_kill_count_statistics() and get_entity_build_count_statistics() methods.
- Removed LuaGameScript::pollution_statistics read.
- Added LuaGameScript::get_pollution_statistics() method.
- Unified the way logistic filters are accessed, removed specific character/spidertron logistic filter methods, and all is done through get_logistic_point and get_section.
- Added LuaControl::get_requester_point() method.
- Removed LuaControl::clear_vehicle_logistic_slot, get_vehicle_logistic_slot, set_vehicle_logistic_slot, clear_personal_logistic_slot, get_personal_logistic_slot and set_personal_logistic_slot.
- Removed LuaEntity::clear_request_slot(), get_request_slot() and set_request_slot() methods.
- Removed LuaEntity::request_slot_count read.
- Added LuaLogisticSection.
- Added LuaLogisticPoint::get_section(), add_section() and remove_section() methods.
- Added LuaLogisticPoint::enabled read/write.
- Added LuaLogisticNetwork::network_id read.
- Added LuaRailEnd.
- Added LuaEntity::get_rail_end.
- Removed LuaTrain::front_rail, back_rail, rail_direction_from_front_rail, rail_direction_from_back_rail. They are replaced with LuaTrain::get_rail_end.
- Added LuaFluidBox::add_linked_connection(), remove_linked_connection(), get_linked_connection() and get_linked_connections() methods.
- Renamed LuaFluidBox::get_fluid_system_id() to get_fluid_segment_id().
- Renamed LuaFluidBox::get_fluid_system_contents() to get_fluid_segment_contents().
- Removed LuaFluidBox::get_flow() method.
- Added LuaPlayer::land_on_planet() method.
- Added LuaPlayer::enter_space_platform() and leave_space_platform() method.
- Added LuaPlayer::display_density_scale read.
- Removed LuaEntityPrototype::collision_mask_with_flags, LuaTilePrototype::collision_mask_with_flags and LuaDecorativePrototype::collision_mask_with_flags. Respective collision_mask returns mask with flags instead.
- Added LuaSurface::global_effect read/write.
- Removed LuaTechnology::effects, use LuaTechnologyPrototype::effects instead.
- Added LuaAirbornePollutantPrototype.
- Removed LuaNoiseLayerPrototype.
- Removed LuaItemPrototype::limitations and LuaItemPrototype::limitation_message_key reads.
- Removed LuaGameScript::get_active_entities_count() method.
- Removed LuaGameScript::count_pipe_groups() method.
- Removed LuaForce::zoom_to_world_* properties.
- Removed LuaForce::research_queue_enabled read/write.
- Removed LuaGuiElement::get_slider_discrete_slider(), set_slider_discrete_slider(), and discrete_slider.
- Removed LuaGuiElement::clear_and_focus_on_right_click, it is now always true.
- Removed LuaEntity::text.
- Removed LuaPlayer::log_active_entity_chunk_counts() and log_active_entity_counts() methods.
- Removed LuaAutoplaceControl::control_order since it was a duplicate of ::order.
- CircuitCondition passed to or given by LuaControlBehavior no longer uses the "condition" table, condition should be given directly.
- Renamed LuaItemStack::blueprint_icons into preview_icons.
- Added LuaTrainManager available through LuaGameScript::train_manager (read).
- Added LuaTrainManager::get_trains. Removed LuaSurface::get_trains and LuaForce::get_trains.
- Added LuaTrainManager::get_train_stops. Removed LuaSurface::get_train_stops, LuaForce::get_train_stops and LuaGameScript::get_train_stops.
- Added snap_to_grid to LuaSurface::create_entity() and LuaControl::teleport().
- Added LuaRenderObject. All LuaRendering methods for manipulating object selected by id were moved to LuaRenderObject.
- Added LuaSurface::localised_name read/write.
- Moved LuaGameScript::get_train_by_id into LuaTrainManager::get_train_by_id.
- Added LuaRecord representing records in the blueprint library.
- Added LuaPlayer::blueprints read.
- Added LuaGameScript::blueprints read.
- LuaGameScript::print, LuaPlayer::print, LuaSurface::print and LuaForce::print no longer accept Color as a second parameter.
- Changed permission related events to also fire when mods edit permissions.
- Changed LuaForce::ghost_time_to_live to LuaForce::create_ghost_on_entity_death bool read/write.
- Renamed on_entity_destroyed event into on_object_destroyed.
- Renamed LuaBootstrap::register_on_entity_destroyed into LuaBootstrap::register_on_object_destroyed.
- Removed help() method from every Factorio Lua object.
- Removed LuaObject::isluaobject.
- Renamed LuaUnitGroup into LuaCommandable. Renamed LuaCommandable::group_number into LuaCommandable::id.
- Added LuaEntity::commandable read. LuaEntity::unit_group moved to LuaCommandable::parent_group. LuaEntity::spawner moved to LuaCommandable::spawner.
- Removed LuaEntity::set_command, set_distraction_command, command, distraction_command and moving.
- Added LuaEquipment::quality read.
- Added LuaEquipment::to_be_removed read.
- Added LuaEquipment::ghost_prototype, ghost_type and ghost_name read.
- Added LuaEquipmentGrid::revive() method.
- Added quality and ghost parameters to LuaEquipmentGrid::put() method.
- Added search_ghosts parameter to LuaEquipmentGrid::find() method.
- Added LuaEquipmentGrid::order_removal() and cancel_removal() methods.
- Added LuaEquipmentGrid::entity_owner and player_owner read.
- Changed LuaEquipmentGrid::generator_energy read to LuaEquipmentGrid::get_generator_energy() method.
- Added LuaPrototypeBase as the common superclass for all Lua*Prototype classes.
- Added LuaItem and LuaItemCommon. LuaItemCommon is the common superclass for LuaItem and LuaItemStack.
- Moved LuaControl::get_blueprint_entities to LuaItemCommon and LuaRecord.
- Added LuaUndoRedoStack available through LuaPlayer::undo_redo_stack (read).
- Added player and undo_index parameters for undo queue to LuaSurface::set_tiles() method.
- Added player and item_index parameters for undo queue to LuaEntity::destroy() method.
- Added item_index parameter for undo queue to LuaSurface::cancel_deconstruct_area() method.
- Added item_index parameter for undo queue to LuaSurface::create_entity() method.
- Added item_index parameter for undo queue to LuaEntity::order_upgrade() method.
- Added item_index parameter for undo queue to LuaEntity::order_deconstruction() method.
- Added super_forced parameter to cancel_deconstruct_area and deconstruct_area in LuaSurface, LuaRecord and LuaItemCommon.
- Added quality condition to count_entities_filtered and find_entities_filtered methods in LuaSurface.
- Added has_double_hidden_tile boolean to count_tiles_filtered and find_tiles_filtered methods in LuaSurface.
- Added LuaSurface::set_property() and get_property() methods.
- Added LuaSurface::set_double_hidden_tile() and get_double_hidden_tile() methods.
- Added LuaTile::double_hidden_tile read.
- Added LuaSurface::execute_lightning() method.
- Added max_gap_size and max_attack_distance to LuaSurface::request_path() method.
- Added LuaSurface::create_global_electric_network() and destroy_global_electric_network() methods.
- Added LuaSurface::has_global_electric_network read.
- Added LuaSurface::platform read.
- Added LuaSurface::pollutant_type read.
- Added LuaSurface::deletable read.
- Added LuaRecipe::productivity_bonus read/write.
- Added LuaNamedNoiseFunction.
- Added LuaSpacePlatform and LuaPlanet.
- Added LuaEntity::custom_status read/write.
- Added LuaEntity::use_filters read/write.
- Added LuaEntity::name_tag read/write.
- Added LuaEntity::get_priority_target() and set_priority_target() methods.
- Added LuaEntity::ignore_unprioritised_targets read/write.
- Changed LuaEntity::electric_output_flow_limit and electric_input_flow_limit read to get_electric_output_flow_limit() and get_electric_input_flow_limit() methods.
- Added quality parameter to LuaEntity::set_recipe() method.
- Added LuaEntity::combinator_description read/write.
- Added LuaEntity::mining_drill_filter_mode read/write.
- Added LuaEntity::tick_grown read/write.
- Added LuaEntity::quality read.
- Added LuaEntity::always_on read/write.
- Renamed LuaEntity::electric_emissions to electric_emissions_per_joule.
- Added LuaEntity::copy_color_from_train_stop read/write.
- Added LuaEntity::train_stop_priority read/write.
- Added LuaEntity::rail_layer read.
- Added LuaEntity::mirroring read/write.
- Added LuaEntity::crane_grappler_destination and crane_grappler_destination_3d write.
- Added LuaEntity::crane_destination and crane_destination_3d read/write.
- Added LuaEntity::artillery_auto_targeting read/write.
- Added LuaEntity::robot_order_queue read.
- Added LuaItemCommon::owner_location read.
- Added LuaForce::unlock_space_location(), lock_space_location() and is_space_location_unlocked() methods.
- Added LuaForce::create_space_platform() method.
- Added LuaForce::unlock_space_platforms(), lock_space_platforms() and is_space_platforms_unlocked() methods.
- Added LuaForce::set_surface_hidden() and get_surface_hidden() methods.
- Added LuaForce::unlock_quality(), lock_quality() and is_quality_unlocked() methods.
- Added LuaForce::copy_from() and copy_chart() methods.
- Added LuaForce::platforms read.
- Renamed LuaForce::stack_inserter_capacity_bonus to bulk_inserter_capacity_bonus.
- Added LuaForce::beacon_distribution_modifier and belt_stack_size_bonus read/write.
- Added LuaSimulation available through LuaGameScript::simulation (read).
- Added LuaGameScript::get_entity_by_unit_number() method.
- Added LuaGameScript::set_win_ending_info() and set_lose_ending_info() methods.
- Added LuaGameScript::planets read.
- Added LuaGameScript::get_vehicles.
- Added LuaSurface::planet read.
- Removed LuaEntityPrototype::max_health. Added LuaEntityPrototype::get_max_health(quality?). Added LuaEntity::max_health read.
- Changed on_cutscene_waypoint_reached event's parameter "waypoint_index" to not be zero indexed.
- Added LuaPlayer::clear_local_flying_texts() method.
- Added LuaSurface::clear_hidden_tiles.

### Bugfixes

- Fixed a crash related to fast-replacing a belt during its created trigger.
- Fixed that character entities couldn't be teleported between surfaces by script directly.
- Fixed mining a tree in multiplayer would make its stump appear with a delay, only after the mining action propagated to the game state.
- Fixed that joining a server while auto-save is running would lead to a deadlock on the client side.
- Fixed reading LuaItemStack::entity_label would return nil when label was set. ( more )
- Fixed reading object_name of LuaTransportBeltControlBehavior would return incorrect value.
- Fixed that linux would not release memory after deleting blueprint library contents. ( more )
- Fixed that enemies could not retaliate to the original cause of some forms of damage.
- Fixed that joining a multiplayer server did not work if the save was larger than 4 gigabytes. ( more )
- Fixed a desync when clicking the "continue" button on the game-won screen. ( more )
- Fixed that mod-defined additional paste entities did not work for splitters. ( more )
- Fixed LuaPlayerBuiltEntityEventFilter ghost_name did not filter tile ghost inner names. ( more )
- Fixed that driving vehicles in the map editor would not open gates. ( more )
- Fixed disabling inserter's circuit condition could activate inserter when it was still requested to say disabled. ( more )
- Fixed a desync when setting tiles during chunk generation that resulted from force_generate_chunk_requests(). ( more )
- Fixed that underground pipe dragging would not use the correct distance if the underground fluidbox connections were not in the center of the entity.
- Fixed potential audio clicks when a filter is used. ( more )
- Improved performance of the upgrade planner GUI when there are many entity prototypes. ( more )
- Fixed plural form localisation of decimal and negative numbers. ( more )
- Fixed silent global programmable speaker sounds taking up audio resources. ( more )
- Fixed single water tile edging weird on border of 2 land tiles. ( more )
- Fixed a desync when changing PathFinderMapSettings cache sizes at runtime. ( more )
- Fixed renaming train stop could skip updating train schedules if there were train stops with same name on other surfaces. ( more )
- Fixed that labs didn't work correctly around high speeds and low science pack stack sizes. ( more )
- Fixed --load-scenario would force map size to be 50x50. ( more )
- Fixed Gui double-click speed was very fast and not respecting the system settings. ( more )
- Fixed that escape didn't work to dismiss the sync mods with save GUI. ( more )
- Fixed setting up blueprint from library would not set the label. ( more )
- Fixed that pickup inserters would not go to sleep when there was a rolling stock present even if it was not valid to interact with. ( more )
- Fixed boilers would not account for output fluid heat capacity when calculating the amount of output fluid produced. ( more )
- Fixed disconnecting lamp from circuit network would disable control behavior even if it was still connected to logistic network. ( more )
- Fixed filter burner inserter was not able to pickup fuel from belt when fuel is not accepted by filters. ( more )
- Fixed burner inserter could get stuck when fueling cycle was interrupted by a player. ( more )
- Fixed burner mining drill could drop items on wrong side of transport belt if the drill was not facing north. ( more )
- Fixed it was not possible to change rail's chart color. ( more )
- Fixed cursor split from quickbar would not round up. ( more )
- Fixed that zoom limits were appearing too small on Apple Retina displays. ( more )
- Fixed that building entities close to vertical rails would trigger train visualisation from train stop rendering even if it goes away from cursor.
- Fixed pressing R while in rail planner would set wrong initial building direction.
- Fixed rolling stock ghost revive was possible when there are diagonal rail ghosts not yet built which could make a train to not connect properly.
- Fixed the wrong technology level shown on the icon in the currently selected technology.
- Fixed upgrading connected underground belt ghost in latency state.
- Fixed that lights of trains on other surfaces would be rendered on selected surface when doing a screenshot.
- Fixed that for train "Fluid count" conditions, a fractional fluid amount below 1.0 would already be considered equal to 0. Amounts between 0.0 and 1.0 are now rounded up instead. The same logic now also applies to fluid storage tanks reading their contents and pumpjacks reading their expected resource yield.
- Fixed undoing tile deconstruction after it was cancelled and undone before.
- Fixed that upgrade tasks might not be processed by mobile roboport as fast as other types of tasks. ( more )
- Fixed responsibility of toggle shortcut buttons in multiplayer.
- Fixed upgrading electric pole would disconnect a power switch.
- Fixed several problems related to character walking and terrain building in latency hiding mode.
- Fixed characters being able to 'jump over' obstacles when moving fast enough.
- Fixed upgraded-modules undo action not saving or loading entity tags.
- Fixed cutscene controller index could go out of bounds and grow indefinitely. ( more )
- Fixed that rocket silo didn't wait for the stack to be full when autolaunching.
- Fixed the 'Error loading mods' window did not allow copying the error message. ( more )
- Fixed the shortcut bar GUI not shrinking when GUI scale is decreased. ( more )
- Fixed furnaces with fluidboxes defined with fluid filters would not have fluid filters. ( more )
- Fixed that trains didn't show wheels in blueprint, even when the rails are present.
- Fixed that trains in blueprints didn't save the connections, so close individual rolling stocks could get connected after the blueprint placement.
- Fixed that assembling machine would not complain when fixed_recipe was specified that cannot be crafted by given machine. ( more )
- Fixed building a blueprint with entities buildable off grid only could fail to center the blueprint properly. ( more )
- Fixed closing quickbar select page gui would not close when using confirm gui binding. ( more )
- Fixed rotating off-center bounding boxes. ( more )
- Fixed long train stop names causing shorter names to be clipped on subsequent selection. ( more )
- Fixed that inserters could sleep incorrectly if pointed at furnaces with fluid inputs. ( more )
- Fixed item stack sizes could cause issues with crafting machine's overloaded status. ( more )
- Fixed that extreme speed assembling machines would calculate productivity incorrectly. ( more )
- Fixed that robots waiting to charge were stuck after removing all charging spots of that roboport prototype.
- Fixed that equipment in armor not currently worn would still apply drain logic. ( more )
- Fixed that worms wouldn't target construction robots correctly in some cases. ( more )
- Fixed that LuaEntity::copy_settings() didn't respect normal copy logic. ( more )
- Fixed that require() would allow files from other drives. ( more )
- Changed burner energy sources without burnt result inventory to void burnt results instead of getting stuck. ( more )
- Fixed wrong hierarchy order of blueprint book nesting when previewing entities in the world.
- Fixed that rich-text used in train stops and train schedule weren't migrated.
- Fixed tiles in the rocket rush lobby could be deconstructed. ( more )
- Fixed translation requests failing because of empty parameters. ( more )

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
