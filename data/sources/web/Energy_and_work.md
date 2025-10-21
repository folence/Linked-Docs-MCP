---
title: Energy and work - Factorio Wiki
source: https://wiki.factorio.com/Energy_and_work
scraped_at: 2025-10-21 14:29:58
tags: [web, documentation]
---

# Energy and work - Factorio Wiki

**Source:** [https://wiki.factorio.com/Energy_and_work](https://wiki.factorio.com/Energy_and_work)

Factorio simulates many aspects of real physics and the quite correct use of energy is one important aspect.

Energy and work are directly dependent.

For another explanation, see the Forum .

## Contents

- 1 Definitions
- 2 Types of energy
- 3 Types of work
- 4 Waste and pollution: differences from real physics

## Definitions

- Energy can be thought of as stored work. It is measured in joules (symbol J).
- Work is the result of converting one type of energy to another. It is also measured in joules. (See the Wikipedia article on work .)
- Power is the rate of work - the amount of work done, or energy produced, over a unit of time. It is measured in watts (symbol W). One watt is equal to one joule divided by one second, i.e. one joule per second.
- Efficiency is the ratio between useful work done and the energy expended. It usually expressed as a percentage. Its unit would be joules per joule, but dividing something by the same thing cancels them out, so it is dimensionless.
- Waste is the difference between energy consumed and useful work done.

If you have a source of power and apply it over some time in order to perform some physical task, you have performed work, using a quantity of energy.

See also Units#Work .

## Types of energy

Energy is available as:

- Fuel . The energy contained in a unit of fuel is described as its fuel energy . Each building or vehicle that can be fuelled generally consumes fuel at a rate according to its power rating as long as it's working. For example: A car's power is 250 kW, meaning it consumes 250 kJ worth of fuel per second while it's accelerating (or driving at maximum speed). Nuclear reactors consume uranium fuel cells at a rate of 40 MW. Like most other fueled appliances, this is constant as long as it has fuel to consume. Conversely, boilers consume fuel at a rate according to their load (rate of steam being carried away), up to a maximum of their power rating.
- Electricity taken from the electric network. In addition to active power consumption, appliances have a drain , the power they consume even when not working as long as they're connected to the power network. For example: An assembling machine 1 has drain 3 kW and power consumption 90 kW. It consumes 3 kJ per second while not working, and 93 kJ per second while working.
- Charge in accumulators , battery armor modules , and flying robots.

Abstractly, energy also exists as:

- The potential energy of a piece of ore or unit of oil/water on the ground or on/in a belt/pipe, compared to the same piece/unit under the ground/in the sea.
- Kinetic energy in robots, vehicles, and items, and the player's avatar while moving.
- The damage dealt by weapons, vehicles and fire.
- The additional order (i.e. reduced entropy) in an assembled item compared to its components.

## Types of work

One can observe work being done in Factorio in numerous ways. Mostly these are abstract and not measured in game in joules. For example:

- The player avatar moving their body and equipment around, mining, building, and crafting, performs work. Unlike in real life, this doesn't require any energy (i.e. your avatar doesn't need to eat); its efficiency is therefore infinite. On the other hand, biters and their spawners apparently absorb pollution and use its energy to move, bite, spit, and reproduce.
- Transport belts and offshore pumps perform work by moving their contents from one place to another. Turrets perform work by rotating to aim and pulling the trigger. Unrealistically, but as a conscious design decision, none of these require a source of energy, and so their efficiency is also infinite.
- Turrets (and other projectiles) also perform work by converting the chemical energy of a bullet's propellant to kinetic energy in the bullet itself, which itself proceeds to do work in the form of damage. Laser turrets convert electricity into damage rather more directly. Flamethrowers and flamethrower turrets convert the chemical energy of oil into damage.
- Vehicles ( cars , tanks and trains ) convert the chemical energy of fuel into kinetic energy (i.e. motion). When they collide with things, they convert some of this kinetic energy into damage (which is why they then slow down).
- Inserters and (non-offshore) pumps perform work by moving items and fluids from one place to another. This requires energy, either in the form of fuel (for a burner inserter ) or electricity (for other types).
- Burner mining drills and electric mining drills convert energy (in fuel and electricity respectively) into potential energy held by a piece of ore on the ground; pumpjacks do the same thing to put crude oil in a pipe.
- Labs perform work by converting science packs and electricity into research.
- Machines that produce items, converting input products into output products ( refineries , assembling machines etc.), do work by assembling the components into a more ordered form, as a product. The resulting increase in order is a form of potential energy. Most use electricity to do this; the major exceptions are stone furnaces and steel furnaces .

The types of work that are measured in joules in game are:

- Boilers convert the chemical energy of fuel into heat, which it transfers into water to produce steam .
- Nuclear reactors convert the nuclear energy in uranium fuel cells into heat. Heat exchangers then transfer this heat, conveyed by heat pipes , into water, producing steam.
- Steam engines and steam turbines turn the energy stored in steam into electricity.
- Solar panels convert sunlight into electricity. ("Sunlight" isn't an expendible resource, so this effectively has infinite efficiency.)

## Waste and pollution: differences from real physics

A process with higher efficiency (useful work per unit energy consumed) produces less waste. In real life, total work done is always equal to energy consumed, but the amount of useful work done may be (usually is) less, but cannot be more. In other words, a process can't have an efficiency greater than 100%, meaning it would do more work than the energy you put into it. This is known as the principle of conservation of energy. The difference between useful and total work is waste or entropy , usually in the form of heat; the impossibility of using (all) waste energy to perform work is known as the second law of thermodynamics.

The actual amount of work done by most processes in game is not quantified, but nonetheless they are generally not 100% efficient. This abstract inefficiency is represented by pollution , produced by almost all machines when they do work (as well as being what happens to the physical matter of fuel when it's consumed). One exception is the electric network. In real life electric cables, transformers etc. hum and get hot, but in Factorio the electric network does not produce pollution.

In Factorio, some things do however have greater than 100% efficiency: transport belts and offshore pumps move stuff without needing to be powered, turrets rotate and shoot without power, and players move around and build things without needing to eat.
