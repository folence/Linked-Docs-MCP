---
title: Damage - Factorio Wiki
source: https://wiki.factorio.com/Damage
scraped_at: 2025-10-21 14:29:46
tags: [web, documentation]
---

# Damage - Factorio Wiki

**Source:** [https://wiki.factorio.com/Damage](https://wiki.factorio.com/Damage)

Taking damage is the effect of lowering the health of the player , enemies , asteroids or other entities.

## Contents

- 1 Overview
- 2 Damage types 2.1 Piercing power
- 3 Resistance 3.1 Decrease, or "flat" resistance 3.2 Percentage resistance
- 4 Combined formulas 4.1 If R+1<D 4.2 otherwise if D>1 4.3 otherwise
- 5 Achievements

## Overview

In Factorio, entities have health, can die/be destroyed, and have resistances. Damage is defined as the concept of lowering an entity's health by using an attack, such as a gun firing at it, or a biter chewing on it. An entity's resistances will define exactly how much damage the entity will take off of an arbitrary attack.

The player's maximum health is 250 (without energy shields ), and this value can be increased through the Health technology. Other entities' health values are listed in their individual entries.

## Damage types

| Damage type | Used by |
| Physical | Bullets, shotgun shells, railgun ammo , defender capsule Biters and wriggler pentapods |
| Physical and explosion | Cannon shells, artillery shell |
| Impact | Collision (of train / car / tank ) |
| Fire | Flamethrower ammo , flamethrower turret |
| Acid | Spitters , worms , and stomper pentapods |
| Poison | Poison capsule Wriggler pentapods |
| Explosion | Rockets, grenades, land mine Strafer pentapods |
| Laser | Laser turret , distractor capsule , personal laser defense |
| Electric | Discharge defense , destroyer capsule , tesla ammo , tesla turret |

### Piercing power

Piercing power is present with tank ammunition. It determines how much HP of enemies can a projectile damage before it is no longer able to travel further. To penetrate an enemy, the enemy has to be killed by the projectile, and the damage dealt for the kill must be less than current piercing power. [1] The damage dealt also decreases piercing power. For example, shooting medium biters with 75 health with a cannon shell of 300 piercing power means that the shell will pierce through 4 medium biters, killing them, and still destroy/damage one more target.

## Resistance

Resistances to specific damage types can be written in two ways:

- A percentage, such as: "Physical: 10%". The incoming damage of this type is simply reduced by this percentage.
- A flat decrease, followed by the percentage, such as: "Physical: 25/10%". This means that incoming damage is reduced by 25 points first, before reducing it by 10%.

Shooting at an object with a physical resistance of "25/10%" has nearly no effect when the bullets inflict less than 25 damage points each. If each bullet does 45 damage points, then the resistance of 25 is subtracted first, and the remaining 20 damage points are reduced by 10%, resulting in 18 damage points being imparted on the target object.

The following two subsections explain the two resistance calculations in detail.

### Decrease, or "flat" resistance

Decrease resistance decreases the damage by specified number as long as the resulting damage wouldn't be less than 1. If the result damage would be less than 1, an alternate formula is used.
Let R denote the flat resistance value, D the incoming damage, and M the modified damage (that is, the damage after accounting for flat resistance). Then

if R+1<D

M=D-R

otherwise if D>1

M=1/(R-D+2)

otherwise

M=1/(R+1) .

If flat resistance matches or exceeds the raw damage, then modified damage is asymptotic towards 0, as shown by following example table:

| Damage | Flat Resistance | Modified damage (with 0% resistance) |
| 5 | 0 | 5 |
| 5 | 1 | 4 |
| 5 | 2 | 3 |
| 5 | 3 | 2 |
| 5 | 4 | 1 |
| 5 | 5 | 1/2 |
| 5 | 6 | 1/3 |
| 5 | 7 | 1/4 |
| 5 | 8 | 1/5 |
| ... | ... | ... |

### Percentage resistance

Percentage resistance reduces the damage by the specified percent. It is applied after flat/decrease resistances (if both are present) and thus changes the 'modified damage' value above, decreasing it by the specified percentage. If the value is 100%, the entity is immune to the damage. This is the only way to have an entity immune to a type of damage, as flat reduction cannot reduce damage to less than 1.

As an example, an entity with 25% resistance to physical damage hit with a bullet dealing 100 physical damage would take 75 damage instead of 100.

The formula used for percentage resistance to damage is as follows:

Let M denote the flat-resistance-modified starter damage, and let P denote the percentage resistance (in decimal form, so 25%=0.25), and let F denote final damage.

F = M * (1 - P)

## Combined formulas

Let D denote the raw incoming damage (of applicable type), R denoted the flat resistance value (against damage of the applicable type), P the percentage resistance (against damage of the same type) in decimal form (e.g. 20%=0.2), and let F denote the final damage (of applicable type) dealt to the target.

### If R+1<D

F = (D - R) * (1 - P)

### otherwise if D>1

F = (1 - P) / (R-D+2)

### otherwise

F = (1 - P) / (R+1)

## Achievements

The concept of damage is directly connected to the following achievements:

|  | Run Forrest, run Destroy 100 trees by impact. |

|  | Pyromaniac Destroy 10k trees with fire. |

|  | Steamrolled Destroy 10 spawners by impact. |

|  | Golem Survive a hit of 500 damage or more. |

|  | Watch your step Get killed by a moving locomotive . |
