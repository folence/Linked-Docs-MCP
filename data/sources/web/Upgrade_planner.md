---
title: Upgrade planner - Factorio Wiki
source: https://wiki.factorio.com/Upgrade_planner
scraped_at: 2025-10-21 15:47:08
tags: [web, documentation]
---

# Upgrade planner - Factorio Wiki

**Source:** [https://wiki.factorio.com/Upgrade_planner](https://wiki.factorio.com/Upgrade_planner)


|  | Upgrade planner | Edit |

| Using an unfiltered upgrade planner. |
| Stack size | 1 |
| Prototype type | upgrade-item |
| Internal name | upgrade-planner |

The upgrade planner is a tool for mass updating entities to alternative entities of the same size and type. It can be used on both placed structures and ghosts . It can also modify the contents of a blueprint . While most commonly used to upgrade entities to their higher tier equivalents - for example to replace transport belts with fast transport belts or fast inserters with bulk inserters - the upgrade planner is able to change a wide range of entities including transport belts , underground belts , splitters , inserters , assembling machines , chests , power poles , rail signals , modules , furnaces and more.

Using an upgrade planner in the game world is similar to the operation of the deconstruction planner and blueprint, in that the player drags a rectangular area in which the upgrade planner will function and this results in orders being queued for construction robots . Upgrade planners can be used blank (unfiltered) to automatically apply a limited set of common upgrades. Alternatively they can be configured  (filtered) to make specific replacements. This can include downgrading higher tier, later-game entities to lower tier equivalents.

Upgrade planners, just like blueprints , can be stored in a blueprint book or blueprint library to prevent them occupying inventory space or for organization or sharing purposes.

## Contents

- 1 Basic operation 1.1 Getting an upgrade planner 1.2 Using a planner in the game world 1.3 Cancelling updates 1.4 Updating blueprints
- 2 Upgrade planner filters 2.1 Using a blank upgrade planner (unfiltered) 2.2 Filtering an upgrade planner 2.2.1 The filter window 2.2.2 Editing the filters
- 3 Valid entities 3.1 Modded entities
- 4 Trivia
- 5 History
- 6 See also

## Basic operation

### Getting an upgrade planner

A blank planner can be obtained by clicking the green upgrade planner icon ( ) on the shortcut bar (available once construction robotics has been researched in at least one game.)

This will result in a blank upgrade planner appearing in the hand. It can be used immediately or placed in the inventory. It must be placed in the inventory before a filter can be applied and before it can be pinned to a quickbar slot.

### Using a planner in the game world

With a planner held in the hand the player can click-drag it ( Left mouse button is held down while moving the mouse) over existing structures to mark them for upgrade. A tooltip appears indicating which entities will be changed and to what.

Once Left mouse button is released yellow circles will appear over any existing structures that are now queued for update. These update operations will be performed by construction robots .

The planner can be used anywhere on the map where the player has radar coverage (map view). Upgrade planners can also affect ghost entities. Any ghost eligible for update will immediately change to the new entity.

- Dragging an upgrade planner.
- The tooltip shows which upgrades will occur.
- Yellow circles indicate pending update operations.
- Ghost entities update immediately.

### Cancelling updates

Pending upgrade operations can be cancelled by holding SHIFT while click-dragging the upgrade planner over the affected area.

### Updating blueprints

Upgrade planners can also be used to change the contents of a blueprint. This allows the player to keep using the same blueprints as they research progressively better entities. As upgrade planners can also downgrade entities this further provides a way for a player to adjust late-game blueprints to make them suitable for re-use in subsequent games.

- The blueprint to be updated must reside in an inventory. It is not currently possible to use an upgrade planner in the blueprint library.
- With a planner held in the hand, the edit window for a blueprint should be opened by clicking Right mouse button on it.
- The upgrade planner can be applied by clicking Left mouse button on the grey upgrade planner slot in the top right corner of the blueprint.
- The entities in the blueprint will immediately update according to the filters in the planner. If a blank planner is used an automatic set of common upgrades is applied, as described in the next section.
- The update is immediate and cannot be undone, except by applying another upgrade planner with filters set to change back the affected entities.

## Upgrade planner filters

A new upgrade planner is blank, meaning it lacks any configuration and will operate on a pre-defined set of upgrade rules. The planner can optionally be edited to provide a custom list of update rules that control which entities will be updated and what to.

### Using a blank upgrade planner (unfiltered)

When a blank upgrade planner is used it operates on a specific list of entities considered automatically upgradable to the next highest tier. The list of entity types that can be affected by a blank planner are as follows:

- Belts
- Underground belts
- Splitters
- Inserters
- Assembling machines
- Furnaces

Entities of the above types will be upgraded to the next highest tier where one exists. A complete list of the entities eligible for upgrade by a blank planner is found in Valid entities .

### Filtering an upgrade planner

The planner must be in an inventory in order for it to be editable.  The filter window can be accessed by clicking Right mouse button on an upgrade planner, either in the inventory or on a quickbar link.

#### The filter window

The filter window consists of 24 entity slot pairs.

In each pair the entity to be updated goes in the left slot and the entity it will be changed to goes in the right slot.

- A blank planner.
- A simple configuration example.

#### Editing the filters

A filter is applied by first clicking Left mouse button on the left-hand slot of any slot pair. This brings up the Select upgrade window. This is similar to the item selection window but is limited to displaying the entities an upgrade planner is able to change.

The right-hand slot is then selected in the same way, choosing the target entity. The select upgrade window for the right slot will only show entities that are a valid update target for the entity in the left slot.

When there is only one possible update target the right slot will be filled in automatically.

Filters can be removed by clicking Right mouse button on the slot.

## Valid entities

The upgrade planner can operate on the entities listed below. It can swap any entity in a given category to any other entity in the same category. For example a transport belt can be changed to a fast or express transport belt and also to any kind of underground belt , but not to a splitter or a chest .

The Blank upgrade planner column indicates which entities will be automatically upgraded when a blank (unfiltered) upgrade planner is used. These entities will upgrade to the entity following them in the table.

| Category | Entity | Blank upgrade planner |
| Belts and undergrounds | Transport belt | Yes |
| Belts and undergrounds | Fast transport belt | Yes |
| Belts and undergrounds | Express transport belt | No/Yes |
| Belts and undergrounds | Turbo transport belt | No |
| Belts and undergrounds | Underground belt | Yes |
| Belts and undergrounds | Fast underground belt | Yes |
| Belts and undergrounds | Express underground belt | No/Yes |
| Belts and undergrounds | Turbo underground belt | No |
| Splitters | Splitter | Yes |
| Splitters | Fast splitter | Yes |
| Splitters | Express splitter | No/Yes |
| Splitters | Turbo splitter | No |
| Inserters | Burner inserter | No |
| Inserters | Inserter | Yes |
| Inserters | Fast inserter | Yes |
| Inserters | Bulk inserter | No |
| Chests | Wooden chest | No |
| Chests | Iron chest | No |
| Chests | Steel chest | No |
| Chests | Active provider chest | No |
| Chests | Passive provider chest | No |
| Chests | Storage chest | No |
| Chests | Buffer chest | No |
| Chests | Requester chest | No |
| Power poles | Small electric pole | No |
| Power poles | Medium electric pole | No |
| Rail signals | Rail signal | No |
| Rail signals | Rail chain signal | No |
| Steam Engine/Turbine | Steam engine | No |
| Steam Engine/Turbine | Steam turbine | No |
| Furnaces | Stone furnace | Yes |
| Furnaces | Steel furnace | No |
| Assembling machines | Assembling machine 1 | Yes |
| Assembling machines | Assembling machine 2 | Yes |
| Assembling machines | Assembling machine 3 | No |
| Modules | Speed module | No |
| Modules | Speed module 2 | No |
| Modules | Speed module 3 | No |
| Modules | Productivity module | No |
| Modules | Productivity module 2 | No |
| Modules | Productivity module 3 | No |
| Modules | Efficiency module | No |
| Modules | Efficiency module 2 | No |
| Modules | Efficiency module 3 | No |
| Modules | Quality module | No |
| Modules | Quality module 2 | No |
| Modules | Quality module 3 | No |

With the Space Age DLC and the quality mod enabled, upgrade planners can also be set to upgrade entities to different qualities of the same entity.

### Modded entities

Modded entities can also be valid entities for an upgrade planner. The filter selection window will expand to automatically include any modded entities compatible with the above categories.

This can also result in extra categories being available for update, beyond those listed above. For example if a mod is installed that adds new types of lamp , it may become possible to update the vanilla lamp to one of the new modded lamps using an upgrade planner.

## Trivia

- In Space Age , it is possible to get a quality upgrade planner by recycling them with quality modules . Quality planners function identically to their normal counterparts

## History

- 0.17.10 : "Make upgrade planner" function is now accessible via keyboard shortcut.

- 0.17.0 : Introduced

## See also

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
