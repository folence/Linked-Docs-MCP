---
title: Console - Factorio Wiki
source: https://wiki.factorio.com/Console
scraped_at: 2025-10-21 14:29:53
tags: [web, documentation]
---

# Console - Factorio Wiki

**Source:** [https://wiki.factorio.com/Console](https://wiki.factorio.com/Console)

The console is Factorio's in-game command-line interface. See command line parameters for the command line interface of the Factorio executable.

The in-game console can be used for:

- Chatting with other players
- Occasional status updates
- Running commands / scripts / cheats

There are three types of commands:

- Normal - Display information about the game and customize your experience.
- Multiplayer - Message filtering, banning users, etc.
- Scripting/Cheating - Run small Lua scripts (but they disable achievements for the save game )

## Contents

- 1 Using the console
- 2 Normal commands
- 3 Multiplayer commands
- 4 Scripting and cheat commands
- 5 Basic example scripts 5.1 Use it as calculator 5.2 Zoom beyond normal bounds 5.3 Mine faster 5.4 Craft faster 5.5 Unlock and research all technologies 5.6 Unresearch all technologies 5.7 Reset your force 5.8 Always show rail block visualization 5.9 Set all trains to Automatic mode
- 6 Inventory manipulation scripts 6.1 Cheat mode 6.2 Refill resources (refill oil, iron etc.) 6.3 Add items to the player's inventory 6.4 Increase player inventory slots
- 7 World manipulation scripts 7.1 Reveal the map around the player 7.2 Hide revealed map 7.3 Reveal all generated map 7.4 Delete chunks 7.5 Delete unrevealed chunks 7.6 Turn off night 7.7 Change game speed 7.8 Freeze time 7.9 Remove all pollution 7.10 Completely turn off pollution 7.11 Add a lot of pollution 7.12 Where speakers are, who placed them 7.13 Disable friendly fire for your force 7.14 Add new resource patch 7.15 Remove resources around the player 7.16 Add new oil patch 7.17 Add new water patch 7.18 Regenerate resources 7.19 Count entities 7.20 Turn off cliff generation 7.21 Remove all cliffs 7.22 Delete all decoratives 7.23 Change map generation settings 7.24 Making a structure indestructible 7.25 Connect linked belts 7.26 Deactivate cars and tanks
- 8 Enemy/evolution scripts 8.1 Set evolution factor 8.2 Disable time-based evolution & increases pollution-based evolution 8.3 Kill all biters on the "enemy" force 8.4 Kill all enemies 8.5 Kill all nearby enemies 8.6 Enable/Disable peaceful mode 8.7 Enable/Disable biter expansion 8.8 Prevent biters being on newly generated chunks
- 9 Player character scripts 9.1 Get player position 9.2 Teleport player 9.3 Enable god mode 9.4 Enable long reach 9.5 Find player corpses 9.6 Run faster
- 10 Research scripts 10.1 Enable faster research 10.2 Research specific technologies 10.3 Unresearch specific technologies 10.4 Enabling specific recipes 10.5 Enable all recipes 10.6 Resetting technology effects to default 10.7 Enable ghosts for destroyed entities
- 11 Modding tools 11.1 Access a mod's data 11.2 Print to console the tile under the player 11.3 Write all researched technologies to file 11.4 Write all enabled recipes to file 11.5 Write mod list to file 11.6 Exporting production statistics
- 12 History
- 13 See also

### Using the console

The console display can be toggled with the GRAVE key ( ` ). This is the key located to the left of the 1 key, above Tab .

You can customize the keys via Settings menu → Controls → Toggle chat (and Lua console) .
When the console is open, you'll see a blinking cursor at the bottom of the screen; type your message or command and hit Return to send it (this will also close the console).
Documentation about message and command prefixes can be found further down this page.

The console supports rich text tags. These tags are useful for sharing blueprints, marking map locations in chat or adding icons to map markers and train stations. Ctrl + Alt-clicking the map or ground will automatically insert a GPS tag and post it into the console. Shift-clicking most things with the console open will insert a tag for that thing into the console.

When the console is closed, only the most recent messages/commands will be displayed, but they will gradually fade away (opening the console will immediately re-display all recent messages).
Note that by default, all executed commands are made visible to all users. The fade-out time can be changed via Settings menu → Interface → Chat message delay .

The console can be cleared with the /clear command.

Use the ↑ and ↓ keys to scroll through the console history. The Tab key provides intelligent code completion on commands, options and player names.

## Normal commands

| Command | Example | Description | Admin only |
| /alerts <enable/disable/mute/unmute> <alert> | /alerts disable turret_fire | Enables, disables, mutes, or unmutes the given alert type. Available alerts: entity_destroyed, entity_under_attack, not_enough_construction_robots, no_material_for_construction, not_enough_repair_packs, platform_tile_building_blocked, turret_out_of_ammo, turret_fire, custom, no_storage, train_out_of_fuel, train_no_path, no_platform_storage, collector_path_blocked, unclaimed_cargo, no_roboport_storage, pipeline_overextended. | No |
| /clear | /clear | Clears the console. | No |
| /color <color> | /color 20 255 255 | Changes your color. Can either be one of the pre-defined colors or RGB value in the format of “# # #”. Available colors: default, red, green, blue, orange, yellow, pink, purple, white, black, gray, brown, cyan, acid. | No |
| /evolution | /evolution | Prints info about the alien evolution factor. | No |
| /help [command] | /help | Prints a list of available commands, the optional argument can specify the command that should be described. | No |
| /h [command] | /h | Same as /help. | No |
| /mute-programmable-speaker <mute/unmute> <local/everyone> | /mute-programmable-speaker mute local | Mutes or unmutes the global sounds created by the Programmable Speaker. Use “local” to mute just the local client. Admins can use “everyone” to mute the sounds for everyone on the server. | No |
| /perf-avg-frames <number> | /perf-avg-frames 100 | Number of ticks/updates used to average performance counters. Default is 100. Value of 5-10 is recommended for fast convergence, but numbers will jitter more rapidly. | No |
| /permissions | /permissions | Opens the permissions GUI. | Yes |
| /permissions <action> <parameters> | /permissions add-player DeveloperGroup kovarex | Available actions are add-player <group> <player>, create-group <name>, delete-group <group>, edit-group <group> <input_action> <true/false>, get-player-group <player>, remove-player <group> <player>, rename-group <group> <new_name> and reset | Yes |
| /reset-tips | /reset-tips | Resets the state of the tips and tricks as if the game was just started for the first time. | No |
| /screenshot [x resolution] [y resolution] [zoom] | /screenshot | Takes a screenshot with the GUI hidden, centered on the player. It is saved in the "script-output" subfolder of your User data directory . Resolution is optional and defaults to the current window size. Zoom is optional and defaults to 1. | No |
| /seed | /seed | Prints the starting map seed. | No |
| /time | /time | Prints info about how old the map is. | No |
| /toggle-action-logging | /toggle-action-logging | Toggles logging all input actions performed by the game. This value isn’t persisted between game restarts and only affects your local game in multiplayer sessions. | Yes |
| /toggle-heavy-mode | /toggle-heavy-mode | Used to investigate desyncs . Will slow down the game and make multiplayer unplayable. | Yes |
| /unlock-shortcut-bar | /unlock-shortcut-bar | Unlocks all shortcut bar items, including blueprint string import, copy & paste, deconstruction and upgrade planner. | No |
| /unlock-tips | /unlock-tips | Unlocks all tips and tricks entries. | No |
| /version | /version | Prints the current game version. | No |

## Multiplayer commands

| Command | Example | Description | Admin only |
| <message> | Hello team! | Console input that does not start with / is shown as a chat message to your team. | No |
| /admin | /admin | Opens the player management GUI. | Yes |
| /admins | /admins | Prints a list of game admins. | No |
| /ban <player> <reason> | /ban xTROLLx Throwing grenades in base | Bans the specified player. | Yes |
| /bans | /bans | Prints a list of banned players. | No |
| /banlist <add/remove/get/clear> <player> | /banlist get | Adds or removes a player from the banlist. Same as /ban or /unban. | No |
| /config | /config | Opens the server configuration GUI. | Yes |
| /config <get/set> <option> <value> | /config set password hunter2 | Gets or sets various multiplayer game settings. Available configs are: afk-auto-kick, allow-commands, allow-debug-settings, autosave-interval, autosave-only-on-server, ignore-player-limit-for-returning-players, max-players, max-upload-speed, only-admins-can-pause, password, require-user-verification, visibility-lan, visibility-public. The units for the options afk-auto-kick and autosave-interval are in minutes. | Yes |
| /delete-blueprint-library <player> | /delete-blueprint-library everybody confirm | Deletes the blueprint library storage for the given offline player from the save file. Enter “everybody confirm” to delete the storage of all offline players. | Yes |
| /demote <player> | /demote AzureDiamond | Demotes the player from admin. | Yes |
| /ignore <player> | /ignore Cthon98 | Prevents the chat from showing messages from this player. Admin messages are still shown. | No |
| /ignores | /ignores | Prints a list of ignored players. | No |
| /kick <player> <reason> | /kick xTROLLx Throwing grenades in base | Kicks the specified player. | Yes |
| /mute <player> | /mute Cthon98 | Prevents the player from saying anything in chat. | Yes |
| /mutes | /mutes | All players that are muted (can’t talk in chat). | No |
| /open <player> | /open AzureDiamond | Opens another player’s inventory. | Yes |
| /o <player> | /o AzureDiamond | Same as /open. | Yes |
| /players [online/o/count/c] | /players | Prints a list of players in the game. (parameter online/o, it prints only players that are online, count/c prints only count) | No |
| /p [online/o/count/c] | /p o c | Same as /players. | No |
| /promote <player> | /promote AzureDiamond | Promotes the player to admin. | Yes |
| /purge <player> | /purge Cthon98 | Clears all the messages from this player from the chat log. | Yes |
| /reply <message> | /reply oh, really? | Replies to the last player that whispered to you. | No |
| /r <message> | /r oh, really? | Same as /reply. | No |
| /server-save | /server-save | Saves the game on the server in a multiplayer game. | Yes |
| /shout <message> | /shout Hello world! | Sends a message to all players including other forces. | No |
| /s <message> | /s Hello world! | Same as /shout. | No |
| /swap-players <player> [player] | /swap-players AzureDiamond | Swaps your character with the given player’s character, or if two players are given swaps the two player characters. | Yes |
| /unban <player> | /unban xTROLLx | Unbans the specified player. | Yes |
| /unignore <player> | /unignore Cthon98 | Allows the chat to show messages from this player. | No |
| /unmute <player> | /unmute Cthon98 | Allows the player to talk in chat again. | Yes |
| /whisper <player> <message> | /whisper AzureDiamond that's what I see | Sends a message to the specified player. | No |
| /w <player> <message> | /w AzureDiamond that's what I see | Same as /whisper. | No |
| /whitelist <add/remove/get/clear> [player] | /whitelist get | Adds or removes a player from the whitelist, where only whitelisted players can join the game. Enter nothing for “player” when using “get” to print a list of all whitelisted players. An empty whitelist disables the whitelist functionality allowing anyone to join. | No |

## Scripting and cheat commands

| Command | Description |
| /cheat [all/<planet-name>/<platform-name>/off] | Researches all technologies and enables cheat mode (allowing free crafting of any item). Using the all option also gives the player some additional items. Specifying a planet-name or platform-name also moves the player to the origin of the specified planet or platform. Using the off option turns cheat mode off. |
| /command <command> | Executes a Lua command (if allowed). |
| /c <command> | Executes a Lua command (if allowed). |
| /editor | Toggles the map editor. |
| /measured-command <command> | Executes a Lua command (if allowed) and measures time it took. |
| /mc <command> | Executes a Lua command (if allowed) and measures time it took. |
| /silent-command <command> | Executes a Lua command (if allowed) without printing it to the console. |
| /sc <command> | Executes a Lua command (if allowed) without printing it to the console. |

This is a very powerful feature, which also allows cheating, and as such achievements will be permanently disabled for the save as soon as you use a script command.

## Basic example scripts

### Use it as calculator

```
/cgame.player.print(1234*5678)
```

### Zoom beyond normal bounds

Note that zooming too far out can cause performance hits. Be careful.

```
/cgame.player.zoom=0.1
```

In freeplay, the farthest you can zoom out is 0.3. In the map editor, it is 0.1. Smaller zoom values will be clamped.

### Mine faster

```
/cgame.player.force.manual_mining_speed_modifier=1000
```

### Craft faster

```
/cgame.player.force.manual_crafting_speed_modifier=1000
```

### Unlock and research all technologies

```
/cgame.player.force.research_all_technologies()
```

Undo this with the command in the next section.

Note: Specific technologies can be researched using the map editor by shift clicking the "start research" button on the technology GUI.

### Unresearch all technologies

This does not reset manually applied bonuses

```
/cfor_,techinpairs(game.player.force.technologies)dotech.researched=falseend
```

Note: Specific technologies can be unresearched using the map editor by clicking the "un-research" button on the technology GUI.

### Reset your force

This resets all data for your force, including kill and production statistics, technologies, bonuses and charting status.

```
/cgame.player.force.reset()
```

### Always show rail block visualization

Permanently show the rail block visualization instead of only when holding a rail signal. Disable by replacing true with false.

```
/cgame.player.game_view_settings.show_rail_block_visualisation=true
```

### Set all trains to Automatic mode

Set all trains to automatic mode - for example after building them with a blueprint.

```
/cforkey,entinpairs(game.player.surface.find_entities_filtered{name="locomotive"})doent.train.manual_mode=falseend
```

## Inventory manipulation scripts

### Cheat mode

Allows for infinite free crafting. Disable by replacing true with false.

```
/cgame.player.cheat_mode=true
```

### Refill resources (refill oil, iron etc.)

While holding the cursor over a resource tile in-game:

```
/cgame.player.selected.amount=7500
```

Alternatively you can refill all resources in the map with the following command. Change ore.amount to the desired value.

```
/csurface=game.player.surfacefor_,oreinpairs(surface.find_entities_filtered({type="resource"}))doore.amount=10000end
```

### Add items to the player's inventory

Replace iron-plate with the internal name of the item desired.

```
/cgame.player.insert{name="iron-plate",count=100}
```

For instance, here's a stack of the god-mode energy system interface:

```
/cgame.player.insert{name="electric-energy-interface"}
```

There are several god-mode items available:

- infinity-chest
- infinity-pipe
- electric-energy-interface
- heat-interface

Add a powerful armor with equipment and some tools for construction:

```
/clocalplayer=game.playerplayer.insert{name="power-armor-mk2",count=1}localp_armor=player.get_inventory(5)[1].gridp_armor.put({name="fission-reactor-equipment"})p_armor.put({name="fission-reactor-equipment"})p_armor.put({name="fission-reactor-equipment"})p_armor.put({name="exoskeleton-equipment"})p_armor.put({name="exoskeleton-equipment"})p_armor.put({name="exoskeleton-equipment"})p_armor.put({name="exoskeleton-equipment"})p_armor.put({name="energy-shield-mk2-equipment"})p_armor.put({name="energy-shield-mk2-equipment"})p_armor.put({name="personal-roboport-mk2-equipment"})p_armor.put({name="night-vision-equipment"})p_armor.put({name="battery-mk2-equipment"})p_armor.put({name="battery-mk2-equipment"})player.insert{name="construction-robot",count=25}
```

Adding higher quality items looks like this:

```
/cgame.player.insert{name="iron-plate",quality="legendary",count=100}
```

### Increase player inventory slots

Gives 100 additional bonus inventory slots to your entire force. Used by the Toolbelt (research) .

```
/cgame.player.force.character_inventory_slots_bonus=100
```

## World manipulation scripts

### Reveal the map around the player

Reveals the map around the player, similar to a radar .

```
/clocalradius=150game.player.force.chart(game.player.surface,{{game.player.position.x-radius,game.player.position.y-radius},{game.player.position.x+radius,game.player.position.y+radius}})
```

or from start position

```
/clocalradius=150game.player.force.chart(game.player.surface,{{x=-radius,y=-radius},{x=radius,y=radius}})
```

Change 150 to the desired radius, higher values take longer.

### Hide revealed map

Hides all revealed chunks, inverted map revealing.

```
/clocalsurface=game.player.surfacelocalforce=game.player.forceforchunkinsurface.get_chunks()doforce.unchart_chunk({x=chunk.x,y=chunk.y},surface)end
```

### Reveal all generated map

Revels all of the generated map to the player's team.

```
/cgame.player.force.chart_all()
```

### Delete chunks

If much of the map is revealed, it increases the size of the save file. The following command cancels the generation of all chunks that are currently queued for generation and removes chunks outside a 32 chunks radius around 0,0. Note that this will remove player entities if there are any on these chunks.

```
/clocalsurface=game.player.surface;game.player.force.cancel_charting(surface);localchunk_radius=32;forchunkinsurface.get_chunks()doif(chunk.x<-chunk_radiusorchunk.x>chunk_radiusorchunk.y<-chunk_radiusorchunk.y>chunk_radius)thensurface.delete_chunk(chunk)endend
```

### Delete unrevealed chunks

This command deletes chunks that are not revealed by the player. Can be used after the command for hiding revealed map to delete the chunks not covered by radar.

```
/clocalsurface=game.player.surfacelocalforce=game.player.forceforchunkinsurface.get_chunks()doifnotforce.is_chunk_charted(surface,chunk)thensurface.delete_chunk(chunk)endend
```

### Turn off night

Enables eternal day.

```
/cgame.player.surface.always_day=true
```

### Change game speed

0.5 is half speed, 1 is default, 2 is double speed, etc. Minimum is 0.01. This can be used for a lot of things like when you know you will have to wait for long periods of time for something to complete. Increasing will decrease performance, be careful.

```
/cgame.speed=X
```

### Freeze time

Stops the advancement of the time. Unfreezes it if you by replace "true" with "false".

```
/cgame.player.surface.freeze_daytime=true
```

### Remove all pollution

```
/cgame.player.surface.clear_pollution()
```

### Completely turn off pollution

```
/cfor_,surfaceinpairs(game.surfaces)dosurface.clear_pollution()endgame.map_settings.pollution.enabled=false
```

### Add a lot of pollution

```
/cgame.player.surface.pollute(game.player.position,1000000)
```

### Where speakers are, who placed them

```
/clocalspeakers=game.player.surface.find_entities_filtered{force=game.player.force,type="programmable-speaker"}forkey,speakerinpairs(speakers)dogame.player.print(speaker.last_user.name.." placed a speaker at "..speaker.gps_tag)end
```

### Disable friendly fire for your force

```
/cgame.player.force.friendly_fire=false
```

### Add new resource patch

This creates a new 11×11 patch of resources, centered on the player character, where the ground is not water.
The patch it creates is perfectly square but it randomizes the amount similar to natural generation, with fewer ore at the edges and more ore in the center.
The default numbers result in a patch with 2500-3000 ore.

If you want a larger patch, change "local size = 5" to a larger number.
A larger patch will have exponentially more ore.
Entering a number above 30 is not recommended.

If you want a richer patch, change "local density = 10" to a larger number.
Entering a very large number shouldn't hurt anything but you probably don't need to go above 100.

To choose which resource is spawned, change "stone" near the bottom to "iron-ore", "copper-ore", "coal", or "uranium-ore".

```
/clocalsurface=game.player.surfacelocalore=nillocalsize=5localdensity=10fory=-size,sizedoforx=-size,sizedoa=(size+1-math.abs(x))*10b=(size+1-math.abs(y))*10ifa<bthenore=math.random(a*density-a*(density-8),a*density+a*(density-8))endifb<athenore=math.random(b*density-b*(density-8),b*density+b*(density-8))endifsurface.get_tile(game.player.position.x+x,game.player.position.y+y).collides_with("ground_tile")thensurface.create_entity({name="stone",amount=ore,position={game.player.position.x+x,game.player.position.y+y}})endendend
```

For more flexibility, the map editor can also be used to create/alter/remove resource patches.

### Remove resources around the player

Removes all resource patches from the ground in a 50 x 50 area around the player.

```
/clocalsurface=game.player.surfacelocalsize=50localpos=game.player.positionfor_,einpairs(surface.find_entities_filtered{area={{pos.x-size,pos.y-size},{pos.x+size,pos.y+size}},type="resource"})doe.destroy()end
```

### Add new oil patch

This creates 9 crude oil patches in a 3×3 square.

```
/cfory=0,2doforx=0,2dogame.player.surface.create_entity({name="crude-oil",amount=100000,position={game.player.position.x+x*7-7,game.player.position.y+y*7-7}})endend
```

or randomly without any collision:

```
/clocalposition=nilfori=1,9doposition=game.player.surface.find_non_colliding_position("crude-oil",game.player.position,0,i/2+1.5)ifpositionthengame.player.surface.create_entity({name="crude-oil",amount=100000,position=position})endend
```

### Add new water patch

This creates a small pond in a 4x2 square.

```
/clocalwaterTiles={}fory=2,4doforx=-2,2dotable.insert(waterTiles,{name="water",position={game.player.position.x+x,game.player.position.y+y}})endgame.player.surface.set_tiles(waterTiles)end
```

### Regenerate resources

For solid resources like iron, destroys all resource entities and creates resource entities as in the original map generation. For fluid resources like oil, sets the yield of all existing resource entities to the original amount. Regenerates resources on the entire surface.

```
/clocalsurface=game.player.surfacefor_,einpairs(surface.find_entities_filtered{type="resource"})doife.prototype.infinite_resourcethene.amount=e.initial_amountelsee.destroy()endendlocalnon_infinites={}forresource,prototypeinpairs(prototypes.get_entity_filtered{{filter="type",type="resource"}})doifnotprototype.infinite_resourcethentable.insert(non_infinites,resource)endendsurface.regenerate_entity(non_infinites)for_,einpairs(surface.find_entities_filtered{type="mining-drill"})doe.update_connections()end
```

### Count entities

Counts all entities whose name includes the string in local entity.

```
/clocalentity="belt"localsurface=game.player.surfacelocalcount=0forkey,entinpairs(surface.find_entities_filtered({force=game.player.force}))doifstring.find(ent.name,entity)thencount=count+1endendgame.player.print(count)
```

### Turn off cliff generation

Sets size to "none". Only effective on chunks that are generated after using this command. Use #Remove all cliffs to delete existing cliffs.

```
/clocalmgs=game.player.surface.map_gen_settingsmgs.cliff_settings.cliff_elevation_0=1024game.player.surface.map_gen_settings=mgs
```

### Remove all cliffs

Removes all cliffs existing cliffs from the world. Use #Turn off cliff generation to turn off cliff generation in new chunks.

```
/cfor_,vinpairs(game.player.surface.find_entities_filtered{type="cliff"})dov.destroy()end
```

### Delete all decoratives

Delete the decoratives that can be found in the world.

```
/cgame.player.surface.destroy_decoratives({})
```

### Change map generation settings

This allows to change the map generation settings for new chunks; it does not alter already generated chunks. Deleted chunks are affected by the setting change because they are newly generated when they get explored again.

To change resource generation settings, replace "iron-ore" with the resource that should be changed and replace "very-high" with the desired MapGenSize in the following command. Replace "iron-ore" with "enemy-base" to change the enemy base generation settings.

```
/clocalsurface=game.player.surfacelocalresource="iron-ore"localmgs=surface.map_gen_settingsmgs.autoplace_controls[resource].size="very-high"mgs.autoplace_controls[resource].frequency="very-high"mgs.autoplace_controls[resource].richness="very-high"surface.map_gen_settings=mgs
```

To change water generation settings, replace "very-high" with the desired MapGenSize in the following command.

```
/clocalsurface=game.player.surfacelocalmgs=surface.map_gen_settingsmgs.water="very-high"--[[ size]]mgs.terrain_segmentation="very-high"--[[ frequency]]surface.map_gen_settings=mgs
```

### Making a structure indestructible

This makes it impossible for an entity to be damaged or killed, e.g. by biters. Hover over the entity and then run:

```
/cgame.player.selected.destructible=false
```

### Connect linked belts

If there exist at least two linked belts , and one of them has the "Entity tag" in , and another linked belt has the "Entity tag" out , then the following command should link these two linked belts.

```
/clocali=game.get_entity_by_tag('in')localo=game.get_entity_by_tag('out')i.linked_belt_type='input'o.linked_belt_type='output'i.connect_linked_belts(o)
```

### Deactivate cars and tanks

The car and tank can be used like larger, 2x3 chests, but doing this at a large scale can have a negative performance impact. Deactivating them reduces their performance impact, though it also prevents them from being driven or moved by belts.

Deactivate selected car or tank (hover with mouse then enter command):

```
/cgame.player.selected.active=false
```

Deactivate all cars and tanks on surface:

```
/cfor_,vinpairs(game.player.surface.find_entities_filtered{type="car"})dov.active=falseend
```

## Enemy/evolution scripts

### Set evolution factor

Ranges from 0 (new game) to 1.

```
/cgame.forces["enemy"].set_evolution_factor(X,game.player.surface)
```

### Disable time-based evolution & increases pollution-based evolution

```
/cgame.map_settings.enemy_evolution.time_factor=0/cgame.map_settings.enemy_evolution.pollution_factor=game.map_settings.enemy_evolution.pollution_factor*2
```

The "2" at the end of the last command will double the default pollution factor. You can substitute another number to increase (or decrease) the pollution factor further.

### Kill all biters on the "enemy" force

Note that this will kill only mobile units, spawners will not be killed.

```
/cgame.forces["enemy"].kill_all_units()
```

### Kill all enemies

This will kill all biters, bases and worms. Anything that is an enemy will be completely destroyed. This only affects enemies in the generated world, so any unexplored parts of the map which still need to be generated will still have enemies. You can prevent biters being on newly generated chunks if desired.

```
/clocalsurface=game.player.surfaceforkey,entityinpairs(surface.find_entities_filtered({force="enemy"}))doentity.destroy()end
```

### Kill all nearby enemies

This will kill all biters, bases and worms in a configurable radius. The default, 250 tiles, is about two zoomed-out screen widths on full HD. After destruction, it shows how many objects were destroyed.

```
/clocalsurface=game.player.surfacelocalpp=game.player.positionlocalcnt=0forkey,entityinpairs(surface.find_entities_filtered({force="enemy",radius=250,position=pp}))docnt=cnt+1entity.destroy()endgame.player.print(cnt)
```

### Enable/Disable peaceful mode

Enabling peaceful mode prevents biter attacks until provoked. Substitute true for false to disable. Already existing biters are not affected by this command so attacks could continue for a while after activating peaceful mode.

```
/cgame.player.surface.peaceful_mode=true
```

### Enable/Disable biter expansion

Biter expansion allows biters to create new nests, it is enabled by default. Substitute true for false to disable.

```
/cgame.map_settings.enemy_expansion.enabled=true
```

### Prevent biters being on newly generated chunks

On newly generated chunks no biters will be present, however all current biters will remain unaffected. Equivalent of setting the Enemy Base Size to None under the Terrain settings during map generation but achieved mid game by changing map generation settings .

```
/clocalsurface=game.player.surfacelocalmgs=surface.map_gen_settingsmgs.autoplace_controls["enemy-base"].size="none"surface.map_gen_settings=mgs
```

Instead of the command, it is also possible to use a GUI in the map editor to changing map generation settings mid game. Access the map editor with /editor , go to the "Surfaces" tab and click "Edit map gen settings".

## Player character scripts

Commands concerning the player directly.

### Get player position

Prints coordinates of your current position.

```
/cgame.player.print(game.player.position)
```

### Teleport player

Moves the player to the specified location. You should be able to teleport to a specific player if you obtain their coordinates via them executing the previous command and giving them to you.

```
/cgame.player.teleport({X,Y})
```

To teleport to the world's origin, use 0,0.

To teleport to a different planet / surface, use:

```
/cgame.player.teleport({X,Y},'surface_name')
```

### Enable god mode

God mode removes your player character allowing you to fly over obstacles and take no damage.

Disassociate your controls from the character and destroy it:

```
/cgame.player.character.destroy()
```

To undo, spawn a player character. This will spawn a new character at the spawn point of the world, and connect your controls to it.

```
/cgame.player.create_character()
```

### Enable long reach

Enables long reach, which allows the player to build and interact with entities at a greater distance. The default reach is 10.

```
/clocalreach=10000game.player.force.character_build_distance_bonus=reachgame.player.force.character_reach_distance_bonus=reachgame.player.force.character_resource_reach_distance_bonus=reachgame.player.force.character_item_drop_distance_bonus=reach
```

### Find player corpses

Pings player corpses on the map.

```
/clocalfound_corpses=game.player.surface.find_entities_filtered{type="character-corpse"}for_,corpseinpairs(found_corpses)dolocalplayer=game.get_player(corpse.character_corpse_player_index)localname=playerandplayer.nameor"????"game.player.print(name.." --> "..corpse.gps_tag)end
```

### Run faster

```
/cgame.player.character_running_speed_modifier=3
```

## Research scripts

### Enable faster research

```
/cgame.player.force.laboratory_speed_modifier=1
```

-0.5 is half speed, 0 is normal speed, 1 is double speed, 2 is triple etc.

### Research specific technologies

The internal technology names can be found in the infoboxes on their respective pages.

```
/cgame.player.force.technologies['electric-energy-distribution-1'].researched=true/cgame.player.force.technologies['steel-processing'].researched=true
```

To research a high level of an infinite technology, set its level:

```
/cgame.player.force.technologies['worker-robots-speed-7'].level=100/cgame.player.force.technologies['mining-productivity-3'].level=100
```

### Unresearch specific technologies

The internal technology names can be found in the infoboxes on their respective pages.

```
/cgame.player.force.technologies['electric-energy-distribution-1'].researched=false/cgame.player.force.technologies['steel-processing'].researched=false
```

### Enabling specific recipes

The internal recipe/item names can be found in the infoboxes on their respective pages.

```
/cgame.player.force.recipes["electric-energy-interface"].enabled=true/cgame.player.force.recipes["rocket-silo"].enabled=true/cgame.player.force.recipes.loader.enabled=true/cgame.player.force.recipes["fast-loader"].enabled=true/cgame.player.force.recipes["express-loader"].enabled=true
```

### Enable all recipes

```
/cforname,recipeinpairs(game.player.force.recipes)dorecipe.enabled=trueend
```

### Resetting technology effects to default

This will reset the enabled/unlocked state of all recipes to what they would be purely based on the currently researched technologies, as well as resetting other technology effects like mining speed, etc. Any manual modifications to these effects and recipe unlocks will be undone.

```
/cgame.player.force.reset_technology_effects()
```

Note: Can be used as a quick workaround when recipes are unavailable after adding or changing mods even though the technology unlocking them has already been researched.

### Enable ghosts for destroyed entities

This is normally unlocked through researching construction robotics (research) , but this command unlocks it independent of the research.

```
/cgame.player.force.create_ghost_on_entity_death=true
```

## Modding tools

A list of the internal names of most things in the vanilla game can also be found on data.raw .

### Access a mod's data

If the first word of the command is __mod-name__ it will run in the context of the mod with the same name. For instance, this command prints the data from the Even Distribution mod:

```
/c__even-distribution__game.player.print(serpent.dump(global))
```

### Print to console the tile under the player

```
/cgame.player.print(game.player.surface.get_tile(game.player.position).name)
```

### Write all researched technologies to file

```
/clocallist={}for_,techinpairs(game.player.force.technologies)doiftech.researchedthenlist[#list+1]=tech.nameendendgame.write_file("techs.lua",serpent.block(list).."\n",true)
```

### Write all enabled recipes to file

```
/clocallist={}for_,recipeinpairs(game.player.force.recipes)doifrecipe.enabledthenlist[#list+1]=recipe.nameendendgame.write_file("recipes.lua",serpent.block(list).."\n",true)
```

### Write mod list to file

Write all currently active mods and their version to the file script-output/mods.txt in the user data directory .

```
/chelpers.write_file("mods.txt",serpent.block(script.active_mods))
```

### Exporting production statistics

Export production statistics out of the game into external JSON files.

```
/clocaltimescales={[defines.flow_precision_index.five_seconds]="5s",[defines.flow_precision_index.one_minute]="1min",[defines.flow_precision_index.ten_minutes]="10min",[defines.flow_precision_index.one_hour]="1h",[defines.flow_precision_index.ten_hours]="10h",[defines.flow_precision_index.fifty_hours]="50h",[defines.flow_precision_index.two_hundred_fifty_hours]="250h",[defines.flow_precision_index.one_thousand_hours]="1000h"}forsurface_name,_inpairs(game.surfaces)dolocalflowdata=game.player.force.get_item_production_statistics(surface_name)fortimescale_index,timescale_nameinpairs(timescales)dolocaltbl={}localtotals=flowdata.input_countsforitem_name,_inpairs(totals)dolocalrow={item_name}fori=1,300dotable.insert(row,flowdata.get_flow_count{name=item_name,category="input",precision_index=timescale_index,sample_index=i,count=true})endtable.insert(tbl,row)endhelpers.write_file("stats-"..surface_name.."-"..timescale_name..".json",helpers.table_to_json(tbl),false)endendgame.player.print("Export done")
```

## History

- 1.1.92 : Added a notification when a technology is researched. Added /enable-research-queue console command to enable the research queue without disabling achievements.

## See also

- Command line parameters
- https://lua-api.factorio.com/latest/index-runtime.html - Factorio API reference for latest version
