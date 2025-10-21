---
title: Fluid system - Factorio Wiki
source: https://wiki.factorio.com/Fluid_system
scraped_at: 2025-10-21 14:29:44
tags: [web, documentation]
---

# Fluid system - Factorio Wiki

**Source:** [https://wiki.factorio.com/Fluid_system](https://wiki.factorio.com/Fluid_system)

Fluids are non-solid items, such as water and oil . They can normally only exist inside entities for fluid handling (like pipes ), and buildings that have fluids as input ingredients or products (like an oil refinery ).

## Contents

- 1 Fluids
- 2 Mechanics 2.1 Storage 2.2 Fluid mixing 2.3 Flow 2.4 Temperature
- 3 Transport 3.1 Pipelines 3.2 Barrels 3.3 Railway
- 4 See also

## Fluids

The following fluids are available in-game:

| Fluid | Resource distribution | Extractor | Alternative recipes | Producer |
| Water |  |  |  |  |
| Steam | N/A | N/A |  |  |
| Crude oil |  |  | N/A | N/A |
| Petroleum gas | N/A | N/A |  |  |
| Light oil | N/A | N/A |  |  |
| Heavy oil |  |  |  |  |
| Lubricant | N/A | N/A |  |  |
| Sulfuric acid |  |  |  |  |
| Thruster fuel | N/A | N/A |  |  |
| Thruster oxidizer | N/A | N/A |  |  |
| Lava |  |  | N/A | N/A |
| Molten iron | N/A | N/A |  |  |
| Molten copper | N/A | N/A |  |  |
| Holmium solution | N/A | N/A |  |  |
| Electrolyte | N/A | N/A |  |  |
| Ammoniacal solution |  |  | N/A | N/A |
| Ammonia | N/A | N/A |  |  |
| Lithium brine |  |  | N/A | N/A |
| Fluorine |  |  | N/A | N/A |
| Fluoroketone (hot) | N/A | N/A |  |  |
| Fluoroketone (cold) | N/A | N/A |  |  |
| Plasma | N/A | N/A |  |  |

## Mechanics

Fluids cannot be carried by the player, moved using inserters , dropped on the ground, nor stored in chests, unless the fluids are stored in barrels . They cannot be spilled or even dumped in a lake, and are counted in continuous fractions, rather than discrete integers. When the player picks up a structure that contains fluids, the contained fluid will try to flow into connected structures and any excess fluid that does not fit is destroyed.

### Storage

In the game, fluid is held in entities that behave as vessels (fluid boxes) of a defined size (volume). The vessels automatically connect to each other if their inputs/outputs are adjacent (pipes connect to all directions) and allow fluids to flow between them.

The volume of fluid contained in a fluid box is a value between 0 and the maximum volume. For instance, the pipe can hold 100 units of fluid, therefore the value in the pipe can be a number between 0 and 100. The level of fluid in a given entity is manifested by a percentage of the entity's maximum volume that is being occupied by a fluid. It can be observed in pipes and tanks; they have windows through which the fluid is seen at a certain level, or perhaps even as just a small trickle.

### Fluid mixing

The game will prevent players from accidentally mixing fluids when placing most buildings, e.g. pipes containing different fluids cannot be placed directly next to each other. However, not every possible case of fluid mixing is considered, so the player may still mix fluids accidentally or by purposely working around the building restrictions. A fluid segment can only contain a single fluid type, so trying to mix multiple fluids will result in all but one fluid being deleted.

### Flow

All connected tanks and pipes are treated as a single vessel in that the level of fluid must be equal in all parts , to even out pressure exacted by a higher fluid level on smaller ones. This is why level is also often referred to as pressure , even though pressure is actually caused by a difference in level between two entities. All flow of fluid that happens between pipes is to achieve this balance (pumps practically ignore it and buildings disrupt it; more on that further below). The flow rate between pipes is dependent on pressure (the difference in level between the adjacent entities), it becomes slower as pipes even their levels out.

Coming back to how the 'level' is defined, this also means that all connected pipes and tanks attempt to even out to the same percentage of their respective volumes. For example, if 12,550 units of fluid are left to flow into a storage tank of 25,000-unit capacity with one pipe of 100-unit capacity connected, there will be 12,500 units in the storage tank and 50 units in the pipe, both being filled to the same percentage (50%) of their capacities, even though the amounts themselves are unequal.

Machines that produce fluids put them in their output slots, which are related to a specifically labeled output pipe socket somewhere on the machine (pressing Alt reveals the labels). The slot will attempt to empty itself into the entity connected to the machine's socket, unless it is full, or contains a non-matching fluid. Machines that consume fluids also have an accordingly labeled pipe input socket. If an entity containing the correct fluid is connected to it, the machine will start behaving like a pipe that can never be filled, meaning the fluid from connected pipes and tanks drains into the machine at a fixed rate, until the machine's input slot is full. There may be machines that have pipe sockets for both input and output (like a drill placed over uranium ore ). They then drain the fluid for themselves first, and once full, behave as a regular pipe that attempts to even out its level with adjacent entitites. If there are multiple output/input sockets for one fluid on a machine, their activity is distributed to them equally unless some of them are blocked/full. Each socket is limited to 6000 fluid transfer per second. The total throughput is then 6000 times the sum of the available sockets for each fluid type. For example, while a cryogenic plant with eight tier three speed modules can produce steam via acid neutralisation at a rate of 26,000/second, it will only be able to export at a theoretical max of 18,000/second (6000 * three output sockets). This limit is multiplied with the fullness ratios of the source and sink to produce the actual flow value. In practice, this means that the practical limit will be lower.

### Temperature

Temperature is currently only relevant in heating water as a medium for power generation. Even though all fluids in the game have a temperature value, it is generally the default 15°C.

Energy, whether harnessed from fuel in boilers , or from nuclear power through heat exchangers , can be used to turn water to steam , being a liquid form of work . Steam holds energy at a ratio of 0.2 kJ per °C per unit. In other words: 0.2 kJ of work is necessary to heat a unit of steam by one °C. Since steam/water is set to have a maximum temperature of 1000°C and minimum of 15°C, the most work that can be done on one unit is 197 kJ.

In practice, this is barely utilized in a great variety: Boilers only output steam of 165°C temperature, and heat exchangers only output 500°C hot steam, never hotter, never colder; if insufficient energy is supplied, the heaters do not output steam altogether. The steam also does not grow colder over time. Using the 165°C steam in a steam engine has the same effect as using it in a steam turbine , although it is impractical, since turbines are made to consume 500°C (superheated) steam, generating proportionally more power. All of this makes for no need of exact calculations.

## Transport

Fluids can be transported through pipelines, barrels, or railway. It is generally practical to use piping for short-distance distribution to machines (or barrelling, if there is need to use belts), and railway transportation for longer distances.

### Pipelines

Pipes are the most basic way to channel fluids from A to B. They automatically connect to any adjacent pipe and can do so to all four cardinal directions simultaneously. Underground pipes only work in two opposite directions, linking to another underground pipe on one side, and to another entity on the other. If a pipe section becomes too long without using pumps (spreading outside a 320×320 tiles or 10×10 chunk area), fluid will not flow until the pipeline is broken up by a pump. Tanks behave the same as pipes, except their volume is much greater.

Pumps use electrical power to transfer fluids in one direction. They also block any back-flow, which means they can pressurize a section of piping, filling it as much as possible. They can also be disabled using the circuit network which stops fluid flow through the pump.

A continuous pipeline (meaning one that is not split by pumps) will transfer fluid instantly, with no flow restriction, irrespective of the distance, as long as the pipeline is not too long (as defined above).

### Barrels

Barrels are used by Assembling machines to effectively "bottle" fluids into an item that can be handled like any other item; carried in an inventory, placed in chests and handled by Inserters . This allows the player to transport fluids via the belt transport system and the logistic network (as well as the railway , although fluid wagons are also an option on rails). Assembling machines are also used to empty the barrels, depositing their contents to pipes and leaving an empty barrel for another use.

Barrels can't be used to transport steam or any fluids introduced in the Space Age expansion (with the exception of fluoroketone (hot) and fluoroketone (cold) ).

### Railway

Railway is another method of transporting fluids, and can be conducted in two ways: Either the fluids are directly pumped into a fluid wagon , or they are poured into barrels and loaded into cargo wagons . Both methods have their advantages:

Advantages of using fluid wagons

- Higher capacity (50k vs 20k)

Advantages of using barrels in cargo wagons

- A single cargo wagon can transport multiple types of barrelled fluid (and regular items at the same time)
- Cargo wagons, as opposed to fluid wagons , don't need to be perfectly aligned to be (un-)loaded, allowing for more flexible train station designs

## See also

- Oil processing
- Power production
