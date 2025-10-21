---
title: Fulgora - Factorio Wiki
source: https://wiki.factorio.com/Fulgora
scraped_at: 2025-10-21 15:46:49
tags: [web, documentation]
---

# Fulgora - Factorio Wiki

**Source:** [https://wiki.factorio.com/Fulgora](https://wiki.factorio.com/Fulgora)

Space Age expansion exclusive feature.

Fulgora is a new barren desert planet . Its surface is split between island-like plateaus, and deep oilsands. During the night, the planet is ravaged by lightning storms, damaging buildings.

Planet discovery Fulgora (research) is required to travel to the planet.

## Contents

- 1 Achievements
- 2 Exclusive Items
- 3 Surface 3.1 Properties
- 4 Biomes 4.1 Terrain
- 5 Mechanics 5.1 Lightning 5.2 Lightning rods and collectors 5.3 Natural resources
- 6 Access to basic resources
- 7 Space routes
- 8 Orbit 8.1 Properties
- 9 Gallery
- 10 Trivia
- 11 History
- 12 See also

## Achievements

|  | Visit Fulgora Travel to planet Fulgora . |

## Exclusive Items

Scrap can only be found on Fulgora, in mineable scrap patches or from detritus scattered across the planet.

The following items are unlocked on Fulgora and can only be crafted on-planet:

- Electromagnetic science pack
- Electromagnetic plant
- Lightning collector
- Lightning rod
- Recycler

The following items are unlocked on Fulgora but can be crafted elsewhere:

- Mech armor
- Personal battery MK3
- Energy shield MK2
- Personal roboport MK2
- Quality module 3
- Tesla turret

## Surface

### Properties

| Property | Value |
| Pollutant Type | None |
| Day Night Cycle | 3 Minutes |
| Magnetic Field | 99 |
| Solar Power | 20% |
| Pressure | 800 |
| Gravity | 8 |

## Biomes

Fulgora is split between two distinct biomes.

- Plateaus are islands dotted around the landscape. They are the only biome where factories can be built. Some plateaus are home to alien ruins , which have fulgoran lightning attractors , which can protect your buildings until unlocking your own lightning rods . Other plateaus hold scrap , Fulgora's sole resource.
- Oilsands are the lowlands between the plateaus. No buildings can be built in them except for rail supports . You can walk through them, but occasional oilpatches will slow you to a crawl. An offshore pump can be placed on the edge of oilsands to produce an unlimited amount of heavy oil .

### Terrain

Fulgoran terrain is mainly composed of oillands , on which nothing except for rail supports can be built. Traversal by foot across the oillands is possible, but slow. The oillands are further divided into deep and shallow areas, with deep areas slowing down player movement even further and not even allowing for rail supports to be built until rail support foundations (research) is researched.

However, the oillands are also scattered with islands of various sizes, on which normal construction is possible. At first, these are the only place on Fulgora where factories can be built, as foundation for building on top of the oillands requires research that can not be performed until much later.

The islands come in three size classes:

- Small islands with high amounts of resources, but with little room to build on
- Medium islands with lower amounts of resources, and with sufficient room for a small factory
- Large islands with no resources, but with enough room to build the main part of a medium-sized factory

It is possible for two or more islands to overlap, potentially creating an even larger island that does have local resources. However, most islands are detached, meaning that transport between islands will have to occur by train. In many cases, the distance between two islands is also too vast for roboports or big electric poles to reach, thus requiring local logistic and electric networks to be built, as neither roboports nor power poles can be built on the oillands without foundation .

Islands are also scattered with fulgorite , Fulgoran lightning attractors , Fulgoran ruins and Fulgoran vault ruins , allowing players without the recycler to get access to basic resources.

## Mechanics

### Lightning

During nighttime , dense thunderstorms occur on Fulgora, with frequent lightning strikes occurring across the surface. Lightning will strike each chunk once, every 10 seconds or so ( lightnings_per_chunk_per_tick = 1 / (60 * 10), --cca once per chunk every 10 seconds (600 ticks) )

If a lightning strike is set to occur near a lightning rod , lightning collector , or Fulgoran lightning attractor , then the lightning will always hit said entity, rendering the lightning harmless. However, if such an entity can not be found, the lightning will strike where it occurs, causing damage to nearby entities.

Lightning will prefer striking the entity with the highest priority, choosing randomly between entities tied for highest priority.

| Entity | Priority value |
| Lightning collector | 10,000 |
| Lightning rod | 1,000 |
| Fulgoran lightning attractor | 1,000 |
| Fulgoran vault ruin | 95 |
| Colossal Fulgoran ruin | 94 |
| Huge Fulgoran ruin | 93 |
| Big Fulgoran ruin | 92 |
| Medium Fulgoran ruin | 91 |

| Entities | Category |
| Anything with the "Metal" impact soundset/category? |
| Pipe Pipe to ground Pump Offshore pump | Pipes and pumps |
| Small electric pole Medium electric pole Big electric pole Substation | Electric poles |
| Power switch Accumulator | Electric routing |
| Recycler Assembling machine 1 Assembling machine 2 Assembling machine 3 | Recyclers and assemblers |
| Beacon | Beacons |
| Radar | Radars |
| Roboport Logistic robot Construction robot | Roboports and bots |
| Burner inserter Inserter Long handed inserter Fast inserter | Inserters (but not bulk / stack inserters ) |
| Iron chest Steel chest Storage chest Passive provider chest Active provider chest Requester chest Buffer chest | Metal chests (notably not wooden chests ) |
| Cargo pod | Landed cargo pods |
| Steel furnace Electric furnace | Metal furnaces |
| Heat exchanger Heat pipe | Heat exchangers and pipes |
| Fusion generator Fusion reactor | Fusion power |
| Car Tank | Cars and tanks |
| Train stop | Train stops |
| Electric energy interface Asteroid collector Thruster | Some modded situations |

| Entities | Category |
| Legacy rail Rail Rail ramps and elevated rails Rail support | Rail pieces |
| Rail signal Rail chain signal | Rail signals (notably not train stops ) |
| Locomotive Artillery wagon Cargo wagon Fluid wagon | Trains |
| Wall Land mine | Walls and mines |
| Tree Rock Fulgorite | Trees and entities that count as a rock for filtered destruction |

### Lightning rods and collectors

Lightning rods and lightning collectors serve a secondary function beyond protecting an area from lightning strikes. They convert lightning into stored power, which they quickly discharge into the local electric system . With enough accumulators to last during daytime or between lightning strikes, this can serve as the factory's main power source.

With this, lightning on Fulgora becomes both a curse and a blessing: players must keep their factory covered by lightning rods or collectors to avoid damage, and nighttime exploration becomes dangerous and risky. However, to an established base, lightning become a convenient source of electric energy, which is especially important given the weak solar output on Fulgora's surface and the difficulty of setting up a global electric network on Fulgora before foundation becomes available.

### Natural resources

Aside from numerous items that can be collected by mining ancient ruins, only two "natural" resources occur on Fulgora, those being heavy oil and scrap .

Heavy oil can be obtained in infinite and non-diminishing amounts by placing an offshore pump on the shore of an island, allowing it to collect heavy oil directly from the oillands.

Scrap is found in deposits on small and medium sized islands, as if it were an ore. However, in stark contrast to most other natural resources, scrap is not directly processed into a single basic resource like iron or copper plates using traditional production methods. Rather, it is recycled to produce a variety of items. Players can also recycle by hand provided the recipe has been unlocked.

| Input | Output | Chance | Rate |
| Scrap | Iron gear wheel | 20% | 0.5/s |
| Solid fuel | 7% | 0.175/s |
| Concrete | 6% | 0.15/s |
| Ice | 5% | 0.125/s |
| Steel plate | 4% | 0.1/s |
| Battery | 4% | 0.1/s |
| Stone | 4% | 0.1/s |
| Copper cable | 3% | 0.075/s |
| Advanced circuit | 3% | 0.075/s |
| Processing unit | 2% | 0.05/s |
| Low density structure | 1% | 0.025/s |
| Holmium ore | 1% | 0.025/s |

Since this list includes intermediate products, such as processing units , but no iron or copper plates, players are generally forced to further recycle many of these items in order to obtain their ingredients. Players are thus left with the decision of what items to recycle, all while having to avoid cluttering their belts with unused resources.

## Access to basic resources

- Water can be obtained from ice (from recycling scrap ) via ice melting
- Stone can be obtained by recycling scrap
- Iron ore can be obtained by recycling concrete
- Iron plate can be obtained by recycling iron gear wheel , battery , or electronic circuit
- Copper plate can be obtained by recycling copper cable , battery , or low density structure
- Coal cannot be obtained and must be shipped in from other planets. However: Plastic bar can be obtained by recycling advanced circuit or low density structure There are no enemies on-planet, so explosives -based ammunition or grenades are not needed
- Crude oil is not available, but heavy oil is readily available using offshore pumps
- Copper ore is not available as the only recipe it is used in is copper plates and smelting processes cannot be reversed

## Space routes

Fulgora is connected to 3 other planets: Nauvis , Gleba , and Aquilo .

| Planet | Distance (km) |
| Nauvis | 15,000 |
| Gleba | 15,000 |
| Aquilo | 30,000 |

Asteroid rate graphs:

| Space route from Nauvis to Fulgora | Space route from Gleba to Fulgora | Space route from Fulgora to Aquilo |

Graph legend:

| Asteroid type | Chunk | Medium | Big |
| Metallic | ● Blue | ● Red | ● Cyan |
| Carbonic | ● Orange | ● Yellow | ● Brown |
| Oxide | ● Green | ● Magenta | ● Purple |

## Orbit

### Properties

| Property | Value |
| Solar Power | 120% |

| Asteroid Type | Spawn Ratio |
| Metallic asteroid chunk | 4 |
| Carbonic asteroid chunk | 3 |
| Oxide asteroid chunk | 1 |
| Promethium asteroid chunk | 0 |

| Asteroid Size | Spawn % |
| Chunk | .25 |
| Medium | .25 |
| Big | 0 |
| Huge | 0 |

Note:

- Chunks spawn at Nauvis at 1.25%
- Huge Asteroids only spawn past Aquilo

## Gallery

- Example landscape of Fulgora.
- Fulgora seen on the expansion's title screen.

## Trivia

- The planet's ruins suggest that an unknown civilization once existed there before the game's events.
- In mythology, Fulgora is the Roman personification of lightning, and a shieldmaiden to the god of thunder, Jupiter.
- The planet is based on real-world desert planets , as well as lightning observed on other planets like Jupiter, Saturn, Uranus, and Neptune.

## History

- 2.0.7 : Introduced in Space Age expansion.

## See also

- Aquilo
- Gleba
- Nauvis
- Vulcanus
- Space platform
- Tutorial:Scrap recycling strategies

| Space |
| Planetside buildings | Rocket silo Cargo landing pad Cargo pod |
| Space platform | Space platform foundation Cargo bay Asteroid collector Crusher Thruster Space platform hub |
| Rocket cargo | Satellite Space platform starter pack |
| Asteroids | Metallic asteroid chunk Carbonic asteroid chunk Oxide asteroid chunk Promethium asteroid chunk |
| Locations | Nauvis Vulcanus Gleba Fulgora Aquilo Solar system edge Shattered planet |
| Navigation | Logistics Production Intermediate products Combat Technology Environment |
