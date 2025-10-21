---
title: Nuclear reactor - Factorio Wiki
source: https://wiki.factorio.com/Nuclear_reactor
scraped_at: 2025-10-21 15:47:13
tags: [web, documentation]
---

# Nuclear reactor - Factorio Wiki

**Source:** [https://wiki.factorio.com/Nuclear_reactor](https://wiki.factorio.com/Nuclear_reactor)


|  | Nuclear reactor | Edit |

| Recipe |
| 8 + 500 + 500 + 500 + 500 → 1 |
| Total raw |
| 4.8k + 500 + 3k + 1k + 1k + 500 |
| Map color |  |
| Health | 500 650 800 950 1250 |  |  | 500 |  | 650 |  | 800 |  | 950 |  | 1250 |
|  |  | 500 |
|  | 650 |  | 800 |
|  | 950 |  | 1250 |
| Stack size | 10 |
| Rocket capacity | 1 (0.1 stacks) |
| Dimensions | 5×5 |
| Energy consumption | 40 52 64 76 100 MW ( burner ) |  |  | 40 |  | 52 |  | 64 |  | 76 |  | 100 |
|  |  | 40 |
|  | 52 |  | 64 |
|  | 76 |  | 100 |
| Heat output | 40 52 64 76 100 MW |  |  | 40 |  | 52 |  | 64 |  | 76 |  | 100 |
|  |  | 40 |
|  | 52 |  | 64 |
|  | 76 |  | 100 |
| Maximum temperature | 1000 °C |
| Mining time | 0.5 |
| Prototype type | reactor |
| Internal name | nuclear-reactor |
| Required technologies |
|  |
| Produced by |
|  |
| Valid fuel |
|  |

The nuclear reactor generates heat by burning uranium fuel cells . Heat can be consumed by heat exchangers to produce 500°C steam , which can be consumed by steam turbines to produce electricity.

Unlike boilers , a nuclear reactor will continue to burn fuel regardless of heat consumption. A uranium fuel cells burns for 200 seconds. The maximum temperature of a nuclear reactor is 1000°C, and once reached, excess heat energy from the uranium fuel cell is wasted. To prevent wasting fuel, the temperature of a reactor can be read to a circuit network and used to enable fuel inserters only when the temperature is relatively low. More heat energy can be stored by placing extra heat pipes. Alternatively, energy can be stored as steam in storage tanks or as electricity in accumulators , which can also be read to control fuel inserters.

Rather than completely consuming fuel, burning a uranium fuel cell results in a depleted uranium fuel cell . These must be removed, else the reactor will stop consuming fuel. Depleted fuel cells can be reprocessed in a centrifuge to recover some uranium-238 .

Nuclear reactors have a heat capacity of 10 MJ/°C. Thus, they can buffer 5 GJ of heat energy across their working range of 500°C to 1000°C, and require 4.85 GJ of energy to warm up from 15°C to 500°C when initially placed.

## Contents

- 1 Neighbour bonus 1.1 Double-row layout 1.2 Square layout
- 2 Explosion
- 3 History
- 4 See also

## Neighbour bonus

Reactors receive a bonus for adjacent operating reactors, which increases their effective thermal output by 100% per each such link. For example, two reactors operating next to each other will output a total of 160 MW of thermal energy, with each reactor producing 40 MW base and receiving 40 MW of neighbour bonus.

The Neighbour bonus only applies if:

- 2 reactors are directly adjacent to each other with all 3 heat connections directly connecting the two.
- Both reactors are fueled.

### Double-row layout

The most efficient practical layout is an aligned double row of arbitrary length (number of reactors as needed). For even numbers of reactors, the total output of the array is 160n − 160 MW (where n = total number of reactors, and assuming all are fueled). Splitting the row, while possibly logistically beneficial, reduces total power output by 160 MW per split.

Odd numbers of reactors are inefficient in maximizing the bonus, but, if needed, the odd reactor should be aligned with one of the rows. Offsetting the longer row instead would not gain the extra reactor any bonus, while the reactor on the other end of the same row would lose its bonus as well. Placing the odd reactor between the ends of aligned rows would also lead to one fewer bonus, and also make the design un-tileable.

In any case however, such concerns are unlikely to arise until one has a very large base, as the individual output of reactors is massive, particularly with neighbour bonuses. As an example, a 5×2 reactor grid would produce 1,440 MW (1.44 GW), the equivalent of 1,600 steam engines, or 24,000 solar panels.

### Square layout

Theoretically, a perfectly square grid of reactors with no spaces between would provide maximum bonus, as it minimizes the number of reactors with unlinked sides. This setup produces 200n − 160×sqrt(n) MW (where sqrt(n) is the square root of the number of reactors).

However, while the heat pipe links will allow energy flow from reactors within the square, with no room around inner reactors, there will be no way to insert and remove fuel cells except manually (heat pipes are traversable by the player), which makes this setup impractical.

Furthermore, the gains compared to the double-row design are not large. After some calculation, one arrives at the expression for the ratio of the two (double-row design in denominator) as (1.25n − sqrt(n)) ÷ (n − 1) which evaluates to, for example, 1 for 4 reactors, 1.07 for 16 reactors, 1.16 for 100 reactors (considering only numbers that both an equal-length double row and a square can be built from), and so on. In the limit (infinite number of reactors), the ratio approaches 1.25 as the edge corrections become insignificant.

## Explosion

If a reactor is destroyed (by damage) while it is above 900°C, it will explode, having the same effects of an atomic bomb . This includes terrain modification in Space Age , such as creating lava lakes on Vulcanus and ammoniacal solution lakes on Aquilo .

This explosion has enough power to destroy nearby reactors, so one explosion can lead to a chain reaction of exploding reactors. [1]

## History

- 0.18.0 : Updated sound effects.

- 0.17.67 : Heat pipes (also in reactors and heat exchangers) glow with high temperatures.

- 0.16.0 : Changed nuclear reactor stack size to 10.

- 0.15.0 : Introduced

## See also

- Power production
- Heat pipe
- Steam turbine
- Comprehensive guide on nuclear power

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
