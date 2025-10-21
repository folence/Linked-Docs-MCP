---
title: Debug mode - Factorio Wiki
source: https://wiki.factorio.com/Debug_mode
scraped_at: 2025-10-21 14:29:51
tags: [web, documentation]
---

# Debug mode - Factorio Wiki

**Source:** [https://wiki.factorio.com/Debug_mode](https://wiki.factorio.com/Debug_mode)

The debug mode is used mainly by developers and modders to analyze the running state of the game. It can be enabled to show detailed information about the game world. The default key to enable debug mode is F5 .

For example, one can:

- See the path the biters are coming from and where they plan to target,
- See the position / coordinates of the cursor,
- See a grid-overlay for the tiles and chunks ,
- See additional non-game related information, such as Updates Per Second and FPS.

Note: In addition to this internal debugging tool there are also third-party debugging tools contributed by the community available on the Factorio sub-forum for mod development tools .

## Activate the debug mode

There are 2 debug-levels:

- Always - This is the default mode, if no mode is active. Keep very few things active here.
- Debug - Toggled by pressing F5 . Allows to toggle the debug overlays.

## Configuring the debug mode

To configure the 2 modes, press F4 . This opens up a menu with many options. You can move this menu with the mouse, if it hides some interesting underlying thing. You can switch between 2 folders, which reflects the option for that debug-mode ("always", "debug"). The options are the same for each mode. Each mode can be configured to the user's liking, the different modes are only for convenience. A search function ( CTRL + F ) is available.

## List of debug-options and their function

| Option | Description |
| show-fps | Will show the current frames-per-second and updates per second, short FPS and UPS . Should be normally about 60. |
| show-clock | Shows a real time clock. |
| show-detailed-info | Shows the cursor position in tiles (and subdivisions of that). Current resolution and zoom. How many objects are on the screen (painted by the graphic card). How many entities, chunks and paths are in the game and used. |
| show-time-usage | Internal statistics about how long some calculations take, in milliseconds per tick . Time is shown as average/min/max of the last 100 ticks, interval can be changed with /perf-avg-frames. Minimum values exclude zeroes (e.g. from ticks where no mod hooks were run). Overall calculation delays (some are parallel) must be under 16.6 ms to maintain normal framerate at 1x speed with 60 ticks per second. The Top section of metrics cover the wider game engines activities. The middle Update section relates to running the simulation for a tick. The bottom Map Generator section relates to the map generation activity. For more details, refer to Tutorial:Diagnosing performance issues . |
| show-entity-time-usage |  |
| show-gpu-time-usage |  |
| show-sprite-counts | The counts of each sprite rendered on screen. |
| show-lua-object-statistics | Statistics related to the Lua garbarge collector. Update time (avg/min/max), created objects (avg/min/max [total]), destroyed objects (avg/min/max [total]). |
| show-heat-buffer-info |  |
| show-multiplayer-waiting-icon | When in a multiplayer game: if the game is currently waiting for the server to process. |
| show-multiplayer-statistics | The latency information when in multiplayer. |
| show-multiplayer-selection-rectangles | Allows to view selection rectangles of other players in multiplayer. |
| show-debug-info-in-tooltips | Shows additional information in the tooltips of entities, items, recipes, tiles etc. |
| show-resistances-in-tooltips-always | Show entity resitances in all entity tooltips instead of just tooltips of enemy entities and entities with hide_resistances set to false. |
| hide-mod-guis | Hides GUIs added by mods. |
| show-tile-grid | Shows the borders of the tiles and chunks . |
| show-blueprint-grid |  |
| show-collision-rectangles | Shows the collision boxes of each entity (red). |
| show-selection-rectangles | Shows a blue box over each entity, if you hover over it, it will be selected. |
| show-render-rectangles | Shows a pink box over each entity, if that is on your screen, the entity will be rendered. |
| show-sticker-boxes |  |
| show-entity-positions |  |
| show-entity-velocities |  |
| show-selected-entity-advanced-tiles | Shows on which advanced tiles (2×2 tiles) the entity is registered. |
| show-selected-input-transport-belts | Shows which entities input into the selected transport line. |
| show-paths | The calculated paths for the biters in different colors. |
| show-path-requests |  |
| show-next-waypoint-bb | Shows waypoints for biters (in green), nearly the same info as the next. |
| show-target | Shows the current target of the biters (red). |
| show-unit-group-info | Biter groups, which belong together (circles and lines belonging together) |
| show-unit-behavior-info |  |
| show-pathfinder-fringe |  |
| show-path-cache | The source-positions of a path and about the length (?) |
| show-path-cache-paths |  |
| show-rail-paths | Which path a train will follow. |
| show-rolling-stock-count | Shows inserter positions |
| show-rail-connections | Shows rail connections. |
| show-rail-joints |  |
| show-rail-segment-collision-boxes |  |
| show-train-stop-point | When a train slows down it shows the calculated point where it should halt |
| show-train-braking-distance | The distance a train will take to stop at its current speed |
| show-train-signals |  |
| show-train-repathing | Display a flying "repathed" text over a train whenever it repaths. |
| show-network-connected-entities | Displays the network-id of the electric network that a pole is connected to |
| show-circuit-network-numbers | Shows the number (and color) of circuit networks |
| show-energy-sources-networks | Which network-id an entity is connected to. |
| show-active-state | Inserters, fish, turrets are turned to passive, if not used; Red = inactive, Purple = inactive when enemies aren't around (turrets etc), Green = inactive when player isn't around (fish). Passive entities consume less CPU power. |
| show-wakeup-lists | When an entity is sleeping in another entity it shows which entities it's sleeping in. |
| show-transport-lines |  |
| show-transport-line-gaps |  |
| show-pollution-values | Shows the numeric pollution amount on each chunk. |
| show-active-entities-on-chunk-counts | Shows counts of active entities per chunk. They are divided into two categories: Blue = active when a player is around (e.g. fish) Green = active when enemies are around (e.g. turrets) |
| show-active-chunks | Shows in the map view, which chunks are "on", unmarked chunks are not calculated. |
| show-polluted-chunks | Shows which chunks have pollution. |
| hide-chart-tags | Hides map tags. |
| show-enemy-expansion-candidate-chunks | Where is space left to spread the brood? Goes from red (nearly no space) to green (space to expand). |
| show-enemy-expansion-candidate-chunk-values | Which chunks the enemies will try to expand into. |
| show-bad-attack-chunks |  |
| show-tile-variations | Shows, which tile-variation (1, 2 or 4 tile sized) is painted for which area of the map. Quite confusing, zoom in to see the meaning. |
| show-raw-tile-transitions | Turns connected textures for land and water off, so the distinction can easily be made. |
| show-fluid-box-fluid-info | How much fluid is in a pipe/storage tank, shows flow of liquid in pipes. |
| show-environment-sound-info | Displays which sound of which entity is played and how loud. |
| show-environment-sound-area |  |
| show-selected-entity-audible-range |  |
| show-recently-played-sound-info |  |
| show-logistic-robot-targets |  |
| show-spidertron-movement |  |
| show-player-robots |  |
| show-fire-info |  |
| show-sticker-info |  |
| show-decorative-names |  |
| show-decorative-collision-rectangles |  |
| allow-increased-zoom |  |
| show-chunk-components |  |
| show-train-no-path-details | Chat shows extra info on pathfinder for no-pathing trains. [1] |
