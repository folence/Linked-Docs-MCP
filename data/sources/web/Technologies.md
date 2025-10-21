---
title: Technologies - Factorio Wiki
source: https://wiki.factorio.com/Technologies
scraped_at: 2025-10-21 14:29:32
tags: [web, documentation]
---

# Technologies - Factorio Wiki

**Source:** [https://wiki.factorio.com/Technologies](https://wiki.factorio.com/Technologies)

Technologies are series of research projects that provide various enhancements. Some technologies unlock new items or recipes, while others provide bonuses.

Most technologies can be researched in labs by consuming science packs of various types. For example, the Logistics technology can be unlocked by placing 20 automation science packs into labs while the technology is selected for research. Some technologies will automatically unlock after meeting specific conditions, without consumption of any science packs.

## Contents

- 1 Infinite technologies 1.1 Pricing formulas 1.1.1 Space Age 1.2 Cumulative cost 1.3 Infinite productivity research limits
- 2 Trigger technologies 2.1 Nauvis 2.2 Space 2.3 Fulgora 2.4 Gleba 2.5 Vulcanus 2.6 Aquilo
- 3 Achievements
- 4 History
- 5 See also

## Infinite technologies

While most technologies in Factorio are either one-off or have a finite, relatively small number of levels available, a few are "infinite", meaning the player can research as many levels as they can afford. All of them unlock bonuses to existing technologies, never new structures or abilities. The per-level bonuses are constant for a particular infinite technologies and, like finite research bonuses, are additive within a single technology. They are subject to diminishing returns; thus, the per-level and per-science pack contributions from very high levels of infinite technologies will eventually provide only marginal improvements.

All base game infinite technologies levels require space science packs , and are also the only technologies that do. As such, they are late-game technologies intended primarily for players who wish to continue playing and expand their factory past the nominal victory condition of launching a rocket.

Infinite technologies are identified in-game by a small ∞ infinity symbol shown in the top right corner of the research technology's card in the research screen.

Most infinite technologies are continuations of ordinary multi-level technologies; the "infinite" mechanic becomes effective once the player reaches the card initially labeled with N - ∞ in the research tree.  In the base game, only the two artillery -related technologies (artillery shell range and shooting speed ) are infinite-only; for these, 1 - ∞ is shown before any levels in them are researched. In either case, once the first infinite level is researched, the card label switches to the one discussed above.

### Pricing formulas

The price of all infinite technologies is generated in a mathematical progression ; for the majority of technologies, the progression is geometric , mostly in powers of 2. Two technologies - mining productivity and follower robot count - use an arithmetic progression instead.

The table below summarizes for all infinite researches their first infinite level, the cost of the first few infinite levels, the cost formula and the per-level bonus.

We denote by N the current level of the research, by F the final non-infinite level of the research (hence F+1 is the first "infinite" level) and by P[N] the price of the research at level N .

| Technology | Category | Bonus | Science Packs | F+1 | P[N] | P[F+1] | P[F+2] | P[F+3] | P[F+4] | P[F+5] | ... |
| Mining productivity | Productivity | +10% Mining productivity |  | 4 | 2,500 × (N - F) | 2,500 | 5,000 | 7,500 | 10,000 | 12,500 | +2500 |
| Physical projectile damage | Weapon Damage | +40% Bullet damage +70% Gun turret damage +40% Shotgun shell damage +100% Cannon shell damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | 2,000 | 4,000 | 8,000 | 16,000 | ×2 |
| Stronger explosives | +50% Rocket damage +20% Grenade damage +20% Land mine damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | 2,000 | 4,000 | 8,000 | 16,000 | ×2 |
| Refined flammables | +20% Fire damage +20% Flamethrower turret damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | 2,000 | 4,000 | 8,000 | 16,000 | ×2 |
| Energy weapons damage | +70% Laser damage +70% Electric damage +30% Beam damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | 2,000 | 4,000 | 8,000 | 16,000 | ×2 |
| Artillery shell range | Non-Damage Weapon Bonus | +30% Artillery shell range |  | 1 | 1,000 × 2^N | 2,000 | 4,000 | 8,000 | 16,000 | 32,000 | ×2 |
| Artillery shell shooting speed | +100% Artillery shell shooting speed |  | 1 | 1,000 + 1,000 × 3^(N - 1) | 2,000 | 4,000 | 10,000 | 28,000 | 82,000 | ×3 then - 2,000 |
| Follower robot count | +25 Maximum following robots |  | 5 | 1,000 × (N - F) | 1,000 | 2,000 | 3,000 | 4,000 | 5,000 | +1,000 |
| Worker robot speed | Other | +65% Worker robot speed |  | 6 | 1,000 × 2^(N - F - 1) | 1,000 | 2,000 | 4,000 | 8,000 | 16,000 | ×2 |

#### Space Age

The table below summarizes all the infinite technologies in Space Age. Some are unique to Space Age, while some have their price and/or effect changed from the base game.

Due to the introduction of tesla weapons , the energy weapons damage technology is split into laser weapons damage and electric weapons damage .

| Technology | Category | Bonus | Science Packs | F+1 | P[N] | P[F+1] | ... |
| Mining productivity | Productivity | +10% Mining productivity |  | 3 | 1,000 × (N - F) | 1,000 | +1,000 |
| Research productivity | +10% Lab research productivity |  | 1 | 1,000 × 1.2^N | 1,200 | ×1.2 |
| Steel plate productivity | Recipe Productivity (no effect beyond level 30) | +10% Steel plate productivity +10% Casting steel productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Low density structure productivity | +10% Low density structure productivity +10% Casting low density structure productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Scrap recycling productivity | +10% Scrap recycling productivity |  | 1 | 500 × 1.5^N | 750 | ×1.5 |
| Processing unit productivity | +10% Processing unit productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Plastic bar productivity | +10% Plastic bar productivity +10% Bioplastic productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Rocket fuel productivity | +10% Rocket fuel productivity +10% Rocket fuel from jelly productivity +10% Ammonia rocket fuel productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Asteroid productivity | +10% Carbonic asteroid crushing productivity +10% Oxide asteroid crushing productivity +10% Metallic asteroid crushing productivity +10% Advanced carbonic asteroid productivity +10% Advanced oxide asteroid crushing productivity +10% Advanced metallic asteroid crushing productivity |  | 1 | 1,000 × 1.5^N | 1,500 | ×1.5 |
| Rocket part productivity | +10% Rocket part productivity |  | 1 | 2,000 × 1.5^N | 3,000 | ×1.5 |
| Physical projectile damage | Weapon Damage | +20% Bullet damage +20% Gun turret damage +40% Shotgun shell damage +100% Cannon shell damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | ×2 |
| Laser weapons damage | +70% Laser damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | ×2 |
| Artillery shell damage | +10% Artillery shell damage |  | 1 | 1,000 × 2^(N - 1) | 1,000 | ×2 |
| Stronger explosives | +50% Rocket damage +20% Grenade damage +20% Land mine damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | ×2 |
| Refined flammables | +20% Fire damage +20% Flamethrower turret damage |  | 7 | 1,000 × 2^(N - F - 1) | 1,000 | ×2 |
| Electric weapons damage | +70% Tesla damage +70% Electric damage +30% Beam damage |  | 4 | 1,000 × 2^(N - F) | 2,000 | ×2 |
| Railgun damage | +40% Railgun damage |  | 1 | 1,000 × 2^(N - 1) | 1,000 | ×2 |
| Artillery shell range | Non-Damage Weapon Bonus | +30% Artillery shell range |  | 1 | 1,000 × 2^(N - 1) | 1,000 | ×2 |
| Artillery shell shooting speed | +100% Artillery shell shooting speed |  | 1 | 1,000 × 2^(N - 1) | 1,000 | ×2 |
| Railgun shooting speed | +15% Railgun shooting speed |  | 1 | 1,000 × 2^(N - 1) | 1,000 | ×2 |
| Follower robot count | +25 Maximum following robots |  | 5 | 1,000 × (N - F) | 1,000 | +1,000 |
| Worker robot speed | Other | +65% Worker robot speed |  | 7 | 1,000 × 2^(N - F) | 2,000 | ×2 |
| Health | +50 Character health |  | 1 | 50 × 2^N | 100 | ×2 |

### Cumulative cost

As the price of most infinite technologies (specifically, those based on geometric progressions) increases very steeply, it may be a good idea for players to set realistic target levels for each of the infinite technologies they wish to pursue, and make their factory plans accordingly. To that end, the following properties of cumulative infinite research prices may be useful:

- For infinite technologies whose underlying equation is a powers-of-two geometric series, the cumulative price of the first N - F infinite levels (skipping the first F level, so counting "infinite" levels only) is 2 × P[N] - P[F+1] ; i.e., twice the price of the final researched level, less the price of the first "infinite" level. As N increases, this is approximated well by 2 × P[N] = P[N+1] , so the cumulative cost of researching to level N is about as much as researching level N+1 . If one decides a level M which one considers the "highest feasible" with their current science pack production capacity, expanding said capacity by a factor of X will allow about log[2](X) additional levels to be researched before the next level takes longer to research with the expanded capacity than level M + 1 would have taken with the pre-expansion production capacity. For example, if one expands production capacity by a factor of 10, they will be able to research at least floor(log[2](10)) = 3 and at most ceiling(log[2](10)) = 4 additional levels in a given technology before the exponential increase in price negates the speed benefits of their ×10 capacity expansion.
- The cumulative price of the first N - F levels of infinite technologies whose underlying equation is an arithmetic series is (N - F) × (P[N] + P[F + 1]) ÷ 2 ; i.e, N - F times the mean of the prices of the first and last "infinite" level. For the Follower robot count (research) , an additional 900 × (N-F) need to be added. Expanding production capacity by a factor of X , as above, will in this case allow an additional N × (X - 1) levels to be researched before the benefit of the expansion is wiped out (i.e., research progress speed drops to or below what it was pre-expansion).
- The cumulative price of the first N levels of artillery shell shooting speed , the sole infinite technology whose underlying equation is a powers-of-three geometric series (equation type (2)) is 1.5 × P[N] - 0.5 × P[1] ; i.e., 1.5 times the price of the final researched level, less half the price of the first level.

Note that these prices reflect research units , which will not be equal to science packs if productivity modules are used in labs. (In that case, the science pack requirement will be lower.)

### Infinite productivity research limits

All recipes have a maximum productivity of 300%. This was primarily done to prevent infinite resource exploits involving the recycler and its 25% return of input items. This cap puts a hard limit on the effectiveness of most infinite productivity researches. It can be researched past level 30, but it will have no practical effect.

Note that miners are not crafting machines that execute recipes, nor are labs. As such, mining productivity (research) and research productivity (research) have no limit.

The railgun turret's shooting speed is limited by its animation , which means it can't shoot faster than 0.845 times per second (once per 71 ticks ). This shooting speed is reached at level 10 and researching past that level will have no practical effect on the railgun turret, however it will continue to increase the shooting speed of the hand-held railgun .

## Trigger technologies

The technologies listed below are researched by the player performing certain actions (usually mining or crafting a specific item) instead of by using science packs in labs.

### Nauvis

| Technology | Research trigger |
| Automation science pack | Craft a lab |
| Steam power | Craft 50 iron plate |
| Electronics | Craft 10 copper plate |
| Steel axe | Craft 50 steel plate |
| Oil processing | Mine crude oil |
| Uranium processing | Mine uranium ore |
| Biter egg handling | Capture a biter/spitter spawner |

### Space

| Technology | Research trigger |
| Space platform | Launch a space platform starter pack |
| Space science pack | Craft an asteroid collector |

### Fulgora

| Technology | Research trigger |
| Recycling | Mine Fulgoran vault ruin |
| Holmium processing | Craft holmium ore |
| Electromagnetic plant | Craft 50 holmium plate |
| Electromagnetic science pack | Craft supercapacitor |

### Gleba

| Technology | Research trigger |
| Jellynut | Mine jellystem |
| Yumako | Mine yumako tree |
| Heating tower | Mine copper stromatolite |
| Agriculture | Mine iron stromatolite |
| Biochamber | Craft 10 nutrients |
| Artificial soil | Craft 500 nutrients |
| Bioflux | Craft biochamber |
| Bacteria cultivation | Craft bioflux |
| Bioflux processing | Craft 25 bioflux |
| Agricultural science pack | Craft 100 bioflux |

### Vulcanus

| Technology | Research trigger |
| Tungsten carbide | Mine big volcanic rock |
| Calcite processing | Mine calcite |
| Foundry | Craft tungsten carbide |
| Big mining drill | Craft a foundry |
| Tungsten steel | Craft a big mining drill |
| Metallurgic science pack | Craft tungsten plate |

### Aquilo

| Technology | Research trigger |
| Lithium processing | Mine big lithium ice formation |
| Cryogenic plant | Craft lithium plate |
| Cryogenic science pack | Craft cryogenic plant |

## Achievements

|  | Tech maniac Research all technologies . |

- Completing infinite technologies of any level is not required for Tech maniac . All non-infinite levels of technologies that have infinite continuations are still required.

## History

- 2.0.7 : Introduced trigger technologies ( https://www.factorio.com/blog/post/fff-376 )

## See also

- Research
- Science pack

| Technologies |
| Machines | Advanced circuit (research) Processing unit (research) Automation (research) 2 3 Bulk inserter (research) Electric energy accumulators (research) Electric energy distribution 1 (research) 2 Fast inserter (research) Fluid handling (research) Logistics (research) 2 3 Nuclear power (research) Oil processing (research) Rocket silo (research) Solar energy (research) Stack inserter (research) ( ) |
| Military/Weaponry | Atomic bomb (research) Defender (research) Distractor (research) Destroyer (research) Flamethrower (research) Military (research) 2 3 4 Rocketry (research) explosive Uranium ammo (research) |
| Bonuses | Artillery shell range (research) Artillery shell shooting speed (research) Asteroid productivity (research) ( ) Braking force (research) Energy weapons damage (research) Follower robot count (research) Inserter capacity bonus (research) Lab research speed (research) Laser shooting speed (research) Low density structure productivity (research) ( ) Mining productivity (research) Physical projectile damage (research) Plastic bar productivity (research) ( ) Processing unit productivity (research) ( ) Refined flammables (research) Research productivity (research) ( ) Rocket fuel productivity (research) ( ) Rocket part productivity (research) ( ) Scrap recycling productivity (research) ( ) Steel plate productivity (research) ( ) Stronger explosives (research) Weapon shooting speed (research) Worker robot cargo size (research) Worker robot speed (research) |
| Player augmentation | Construction robotics (research) Logistic robotics (research) Steel axe (research) Toolbelt (research) |
| Defense | Heavy armor (research) Modular armor (research) Power armor (research) MK2 Mech armor (research) ( ) Gate (research) Land mines (research) Stone wall (research) Gun turret (research) Laser turret (research) Artillery (research) |
| Crafting | Advanced material processing (research) 2 Advanced oil processing (research) Automation science pack (research) Battery (research) Biter egg handling (research) ( ) Calcite processing (research) ( ) Circuit network (research) Chemical science pack (research) Cliff explosives (research) Coal liquefaction (research) Concrete (research) Electronics (research) Engine (research) Electric engine (research) Explosives (research) Flammables (research) Foundation (research) ( ) Kovarex enrichment process (research) Landfill (research) Laser (research) Logistic science pack (research) Logistic system (research) Low density structure (research) Lubricant (research) Military science pack (research) Nuclear fuel reprocessing (research) Lamp (research) Overgrowth soil (research) ( ) Plastics (research) Production science pack (research) Robotics (research) Rocket fuel (research) Space science pack (research) Steel processing (research) Sulfur processing (research) Uranium processing (research) Utility science pack (research) |
| Transportation | Automated rail transportation (research) Automobilism (research) Elevated rail (research) ( ) Fluid wagon (research) Rail support foundations (research) ( ) Railway (research) Tank (research) Spidertron (research) |
| Equipment modules | Belt immunity equipment (research) Discharge defense (research) Energy shield equipment (research) MK2 Exoskeleton equipment (research) Nightvision equipment (research) Personal battery (research) MK2 MK3 ( ) Personal laser defense (research) Personal roboport (research) MK2 Portable fission reactor (research) Portable fusion reactor (research) ( ) Portable solar panel (research) |
| Modules | Modules (research) Effect transmission (research) Efficiency module (research) 2 3 Productivity module (research) 2 3 Speed module (research) 2 3 Quality module (research) ( ) 2 ( ) 3 ( ) |
| Navigation | Logistics Production Intermediate products Space ( ) Combat Environment |
