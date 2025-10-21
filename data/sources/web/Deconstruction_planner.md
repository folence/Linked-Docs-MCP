---
title: Deconstruction planner - Factorio Wiki
source: https://wiki.factorio.com/Deconstruction_planner
scraped_at: 2025-10-21 15:47:07
tags: [web, documentation]
---

# Deconstruction planner - Factorio Wiki

**Source:** [https://wiki.factorio.com/Deconstruction_planner](https://wiki.factorio.com/Deconstruction_planner)


|  | Deconstruction planner | Edit |

| Using an unfiltered deconstruction planner to queue orders for construction robots . |
| Stack size | 1 |
| Prototype type | deconstruction-item |
| Internal name | deconstruction-planner |

The deconstruction planner is an item which allows the player to mark tiles and entities, including trees , rocks , cliffs , fish and items on the ground, for removal.

By default, tiles are only marked when no entities are found. Tiles or entities queued for deconstruction will be marked with a red 'X'. When within the range of construction robots they will be removed by the robots and the resulting items stored in logistic network chests or, when a personal roboport is used, the player's inventory. Ghosts will be removed immediately. Anything marked for deconstruction will immediately stop functioning. Deconstruction orders can be cancelled prior to the removal of the target. The deconstruction planner can be used unfiltered (blank) to remove all entities or tiles within its selection area, or it can be filtered to specific targets.

Deconstruction planners, just like blueprints , can be stored in a blueprint book or blueprint library to prevent them occupying inventory space or for organization or sharing purposes.

## Contents

- 1 Usage 1.1 Getting a deconstruction planner 1.2 Accessing settings 1.3 Deleting a planner 1.4 Using the deconstruction planner 1.5 Effects of deconstruction 1.6 Cancelling deconstruction orders 1.7 Undo
- 2 Valid targets 2.1 Tiles 2.2 Environmental entities
- 3 Configuration and filtering 3.1 Blank planner rules 3.2 Filter settings window 3.3 Principles of filtering 3.4 Setting and removing filters 3.5 Entities tab 3.5.1 Trees/rocks only toggle 3.5.2 Special items in the Unsorted section 3.6 Tiles tab 3.7 Exporting and importing with strings
- 4 Achievements
- 5 Trivia
- 6 History
- 7 See also

## Usage

### Getting a deconstruction planner

A planner can be obtained by:

- Clicking the red deconstruction planner icon ( ) in the shortcut bar . (Available once construction robotics is researched in at least one game.)
- Pressing the keyboard shortcut assigned to Make new deconstruction planner ; default: ALT + D .
- Importing a deconstruction planner string .

Once a new planner is in the hand it can be used immediately and then deleted by pressing Q to clear the hand. Alternatively, it can be dropped into the player's inventory for later use. Once in the inventory it can be pinned to a quickbar slot.

### Accessing settings

The planner must be in an inventory in order for its configuration to be changed. Settings can be accessed by clicking Right mouse button on a planner's icon, either in the inventory or on a quickbar link.

A full description of available settings and filters can be found under configuration and filtering .

### Deleting a planner

A planner that has been stored in an inventory can be deleted by clicking the red trash-can icon labelled Destroy deconstruction planner ( ) in the top right of its settings window.

Care should be taken when the planner has been configured as this operation is performed immediately without confirmation and cannot be undone.

### Using the deconstruction planner

With a planner held in the hand the player can click-drag it ( Left mouse button is held down while moving the mouse) over existing structures and ghosts to mark them for deconstruction. A tooltip appears indicating what will be removed.

The planner can be used anywhere on the map where the player has radar coverage (map view).

Once Left mouse button is released the deconstruction planner will take effect according to the rules listed below.

- Dragging a deconstruction planner.
- The tooltip shows what will be removed.
- Red Xs indicate queued deconstruction orders. Ghosts were immediately removed.

### Effects of deconstruction

The following describes the possible results of using a deconstruction planner in the game world:

- Any selected entity ghosts and tile ghosts will be immediately removed.
- Any selected entities and tiles will be queued for deconstruction, indicated with a red X.
- Anything queued for deconstruction will stop functioning; for example transport belts will stop moving, assembling machines will cease producing items, walls stop connecting to each other, and so on. Laser and gun turrets will continue functioning even when marked for deconstruction.
- If the deconstruction orders are within the construction area of construction robots the orders will be added to the bots' queue and will be removed in due course: Bots will fly in and remove all entities and tiles and place the resulting items in logistic network chests, or the player's inventory when the bots flew from a personal roboport. Where there are items to be removed - for example being carried by transport belts or stored inside a chest or assembling machine - these will also be picked up by bots and placed in the appropriate storage. Items must be removed before the entities that carry or hold them. For example if a wooden chest holding 500 iron plates is marked for removal, the plates will be picked up first and only when all have been removed will the bots deconstruct the chest itself. Environmental entities such as trees, rocks and fish are handled in the same way, except bots mine them and collect and store the resource items they leave behind. Cliffs are a special case: they are destroyed by bots carrying cliff explosives and do not yield any item to be stored.

### Cancelling deconstruction orders

Queued deconstruction orders can be cancelled by holding SHIFT while click-dragging a deconstruction planner over the affected area.

When SHIFT is held down the area selection border will change from red to blue to indicate cancellation mode is in effect.

### Undo

The undo tool can be used to revert the actions of a deconstruction planner. This applies both to pending deconstruction orders and completed removals.

Undo is triggered by pressing CTRL + Z (on macOS: Command + Z )

Performing an undo will cancel any queued removal orders (red Xs) that have not yet been actioned. Any ghosts that were removed will be immediately replaced. Where built entities and tiles have already been removed the undo will reinstate them in the form of new ghosts that can then be re-built by any construction robots in range.

Items that were removed as part of the deconstruction - for example the inventory of chests or items carried by a transport belt - will not be restored by an undo. This means that a deconstruction that consisted exclusively of items, for example picking up stone from the ground, cannot be undone.

It is also not possible to undo the removal of trees, rocks, cliffs and fish.

- Cancelling deconstruction orders by dragging with Shift held down. The entities start working when the deconstruction is cancelled.
- Using then undoing a deconstruction planner. Deconstruction markers are cancelled, ghosts re-appear, and removed entities are reinstated as new ghosts for bot rebuilding.

## Valid targets

The deconstruction planner can remove player-built entities, entity ghosts , tiles, tile ghosts and loose items. In addition, it can remove trees , rocks , cliffs and fish .

### Tiles

Tiles are treated differently to entities, entity ghosts and tile ghosts. By default a deconstruction planner will not select any tiles unless the area selected contains only tiles; whenever one or more entities, entity ghosts or tile ghosts is included, tile selection is disabled. This is done to allow the player to use a deconstruction planner to remove entities that are placed on top of path tiles (such as concrete ) without the floor always being removed as well.

When the user wishes to select tiles in areas where other objects also exist the deconstruction planner configuration must be changed as described in the next section.

### Environmental entities

These are handled in the same way as entities and tiles placed by the player: they are marked with a red X and construction robots will remove them. A difference with environmental entities is that bots will collect resources rather than the entity itself, such as wood from trees and stone from rocks.

The removal of cliffs requires that the bots have access to cliff explosives. Cliffs do not leave behind any resource.

The ability to use a deconstruction planner to remove and collect fish provides a convenient way for a player equipped with a personal roboport to replenish their stocks of healing items even in the middle of combat. Fish marked with a deconstruction planner will stop moving.

## Configuration and filtering

A new deconstruction planner is blank, meaning it removes according to a pre-defined set of rules. The planner can optionally be edited to provide a custom list of removal rules which control which types of entities and tiles will - or won't - be removed. These rules are called filters.

A filtered planner will show its filtered items on its icon. Up to the first four filters will be shown.

### Blank planner rules

A blank planner will select:

- Any entities and entity ghosts, including trees, rocks, cliffs and fish;
- Tile ghosts;
- Or , if and only if no entities, entity ghosts and tile ghosts are found, it will instead select tiles.

These rules are the base point from which a filtered planner can then be customized.

### Filter settings window

The deconstruction planner interface is divided into two sections: entities and tiles .

- The entities tab.
- The tiles tab.

### Principles of filtering

Each tab consists of 30 slots in which an entity or tile can be chosen. When one or more slots is filled the planner becomes filtered and will now act according to those filters.

A set of filters is either a whitelist or blacklist, and this is set with a toggle at the top of each tab. The default is whitelist. In whitelist mode the planner will act only upon those items added to the filter slots - any entities and tiles not added as filters will be ignored by the planner.

In blacklist mode the opposite applies: the planner will mark everything except the entities or tiles filtered on.

### Setting and removing filters

Clicking any slot with Left mouse button will open the Set the filter window in which the desired item can be chosen. Alternatively, an item in the hand can be clicked into a slot to filter on that item.

A filter is removed by clicking on a filled slot with Right mouse button .

### Entities tab

In the entities tab the user can select items to filter from the follow categories:

- Environment
- Logistics
- Production
- Combat
- Unsorted

Logistics, production and combat will be familiar to the player from the item selection window. Environment and unsorted are unique to the deconstruction planner.

The environment tab lists cliffs, fish, and every individual kind of tree and rock. This facilitates filtering on specific environmental entities if desired.

#### Trees/rocks only toggle

At the top of the entities tab is the Trees/rocks only tick-box. With this enabled the deconstruction planner will filter on all kinds of trees and rocks from the Environment section, and the filter slots will be disabled. The Whitelist/Blacklist toggle is still in effect and controls whether the planner selects only trees and rocks, or selects everything but them. Fish and cliffs are not included in this filter.

#### Special items in the Unsorted section

The unsorted section provides four special items, each using a red X icon.

- Entity ghost: To filter on any type of entity ghost, separate from constructed entities.
- Item on ground: Loose items on the ground, such as dropped by the player, spilled from removing armor , and stones dropped from destroyed rocks . Does not include items on transport belts .
- Item request slot: Filters on the pending addition of items such as modules to assembling machine 2 or electric furnace . This would also target fuel queued for addition to a locomotive . Does not target items already installed, only those waiting to be added following the placement of a blueprint or as a result of an undo operation.
- Tile ghost: As with entity ghost, this will target tile ghosts separately from constructed tiles. If the user wants a deconstruction planner that only removes tile ghosts, they can place this item as an entity filter. If they want a filter that removes all types of tiles and tile ghosts, they should add Tile ghost under Entities and then set the Tiles tab drop-down to 'Always'.

### Tiles tab

Clicking a filter slot will bring up the Set the Filter window showing the available tiles.

At the top of the Tiles tab is a drop-down that controls constructed tile removal behavior. It has four options:

- Normal: The default. Constructed tiles are removed only when no entities, entity ghosts or tiles ghosts are found in the deconstruction area.
- Always: Constructed tiles are always removed, even if the deconstruction planner also selects entities or entity ghosts. Tile ghosts are not selected unless Tile ghost is added under the Entities tab.
- Never: Constructed tiles are never removed, even if they are the only object selected. Tile ghosts are not selected unless Tile ghost is added in the Entities tab.
- Only: Constructed tiles are always removed, and nothing else will be. Entities, entity ghosts and tile ghosts will be ignored. The Entities tab is effectively disabled when this mode is selected.

The deconstruction planner always follows the settings of this drop-down, regardless of any filters set in the Tiles tab. For example if a user wishes to configure a planner that removes both walls and concrete , they must first set those filters in the Entities and Tiles tabs, and then also set the Tiles drop-down to Always . Without changing the drop-down the planner would only select concrete in places where no entities, entity ghosts or tile ghosts were found, as per the rules described under Normal in the above list.

### Exporting and importing with strings

The settings for a deconstruction planner can be exported in string form.

Clicking the Export to string button ( ) in the top right of the planner edit window will pop up a window containing the Deconstruction item string . This string can be copied to the operating system clipboard, from where it could be saved to a text file or uploaded to a website.

To import a deconstruction planner the player can click the Import String icon on the shortcut bar ( ). A dialogue box will appear into which the string can be pasted. This will result in a deconstruction planner appearing on the hand with the same configuration as the one that was exported.

The export/import process can be used to copy deconstruction planners between games and to other players.

## Achievements

|  | Automated cleanup Deconstruct 100 objects with the construction robots . |

## Trivia

- In Space Age , it is possible to get a quality deconstruction planner by recycling them with quality modules . Quality planners function identically to their normal counterparts

## History

- 0.18.37 : Deconstruction planners can be inserted into blueprint books and the blueprint library. Deconstruction planners can now have custom icons specified. Icons and filters in the deconstruction planners are preserving the original values so whenever the mods would be re-added, the original values can be restored, unless the player clears the related icons manually. Deconstruction planners can no longer be cleared by shift-right mouse button.

- 0.18.13 : Allowed to delete deconstruction planners also when opened in other inventory.

- 0.17.10 : "Make deconstruction planner" function is now accessible via keyboard shortcut.

- 0.17.0 : Added cliffs as a valid deconstruction target. Trains can be deconstructed.

- 0.15.3 : Deconstruction planners can be destroyed by clicking the trash can icon in the GUI.

- 0.15.0 : Blueprint library: Allows for keeping players blueprints between individual game saves and allows sharing blueprints in multiplayer games. Added ability to export and import blueprints, blueprint books, and deconstruction planners as strings. Blueprints, blueprint books and deconstruction planners are obtainable from the library GUI with no crafting cost.

- 0.13.0 : Several non-stackable items can be swapped directly with counterparts, this includes the deconstruction planner.

- 0.11.15 : When using the deconstruction planner, the logistic network is not drawn if the mouse is over a GUI element.

- 0.11.0 : Added a cancel deconstruction option to the deconstruction planner.

- 0.9.0 : Introduced

## See also

- Blueprint
- Upgrade planner
- Roboport
- Construction robot

| Production items |
| Tools | Repair pack Blueprint Deconstruction planner Upgrade planner Blueprint book |
| Electricity | Boiler Steam engine Solar panel Accumulator Nuclear reactor Heat pipe Heat exchanger Steam turbine Fusion reactor ( ) Fusion generator ( ) |
| Resource extraction | Burner mining drill Electric mining drill Big mining drill ( ) Offshore pump Pumpjack |
| Furnaces | Stone furnace Steel furnace Electric furnace Foundry ( ) Recycler ( ) |
| Agriculture | Agricultural tower Biochamber Captive biter spawner |
| Production | Assembling machine 1 Assembling machine 2 Assembling machine 3 Oil refinery Chemical plant Centrifuge Electromagnetic plant ( ) Cryogenic plant ( ) Lab Biolab ( ) |
| Environmental protection | Lightning rod Lightning collector Heating tower |
| Modules | Beacon Speed module Speed module 2 Speed module 3 Efficiency module Efficiency module 2 Efficiency module 3 Productivity module Productivity module 2 Productivity module 3 Quality module ( ) Quality module 2 ( ) Quality module 3 ( ) |
| Navigation | Logistics Intermediate products Space ( ) Combat Technology Environment |
