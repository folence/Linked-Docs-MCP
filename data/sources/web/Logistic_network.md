---
title: Logistic network - Factorio Wiki
source: https://wiki.factorio.com/Logistic_network
scraped_at: 2025-10-21 14:29:38
tags: [web, documentation]
---

# Logistic network - Factorio Wiki

**Source:** [https://wiki.factorio.com/Logistic_network](https://wiki.factorio.com/Logistic_network)

A logistic network is a series of different logistics chests and logistic robots all covered by one or more connected roboports .

Depending on the type and configuration of the chests and area of the logistic network the robots will transport items between these chests as a power-hungry alternative to moving items manually, or by belts or railway . However, robots offer much higher mobility, since they can fly over obstacles in a beeline.

The player character can also act as requester chest in the logistic network, allowing them to 'request' various items be kept at a set limit within their personal inventory. After researching logistic robotics , they can configure an amount of items; and logistic robots will start to move the specified items from the network to the character's inventory.

## Contents

- 1 Items
- 2 Usage 2.1 Expanding the logistic network
- 3 Electricity management 3.1 Roboports 3.2 Construction and logistic bots
- 4 Setting logistic requests
- 5 Logistics groups 5.1 Blueprints 5.2 Constant combinators
- 6 Mechanics 6.1 Negative numbers 6.2 Receiving more items than requested 6.3 Space requests 6.3.1 Space platforms 6.3.2 Cargo landing pad
- 7 Priorities of robots 7.1 Construction 7.2 Distance
- 8 Achievements

## Items

| Entity | Description |
| Roboport | Central component of the logistic network in which the robots operate. Roboport coverage defines the area of the logistic network. Robots need to periodically return here to recharge. |
| Logistic robot | Moves items between logistic chests. 1 |
| Construction robot | Repairs broken or replaces destroyed entities. Builds , deconstructs and upgrades entities on command. Deliver item requests and execute item removal requests created in remote view . |
| Active provider chest | Logistic chest: Pushes stored items into the logistic network. 2 |
| Passive provider chest | Logistic chest: Places stored items at the logistic network's disposal. 2 |
| Storage chest | Logistic chest: Stores items currently not requested. Can be filtered to only store one type of item. Supplies stored items to the logistic network. 2 |
| Requester chest | Logistic chest: Will be filled by logistic robots until the configured amount is reached, or the chest becomes full. Can request multiple different types of items. Can be configured to put excess or unwanted items into trash slots, pushing them into the logistic network. 2 |
| Buffer chest | Logistic chest: Functions as both a requester chest and passive provider chest . 2 |
| Cargo landing pad | Places stored items at the logistic network's disposal. 2 Requests items from space platforms . |
| Rocket silo | If "Automatic requests from space platforms" is set, requests items from the logistic network based on requests from space platforms. |
| Player | Can set logistic requests to function as a requester chest. |
| Tank |
| Spidertron |

(1) Default capacity is 1 item per robot. This can be increased by researching Worker robot cargo size (research) .

(2) Logistic chests can also be connected to the circuit network with red wire or green wire .

## Usage

To start with, just use passive provider- and requester chests. Place the passive provider chests at the output inserters of assembling machines and requester chests at the input (let them request the needed items). Place a roboport , which covers these chests with the inner orange area. Place some logistic bots in the roboport. The robots will fly out of the top hatch and will begin to work. You can now limit the number of produced item with the stack limitation -feature.

The logistic network makes it possible to create complex items in a relatively small factory area, but its throughput is limited by how many robot charge points (roboports) exist in the network.

The basic thing needed for item transportation is roboports . The roboport shows the orange logistic coverage and the green construction coverage when held in the cursor or hovered after placing.

- The orange zone is the logistic network coverage. This is also the maximum distance for connecting two roboports.
- The green zone is the construction area.

### Expanding the logistic network

There can be many separate logistic networks. Two roboports are in the same network only if they are connected, so if their logistic areas are touching. Visually this is represented by a dashed yellow line connecting them.
To prevent roboports from linking, the player needs to build them far enough away from each other so that the orange zones don't touch.

Bots do not fly/migrate from one network to another, unless their home network is destroyed in some way, for example when all roboports are removed or out of power.

## Electricity management

Unit reminder: 1 Watt = 1 Joule/Second

### Roboports

Robots may run out of charge on longer journeys which will reduce their flying speed to 20% of their normal speed. Robots that run out of charge will fly to the closest recharge point that is closer to their final destination than its current position if possible.
This means that they may depart from the original route, depending on where the chosen charging point is, but they should always make progress, rather than endlessly backtrack to their origin.

Roboports have 4 charging slots each, which charge each bot at 1MW, taking 1.5 seconds to charge 1 robot. Furthermore, a roboport also has a 100MJ internal battery allowing bots to keep working for a limited amount of time under low power. Generally, a roboport can charge between 50 and 70 bots per min, 4 at a time, but are not very efficient at charging large queues of bots and can quickly become overworked. Higher quality roboports charge robots more quickly.

When the charging-queue for the bots gets too long, the bots (and their loads) will slow down. Normally a robot flies to the nearest roboport to recharge. If the queue on that roboport (including other robots en route to charge there) is too long, they eventually choose another port.
This is specified by the ratio of <distance to different roboport in tiles> / <queue size of robots waiting>.

Currently, to choose the more distant roboport, the distance must be at most <Number of robots in the queue and on the way> / 2. So, to choose a roboport that is 10 tiles more distant, it has to have 20 less robots waiting in the queue.

### Construction and logistic bots

Bots store 1.5MJ of energy each. They use 3kW at all times while flying and use an additional 5kJ for every tile travelled. It must be noted that increasing robot speed does not increase range significantly, see worker robot speed (research) . With no research upgrades, the speed of logistic robots is 3 tiles/s and for construction robots 3.6 tiles/s. Higher quality robots store more energy and thus have longer range and waste less time charging, but take correspondingly longer to charge.

The robots go to recharge when they hit 20% of their energy capacity. That means for 80% of their maximum distance they go straight towards the target, and the other 20% towards a roboport to charge.

The maximum travel distance can be calculated using the following formula: 1500 ÷ (3 ÷ speed + 5) , speed in tiles/s. This results in a maximum distance of 250 tiles for logistics robots and 257 tiles for construction robots without speed upgrades.

For infinite research levels, the bot speed can be calculated with these formulas:

Construction: speed = 3.6 × (3.4 + 0.65 × (Level-5))

Logistic: speed = 3.0 × (3.4 + 0.65 × (Level-5))

## Setting logistic requests

Certain entities can make logistic requests. These are requests to an external system (usually logistic robots taking from the current logistic network) to ensure that the entity has at least a given minimum amount of specific items. For requests to a logistic network, the entity must be within the logistic network for the request to be satisfied. If the entity moves out of that range, robots currently carrying cargo bound for that entity will place it back into that network.

The following entities can make logistic requests.

- The player , once logistic robotics has been researched
- Tank , once logistic system has been researched
- Spidertron
- Buffer chest
- Requester chest
- Space platform (requests go to rocket silos on the planet being orbited)
- Cargo landing pad (requests go to space platforms in orbit around the planet)

Each logistic request contains two pieces of information: the minimum amount desired in the entity, and the maximum amount allowed to be stored in that entity. The maximum number may be infinity. Logistic robots will deliver more items to the entity if the number of items in the entity's inventory is less than the minimum number.

Any entity which can use logistic requests has a number of trash slots for items which the logistic requests on that entity say are to be removed. Items beyond the maximum amount for that request will be trashed. Logistic robots will remove such items and take them to other chests in the network.

Items which are not named in any logistic request are permitted to be in the entity's inventory. However, most such entities have a checkbox in their logistic request UI to trash any item in its inventory for which no logistic request is made. To force the trashing of certain specific items, a request with a maximum value of 0 may be made.

## Logistics groups

A set of logistic requests can be grouped together. Groups with no name are denoted by the name "[No group assigned]". A name can be assigned to a group by pressing the edit button and typing a new name. This will create a new group if no group with that name already exists. To pick an existing group by name, press the edit button and select the desired name from the drop-down list.

Logistics groups, named or unnamed, can be enabled separately from one another, and each entity can have multiple groups assigned to it at once.

Logistics group names are global. This means that if you use the same name for two groups in two different entities, no matter where they are, they are using the same logistic requests. Updates to requests from one entity will be shared among all entities using that named group.

### Blueprints

If an entity which uses a logistics group is captured in a blueprint , all of the requests in that group will be stored in the blueprint. Pasting the blueprint will put all of those values into the pasted entity.

The above includes named logistics group. However, named groups are global. As such, if a group with that name already exists when you paste the blueprint, the contents of that group will not be changed to match what they were when the blueprint was captured. The entity will simply use the existing named group. This means that, if you have changed a logistics group's contents in the world, pasting a new blueprint which uses that group will not undo your changes to that group. The new entity will see the updated group.

### Constant combinators

Constant combinators can also use named logistics groups, allowing signals to be sent to a circuit network that match the request values in a logistics group. However, logistics requests for a particular item have 2 numbers attached to them: the minimum amount to request desired and the maximum amount to retain before trashing the rest. Circuit networks can only assign a single value to a signal. When a constant combinator uses a logistics group, the value it sends is the minimum requested amount, not the amount to retain.

Note also that the UI for setting a constant in a combinator does not provide a way to specify the maximum retention amount. So if you set a new signal into a named logistics group through a constant combinator, the maximum value will default to infinity. If you modify the signal value of an existing signal which has a maximum request value, the maximum value will be unaltered.

## Mechanics

### Negative numbers

It is possible to notice negative numbers on the 'Logistic Network'-Screen when looking at network storage or opening the logistic networks GUI the with L .

The logistic network reports the total number of items in provider, buffer and storage chests, minus the amount of items scheduled to be picked up by robots. When a bot starts its journey to pick up items from a chest, it reserves the items in advance by subtracting the items it wants from the total logistics storage. A bot will always reserve the maximum amount that it can carry, even when the box does not currently have that amount. This means that the number can go negative when a bot embarks on a pickup while the box is almost empty.
Negative numbers in the logistic network are not the deficit of the total number of requested items. If there are no bots picking up any items, there are no negative numbers in the network, regardless of requests in requester chests.

For example, with a full worker robot cargo size bonus, a bot can carry 4 items. If there is only 1 iron plate in the logistic network, and a robot comes to pick it up, it will reserve the full 4 it can carry and the amount in the network will be displayed as follows:

After the robot has picked up the item, the reservation is removed and the number goes back to 0.

The reason this happens is that a bot can be dispatched to pick up an item when there is only 1 item available. While it is travelling to pick up that item, additional items can be put into the chest, and once the bot gets to the chest, it has already reserved those items in advance and can pick them up immediately.

### Receiving more items than requested

The delivered number of items in the requester chest can be higher than requested. This depends on the researched Worker robot cargo size -bonus, since bots will always take as much as they can carry if an unlimited amount is available.

### Space requests

In the Space Age expansion, cargo landing pads gain the ability to make logistics requests. Space platforms also have the ability to make logistics requests. In both cases, these requests are not (directly) made to a logistic network; they are instead made to specific entities on other surfaces. Though they do not request from a logistic network, the user-interface for setting these requests is (almost) identical to any other logistics requesting entity.

#### Space platforms

When a space platform is in orbit around a planet, it can send logistic requests to the planet below. These requests are not directly handled by any particular logistic network. They are instead handled by rocket silos .

Every rocket silo on the planet will receive all requests from space platforms. Rocket silos can be set to automatically forward any platform requests to the local logistic network that the silo resides in. If a platform requests a rocket load of assemblers, and a rocket silo (with at least one rocket at the ready) using this setting is in a logistic network that contains at least the requested amount of assemblers, the rocket silo will act as a requester chest and request those assemblers. Once logistics robots load the silo, the rocket will launch.

Rocket silos can also be loaded via non-logistic network means. Rocket silos can store cargo loaded via inserters. If the silo has a rocket prepared and has a rocket load of a single kind of item is in its cargo, and a space platform requests a rocket load of that item, the silo will automatically launch to that platform. Alternatively, the circuit network can be used to read requests from platforms through the rocket silo. Circuit network conditions and combinators can be used to allow inserters to load the silo with requested materials.

Note that you cannot load processing units , low density structures , or rocket fuel in this way, as the silo assumes those are meant to make rocket parts .

Individual logistic requests on a space platform have two pieces of extra information associated with them. This extra information can only be specified when accessing the request from a space platform. So if a named logistics group is shared between a platform and some other kind of entity, if you want to change these settings, you must do so through the platform itself. This information is stored in named logistics groups and blueprints.

The first platform-specific information is the target planet. Each individual item requested by space platforms targets a specific planet. This means that requests for an item are only sent to a specific planet. The UI to specify which planet to request from can only be access from a space platform. If you create a new request in a named logistics group that is shared with a platform from outside of the space platform's UI, it will use the default planet for that item. The default planet is usually Nauvis unless the main recipe for that item is restricted to a specific planet, in which case it defaults to that planet.

So if you share a logistics group between a platform and the destination planet, you will need to set any new requests in the space platform's version of the logistics group.

The other platform-specific information is the "Custom minimum payload". When this is checked, the player can specify that the space platform can receive less than the full rocket capacity of the requested item. By default, rockets will only automatically launch when full; this setting is a per-item override to this, allowing rockets to launch with a minimum of the specified amount. By default, this setting is unchecked.

Trashing items via requests works like any other entity. Instead of having logistics robots remove trash, they are dropped to a planet whenever the platform is in orbit (and has "unload" checked). Note that this can fill cargo landing pads with unwanted items, possibly filling them up completely.

#### Cargo landing pad

The cargo landing pad on a planet can request items from the space platform hub of any space platform currently in orbit around that planet which is set to unload items to that planet. Such requests can be set by the circuit network as well.

Cargo landing pad requests can include trashing items beyond the maximum amount in the request. Trashed items are exported to the logistic network the landing pad appears within.

## Priorities of robots

This overview reflects the priorities in which order the chests are filled/emptied.

Logistic robots on the logistic network look for orders by the chests in this order:

- A requested item is first looked up in active provider chests and in the player's trash slots, then in the storage chests and buffer chests, then the passive provider chests. So, the active provider chests are emptied first, then the storage chests and buffer chests, then the passive provider chests.

- Requests are assigned first for player logistics, then for requester chests, then for buffer chests.

| Source Priority | > > | Target Priority | 1 > > 2 > 3 |

(1) Requesters with "request from buffer chests" have higher priority than others, the same as a player.

(2) Buffer chests will only ever be a target when having requests specified.

(3) Storage does not "request" items on its own. It receives actively discarded items from a) active providers, b) player trash slots, c) deconstruction, and d) robots that have their orders cancelled while carrying items. Storage is the last priority, and receives only items that have nowhere else to go.

- To place items into storage chests, the bots search for one which has its filter set to the item type, then for a storage chest that already stores items of the same type. If that can't be found, they choose the first (unfiltered) storage chest with a free slot from the list, which is sorted by the order they were built in. [1] This is to avoid having storage chests with different items inside, allowing greater organisation.

### Construction

When construction robots want to build a ghost, they look for the chests that is closest to the ghost they want to build. The type of chest does not matter. [2]

### Distance

When looking to pick up requested items from multiple chests of equal priority, bots will always choose the closest one. [3]

This is however only true when an item is being requested, not when an item is sent away via player trash slots or active provider chests. In the case of items being sent into the logistics network, distance does not matter, instead when chests have the same priority, for example two active provider chests, the bots will alternate between the chests in a round-robin fashion.

## Achievements

|  | You've got a package Supply the character by logistic robot . |

|  | Delivery service Supply the character with 10k items delivered by logistic robots . |

|  | Logistic network embargo Finish research with space science pack for the base game or any planetary science pack for Space Age without building any active provider , buffer , or requester chests . |

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
