---
title: Burner inserter - Factorio Wiki
source: https://wiki.factorio.com/Burner_inserter
scraped_at: 2025-10-21 14:30:18
tags: [web, documentation]
---

# Burner inserter - Factorio Wiki

**Source:** [https://wiki.factorio.com/Burner_inserter](https://wiki.factorio.com/Burner_inserter)


|  | Burner inserter | Edit |

| Recipe |
| 0.5 + 1 + 1 → 1 |
| Total raw |
| 1 + 3 |
| Map color |  |
| Health | 100 130 160 190 250 |  |  | 100 |  | 130 |  | 160 |  | 190 |  | 250 |
|  |  | 100 |
|  | 130 |  | 160 |
|  | 190 |  | 250 |
| Resistances | Fire: 0/90% |
| Stack size | 50 |
| Rocket capacity | 50 |
| Dimensions | 1×1 |
| Energy consumption | 144 187 230 274 360 kW ( burner ) |  |  | 144 |  | 187 |  | 230 |  | 274 |  | 360 |
|  |  | 144 |
|  | 187 |  | 230 |
|  | 274 |  | 360 |
| Rotation speed | 281°/s 365°/s 449°/s 534°/s 702°/s |  |  | 281°/s |  | 365°/s |  | 449°/s |  | 534°/s |  | 702°/s |
|  |  | 281°/s |
|  | 365°/s |  | 449°/s |
|  | 534°/s |  | 702°/s |
| Mining time | 0.1 |
| Prototype type | inserter |
| Internal name | burner-inserter |
| Boosting technologies |
|  |
| Produced by |
|  |
| Valid fuel |
|  |

The burner inserter is the most basic and slowest type of inserters . It is powered by burning fuel , compared to the more advanced inserters which are powered by electricity . It will add fuel to its own supply if it picks any up, which makes it useful for filling boilers with coal . This has the advantage that it will continue working even if the power fails, as opposed to electrically-powered inserters which will be unable to function. It consumes no fuel while idle, though it consumes vastly more energy than most other inserters when active.

Even though it doesn't use electricity, a burner inserter can be connected to and controlled by the logistic and the circuit network .

Burner Inserters do not directly produce any pollution in their operation. A common misconception implied by the early game is anything that runs on burner power must be polluting (e.g. burner miner, boiler, furnace, etc.). Pollution is only ever produced by buildings, not entities like inserters or vehicles, and non burning buildings like assemblers also pollute. For more information reference the dedicated page on Pollution. Burner Inserters can still indirectly contribute to pollution significantly by consuming excessive amounts of fuel, which costs pollution to gather, so be mindful of that.

## Fuel consumption

A burner inserter consumes no power while idle and does not continuously consume the maximum amount of power when working. Burner Inserters spawn with an internal energy buffer of 500 kJ, represented as 25% the value of a piece of wood fuel (which is 2MJ). Aside from not having drain, all its other power characteristics are identical to the rest of the inserters. It simply pulls its joules from its fuel rather than your power grid. For more detailed information on inserter power characteristics you can reference the main page here .

Burners also have a behavior known as "leeching" where they will pull fuel from their input and commandeer it for their own use. This leeching behavior is not exactly quantified, but it is triggered whenever the internal fuel inventory reaches zero, and performing the action also consumes fuel since motion is never free.

## History

- 2.0.7 : All inserters now have filter option. Energy consumption increased from 94.2 kW to 144 kW. Burner inserters now reliably pick up items off of fast transport belts and express transport belts .

- 0.13.2 : Inserters connected to the circuit network now have the option to only read hand contents.

- 0.13.0 : Inserters can now send the item held in hand to the circuit network. Inserters are able to squeeze things slightly better to belts. All types of inserters can be controlled by the circuit and logistic network, once the respective network is researched.

- 0.12.16 : Improved burner inserter's fuel searching logic; it will now search both transport belt lines for fuel

- 0.12.11 : Burner inserter now grabs fuel for itself even if the target doesn't need it

- 0.12.2 : Inserters will never take more than the max stack size of an item. Inserters and logistic robots no longer extract from enemy chests Inserters now correctly pick up items from splitters

- 0.12.1 : Burner inserters start with enough energy to pick up 1 item and fuel themselves.

- 0.12.0 : Inserters can now extract from roboports and beacons. Inserters now take items from right behind them, not from the center of the pickup target entity.

- 0.10.0 : New icon New sounds

- 0.9.2 : Inserters can have arbitrary pickup and insert positions.

- 0.9.0 : Inserter code optimisation, inserters that have nothing to do will sleep.

- 0.8.0 : Improved inserter's ability to pull from train wagons.

- 0.7.1 : Fast inserter now has the same speed as the smart inserter.

- 0.5.0 : Inserter can now pick up up to 5 items when researched.

- 0.4.0 : Smaller inserter bounding box

- 0.3.0 : New Inserter graphics

- 0.2.1 : The item in the hand of the inserter is returned to the player when mined.

- 0.2.0 : Show direction of inserter

- 0.1.0 : Introduced

## See also

- Inserters

| Logistics |
| Storage | Wooden chest Iron chest Steel chest Storage tank |
| Belt transport system | Transport belt Fast transport belt Express transport belt Turbo transport belt ( ) Underground belt Fast underground belt Express underground belt Turbo underground belt ( ) Splitter Fast splitter Express splitter Turbo splitter ( ) |
| Inserters | Burner inserter Inserter Long-handed inserter Fast inserter Bulk inserter Stack inserter ( ) |
| Electric system & Fluid system | Small electric pole Medium electric pole Big electric pole Substation Pipe Pipe to ground Pump |
| Railway | Rail Rail ramp ( ) Rail support ( ) Train stop Rail signal Rail chain signal Locomotive Cargo wagon Fluid wagon Artillery wagon |
| Transport | Car Tank Spidertron Spidertron remote |
| Logistic network | Logistic robot Construction robot Active provider chest Passive provider chest Storage chest Buffer chest Requester chest Roboport |
| Circuit network | Lamp Red wire Green wire Arithmetic combinator Decider combinator Selector combinator Constant combinator Power switch Programmable speaker Display panel |
| Terrain | Stone brick Concrete Hazard concrete Refined concrete Refined hazard concrete Landfill Artificial yumako soil ( ) Overgrowth yumako soil ( ) Artificial jellynut soil ( ) Overgrowth jellynut soil ( ) Ice platform ( ) Foundation ( ) Cliff explosives |
| Navigation | Production Intermediate products Space ( ) Combat Technology Environment |
