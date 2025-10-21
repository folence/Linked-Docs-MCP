---
title: Heat exchanger - Factorio Wiki
source: https://wiki.factorio.com/Heat_exchanger
scraped_at: 2025-10-21 15:47:16
tags: [web, documentation]
---

# Heat exchanger - Factorio Wiki

**Source:** [https://wiki.factorio.com/Heat_exchanger](https://wiki.factorio.com/Heat_exchanger)


|  | Heat exchanger | Edit |

- Base game
- Space Age mod

| Recipe |
| 3 + 100 + 10 + 10 → 1 |
| Total raw |
| 8 + 100 + 10 + 10 |
| Map color |  |
| Fluid storage volume | Input: 200 Output: 200 |
| Health | 200 260 320 380 500 |  |  | 200 |  | 260 |  | 320 |  | 380 |  | 500 |
|  |  | 200 |
|  | 260 |  | 320 |
|  | 380 |  | 500 |
| Resistances | Explosion: 0/30% Fire: 0/90% Impact: 0/30% |
| Stack size | 50 |
| Rocket capacity | 25 (0.5 stacks) |
| Dimensions | 2×3 |
| Energy consumption | 10 13 16 19 25 MW ( heat ) |  |  | 10 |  | 13 |  | 16 |  | 19 |  | 25 |
|  |  | 10 |
|  | 13 |  | 16 |
|  | 19 |  | 25 |
| Heat output | 103/s 134/s 165/s 196/s 258/s steam |  |  | 103/s |  | 134/s |  | 165/s |  | 196/s |  | 258/s |
|  |  | 103/s |
|  | 134/s |  | 165/s |
|  | 196/s |  | 258/s |
| Maximum temperature | 1000 °C |
| Fluid consumption | 10.3/s 13.4/s 16.5/s 19.6/s 25.8/s water |  |  | 10.3/s |  | 13.4/s |  | 16.5/s |  | 19.6/s |  | 25.8/s |
|  |  | 10.3/s |
|  | 13.4/s |  | 16.5/s |
|  | 19.6/s |  | 25.8/s |
| Mining time | 0.1 |
| Prototype type | boiler |
| Internal name | heat-exchanger |
| Required technologies |
|  |
| Produced by |
|  |

| Recipe |
| 3 + 100 + 10 + 10 → 1 |
| Total raw |
| 8 + 100 + 10 + 10 |
| Map color |  |
| Fluid storage volume | Input: 200 Output: 200 |
| Health | 200 260 320 380 500 |  |  | 200 |  | 260 |  | 320 |  | 380 |  | 500 |
|  |  | 200 |
|  | 260 |  | 320 |
|  | 380 |  | 500 |
| Resistances | Explosion: 0/30% Fire: 0/90% Impact: 0/30% |
| Stack size | 50 |
| Rocket capacity | 25 (0.5 stacks) |
| Dimensions | 2×3 |
| Energy consumption | 10 13 16 19 25 MW ( heat ) |  |  | 10 |  | 13 |  | 16 |  | 19 |  | 25 |
|  |  | 10 |
|  | 13 |  | 16 |
|  | 19 |  | 25 |
| Heat output | 103/s 134/s 165/s 196/s 258/s steam |  |  | 103/s |  | 134/s |  | 165/s |  | 196/s |  | 258/s |
|  |  | 103/s |
|  | 134/s |  | 165/s |
|  | 196/s |  | 258/s |
| Maximum temperature | 1000 °C |
| Fluid consumption | 10.3/s 13.4/s 16.5/s 19.6/s 25.8/s water |  |  | 10.3/s |  | 13.4/s |  | 16.5/s |  | 19.6/s |  | 25.8/s |
|  |  | 10.3/s |
|  | 13.4/s |  | 16.5/s |
|  | 19.6/s |  | 25.8/s |
| Mining time | 0.1 |
| Prototype type | boiler |
| Internal name | heat-exchanger |
| Required technologies |
|  |
| Produced by |
|  |

The heat exchanger exchanges heat between a heat connection (normally from a heat pipe leading to a nuclear reactor or heating tower ) and water to produce steam .

Heat exchangers produce ~103 steam with a temperature of 500°C every second.

Heat exchangers will not produce steam until they reach 500°C. The steam produced is exactly 500°C hot, even if the exchanger is hotter. Heat exchangers have a heat capacity of 1 MJ/°C. Thus, they can buffer 500 MJ of heat energy across their working range of 500°C to 1000°C, and require 485 MJ of energy to warm up from 15°C to 500°C when initially placed.

## Calculating steam production rate

Heat exchangers produce 103 steam/second. This can be calculated by relying on steam turbine data: A steam turbine consumes 60 steam/second and produces 5.82MW (assuming 500°C steam). This means a single unit of 500°C steam has 5.82MW / (60/s) = 0.097 MJ of energy. A heat exchanger produces 10 MJ a second, therefore it produces 10MJ / 0.097MJ = 103.0927835 steam per second.

The steam production rate can also be calculated using the energy consumption: 1 heat exchanger consumes 10MW, so it's putting 10MJ of energy into heating water/steam per second. To heat up 1 unit of steam 1 degree, 200 joules are needed, so the heat exchanger is heating up water by 50,000 unit-°C in total. We observe that this heating results in a temperature increase from 15°C to 500°C, so an increase of 485°C. So the 50,000 unit-°C is divided among 103 units of steam per second, since 50,000 / 485 = 103.09 . Since steam is produced from water in a 10:1 ratio, this also means that 10.3 units of water are consumed per second.

## History

- 2.0.7 : 1 Water will now produce 10 Steam in boilers/heat exchangers.

- 0.17.67 : Heat pipes (also in reactors and heat exchangers) glow with high temperatures.

- 0.15.0 : Introduced Doubled the heat capacity of water from 0.1kJ per degree per liter to 0.2kJ

## See also

- Nuclear power
- Steam turbine
- Nuclear reactor
- Heating tower
- Heat pipe

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
