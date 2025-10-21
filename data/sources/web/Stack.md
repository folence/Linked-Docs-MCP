---
title: Stack - Factorio Wiki
source: https://wiki.factorio.com/Stack
scraped_at: 2025-10-21 14:29:39
tags: [web, documentation]
---

# Stack - Factorio Wiki

**Source:** [https://wiki.factorio.com/Stack](https://wiki.factorio.com/Stack)

A stack is the basic element in Factorio to store items. One space in an inventory can hold one stack.

## Contents

- 1 Examples of stacks
- 2 How do stacks work? 2.1 Stack size 2.2 Filtered stacks 2.3 Damaged items 2.4 Items with durability
- 3 Stack size bonuses
- 4 Stack limitation
- 5 Handling stacks
- 6 History

## Examples of stacks

- The player's inventory Main inventory Armor, weapon, and ammunition stacks Logistic trash slots The player's hand (is also a stack)
- Vehicles Car (fuel, ammunition, inventory) Tank (fuel, ammunition, inventory) Spidertron (ammunition, inventory) Train (wagons, engines for fuel)
- Chests : The archetypal example of stacks outside the player's inventory; a chest is basically just a group of stacks.
- Devices Furnace : Burner stack ( stone and steel furnace only), input and output stack Assembling machines and chemical plants : 1 or more output and 1-6 input stacks, depending on item type being assembled Labs Burner-based: Boiler , burner mining drill , burner inserter Roboport (filtered for robots and repair packs only) Gun turret
- Special Inserters and worker robots (Small, variable-size stacks allow these entities to move items between other stacks. See also the inserter and robot stack size bonus research topics.)

## How do stacks work?

A stack can store a number of identical items.

The first inserted item determines which item types can be stored. This also indirectly determines how many items can be stored in the stack, as this depends on the item type's maximum stack size.

Only items can be stored within stacks; stacks cannot hold liquids or other entity types.

### Stack size

The number of items a stack can store. Stack size depends on the item; existing stack sizes and (non-exhaustive) examples include (click to expand):

| Stack size | Examples |
| 1 | Nuclear fuel , artillery shell , satellite , modular armor , blueprint . |
| 5 | Locomotive , all wagons . |
| 10 | Roboport , rocket fuel , artillery turret , atomic bomb , low density structure . |
| 20 | Some equipment modules , pumpjacks . |
| 50 | All ores, stone , coal , all modules , electric mining drill , electric furnace , all assemblers , all chests , all inserters , gun turret , laser turret , all power poles including substation , both types of worker robots , solid fuel . |
| 100 | Iron plate , copper plate , steel plate , processing unit , iron gear wheel , stone brick , all types of concrete , both isotopes of processed uranium , pipe (regular), all belts , wall , landfill . |
| 200 | Electronic circuit , advanced circuit , all types of magazine , all types of tank cannon shell , copper cable , both colors of circuit wire , all types of science pack except space science pack. |
| 2,000 | Unique to space science pack , present to allow stacking up to 2 rockets ' worth of packs in the rocket silo 's single output slot. |

### Filtered stacks

Stacks can be filtered either by default (in burner-type entities, furnaces , roboports , turrets , labs , and other entities that can only accept one or a few item types in a particular slot), or manually by the player (normally set via the middle mouse button / scroll-wheel click, see Keyboard bindings ). Manual filtering is available for cargo wagons , cars , tanks , spidertrons and the player inventory, but not for other types of containers (in particular, chests of any type).

This can be used to ensure only one item type goes into the inventory space. Inserters (or bots , where applicable) will not attempt to insert anything except the allowed item type into filtered slots, and manual insertion of other item types by the player is also not allowed unless and until the filter is cleared.

### Damaged items

Damaged items (i.e, damaged entities now stored as items) stack with other damaged items (of the same type), but not with undamaged items. When items with different amounts of damage are stacked together, the health of the items is averaged.

### Items with durability

Items with durability, such as science packs and repair packs , always stack with items of the same type, regardless of how much durability remains. The durability displayed on the stack is the durability of the first item. After that item is removed from the stack, a stack of items with full durabilities remains. This means that when multiple items with durabilities are stacked together, their durabilities are merged, which can result in a lower overall item count while the overall remaining durability stays the same.

## Stack size bonuses

Inserters and logistic robots can be boosted with research to hold and transfer more items, see:

- Inserter capacity bonus (research)
- Worker robot cargo size (research)

## Stack limitation

Optionally, the usable space in chests and wagons can be decreased below their default values. Typically, this is done to store a small amount of items in an automated process, without consuming the resources that would be required to fill the entire container.

To limit a container, click the red X at the end of the last stack. Then, click on one of the stacks to set the new limit. The unused stacks will be highlighted red (see right).

When full, inserters will no longer add to a limited container. However, the player is still free to manually place items in the unused (red) slots.

## Handling stacks

There are some keyboard bindings to quickly handle movement of stacks between inventories, like moving half of a stack to another stack.

## History

In game version 0.10, the number of items which can be stored in a stack changed for most items from powers of 2 to multiples of 10. This change was mainly made because most people find it more intuitive to calculate numbers in a base-10 system.

Example: Before the change, a stack could store 64 iron ore, while after the change it is 50. This created some controversy, as some players preferred the old stack sizes.
