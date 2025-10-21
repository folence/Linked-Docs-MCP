---
title: Module - Factorio Wiki
source: https://wiki.factorio.com/Module
scraped_at: 2025-10-21 14:29:45
tags: [web, documentation]
---

# Module - Factorio Wiki

**Source:** [https://wiki.factorio.com/Module](https://wiki.factorio.com/Module)

Modules are items used to enhance existing buildings' capabilities. They are expensive, require appropriate research , and are produced slowly, but can eventually greatly improve the efficiency of a factory.

Quick usage summary:

- For more products per second a speed module should be used.
- For more products per input resource a productivity module should be used.
- For more products per watt of energy an efficiency module should be used (except in rare cases when productivity modules are also used - then a speed module might be better).
- For higher quality products, quality modules should be used, and they should not be paired with speed modules, whether directly in the machine or in beacons .

Note that changing a machine's energy consumption directly affects how much pollution the machine generates. This is the case because the pollution production rate is directly linked to the machine's energy consumption, so this applies even when power is produced in a pollution-free way.

## Contents

- 1 Types of modules 1.1 Speed module 1.2 Productivity module 1.3 Efficiency module 1.4 Quality module
- 2 Usage tips 2.1 Quality and module scaling 2.2 Examples of usage
- 3 Achievements
- 4 See also

## Types of modules

There are three types of modules in Factorio , each with 3 tiers of effect. Higher tiers have stronger effects but are more expensive. Note that the machine's properties (speed, energy consumption and pollution) cannot be reduced below 20% of the original value.

### Speed module

Speed modules increase the speed and energy consumption of a machine.

| Module | Speed bonus | Energy consumption | Quality |
|  | +20% +26% +32% +38% +50% |  |  | +20% |  | +26% |  | +32% |  | +38% |  | +50% | +50% | -1% |
|  |  | +20% |
|  | +26% |  | +32% |
|  | +38% |  | +50% |
|  | +30% +39% +48% +57% +75% |  |  | +30% |  | +39% |  | +48% |  | +57% |  | +75% | +60% | -1.5% |
|  |  | +30% |
|  | +39% |  | +48% |
|  | +57% |  | +75% |
|  | +50% +65% +80% +95% +125% |  |  | +50% |  | +65% |  | +80% |  | +95% |  | +125% | +70% | -2.5% |
|  |  | +50% |
|  | +65% |  | +80% |
|  | +95% |  | +125% |

Advantages & Disadvantages:

- Increases speed of machine.
- If used with productivity modules, it can increase the efficiency of the machine in terms of items produced per joule (or items produced per pollution generated).
- Increases energy use per cycle (exceptions exist). Increased energy usage means increased pollution generation (pollution depends on power usage).
- Reduced chance of producing quality items.

### Productivity module

Productivity modules provide a productivity improvement to a machine when placed inside item-producing buildings and labs . Each time the machine finishes crafting the recipe it is set to, an amount is added to the bar equal to the percentages of the productivity modules inside the machine. When the bar reaches 100%, an extra set of products is immediately generated without consuming any resources.

Productivity modules cannot be used for every recipe. They can generally only be used in recipes that make an intermediate products . If you have productivity modules in a machine and you change the recipe to one which cannot accept them (manually or via the circuit network , the machine will eject the modules.

Intermediate recipes which cannot accept productivity modules include (but are not limited to):

- barrel filling and emptying.
- Producing barrels from steel.
- Steam condensation (likely to prevent loops that can generate more water than put into them).

The non-intermediate product recipes can accept productivity modules are:

- Stone brick
- Concrete from molten iron (but not the standard concrete recipe).
- Artificial jellynut and yumako soils
- Overgrowth jellynut and yumako soils

Productivity modules cannot be placed in beacons .

| Module | Productivity bonus | Energy consumption | Speed | Pollution multiplier |
|  | +4% +5% +6% +7% +10% |  |  | +4% |  | +5% |  | +6% |  | +7% |  | +10% | +40% | -5% | +5% |
|  |  | +4% |
|  | +5% |  | +6% |
|  | +7% |  | +10% |
|  | +6% +7% +9% +11% +15% |  |  | +6% |  | +7% |  | +9% |  | +11% |  | +15% | +60% | -10% | +7% |
|  |  | +6% |
|  | +7% |  | +9% |
|  | +11% |  | +15% |
|  | +10% +13% +16% +19% +25% |  |  | +10% |  | +13% |  | +16% |  | +19% |  | +25% | +80% | -15% | +10% |
|  |  | +10% |
|  | +13% |  | +16% |
|  | +19% |  | +25% |

Advantages & Disadvantages:

- Creates an additional free item occasionally.
- Increases energy use per cycle.
- Increases pollution generated.
- Slows the machine.

### Efficiency module

Efficiency modules reduce the required electricity to run the machine. The lowest amount of energy that efficiency modules can be used to achieve is 20% of the machine's base energy usage.

| Module | Energy consumption |
|  | -30% -39% -48% -57% -75% |  |  | -30% |  | -39% |  | -48% |  | -57% |  | -75% |
|  |  | -30% |
|  | -39% |  | -48% |
|  | -57% |  | -75% |
|  | -40% -52% -64% -76% -100% |  |  | -40% |  | -52% |  | -64% |  | -76% |  | -100% |
|  |  | -40% |
|  | -52% |  | -64% |
|  | -76% |  | -100% |
|  | -50% -65% -80% -95% -125% |  |  | -50% |  | -65% |  | -80% |  | -95% |  | -125% |
|  |  | -50% |
|  | -65% |  | -80% |
|  | -95% |  | -125% |

Advantages & Disadvantages:

- Reduces energy use per cycle. Decreased energy usage means decreased pollution generation (pollution depends on power usage).
- Cannot lower energy usage below 20%.
- If used with productivity modules, sometimes the efficiency gain is lower than what a speed module could achieve.

### Quality module

Space Age expansion exclusive feature.

Quality modules increase the chance of items being produced in higher qualities, which in turn grant bonuses which makes items and buildings work more efficiently. Higher quality items have a lesser chance of being created. Note that quality modules themselves can be made with higher qualities, which further increases the chance of higher quality products being made.

| Module | Quality bonus | Speed |
|  | +1% +1.3% +1.6% +1.9% +2.5% |  |  | +1% |  | +1.3% |  | +1.6% |  | +1.9% |  | +2.5% | -5% |
|  |  | +1% |
|  | +1.3% |  | +1.6% |
|  | +1.9% |  | +2.5% |
|  | +2% +2.6% +3.2% +3.8% +5% |  |  | +2% |  | +2.6% |  | +3.2% |  | +3.8% |  | +5% | -5% |
|  |  | +2% |
|  | +2.6% |  | +3.2% |
|  | +3.8% |  | +5% |
|  | +2.5% +3.2% +4% +4.7% +6.2% |  |  | +2.5% |  | +3.2% |  | +4% |  | +4.7% |  | +6.2% | -5% |
|  |  | +2.5% |
|  | +3.2% |  | +4% |
|  | +4.7% |  | +6.2% |

Advantages & Disadvantages:

- Can provide higher quality items.
- Quality modules themselves can have higher quality. Modules with higher qualities have larger bonuses, further increasing the chance of better items being made.
- Slightly decreases speed of buildings.
- Not all higher quality items have bonuses.

## Usage tips

As a rule, the effects of multiple modules are additive, not multiplicative , meaning they don't have diminishing returns (except that consumption is capped to -80%), so if an assembler is making 2 items per second, adding one speed module 3 (+50% speed) will increase item production by 1/s, and a second speed module 3 will increase production by another 1/s. Consumption modifiers work the same way, for example if a machine is consuming 180kW, the first efficiency module 1 will reduce energy use by 54kW, the second will also reduce energy use by 54kW. There is no difference between putting two speed module 1's in one machine and two efficiency module 1's in a second machine, compared to putting one of each in both machines - in both cases the total items produced per second and average energy required per item is identical.

There is however synergy between productivity modules and speed modules, productivity modules reduce crafting speed which lowers the production rate of items and increases the energy consumed per item, the speed bonus from speed modules increases production rate of items and lowers the energy consumed per item - in fact when dealing with productivity modules, the reduction in energy consumption from the increased speed from speed modules can be greater than the increased energy consumption. For detailed calculations on the synergy between productivity modules and speed modules refer to this discussion as well as this warning .

Filling the device with speed modules is useful when a resource is infinite but the amount of resource pools is low. The best example would be oil deposits . Another good place to use speed modules would be for assembly machines which make products that take a long time to make, for example engine units. Using speed modules allows more compact setups, because one machine can provide materials to more consumers than normal. If used together with productivity modules, they can also increase efficiency (in terms of items produced per watt or per pollution generated) of a machine.

Filling devices with productivity modules is recommended when resources are scarce. An example would be more advanced products not being produced enough due to bottlenecks. It will take longer and more energy, but the overall amount of products per time will be higher. Productivity is especially useful in recipes that consume a lot of resources per second such as electronic circuits , as this will result in a lot of free items being created and quickly cover the cost of the module. Also by saving the need to mine ore, smelt plates and process intermediates for those free items the additional energy cost can be easily covered.

Filling devices with efficiency modules is recommended for electric furnaces as these use a lot of power. Note that making higher level efficiency modules are not worth it in terms of power saved vs materials used to build a solar panel setup with same power output so the only incentive is to further reduce pollution or space utilization. Modules are also able to control pollution , as pollution depends also on energy usage . So reducing a machine's energy usage by 40% with a efficiency module 2 will also reduce its pollution by 40%. Beware as this also works vice versa! Also note that if you're using productivity modules, a speed module can sometimes provide better efficiency gains due to the fact that the machine will now be producing much more items per second. Efficiency modules also generally don't work well in beacons.

### Quality and module scaling

Getting modules of higher quality improves the benefits of the modules but not their drawbacks. Modules of sufficiently high quality can eclipse at least some of their drawbacks.

Speed modules make machines faster, which effectively makes them act like more machines of the same type. But they also cause them to increase power consumption, and this increase is higher than the speed increase. So speed modules can make machines act as if there were more machines, but they consume more power than the equivalent number of un-moduled machines.

Quality changes things.

Because a higher quality speed module provides a higher speed bonus, but not higher power consumption, it is possible to reach a break-even point where the speed bonus is equal to or greater than the power penalty. Speed module 1s do not achieve this break-even point until legendary quality, when their 50% speed bonus exactly matches the 50% power penalty.

Speed module 2s also require legendary quality to surpass their power penalty, though since the speed bonus of 75% exceeds the power consumption of 60%, it effectively provides a small efficiency effect.

Speed module 3s reach this break even point at rare quality, with an 80% speed vs. 70% power.

Productivity modules have a similar break even point with regard to their speed penalty (though not their power penalty). Adding productivity to a process gives a de-facto speed increase in terms of the number of output products produced. The speed penalty of productivity modules offsets this de-facto speed increase. However, computing that break-even point is more complex.

5% productivity means that 5% more outputs are generated over a given space of time. So if a machine would have output 100 products in a given time, it outputs 105. A 5% speed penalty means the machine operates 5% slower. If a machine would have output 105 products in a given time, it only outputs 95% of that, which is not 100; it is 99.75.

Productivity module 1s have a 6% speed penalty. The minimum productivity bonus needed to overcome this speed penalty is 6.3%, which requires an epic prod 1 (though rare comes close). To offset the 10% speed penalty from a productivity module 2 , you need a productivity of at least 11.1%, which requires an legendary prod 2 (though epic comes very close). To offset the 15% speed penalty from a productivity module 3 , you need productivity of at least 17.6%, which requires an epic prod 3 (though rare comes very close).

Quality modules have unusual scaling for their quality bonuses due to how strong quality module 2s are. A rare quality module 2 has the same bonus as an uncommon quality module 3 . And a legendary quality module 2 beats any non-legendary quality module 3. With the Space Age mod, quality module 3s require superconductors , which makes acquiring quality versions of quality module 3s much more expensive than quality module 2s.

Efficiency modules have a similar scaling effect, though much more pronounced. An uncommon efficiency module 1 is almost as good as a common efficiency module 2 , and a rare eff1 nearly matches a common efficiency module 3 . Quality versions of efficiency module 2s are usually nearly as good as eff3s of one step lower quality. Though getting quality versions of spoilage is much cheaper than superconductors ( bioflux can mass-produce nutrients , which can be recycled using quality modules to produce quality spoilage, with any lower quality spoilage being fed back into the recycler), so making quality efficiency module 3s is much easier than most other module 3s.

### Examples of usage

Electric furnaces are huge power hogs at 180 kW per furnace. 1 basic efficiency module reduces it by 54 kW (−30%) – almost a solar panel worth of power. Electric mining drills normally create 10 units of pollution , using 3 basic efficiency modules on them reduces their pollution production by 80% to 2 units per minute.

Using productivity module 3s in the rocket silo reduces the total resource cost for 1 rocket launch by almost 30%, saving 26k copper ore per rocket launch.

## Achievements

|  | Crafting with speed Craft a speed module 3 . |

|  | Crafting with efficiency Craft an efficiency module 3 . |

|  | Crafting with productivity Craft a productivity module 3 . |

|  | Crafting with quality Craft a quality module 3 . |

## See also

- Beacon
- Speed modules are sometimes more efficient than Efficiencies

| Production items |
| Tools | Repair pack Blueprint Deconstruction planner Upgrade planner Blueprint book |
| Electricity | Boiler Steam engine Solar panel Accumulator Nuclear reactor Heat pipe Heat exchanger Steam turbine Fusion reactor ( ) Fusion generator ( ) |
| Resource extraction | Burner mining drill Electric mining drill Big mining drill ( ) Offshore pump Pumpjack |
| Furnaces | Stone furnace Steel furnace Electric furnace Foundry ( ) Recycler ( ) |
| Agriculture | Agricultural tower Biochamber Captive biter spawner |
| Production | Assembling machine 1 Assembling machine 2 Assembling machine 3 Oil refinery Chemical plant Centrifuge Electromagnetic plant ( ) Cryogenic plant ( ) Lab Biolab ( ) |
| Environmental protection | Lightning rod Lightning collector Heating tower |
| Modules | Beacon Speed module Speed module 2 Speed module 3 Efficiency module Efficiency module 2 Efficiency module 3 Productivity module Productivity module 2 Productivity module 3 Quality module ( ) Quality module 2 ( ) Quality module 3 ( ) |
| Navigation | Logistics Intermediate products Space ( ) Combat Technology Environment |
