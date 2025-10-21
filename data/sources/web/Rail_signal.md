---
title: Rail signal - Factorio Wiki
source: https://wiki.factorio.com/Rail_signal
scraped_at: 2025-10-21 14:30:38
tags: [web, documentation]
---

# Rail signal - Factorio Wiki

**Source:** [https://wiki.factorio.com/Rail_signal](https://wiki.factorio.com/Rail_signal)


|  | Rail signal | Edit |

| Recipe |
| 0.5 + 1 + 5 → 1 |
| Total raw |
| 1.75 + 1.5 + 6 |
| Map color |  |
| Health | 100 130 160 190 250 |  |  | 100 |  | 130 |  | 160 |  | 190 |  | 250 |
|  |  | 100 |
|  | 130 |  | 160 |
|  | 190 |  | 250 |
| Stack size | 50 |
| Rocket capacity | 50 (1 stack) |
| Mining time | 0.1 |
| Prototype type | rail-signal |
| Internal name | rail-signal |
| Required technologies |
|  |
| Produced by |
|  |

The rail signal divides rails into blocks and allows locomotives to react to other locomotives allowing multiple trains use the same rails without colliding. Blocks span all connected rails regardless if a train can actually travel between them. Rail signals can also be used in with conjunction rail chain signals , which also separate rails into blocks. In addition to the explanation on this page, there is also the rail signal tutorial .

## Contents

- 1 Direction
- 2 States
- 3 Circuit network
- 4 History
- 5 See also

## Direction

Which block a signal monitors depends on which side of a rail it is placed. When a signal is on the right-hand side of the track, it monitors and protects the rail block behind it, up to the next signal or the end of the track. When placing rail signals, the rail signal blocks will be visible, and the opposite signal position will be highlighted in white. A train in automatic mode will not drive on a track if it would pass a signal on the left side unless there is also a signal on the right side at that signal.

## States

Rail signals have four states:

- Green - The monitored block is empty.
- Yellow - A train is not able to stop before the monitored block and will pass the signal. The debug option show-train-braking-distance can be used to see the distance locomotives need to stop. A yellow signal means that a train is approaching and already has the approval to enter the following block. The block is reserved for a train and all other entrance signals of that block turn red.
- Red - The monitored block is not empty or another signal monitoring it is yellow.
- Blinking - The signal is not on a rail, or the monitored block is also the block before the signal.

When a signal is red, locomotives will stop before it. A rail chain signal can be used to make locomotives stop earlier, as they will always mimic the signal of what is in front of them.

## Circuit network

A circuit network condition can be configured that when true will make the rail signal red.

A rail signal can also output three different signals depending on if it is in its green, yellow or red state. If a rail signal is red because of a circuit network condition the rail signal won't output a circuit network signal.

## History

- 0.13.0 : The rail signal is now connectable to the circuit network. Halved the mining time of the rail signal. Rail signal stop placement indicator added.

- 0.11.4 : Rail signal that fails to divide two sections of rail will blink multiple colors.

- 0.9.0 : Players no longer collide with the rail signal.

- 0.5.0 : Players can now see a visualization of the protected rail area when building/selecting the signal.

- 0.4.1 : Rail signals connect to more than one rail when connected to a junction.

- 0.4.0 : Introduced

## See also

- Rail chain signal
- Railway
- Tutorial:Train signals

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
