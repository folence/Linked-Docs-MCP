---
title: Tutorial:Nuclear power - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Nuclear_power
scraped_at: 2025-10-16 15:45:56
tags: [web, documentation]
---

# Tutorial:Nuclear power - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Nuclear_power](https://wiki.factorio.com/Tutorial:Nuclear_power)


|  |
| Page "Nuclear power" has been recommended for clean-up. Reason: This tutorial needs to be updated due to changes in Factorio 2.0. For example, it is now simple to automate nuclear power production control without any tanks since reactors can be wired directly to read their heat level. |
| This may mean fixing grammar or broken links, providing better explanations, or removing incorrect/outdated info. |
| Further recommendations for this page's clean-up can be made at Tutorial talk:Nuclear power . |

Nuclear power requires higher level technology compared to either solar power or steam boiler power, but it offers very high power output in exchange. It's a great solution for middle- to end-game power generation and it works well in combination with other power generation techniques.

This guide is written for people who want to know exactly how nuclear power works, but don't necessarily want all the solutions. It focuses on what you should do and what you should know to get Nuclear up and running, but doesn't tell you what to do or exactly how to solve the problems.

## Contents

- 1 First steps 1.1 Uranium ore 1.2 Ore processing 1.3 Fuel 1.4 Nuclear reactor 1.5 Heat exchanger 1.5.1 Heat pipes 1.6 Steam turbine 1.7 Simplest thing that works
- 2 Moving forward 2.1 Neighbor bonus 2.2 Always on! 2.3 Enrichment 2.4 Reprocessing fuel 2.5 Raw resource cost of running a single reactor (late game) 2.6 Weapons
- 3 Version
- 4 Other power related tutorials

## First steps

### Uranium ore

To start, you'll need uranium ore. It glows green, so you can't miss it. It tends to form smaller deposits, though, and you may have to search a while to find a good patch.

Like every other ore in the game, you can mine it with an Electric mining drill . Unlike every other ore, however, you will need more than just an Electric mining drill . You also need to supply sulfuric acid to the drill. The drills conduct excess acid through themselves, so a row of drills can be supplied by acid from a single side.

### Ore processing

Once you've got raw uranium ore, you'll need to process it into uranium-235 and uranium-238 . You do this in a centrifuge.

In an un-moduled centrifuge , you can process ten ore every 12 seconds.

Centrifuges produce a combination of U-235 (the light green stuff) and U-238 (the dark green stuff). Every ten ore processed have a chance to become precisely one of these two products. Out of every 10k ore you process, you can expect to get, on average:

| Count | Product |
| 7 | U-235 |
| 993 | U-238 |

That means you can roughly expect to get a single U-235 in one out of every 1428 ore. A centrifuge can then be expected to produce U-235 every 1716 seconds. Later on, this won't matter so much. However, when you first start out, this will be an important bottleneck.

### Fuel

Before you can burn it in a nuclear reactor, you need to create uranium fuel cells . You'll probably be using an assembling machine 2, so these will take 13.3 seconds to create as well. Which is fine because fuel cell creation will very rarely be the bottleneck.

You won't want to automatically convert all U-235 into fuel. Only convert what you need to fill your reactor. You're going to want a big fat stockpile of it when you research kovarex enrichment later on.

Fuel cells are produced in stacks of 10, and to produce one such stack you need 1 U-235, 19 U-238, and 10 iron plate.

Each fuel cell has a nominal energy value of 8 GJ, but it's possible to make them go even farther with reactor neighbor bonuses (more on that later).

### Nuclear reactor

Once you've got fuel, you'll need to burn it in a nuclear reactor. This is the first step toward turning it into usable energy.

A reactor will produce exactly 40 MW of heat energy. Since a Watt is a Joule per second, this means the reactor will consume one fuel cell every 200 seconds.

Once expended, reactors will produce a " used up uranium fuel cell ", which will need to be cleared. Initially, these will simply accumulate in a chest. Eventually, you can reprocess them into U-238.

The reactor needs input of fuel and produces heat that needs to be exported using heat pipes that go to a heat exchanger (unless a heat exchanger is attached to the reactor).

### Heat exchanger

The heat exchanger takes heat and uses it to convert water into steam . It works much like the boiler, but instead of burning fuel, you need to connect it to a heat source. The heat input is marked by a flame when you're placing it.

For simple reactor designs, you can connect it directly to your reactor (which produces heat at points also marked with a flame).

Heat exchangers also require water input, in precisely the way boilers do. They can heat up to about 10.3 units/second of water into about 103 units/second of 500°C steam. One water pump can maximally produce 1200 water/second, satisfying exactly 116.4 heat exchanger.

Heat exchangers produce nothing when they are below 500°C. Since they only cool as a consequence of heating water, they will never cool to below that temperature once they've reached it.

Heat exchangers transfer 10 MW of power, so you'll need 4 exchangers to fully consume the power produced by a lone reactor. (Neighbor bonuses can increase this significantly. Again, discussed later.)

The steam can then be transported to the steam turbine using normal pipes .

#### Heat pipes

More complex designs will require heat pipes. Unlike regular pipes, they have limited throughput, which means that shorter pipes are better.

Connect heat pipes point to point, flame to flame, exactly as you would with water pipes. Heat pipes cannot go underground, so if water pipes need to cross them, the water pipe will need to go under. They don't block movement, though, so you can walk right over them.

Throughput on heat pipes, in contrast to regular pipes, is limited. Here are some rough limits on transfer distance:

| Power | Distance |
| 40 MW | ~133 |
| 80 MW | ~59 |
| 120 MW | ~45 |
| 160 MW | ~30 |
| 240 MW | ~10 |
| ~278 MW | 4 |
| ~284 MW | 3 |
| ~290 MW | 2 |
| ~297 MW | 1 |
| ~302 MW | 0 |

Past these distances, less than 100% of the power will be transferred. This is because at this distance, the heat from the reactor does not travel fast enough to heat the pipe to beyond 500ºC in a running setup. However, if the heat is unused, the heat will spread much farther, because there is no heat loss over time or distance, so it builds up until it is used again.

Throughput may also be thought of in terms of exchangers per pipe. Exchangers can be placed on one or both sides of a heat pipe. Laying two or more pipes in parallel can increase the distance heat travels.

| Parallel Pipes | Exchangers on one side | Exchangers on both sides |
| 1 | 21 | 31 |
| 2 | 29 | 42 |

This picture also shows how distance between your heat source and heat exchangers will affect output. The last exchanger in a given row may not operate at full capacity.

### Steam turbine

These are the steam engine's beefy big brother. Using regular fluid pipes, you'll pipe the steam produced by heat exchangers into these turbines.

Steam turbines consume up to 60 units of steam/second, so you need roughly two steam turbines for every heat exchanger. At large scales, however, you can use fewer turbines, since exchangers only produce 103.09 steam/second, compared to the 120 steam/seconds two turbines can consume. The exact ratio, rounded up, is 1.718.

### Simplest thing that works

At this point, you have all the parts to build your very first reactor:

- A few uranium miners, supplied with sulfuric acid
- 1 Centrifuge, processing uranium ore
- 1 Assembling machine, making uranium fuel cells
- 1 Nuclear reactor
- 4 Heat exchangers, supplied by a single off-shore pump
- 8 Steam turbines

And, of course, assorted belts, inserters, filter inserters, and other tools for moving things around. This will produce a maximum of 40 MW of power.

## Moving forward

Past your simplest reactor, there are some additional nuclear features of which you should be aware.

### Neighbor bonus

This is a critical part of how nuclear designs scale, but it's not complicated. Simply put:

Every reactor gets +100% heating power for every active neighboring reactor.

Neighbors have to align completely on each side, so reactors will line up in a nice square grid. When they do, the neighbor bonus is activated. You can see the current bonus by hovering over an active reactor.

The bonus to heating power does not increase the fuel consumption. Rather, it simply increases the heat produced!

This, of course, means you'll need more heat exchangers and steam turbines to turn that heat into electricity.

| Configuration | Reactors | Exchangers | Water pumps | Turbines | Power | Power per reactor |
| Single | 1 | 4 | 1 | 7 | 40MW | 40MW |
| 2×1 | 2 | 16 | 1 | 28 | 160MW | 80MW |
| 2×2 | 4 | 48 | 1 | 83 | 480MW | 120MW |
| 2×3 | 6 | 80 | 1 | 138 | 800MW | 133MW |
| 2×4 | 8 | 112 | 1 | 193 | 1120MW | 140MW |
| 2×5 | 10 | 144 | 2 | 248 | 1440MW | 144MW |
| 2×6 | 12 | 176 | 2 | 303 | 1760MW | 147MW |
| 2×7 | 14 | 208 | 2 | 358 | 2080MW | 149MW |
| 2×8 | 16 | 240 | 3 | 413 | 2400MW | 150MW |
| 2×N | 2 ⸱N | 32 ⸱N | 0.275 ⸱N | 55.2 ⸱N | 320MW ⸱N | 160MW |

How to count heat exchangers: Count the number of edges where reactors fully touch. Double that. Add the total number of reactors. Then multiply it all by 4. That's your count of Heat Exchangers. You'll need 1.718 turbines per exchanger (rounded up). Each exchanger will provide up to 10 MW of power. One water pump can supply for exactly 1164MW of power or 116.4 exchangers.

### Always on!

Unlike every other power generation technique, nuclear reactors DO NOT scale down power usage. Nuclear reactors will continue consuming one fuel cell every 200 seconds, regardless of the need.

As the reactor consumes its fuel, it heats up to a maximum temperature of 1000°C. At that point, additional fuel burned is simply wasted. This is the only way to lose energy in the system as all heat transfers are perfectly efficient.

Turbines do scale their production (and steam consumption) to match demand. Likewise, exchangers won't consume heat if there's nowhere to put the steam.

The simplest solution to this problem is to add the following two items:

- An inserter
- A decider combinator

Wire the input of the combinator to the nuclear reactor, then open the reactor and tick both options "Read temperature" and "Read fuel". For the temperature signal, choose (the default).

Click the combinator, and set its signals to:

```
Conditions= 0AND< 650 

Output
X in 1 amount (X can be any signal)
```

Wire the output of the combinator to the inserter, then open the inserter and tick both options "Override stack size" and "Enable/disable". For the stack size choose 1. For the enable condition, choose X = 1. This way, it will only grab items when it is not at max temperature (1.0k) and will not grab over-excessive amounts of fuel, ensuring that no power will be wasted!

Note a fuel cell is added while the reactor's temperature is too high, drawing the maximum amount of power from the steam turbines, the reactor will max out its temperature and lose energy. As such, it is important to have the test temperature be low enough, relative to the amount of power being consumed, that the reactor will not hit 1000 C before the cell is fully consumed.

| Example fueling circuit | Nuclear reactor settings for monitoring | Decider combinator conditions for monitoring and control | Inserter settings for controlling fuel usage |

### Enrichment

Your first few patches of uranium ore will last you a reasonable length of time, but eventually you will start running out of ore and places to put extraneous U-238. Enrichment helps solve both problems.

The enrichment process takes 60 seconds in an un-moduled centrifuge. It requires 40 U-235 (!) and 5 U-238 and makes 41 U-235 and 2 U-238. In effect, it takes 3 U-238 and turns it into 1 U-235; it just requires an extra 40 U-235 and 2 U-238 along for the ride to act as a catalyst.

One un-moduled Centrifuge enriching uranium is sufficient to supply 33.33 reactors with fuel, assuming plenty of U-238. One Centrifuge with two Productivity modules is enough to supply 25.2 reactors, one Centrifuge with two Productivity modules 3 is enough to supply 28 reactors.

You only get 1 Uranium-235 from bonus productivity (not 41!) as it is a catalytic recipe.

### Reprocessing fuel

Eventually, you will run out of places to put spent fuel. You can use reprocessing to turn it back into U-238 to use for enrichment, fuel cells, or ammo. Of the 19 U-238 that go into each 10-pack of fuel cells, this returns 6. This significantly reduces the total ore requirement for nuclear fuel.

### Raw resource cost of running a single reactor (late game)

Water is free and infinite, so there are only two costs to run a Nuclear Reactor. One is the material cost for the buildings involved, and the other is the materials needed for the fuel cells. Since the building materials are only needed once, we will only consider the resources needed to produce enough fuel cells for a reactor to continously run. And we will do this computation for the late game by including Kovarex processing and the reprocessing of used fuel cells.

- 1 reactor uses 1 fuel cell every 200 seconds, which is 0.005 fuel cells per second
- To make 10 fuel cell the recipe uses 1 U235, 19 U238 and 10 Iron plate
- So 1 fuel cell costs 0.1 U235 + 1.9 U238 + 1 Iron plate
- 1 fuel cell cost after reprocessing the used fuel cells (1 used cell gives back 0.6 U238): 0.1 U235 + 1.3 U238 + 1 Iron plate
- 1 fuel cell cost after reprocessing + Kovarex (where you get 1 U235 for 3 U238): 0.3 U238 + 1.3 U238 + 1 Iron plate = 1.6 U238 + 1 Iron plate#
- 1 fuel cell cost after reprocessing + Kovarex (measured in raw ore cost): 16 Uranium ore + 1 Iron ore

So to power 1 reactor continously with Kovarex enrichment you need 0.005 times the above ore cost, which is 0.08 Uranium ore and 0.005 iron ore being mined every second . (Because a small fraction of U235 does not require Kovarex enrichment, the actual cost is marginally less, 0.0789 Uranium ore per second.)

### Weapons

With the Nuclear Age comes nuclear weapons. Uranium ammunition is top-tier, with 3 times as much damage as piercing rounds and when loaded into a tank mows down biter nests and clears swarms quite quickly. It uses U-238, so you've probably got plenty of it lying around.

On the other side, you can get atomic bombs , which are rockets (shot by a rocket launcher ) that do incredible damage. Be aware, they can easily kill you if you fire them anywhere near you, and even at max range, it's advised that you run in the opposite direction. Rather than a single explosion, they do damage in an expanding ring, giving you time to escape. They require a lot of U-235 and blue chips, so they're an expensive weapon.

## Version

This guide is compatible with Factorio 0.17, 0.16 and 0.15.13+.

## Other power related tutorials

- Applied power math
- Producing power from oil
