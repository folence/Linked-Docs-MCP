---
title: Tutorial:Applied power math - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Applied_power_math
scraped_at: 2025-10-16 15:45:55
tags: [web, documentation]
---

# Tutorial:Applied power math - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Applied_power_math](https://wiki.factorio.com/Tutorial:Applied_power_math)

In this tutorial we'll be answering the question: how much coal is needed to power a factory?

First off, we need to know: how much power does our factory use? That's easy - you can check the electricity tab by clicking on a power pole.

Here we see one radar using 300 kW of electrical power P . Factorio uses real science here. The unit of power, or energy transfer, is measured in Watt (W). A kilowatt (kW) is 1000 W, a megawatt (MW) is 1000 kW, and if you're lucky enough to ever make a factory big enough, a gigawatt (GW) is 1000 MW.

So that answers the question of how much power our factory uses. To keep our factory running at full speed we need to maintain 300 kW. For ease of comparison, we'll convert that to 0.3 MW.

Next question! How much energy E is released when burning one piece of coal? That's also easy, because it tells us when we hover over it: 4 MJ.

A Joule is the standard measure of energy E . As with Watts a kilojoule (kJ) is 1000 J, and so on. There is a fixed relationship between Joules and Watts. 1 Joule of energy can provide 1 Watt of power for 1 second of time. So one Joule is equal to one Wattsecond.
As a formula:

E = P ⋅ t [ J ] = [ W ] ⋅ [ s ]

So to run our factory at 0.3 MW, we need to consume 0.3 MJ every second.

## Quiz

How long could one piece of coal E = 4 MJ run
our single radar P = 0 . 3 MW ?

Expand to reveal answer

J = P ⋅ t t = J P = 4 MJ 0 . 3 MW = 4 0 0 0 0 0 0 J 3 0 0 0 0 0 W = 1 3 . 3 3 3 s

A bit more than 13 seconds.

What is the maximum size factory (in watts)
a single piece of coal E = 4 MJ could run for t = 5 s ?

Expand to reveal answer

J = P ⋅ t P = J t = 4 MJ 5 s = 4 0 0 0 0 0 0 J 5 s = 8 0 0 0 0 0 W = 0 . 8 MW

0.8 megawatts.

BONUS! A metric ton of real world coal m = 1 ton can produce about 7.2 GJ in an electrical power plant . How much does a piece of Factorio coal weigh?

Expand to reveal answer

The energy ratios will match the weight ratios, so:

m Factorio m real = E Factorio E real ⇔ m Factorio = E Factorio ⋅ m real E real 1 unit = 4 MJ ⋅ 1 ton 7 . 2 GJ = 4 0 0 0 0 0 0 J ⋅ 1 0 0 0 kg 7 2 0 0 0 0 0 0 0 0 J = 0 . 5 5 5 5 5 5 kg = 5 5 5 . 5 5 5 g

About 555g! Still doesn't explain how our character can carry so much of it...

Now we have everything we need to answer our initial question: how much coal do we need to power our factory? Well, the question actually needs to be a bit more precise: how much coal do we need per second to power our factory?

Aside: why did the radar run for 20s and not 13.5s (50% of 27s)?

Because it doesn't turn on and off instantly, the radar's demand of electrical power ramps up before reaching its operating power demand, therefore its electrical power usage is a function of time p el ( t ) . When speaking of a machine using power over time, the common equation symbol is W for performed work , which must be equal to the amount of energy supplied E s u p p l y . To easier visualize the amount of energy or work, in the real world, instead of Joule, the unit in use is the kilowatt-hour (kWh).

E s u p p l y = W = ∫ p el ( t ) d t

However, as the accuracy of integration is not required, to conservatively approximate the required power supply the equation can be simplified by treating the average power P ¯ el as the radars peak operating power P ^ el within a duration T as a constant.

E s u p p l y = ∫ t 0 t 0 + T P ^ el ( t ) d t = P ^ el ⋅ T

For completeness sake it should be mentioned that the boilers turn 4 MJ of chemical energy E chem stored in coal, to 4 MJ of thermal energy E therm stored in the steam, which steam turbines only consume as the grid demands electrical energy E el , where the grid then transfers electrical power per second .

## Quiz

How much coal per second is needed to power a 20 MW factory?

Expand to reveal answer

Since E = P ⋅ t , a 20 MW factory will consume 20 MJ/s. Since coal contains 4 MJ, we'll need 5 coal per second .

5 ⋅ 4 MJ = 2 0 MW

BONUS! How many mining drills are needed to produce that much coal?

Expand to reveal answer

Per the linked page, an electric mining drill mines 0.5 coal per second, so we'll need 10 electric mining drills .

5 units s 0 . 5 units s = 5 .

SECOND BONUS! The average American household uses 3.2 GJ in a month (typically expressed as 888 kilowatt-hours ). How much Factorio coal would be needed to power one of these homes for that period, and how many homes could a steam engine support ( 900 kW ), assuming the power is used at a constant rate? (Assume 30 days in a month.)

Expand to reveal answer

3 . 2 G J = 3 2 0 0 M J 3 2 0 0 M J 4 M J = 8 0 0 3 2 0 0 M J ⋅ 1 m 3 0 d ⋅ 1 d 2 4 h ⋅ 1 h 6 0 m i n ⋅ 1 m i n 6 0 s = 1 2 3 4 . 5 6 7 9 W 9 0 0 k W 1 2 3 4 . 5 6 7 9 W = 7 2 9

800 pieces of coal per household and a single steam engine could power 729 households exactly.
