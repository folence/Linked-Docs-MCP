---
title: Mining - Factorio Wiki
source: https://wiki.factorio.com/Mining
scraped_at: 2025-10-21 14:29:47
tags: [web, documentation]
---

# Mining - Factorio Wiki

**Source:** [https://wiki.factorio.com/Mining](https://wiki.factorio.com/Mining)

Mining is used to extract resources from the world. Mining drills are the first step to automating manufacture, although most resources have to be smelted in a furnace for further usage.

## Contents

- 1 Mining speed formula 1.1 Mining by hand 1.2 Infinite resources
- 2 Drill types
- 3 Output 3.1 Productivity and resource drain
- 4 Resource output
- 5 Achievements

## Mining speed formula

Mining drills have a "mining speed" factor which determines how quickly they produce resources. Resource patches have a "mining time" stat which represents the "hardness" of the resource to mine. Higher mining time means slower mining.

The rate at which resources are produced is given by:

```
Mining speed / Mining time = Production rate (in resource/sec)
```

To calculate the time needed for one resource-item use this formula:

```
Mining time / Mining speed = Seconds for one resource item
```

Mining speed is a function of the miner while mining time is a function of the resource you are currently mining (you can place a miner over a mixed field).

### Mining by hand

When mining by hand, the formula is modified slightly:

```
(1 + Mining Speed Modifier) * .5 / Mining time = Production rate (in resource/sec)
```

Expanded description:

```
(1 + Force Modifier) * (1 + Character Modifier) * (Character mining speed) / Mining time = Rate
```

### Infinite resources

The output of the unmodified resource is the percentage yield of the tile currently used by the miner.

```
Output of unmodified field * ( Number of modules in miner * Bonus from module ) + Output of unmodified field * ( Number of beacons * ( Number of modules * Distribution efficiency ) * Bonus from module + Productivity research bonus + 1 ) = Raw output per second
```

```
(Raw output per second * Mining speed) / Mining time = Production rate (in resource/sec)
```

The mining drill or pumpjack will sum the production rate of all tiles below it and show that value in the tooltip.

## Drill types

| Item | Total raw | Mining speed | Mining power | Covered area | Max health | Pollution |
| Player | - | 0.5 | - | 1 × 1 | 250 | - |
| Burner mining drill | 9 5 | 0.25 | 150 kW ( burner ) | 2 × 2 | 150 | 12/m |
| Electric mining drill | 23 4.5 | 0.5 | 90 kW ( electric ) | 5 × 5 | 300 | 10/m |
| Big mining drill | 200 43 54.5 20 10 20 | 2.5 | 300kW ( electric ) | 13 × 13 | 300 | 40/m |

Note that the Burner mining drill's size matches its coverage (both being 2x2), the Electric mining drill's size is one tile bigger in either direction while covering two tiles more (3x3 size, 5x5 coverage) and the big mining drill is a further two tiles bigger in either direction, while also increasing coverage by eight tiles (5x5 size, 13x13 coverage).

Mining drills can only be placed if its mining area would touch a mineable resource. When all resources in its mining area are exhausted, the drill will shutdown and an icon will appear on it.

## Output

| Resource | Burner mining drill | Electric mining drill | Big mining drill |
| Speed : 0.25 | Speed : 0.5 | Speed : 2.5 |
| Scrap | Time: 0.5 | 0.5/s | 1/s | 5/s |
| Iron | Time: 1 | 0.25/s | 0.5/s | 2.5/s |
| Copper | Time: 1 | 0.25/s | 0.5/s | 2.5/s |
| Coal | Time: 1 | 0.25/s | 0.5/s | 2.5/s |
| Stone | Time: 1 | 0.25/s | 0.5/s | 2.5/s |
| Calcite | Time: 1 | 0.25/s | 0.5/s | 2.5/s |
| Uranium | Time: 2 | N/A | 0.25/s | 1.25/s |
| Tungsten | Time: 5 | N/A | N/A | 0.5/s |

### Productivity and resource drain

Mining productivity is a technology that increases the productivity of all mining drills, which adds to any bonus from productivity modules . Productivity for miners works similarly to productivity for assemblers: extra ore products for every "real" ore mined from the patch. However, since mining productivity research does not slow the mining drill down (unlike productivity modules), mining productivity effectively makes the drill faster. Furthermore, because more ore is output than is removed from the patch, mining productivity extends the amount of ore generated from a patch.

Mining drills have a property called resource drain. When the drill generates a non-productivity ore, it subtracts one ore from the patch. Resource drain is the probability that this subtraction actually takes place. 100% resource drain means that the subtraction always happens; 50% resource drain means that the resource is only drained from the patch 50% of the time. This means that, with 50% resource drain, the patch will last twice as long.

Unlike mining productivity, low resource drain does not generate more ore in the same period of time; it merely extends the life span of the resource patch. As these are two independent factors, they multiply into each other. A +100% productivity bonus combined with 50% resource drain means that a 1M ore patch will generate 4M ore. It will generate that 4M ore twice as fast as it would with no productivity, and the patch will last twice as long as with 100% resource drain (assuming ore is consumed as quickly as it is produced).

Burner and electric drills have 100% drain, while big mining drills have 50%. Quality lowers the resource drain by 1/6th of the base-quality drain per quality level, with legendary providing a double-bonus.

## Resource output

Unlike most other equipment, mining drills will output resources directly without the need of inserters . This includes transport belts , chests , other mining drills, furnaces , assembling machines , etc.

- Burner drill to chest
- Burner drill to furnace
- Burner drill to burner drill

## Achievements

|  | Mining with determination Completely deplete a resource patch. |
