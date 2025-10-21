---
title: Tutorial:Main bus - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Main_bus
scraped_at: 2025-10-16 15:45:52
tags: [web, documentation]
---

# Tutorial:Main bus - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Main_bus](https://wiki.factorio.com/Tutorial:Main_bus)

The concept of a Main Bus is to put the most used and useful ingredients in a central spot to use for assembling machines. 
This is a good measure to combat "spaghetti factories" as it forces someone to plan a structured layout and move everything to use items from the bus.
This is also a downside as there are more belts used and therefore more room for belt-buffer and everything is less compact.

Whether one uses a bus is often decided before starting a map or when first building an array of furnaces.

A bus often starts at the smelting of iron, copper and steel, and then over time and distance gains more and more different items.
When one doesn't have enough production to saturate a belt (or splits it into more) then this can be called a "fake"-bus as it can not be saturated. 
This is especially deceiving when the item isn't moving and all belts have filled up as these belts can't carry the amount they lead one to believe they can.
This can be done to reserve room for later expansion, blueprint-ghosts are a good usage for that as they don't allow the belt to be filled with non-usable items.

The direction of a bus, being horizontal or vertical depends on personal preference and how one likes to work on the production that splits off it, which can almost always be expanded for greater use later on. 
The orientation of and how wide the players monitor is also plays a role in this decision. 
A corner is not unheard of but very unusual and is often only necessary when a lake appears that is not planned for.

## Contents

- 1 Content
- 2 Advice and Limitations
- 3 Split-off
- 4 See Also

## Content

What items one puts on a bus is a personal preference.
Some items are a good candidate to be built "on-site" meaning not carried by the bus but rather made where they are needed.
A good example of this are copper cables as they consume more space on a belt than in the form of copper plates.

Here are some things people have put on their bus in the past:

- Several belts of iron plates , usually a multiple of four as that is the length one underground belt can pass under.
- Some belts of copper plates . You need about as much copper overall as iron.
- Iron gear wheels are seen on some buses as they take up half as much room than iron plates and see usage in a lot of recipes.
- Electronic circuits .  You will need many of these to handle advanced circuit and processing unit production later on.
- Advanced circuits .
- Steel plates .
- Processing units .
- Batteries .
- Plastic bars (sometimes replaced by coal from which plastic is produced).
- Stone . Needed for production science packs and for stone bricks .
- Sulfur . This is an ingredient needed for the chemical science pack .

Each of these items would get a dedicated line of belts from which one would draw from if there is a need for the item.

Some people like to have fluids part of their bus which could include:

- Sulfuric acid for processing units.
- Water for concrete .
- Lubricant for express transport belt and electric engine units for the utility science pack .

## Advice and Limitations

Having all possible items on a bus results in a huge wide bus with a lot of belt-buffer for expensive items and standing belts of output-items that won't get used in another process.
These items are often just put into chests for personal use rather than on a bus.

The width of the bus can become a problem if it is very wide.
Players sometimes choose to only build on one side of the bus until they can estimate that they won't need more belts on the bus.

It is advisable to leave space between the groups of belts of one item for underground belt to surface and for other things to cross the bus.
A recommended number is two free spaces for every group of four belts, although leaving more space can be useful too.
Same with the production that is to the side of the bus, leave space between the builds for later expansion or belts that go between, at least three, six to ten is fitting.
Grouping differing items together can cause problems when splitting them off, hence only groupings of two differing items is recommended. 
Having smaller groups of only one or two is also not a bad thing.

When logistic robots are available one might start moving some items by robots instead of using the bus. 
Some players eventually phase out the main bus entirely in favor of robots. 
This may happen at a later stage in the game up to which a bus is a very good tool to reduce clutter. 
But robots have their own difficulties and require a lot more resources and knowledge of the game.

For very large amounts of items railways may be a better alternative that can not only carry large amounts of ore but also the intermediate and end-products.
This can lead to designs of a base consisting of only train-stations with small logistic networks without any belts.
For a comparison of belt, logistic robot and railway transport systems, refer to the Transport use cases tutorial .

One reddit post mentions the use of cargo wagons as a means to increase throughput and reduce the size of a bus.

## Split-off

When one wants to use the items on their bus one could directly take items off the bus as if it is just a belt, though that would mean an extremely long bus and useless lengths of other belts.
This is sometimes done to get Items crafted into a chest for personal use like pipe which only uses Iron plates.
However, in most cases a belt is split away from the main bus that can deliver the resource to a sub-factory. 
Split-off designs aren't strictly necessary but help immensely. 
The following designs have the additional property that if the incoming belts are fully saturated then the split-off belt will be full (recall that a single splitter with a single full input belt will by default split off a half-filled belt).

With splitter priorities that were added in 0.16 it is very simple to split off a belt from a main bus while ensuring good throughput properties. The design shown here makes sure that the belts on the right side are filled first, so belts can be taken from the right every time without the need to further rebalance. 
Thus up to a full belt can be delivered and the remaining resources can go through on the main bus. 
One downside to this can be that all resources are used up before every machine gets fed. 
This indicates not enough products being produced to meet demand, this can be remedied with adding more lanes with corresponding more production further up the chain of production. 
Using a non-prioritizing split-off will only distribute the shortage, not magically create more production.

Alternatively, one can make split-off setups without priority splitters. 
The idea is that one wants to draw from every belt (and lane even) equally to not have too few items at the current planned production and not have empty and at the same time standing belts of items.
That way at every step along the bus a few items are split off and used up and when the production comes to a stop the items go on to be used by the next production.

The following are 2 designs for a split-off off a 2-wide bus (by reddit user /u/unique_2 ).

- Copy blueprint string 0eNqVld9ugyAUxl/FnKstwRbwT1sfY7fL0mhLHIlFh9DMGN99qO1mWrrCFfHI9+NwvgP0UFSaNZILBVkP/FCLFrL3HlpeirwaY6prGGRw5lJpE0Eg8tMYmGeEFAYEXBzZN2RkQB7Kt4WSWpVcsdNC1lRcKSYXsshBpmQu2qaWKixYpRbiePhAwITiirN509NHtxf6VJhlMvKIgaCpWyOrxbiqQYUUQWeGeBgTusFQdwz5BxN5ZxPZMLE3htowiTMGXykIjlyyw/wrtjBT70LdQKkFuvmFamO7LGVtxidY01bXXqq1avTYNXfgrW8hsa2Ou/v2tqS1SubEiA1BsKcX+HnVCPH1lzhAqb8X+M8KLh44QSKHIl6sxavEIVHvQ2I3JvEx13rMSOqCwBeEPYuN72as9wbZ+p5OgzEX7HQZZ4tnBkGVG52J0XDaUyB5+amCl6IL1nqtBf/SbE9fg9xMPTPZTuA0jmmabiihu2H4AQXcOK0=
- Copy blueprint string 0eNqVlNFugzAMRX8F+WmTwkpSSlc+Y6/TVEEbdZZoYMGphir+fYZOHVrTijwhQu7J9Y3xGcrK6caiIcjPgLvatJC/n6HFgymqYY26RkMOJ7TkeEWAKY7DwmVHrKAXgGavvyGXvQhQvk2UyqtE0seJrKmQSNuJbDlDRrYwbVNbiktd0USc9h8CtCEk1Jeix5dua9yx5GNyeY8hoKlbltVmOJVRMW/t+JH2g6F/GDUbkzygLIPNLH2YNBijfJjVbMzVjIA9Wr27fFIeZnZ707cJvaweuFpfCY6v2B5szc/HWQ++ftumdtS4oUFuuK+hoSU+d5sZ9cXXAqUPIZPA3L1GpAy9Pb8ZFRx38pc2mjthy+BO97tLQ+L2tpNcBXSk30QWWov3p5XrwBHCFJ5t4xzMJxNeQFWwjNdUPFYUWTx8UvRUdtHCLZzBL6e36jkqeetJ23bkZmmqsmytpNr0/Q+uzw2D

Putting a lane-balancer after a split-off is not necessary most of the time as the rest moves on if the belt has no draw or if only one lane is used. 
If there is enough input for the item to saturate a whole belt then putting a lane-balancer in won't help to get more items later on. 
Putting a lane-balancer after an inherently balanced build that produces the item is also not necessary as then half of the production pauses and the other half fills the moving lane to saturation. 
The following is a split-off off a 4-wide bus.

- Copy blueprint string 0eNqlld1qhDAQhV+lzHUsxv/6DPsGpRTdDUvAjRLjUhHfvaPWVTBbMu1VcPR8OTOTMQOUVScaLZWBfAB5rlUL+fsArbyqoppipm8E5HCX2nQYYaCK2xRYvvAiGBlIdRFfkPOREZSnnTKwKqURt01mdKHaptbGK0VlduLwP+Jo/GAglJFGiiX1+aH/VN2tFBqTejA6VOirrnFdKAyaukVhraZ9EeYFDHpc0NFqo+5M000bHsABAewTuCHFMCeAo2fVPGAfVAsl/kM9+WZPqifuEmd3KxUPHVykFuflXWKBpu5Q7gzNtkloKmkMxo44/zVec7cg3qitCGwU7lMxVjOcuyTEfxLyrYiA2j27k9DBif+rkYg8lS6Hk8f0oXTiJsQO2suWUhpoP0oZofJIwJ/u/IPOdxcQg6pA7xiLvBnyMl0ad6HbZZSyNOBZmPhhNI7frCw6ag==
- Copy blueprint string 0eNqdld9qgzAUxl9lnOs4TBq19Rl6tdsxhrahBGyUGMuK+O476jqFxpGzq+DR75fv/DHpoaw61VhtHOQ96FNtWsjfe2j1xRTVGHP3RkEON21dhxEGpriOgfmLSMLAQJuz+oKcD8yj1E5dF5mzhWmb2rqoVJVbiYVXvLXtcaXckZRvK6UcPhgo47TTas57erh/mu5aKosZ/ao7VNiLrXGdnTNo6haFtRk3RVgkGNxxQTsPD3Xnmm5M8gksCOCYwN1RDHMCWBLAFG7yjwrzBazNBjfdmrhNKg4gnLVVp/ld6oFmwdDYyxQe5j7cKA82elimvqm0cxh7xsWvyaOeHgSP6R0PaQznwQnz4CJyEZIw/0k49ua7o06Mv2wywEn8p5GEfDYE1T2lHw1B3IzYT3/Z9pQGCi/iQKg8EvDon66mfHUHMqgK9I4xGU2Ql2qE3JRt539NSpGmmeDiMAzfI+ZmDA==
- Copy blueprint string 0eNqlldFugzAMRX9l8nOYcEih5TP2Ok0TbaMqEgQUQjVU8e8LdAy0hirWniIM9+TajsMNjmUnG6O0hfwG6lTrFvL3G7TqootyjNm+kZDDVRnbuQgDXVRj4P5FJGBgoPRZfkGOAyMo31ZK7lUqK6tFZk2h26Y2NjrK0q7EyX/EYvhgILVVVsl76tND/6m76iiNS2qLwaCpWyer9birQ0WcQe+WZBgN/cHwX0znNjYXU7t1AxTPHDYnU3e26UbbD9yEwI2QABYEMIW7I9eT++qZkjHow2TBmHg2w+CsjDzdX3EPc7+c9KZU1rrYo6n4dffE1iHYFgbbwpjeUVw6qvRGQxFD8sWffGNfusip3fRWDZMAJ/FTI4I8pkEl2tGnNIibEs+Jv2wZpYHeacQ9ofKO4O7c6X7OV/8fBmXhvLuYiCbIy8i4StNOiFQInqYZR34Yhm/sYzpB

Taking two belts off of this won't produce two belts worth of output, the middle one only carries half a belt to each side!
As of 0.16 Splitters can prioritize one in- and output lane, therefore the above design can supply fully saturated belts if the splitters are set up in a way that prioritizes the output belt (to earlier production) rather than letting items go on.

The following are two designs for a split-off off a 4-wide bus that feature an in-line lane-balancer(by reddit user /u/moomaka ).

- Copy blueprint string 0eNqVllFugzAMhq9S5WmToCUh0JYz7AbTNEGbVdEgQSFUQxV3n4ExsTVs8VOEyf/Z2I7DjRRlK2ojlSXZjciTVg3Jnm+kkReVl4PNdrUgGblKY1uwBETl1WCYdoSc9AGR6iw+SEb7AKF8WiiZUymtqBayupTWCrOQxR4ya3LV1NrYsBClXYh5/xIQoay0UkwfPT50r6qtCnCT0W9GCwpzMRrWiRKQWjcg1GrwC7AQNnewQERzGLq1dTs4vAMzBBjDjRHcCMHla8m8o7KZ6qAk3pTwCwNdQc7SiNP0jjugKRpKf0JTB3R/33OrBafb5H/gAV+Y32F6lOmI98LwXmiE795VN1KteaHehZ0L4eo5yrCty5yYGItxR8PxEyXqPZKV+DRstE1Goju01AMxEyInwefU0D9jOCCz7I7j6D8SphQ7S84iTE6dA49R9ElhHtVmDH3OvbAxon7u78XeE5B4uILH6zpb/IgEpMxBBjYejqFsSvFmNw9Ft9m1u0rrKn/PH2HbVZhmGiicszTdM8qOff8JVpvtyQ==
- Copy blueprint string 0eNqdlt1ugjAUx1/F9GpLitJDReUxdrssC2jjmkFLSjEjhndfwbkQLabHq4bC/3c+e8qZFGUraiOVJdmZyL1WDcnez6SRR5WXw57takEycpLGtm6HEpVXw8bli4iTnhKpDuKHZKynCOXbRAlepbSimsjqUlorzESWBMisyVVTa2OjQpR2Iub9ByVCWWmluAQ9PnSfqq0KZyZjcwxKat04mVaDVYeKEkq6YekHh24w8I9pnWFzNNqtcyB2BdFrNLq1dTv4fQdOMGBAgDkCHCO4a3RCmS+hKRoDPswmHAMPvNk+UV53UMhBGrG/vIOA3O2eKDbMmZFqxgqLn4gG8NGw8LPlN8J9UMBCb+vggyb3A2juELDlOgDIse0b+9qOrQP8imC5HhHezmVpCIL9IfxebEIQ8UMvtuhpE/cBnbzDptk7JCDGpNk//xn+TEFAhAD4kRDETTA19Ycc3uPxNffuMh4v7mzyS0JJmTuZ2+PR6MvCyOOXXbwU3WLVriqtq/w7f3XfnYRpRmjKOaTpBhjs+v4XLT/v+g==

The way in which materials are split off from the main bus determines which production setups in the factory are prioritized if the bus delivers less input than all the setups combined need. 
The split-offs shown above generally prefer setups near the start of the main bus but will also supply some limited materials to the later setups. 
There are alternative designs, for example, using splitter priorities to fully prefer the setups near the start of the main bus and only allow materials to go through to a later setup if that earlier setup's needs are satisfied. 
The priorities can be set in various ways but this should not distract from the fact that more resource input should be added whenever this becomes a concern.

## See Also

- What Transport for which case?
- Belt transport system
- Logistic network
- Railway
- Splitter
- Balancer mechanics
