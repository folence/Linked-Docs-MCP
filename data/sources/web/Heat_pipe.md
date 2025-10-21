---
title: Heat pipe - Factorio Wiki
source: https://wiki.factorio.com/Heat_pipe
scraped_at: 2025-10-21 15:47:15
tags: [web, documentation]
---

# Heat pipe - Factorio Wiki

**Source:** [https://wiki.factorio.com/Heat_pipe](https://wiki.factorio.com/Heat_pipe)


|  | Heat pipe | Edit |

- Base game
- Space Age mod

| Recipe |
| 1 + 20 + 10 → 1 |
| Total raw |
| 1 + 20 + 10 |
| Map color |  |
| Health | 200 260 320 380 500 |  |  | 200 |  | 260 |  | 320 |  | 380 |  | 500 |
|  |  | 200 |
|  | 260 |  | 320 |
|  | 380 |  | 500 |
| Resistances | Explosion: 0/30% Fire: 0/90% Impact: 0/30% |
| Stack size | 50 |
| Rocket capacity | 50 (1 stack) |
| Dimensions | 1×1 |
| Maximum temperature | 1000 °C |
| Mining time | 0.1 |
| Prototype type | heat-pipe |
| Internal name | heat-pipe |
| Required technologies |
|  |
| Produced by |
|  |

| Recipe |
| 1 + 20 + 10 → 1 |
| Total raw |
| 1 + 20 + 10 |
| Map color |  |
| Health | 200 260 320 380 500 |  |  | 200 |  | 260 |  | 320 |  | 380 |  | 500 |
|  |  | 200 |
|  | 260 |  | 320 |
|  | 380 |  | 500 |
| Resistances | Explosion: 0/30% Fire: 0/90% Impact: 0/30% |
| Stack size | 50 |
| Rocket capacity | 50 (1 stack) |
| Dimensions | 1×1 |
| Maximum temperature | 1000 °C |
| Mining time | 0.1 |
| Prototype type | heat-pipe |
| Internal name | heat-pipe |
| Required technologies |
|  |
| Produced by |
|  |

The heat pipe can transport heat over longer distances and connect devices which produce and use heat. Currently, this is limited to heat exchangers , nuclear reactors , and heating towers .

Heat pipes have a heat capacity of 1 MJ/°C. Thus, they can theoretically buffer 500 MJ of heat energy across their working range of 500°C to 1000°C, making them a space-efficient energy store. However, because temperature needs a drop of greater than 1 degree before it will "flow," you can't raise them all the way to 1000°C or drain them all the way to 500°C, so the practical energy capacity will depend on the layout.

As heat pipes rise in temperature, they will give off a very low-distance glow.

On the planet Aquilo , heat pipes are a necessity due to the freezing temperatures. If buildings are not adjacent to heat pipes (or similar objects) with a temperature of at least 30°C, the building will freeze and stop working.

## Heat pipe throughput

Each heat pipe holds an amount of heat energy, and there is a limit to how much energy can go through each of them for a given duration.

For any heat pipe entity with one input connection on one side and one output connection on another, this entity will lower the temperature by 1 + (P / 15) °C with P being the power going through this entity expressed in MW.

A heat exchanger must heat up to 500°C before it can generate steam. And the maximum temperature of a heat generator (such as a nuclear reactor) is 1000°C. As such, the temperature difference between a heat source and the heat exchanger is at most 500°C. We can thus express the maximum length of a straight line of heat pipe as 500 / (1 + P/15) .

For example let's take a single nuclear reactor outputting 40MW of heat power to a single line of heat pipes. The furthest that line can go is 500 / (1 + 40/15) which is around 136 heat pipes long.

A nuclear reactor can also be used to transfer heat in a similar manner as a heat pipe, whether or not it is fueled. In this case, the reactor will drop the temperature by 1 + (P / 387) °C , with P again being the power in MW going through the entity. Note that this is an approximation, the actual value measured is supposed to be 200000/517 or about 386.847.

That being said, the nuclear reactor entity is also much bigger, meaning that we must compare it to 5 lines of 5 heat pipes instead of just a single one. The nuclear reactor will thus lower the temperature 5 times less with near-zero power going through it, and nearly 26 times less when approaching infinite power, compared to those lines of heat pipes.

As an example, a single line of 100 nuclear reactors (or 500 tiles) will only lower the temperature by about 360°C while carrying 1GW.

In Space Age , on Aquilo , heat pipes are used to prevent entities from freezing . They automatically transfer heat into neighboring entities. Different entities consume different amounts of heat to prevent freezing, but they do not have the temperature requirements of a heat exchanger. Heat pipes only need to be at least 30°C to keep an entity warm. Also, heat pipes do not lose heat to the environment; they only lose heat to entities that need to be kept warm.

## History

- 0.17.67 : Heat pipes (also in reactors and heat exchangers) glow with high temperatures.

- 0.15.11 : Changed heat transfer mechanics, prior to this heat would flow better following the order of heat pipe placement

- 0.15.0 : Introduced

## See also

- Power production
- Heating tower
- Heat exchanger

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
