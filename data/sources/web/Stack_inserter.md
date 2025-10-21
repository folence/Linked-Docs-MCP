---
title: Stack inserter - Factorio Wiki
source: https://wiki.factorio.com/Stack_inserter
scraped_at: 2025-10-21 14:30:24
tags: [web, documentation]
---

# Stack inserter - Factorio Wiki

**Source:** [https://wiki.factorio.com/Stack_inserter](https://wiki.factorio.com/Stack_inserter)


|  | Stack inserter | Edit |

| Recipe |
| 0.5 + 1 + 2 + 10 + 1 → 1 |
| Total raw |
| 44.5 + 2 + 32 + 55 + 2.5 + 2 + 1 |
| Map color |  |
| Health | 160 208 256 304 400 |  |  | 160 |  | 208 |  | 256 |  | 304 |  | 400 |
|  |  | 160 |
|  | 208 |  | 256 |
|  | 304 |  | 400 |
| Resistances | Fire: 0/90% |
| Stack size | 50 |
| Rocket capacity | 50 |
| Dimensions | 1×1 |
| Energy consumption | 337 438 539 639 841 kW ( electric ) |  |  | 337 |  | 438 |  | 539 |  | 639 |  | 841 |
|  |  | 337 |
|  | 438 |  | 539 |
|  | 639 |  | 841 |
| Drain | 1 kW ( electric ) |
| Rotation speed | 864°/s 1123°/s 1382°/s 1642°/s 2160°/s |  |  | 864°/s |  | 1123°/s |  | 1382°/s |  | 1642°/s |  | 2160°/s |
|  |  | 864°/s |
|  | 1123°/s |  | 1382°/s |
|  | 1642°/s |  | 2160°/s |
| Mining time | 0.1 |
| Prototype type | inserter |
| Internal name | stack-inserter |
| Required technologies |
|  |
| Boosting technologies |
|  |
| Produced by |
|  |

Space Age expansion exclusive feature.

This article is about the new inserter introduced in Space Age . For the base game inserter with large transfer abilities, see bulk inserter .

The stack inserter is an electric inserter that can move multiple items at the same time and build stacks on belts . It has a larger maximum hand size than the bulk inserter while turning at the same rate, giving it a 33% higher throughput.

Unlike other inserters, it will not insert into its target until it has collected a full hand size of items. While usually beneficial, this can be a problem if more materials from the source are not forthcoming. In particular, holding onto spoilable items can lead to reduced freshness or even completely spoiling into a less useful item.

This particular feature of the stack inserter means that it is not a complete upgrade to the bulk inserter ; there will be cases where the latter is more appropriate.

To avoid getting stuck, if the item it is holding while waiting for more items spoils into a different item, then it will turn immediately to discard its hand. Similarly, if the inserter is given a filter, and that filter changes to no longer include the item in its hand, the stack inserter will immediately turn and discard its hand. This latter feature can make it easy to force the inserter to become unstuck .

## Contents

- 1 Belt stacking
- 2 Stack size
- 3 Tips
- 4 Trivia
- 5 History
- 6 See also

## Belt stacking

When a stack inserter inserts items onto a belt, it will stack them to the maximum belt stack size currently researched. The Stack inserter research increases the maximum belt stack to 2, with two further researches increasing it to 4.

The stack inserter will attempt to always build stacks of the maximum size currently researched. This has particular interactions with the inserter's hand size. When inserting onto a belt (and only when doing so), the hand size is always rounded down to the next multiple of the current maximum belt stack size. This means that it will almost always build full stacks even if this moves fewer items than the hand size says it should.

There are several cases where the stack inserter will not build full stacks on belts. First, if the hand size is less than the current maximum belt stack size (so rounding down would result in a hand size of 0), then the stack inserter will respect the exact hand size and build partial stacks.

Second, as previously indicated, if the stack inserter is holding a spoilable item, and that item spoils, then the stack inserter will insert that item into its destination immediately, building whatever stacks it can when inserting onto a belt. This also applies to changing the filter of the stack inserter.

There is a very rare third case: if the research for maximum belt stacks changes while the inserter is moving to insert onto a belt, then it will build whatever stacks it can onto that belt using the new belt stack limit.

When inserting into containers or machines, the hand size will be exactly respected.

## Stack size

The stack size for stack inserters is increased by the Inserter capacity bonus (research) technology (though you will likely have already researched most if not all of these upgrades before researching stack inserters). The stack size can be overridden to set how many items it picks up at one time, with the maximum being the highest research level currently unlocked.

| Inserter capacity bonus | Stack size bonus | Total stack size |
| none | 0 | 6 |
| 1 | +1 | 7 |
| 2 | +1 | 8 |
| 3 | +1 | 9 |
| 4 | +1 | 10 |
| 5 | +2 | 12 |
| 6 | +2 | 14 |
| 7 | +2 | 16 |

## Tips

The stack inserter usually does not turn until it has its full hand size. While this is often desireable, there are circumstances where this behavior can pose a problem. There are ways to force a stack inserter to discard its current hand contents.

The primary tool for doing this is to control the stack inserter's filtered item list. If the filters change such that the item in the inserter's hand is no longer on the list of valid filtered items, then the inserter will immediately turn to drop its hand regardless of how much is there.

When inserting from a container into something else (a belt, machine, etc), one can employ the circuit network . If you wire the stack inserter to that container, and set the stack inserter to filter items based on the circuit network, then everything automatically works. If the stack inserter's hand is not full, that can only be because the container ran out of items of that type. Which means that the container will no longer broadcast a positive signal of that item's type. And that means the stack inserter's filters will not be filtered on the item in the stack inserter's hand. And therefore, it will immediately turn to drop the items.

This can also work on various crafting machines, as they can be set to broadcast their contents. Their contents do include their input slots, but this is safe as output inserters cannot output items in the input slots of a machine.

However, because broadcasting contents does include the items in those input slots as filters, if the recipe requires more than 5 total inputs and outputs, this mechanism may not work. Inserter filters can only filter on 5 items at once, so if there are more than 5 items to be filtered, then the system will pick 5 of them arbitrarily. And if there are 5 inputs, the filtered set may never include any of the outputs.

Note that for machines dealing with spoilable items , the 5 item limit also includes any possible spoil products.

This mechanism can be adapted to handle recipes with larger numbers of inputs by using combinator machinery to filter out any signals that are not the desired outputs.

Stack inserters that insert from a belt can also do this. The belt they are inserting from can be wired to the stack inserter and told to read that belt tile's contents. However, this will prevent the inserter from waiting for more items, so it can lead to more insertions than is strictly needed.

## Trivia

- When first mentioned in FFF #393 , the stack inserter was instead called the "bulk inserter". However, in response to feedback from the audience, the developers announced in the following FFF that its name would be swapped with that of what was previously known as a "stack inserter" , as this naming was deemed more appropriate.

## History

- 2.0.18 : Bulk inserter no longer can be upgraded to a stack inserter.

- 2.0.7 : Introduced in Space Age expansion.

## See also

- Bulk inserter
- Electric system
- Inserters

| Logistics |
| Storage | Wooden chest Iron chest Steel chest Storage tank |
| Belt transport system | Transport belt Fast transport belt Express transport belt Turbo transport belt ( ) Underground belt Fast underground belt Express underground belt Turbo underground belt ( ) Splitter Fast splitter Express splitter Turbo splitter ( ) |
| Inserters | Burner inserter Inserter Long-handed inserter Fast inserter Bulk inserter Stack inserter ( ) |
| Electric system & Fluid system | Small electric pole Medium electric pole Big electric pole Substation Pipe Pipe to ground Pump |
| Railway | Rail Rail ramp ( ) Rail support ( ) Train stop Rail signal Rail chain signal Locomotive Cargo wagon Fluid wagon Artillery wagon |
| Transport | Car Tank Spidertron Spidertron remote |
| Logistic network | Logistic robot Construction robot Active provider chest Passive provider chest Storage chest Buffer chest Requester chest Roboport |
| Circuit network | Lamp Red wire Green wire Arithmetic combinator Decider combinator Selector combinator Constant combinator Power switch Programmable speaker Display panel |
| Terrain | Stone brick Concrete Hazard concrete Refined concrete Refined hazard concrete Landfill Artificial yumako soil ( ) Overgrowth yumako soil ( ) Artificial jellynut soil ( ) Overgrowth jellynut soil ( ) Ice platform ( ) Foundation ( ) Cliff explosives |
| Navigation | Production Intermediate products Space ( ) Combat Technology Environment |
