---
title: Storage tank - Factorio Wiki
source: https://wiki.factorio.com/Storage_tank
scraped_at: 2025-10-21 14:30:04
tags: [web, documentation]
---

# Storage tank - Factorio Wiki

**Source:** [https://wiki.factorio.com/Storage_tank](https://wiki.factorio.com/Storage_tank)

This article is about the liquid storage container. For the armored combat vehicle, see Tank .

|  | Storage tank | Edit |

| Recipe |
| 3 + 20 + 5 → 1 |
| Total raw |
| 3 + 20 + 5 |
| Map color |  |
| Fluid storage volume | 25000 |
| Health | 500 650 800 950 1250 |  |  | 500 |  | 650 |  | 800 |  | 950 |  | 1250 |
|  |  | 500 |
|  | 650 |  | 800 |
|  | 950 |  | 1250 |
| Stack size | 50 |
| Rocket capacity | 50 |
| Dimensions | 3×3 |
| Mining time | 0.5 |
| Prototype type | storage-tank |
| Internal name | storage-tank |
| Required technologies |
|  |
| Produced by |
|  |
| Consumed by |
|  |

The storage tank is a building that can store up to 25,000 units of a fluid . It is a passive storage — it has no input and no output, essentially acting as volume increase of the pipe segment it is connected to.

## Contents

- 1 Usage
- 2 Usage as "Energy-tank" 2.1 Calculations
- 3 Gallery
- 4 History
- 5 See also

## Usage

The storage tank is often used to store raw materials and excess products from oil processing , allowing a refinery to run without interruptions. It can be used as short term buffer to keep up throughput for high volume recipes such as acid neutralisation and steam condensation to avoid the machines getting full or empty. It can also be connected to the circuit network , sending the fluid contents as a signal to the network.

Storage tanks are part of the fluid segment they are connected to, so they are always filled to the same percentage of capacity as the pipes that lead to it. As there is no real flow in the pipes, a storage tank is always filled evenly with the segment it is connected to, regardless of how far away an inflow is. If there are multiple storage tanks connected to the same pipe segment, they all have exactly the same fill state.

The fluid inside the storage tank can be destroyed by flushing the storage tank or the whole fluid system in the GUI, or by mining and rebuilding the storage tank. The storage tank can be emptied without destroying the contained fluid by draining it with a pump . Mining a storage tank will send its contents to the next nearest storage tanks, if the fluids match.

## Usage as "Energy-tank"

Storage tanks can also be used as a replacement for accumulators . If steam consumption by steam engines or turbines changes a lot over a daily cycle (for example due to solar panels or laser turrets ), storage tanks can be filled with steam during low power usage and then emptied during heavy load.

A storage tank filled with heat exchanger 500°C steam stores around 2.4GJ; a storage tank filled with boiler 165°C steam stores 750MJ.

### Calculations

- 1 Storage tank can store 25,000 units of 500ºC steam.
- 1 Steam turbine can output 5,820kW = 5,820kJ/s using 60 units of 500ºC steam/s.
- 1 Storage tank can keep 1 steam turbine working at full capacity for 25,000 ∕ 60 ≈ 416.6667s
- A Storage tank can store up to 25,000 ∕ 60 × 5,820 = 2,425,000kJ using 500ºC steam.

- 1 Storage tank can store 25,000 units of 165ºC steam.
- 1 Steam engine can output 900kW = 900kJ/s using 30 units of 165ºC steam/s.
- 1 Storage tank can keep 1 steam engine working for 25,000 ∕ 30 ≈ 833.3333s
- A Storage tank can store up to 25,000 ∕ 30 × 900 = 750,000kJ using 165ºC steam.

## Gallery

- The storage tank's GUI with the ability to clear the contained fluid.
- Four storage tanks linked together to form a large storage facility.

## History

- 0.15.7 : Reduced the mining time of the storage tank from 3 seconds to 1.5 seconds.

- 0.15.0 : Multiplied all fluid amounts by 10.

- 0.13.12 : Fluid icon now scales with size of tank.

- 0.12.0 : Liquid inside can be seen through a small window. Now connectible to the circuit network .

- 0.9.1 : Storage tank has 2.5 times bigger capacity (25000 litres) and takes longer to mine.

- 0.9.0 : Introduced

## See also

- Fluid system

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
