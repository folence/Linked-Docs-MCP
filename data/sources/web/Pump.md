---
title: Pump - Factorio Wiki
source: https://wiki.factorio.com/Pump
scraped_at: 2025-10-21 14:30:32
tags: [web, documentation]
---

# Pump - Factorio Wiki

**Source:** [https://wiki.factorio.com/Pump](https://wiki.factorio.com/Pump)


|  | Pump | Edit |

| Recipe |
| 2 + 1 + 1 + 1 → 1 |
| Total raw |
| 2.5 + 1 + 1 + 1 |
| Map color |  |
| Fluid storage volume | 400 |
| Health | 180 234 288 342 450 |  |  | 180 |  | 234 |  | 288 |  | 342 |  | 450 |
|  |  | 180 |
|  | 234 |  | 288 |
|  | 342 |  | 450 |
| Resistances | Fire: 0/80% Impact: 0/30% |
| Stack size | 50 |
| Rocket capacity | 50 (1 stack) |
| Dimensions | 1×2 |
| Energy consumption | 30 kW ( electric ) |
| Pumping speed | 1200/s 1560/s 1920/s 2280/s 3000/s |  |  | 1200/s |  | 1560/s |  | 1920/s |  | 2280/s |  | 3000/s |
|  |  | 1200/s |
|  | 1560/s |  | 1920/s |
|  | 2280/s |  | 3000/s |
| Mining time | 0.2 |
| Prototype type | pump |
| Internal name | pump |
| Required technologies |
|  |
| Produced by |
|  |

This article is about the pump. For the water extraction device, see offshore pump . For the oil extraction device, see pumpjack .

## Contents

- 1 Overview
- 2 Throughput
- 3 Loading/unloading fluid wagons
- 4 Use as a valve
- 5 Moving fluids over long distances
- 6 Animations and visuals
- 7 History
- 8 See also

## Overview

A Pump is a multipurpose fluid handling device which can be used to move fluids over long distances, perform flow control, prevent back-flow and load/unload trains. The pump can be seen as the inserter for fluids.

When connected to pipes on both ends of the pump and powered, the pump will transfer fluid from the source side to the output side if it will fit. This will occur even if the input side has significantly lower fluid levels.

Furthermore, unlike normal pipes, pumps can connect to pipes only on the front and back of the pump instead of connecting to pipes from all sides. This can be useful for having tightly packed lines of pipes being parallel to each other, without the risk of fluids mixing, acting as a "diode" pipe.

## Throughput

Pumps can move up to 20 units of fluid per tick, or 1200 per second. Whether this throughput is actually achieved depends on the fluid level of the fluid segments upstream and downstream of the pump. If the level of the source segment is below 20%, 1200 units can no longer be achieved. The same applies if the level of the output segment is above 80%. Comprehensive information on the general behavior of fluids can be found on the page fluid system .

## Loading/unloading fluid wagons

Pumps can load and unload fluid wagons at train stops . When a pump is placed with one end facing a rail track and the other end connected to a pipe, it will visually change. When a fluid wagon is stopped adjacent, the pump head will connect to the top of the nearest tank and begin transferring fluids. It will not connect if a circuit condition is preventing it, or it is unpowered.

## Use as a valve

The pump works as a controllable valve:

- When powered, the pump will let fluids through, but only in its set direction.
- If unpowered, the pump doesn't let anything through.
- If the pump is powered but has a circuit condition, it will only let fluids through when the condition is met. This can be used to control some parts of a player's factory. For example, with a single wire from a lubricant tank to a pump pumping heavy oil , you can disable cracking heavy oil → light oil when lubricant is needed.

## Moving fluids over long distances

When a fluid is created, it can travel up to 320 tiles from its existing location until it needs a pump. Pumps reset this value, allowing fluids to travel for another 320 tiles until another one is needed. If a pipe has been overextended, a warning will show on the map. Multiple pump effects don't stack.

## Animations and visuals

## History

- 2.0.7 : Lowered Fluid pumping speed from 12000 to 1200. Fluid dynamics changed The pump now has an optional fluid filter (Described in FFF-405)

- 0.15.0 : Graphics changed, now has a nice animation Size changed to 2×1 tiles Recipe changed, now requires engine units rather than electric engine units . Throughput massively increased. Renamed from Small Pump to Pump

- 0.12.1 : Copy pasting settings now works for small pumps.

- 0.12.0 : Now connectible to the circuit network .

- 0.10.0 : Changed collision box logic

- 0.9.0 : Introduced

## See also

- Fluid system
- Pipe
- Fluid wagon

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
