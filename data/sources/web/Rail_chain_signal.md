---
title: Rail chain signal - Factorio Wiki
source: https://wiki.factorio.com/Rail_chain_signal
scraped_at: 2025-10-21 14:30:39
tags: [web, documentation]
---

# Rail chain signal - Factorio Wiki

**Source:** [https://wiki.factorio.com/Rail_chain_signal](https://wiki.factorio.com/Rail_chain_signal)


|  | Rail chain signal | Edit |

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
| Prototype type | rail-chain-signal |
| Internal name | rail-chain-signal |
| Required technologies |
|  |
| Produced by |
|  |

Rail chain signals are used for automated transportation on a railway network . With rail chain signals, it is possible to use multiple trains on a single track, or multiple rails that intertwine. Rail chain signals can be used to ensure that trains only enter a crossing if they can also leave it, which ensures that they do not block other traffic by waiting on the crossing. In addition to the explanation on this page, there is also the rail signal tutorial .

## Contents

- 1 Basic
- 2 Definition
- 3 Advanced
- 4 Usage examples
- 5 History
- 6 See also

## Basic

- The best prerequisite to understand chain signals is to understand signal blocks .
- Rail chain signals are placed like regular signals at the right side of the railway track. If automated trains are required to drive in both directions on the same track segment, signals need to be added on both sides of the track, opposite each other.

## Definition

Both normal signals and chain signals prevent a train from entering the next block if it is obstructed.  However, a chain signal also looks ahead to the next signal, and turns red if the next signal is red.  In effect, this prevents a train from entering a block if it won't be able to leave. When more than one exits exist, the one where the train is pathing to is considered.

## Advanced

- If the chain signal has only one exit, it doesn't allow the train to enter its block, if the train would have to stop in said block.
- Since trains react to chain signals based on their own path, chain signals before a crossing will not stop trains if the other track's exit is blocked.
- If there are several chain signals before a regular one, a train waits before the first chain signal if the block after the regular signal is occupied.

- If a chain signal switches to green , all exits are free.
- If it switches to yellow , the block is reserved for a train and all other entrance signals of that block turn red .
- If it switches to red , all exits are occupied.
- If it switches to blue , some but not all exits are free. In this case trains may or may not stop, depending on their path.
- If it is blinking , it is not on a rail, or unable to divide it into separate blocks.

## Usage examples

Regular signal compared to a chain signal

With a regular signal, the block after it is empty, so the train can go there.

Chain signal with one exit doesn't allow the train to enter the block, since it can't leave immediately.

Simple example with practical usage

The chain signal prevents the train from blocking the crossing route while waiting.

Double crossing

Double crossings are a common cause of train jams, as trains can stop in the middle of the crossing and block everything. It can even cause total deadlock, which require manual intervention to fix the problem. With chain signals, the rails that don't cross are still separated, but trains won't stop in the middle of the crossing.

Deadlock prevention

Another common cause of blockages are bidirectional single track lines with occasional bypasses. Here a train can't enter the line because another train is in it, but that train in turn can't leave the line.

With chain signals, this problem can be totally avoided by preventing the train from going to the shared section unless it can exit it.

## History

- 0.16.0 : Rail chain signals can be read by the circuit network .

- 0.12.0 : Introduced

## See also

- Rail signal
- Railway
- Tutorial: Train signals

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
