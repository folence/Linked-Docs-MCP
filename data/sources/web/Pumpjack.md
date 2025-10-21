---
title: Pumpjack - Factorio Wiki
source: https://wiki.factorio.com/Pumpjack
scraped_at: 2025-10-21 15:47:24
tags: [web, documentation]
---

# Pumpjack - Factorio Wiki

**Source:** [https://wiki.factorio.com/Pumpjack](https://wiki.factorio.com/Pumpjack)


|  | Pumpjack | Edit |

| Recipe |
| 5 + 5 + 10 + 10 + 5 → 1 |
| Total raw |
| 21.25 + 7.5 + 35 + 5 |
| Map color |  |
| Fluid storage volume | 1000 |
| Health | 200 260 320 380 500 |  |  | 200 |  | 260 |  | 320 |  | 380 |  | 500 |
|  |  | 200 |
|  | 260 |  | 320 |
|  | 380 |  | 500 |
| Stack size | 20 |
| Rocket capacity | 20 |
| Dimensions | 3×3 |
| Energy consumption | 90 kW ( electric ) |
| Mining time | 0.5 |
| Mining speed | 1 |
| Mining area | 1 tiles |
| Resource drain | 100% 83% 66% 50% 16% |  |  | 100% |  | 83% |  | 66% |  | 50% |  | 16% |
|  |  | 100% |
|  | 83% |  | 66% |
|  | 50% |  | 16% |
| Pollution | 10/m |
| Module slots | 2 slots |
| Prototype type | mining-drill |
| Internal name | pumpjack |
| Required technologies |
|  |
| Boosting technologies |
|  |
| Produced by |
|  |

Pumpjacks extract fluids from resource fields. Each field can be covered by only one pumpjack at a fixed spot. The pumpjack will then output an amount of fluid equal to 10 multiplied by the field's yield per second. For example, a field with 538% yield will generate 54 fluid per second. Without speed modules , one pumpjack cycle takes one second to complete.

Extracting fluid lowers the field's yield by 1% per 300 pumpjack cycles, to a minimum of 20% of the initial yield or 2 fluid per second, whichever is larger.

They are limited to a maximum output of 1000 fluid per cycle, achieved by a field with more than 9999% yield. However, such a high yield is rare with standard map generator settings.

Pumpjacks can only be placed on fluid resource field tiles. Furthermore, the output pipe location is fixed relative to the pumpjack's orientation.

In the base game, the only kind of resource field yields crude oil . In Space Age , the pumpjack can also extract sulfuric acid from Vulcanus , as well as fluorine and lithium brine from Aquilo .

Lithium brine resource fields are special; unlike the other resource fields, these can run out. These patches do not display a percentage; they instead report the total amount of fluid in the field. They also do not produce less fluid over time. A pumpjack will always produce the same amount of fluid per second on any lithium brine field until it is exhausted: 60 fluid per cycle.

## Contents

- 1 Tips
- 2 Gallery
- 3 History
- 4 See also

## Tips

A resource field that has depleted (to the minimum of 20%) can still make use of speed modules , which are thus a good option for raising the pumpjack's output. With two speed module 3s , the output doubles from 2 to 4 fluid per second. With two legendary speed module 3s, the output increases by a factor of 3.5 from 2 to 7 fluid per second.

The formula to determine the modified output is:

```
Output of unmodified pumpjack x (1 + number of modules in pumpjack x average module bonus + transmission strength x number of modules in each beacon x average module bonus)
```

Example:

For a pumpjack on a depleted resource field with two level 3 speed modules and 4 beacons with each two level 3 speed modules:

```
2 x (1 + 2 x 0.5 + √4 x 1.5 x 2 x 0.5) = 10 fluid per second.
```

Assuming that there will be always two speed 3 modules equipped in the pumpjack and beacons, the formula for 4 beacons can be shortened:

```
2 x (2 + √4 x 1.5) = 10 fluid per second.
```

## Gallery

- Animation of different speeds of pumpjacks: one with two speed modules, one with no modules and one with two production modules. (Click to see GIF animation)

## History

- 0.15.0 : Pumpjacks can be turned on and off using the circuit network. They can also output the current oil mining rate.

- 0.9.0 : Introduced

## See also

- Fluid system

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
