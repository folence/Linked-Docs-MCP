---
title: Balancer mechanics - Factorio Wiki
source: https://wiki.factorio.com/Balancer_mechanics
scraped_at: 2025-10-21 14:29:56
tags: [web, documentation]
---

# Balancer mechanics - Factorio Wiki

**Source:** [https://wiki.factorio.com/Balancer_mechanics](https://wiki.factorio.com/Balancer_mechanics)

Balancers are used to evenly distribute items over multiple belts or multiple belt lanes.

Balancers that are input balanced take evenly from all input belts/belt lanes. Balancers that are output balanced distribute evenly to all output belts/belt lanes. Ideally, a balancer should be input and output balanced.

## Contents

- 1 Belt balancers 1.1 Throughput 1.2 Universal balancers
- 2 Lane balancers
- 3 See also
- 4 Further reading

## Belt balancers

Belt balancers utilize the mechanic that splitters output items in a 1:1 ratio onto both their output belts. That means that a splitter can be used to put an equal amount of items on two belts. Since the process can be repeated infinitely, balancers with 2 n output belts are easy to create.

Balancers also use the mechanic that splitters take an equal amount of items from both input belts. That means that a splitter connected to two input belts will evenly distribute those items onto the the two output belts. To balance belts it has to be made sure that the output belts contain an equal number of items from each input belt.

- 1 full input belt gets split into two 50% full belts which get split into 4 belts that are each 25% full
- First the belts A and B go through a splitter so that the output belts contain an equal amount of items from each input belt (AB). The same is done with belts C and D. Then the mixed belts AB and CD go through splitters so that their output belts contain items from each input belt (ABCD)!

### Throughput

Balancers that are throughput limited may not be able to provide maximum output if one or more outputs are blocked. To be throughput un limited , a balancer must fulfil the following conditions:

- 100% throughput under full load.
- Any arbitrary amount of input belts should be able to go to any arbitrary amount of output belts.

Balancers often do not fulfill the second condition because of internal bottlenecks. The figure 1 below on the left shows a 4 → 4 balancer being fed by two belts, but only outputting one belt which means that its throughput in that arrangement is 50%. The bottleneck in this balancer is that the two middle belts only get input from one splitter. So, if only one side of that splitter gets input, as can be seen in the figure 1, it can only output one belt even though the side of the splitter is fed by a splitters which gets two full belts of input. In this particular case, the bottleneck can be fixed by feeding the two middle output belts with more splitters. This is done by adding two more splitters at the end of the balancer, as it can be seen at figure 2 below on the right:

- Figure 1: a 4 to 4 balancer with 2 belts being fed but only one total belt of output.
- Figure 2: the improved 4 to 4 balancer fully saturates both output belts.

However most balancers' bottlenecks can't be solved as easily. A guaranteed method to achieve throughput unlimited balancers is to place two balancers back to back that fulfil the first condition for throughput unlimited balancers (100% throughput under full load). The resulting balancer is usually larger than a balancer that was initially designed to be throughput unlimited. This is the case because they use more splitters than the minimum required amount of splitters for a throughput unlimited balancer. For n → n balancers where n is a power of two numbers, n×log 2 (n)−n÷2 can be used to calculate how many splitters are needed. This formula is based on the number of nodes in a Beneš network , which is essentially the same as a throughput unlimited balancer — it allows any input to reach any output.

### Universal balancers

Many balancers fail to balance properly once an output backs up or if an output is not used. In essence this means that an n-n balancer is not a functional n-(n-1) balancer. Sometimes this can be fixed by looping the unused output back around the balancer and distributing it among the inputs. Other times, this is not an option. Universal balancers solve this issue by having the back-looping built in. These balancers can balance evenly between any inputs and any outputs. Universal balancers can be throughput limited. If a universal balancer is throughput limited, the bottleneck may be in the loops or the balancer itself. A throughput limited universal balancer may only have the capacity for a few unused outputs. When more than the number of allowed outputs backs up, the universal balancer behaves like a normal balancer, and may not balance properly.

## Lane balancers

Lane balancers may be output balanced or input balanced. Input balanced lane balancers draw evenly from each side of the input belt, while output balanced lane balancers output evenly onto each lane of the output belt.

- This output balanced lane balancer distributes the items evenly among the output lanes, achieving output balance. Copy blueprint string 0eNqd01GLwyAMAOD/kmc3qlU7+1fGcbRbOIQ2LeqOG8X/PruN3cNZuPmmknwmhCzQDxecnaUA7QL2NJGH9riAt1/UDesbdSNCC8F15OfJhV2PQ4DIwNIZf6Dl8YMBUrDB4iP3frl+0mXs0aUAtmEwmCef0iZa/0nUTlZ8rxhc01Ec9ipG9kcTZZrJa/U7mnhpTdIYnK3D0yNEZmxZZut8paqs7yav6Xe0artvLjJ4U4ZvNH4oa1z/Z0TmZft5sCGkt+xwnqbKV8irshLlBle4MPXKpV20AceU+7vYDL7R+XuW0sJIY5QSSteCx3gD6bVJ7A==

## See also

- Belt transport system Splitters Transport belts Underground belts

## Further reading

- Command line belt balancer analyzer
- Fractal (2 n ) balancer generation tool
- Belt Balancers - how they work and how to make them
- Finding balance: A guide to belt balancers
