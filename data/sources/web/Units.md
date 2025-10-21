---
title: Units - Factorio Wiki
source: https://wiki.factorio.com/Units
scraped_at: 2025-10-21 14:29:57
tags: [web, documentation]
---

# Units - Factorio Wiki

**Source:** [https://wiki.factorio.com/Units](https://wiki.factorio.com/Units)

Units - by definition - are definite, representational quantities of measurement for different systems. Units can represent the  measuring of electricity, amount of items, the time taken/required to perform a task or even the amount of stacks of items with differing amounts within said stacks.

Not all in-game units are simulated with full realism.

## Contents

- 1 Numerical abbreviations
- 2 Power 2.1 Watt (W)
- 3 Work 3.1 Joule (J)
- 4 Time 4.1 Tick (1/60 s) 4.2 Second (s) 4.3 Day
- 5 Distance / Space 5.1 Tile 5.2 Chunk 5.3 Kilometers
- 6 Force 6.1 Newtons (N)
- 7 Mass / Weight 7.1 Tons (t)
- 8 Logistics 8.1 Throughput 8.1.1 Belts 8.1.2 Logistic robots 8.1.3 Trains 8.2 Capacity 8.3 Density 8.3.1 Belts 8.4 Stacks/chests

## Numerical abbreviations

Each unit in the game can be abbreviated with the following:

| Abbreviation | Value | Numeral | SI Prefix |
| k | 10^3 | thousand | kilo |
| M | 10^6 | million | Mega |
| G | 10^9 | billion | Giga |
| T | 10^12 | trillion | Tera |
| P | 10^15 | quadrillion | Peta |
| E | 10^18 | quintillion | Exa |
| Z | 10^21 | sextillion | Zetta |
| Y | 10^24 | septillion | Yotta |
| R | 10^27 | octillion | Ronna |
| Q | 10^30 | nonillion | Quetta |

For example, instead of using 1000 J is equal to 1kJ.

## Power

Power is defined as work being done per unit of time.

### Watt (W)

The basic unit of power is 1 watt (W), which is defined as 1 W = 1 J/s , ie. one Joule of work being done every second.

The game commonly deals with larger units, namely kilowatts (kW) and megawatts (MW).

Lamps use 5 kW while turned on. A Radar uses 300 kW while active - equivalent to 60 lamps. 
One Steam engine is capable of outputting 900 kW.

## Work

Work is defined as a transfer of energy, or as energy being "spent".

### Joule (J)

The basic unit of work is 1 joule (J), and is equivalent to the work done (total energy transferred) by one watt applied for one second: 1 J = 1 W s .

In-game, Fuel is really just potential energy, which, when applied, does work. For example, every piece of coal burned will produce 4 MJ. One Accumulator is capable of storing 5 MJ.

In the real world, kilowatt hours is a much more common unit for energy, but it is not an SI derived unit so it is not used by the game.

## Time

### Tick (1/60 s)

A 1/60 second in game. This is the shortest time fraction the game handles.

### Second (s)

One second in-game. This is not guaranteed to correspond to one real second. For example, slow computers may not manage to calculate an entire tick during the corresponding real time frame of 1/60th of a second.

### Day

A day is 25200 in-game ticks or 420 in-game seconds (= 7 in-game minutes) long.

## Distance / Space

### Tile

The tile is both used as a unit of distance/length and a unit of area. For example, the size of an object may be expressed as "2×2 tiles", which means the object covers an area of 4 square tiles or tiles². The unit of square tiles is often simplified into tiles. It can be assumed, that a tile has the length of 1 meter.

### Chunk

A chunk is a quadratic area where one side is 32 tiles long. (1024 square tiles). A grid of tiles and chunks in can be viewed in the debug mode by pressing F5 .

### Kilometers

A kilometer is 1000 meters, it is used to measure distance traveled in a space platform .

## Force

### Newtons (N)

Newtons measure the amount of forceful thrust of a space platform being moved by thrusters . This can be increased by adding more thrusters. More force can add damage to asteroids colliding with a platform, but the asteroids will, in turn, damage the platform as well.

## Mass / Weight

### Tons (t)

A single ton is 1000 kilograms. The only time mass is measured in Factorio is calculating the sum of all parts that make up a space platform. The more components added and the bigger the platform's size, the more mass it will accumulate. The larger the mass of a platform, the harder it is for thrusters to move it to its destination.

## Logistics

### Throughput

Items per time, or fluid-units per time. A unit measurement is

```
items / game-minute
```

#### Belts

Throughput = speed × density

For comparison: A transport belt transports normally about 900 items per in-game minute. A fast transport belt up to 1800 items/min and express transport belt nearly 2700 items / min.
See physics of transport belts for more information.

#### Logistic robots

Throughput depends on the distance, the number of robots and their item-stacksize. Let's assume a robot can travel 1 tile per second and can transport only one item at once. It needs also to return. Then this robot can transport ½ item per second. If you use 2 you can transport 1 item per second. If you double the distance, we are again at ½ item per second.

#### Trains

Items per train is the sum of all wagons' capacity (40 stacks for cargo wagon , 50000 fluid for fluid wagon & 100 shells for artillery wagon )

Top speed (later referred to as S) and acceleration (later referred to as A) depend on fuel type and train weight, for a coal-powered single locomotive without wagons they are 72 tiles/s and 9.26 tiles/s/s.

After some threshold the top speed starts decreasing linearly as train mass increases; acceleration is proportional to amount of locomotives pointing towards the travel direction and inversely proportional to train mass; deceleration is proportional to amount of wagons + amount of locomotives, inversely proportional to train mass, and affected by braking force (research) (train mass is the sum of all wagon and locomotive masses; see detailed info on wagon masses on locomotive , cargo wagon , fluid wagon , and artillery wagon pages).

Warning: The following calculations assume deceleration = acceleration and do not account for red lights.

Travel time is

```
(2S/A)+(distance-4*S^2/A)/S
```

if the stations are far enough for the train to achieve full speed. If they are closer than that, the time is

```
2*sqrt(distance/A)
```

Since a train has to make a trip back to load, the total throughput is

```
itemspertrain/(2*traveltime)
```

### Capacity

Basically items per transport unit. This depends in many cases on the item type you use. A cargo wagon has a capacity of 40 stacks. Stack size depends on the item type so this means that it can hold 2000 items for ore, or 4000 for steel or copper plates.

### Density

Measured in items per tile.

An item, that lays on ground has the size of 0.28 tiles 2 . On one tile we can place 12.752041 items, which means, that we can put in the best case 12 items on one tile.

#### Belts

For belts this is the same: We have two lanes on a belt, 4 items per lane or 8 item on one belt.

On belts there comes also another thing into play: Compression. Good compression is, when you fill a belt so, that you come to the maximum density and so to the maximum throughput .
See also physics of transport belts for more information.

### Stacks/chests

On the first glance, it is simple: A chest has the size of one tile. You have X number of stack in a chest, where you can put Y numbers of items into each, so the density is simply X × Y.

The thing changes, if you use mods, that add chest-like transport boxes, which enables to pack/box items.
