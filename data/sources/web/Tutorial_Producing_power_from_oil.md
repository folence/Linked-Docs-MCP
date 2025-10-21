---
title: Tutorial:Producing power from oil - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Producing_power_from_oil
scraped_at: 2025-10-16 15:45:57
tags: [web, documentation]
---

# Tutorial:Producing power from oil - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Producing_power_from_oil](https://wiki.factorio.com/Tutorial:Producing_power_from_oil)


|  |
| Page "Producing power from oil" has been recommended for clean-up. Reason: The maths on this page is based on an old version of the game and is likely not correct for the current version of the game. |
| This may mean fixing grammar or broken links, providing better explanations, or removing incorrect/outdated info. |
| Further recommendations for this page's clean-up can be made at Tutorial talk:Producing power from oil . |

Oil can be converted into solid fuel (and by extension rocket fuel), which when used to produce power will result in a net profit of power at the cost of oil.

## Contents

- 1 Energy costs and modules 1.1 Light oil and petroleum gas into solid fuel 1.2 Heavy oil into light oil 1.3 Basic vs Advanced oil processing 1.4 Pumpjacks
- 2 Converting solid fuel into rocket fuel
- 3 See also

## Energy costs and modules

Power cost and power results will be worked out in reverse, with the result that gives the most power being used for each step thereafter.

#### Light oil and petroleum gas into solid fuel

Petroleum gas and light oil will be used as-is for producing solid fuel. Light oil is not cracked since it takes twice as much petroleum gas to make one solid fuel.

This table shows the results of various module combinations for a single cycle of the chemical plant for either light oil or petroleum.
Since the solid fuel is being used in a closed loop, and therefore is going into boilers, the 25MJ fuel value is halved when used.

Combinations without productivity modules are omitted, since the first combination produces more net energy per cycle than a single piece of solid fuel is worth.

Combinations for each number of productivity modules show their best combination in bold, and only that combination is used to work out energy gained per cycle.

| Modules | Energy cost | Time per cycle | Energy cost per cycle | Cost | Solid fuel per cycle | Energy gained per cycle | Result |
|  | 168kW + 7kW = 175kW | 3s / 1.0625 = 48/17s | 175kW × 48/17s = 8,400/17kJ | ~494.117kJ | 1.1 | (25MJ/2) × 1.1 - 8,400/17kJ = 225,350/17kJ | ~13,255.882kJ |
|  | 420kW + 7kW = 427kW | 3s / 1.687 = 16/9s | 427kW × 16.9s = 6,832/9kJ | ~759.111kJ |
|  | 672kW + 7kW = 679kW | 3s / 2.3125 = 48/37s | 679kW × 48/37s = 32,592/37kJ | ~880.865kJ |
|  | 693kW + 7kW = 700kW | 3s / 1.5 = 2s | 700kW × 2s = 1,400kJ | 1,400.000kJ | 1.2 | (25MJ/2) × 1.2 - 1,400kJ = 13,600kJ | 13,600.000kJ |
|  | 441kW + 7kW = 448kW | 3s / 0.875 = 24/7s | 448kW × 24/7s = 1,536kJ | 1,536kJ |
|  | 714kW + 7kW = 721kW | 3s / 0.6875 = 48/11s | 721kW × 48/11s = 34,608/11kJ | ~3,146.181kJ | 1.3 | (25MJ/2) × 1.3 - 34,608/11kJ = 144,142/11kJ | ~13,103.818kJ |

In a closed power loop, it is most efficient to convert light oil and petroleum gas into solid fuel with 2 productivity 3 modules and 1 speed 3 module.

Using beacons may further increase produced energy, even using 1 beacon for 2 chemical plants gains a little more. It is advisable to use beacons, since this process usually involves more facilities than other steps in this production chain. However, beaconed designs require more planning while placing and operating.

Main rule on using beacons is "full productivity on industry and full speed on beacons". There is some math, that proves it, see threads 1 , 2 , 3 , 4

This tables shows the results of various beacon-per-industry ratios on some reasonable layouts (12 or less chemical plants)

| Beacons per industry | Total beacons and industries count | Total modules effect | Energy cost | Time per cycle | Energy cost per cycle | Energy gained per cycle | Energy gained per cycle per 1 industry |
| 1 | 1 2 |  | 2 × (861kW + 7kW) + 480kW = 2,216kW | 3s / 1.3125 = 16/7s | 2,216kW × 16/7s = 35,456/7kJ | 2 × (25MJ/2) × 1.3 - 35,456/7kJ = 192,044/7kJ | 192,044/7kJ / 2 = 96,022/7kJ = ~13,717.429kJ |
| 1 12 | 12×(861kW + 7kW) + 480kW = 10,896kW | 10,896kW × 16/7s = 174,336/7kJ | 12 × (25MJ/2) × 1.3 - 174,336/7kJ = 1,190,664/7kJ | 1,190,664/7kJ / 12 = 99,222/7kJ = ~14,174.429kJ |
| 2 | 2 6 |  | 6 ×(1,008kW + 7kW) + 2 × 480kW = 7,050kW | 3s / 1.9375 = 48/31s | 7,050kW × 48/31s = 338,400/31kJ | 6 × (25MJ/2) × 1.3 - 338,400/31kJ = 2,684,100/31kJ | 2,684,100/31kJ / 6 = 447,350/31kJ = ~14,430.645kJ |
| 3 12 | 12 × (1,008kW + 7kW) + 3 × 480kW = 13,620kW | 13,620kW × 48/31s = 653,760/31kJ | 12 × (25MJ/2) × 1.3 - 653,760/31kJ = 5,391,240/31kJ | 5,391,240/31kJ / 12 = 449,270/31kJ = ~14,492.581kJ |
| 3 | 6 12 | 3 3 | 12 × (1155kW + 7kW) + 6 × 480kW = 16,824kW | 3s / 2.5625 = 48/41s | 16,824kW × 48/41s = 807,552/41kJ | 12 × (25MJ/2) × 1.3 - 807,552/41kJ = 7,187,448/41kJ | 7,187,448/41kJ / 12 = 598,954/41kJ = ~14,608.634kJ |
| 4 | 9 12 | 3 4 | 12 × (1,302kW + 7kW) + 9 × 480kW = 20,028kW | 3s / 3.1875 = 16/17s | 20,028kW × 16/17s = 320,448/17kJ | 12 × (25MJ/2) × 1.3 - 320,448/17kJ = 2,994,552/17kJ | 2,944,552/17kJ / 12 = 249,546/17kJ = ~14,679.176kJ |
| some theoretical upper (non-reachable) values |
| 4 | infinite row of 1 2 | 3 4 | 2 × (1,302kW + 7kW) + 480kW = 3,098kW | 3s / 3.1875 = 16/17s | 3,098kW × 16/17s = 49,568/17kJ | 2 × (25MJ/2) × 1.3 - 49,568/17kJ = 502,932/17kJ | 502,932/17kJ / 2 = 251,466/17kJ = ~14,792.118kJ |
| 8 | infinite grid of 1 1 | 3 8 | 1,890kW + 7kW + 480kW = 2,377kW | 3s / 5.6875 = 48/91s | 2,377kW × 48/91s = 114,096/91kJ | (25MJ/2) × 1.3 - 114,096/91kJ = 1,364,654/91kJ | 1,364,654/91kJ = ~14,996.198kJ |

#### Heavy oil into light oil

Based on the above tables, 1 light oil will be given an energy worth of 680kJ, since this is the optimal amount of power that can be made when converting into solid fuel in non-beaconed setup.

Combinations without productivity modules are omitted, since the first combination produces more net energy per cycle than 30 units of light oil (20,400kJ) is worth.

Since energy costs per cycle will be the same as above (same machine), only the optimal combination per number of productivity modules will be shown.

| Modules | Energy cost | Time per cycle | Energy cost per cycle | Light oil per cycle | Energy gained per cycle | Result |
|  | 168kW + 7kW = 175kW | 3s / 1.0625 = 48/17s | 175kW × 48/17s = 8,400/17kJ | 33 | 680 × 33 - 8,400/17kJ = 373,080/17kJ | ~21,945.882kJ |
|  | 693kW + 7kW = 700kW | 3s / 1.5 = 2s | 700kW × 2s = 1,400kJ | 36 | 680kJ × 36 - 1,400kJ = 23,080kJ | 23,080kJ |
|  | 714kW + 7kW = 721kW | 3s / 0.6875 = 48/11s | 721kW × 48/11s = 34,608/11kJ | 39 | 680kJ × 39 - 34,608/11kJ = 257,112/11kJ | ~23,373.818kJ |

In a closed power loop, it is most efficient to convert heavy oil into light oil with 3 productivity 3 modules.
Since optimal result includes maximum productivity modules, this conclusion still stand if you use greater value for light oil gained energy, e.g. from your favorite beaconed setup.

As for previous conversion, using beacons with speed 3 modules will further increase produced energy.

| Beacons per industry | Layout and modules | Energy cost per cycle | Energy gained per cycle | Energy gained per cycle per 1 industry |
| 1 | 1 x 2 + 2 x 3 | 35,456/7kJ | 2 × 680 × 39 - 35,456/7kJ = 335,824/7kJ | 167,912/7kJ = ~23,987.429kJ |
| 1 x 2 + 12 x 3 | 174,336/7kJ | 12 × 680 × 39 - 174,336/7kJ = 2,053,344/7kJ | 171,112/7kJ = ~24,444.571kJ |
| 2 | 2 x 2 + 6 x 3 | 338,400/31kJ | 6 × 680 × 39 - 338,400/31kJ = 4,594,320/31kJ | 765,720/31kJ = ~24,700.645kJ |
| 3 x 2 + 12 x 3 | 653,760/31kJ | 12 × 680 × 39 - 653,760/31kJ = 9,211,680/31kJ | 767,640/31kJ = ~24,762.581kJ |
| 3 | 6 x 2 + 12 x 3 | 807,552/41kJ | 12 × 680 × 39 - 807,552/41kJ = 12,240,288/41kJ | 1,020,024/41kJ = ~24,878.634kJ |
| 4 | 9 x 2 + 12 x 3 | 320,448/17kJ | 12 × 680 × 39 - 320,448/17kJ = 5,089,632/17kJ | 424,136/17kJ = ~24,949.176kJ |
| 1 x 2 + 2 x 3 (infinite row) | 49,568/17kJ | 2 × 680 × 39 - 49,568/17kJ = 852,112/17kJ | 426,056/17kJ = ~25,062.118kJ |
| 8 | 1 x 2 + 1 x 3 (infinite grid) | 114,096/91kJ | 680 × 39 - 114,096/91kJ = 2,299,224/91kJ | 2,299,224/91kJ = ~25,266.198kJ |

#### Basic vs Advanced oil processing

Crude oil can be processed with either basic or advanced oil processing. Based on the above tables, the following fuel values for each product will be used:

- Heavy oil = 32,139/55kJ (based on optimal non-beaconed conversion to light oil)
- Light oil = 680kJ
- Petroleum gas = 340kJ (half of light oil)

Since all products scale equally based on productivity, each recipe can be expressed solely as the fuel value of the products combined and that value can be scaled based on productivity below.

Basic oil processing:

- 30 Heavy oil = 192,834/11kJ
- 30 Light oil = 20,400kJ
- 40 Petroleum gas = 13,600kJ
- Total = 566,834/11kJ = ~51,530.364kJ

Advanced oil processing:

- 10 Heavy oil = 64,278/11kJ
- 45 Light oil = 30,600kJ
- 55 Petroleum gas = 18,700kJ
- Total = 606,578/11kJ = ~55,143.455kJ

Since advanced oil processing produces more overall, its total fuel value will be used.

Combinations without productivity modules are omitted, since the first combination produces more net energy per cycle than the total fuel value.

Since energy costs per cycle will be the same as above but scaled (same module slot count), only the optimal combination per number of productivity modules will be shown.

| Modules | Energy cost | Time per cycle | Energy cost per cycle | Productivity level | Energy gained per cycle | Result |
|  | 336kW + 14kW = 350kW | 5s / 0.85 = 100/17s | 350kW × 100/17s = 35,000/17kJ | 10% | 606,578/11kJ × 1.1 - 35,000/17kJ = 9,961,826/170kJ | ~58,598.976kJ |
|  | 1,386kW + 14kW = 1,400kW | 5s / 1.2 = 25/6s | 1,400kW × 25/6s = 35,000/6kJ | 20% | 606,578/11kJ × 1.2 - 35,000/6kJ = 9,955,904/165kJ | ~60,338.812kJ |
|  | 1,428kW + 14kW = 1,442kW | 5s / 0.55 = 100/11s | 1,442kW × 100/11s = 144,200/11kJ | 30% | 606,578/11kJ × 1.3 - 144,200/11kJ = 58,577.4kJ | 58,577.4kJ |

In a closed power loop, it is most efficient to convert crude oil into its products using 2 productivity 3 modules and 1 speed 3 module.

This only applies if all products are used for solid fuel production. If petroleum gas is being used for anything other than solid fuel, the optimal combination might change.

As for previous processes, beacons may be used and will further increase gained energy.

| Beacons per industry | Layout and modules | Energy cost | Time per cycle | Energy cost per cycle | Energy gained per cycle | Energy gained per cycle per 1 industry |
| 1 | 1 x 2 + 1 x 3 | 1,722kW + 14kW + 480kW = 2,216kW | 5s / 1.05 = 100/21s | 2,216kW × 100/21s = 221,600/21kJ | 606,578/11kJ × 1.3 - 221,600/21kJ = 70,609,897/1,155kJ | 70,609,897/1,155kJ = ~61,134.110kJ |
| 1 x 2 + 8 x 3 | 8 × (1,722kW + 14kW) + 480kW = 14,368kW | 14,368kW × 100/21s = 1,436,800/21kJ | 8 × 606,578/11kJ × 1.3 - 1,436,800/21kJ = 583,359,176/1,155kJ | 72,919,897/1,155kJ = ~63,134.110kJ |
| 2 | 2 x 2 + 4 x 3 | 4 × (2,016kW + 14kW) + 2 × 480kW = 9,080kW | 5s / 1.55 = 100/31s | 9,080kW × 100/31s = 908,000/31kJ | 4 × 606,578/11kJ × 1.3 - 908,000/31kJ = 438,961,868/1,705kJ | 109,740,467/1,705kJ = ~64,363.910kJ |
| 3 | 3 x 2 + 4 x 3 | 4 × (2,310kW + 14kW) + 3 × 480kW = 10,736kW | 5s / 2.05 = 100/41s | 10,736kW × 100/41s = 1,073,600/41kJ | 4 × 606,578/11kJ × 1.3 - 1,073,600/41kJ = 587,564,148/2,255kJ | 146,891,037/2,255kJ = ~65,140.149kJ |
| 4 | 5 x 2 + 4 x 3 | 4 × (2,604kW + 14kW) + 480kW = 12,872kW | 5s / 2.55 = 100/51s | 12,872kW × 100/51s = 1,287,200/51kJ | 4 × 606,578/11kJ × 1.3 - 1,287,200/51kJ = 733,526,428/2,805kJ | 183,381,607/2,805kJ = ~65,376.687kJ |
| 5 | 9 x 2 + 6 x 3 | 6 × (2,898kW + 14kW) + 9 × 480kW = 21,792kW | 5s / 3.05 = 100/61s | 21,792kW × 100/61s = 2,179,200/61kJ | 6 × 606,578/11kJ × 1.3 - 2,179,200/61kJ = 1,323,193,062/3,355kJ | 220,532,177/3,355kJ = ~65,732.393kJ |
| 2 x 2 + 2 x 3 (infinite row) | 2 × (2,898kW + 14kW) + 2 × 480kW = 6,784kW | 6,784kW × 100/61s = 678,400/61kJ | 2 × 606,578/11kJ × 1.3 - 678,400/61kJ = 443,704,354/3,355kJ | 221,852,177/3,355kJ = ~66,125.835kJ |
| 10 | 2 x 2 + 1 x 3 (infinite grid) | 4,368kW + 14kW + 2 × 480kW = 5,342kW | 5s / 5.55 = 100/111s | 5,342kW × 100/111s = 534,200/111kJ | 606,578/11kJ × 1.3 - 534,200/111kJ = 408,265,027/6,105kJ | 408,265,027/6,105kJ = ~66,873.879kJ |

#### Pumpjacks

Based on the above table, 100 crude oil will be given an energy worth of 9,955,904/165kJ, since this is the optimal amount of power that can be made when converting into solid fuel in non-beaconed setup.

Results will be given for a depleted oil well, which provides 2 crude oil per second. As the amount of crude oil increases, the importance of optimal modules decreases since the power draw for a given amount of oil output also decreases. Using the minimum amount is important to prove that creating power from crude oil is always possible.

It is also important to note that pumpjacks are affected by mining productivity level. The higher the level, the less effective productivity modules become.

Since pumpjacks operate on an infinite resource that has a finite count (oil wells), results will be shown in kW instead of kJ, since the goal here is to produce as much power as possible.

Pumpjacks only have two module slots, so all combinations will be shown. In this instance, results cannot be grouped by number of productivity modules, as the speed is also important.

| Modules | Energy cost | Time per cycle | Energy per cycle | Productivity level | Energy gained per second | Result |
|  | 18kW | 1s / 1 = 1s | 18kW × 1s = 18kJ | 0% | (9,955,904/165kJ × 1 - 18kJ) / 1s = 9,952,934/165kW | ~60,320.812kW |
|  | 108kW | 1s / 1.5 = 2/3s | 108kW × 2/3s = 72kJ | 0% | (9,955,904/165kJ × 1 - 72kJ) / 2/3s = 14,916,036/165kW | ~90,400.218kW |
|  | 216kW | 1s / 2 = 0.5s | 216kW × 0.5s = 108kJ | 0% | (9,955,904/165kJ × 1 - 108kJ) / 0.5s = 19,876,168/165kW | ~120,461.624kW |
|  | 116kW | 1s / 0.85 = 20/17s | 116kW × 20/17s = 2,320/17kJ | 10% | (9,955,904/165kJ × 1.1 - 2,320/17kJ) / 20/17s = 358,917,532/6,375kW | ~56,300.789kW |
|  | 225kW | 1s / 1.35 = 20/27s | 225kW × 20/27s = 500/3kJ | 10% | (9,955,904/165kJ × 1.1 - 500/3kJ) / 20/27s = 11,172,267/125kW | 89,378.136kW |
|  | 234kW | 1s / 0.7 = 10/7s | 234kW × 10/7s = 2,340/7kJ | 20% | (9,955,904/165kJ × 1.2 - 2,340/7kJ) / 10/7s = 69,369,578/1,375kW | ~50,450.602kW |

In a closed power loop, it is most efficient to obtain crude oil using 2 speed 3 modules. This also improves with higher levels of productivity research.

Since there are a limited number of oil wells, it is advisable to use beacons in order to increase the amount of crude oil being collected. However, due to the nature of oil wells in the world and beacons affecting multiple pumpjacks at once, there will not be a table showing this.

## Converting solid fuel into rocket fuel

Solid fuel can be converted into rocket fuel in order to increase the fuel value. Normally this would result in a loss since 10 solid fuel (250MJ) is worth more than 1 rocket fuel (225MJ), but productivity modules can be used to increase yield.

At least 2 productivity 3 modules must be used in order to increase yield, so combinations with fewer are omitted.

| Modules | Energy cost | Time per cycle | Energy cost per cycle | Cost | Rocket fuel per cycle | Energy gained per cycle | Result |
|  | 336kW + 7kW = 343kW | 30s / 0.875 = 240/7s | 343kW × 240/7s = 11,760kJ | 11,760.000kJ | 1.2 | (225MJ×1.2-250MJ)/2 - 11,760kJ = -1,760kJ | -1,760.000kJ |
|  | 588kW + 7kW = 595kW | 30s / 1.5 = 20s | 595kW × 20s = 11,900kJ | 11,900.000kJ |
|  | 840kW + 7kW = 847kW | 30s / 2.125 = 240/17s | 847kW × 240/17s = 203,280/17kJ | ~11,957.647kJ |
|  | 609kW + 7kW = 616kW | 30s / 0.6875 = 480/11s | 616kW × 480/11s = 26,880kJ | 26,880.000kJ | 1.3 | (225MJ×1.3-250MJ)/2 - 19,840kJ = 1,410kJ | ~1,410kJ |
|  | 861kW + 7kW = 868kW | 30s / 1.3125 = 160/7s | 868kW × 160/7s = 19,840kJ | 19,840kJ |
|  | 882kW + 7kW = 889kW | 30s / 0.5 = 60s | 889kW × 60s = 53,340kJ | 53,340.000kJ | 1.4 | (225MJ×1.4-250MJ)/2 - 53,340kJ = -20,840kJ | -20,840.000kJ |

In a closed power loop, it is most efficient to convert solid fuel rocket fuel with 1 speed 3 module and 3 productivity 3 modules. In fact, this is the only combination of modules that produces a net positive when accounting for boiler inefficiency.

As always, using beacons will further improve efficiency. This table shows optimal combinations for reasonable beacon setups (no more than 12 assemblers), and additionally, upper theoretical limits.

| Beacons per industry | Beacons and assemblers | Modules effect | Energy cost | Time per cycle | Energy cost per cycle | Energy gained per cycle | Energy gained per cycle per 1 industry |
| 1 | 1 + 2 | 2 3 | 2 × (1,008kW + 7kW) + 480kW = 2,510kW | 30s / 1.9375 = 480/31s | 2,510kW × 480/31s = 1,204,800/31kJ | 2 × (225MJ×1.3-250MJ)/2 - 1,204,800/31kJ = 112,700/31kJ | 56,350/31kJ = ~1,817.742kJ |
| 1 + 12 | 12 × (1,008kW + 7kW) + 480kW = 12,660kW | 12,660kW × 480/31s = 6,076,800/31kJ | 12 × (225MJ×1.3-250MJ)/2 - 6,076,800/31kJ = 1,828,200/31kJ | 152,350/31kJ = ~4,914.516kJ |
| 1 4 | 12 × (1,029kW + 7kW) + 480kW = 12,912kW | 30s / 1.125 = 80/3s | 12,912kW × 80/3s = 344,320kJ | 12 × (225MJ×1.4-250MJ)/2 - 344,320kJ = 45,680kJ | 11,420/3kJ = ~3,806.667kJ |
| 2 | 2 + 6 | 2 4 | 6 × (1,176kW + 7kW) + 2 × 480kW = 8,058kW | 30s / 1.75 = 120/7s | 8,058kW × 120/7s = 966,960/7kJ | 6 × (225MJ×1.4-250MJ)/2 - 966,960/7kJ = 398,040/7kJ | 66,340/7kJ = ~9,477.143kJ |
| 3 + 12 | 12 × (1,176kW + 7kW) + 3 × 480kW = 15,636kW | 15,636kW × 120/7s = 1,876,320/7kJ | 12 × (225MJ×1.4-250MJ)/2 - 1,876,320/7kJ = 853,680/7kJ | 71,140/7kJ = ~10,162.857kJ |
| 3 | 6 + 12 | 3 4 | 12 × (1,323kW + 7kW) + 6 × 480kW = 18,840kW | 30s / 2.375 = 240/19s | 18,840kW × 240/19s = 4,521,600/19kJ | 12 × (225MJ×1.4-250MJ)/2 - 4,521,600/19kJ = 2,888,400/19kJ | 240,700/19kJ = ~12,668.421kJ |
| 4 | 9 + 12 | 4 4 | 12 × (1,470kW + 7kW) + 9 × 480kW = 22,044kW | 30s / 3 = 10s | 22,044kW × 10s = 220,440kJ | 12 × (225MJ×1.4-250MJ)/2 - 220,440kJ = 169,560kJ | 14,130kJ |
| 1 + 2 (infinite row) | 2 × (1,470kW + 7kW) + 480kW = 3,434kW | 3,434kW × 10s = 34,340kJ | 2 × (225MJ×1.4-250MJ)/2 - 34,340kJ = 30,660kJ | 15,330kJ |
| 8 | 1 + 1 (infinite grid) | 8 4 | 2,058kW + 7kW + 480kW = 2,545kW | 30s / 5.5 = 60/11s | 2,545kW × 60/11s = 152,700/11kJ | (225MJ×1.4-250MJ)/2 - 152,700/11kJ = 204,800/11kJ | 204,800/11kJ = ~18,618.182kJ |

This is also applicable for rocket fuel production for trains, however the results are different since locomotives are 100% fuel efficient.

## See also

- Crude oil
- Solid fuel
- Rocket fuel
- Electric system
