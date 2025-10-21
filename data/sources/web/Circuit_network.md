---
title: Circuit network - Factorio Wiki
source: https://wiki.factorio.com/Circuit_network
scraped_at: 2025-10-21 14:29:48
tags: [web, documentation]
---

# Circuit network - Factorio Wiki

**Source:** [https://wiki.factorio.com/Circuit_network](https://wiki.factorio.com/Circuit_network)

Circuit networks are built using red or green wire , and enable the control of receivers, based upon information broadcast onto the network by connected senders.  Most senders are storage devices, and broadcast their information onto a specific channel, based on the item or liquid the storage device contains.  Each circuit network contains a channel for every kind of item, as well as 48 extra virtual signals which act as user-definable channels. ' Everything ', ' Anything ' and ' Each ' are also available wildcards.

## Contents

- 1 Usage 1.1 Send information 1.2 Control devices
- 2 Devices
- 3 Physical network structure
- 4 Combinators
- 5 Virtual signals 5.1 Logic signals 5.1.1 Everything 5.1.2 Anything 5.1.3 Each
- 6 Tutorials
- 7 Logistic network
- 8 History

## Usage

### Send information

Senders broadcast the amount of items or fluids they contain or other data definable by the player. Each amount is broadcast as a numeric value on a 'channel' corresponding to the item.  For example, a Storage Tank containing 1000 Crude Oil will broadcast 1000 on the Crude Oil channel.

The channels are separated from each other, so each network can simultaneously carry a number for each item and fluid in the game, and for each of the extra user-defined channels (digits 0-9, letters A-Z, and 9 different colors). All unused channels have the value zero.

Multiple broadcasts of the same item or fluid are additive: If there are two connected Storage Tanks with 1000 Crude Oil each, the value of the Crude Oil channel within the network will be 2000.

All wires of the same color which are connected together by junctions form a network, i.e. they will pass their signals to each other.  For example, if two red wires are connected to the same combinator input, each wire receives the content from the other.  This can result in feedback if care is not taken; see Feedback (under arithmetic combinator , below) for discussion.

Numbers are in the signed 32 bit integer range, i.e. from -2147483648 to 2147483647 inclusive, and are encoded in two's complement representation . The numbers wrap around on overflow, so e.g. 2147483647 + 10 becomes -2147483639. When entering a number in a combinator it can appear to exceed the 32 bit limit until the GUI is closed, at which point the number will overflow/underflow. [1]

### Control devices

Receivers can use broadcast information, in most cases to enable/disable the device. They can either compare results between different channels, or compare a channel to a specific value.

Receiving devices sum all signals from each wire connected to them, even red and green wires. For example, if an inserter is connected to a red wire carrying a signal for 20 copper plates and a green wire with 10 copper plates, the input signal set for that receiver will be 30 copper plates.

Multiple wires of the same color will share & sum their signals. For example, 3 chests A, B and C connected in a row (A -> B -> C) with green wire will output the sum of their contents along any green wire connected to any of the chests. However, if a red wire connects chest A to an inserter, that inserter will only be given the contents of A as its input signal.

## Devices

Each device that is able to be connected to a circuit network has a icon located in the top right corner of its info pane. Clicking this icon will display the available circuit network options for that device (note: a red or green wire must be connected, otherwise the message "not connected" will display instead). Clicking the icon next to it, the device can be connected to a logistic network if in range of one, which also allows conditions to be set.

Conditions can be set for both circuit (signals of red and green wires are summed) and logistic network, which will together act as a logical AND.

The following devices can be connected to a circuit network:

| Icon | Name | Possible output signals | Possible circuit control | Possible logistic network control |
|  | Transport belts | Transport belts can send their content to the circuit network. Pulse mode : The signal is sent for only 1 tick when the item enters the belt. Hold mode : The signal is sent continuously as long as the items are on the belt. Hold mode (All belts): The signal is sent continuously for all items on the entire transport belt line. The count continues through underground belts, but not splitters or side loading. | Transport belts can be enabled on a condition. | Transport belts can be enabled on a logistic network condition. |
|  | Splitters |  | Can set the priority input and/or output sides on a condition. Can set the filter based on a signal. Setting a filter will only work if "set output sides" is enabled and the condition for either left or right is true. If both sides are true, then the splitter will default to filtering the item to the left side. If there are multiple input signals that can be used as a filter, then the splitter will choose the item that appears first in the Factoriopedia. |  |
|  | Inserters | All inserters can send their held items to the circuit network. Pulse mode : The signal is sent for only 1 tick when the item is picked up. Hold mode : The signal is sent continuously as long as the inserter is holding the item. | All inserters can be enabled on a condition. The inserter stack size can also be overridden from a control signal (configurable; values less than 1 are treated as 1). Filters can be set on a signal. | All inserters can be enabled on a logistic network condition. |
|  | Assembling machines , Oil refinery , Chemical plant , Centrifuge , Crusher , Foundry , Electromagnetic plant , Biochamber , Cryogenic plant | All crafting machines can output: Their contents, including fluids, in all slots Optionally, can include the items within the current crafting job If the machine has fuel, can optionally include the current fuel, including the unit of fuel currently being burned The ingredients of the set recipe A control signal, for 1 tick, when the recipe finishes crafting The signal value indicates the number of crafts finished last tick Includes productivity crafts A control signal, while the building is working | All crafting machines can enable on a condition and set their recipe based on a signal. The machine, if not given a recipe signal, will use the main crafting recipe for the item/fluid (as shown in the Factoriopedia) |  |
|  | Furnaces and the Recycler | Furnace-style crafting machines can output: Their contents, including fluids, but not fuel, in all slots Optionally, can include the items within the current crafting job If the machine requires fuel, can optionally include the current fuel, including the unit of fuel currently being burned The ingredients of automatically determined recipe A control signal, for 1 tick, when the recipe finishes crafting The signal value indicates the number of crafts finished last tick Includes productivity crafts A control signal, while the building is working | All furnace-style crafting machines can enable on a condition |  |
|  | Chests | Can send its content to the circuit network. |  |
|  | Cargo landing pad | The landing pad can send its contents to the circuit network. | The landing pad can have its requests set by the circuit network. |  |
|  | Rocket silo | The rocket silo can output its contents or requests from space platforms. |  |  |
|  | Space platform hub | Can output its contents, destination and source planet, current speed, and damage taken Default : Read Speed = Signal V Default : Read Damage Taken = Signal D | Platform hub can be sent the contents of the circuit network to use for wait conditions |  |
|  | Asteroid collector | Can output its contents to the circuit network | Can enable on a condition and set filters on a signal |  |
|  | Requester chest , Buffer chest , Storage chest , Passive provider chest , Active provider chest | Can send its contents to the circuit network. | Buffer and requester chests can have their requested items set by the circuit network. Can be enabled/disabled via a circuit network condition. When disabled, chests that provide items to the logistics network no longer provide those items. When disabled, chests that request items from the logistics network no longer request those items. |  |
|  | Storage tank | The storage tank can send its fluid content to the circuit network. |  |
|  | Gate | Gates can send a signal to the circuit network. Default : Player detected = | Gates can be opened on a condition. |  |
|  | Nuclear reactor , Heating tower | The reactor and heating tower can output any fuel, including the fuel currently being burned, to the circuit network, as well as its current temperature Default : Read temperature = |  |
|  | Agricultural tower | Can output any seeds and harvested plants in its inventory | Agricultural tower can be enabled on a condition | Can be enabled on a logistic network condition |
|  | Gun turret , Laser turret , Flamethrower turret , Rocket turret , Tesla turret , Railgun turret | Can send their respective ammunition to the circuit network Laser and tesla turrets will not send any signal if this option is selected, due to not using ammo | Can enable, set priorities, and ignore priorities on a condition | Can be enabled on a logistic network condition |
|  | Artillery turret | Can send its ammunition to the circuit network | Can be enabled on a condition | Can be enabled on a logistic network condition |
|  | Rail signal | Rail signals can send their state to the circuit network. Default : Note: If red due to circuit network, does NOT output red signal | Rail signals can be set to red on a condition. |  |
|  | Rail chain signal | Rail chain signals can send their state to the circuit network. Default : |  |
|  | Train stop | Train stops can output: The contents, except fuel, of a stopped train Any fluid amounts are rounded down to the nearest full number, except when the fluid is < 1, then it is rounded to 1. The unique Train ID of a stopped train, defaulting to The number of trains en-route to the current stop, including the currently stopped train, defaulting to | Send the signal to the train, to use in wait conditions Enable the stop on a condition Disabled stops act as if their train limit = 0. Trains attempting to go here will enter the "Destination Full" state. Set the stop's train limit to the value of a control signal, defaulting to Set the stop's priority to the value of a control signal, defaulting to "P" | Train stops can be enabled on a logistic network condition. |
|  | Accumulator | It can send its charge level in percent to the circuit network. Default : Charge % = |  |  |
|  | Roboport | It can send its logistic network contents and/or its robot statistics to the circuit network. The signals used for robot statistics are configurable. Default : Available Logistics Bots = Default : Total Logistics Bots = Default : Available Construction Bots = Default : Total Construction Bots = Default : Roboports in Network = |  |
|  | Radar | Radars will transmit any signals passed into it to all other radars on the same planet. Unlike other machine outputs, signals from red and green wires are transmitted separately. |  |  |
|  | Display panel |  | Can display a label and/or custom message on a condition |  |
|  | Mining drills | All mining drills can send the expected resources, either from the drill itself or from the whole ore patch the drill is on. | Mining drills can be enabled on a condition. | Mining drills can be enabled on a logistic network condition. |
|  | Pumpjack | It can output the current oil mining rate. | It can be enabled on a condition. | It can be enabled on a logistic network condition. |
|  | Power switch |  | Power switches can connect power networks on a condition. | It can be enabled on a logistic network condition. |
|  | Programmable speaker |  | Shows alerts and plays sounds based on circuit network signals. It can be used to make simple tunes. |
|  | Lamp |  | The lamp can be enabled on a condition. Color mapping : The color is set based on the provided color signals Color components : The color is set based on the values of incoming red, green, and blue color signals, which should be between 0 and 255 Packed RGB : The color is set based on a single hex encoded RGB color on the white color signal. It should be between 0 and 16777215 | The lamp can be enabled on a logistic network condition. |
|  | Offshore pump |  | The offshore pump can be enabled on a condition. | The offshore pump can be enabled on a logistic network condition. |
|  | Pump |  | The pump can be enabled on a condition and set its filter on a signal | The pump can be enabled on a logistic network condition. |

## Physical network structure

A circuit network consists only of those devices connected together with the same color wire. Wire can be strung directly from device to device, or across any intervening power poles. Wire length is limited by its previous connection.

Note that each connected set of wires forms a separate network.  For example, it's entirely possible to have four red-wire networks and three green-wire networks. If red and green wires happen to touch the same power pole or device, the red and green networks will remain separate and will not link up. However, two red cables or two green cables will link if they touch. Use different colored cables to separate networks in close proximity.

- To connect wires or cables to a power pole, simply click on one entity, then on the base of the power pole.
- To erase a wire or cable connection, place the same color wire over an existing connection. You don't get the wire/cable back.
- To remove all connections from a power pole, shift-click on the pole.  The first shift-click will remove all electrical connections, and the second will remove all red and green wires.
- When connecting to a arithmetic combinator or decider combinator , take care to connect the wire to the correct input or output side. Use "Show details" mode to see the orientation of the combinator.
- Hovering the mouse cursor over an item will highlight all wires which connect to the item.
- Hovering the mouse cursor over a power pole which is part of a network will display the signals on its network. Some items like combinators will also display their input and output signals when hovered over.
- Cut-pasting entities tries to preserve all wire connections to external entities and reconnect the new ghost to all its previous connection points, even when pasted multiple times, making it easy to rearrange entities without breaking connections.
- Deconstructing a power pole tries to keep all affected wire connections intact, forming new wires between previously-connected entities as needed. This can result in redundant wire connections forming when cut-pasting or undoing deconstruction. Note that this doesn't happen when the power pole is destroyed, though its ghost remains connected.

## Combinators

Combinators can function as both receiving and sending devices and allow more advanced functions to be used on a circuit network.

- The constant combinator broadcasts up to 20 values on any of the channels for whatever networks it is connected to.  (You cannot currently specify whether a value should be on the red or green channel; if you need different values, use two combinators, one for each color wire.)  You can use any item channel or any of the virtual signal channels. Note that using two of the 20 slots to broadcast values on the same channel is the same as broadcasting the sum of the two values from one slot.
- The arithmetic combinator performs arithmetic operations on input values and broadcasts the result to the specified output channel.  The input and output channels can be any item channel or any of the virtual signal channels. Connecting: The arithmetic combinator connects to a red or green network on its input side (the terminals are set into the main body and look like spark plugs) and performs an arithmetic calculation which is broadcast into the specified channel on its output side (the output wires appear to stretch out a bit from the body of the device). Feedback: Note that the input network and the output network are not the same network .  Connecting the output network back to the input network will result in a feedback loop.  For example, adding 1 to the value for copper plates and broadcasting it as copper plates is an action that results in an infinite loop if output is connected back to input.  The value for copper plates will rapidly (but not instantly) shoot upward. (The rate at which it climbs is determined by the current tick rate.) This technique can be combined with decider combinator logic to make electronic clocks, gates, and other systems; see Combinator Tutorial for advanced techniques. Each:  This combinator can use the 'Each' signal for both input and output, in which case all non-zero input channels will have the combinator's operation performed and broadcast on the output side.  Having Each signals for input and output and using a non-changing operation (like adding zero) is equivalent to having a 'one-way' wire; all the information from the input network is copied to the output network, but the reverse is not true. Multi-network: The arithmetic combinator can be joined to both red and green networks on the input side and will sum their inputs.
- The decider combinator functions much like an arithmetic combinator, but is designed to compare values. Essentially, it is a conditional. In terms of connecting, feedback, and the Each signal it functions as specified above.  In addition, it can handle the Everything and Anything signals, and performs more complex functions than summing when attached to multiple networks.  See the decider combinator page for more details on how to use this.
- The selector combinator has various functions designed for filtering out and analyzing specific signals from its inputs. It is able to output the largest or smallest signal in a series of inputs, output the stack size of items, count the number of inputs, and output a random input every certain number of game ticks. If Space Age is enabled, it has three more functions for detecting an item's rocket capacity, and filtering/transferring quality grades.

## Virtual signals

Virtual signals are special signals that do not correspond to game items or fluids. Other than the three logic signals, virtual signals do not behave differently from item signals.

There are 177 virtual signals available (or 241 in Space Age ) split between the Signals, Enemies, Environment, and Unsorted tabs. These include but are not limited to, numbers, letters, various lines & arrows, information icons, every enemy variant, environmental features, and the signal for the planet Nauvis .

Additionally, if the "Show parameters in selection lists" option is enabled under game Settings > Interface > Interaction, the Unsorted tab receives 10 special purple "parameter" icons which can be used for blueprint parameterisation .

### Logic signals

Three of the virtual signals cannot be sent over a network but apply special logic to multiple signals.

#### Everything

Everything can be used on the left side in conditionals. The condition will be true when the condition is true for each input signal. The condition is also true if there are no signals. This means that the everything signal behaves as universal quantification . A signal is present if it is nonzero, so "Everything ≠ 0" is always true.

If a signal (rather than a constant number) is used on the right side of the comparison with everything , it is implicitly excluded from the set of signals that everything checks, so the signal is not matched against itself. That means it is meaningful to test e.g. everything > X , without getting a trivially false result on X > X .

The output of a decider combinator may also use everything , unless the input is set to each . When used, the combinator will output a signal on every channel with non-zero input as long as the condition is true; the value will either be the input value or 1, depending on the corresponding setting.

#### Anything

Anything can be used on the left side of conditions. It will be false when there are no inputs. The condition will be true when the condition is true for at least one signal. This means the anything signal behaves as existential quantification . A signal is present if it is nonzero, so "Anything = 0" is always false.

If a signal (rather than a constant number) is used on the right side of the comparison with anything , it is implicitly excluded from the set of signals that anything checks, so the signal is not matched against itself. That means it is meaningful to test e.g. anything >= X , without getting a trivially true result on X >= X .

When used in both the input and output of a decider combinator, anything will return the first matching signal following the order of precendence as they appear in Factoriopedia, wooden chest being first in line.

#### Each

Each can only be used in left input side and output of decider and arithmetic combinators. The signal can only be used as an output when also used as an input. When used in both the input and output, it makes a combinator perform its action on each input signal individually. The combinator will output the sum of each of the actions if only used in the input.

A combinator using each is like a stack of combinators with all inputs connected and all outputs connected in parallel. For example, if there are signals "copper plate" and "iron plate" present, one combinator would be evaluating conditions for copper, and the other combinator would be evaluating conditions for iron. The different output signals would then be added together on the shared wire.

Unlike everything and anything above, if a signal is used on the right hand side of an each operation, it is not implicitly excluded. So if you have e.g. each * X then you will also get X multiplied with itself in the output.

Each as an input will only be processed on signals that have a non-zero value. If you have a decider condition that inputs and output each, but wants to output only one value for an input signal that passes the condition, it will never output 1 for a signal which has a zero value, even if the condition is one that would be passed for a zero value.

## Tutorials

- Tutorial:Circuit network cookbook - Example-heavy tutorials; for beginners who want to get to know and use the benefits of the circuit network.
- Tutorial:Combinator tutorial - Mainly textual and detailed tutorials.

## Logistic network

The logistic network used by logistic robots is essentially a third network (a wireless one), along with the green and red wired networks. The logistic network is based on coverage by roboports .

Some devices can also be connected to the logistic network and enabled based on a condition. If a device has conditions set for circuit and for logistic network, it will become activated if both conditions are true. Devices that can also be controlled with the logistic network:

- Agricultural tower
- Crafting machines
- Inserters
- Lamp
- Mining drills
- Offshore pump
- Power switch
- Pump
- Pumpjack
- Train stop
- Transport belts
- Turrets

See the logistic network and roboport articles for more information.

## History

- 2.0.67 : Splitters can be connected to circuit network.

- 2.0.35 : Furnaces can be connected to circuit network.

- 2.0.34 : Extended the virtual signals, and unified/changed graphics of some of the existing ones.

- 2.0.7 : Added selector combinator. It allows to select one of the signals, or the signal count from an input. Added display panel. 1X1 entity which can show specified icon and/or text, possibly also on the map. It can be also controlled by the circuit network. Added editable description to combinator entities. Decider Combinators are now allowed to check multiple conditions and send multiple outputs per combinator. Radar can now be connected to circuit network, allowing to wirelessly transmit a single channel of red and green signals on each planet/surface. All turrets (including artillery) can now be connected to the circuit network to read their current ammo count and/or deactivate them. Assembling machines, chemical plants, oil refineries and centrifuges can now send the ingredient list of their recipes to the circuit network.

- 0.15.0 : Significantly improved circuit network performance. Up to 25 times less CPU usage and 10% less memory usage. Added the Programmable Speaker: it shows alerts and plays sounds based on circuit network signals. It can be used to make simple songs. Train Stop can output the contents of the stopped train's cargo. Train Stop can be disabled using the circuit network. Trains will skip disabled Train Stops, allowing simple train control. Mining Drills can be turned on and off using the circuit network. They can also output the remaining expected resources. Pumpjacks can be turned on and off using the circuit network. They can also output the current oil mining rate. Added Modulo, Power, Left Bit Shift, Right Bit Shift, Bitwise AND, Bitwise OR and Bitwise XOR to the Arithmetic Combinator. Added additional operators to the Decider Combinator and Circuit Conditions.

- 0.13.0 : Many machines are now connectible to the circuit network. Wire disconnecting is incorporated into the latency hiding. Wires are now highlighted on entity mouseover. Reduced memory usage of circuit network.

- 0.12.33 : Fluid values are rounded to the closest value instead of rounding down when transmitted to circuit network.

- 0.12.1 : One can copy paste circuit network conditions between the inserter , lamp , pump and offshore pump .

- 0.12.0 : Improvements to circuit network connection, one can connect multiple wires of the same color to the same entity. The lamp , storage tank , pump and offshore pump can be connected to the circuit network.

- 0.10.0 : Blueprints copy circuit network connections.

- 0.8.3 : Circuit network contents info has colored slots to specify the network it represents.

- 0.1.0 : Introduced
