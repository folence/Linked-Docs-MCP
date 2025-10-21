---
title: Train stop - Factorio Wiki
source: https://wiki.factorio.com/Train_stop
scraped_at: 2025-10-21 14:30:37
tags: [web, documentation]
---

# Train stop - Factorio Wiki

**Source:** [https://wiki.factorio.com/Train_stop](https://wiki.factorio.com/Train_stop)


|  | Train stop | Edit |

| Recipe |
| 0.5 + 5 + 6 + 6 + 3 → 1 |
| Total raw |
| 8.25 + 7.5 + 14 + 3 |
| Map icon |  |
| Health | 250 325 400 475 625 |  |  | 250 |  | 325 |  | 400 |  | 475 |  | 625 |
|  |  | 250 |
|  | 325 |  | 400 |
|  | 475 |  | 625 |
| Stack size | 10 |
| Rocket capacity | 10 (1 stack) |
| Dimensions | 2×2 |
| Mining time | 0.2 |
| Prototype type | train-stop |
| Internal name | train-stop |
| Required technologies |
|  |
| Produced by |
|  |

Train stops are used to automate item transportation by trains by providing nameable locations for trains to travel to. Like locomotives , the color of the stops can be customized. Furthermore, the stop can be named, with rich text making it possible to further customize the name, such as by adding item icons.

## Contents

- 1 Mechanics
- 2 Circuit Network
- 3 Indicators
- 4 Gallery
- 5 History
- 6 See also

## Mechanics

Train stops are used to denote a place for a train to stop. Every placed train stop will appear as a possible stop in the scheduling area of a train 's GUI. This can be used to create loading and unloading stations for trains.

When there are multiple train stops with the same name, trains will always travel to the closest stop. "Closest" in this case does not mean rail distance, instead the pathfinding distance is used. This distance is influenced by trains on the track, in addition to rail distance, so empty train stops are preferred over occupied ones if the empty stop is not too far away.

Opening the GUI of a stop will show the information of every train connected to that stop, including its name, current activity and location on the map. Additionally, it is possible to set a train limit for train stops via their GUI or with the circuit network. Only the set amount of trains may reserve the train stop as their destination when trying to path to it. If the train limit is lowered below the amount of trains that currently have the stop reserved as their destination, those trains will continue to go to the stop. [1]

Trains will attempt to avoid routes that pass through stops that are not designated as the next destination. This is represented by a penalty to the pathfinding distance, which usually forces a train to pick a "shorter" path.

## Circuit Network

Train stops can be enabled or disabled using the circuit network . When a train stop is disabled, trains will not go to that station. If a train is scheduled to go to a stop that is disabled, it will select a stop with the same name which is enabled. If no such stops exist, the train will enter the "destination full" state and wait until a stop becomes enabled again. If a train is en-route or already parked at a stop when it becomes disabled, the train will continue to the stop and complete its wait conditions.

When a train attempts to go to an enabled stop, it first checks to see if the stop has a "train limit" set. This limit specifies the maximum number of trains allowed to go to this station. If the number of trains headed to that stop (including one sitting at the stop) is greater than or equal to the stop's current train limit, then the train will not go to that stop. It will check other enabled stops with that name. If all stops with that name are full, the train will enter the "destination full" state. Once a stop with that name opens up to allow more trains, the train will proceed. Like disabling, if a train limit changes while a train is en-route to a stop, the train will continue to the stop and complete its wait conditions. A stop with a train limit of 0 behaves identically to a stop which has been disabled.

When there are multiple valid stops with the same name, the train will next check each stop's "priority". Stop priority can be set manually or with the circuit network, and can be set between 0 and 255, defaulting to 50. The lowest priority is 0, and the highest priority is 255. Trains will prefer stops with a higher priority. If all valid stops have the same priority value, the train will select the closest stop. Priority values are only considered when a train is dispatched; if a train is en-route and priority values of its stop change so that it is no longer going to the highest priority stop, the train will not re-path to the new highest priority stop and will continue on its original schedule.

While a train is en-route, it may repath to a different train stop of the same name, provided the new train stop has not reached its capacity. When this happens, the train ceases to count toward the train limit of the original stop.

Train stops can be used to pass circuit signals to trains, read train contents, uniquely identify trains with an ID number, or count the amount of trains going to the train stop.

When reading the content of a stopped train, fluid amounts are rounded down to the nearest integer, except when the fluid amount is < 1, then it is is rounded to 1.

## Indicators

There are indicator lights on the top of the train stop. These show:

Solid light – The train stop is unoccupied/available.

Alternate blinking – A train is approaching or passing the train stop.

Simultaneous blinking – A train is stopped/occupying the train stop.

No lights – The train stop is invalid.

Blinking red – The train stop is disabled via circuit network.

## Gallery

- Three railways with different color train stops.
- Four trains listed in a train stop's GUI.

## History

- 1.1.0 : Train stop allows to set limit of incoming trains. Fluids in train circuit logic treat summed < 1 fluid values as 1 instead of 0.

- 0.17.0 : Train stop recipe now uses iron sticks.

- 0.15.0 : Train station adds 2000 tiles penalty when path finding, so trains try to avoid stations not related to their path. Train Stop can output the contents of the stopped train's cargo. Train Stop can be disabled using the circuit network. When the active train stop is removed, trains will immediately leave the station if they're waiting at the station.

- 0.13.0 : New graphics Placement indicator Indicator of train position when stopped at station on hover.

- 0.10.0 : Station names can now be changed.

- 0.7.0 : Show the direction of incoming trains when being built. Multiple train stops for each train station.

- 0.4.1 : Cannot be rotated after building.

- 0.4.0 : Introduced

## See also

- Locomotive
- Railway
- Rail signal
- Rail chain signal

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
