---
title: Requester chest - Factorio Wiki
source: https://wiki.factorio.com/Requester_chest
scraped_at: 2025-10-21 14:30:56
tags: [web, documentation]
---

# Requester chest - Factorio Wiki

**Source:** [https://wiki.factorio.com/Requester_chest](https://wiki.factorio.com/Requester_chest)


|  | Requester chest | Edit |

| Recipe |
| 0.5 + 1 + 3 + 1 → 1 |
| Total raw |
| 14.25 + 9.5 + 5 + 2 + 8 |
| Map color |  |
| Storage size | 48 62 76 91 120 |  |  | 48 |  | 62 |  | 76 |  | 91 |  | 120 |
|  |  | 48 |
|  | 62 |  | 76 |
|  | 91 |  | 120 |
| Health | 350 455 560 665 875 |  |  | 350 |  | 455 |  | 560 |  | 665 |  | 875 |
|  |  | 350 |
|  | 455 |  | 560 |
|  | 665 |  | 875 |
| Resistances | Fire: 0/90% Impact: 0/60% |
| Stack size | 50 |
| Rocket capacity | 50 (1 stack) |
| Dimensions | 1×1 |
| Mining time | 0.1 |
| Prototype type | logistic-container |
| Internal name | requester-chest |
| Required technologies |
|  |
| Produced by |
|  |

The requester chest is a large advanced storage item that is part of the logistic network . Requester chests can be configured to request of a specified number of up to 1000 types of items from the network. Logistic robots will then bring the specified items from provider chests , storage chests , and buffer chests , if the "Request from buffer chests" checkbox is checked, until the request is met.

When fulfilling requests from requester chests, logistic robots will first attempt to pick up the specified items from active provider chests , then from buffer chests if the "Request from buffer chests" checkbox is checked , then from storage chests, and lastly from passive provider chests .

By using SHIFT + Right mouse button and SHIFT + Left mouse button to copy-paste a recipe from an assembling machine to a requester chest, the requester chest is automatically configured to request enough ingredients for 30 seconds of continuous crafting.

Requester chests can be disabled via a condition on the circuit network . A disabled chest will not request items even if active requests are set on it.

Requester chests can be configured to take their requests from the circuit network in addition to requests set on them directly. They may also use logistic groups in the logistic network to share sets of requests with other requesters.

## Contents

- 1 Achievements
- 2 Gallery
- 3 History
- 4 See also

## Achievements

|  | Logistic network embargo Finish research with space science pack for the base game or any planetary science pack for Space Age without building any active provider , buffer , or requester chests . |

## Gallery

## History

- 2.0.7 : Requester chests now use logistics groups. New option to trash unrequested items. Requester chests can be enabled or disabled via the circuit network .

- 0.18.27 : Increased logistic request count from 12 to 30.

- 0.17.0 : New animated graphics.

- 0.16.21 : Requesters requesting from buffer chests (which includes players) have higher priority than other requesters.

- 0.16.8 : Requester chests can now request stuff from buffer chests as was originally intended. Requester chests have a checkbox that specifies whether it should or shouldn't request things from buffer chests. It is off by default.

- 0.16.0 : Copy Paste from assembler to requester chest now scales with assembler speed and recipe crafting time.

- 0.15.28 : Warning icon for logistic chests that are not in a reach of roboport.

- 0.13.0 : Requester chest's requested items can be set automatically from the circuit network. All types of chests can be connected to the circuit network.

- 0.12.0 : Copy entity settings mechanism now allows copy from assembling machines and paste to requester chests.

- 0.10.3 : For requester chests, robots take always as much as they can carry and leave it in the chest, so it can get a bit more than requested.

- 0.8.1 : Keep the inventory limit of chests when fast rebuilding.

- 0.8.0 : Chests inventory size can be limited.

- 0.7.3 : Logistic robots delivery is evenly distributed between provider/requester chests.

- 0.2.0 : Introduced.

## See also

- Circuit network
- Logistic network

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
