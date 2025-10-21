---
title: Power production - Factorio Wiki
source: https://wiki.factorio.com/Power_production
scraped_at: 2025-10-21 14:29:30
tags: [web, documentation]
---

# Power production - Factorio Wiki

**Source:** [https://wiki.factorio.com/Power_production](https://wiki.factorio.com/Power_production)

Electricity has to be produced before it can be transferred to consumers over the electric system . There are multiple methods to produce electricity:

## Contents

- 1 Steam engine power
- 2 Solar panels and accumulators 2.1 Optimal ratio 2.2 Calculations 2.3 Vulcanus 2.4 See also
- 3 Nuclear power
- 4 Heating tower
- 5 Lightning power
- 6 Fusion power 6.1 Ratio calculations
- 7 Ensuring enough energy is produced

## Steam engine power

Each steam engine needs 0.5 boilers when running at full capacity. One offshore pump can supply 200 boilers and 400 steam engines.

The above ratio can be calculated from information available in-game: One boiler consumes 1.8MW of fuel and produces energy stored in steam at 100% efficiency. One steam engine consumes 900kW (0.9MW) of energy stored in steam, so each boiler can supply 2 steam engines: 1 . 8 0 . 9 = 2 . One boiler consumes 6 units of water to produce 60 units of steam per second, one steam engine consumes 30 steam per second (3 units of water) and one offshore pump produces 1200 water per second, so each offshore pump produces enough water to supply 200 boilers: 1 2 0 0 6 = 2 0 0 . Two steam engines per boiler gives us 400. This produces the 1:200:400 ratio.

## Solar panels and accumulators

### Optimal ratio

The optimal ratio is 0.84 (21:25) accumulators per solar panel , and 23.8 solar panels per megawatt required by your factory (this ratio accounts for solar panels needed to charge the accumulators). This means that you need 1.428 MW of production (of solar panels) and 100MJ of storage to provide 1 MW of power over one day-night cycle.

A "close enough" ratio is 20:24:1 accumulators to solar panels to megawatts required (for example, a factory requiring 10 MW can be approximately entirely powered, day and night, by 200 accumulators and 240 solar panels - this approximation differs from optimal only in that it calls for 2 extra solar panels, which is negligible but remember that the difference between the "close enough" ratio and the optimal ratio increases as you add more solar panels).

This is taken from Accumulator / Solar Panel Ratio (which calculates this in an impressive mathematical way!) and another post in that thread (which calculates the solar panel to megawatt ratio in a different way).

### Calculations

The optimal ratio of accumulators per solar panel relies on many values in the game. These include the power generation of a solar panel, the energy storage of an accumulator, the length of a day , and the length of a night. There are also times between day and night called dusk and dawn which complicate the calculations. In vanilla factorio, without mods which change any of these values, the optimal ratio will be the same. This ratio is

A c c u m u l a t o r s S o l a r P a n e l s = ( d a y + d a w n ) g a m e d a y ⋅ ( n i g h t + d a w n ⋅ ( d a y + d a w n ) g a m e d a y ) ⋅ S o l a r P o w e r A c c u m u l a t o r E n e r g y

which, given the default time lengths of: day = 12500/60 s; dawn or dusk = 5000/60 s; night = 2500/60 s, and the default: Solar_power = 60 kW; Accumulator_energy = 5 MJ = 5000 kJ, gives the optimal ratio of 0.84 accumulators per solar panel. If the player uses mods which change the power generation of solar panels, or the energy storage of accumulators, but not the length of days, a simplified version of this equation can be used.

```
Accumulators / Solar_panels = 70 s × Solar_power / Accumulator_energy
```

This equation could also be used to remember the vanilla optimal ratio given its simplicity. If the only effect the mod has on the game is it changes the total length of one day, without changing the ratio of dusk : day : dawn : night, then the equation can be simplified as

```
Accumulators / Solar_panels = 0.002016 /s × game_day
```

where game_day is the number of seconds in the game day which is 25000/60 s by default.

### Vulcanus

In Space Age, the day/night cycle on Vulcanus is 90 seconds with each phase of that cycle proportionally smaller: day = 45 s; dawn or dusk = 18 s; night = 9 s. The formula above simplifies to:

```
Accumulators / Solar_panels = 15.2 s × Solar_power / Accumulator_energy
```

Additionally, solar power production in Vulcanus atmosphere is 400% of that of Nauvis. With normal quality solar panels and accumulators, the ratio is 0.72576 accumulator per solar panel. 3 accumulators per 4 panel is pretty close.

### See also

- Perfectly optimal solar network (Factorio forums)
- Solar ratios (Factorio forums)
- 1 solar panel produces 42KW after factoring in the night (Factorio forums)
- Day-Night cycle times in Space Age and Solar Power (Factorio forums)
- Solar Power in Space Age - Definitive Ratios for Planets, Qualities and Throughput-Limits (Factorio forums)

## Nuclear power

In general, nuclear power is produced by the following production chain: Uranium ore is mined and processed to uranium-235 and uranium-238 , then uranium fuel cells are created from the two. These fuel cells are then burned in a nuclear reactor to create heat. The heat is transferred via heat pipes to one or more heat exchangers , which convert water to steam that is then consumed by steam turbines to produce power.

A reactor without neighbor bonus needs 4 heat exchangers so that all its heat gets consumed. For each 100% neighbor bonus, the reactor needs 4 more heat exchangers.

| Ideal Ratio | Simple Ratio | Building |
| 2 | 1 | Offshore pump |
| 233 | 116 | Heat exchanger |
| 400 | 200 | Steam turbine |

## Heating tower

The Heating tower , initially researched on Gleba , is an alternate source of heat for Heat pipes and Heat exchangers . Unlike nuclear reactors, heating towers are traditional burner devices , burning standard fuels .

Heating towers burn fuel, extracting 16MW of power from the fuel. However, because they have 250% efficiency, they generate 40MW of heat from the fuel. Like a nuclear reactor, the heat must be transferred to heat exchangers to generate useful electricity. Since they use the same fuel, but can produce 2.5x the energy from it, one can think of a heating tower as a boiler "Mk 2".

A single heating tower can produce the same power output as a single nuclear reactor. However, they do not get neighbor bonuses the way reactors do. As such, the ratio of heating towers to exchangers is always 1:4.

Like reactors, they have a maximum temperature of 1000 C. And also like reactors, they will continue to burn fuel even after they reach their maximum temperature. This gives them a secondary use as a quick way to dispose of unwanted burnable materials, such as excess fruit products/ spoilage on Gleba or excess solid fuel on Fulgora .

Note that heating towers produce less pollution per MW of power produced than boilers. Boilers produce 3.6MW of power per pollution generated, while heating towers produce 24 MW per pollution.

## Lightning power

On Fulgora, when a lightning rod or lightning collector is struck by lightning, it becomes a short-lived source of electrical power. The way it works is as follows.

A single lightning bolt contains 1 GJ of energy. Rods and collectors can collect some portion of this energy and supply it to their connected grid.

A rod/collector has an energy capacity as well as an efficiency value (the latter varies by quality ). The efficiency value determines the percentage of the 1 GJ of energy contained in the bolt which will be stored by the rod/collector. If the energy absorbed from lightning exceeds the storage capacity of the rod, the excess is lost.

A normal quality rod has 20% efficiency, so a single bolt will charge the collector by 20% of 1,000 MJ, or 200 MJ. A normal quality collector, with an efficiency of 40%, will store 400 MJ.

Rods/collectors have a discharge rate of 150 MW. When they have stored energy, they will supply all the demands of the attached Electric system . This will provide power to any buildings in the same electrical system as the rod/collector, including accumulators . In addition, 150 MJ per second (2.5 MJ/tick) will be lost, unable to be used for anything. So lightning power is a "use it or lose it" arrangement.

A normal quality lightning rod struck by a single bolt will only generate power for a maximum of 1.33 seconds. A normal quality lightning collector will generate power for a maximum of 2.67 seconds. The principle advantages of collectors is the larger range for lightning strikes and their longer discharge times.

The key to taking advantage of this is to use accumulators. But because accumulators have a low charge speed compared to the rod/collectors' drains (0.3 MW at normal quality vs. 150MW), storing a significant fraction of the energy from a single bolt of lightning is not generally feasible. For a single lightning rod struck by a single bolt of lightning, 125 normal accumulators will draw 37.5 MW for just over 1 second, storing 40 MJ of the 200 MJ captured by the rod. The other 160 MJ are lost to the rod’s internal drain. 500 accumulators will store 100 MJ in 0.67 seconds, and 1,000 accumulators store 135 MJ in just under 0.5 seconds. To capture all the energy available in a lightning strike, the network must be able to absorb all the energy in a single tick: 12 GW for a normal rod, up to 60 GW for a legendary collector.

Do note that 500 normal quality accumulators cannot fit in the area protected by a single lightning collector, let alone the smaller area of a lightning rod.

## Fusion power

Fusion power requires the production of two ingredients to function: fusion power cells and fluoroketone (cold) . Both can only be produced on Aquilo using the planet's exclusive fluid resources, and holmium plates imported from Fulgora .

Fusion reactors consume the power cells, cold fluoroketone, and electricity to produce plasma . The plasma is fed into fusion generators which produce electricity and fluoroketone (hot) . The hot fluoroketone must then be fed into a cryogenic plant to cool it back down, which can produce a self-sustaining loop. However, as the reactors require electricity (10 mW) to generate plasma, there must be some other power source already on the network to jump-start the system. After that, even a single fusion generator will create enough power to sustain the reactor.

Because ammonia , which is needed to produce the power cells cannot be barrelled , production of them is confined to Aquilo. However, as the cold and hot fluoroketone can be barreled, it and the power cells can be shipped to other planets with relative ease.

### Ratio calculations

Fusion reactors produce plasma at a base temperature of 1 . 0 M ∘ C . Each directly connected reactor adds an additional 1 . 0 M ∘ C to the maximum achievable plasma temperature. The actual plasma temperature depends on the neighbor bonuses, which are determined by the arrangement of reactors and their current plasma production rate. For example, if a reactor produces plasma at its maximum rate, all reactors connected to this reactor receive a 100% neighbor bonus. The temperature used by generators is the average plasma temperature of all reactors in the setup.

The optimal ratio of fusion reactors to generators can be calculated in a single step:

G = ( R + N ) ⋅ P O P C

where:

- G is the optimal number of fusion generators for the given reactor setup
- R is the number of fusion reactors
- N is the sum of the neighbor bonuses of all reactors (expressed as an integer)
- P O is the maximum plasma output of a reactor
- P C is the maximum plasma consumption of a generator

Thus, the optimal reactor-to-generator ratio is R : G

If the fusion reactors and generators have the same quality tier (e.g. normal), then the formula simplifies to:

G = 2 ⋅ ( R + N )

Note :

- This formula applies to all quality tiers and mixed setups where reactors and generators share the same quality tier respectively.
- Initially, a not fully utilized fusion power setup will produce plasma at a lower temperature than what is possible. As more power is needed, more plasma is produced, and therefore the neighbor bonuses rise. With rising neighbor bonuses, the resulting plasma temperature also increases, resulting in more efficient plasma usage. This cycle continues until the setup reaches its maximum plasma temperature, allowing it to deliver peak power output.

## Ensuring enough energy is produced

Try this checklist before you completely revamp your power source. You may also use this to rectify brownouts/blackouts .

- Did you connect the steam engine to the electric system ? If not, a small yellow triangle will flash. To fix, Add some power poles near the steam engines that go to machines needing that power. Any power pole will work.
- Is steam able to reach all steam engines?
- Do your pipes have water? Look at the windows in the pipes, hover over the pipes! Place some pipes or a tank at the end to see if there is really water coming through. If not, ensure all pipes or underground pipes are connected together.
- Is the factory producing enough fuel (coal, solid fuel, uranium fuel cells)?
- Are there enough steam generators (boilers, heat exchangers)?
- Are there enough steam engines/turbines?

See also the applied power math tutorial to answer the question how much coal do I need?
