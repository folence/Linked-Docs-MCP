---
title: Recycler - Factorio Wiki
source: https://wiki.factorio.com/Recycler
scraped_at: 2025-10-21 15:47:29
tags: [web, documentation]
---

# Recycler - Factorio Wiki

**Source:** [https://wiki.factorio.com/Recycler](https://wiki.factorio.com/Recycler)


|  | Recycler | Edit |

| Recipe |
| 3 + 20 + 40 + 6 + 20 → 1 |
| Total raw |
| 23 + 20 + 80 + 6 + 20 |
| Map color |  |
| Health | 300 390 480 570 750 |  |  | 300 |  | 390 |  | 480 |  | 570 |  | 750 |
|  |  | 300 |
|  | 390 |  | 480 |
|  | 570 |  | 750 |
| Resistances | Fire: 0/80% |
| Stack size | 20 |
| Rocket capacity | 10 |
| Dimensions | 4×2 |
| Energy consumption | 186 kW ( electric ) |
| Drain | 6.0 kW ( electric ) |
| Crafting speed | 0.5 0.65 0.8 0.95 1.25 |  |  | 0.5 |  | 0.65 |  | 0.8 |  | 0.95 |  | 1.25 |
|  |  | 0.5 |
|  | 0.65 |  | 0.8 |
|  | 0.95 |  | 1.25 |
| Mining time | 0.2 |
| Pollution | 2/m |
| Crafted only on |  |
| Module slots | 4 slots |
| Prototype type | furnace |
| Internal name | recycler |
| Required technologies |
|  |
| Produced by |
|  |

Space Age expansion exclusive feature.

The recycler is a building that can convert most items into the ingredients used in their recipes, at the cost of losing 75% of said ingredients. In other words, it performs a lossy reversal of crafting.

Although it can only be crafted on Fulgora, it can be transported to be placed on other planets or space platforms . When the quality mod (which provides the recycler) is used without the Space Age mod, the recycler can be crafted on Nauvis and the research has different prerequisites.

The recycler has 4 module slots, but it cannot use productivity modules .

## Contents

- 1 Mechanics 1.1 Non-recyclable items 1.2 Unique recycling recipes 1.3 Stats 1.4 Technical details
- 2 Trivia
- 3 Gallery
- 4 History
- 5 See also

## Mechanics

When an item enters a recycler, the item's main recipe is found, and the recycler is automatically set to perform its inverse.

For each type of item used as an ingredient in the recycled item's main recipe, the number of items returned by the recycler is decided by ⌊ 0 . 2 5 ⋅ i o + r ⌋ , where i is the number of items used as ingredients, o is the number of items returned by the recipe, and r is a random number that is greater than or equal to 0 but less than 1. On average, this returns exactly 25% of the items needed to craft one item of the same type as the recycled item. For example, recycling a processing unit always gives 5 electronic circuits while having a 50% chance of returning one advanced circuit .

All fluid ingredients are lost when recycling, as the recycler has no fluid output.

Without quality modules, the resulting items have the same quality as the item being recycled, even if the latter was crafted using lower-quality ingredients. Quality modules can further increase the output's quality, just like with regular non-recycling recipes.

The recycler has 12 internal slots for its output, but can only hold one stack of each item. The recycler will try to eject the contents of these slots, much like a mining drill. It is therefore not necessary to use an inserter to collect its output. Much like the big mining drill , if the recycler has more than one of an individual item type in its inventory, the recycler will output stacks of materials onto a belt if the stack inserter has been researched.

### Non-recyclable items

The broad rule governing the recycler's ability to reverse a recipe is that it can only reverse recipes made in assembling machines of some type. There are many exceptions to this, however. For the purposes of the recycler's ability to recycle items, the electromagnetic plant counts as an "assembler". So all of its recipes count unless otherwise stated. Recipes shared by assemblers and other machines are not so clear-cut: sometimes they count as recipes for those other machines, but sometimes they count as pure assembler recipes.

Items can have multiple recipes; all that is needed for the recycler to reverse it is to find a single reversible recipe that produces that item.

If no valid recipe producing the item can be reversed, the recycler will return the same item 25% of the time (possibly with a quality bonus if the appropriate modules are used), with the other 75% destroying the item. The in-game description says "Other items are ... turned to spoilage if they were biological." Despite this, only nutrients are turned to spoilage. Most other apparently biological items, such as jelly , eggs, or biolabs , get returned 25% of the time, as listed (or not listed, since eggs cannot be created in assemblers) in the table below.

Recipes which can be made in an assembler (possibly also in non-assembler buildings) which cannot be reversed:

| Recycler Input | Time | Rate |
| Automation science pack | 0.625s | 1.6/s |
| Logistic science pack | 0.75s | 1.33/s |
| Military science pack | 1.25s | 0.8/s |
| Chemical science pack | 3s | 0.33/s |
| Production science pack | 2.625s | 0.38/s |
| Utility science pack | 2.625s | 0.38/s |
| Space science pack | 1.875s | 0.53/s |
| Electromagnetic science pack | 1.25s | 0.8/s |
| Biolab | 1.25s | 0.8/s |
| Holmium plate | 0.125s | 8/s |
| Landfill | 0.0625s | 16/s |
| Superconductor | 0.625s | 1.6/s |
| Tungsten carbide | 0.125s | 8/s |
| Uranium fuel cell | 1.25s | 0.8/s |
| Wood processing | 0.25 | 4/s |
| Yumako mash | 0.125s | 8/s |
| Jelly | 0.125s | 8/s |
| Iron bacteria | 0.125s | 8/s |
| Copper bacteria | 0.125s | 8/s |

Recipes exclusively executed by non-assembler machines, but can still be reversed:

| Recycler Input | Time | Rate |
| Battery | 0.5s | 2/s |
| Big mining drill | 3.75s | 0.27/s |
| Fusion reactor | 7.5s | 0.13/s |
| Fusion generator | 3.75s | 0.27/s |
| Railgun | 1.25s | 0.8/s |
| Railgun turret | 1.25s | 0.8/s |
| Turbo transport belt | 0.0625s | 16/s |
| Turbo underground belt | 0.25s | 4/s |
| Turbo splitter | 0.25s | 4/s |

Recipes shared by assembler/EMP and non-assembler machines which can be reversed:

| Recycler Input | Time | Rate |
| Biochamber | 2.5s | 0.4/s |
| Cryogenic plant | 1.25s | 0.8/s |
| Foundry | 1.25s | 0.8/s |
| Nutrients from spoilage | 0.25s | 4/s |

### Unique recycling recipes

Some items have unique recycling recipes:

- Recycling scrap will perform the scrap recycling recipe, for which there is no inverse, as scrap cannot be crafted. This is used to obtain most resources on Fulgora .
- Recycling nutrients will yield 2.5× that amount of spoilage , as if they were made using the nutrients from spoilage recipe.

### Stats

The recycling recipe for an item, other than scrap, is equal to 1/16th (0.0625) of the time it takes to craft that item. (Items without recipes, such as ore, are treated as having a crafting time of 0.5 seconds.) However, because the recycler has a base crafting speed of 0.5, the time it takes one recycler to recycle one item without modules or beacons is effectively 1/8th (0.125) of the item's crafting time. For example, the time it takes to craft a steel plate in a stone furnace (which has a crafting speed of 1) is 16 seconds, and so recycling a steel plate takes 2 seconds. Some items with long crafting times (most notably steel plates and concrete ) can be processed much more quickly by crafting them into other items and then recycling the result instead.

The following table provides some examples of how long it takes a recycler without modules or beacons to recycle one of that item, and the rate at which it recycles those items.

| Recycler input | Time | Rate |
| Steel plate | 2.0s | 0.5/s |
| Low density structure | 1.875s | 0.533/s |
| Processing unit | 1.25s | 0.8/s |
| Concrete | 1.25s | 0.8/s |
| Advanced circuit | 0.75s | 1.33/s |
| Copper plate | 0.4s | 2.5/s |
| Steel chest | 0.0625s | 16/s |
| Iron ore | 0.0625s | 16/s |
| Hazard concrete | 0.03125s | 32/s |

The scrap recycling recipe takes 0.2 seconds, meaning that it actually takes 0.4 seconds to run in a recycler, so a recycler takes in 2.5 scrap/s. The output rates are as follows:

| Input | Output | Chance | Rate |
| Scrap | Iron gear wheel | 20% | 0.5/s |
| Solid fuel | 7% | 0.175/s |
| Concrete | 6% | 0.15/s |
| Ice | 5% | 0.125/s |
| Steel plate | 4% | 0.1/s |
| Battery | 4% | 0.1/s |
| Stone | 4% | 0.1/s |
| Copper cable | 3% | 0.075/s |
| Advanced circuit | 3% | 0.075/s |
| Processing unit | 2% | 0.05/s |
| Low density structure | 1% | 0.025/s |
| Holmium ore | 1% | 0.025/s |

In total, the recycler spits out 1.5 items/s, meaning 10 recyclers are just enough to saturate a yellow belt. The output values are increased by scrap recycling productivity research .

### Technical details

Internally, the recycler uses the furnace prototype , which performs recipes that are automatically selected based on input ingredients. Every item in the game has its own "recycling" recipe, those recipes can only be performed by a recycler.

Since there are hundreds of items in the game, as well as to ensure compatibility with third-party mods, most recycling recipes are not explicitly defined. Instead, recycling recipes are procedurally generated based on existing recipes. Depending on whether or not the item is deemed "recyclable", these procedurally generated recipes will either output a quarter of an item's ingredients or have a 25% chance of outputting the item itself.

The recyclabillity of most items is based on the category of their recipes, with some exceptions being explicitly filtered by the name of the recipe's prototype. Furthermore, items with multiple viable recycling recipes are made non-recyclable to avoid ambiguity, and recipes with multiple different products will fail to generate a recycling recipe, thereby making them irreversible as a default. Third-party mods can also explicitly make a recipe irreversible by setting the recipe's auto_recycle field to false .

The scrap recycling recipe is a special case, as it is the only hard-coded recipe. It is also the only recycling recipe that is not hidden from the player, and which can be performed without a recycler. (Notably, this recipe is defined by the Space Age mod rather than the Quality mod, as scrap is exclusive to the former.)

The generation of recycling recipes, as well as the filtering of non-recyclable recipes, is defined by the file recycling.lua in the Quality mod's prototype folder. More specifically, the function default_can_recycle decides whether a given recipe can be recycled or not, and the function add_recipe_values does most of the configuration of recycling recipes, which includes setting the products of these recipes and how long they take to perform.

## Trivia

- If the recycled item has a fluid ingredient, then the smoke emitted from the recycler matches the fluid in colour.

## Gallery

## History

- 2.0.7 : Introduced in Space Age expansion.

## See also

- Quality
- Tutorial:Scrap recycling strategies

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
