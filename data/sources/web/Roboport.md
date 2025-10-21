---
title: Roboport - Factorio Wiki
source: https://wiki.factorio.com/Roboport
scraped_at: 2025-10-21 14:30:57
tags: [web, documentation]
---

# Roboport - Factorio Wiki

**Source:** [https://wiki.factorio.com/Roboport](https://wiki.factorio.com/Roboport)


|  | Roboport | Edit |

| Recipe |
| 5 + 45 + 45 + 45 → 1 |
| Total raw |
| 455 + 225 + 180 + 90 + 45 |
| Map color |  |
| Health | 500 650 800 950 1250 |  |  | 500 |  | 650 |  | 800 |  | 950 |  | 1250 |
|  |  | 500 |
|  | 650 |  | 800 |
|  | 950 |  | 1250 |
| Resistances | Fire: 0/60% Impact: 0/30% |
| Stack size | 10 |
| Rocket capacity | 10 (1 stack) |
| Radar coverage distance | 2 |
| Dimensions | 4×4 |
| Drain | 50 kW ( electric ) |
| Robot recharge rate | 4×500 kW 4×650 kW 4×800 kW 4×950 kW 4×1.25 MW ( electric ) |  |  | 4×500 kW |  | 4×650 kW |  | 4×800 kW |  | 4×950 kW |  | 4×1.25 MW |
|  |  | 4×500 kW |
|  | 4×650 kW |  | 4×800 kW |
|  | 4×950 kW |  | 4×1.25 MW |
| Internal buffer recharge rate | 2.1 MW 2.7 MW 3.3 MW 3.9 MW 5.1 MW ( electric ) |  |  | 2.1 MW |  | 2.7 MW |  | 3.3 MW |  | 3.9 MW |  | 5.1 MW |
|  |  | 2.1 MW |
|  | 2.7 MW |  | 3.3 MW |
|  | 3.9 MW |  | 5.1 MW |
| Mining time | 0.1 |
| Supply area | 50×50 tiles |
| Construction area | 110×110 tiles |
| Prototype type | roboport |
| Internal name | roboport |
| Required technologies |
|  |
| Produced by |
|  |

The roboport is the resting place for all construction robots and logistic robots . It emits an area of 50×50 tiles, in which logistic robots can interact with logistic network entities, such as storage chests , or requester chests . Additionally, a 110×110 tile area is created for construction robots to repair, construct or remove structures. These areas can be seen by hovering the mouse on a roboport, or logistics chest which is inside the logistic zone.

- The smaller orange square represents the reach of the logistics network where both logistics and construction robots can move.
- The larger green square represents the extent of the construction network where only construction robots can move.

Robots placed into the air from the player's inventory inside of a roboport's coverage will seek out the nearest roboport to charge and rest.

Two or more roboports can connect to form a logistic network , if the borders of the orange logistic areas touch. This is shown by a dotted line running between the two ports. An example of this can be seen on the bottom-right. Non-connected roboports will not share robots.

Similar to the stationary radar 's nearby scanning, a roboport constantly reveals an area of 5×5 chunks, centered on the chunk the roboport occupies.

Quality does not affect the size of the roboport's construction or logistics areas.

## Contents

- 1 Storage
- 2 Power usage
- 3 Interaction with personal roboports
- 4 History
- 5 See also

## Storage

A roboport contains 7 slots , each reserved for 50 robots of the same type, and another 7 for repair packs . Robots and repair packs can be inserted into the roboport with an inserter . Furthermore, robots (but not repair packs) can be removed from the roboport with an inserter. Repair packs inside a roboport are available for all robots and requester chests inside the logistic zone of that roboport. Construction bots, when provided with repair packs, will automatically repair all damaged structures inside of a roboport's coverage area.

If a roboport is full of robots, robots attempting to rest will find a different roboport, if one is available.

It's possible to request idle robots from other roboports by configuring corresponding requests in the roboport GUI. This way it's possible to request one type or quality of robot, then remove them from the roboport with a filtered inserter, to gradually clean a logistics network from this type of robot. Unlike logistic requests , these requests can only set a minimum number of robots to have in the roboport. They cannot set a limit to the number of robots desired.

Like logistics groups , roboport requests can be named. Request groups that use the same name will request the same number of robots, and changes to the named group will be propagated to other roboports. However, request groups and logistics groups do not share the same space of names. A request group with the same name as a logistics group does not refer to the same set of requests.

## Power usage

Roboports have 4 chargers, which are used to recharge the flying bots. More roboports in a small area will allow for greater charging throughput, if a lot of robots need charging. Robots waiting to be charged will float in place near the roboport and wait their turn.

Robots will not enter a roboport to rest unless they have full charge. Robots with low/no charge can still fly, but will move extremely slowly.

## Interaction with personal roboports

An entity with an equipment grid (usually a character wearing armor that grants one, but also a tank or spidertron ) equipped with a personal roboport or personal roboport MK2 can act as a mobile roboport. This mobile roboport uses the associated entity's own inventory rather than the local logistic network for robot, item and repair pack storage. The network it creates is separate from the static network; it doesn't share robots or items with other networks.

Since it only has one inventory, a personal robot network has no use for logistic robots. It has no associated logistic network ; the entity's logistic requests and trash slots instead form part of whatever logistic network the entity is standing in, and are serviced by that network's robots. However, its construction robots will cooperate with other networks in getting construction tasks achieved as quickly as possible.

## History

- 2.0.7 : Roboports have built-in radar coverage of 2 chunks. Roboports can be configured to attempt to keep a certain amount of construction/logistics bots in reserve. Robot recharge rate reduced from 1 MW to 500 kW. Reduced max energy consumption from 5 MW to 2.1 MW.

- 0.16.17 : Increased the stack size of roboport from 5 to 10.

- 0.16.0 : Roboports now provide the repair packs they have for other robots to use.

- 0.15.6 : Increased roboport construction range to 55 (110×110 area) to make roboports able to build each other without interconnecting their logistic areas, and not break when there are obstacles like trees or rocks.

- 0.15.0 : Roboport construction area changed from 50 to 51 to allow roboports build/deconstruct each other even when there is a 1 tile gap between their logistic areas.

- 0.13.0 : Roboport is connectible to the circuit network, it sends the logistic network contents or the robot statistics of the network. Roboports have decreased transmission power consumption (200 kW to 50 kW) while the robots and their recharging have increased power consumption (200 kW per recharge slot to 1MW per slot) Reduced number of drawn connections between roboports again. Optimized roboport radius rendering.

- 0.12.5 : Robots can charge from a closer roboport on their way to a more distant one.

- 0.12.0 : Reduced number of rendered roboport connections. Inserters can now extract from roboports. Optimized adding and removing roboports, robots keep their tasks if possible.

- 0.10.7 : Roboport gui labels updated to state "Roboport" Roboport is no longer categorized as a military structure.

- 0.10.0 : Backer names are used to name roboports.

- 0.9.0 : Roboports have a separate logistic radius (now 25) and construction radius (now 50) Area visualizations for roboports are displayed under their entities.

- 0.8.5 : Only repair packs may be placed into the roboport slots.

- 0.8.2 : Roboport supply area increased from 40×40 to 50×50.

- 0.8.1 : Lowered transmission energy consumption of roboport from 200 W to 100 W.

- 0.8.0 : Introduced

## See also

- Logistic network
- Repair pack
- Robots

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
