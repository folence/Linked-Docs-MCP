---
title: Map editor - Factorio Wiki
source: https://wiki.factorio.com/Map_editor
scraped_at: 2025-10-21 14:29:55
tags: [web, documentation]
---

# Map editor - Factorio Wiki

**Source:** [https://wiki.factorio.com/Map_editor](https://wiki.factorio.com/Map_editor)

Factorio includes a fully featured map editor. You can access it by selecting "Map editor" on the Factorio main menu, or by either using the console command "/editor" or pressing CTRL + SHIFT + F11 in-game. In-game, /editor can also be used to leave the map editor again. Enabling the editor disables achievements.

The editor allows the player full creative control to completely change map terrain, clone parts of the map and much more. However, the map editor cannot be used to create custom scenario scripts , for that see modding .

## Contents

- 1 Editor modes 1.1 None 1.2 Decoratives 1.3 Entities 1.4 Forces 1.5 Resources 1.6 Surfaces 1.7 Tiles 1.8 Cloning 1.9 Areas and positions 1.10 Time 1.11 Cliffs 1.12 Asteroid chunks
- 2 Editor entities
- 3 Setting up research
- 4 Saving scenarios

## Editor modes

The "Tools" tab in the GUI shown in the top left when using the map editor allows to switch between different map editor modes. Each of the modes provides different tools and ways to change the map. All editor modes use Q to clear the cursor, like the normal game. Placing entities/tiles/decoratives is done using Left mouse button , they can be removed with Right mouse button . The size of brushes and sprays can be increased and decreased using Numpad + and Numpad - .

### None

The "None" mode is the default editor mode when opening the map editor. It works very similar to the normal game, mostly providing additional utilities such as instant blueprinting, deconstruction and upgrading, and the ability to craft any item infinitely, even if item is not researched yet or hidden. Similarly, recipes in machines can be set even if they are not researched yet. The "None", surface and time editor modes are the only modes where the player's inventory is accessible so the mentioned features can be used.

### Decoratives

The decoratives editor mode allows to place and delete decoratives as desired. The brush allows to place decoratives in a large area at once, while the cursor places single decoratives.

In this mode, it is possible to see the bounding boxes of the decoratives when hovering near them with an empty cursor. The graphical variation of the decorative depends on its position in the world and cannot be changed.

### Entities

The entities editor mode can be used to bulk place many entities at once or to place entities that don't have an associated item.

The "build-as force" option allows to choose the force the entities should be placed as. The brush and spray tools allow to place many entities at once. The difference between spray and brush is that the brush will not place more entities on already placed areas without clicking again.

### Forces

Forces can be created and deleted using the forces editor mode. Furthermore, entities can be selected to change their force. The red flag that can be placed with this editor mode changes the spawn location of that force on that surface.

### Resources

The resources editor mode allows to easily create or delete resources. The difference between spray and brush is that the brush will not place more resources on already placed areas without clicking again. The intensity setting controls how rich the resource entities are. The slider does not allow much variation in this by default, however the textfield next to it is not limited in any way, so it can be used to set much higher richness.

### Surfaces

The surface editor mode allows to create and delete surface and switch between them. Furthermore, it can be used to remove all entities from a surface, change the surface's map generation settings, remove chunks that contain only out-of-map tiles and more. Additionally, it is possible to import a different save file into the save that is currently being edited. This operation will create a new surface that contains the map from the imported save file.

### Tiles

The tile editor mode allows to place any kind of tile, anywhere. The brush mode can be used for bulk placing and the paint bucket can be used to easily replace one tile type with another. To place other tiles on out-of-map tiles, SHIFT must be held. The variations tab allows to randomize what graphics the tiles use, each tile has up to 16 different graphics variations that it can be use.

### Cloning

The clone editor mode allows to clone entire areas of the map, including decoratives and tiles, or to clone single entities. To de-select the clone source area/entity or set an entity as the source entity, use Q .

### Areas and positions

The area and position editor mode allows to create positions and areas in the world that can be named. These can then be easily accessed in scripts.

### Time

The time editor mode can be used to pause and unpause the game, make it run only for a single tick/a custom interval or to speed up/slow down the game. Furthermore, it can be used to control the current day time and how long one day takes.

### Cliffs

The cliff editor mode allows to create cliffs easily. They can be placed in lines by holding and dragging the mouse, or be placed as single entities. Use R and SHIFT + R when placing single cliffs to rotate through all their possible orientations.

### Asteroid chunks

The asteroid chunks editor mode allows to place and delete asteroid chunks as desired. The brush allows to place chunks in a large area at once, while the cursor places single chunk. Asteroid chunks can only be placed on space platform surfaces.

## Editor entities

There are some entities not accessible in a normal playthrough. They can all be configured.

| Entity | Internal name | Size | Health | Resistance | Uses |
| Infinity chest | Infinity chest | 1x1 | 350 | Fire: 100% Impact: 100% Physical: 100% Explosion: 100% | Can either generate items or discard items. |
| Infinity pipe | infinity-pipe | 1x1 | 100 | Fire: 100% Impact: 100% Physical: 100% Explosion: 100% | Can either generate fluid or discard fluid, at any temperature. |
| Electric energy interface | electric-energy-interface | 2x2 | 150 | All: 0% | Can generate up to 500 GW, drain up to 100 GW, or buffer up to 100 GJ. |
| Lane splitter | lane-splitter | 1x1 | 170 | All: 0% | Can be used to move items to either side of a belt. Has a maximum belt speed of 15 /s. |
| Loader | loader | 2x1 | 170 | Fire: 60% | Instantly loads items from the belt, at a rate of (15, 30, 45, 60) /s. |
| Linked chest | linked-chest | 1x1 | 100 | All: 0% | Is linked to all other linked chests. |
| Linked belt | linked-belt | 1x1 | 100 | Fire: 60% Impact: 30% | Can be connected to a belt anywhere else. |
| Heat interface | heat-interface | 1x1 | 150 | Fire: 100% Impact: 100% Physical: 100% Explosion: 100% | Warms up adjacent heat pipes by up to 1000 degrees. |
| Burner generator | burner-generator | 5x3 | 400 | All: 0% | Consumes 2 MW with 50% efficiency. Unlike boilers , Burner generators do not require water . |

## Setting up research

In the technology GUI T technologies can be instantly researched by shift clicking the research button after selecting the desired technology. Already researched technologies can be un-researched by selecting the technology and clicking "unresearch". Furthermore, the console is accessible like in the normal game, so it can be used to research all technologies and more: Console .

## Saving scenarios

Maps created with the map editor can be saved as Scenarios via the in-game escape menu. These scenarios are saved to the user data directory . The scenario may then be played from selecting Play->Custom Scenario from the Main Menu. Alternatively, it can be played directly from the escape menu, using the "save and play" option. If one wishes to add scripting to the scenario, they may do so by modifying the control.lua file created inside the scenario file.
