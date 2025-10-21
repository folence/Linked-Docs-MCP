---
title: Locomotive - Factorio Wiki
source: https://wiki.factorio.com/Locomotive
scraped_at: 2025-10-21 14:30:40
tags: [web, documentation]
---

# Locomotive - Factorio Wiki

**Source:** [https://wiki.factorio.com/Locomotive](https://wiki.factorio.com/Locomotive)


|  | Locomotive | Edit |

| Recipe |
| 4 + 10 + 20 + 30 → 1 |
| Total raw |
| 16.5 + 15 + 20 + 10 + 30 |
| Map icon |  |
| Storage size | 3 (fuel only) |
| Health | 1000 1300 1600 1900 2500 |  |  | 1000 |  | 1300 |  | 1600 |  | 1900 |  | 2500 |
|  |  | 1000 |
|  | 1300 |  | 1600 |
|  | 1900 |  | 2500 |
| Resistances | Acid: 3/20% Explosion: 15/30% Fire: 15/50% Impact: 50/60% Physical: 15/30% |
| Stack size | 5 |
| Rocket capacity | 5 (1 stack) |
| Dimensions | 2×6 |
| Energy consumption | 600 kW ( burner ) |
| Mining time | 0.5 |
| Weight | 2000 |
| Prototype type | locomotive |
| Internal name | locomotive |
| Required technologies |
|  |
| Boosting technologies |
|  |
| Produced by |
|  |
| Valid fuel |
|  |

The Locomotive is the engine for movement of trains over tracks . Trains are useful for moving large amounts of items over large distances. With the Space Age expansion, locomotives can also utilize elevated rails , which are rails built off of a rail ramp , allowing trains to freely drive over obstacles on the ground.

Locomotives are also good vehicles for the player to reach fixed destinations, as they are considerably faster than the car or tank .  Naturally, they do not have the same freedom of movement, as they are confined to the track. They can be set up to travel automatically between train stops , or be controlled manually, even if the player is in a cargo wagon attached to the train instead of the locomotive itself. Automatic trains can also use rail signals and rail chain signals to designate different or changing paths on a railway, as well as manage multiple trains on multiple or intertwining tracks.

Locomotives are burner devices and require fuel to run; the more powerful the fuel used, the faster the locomotive's acceleration and top speed will be. Solid fuel , rocket fuel and nuclear fuel will give +20%, +80% and +150% acceleration respectively, and provide +5%, +15% and +15% for top speed respectively. Multiple locomotives can be used on a single train to increase its speed. If a locomotive has no fuel, it can still be moved manually, albeit very slowly.

While locomotives can be assembled by hand, the engine unit for it requires automated construction to build, so it cannot be built from raw materials by hand. The color of the locomotive can be customized.

## Contents

- 1 Connecting/Disconnecting a locomotive
- 2 Defense
- 3 Maximum speed
- 4 Fuel duration (in seconds)
- 5 Driving controls
- 6 Achievements
- 7 Gallery
- 8 History
- 9 See also

## Connecting/Disconnecting a locomotive

To connect locomotives, cargo wagons, or fluid wagons to each other, either place the cars next to each other on the track (there will be an outlined green connection), or connect an already existing disconnected car by driving the locomotive near the car and press G by default. To disconnect the last car in a train, press V by default.

## Defense

Locomotives in transit can usually crash through everything in its way (including biters, other vehicles , and the player). However, if the locomotive is moving too slowly, or the target is too tough, it will stop the train instead. Once stopped, the train will continually do damage if trying to accelerate. If the locomotive hits an enemy , the enemies will fight back and try to destroy the train and the rails.

Construction robots are a good way to automatically repair damage at train stations.

## Maximum speed

The maximum speed that a locomotive can get to depends on the train that it is pulling. The speed of an accelerating, fully fueled, train is calculated every tick by the game with the following formula:

```
train_speed = max(0, abs(train_speed) - train_friction_force ÷ train_weight)
train_speed = train_speed + (10 × number_of_locomotives_in_moving_direction × fuel_acceleration_bonus ÷ train_weight)
train_speed = train_speed × (1 - air_resistance_of_front_rolling_stock ÷ (train_weight ÷ 1000))
```

where train_friction_force is the total friction of each wagon and locomotive (0.5 for any type of wagon including locomotives) and train_weight is the total weight of each wagon and locomotive (see their individual pages for the weight values). The friction and air resistance of wagons and locomotives can be found in their prototypes. The calculated train_speed is capped to max_speed = 1.2 * fuel_top_speed_multiplier .

## Fuel duration (in seconds)

| 1 item of | Burning time in seconds |
| Wood | 3.33 |
| Coal | 6.67 |
| Solid fuel | 20 |
| Rocket fuel | 166.67 |
| Nuclear fuel | 2016.67 |

## Driving controls

These are the default bindings, they can be changed in the Settings menu.

| Command | Keyboard and mouse | Controller |
| Enter/Exit | ENTER | ZR + X |
| Accelerate | W | Use left joystick |
| Decelerate/Reverse | S | Use left joystick |
| Pick which fork to take at junction (left, right) | A , D | Use left joystick |
| Connect/Disconnect train | G , V | Not set |

When using a controller, such as on the Nintendo Switch , the behaviour of the left joystick in vehicles can be switched between two modes:

- Relative vehicle driving mode (default): Moving the stick in a direction will make vehicles automatically turn and accelerate to that side of the screen.
- Absolute vehicle driving mode: Moving the stick up/down will make vehicles accelerate/brake. Moving the stick left/right will make vehicles turn in that direction.

## Achievements

Locomotives are directly connected to the following achievements:

|  | Getting on track Build a locomotive . |

|  | Getting on track like a pro Build a locomotive within the first 90 minutes of the game. |

|  | Watch your step Get killed by a moving locomotive . |

## Gallery

- The player among different colored locomotives.

## History

- 2.0.7 : Locomotive sounds overhauled.

- 0.17.0 : Locomotive fuel consumption doubled.

- 0.16.0 : Locomotive will show train ID in its tooltip. The ID can be used in circuit network conditions.

- 0.15.19 : Locomotive snaps to a train stop when placing the first locomotive next to the train stop.

- 0.15.7 : Inserters will no longer take fuel from locomotives and instead will take the burnt result items if the locomotive fuel uses that system.

- 0.15.0 : Renamed "diesel-locomotive" to "locomotive"

- 0.14.0 : Added support for equipment grids in locomotives.

- 0.13.0 : New locomotive graphics. Can now be colored. Trains are now regular size in horizontal and vertical orientations.

- 0.12.1 : Trains that are moving automatically cannot be rotated.

- 0.12.0 : Now show contents in tooltip.

- 0.11.18 : Increased the crafting cost of the cargo wagon and locomotive. Removing and merging the locomotive of a train without any additional locomotives doesn't clear the schedule anymore.

- 0.11.6 : Copy paste can now be used for train schedules.

- 0.10.2 : Now recalculates path on rotation.

- 0.10.0 : Backer names are used for locomotives.

- 0.9.0 : Recipe change

- 0.5.0 : Train can find the path backward when it has locomotives in the back New locomotive graphics. Locomotive + wagon + rails are more expensive.

- 0.4.1 : Smooth (precise) rolling stock placement. Rotating while building affects the direction of the rolling stock. Rolling stocks can be disconnected from both sides.

- 0.4.0 : Locomotive uses fuel. Locomotive and Car are minable Easier riding in locomotive and car (accelerate vs. brake vs. reverse) Automated train transportation. Trains can be given schedule to go to Train Stops (named after backers).

- 0.2.8 : Now shows health bar below locomotive.

- 0.2.1 : Now emits light if active.

- 0.1.0 : Introduced

## See also

- Railway
- Cargo wagon
- Fluid wagon

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
