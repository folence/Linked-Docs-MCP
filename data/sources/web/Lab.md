---
title: Lab - Factorio Wiki
source: https://wiki.factorio.com/Lab
scraped_at: 2025-10-21 15:47:40
tags: [web, documentation]
---

# Lab - Factorio Wiki

**Source:** [https://wiki.factorio.com/Lab](https://wiki.factorio.com/Lab)


|  | Lab | Edit |

- Base game
- Space Age mod

| Recipe |
| 2 + 10 + 10 + 4 → 1 |
| Total raw |
| 21.5 + 15 + 36 |
| Map color |  |
| Health | 150 195 240 285 375 |  |  | 150 |  | 195 |  | 240 |  | 285 |  | 375 |
|  |  | 150 |
|  | 195 |  | 240 |
|  | 285 |  | 375 |
| Stack size | 10 |
| Rocket capacity | 10 |
| Dimensions | 3×3 |
| Energy consumption | 60 kW ( electric ) |
| Research speed | 1 1.3 1.6 1.9 2.5 |  |  | 1 |  | 1.3 |  | 1.6 |  | 1.9 |  | 2.5 |
|  |  | 1 |
|  | 1.3 |  | 1.6 |
|  | 1.9 |  | 2.5 |
| Mining time | 0.2 |
| Module slots | 2 slots |
| Prototype type | lab |
| Internal name | lab |
| Required technologies |
|  |
| Boosting technologies |
|  |
| Produced by |
|  |

| Recipe |
| 2 + 10 + 10 + 4 → 1 |
| Total raw |
| 21.5 + 15 + 36 |
| Map color |  |
| Health | 150 195 240 285 375 |  |  | 150 |  | 195 |  | 240 |  | 285 |  | 375 |
|  |  | 150 |
|  | 195 |  | 240 |
|  | 285 |  | 375 |
| Stack size | 10 |
| Rocket capacity | 10 |
| Dimensions | 3×3 |
| Energy consumption | 60 kW ( electric ) |
| Research speed | 1 1.3 1.6 1.9 2.5 |  |  | 1 |  | 1.3 |  | 1.6 |  | 1.9 |  | 2.5 |
|  |  | 1 |
|  | 1.3 |  | 1.6 |
|  | 1.9 |  | 2.5 |
| Mining time | 0.2 |
| Module slots | 2 slots |
| Prototype type | lab |
| Internal name | lab |
| Required technologies |
|  |
| Boosting technologies |
|  |
| Produced by |
|  |
| Consumed by |
|  |

Labs are buildings that perform research for technologies by consuming science packs . Use of a lab is required to progress in Factorio.

When productivity modules are used in labs, the productivity bonus is directly calculated and applied each tick so the productivity bar is simply cosmetic. This means that it does not matter that the productivity bar resets when the research is changed, no productivity bonus is lost. [1]

The player can only research one technology at a time, but can use multiple labs for faster results. The speed bonus of labs when lab research speed is researched and modules are present can be calculated using this formula: research_bonus × module_bonus = speed_bonus ; the percentage bonuses have to be converted to decimals (e.g. +140% = 2.4) before the formula is used.

Inserters can insert and remove science packs from labs. This allows chaining multiple labs together with inserters, each inserter taking science packs, as needed, from one lab and placing it into the next.

## Contents

- 1 Production requirements 1.1 Equation simplification
- 2 History
- 3 See also

## Production requirements

Calculating the number of science packs needed per second is straightforward:

- E R S = ( 1 + B [ r ] 1 0 0 ) × ( 1 + M [ r ] 1 0 0 ) × B L S
- A C T = T [ r ] E R S
- P P S = N A C T

Where:

- ERS is "effective lab research speed"
- B[r] is the speed bonus from the Lab research speed (research) , in percent
- M[r] is the sum of all module speed effects ( speed modules - positive; productivity modules - negative), in percent
- BLS is the base lab speed, which is adjusted by the quality of the lab
- ACT is "adjusted cycle time"
- T[r] is the research cycle time as displayed in the research screen
- PPS is "packs per second"
- N is the number of labs available.

Note: while the biolab has twice the speed of a regular lab, it also consumes packs half as fast. As such, the consumption rate of a biolab is the same as the consumption rate of an equal quality regular lab.

Thus, with 10 base quality standard labs, researching Nuclear Power (30 second cycle time) with Lab Research Speed 4 (140% bonus) and no module effects, the calculation is:

- E R S = 1 + 1 4 0 1 0 0 = 2 . 4
- A C T = 3 0 2 . 4 = 1 2 . 5 s
- P P S = 1 0 1 2 . 5 = 0 . 8

This means 0.8 science packs per second, of each type, would need to be produced to continuously supply the labs.

### Equation simplification

Assuming all labs have the same B[r] and BLS ), the above calculations can be combined into one equation:

- P P S = N T [ r ] × ( 1 + B [ r ] 1 0 0 ) × ( 1 + M [ r ] 1 0 0 ) × B L S

Thus for the numerical example:

- P P S = 1 0 × ( 1 + 1 4 0 1 0 0 ) × 1 3 0 = 1 0 3 0 × ( 1 + 1 . 4 ) = 1 3 × 2 . 4 = 2 . 4 3 = 0 . 8 packs per second

If trying to find the amount of labs needed to consume a given amount of packs per second, use the following rearrangement:

- N = [ ( 1 + B [ r ] 1 0 0 ) × ( 1 + M [ r ] 1 0 0 ) × B L S × 1 T [ r ] × P P S ] − 1

## History

- 0.15.12 : Lab speed info in the description contains the researched speed bonus as well.

- 0.12.6 : The research speed of a lab is now not dependent on its electricity consumption, and can be scripted.

- 0.12.0 : Lab research is now continuous; Science packs now have progress bars.

- 0.9.2 : Labs are now named after early access backers when built from blueprints .

- 0.7.2 : Changed the recipe of Lab to require 4 transport belts, down from 5.

- 0.7.0 : Added support for modules to labs.

- 0.6.0 : New graphics. Labs are dedicated to backers (displayed in entity info).

- 0.2.7 : Contents of the Lab is now shown in the entity info.

- 0.1.0 : Introduced

## See also

- Electric system
- Crafting

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
