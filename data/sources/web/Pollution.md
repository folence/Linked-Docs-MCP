---
title: Pollution - Factorio Wiki
source: https://wiki.factorio.com/Pollution
scraped_at: 2025-10-21 14:29:43
tags: [web, documentation]
---

# Pollution - Factorio Wiki

**Source:** [https://wiki.factorio.com/Pollution](https://wiki.factorio.com/Pollution)

Pollution is represented as an abstract "cloud", updated per chunk every 64 ticks (which is 4 ticks more than a game-second). It is visible on the map if the "pollution" setting is on, and appears as a blocky red cloud.

It is produced by many buildings involved in processing items and spreads outwards at a steady rate.

The evolution factor is not increased by the spreading/absorbed pollution, but by the pollution produced by all the player's machinery at every tick. This means that no matter how hard the player tries to contain the pollution, enemies will still evolve at the same rate. They just won't attack the player as frequently. The pollution cloud is used to trigger biter attacks and determines the size of the attacks.

Pollution settings can be changed via map generation settings, or can be disabled entirely.

## Contents

- 1 Pollution spread
- 2 Pollution dissipation
- 3 Native life
- 4 Modules
- 5 Production/Absorption 5.1 Polluters 5.2 Space Age polluters 5.3 De-polluters 5.3.1 Spawners 5.3.2 Chunks 5.3.3 Trees 5.3.4 Biochambers
- 6 Spores
- 7 Achievements
- 8 History
- 9 See also

## Pollution spread

As soon as a chunk has reached 15.0 pollution it starts spreading in all four cardinal directions at a rate of 2% per 64 ticks. Pollution can generate new chunks if it needs to spread to them.

For example, a chunk with 400.0 pollution and 4 adjacent chunks with 100.0 pollution each, raises the pollution in all adjacent chunks by 8.0 while reducing its own pollution by 32.0. But every one of the 4 surrounding spreads 2.0 pollution "back" to the center chunk, so it only loses 24.0 + absorbed value .

## Pollution dissipation

- Every chunk (32x32) of map slowly reduces the pollution it covers (See #Chunks ). So the more the pollution spreads, the more is absorbed.
- Trees also absorb some pollution (See #Trees ).
- Spawners absorb a great amount of pollution, and use this to assign enemies to attacks.

## Native life

Pollution attracts biters to the Player's factory. Biters who find themselves in a polluted area will attempt to reach the source of pollution and destroy it. Any water near the source of pollution will turn green, which is a visual-only effect. The effect can be turned off by disabling animated water in the graphics settings.

If a chunk's pollution is greater than 20, each enemy spawner absorbs 20 + 0.01 * [chunk's pollution] every 64 ticks, otherwise it absorbs 3 times the amount of pollution needed for the most expensive unit it can spawn for the current evolution factor.

Higher pollution values decrease the time it takes for biters to join the attack force. After a certain amount of pollution is absorbed the spawner sends one of its biters/spitters to a rendezvous point. Every 1 to 10 minutes (random) the mustered biters launch an attack. If not all biters have arrived at the rendezvous point by that time, they will wait up to an additional 2 minutes for stragglers.

This also applies to pentapods on Gleba .

Required pollution to add an additional biter/spitter to the attack wave:

| Type | Pollution |
| Small biter | 4 |
| Medium biter | 20 |
| Big biter | 80 |
| Behemoth biter | 400 |
| Small spitter | 4 |
| Medium spitter | 12 |
| Big spitter | 30 |
| Behemoth spitter | 200 |

## Modules

Modules that list "+x% pollution" increase pollution multiplier, not a flat pollution rate. Final pollution value is (pollution multiplier * energy usage multiplier * base pollution), meaning heavily boosted buildings are likely to account for most of the pollution produced in a factory.

## Production/Absorption

These tables contain information about the levels of pollution produced/absorbed by items in the base game.

### Polluters

| Structure | Pollution per minute at full power |
| Stone furnace | 2 |
| Steel furnace | 4 |
| Electric furnace | 1 |
| Burner mining drill | 12 |
| Electric mining drill | 10 |
| Pumpjack | 10 |
| Assembling machine 1 | 4 |
| Assembling machine 2 | 3 |
| Assembling machine 3 | 2 |
| Boiler | 30 |
| Oil refinery | 6 |
| Chemical plant | 4 |
| Centrifuge | 4 |

Fire on the ground and burning trees produce 0.3 pollution per minute.

### Space Age polluters

| Structure | Pollution per minute at full power |
| Foundry | 6 |
| Electromagnetic plant | 4 |
| Cryogenic plant | 6 |
| Recycler | 2 |
| Big mining drill | 40 |
| Heating tower | 100 |
| Biolab | 8 |
| Crusher | 1 |

### De-polluters

#### Spawners

Every 64 ticks, spawners absorb pollution until they have absorbed more than 3 times the amount needed to send the most expensive unit at the current evolution level.

If they have not absorbed more than that threshold, they will absorb 20 + 0.01 * [chunk's pollution] and check the threshold again.

Note that absorbing pollution is not for spawning biters, but for sending biters to an attack group. Spawners will spawn enemies regardless of pollution absorption until they reach their spawn limit.

Captive biter spawners absorb 1 pollution per minute. Captive spawners which have decayed to the wild type use the rules above for pollution absorption.

#### Chunks

Every chunk has a natural absorption rate per second which is determined by the sum of the pollution absorption of its floor tiles .

| Tile | Pollution per tile per second | Pollution per chunk per minute |
| Water, green water, deep water, deep green water, shallow water, mud water | -0.000025 | -1.536 |
| Grass 1-4 | -0.000018 | -1.10592 |
| Dirt 1-7, dry dirt | -0.000018 | -1.10592 |
| Red desert 0-3 | -0.000015 | -0.9216 |
| Sand 1-3 | -0.000015 | -0.9216 |
| Nuclear ground | -0.0000125 | -0.768 |
| Path tiles (Stone bricks, concrete etc), landfill | 0 | 0 |
| Special tiles (Lab tiles, tutorial grid, Water Wube) | 0 | 0 |
| Out of map | -0.0001 | -6.144 |

#### Trees

Every single tree absorbs a small amount of pollution in its chunk per second. If the total pollution in a chunk is above 60 units, once per second some of the trees in that chunk each have a chance to either lose one stage of leaves (33% or 50% damage) or have their leaves become one stage more gray (6.7% damage). Regardless of whether the tree loses leaves or gets grayer, 10 pollution are absorbed by the tree. A tree stops losing leaves/becoming more gray once the sum of its gray percentage and its leaves lost percentage is above 120%. Half of trees stop their leaf progression one stage earlier. As the grayness and leaf stage are then locked for that tree forever, it is possible for trees to keep some leaves in heavily polluted chunks but in turn be very gray, or the other way around. The less dense the leaves, the slower the tree absorbs pollution, however tree grayness does not affect pollution absorption.

| Object | Stage | Pollution per second |
| Tree, red tree, brown tree | 0 (Max leaf density) | -0.001 |
| 1 | -0.00067 |
| 2 | -0.00033 |
| 3 (Min leaf density) | 0 |
| Dead dry hairy tree | No stages | -0.0001 |
| Dead gray trunk | No stages | -0.0001 |
| Dead tree - desert | No stages | -0.0001 |
| Dry hairy tree | No stages | -0.0001 |
| Dry tree | No stages | -0.0001 |

#### Biochambers

The biochamber "generates" negative pollution, at a base rate of -1 per minute. This effectively means that the building removes pollution while active.

This pollution value works like any other building, including how it scales with energy consumption. That is, if a module affects its energy consumption, the pollution is proportionately higher as well. However, because the base rate is negative, the Biochamber "generates" more negative pollution. Productivity modules and their direct pollution increase work in a similar way, boosting the negative pollution of the building even more.

## Spores

Spores are a unique form of pollution on Gleba. They are generated when yumako trees or jellystems are harvested (not destroyed). Machines do not produce spores, with the only exception being the agricultural tower . Spores are displayed as green squares on the map.

Spores will attract the native inhabitants of Gleba, pentapods .

Spores are consumed by egg rafts (pentapod nests) and most tiles. Biochambers do not absorb spores.

| Entity | Spores generated | Generates spores |
| Yumako tree | 15 | Per harvest |
| Jellystem | 15 | Per harvest |
| Agricultural tower | 4 | Always |

## Achievements

Pollution is directly connected to the following achievement:

|  | It stinks and they don't like it Trigger an alien attack by pollution . |

Spores are directly connected to the following achievement:

|  | It stinks and they do like it Attract a group of pentapods using spores. |

## History

- 2.0.43 : Trees no longer take damage from spores nor absorb spores as a result of taking pollution damage. Gleba wetlands, lowlands, and water tiles now absorb 3 times as many spores as other tiles.

- 2.0.7 : Greatly increased default tile pollution absorption. (Out of map x10, water and nuclear ground x5, rest roughly x2.5)

- 0.17.12 : Added pollution tab to the production statistics. Spawner tooltip (including the pollution statistics), shows distribution of biters spawn for the current evolution factor with the pollution costs. Pollution generation is now shown in the x/s format both on the entity and in the item/crafting slot. Internal pollution values have been normalized, and they are now roughly 60 times less compared to what they were.

- 0.17.0 : Rebalanced assembling machine 1,2 and 3 power consumption and pollution - higher tiers eat more power, but produce less pollution. Changed spawner pollution absorption logic so that all the pollution on a chunk doesn't build up un-spent in a single spawner.

- 0.13.2 : Optimized rendering of huge pollution clouds on the map.

- 0.13.0 : Large amounts of pollution is created when burning fires. Pollution creation of the productivity module was reduced drastically. Optimized pollution rendering on map and minimap.

- 0.12.0 : Trees degenerate slowly when exposed to pollution at high levels.

- 0.8.0 : Added option to turn off pollution visibility even when detailed info is on.

- 0.7.1 : Speed modules no longer produce extra pollution. Added missing pollution descriptions. Pollution is only shown on the minimap with alt mode on.

- 0.7.0 : Introduced concept of pollution.

## See also

- Crafting
- Modules
- Enemies
