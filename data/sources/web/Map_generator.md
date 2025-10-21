---
title: Map generator - Factorio Wiki
source: https://wiki.factorio.com/Map_generator
scraped_at: 2025-10-21 14:29:28
tags: [web, documentation]
---

# Map generator - Factorio Wiki

**Source:** [https://wiki.factorio.com/Map_generator](https://wiki.factorio.com/Map_generator)

World generation is the procedure by which the in game landscape is generated. In short: a number of settings, editable at the start of a new world, define what that world will look like. This can dramatically alter gameplay — a new player is advised to start with the default settings before deciding to change their world.

## Contents

- 1 Map generation presets 1.1 Default 1.2 Rich resources 1.3 Marathon 1.4 Death world 1.5 Death world marathon 1.6 Rail world 1.7 Ribbon world 1.8 Lakes 1.9 Island
- 2 Manual configuration 2.1 Resources 2.2 Terrain 2.3 Enemy 2.4 Advanced 2.5 Map exchange string
- 3 Mechanics 3.1 Starting area 3.2 Chunks 3.2.1 Invisible chunks (fog of war) 3.2.2 Charting (removing fog of war) 3.2.3 Maximum map size and used memory
- 4 History

## Map generation presets

A preset may be chosen in the top left dropdown instead of manually configuring the generation. If playing in Space Age , presets will only change settings on Nauvis .

### Default

Normal settings. The recommended way to play Factorio.

All sliders are set to the center position. Map height and width is unlimited, peaceful mode is disabled.

All other settings are set to their defaults:

| Enemy expansion | Default | Evolution | Default |
| Enabled | Yes | Enabled | Yes |
| Maximum expansion distance | 7 | Time factor | 40 |
| Minimum group size | 5 | Destroy factor | 200 |
| Maximum group size | 20 | Pollution factor | 9 |
| Minimum cooldown (Minutes) | 4 |
| Maximum cooldown (Minutes) | 60 |

| Pollution | Default | Recipes/Technology | Default |
| Enabled | Yes | Technology price multiplier | 1 |
| Absorption modifier | 100% |
| Attack cost modifier | 100% |
| Minimum damage to trees | 60 |
| Absorbed per damaged tree | 10 |
| Diffusion ratio | 2% |

### Rich resources

Resources patches on Nauvis have a larger richness, so you don't have to expand far.

Difference from default: Resources have 200% richness instead of 100%.

### Marathon

Technologies are more expensive.

Difference from default: Technology price multiplier 4.

### Death world

Biters are more dangerous and evolve faster.

Difference from default: 200% enemy base frequency and 200% enemy base size on Nauvis, 75% starting area size, enemy evolution time factor is set to 200, pollution factor is set to 12. The pollution absorption and attack cost modifiers are set to 50% instead of 100%

### Death world marathon

Technologies are more expensive and biters are dangerous and plentiful. Only select this if you are a Factorio veteran.

Combines "Marathon" and "Death world" with some additional changes: Enemy evolution time factor is set to 150, pollution factor is set to 10. Attack cost modifier is set to 80% instead of 100% (50% for death world).

### Rail world

Resource patches are large and spread far apart, to encourage train systems. Biters won't create any new bases or re-expand into cleared territory.

Difference from default: Resources on Nauvis are set to 33% frequency and 300% size. Nauvis water is set to 200% scale and 150% coverage. The evolution time factor is set to 20 from 40 and enemy expansion is disabled.

### Ribbon world

The map height is limited to only 128 tiles, which introduces a range of challenges and interesting situations.

Difference from default: Map height on all planets is limited to 128. Resources on Nauvis are set to 300% frequency, 50% size and 200% richness. Nauvis water is set to 25% coverage and size. Starting area size is increased to 300%.

### Lakes

Lakes with consistent size and cliffs that tend to follow the coastline. Forest paths are disabled. The same elevation as Factorio 1.1.

Difference from default: Tree coverage is set to 50%. This preset uses the map and cliff generation from version 1.1

### Island

A large island in an endless ocean. Forest paths are disabled.

Difference from default: Tree coverage is set to 50%. Terrain map type is set to island. This preset uses the map and cliff generation from version 1.1.

## Manual configuration

It is possible experiment with different settings by opening the map preview, changing the settings and observing their effects. This makes it possible to directly observe what exactly particular settings modify in the world, beyond the textual descriptions provided on this page. If playing in Space Age , you can preview any planet by using the drop-down menu in the top right. There will also be additional settings for planet-specific settings, and each setting will show an icon telling which planet it affects.

The seed is the starting value for the random number generator that Factorio uses for generating the world based on the generation settings. This means that even with the same generation settings, the world can look very different depending on the seed. If playing in Space Age, a single seed will effect all planets at once.

All resources and terrain features can be disabled by unchecking the checkbox in front of them.

### Resources

Frequency determines the number of resource patches in a given area. It does not affect resource patch size or richness. A setting of 200% frequency that means roughly double the patches can be found in a given area.

The size setting adjusts the size of the resource patches. Setting the slider to 200% means the surface area of the patch is doubled.

Richness defines the yield of every ore tile and every oil field. If richness is set to 200%, each ore tile and oil field contains about double the amount of ore/oil. Outside of this, resource patch richness increases by distance from the starting area.

If playing in Space Age, resource settings can be changed for each planet individually, even if that resource appears on multiple planets. For example, coal can be configured differently for its appearences on Nauvis and Vulcanus .

### Terrain

Setting the map type to island generates a single island around the spawn point and endless ocean beyond that. The normal map type generates endless terrain.

Water scale changes how much space there is between lakes. The smaller the scale, the swampier the terrain. Higher scale leads to bigger oceans separated by bigger landmasses. Water coverage influences the overall amount of water. Reducing it generates small lakes, increasing it generates large oceans.

The settings for trees behave in the same way. Higher scale increases the distance between forests while lower scale reduces it. High tree coverage allows to completely cover the world in trees, and low coverage nearly removes them from the world.

Cliff frequency influences how many cliff lines there are in the world. Higher frequency means more cliffs, lower frequency reduces their number. The continuity setting changes how long and unbroken the cliff lines are. Low continuity leads to very short lines, high continuity to long, nearly unbroken lines of cliffs. Cliffs can be set separately for their appearances on Fulgora and Gleba .

The moisture settings control the distribution of grass versus desert. Higher bias generates more grass, lower bias generates more desert. Higher scale increases the size of the grass/desert areas, low scale leads to small grass and desert patches.

The terrain type setting controls the distribution of red desert versus sand. Higher bias generates more red desert, lower bias generates more sand. Higher scale increases the size of the red desert/sand areas, low scale leads to small red desert and sand patches.

Vulcanus volcanism determines the distribution of lava compared to the mountains and ashlands on Vulcanus. Higher scale means more lava rivers, lower scale generates more mountains instead. Higher coverage means larger lava pools, smaller coverage means more ashlands.

Gleba water control the distribution of swamps compared to the highlands on Gleba . Higher scale means more swamplands, lower scale generates more infrequent patches of highland. Higher coverage means larger bodies of deep water, lower coverage means less water and larger highlands.

Gleba plants control the distribution of Gleba's many flora. It behaves similarly to Nauvis trees.

### Enemy

Frequency determines the number of enemy bases in a given area. It does not affect enemy base size. A setting of 200% frequency that means roughly double the enemy bases can be found in a given area.

The size setting adjusts the size of enemy bases. Setting the slider to 200% means the surface area covered by the enemy bases is doubled. Bases can be changed for both Nauvis and Gleba individually.

There are two ways to disable enemies alltogether: "no enemies mode", or "peaceful mode". Selecting either will disable some achievements .

- No enemies : Nests will still spawn, but no enemies themselves will spawn from them. Pollution will still effect the nests by increasing their health. In Space Age, on Vulcanus, Demolishers will also not spawn, and thus there will be no territories. On Gleba, destroying egg rafts will no longer spawn wrigglers. Pentapod egg and biter egg will no longer spawn their creatures upon spoiling, and will instead simply disappear.
- Peaceful mode : Enemies don't begin fights, only responding if the player (or a structure) fires at them. Only the enemies located near the fired shot are aggravated and they do not call other enemies to join them. The aggravated enemies primarily attack the structures and players that initiated the aggression and also the structures that block their paths. After destroying their targets, most of the time the aggravated enemies will return to being peaceful, but some of them continue a nonstop rampage where they target nearby structures (but not faraway ones). Additionally, when a map is in peaceful mode, the enemies will not expand . In Space Age , Demolishers will not attack if you build in their territory, but will still destroy buildings if they are placed in its path.

The starting area is an almost circular radius around the spawn point that does not contain enemy bases or demolisher territory. Increasing its size pushes the bases further out, while decreasing its size generates enemy bases closer to the spawn point. The size setting does not have any other effect.

Enemy expansion can be enabled/disabled and further adjusted using the below settings.

| Enemy expansion setting | Description |
| Maximum expansion distance | The maximum distance enemies will look to expand from other enemy bases. |
| Minimum group size | The minimum size of an enemy expansion party modified by the current evolution level. |
| Maximum group size | The maximum size of an enemy expansion party modified by the current evolution level. |
| Minimum cooldown (Minutes) | The minimum time between enemy expansions being sent out. |
| Maximum cooldown (Minutes) | The maximum time between enemy expansions being sent out. |

Evolution can be enabled/disabled and further adjusted using the below settings.

| Evolution setting | Description |
| Time factor | Controls how fast evolution increases over time. |
| Destroy factor | Controls how fast evolution increases due to destroying enemy spawners. |
| Pollution factor | Controls how fast evolution increases due to producing pollution. |

### Advanced

The map width and height allow generating maps with finite resources and area. It is possible to limit generation to only one dimension, like the ribbon world . The technology price multiplier allows one to multiply the technology cost .

Pollution can be enabled/disabled and further adjusted using the below settings.

| Pollution setting | Description |
| Absorption modifier | Modifier of how much pollution is absorbed by trees and tiles. |
| Attack cost modifier | Modifier of how much pollution is absorbed by enemy attacks. |
| Minimum damage to trees | Trees have 4 different stages of the progression towards being destroyed by pollution. Any pollution above this amount starts the process of moving a tree towards a more damaged stage. |
| Absorbed per damaged tree | Trees have 4 different stages of the progression towards being destroyed by pollution. This value specifies how much pollution is absorbed when moving to a more damaged stage. |
| Diffusion ratio | The amount of pollution diffused into neighboring chunks per second. |

### Map exchange string

A map exchange string generally looks like this:

```
>>>eNp1UTGIE0EU/WMu3F4EUUjhgR4prrDZJTlFJRyZURAR0d7Oz
  WYiA5udOLsLnhaX4kptxEaraz3hOgu7wIEoKBxa2UVsLFROBC0U4
  p+dnWSNdw/+583/f97/fwbgGLhAADGgAEPqzAXSD/HI8JRZJZD9P
  leuVNyGtC0EKu1wV4qwGK3wiPfW3LYfc6NozBFKRv8qMFaOExnlE
  WDPtrZoOVGcx3igxgb0cKr8SKQ9c1eL5aOSGIcebCxlNl6H2nisD
  dkIC0YAtpIQjOWYOx7IKFEydGOeJCK61fTTO8228OMFt+416hqn9
  ivpKn475VGw1uylYSL6oeDKqXtnNc6dnL3RkyJOUsUzZccKuweW7
  ave8E5nKAeh6HYBahfQLuotCJB71e3LH+8+osTs5bGc7OWRYdtGr
  lhynR2YWrbkTEHHdP9RIKZpgi3yKodNiUlu6CQhD74+3/z1crdF/
  jz9/u5a+yYljUvVb3sr2y1MzusVDk3ck8caL+wqYDVHNE99oOTtG
  40vlJT1jap27Dy64dUSkKNHkG3eR1c7AXa0lpWpMtLN8NNu8smS9
  3R2D3yIVS2+pN0r7bKGk8lITm8wk1icZvHqChTbd6bLvbYddwqtZ
  2b4/w+KK8xElgsPX9F9OhP3uTQZAl9wd96e2DorwRT4wTu/vYd/A
  dl73Kk=<<<
```

The map exchange string can be used to share all map generation settings between different players. The player can paste the string (using CTRL + V ) into the map exchange string field and the game will set the generation settings to the settings saved in the string, resulting in a complete copy of the map when generated.

The map exchange string can be retrieved from save files by going into the load game screen, selecting the desired map, clicking the map exchange string button in the upper right corner and copying the string from the window that pops up.

For a technical description of the map exchange string, see map exchange string format .

## Mechanics

### Starting area

There is a second internal starting area that is completely separate from the starting area that can be changed in the enemy settings tab. This starting area always has a constant size and affects the spawning of resources, cliffs and water directly at the spawn. The map generation logic makes sure that there is always at least one patch of coal , iron ore , copper ore , and stone each. Furthermore, there is always a lake in the starting area, even when water is turned off, and there are never any cliffs there. Uranium ore and crude oil do not spawn in the starting area. The richness of the ore patches is slightly influenced by the frequency setting. [1]

### Chunks

A map is endless by default, though its size can be limited by height and width — see above. Because it is technically endless, the whole map is not generated from the start. Instead, a new chunk of the map is generated only when needed, similar to other procedurally generated world games.

#### Invisible chunks (fog of war)

Outside of the visible chunk area, an invisible area of about 3 chunks wide is generated as a preloading mechanism. Enemies may be located inside these invisible chunks and can attack the player from there, while artillery turrets and wagons may automatically shoot enemy bases in these chunks if they are within their automatic range. Invisible chunks are also generated if pollution is generated heavily; the game generates (invisible) chunks as it needs to spread the pollution into the area.

#### Charting (removing fog of war)

As long as a chunk is invisible, the part of the players map stays black. This changes when a chunk is charted , which means when it is "touched" by a radar. This can be either the player's internal radar, which is always available and continually charts chunks around the player, or the radar entity. If a far-away and thus ungenerated chunk is charted, it will be generated, together with the above-mentioned invisible 3 chunk radius of map around it.

#### Maximum map size and used memory

The map size is limited to 2,000 x 2,000 kilometers; internally, this is a square 2,000,000 tiles on a side, with an area of 4,000,000,000,000 (4 trillion) square tiles (assuming 1 tile = 1 meter on a side yields 2,000 x 2,000 km = 4 million square km). In real-world terms, this is between the sizes of India and Australia (or about 40% the area of the United States, or over 10 times the area of Germany). It would take around 200 game-minutes (ca 3.3 hours real time) to reach that border from the center when riding a train fueled with rocket or nuclear fuel . This makes the world essentially endless for practical purposes. The generated chunks are fully mapped and stored in the player's RAM, which is the practical limiting factor of exploration.

Because chunks are only generated in and close around the area revealed by radar, it is possible to reach that border without overloading your computer, as the size of the map in computer memory is dependent only on chunks actually generated. If only a narrow stripe of land is explored to far away, this remains manageable.

## History

- 2.0.7 : Added "No enemies" setting that disables enemy unit spawning from enemy spawners, map gen, and items. Does not disable enemy spawners. Added "Lakes" map generation preset Map generation system reworked

- 0.17.44 : The resource frequency slider in the map generator settings has a smaller influence over the amount of ore in the starting area patches.

- 0.17.0 : Resource generation changed significantly: The starting area contains only iron, copper, coal and stone, in very predictable amounts. Uranium and oil are excluded from the starting area. Resource generation settings now have a much more dramatic effect. Increased the number of steps for each setting. Ore patches are slightly less frequent but richer. There will be a more balanced amount of resources within a large enough region. Many other small tweaks. Biter generation changed significantly: Biter richness slider removed, biter placement is only configured by size and frequency settings. Biter generation settings now have a much more dramatic effect. Increased the number of steps for each setting. Biter bases will increase in size, frequency and number of worms depending on the distance from player spawn. Worm size increases depending on the distance from player spawn. Small biter bases are now closer to the player spawn. At large distances from player spawn, biter base frequency is lower than before but biter bases are larger. Other small tweaks. Terrain generation changed significantly: Water is generated as large lakes instead of swamps. Tile generation improved. Tile placement respects biomes better. More predictable cliff placement. Better controls in the map generator GUI for water, tiles and cliffs. New map terrain type selectable: Island. Launch the rocket with only a limited amount of resources available on the map.

- 0.16.0 : Added cliffs. New terrains and new terrain generation. Trees can now be configured in the generate-map GUI. Terrain can be configured in the generate map GUI. Biters scale less with distance and there are generally less biters. No uranium as a starting resource also no uranium is ever generated near the starting area, you need to go look for it.

- 0.15.0 : Extended map generator settings to include an advanced section. Added map generator presets. The map seed is used to generate unique maps instead of just shifting the starting position.

- 0.13.7 : Map size is now limited to 2000 km by 2000 km with a black bar rather than crashing when reaching this distance.

- 0.13.0 : Map generator algorithm changed, further resource field now have greater richness.
