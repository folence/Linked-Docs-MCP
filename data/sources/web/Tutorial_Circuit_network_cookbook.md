---
title: Tutorial:Circuit network cookbook - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Circuit_network_cookbook
scraped_at: 2025-10-21 14:29:50
tags: [web, documentation]
---

# Tutorial:Circuit network cookbook - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Circuit_network_cookbook](https://wiki.factorio.com/Tutorial:Circuit_network_cookbook)


|  |
| Page "Circuit network cookbook" has been recommended for clean-up. Reason: Combinator GUI and circuit network changed in 2.0 |
| This may mean fixing grammar or broken links, providing better explanations, or removing incorrect/outdated info. |
| Further recommendations for this page's clean-up can be made at Tutorial talk:Circuit network cookbook . |

This is a beginners tutorial. See also the Circuit network page for an overview over the circuit network and the Tutorial:Combinator tutorial for an advanced tutorial.

## Contents

- 1 Foreword
- 2 Lights 2.1 Lamp showing chest content condition 2.1.1 Setting up circuit connection 2.1.2 To set the light condition 2.2 Conditional Lights 2.3 Colored Lights
- 3 Oil Setups 3.1 Light Oil Cracking 3.2 Heavy Oil Cracking 3.3 Alternative Setup for Cracking and Lubricant Production
- 4 Misc 4.1 Multiple Storages 4.2 Constant Combinator 4.3 Constant Combinator Signs (Words) 4.4 Constant Combinator Signs (Managing Belts) 4.5 Memory Cell / Counter
- 5 Inserters 5.1 Limit items placed into a chest 5.2 Balanced chest insert 5.3 Keeping outpost stocked with specified items 5.4 Balanced Solar panel / Accumulator Production
- 6 Sushi Belts 6.1 Reading Belt Design 6.2 Memory Cell Design
- 7 Power 7.1 Backup steam power 7.2 Optimal usage of fuel for nuclear power 7.3 Prioritize usage of uranium towards nuclear fuel production
- 8 Railway network 8.1 Set train routing 8.2 Player safety
- 9 Latches 9.1 RS latch - single decider version 9.2 SR latch 9.3 Backup steam example 9.4 Belt only latch
- 10 Displays 10.1 Numerical Display 10.2 Black and White Grid Display 10.3 Multicolor Display by DaveMcW
- 11 Setting Recipes 11.1 Multiple Item Assembling Machine
- 12 Signal Switch 12.1 Simple Signal Switch 12.2 Latching Signal Switch
- 13 See Also

## Foreword

This page provides examples of simple circuit network designs and some not so simple designs that others can use, combine and modify. They are designed to be as easy to understand as possible.  To see the settings of combinators without opening them, the option "Show combinator settings in "Alt-mode"" in the Interface/Alt-mode settings has to be checked and "Alt-mode" has to be turned on.

## Lights

### Lamp showing chest content condition

This is one of the simplest possible use of circuit-network. A lamp is light depending on the number of goods (in this example empty barrels) in a chest.

#### Setting up circuit connection

- The lamp is connected to the chest.
- The lamp is set to light if the chest contain less than 10 empty barrels.

#### To set the light condition

- Open the lamp (left click on it).
- Set the input to barrels.
- Set the operator to < (less than).
- Set the constant number: Left click on the constant number Move the slider until 10 is shown, or edit the value box directly. Press set.

Depending on the condition you set, the lamp may light if the chest is empty, or if it contains the required quantity of items.

The drawback with this scenario is that the lamp has a white light , and is therefore difficult to differentiate from an ordinary lamp at night.

### Conditional Lights

- In this circuit we connect a series of lamps to a storage tank .
- By setting different conditions on each lamp we can build an indicator strip.
- The Enabled condition of the first lamp is Petroleum gas > 100 .
- The others light up when gas is greater than 200, 300, 400 and 500 respectively.

In this setup you can connect the storage tank to the lamps directly.

### Colored Lights

To light a lamp with a color rather than white, you need an intermediate device like an arithmetic combinator that can send a color signal.  
Instead of directly connect the lamp and the Storage tank you need:

- Add the arithmetic combinator.
- Connect the storage tank with the input of the  arithmetic combinator.
- Connect the  output of the arithmetic combinator with the lamp.
- Set up the arithmetic combinator: Setting the input to petroleum Gas + 0 (the constant 0 not the signal 0) Set the output to the pink signal (on the bottom row of the last tab of signals.)
- Set up the lamp : Select the "Use colors" check box on the lamp. Set the condition to the pink signal, and what value you want (i.e. > 100)

## Oil Setups

Balancing the production of petroleum gas, light oil and heavy oil is one of the most important use cases of the circuit network.

### Light Oil Cracking

- This circuit provides balanced light oil and petroleum gas production by cracking excess light oil into gas.
- The pump is connected to the storage tank by a red wire .
- The pump has an enabled condition set to Light Oil > 20000 .

### Heavy Oil Cracking

- This circuit extends on the previous circuit by adding optional heavy oil cracking to provide lubricant etc.
- The pump has an enabled condition set to Heavy oil > 20000 .

### Alternative Setup for Cracking and Lubricant Production

This setup compares different fluid levels to each other instead of checking fixed values. It offers some guarantees such as petroleum gas being produced when you have light oil to spare, and light oil not being cracked when you have plenty of petroleum gas, and similar rules for heavy oil cracking and lubricant production.

It takes 4 steps:

- Have a fluid tank for heavy oil, light oil, petroleum gas, and lubricant. For each fluid, make sure to connect the tank via pipes to every location where the fluid is being produced or consumed.
- For each chemical plant (or each row of them, if you use rows) add a pump to the non-water fluid input pipe to make it possible to block the flow. Note: Alternatively, the blocking pumps could be added to the chemical plant output pipes, but there is no need to add pumps to both inputs and outputs.
- Connect every pump and every fluid tank to a single circuit network of red (or green) wire. The resulting circuit network will know about the fluid level in every storage tank and pass this information to every pump.
- For each connected pump set the circuit “enable condition” to "[input fluid] > [output fluid]" , for its respective chemical plant recipe. E.g. set "heavy oil > light oil" for the heavy oil cracking input pump, set "heavy oil > lubricant" for the lubricant production input pump, and set "light oil > petroleum gas" for the light oil cracking input pump.

Done! Now all the pumps will move to equalize the fluid levels to each other. This will prevent fluid system deadlocks where you have plenty of one fluid but you are unable to make any of the other.

## Misc

### Multiple Storages

- If you connect multiple chests to a pole, the pole displays the sum of items in all the chests.
- This also works with storage tanks and roboports .

### Constant Combinator

- With a constant combinator you can generate any signals you may need.
- In this example we have generated a signal of 50 Laser turrets and 200 Piercing round magazine.
- Constant combinators are not of much use on their own but we shall use them later.

### Constant Combinator Signs (Words)

- You can use constant combinators to make signs, just set the letter signals in the combinator, each combinator can display 2 characters side by side.
- Note that to see these letters, Alt-mode must be on and the Interface setting “Show combinator settings in “Alt-Mode”” must also be enabled.
- As of the 2.0 update, these signs have become obsolete due to the addition of Display panels , as text on display panels is always visible.

### Constant Combinator Signs (Managing Belts)

- Somewhat similar to the previous example, constant combinator signals can be used with belts to help indicate what items should be on which belts. This is extremely useful when sharing blueprints, as it's possible for blueprints to be shared albeit with no indication on which items are meant for which belts.
- Note again that Display panels are more useful here as of the 2.0 update.

### Memory Cell / Counter

- Basic memory cell that counts all the items moved by the inserter
- The fast inserter is connected to BOTH ends of the arithmetic combinator.
- If the fast inserter hasn't picked anything up this tick the input to the Arithmetic combinator is the same as and output and hence the values are persisted.
- When the fast inserter does pick something up its value is added to the output from the previous tick thus incrementing that item.

## Inserters

### Limit items placed into a chest

- The inserter is connected to the wooden chest using a red wire .
- The inserter's enabled condition is Advanced Circuit < 10 .
- In reality this means the inserter may place more than 10 Advanced circuits in the chest because it could pick up to 3 at once due to stack size bonuses.
- This effect can be even greater with Stack inserters because of their large carrying capacity.
- This technique still gives far greater control than limiting the inventory on the chest.

### Balanced chest insert

Goal: Load n chests with approximately the same number of items. This can be used for train stations: MadZuri's smart loading train station

- Place n chests and n inserters.
- Place 1 arithmetic combinator
- Set the combinator to take Each (yellow star) and divide by the negative number of chests. ie −n.
- Connect all chests to each other and to the input of the combinator using red wire.
- Connect all inserters to each other and to the output of the combinator using red wire.
- Connect each inserter to the box it inserts into with green wire.
- Set the enable condition on each inserter to be Everything (red star) < 0.

The combinator calculates the average number of items in the chests, and makes it negative. Each inserter gets the amount in the chest it is inserting to and adds the negative average, i.e. it calculates how many more than the average it has in its chest. Thus if that number is negative, it has less than the average in the chest and it enables.

Due to inserter stack bonus the count is not exact. If a precise count is needed, set the inserter stack size to 1.

### Keeping outpost stocked with specified items

- This circuit keeps a storage chest at an outpost stocked with customized levels of different items.
- For example you could keep an outpost stocked with 50 laser turrets and 200 piercing magazine rounds but not have to worry about it being over filled.
- The storage chest is attached to the input of the arithmetic combinator (left side in the picture) with a red wire .
- Another couple of red wires join the output of the arithmetic combinator (right side) to the constant combinator and to the stack filter inserter .
- The arithmetic combinator multiplies each input value (from the storage chest) by -1 .
- Finally the filter stack inserter's mode of operation is set to Set filters .
- So the input to the stack filter inserter is <constant combinator> - <storage chest contents> and the filter is set to filter for the first item by inventory order.

### Balanced Solar panel / Accumulator Production

- This circuit balances production of solar panels and accumulators to a desired ratio in my case 24:20.
- The first arithmetic combinator takes the number of accumulators in the chest and multiplies it by 24 .
- The second arithmetic combinator takes the output of the first combinator and divides it by 20 .
- This gives us the number of accumulators that we can directly compare to the number of Solar panels in both inserters.
- If the number of accumulators is greater we enable the Solar panels inserter, if the number of Solar panels is greater we enable the accumulators inserter.
- However, if they are equal, neither machine does anything. So we add a single accumulator to one of the inserters using a constant combinator and a wire of the other color, therefore breaking the deadlock.

## Sushi Belts

### Reading Belt Design

- Six belts in a row are connected with Red wire and set to Read belts contents and Hold
- This red wire is then connected to the inserters that insert onto the belt.
- Read hand contents is unselected for all inserters.
- Mode of operation is set to Enable/Disable on all inserters.
- The first inserter is enabled when Automation science pack = 0
- The other inserters are set similarly for the other science packs.

### Memory Cell Design

- This recipe produces a rolling sum of the number of items of each type, as they added or removed from a looping conveyor belt. Inserters placing items onto the belt can use this sum to turn on or off as needed.
- It achieves this through two networks, one red (subtraction) and one green (addition), connected to their own inserters, and two arithmetic combinators: one basic arithmetic combinator to do the subtraction, and one memory cell, to update and persist the values.

- Each inserter that takes items from the belt is connected with Red wire. Each of these inserters is set to Mode of operation: None , Read hand contents is checked , and Hand read mode is set to Pulse (sends 1 each time an item is picked up).
- These red wire inserters are connected to the input of the subtraction arithmetic combinator, in this example, it is the one on the left.
- The left arithmetic combinator multiples each input by -1 and outputs it to each . This subtracts 1 each time an inserter removes an item from the belt, for the specific type of item taken.
- The right arithmetic combinator is the memory cell .
- The memory cell's input is connected to: 1. A green wire network of inserters placing items onto the belt (the addition), 2. The output of the left arithmetic combinator (the subtraction).
- The memory cell's output should be connected to its input, so that each time an update is sent from either the addition network (green wire) or subtraction network (red wire), the updated value is persisted.
- When a Green wire inserter adds an item to the belt, that item's count in the memory cell is increased by 1.
- The inserters that place items onto the belt (green wire) should be set to: Enable/disable , Read hand contents is checked and Hand read mode is set to Pulse .
- The Enable/disable condition is set based on the number of items you'd like picked up by the red wire inserters, e.g. Automation science pack <= 16 (one pack for each lab in the example shown here).

## Power

### Backup steam power

- The steam engines are not directly connected to the power network. They are connected to the power network through a power switch .
- The power switch is connected to one of the accumulators in the main network.
- The power switch turns on when A < 10. That is when the accumulators are less than 10% full.

### Optimal usage of fuel for nuclear power

Unlike the normal steam power that adjusts fuel usage based on power usage, the nuclear reactors spend fuel in fixed units of time. To be exact, the consumption of 1 fuel cell takes exactly 200 seconds.

Combined with the fact that creating the nuclear fuel cells are time consuming and expensive to create, it is therefore beneficial to optimize their use to match the actual consumed power.

This picture shows a setup with 4 reactors, that spend only 1 fuel cell each whenever steam runs low. Note: The GUI in the image above has been altered to make sure all important info fits within the image size.

There are a few elements in this setup:

- Storage tank that provides the steam signal.  You should only read from one storage tank, and it should have pipe connections to all your other steam storage tanks.
- Chests containing uranium fuel cells for the reactor.
- Output inserter that takes empty fuel cells from the reactor. This is connected to the storage tank to listen for the steam signal, and to the chests to listen for the uranium fuel cell signal. If the steam level is low and there are uranium fuel cells available, it removes the empty fuel cells from the reactor and sends an empty fuel cell signal (since "Read hand contents" is checked).
- Input inserter that put uranium fuel cells into the reactor. This is connected to the output inserter and listens for the empty fuel cell signal. The "Override stack size" is set to 1, so that it only inserts 1 fuel cell at a time.
- If you are using multiple reactors you should only wire one output inserter to one steam tank, and then connect all input inserters to the single output inserter. This will synchronize fuel insertion to maximize the reactor neighbour heat bonus. The other reactors can have "dumb" output inserters that remove empty fuel cells immediately.

Since this design uses empty fuel cells as a signal to fill the reactor, you need to manually insert 1 uranium fuel cell into the reactor to get it started.

### Prioritize usage of uranium towards nuclear fuel production

Because a continuous supply of uranium fuel cells is critical to maintaining a nuclear reactor , the circuit network can be used to set up a system where uranium-235 and uranium-238 are conserved for the production of nuclear fuel before other uses.

Using a splitter , divert the two types of uranium onto two parallel conveyors, with an inserter positioned to gather uranium from each conveyor (a long-handed inserter will be needed for the far belt). Each of these inserters deposits their load into a container, from which two more inserters deliver the contents to an assembling machine making nuclear fuel. An inserter delivers the produced fuel to a third container, from which inserter(s) delivers the fuel to your nuclear reactor. Wire the two inserters gathering from the conveyors to the container each of them is delivering to, and to the tile of conveyor immediately after the tile the inserter is gathering from. Set each inserter's enable condition to "less than or equal to X amount of uranium", using the appropriate type of uranium the inserter is gathering and X being the number of reserve uranium desired (optimally, one uranium-235 and nineteen uranium-238, the amount needed to produce nuclear fuel; the amount may be increased if a greater stockpile is desired). Set each conveyor's enable condition to "greater than or equal to X amount of uranium" in the same manner. Finally, connect the inserters delivering uranium to the assembly machine up to the container the assembly machine is delivering nuclear fuel to, and set each of their enable conditions to "nuclear fuel = 0 (the enable condition can be set to "less than or equal to X amount of nuclear fuel" if a larger stockpile is desired).

This set-up accomplishes the following:

- When there is sufficient nuclear fuel and uranium stockpiled, the inserters will deactivate and the conveyors activate, allowing the uranium to continue down the conveyors to other facilities.
- When the nuclear fuel stockpile hits zero (or decreases below the desired amount), the inserters delivering to the assembly machine will activate and deliver uranium to resume production of nuclear fuel until quota is reached again.
- When there is not enough uranium stockpiled to produce a batch of nuclear fuel, the inserters gathering uranium will activate and and resume gathering uranium until they reach their quota. The conveyors carrying uranium will stop past the inserters, cutting off other facilities from that type of uranium until its respective inserter reaches quota.
- The assembly machine will only be provided with uranium when the stockpile of nuclear fuel hits zero (or decreases below the desired amount), preventing over-production of nuclear fuel and thus over-consumption of uranium.

## Railway network

### Set train routing

The circuit network can be used to allow deeper micromanagement of trains . Circuits can be used to adjust train limits for stops , effectively disabling a stop when a resource is not available for loading, or if an unloading station already has more than enough of a resource. Note that adjusting train limits runs into fewer problems than fully enabling/disabling stops; see Friday Facts #361 - Train stop limit, Tips and tricks and the Train stop page for additional information about using train limits.

### Player safety

The circuit network can be used to ensure the player's safety when crossing train tracks so they do not get hit. Place gates at designated crossing areas and connect an adjacent wall to rail signals near the gate. Set the gate to "read sensor" and the signal to "close signal" with the condition being the signal the gate sends out being "1". This means that when the gate is closed, the signal will be green and trains can pass freely, but when the player approaches the gate and it opens for them, the train signal will be turned red and trains will be stopped until the player clears the area.

Alternatively, this system can be reversed - by setting the gate to "open gate" and the train signal set to "read signal", the gate will remain open normally and will close when a train is approaching, preventing the player from crossing until it is safe.

In lieu of gates, the player can connect a programmable speaker to the train signals to broadcast a warning siren when a train is approaching the area.

## Latches

### RS latch - single decider version

This discussion on the Factorio forums starts with the common 2 decider RS latch version, but later a single decider version was proposed . The thread goes on to explain why this is better. In the thread, the latch is described as an SR latch. However, when both inputs are true, the latch will reset, so it is an RS latch.

### SR latch

In 2.0, an SR latch can be accomplished in a single decider combinator with many combinations of set and reset conditions. This latch, for example will set if the steam levels or the accumulator levels fall too low, and will reset when both levels recover. This is an SR latch; if both inputs are true, the latch will set.

### Backup steam example

This example will turn on the steam generator when the Accumulator charge drops to 20%, but will "latch" (remember) the On state until the accumulator is charged to 90%.

Latching is used to introduce hysteresis and avoid the power switch rapidly cycling on and off (as the accumulator falls to 19%, charges to 20%, falls to 19% and so on).

0eNqllMmO2zAMht+FZ2UQx0trHwr0GXoMAkO2mRkBWgwtyQSB330oJXGKxmg604tNUdQnkr+kM3Qy4GiF9tCcQfRGO2i2Z3DiVXMZfZorhAacR65WqF+FRpgYCD3gOzTZtGOA2gsv8LIyDU6tDqpDSwHsRlA4iEAIib23ol+NRiIwGI2jxUbHvQhY5C8lgxMZ9Us5TewBuPkksMyeAPMZ6BSX8inv+xNeMfN43wcVJPfGLhRaJ0qZUTOp7d4a2Xb4xg+CoinEBD8G396F8KcxQg/C+kCee9YpYvUTpqVsyjluwF4MaFe9UZ3Qy0mV+TUpKo3BICy1Is0Wy0lemS3NDYnjovf3EZ2IvbDuc4WkzZzn8VRu1rGq/2PUX2H8ujDUyG1qVgM/4ObA9rqY6wHiFbio9efd+bcdxhP1L2jf7q1RrdAEgmbPpcNpt6hpNYNGcyRF3VH4/m1BzervR6wXtg/Ct6h5J3GAxtuAbHbPMsbYrzXvJsD6oZNUF1zybinG463ix2q/scU36KHaan29mAunN0p0pHEUaJuxkm1YuWNb+rIqWXmyKrIKFuczslIUK5JV0OxmRxThUVEq92eTwQGtS9uU1aYu6pp+eZ1X+TR9AMRRzM0=

Accumulator outputs the current charge level as % on signal

The decider sets and latches the Set signal when the accumulator falls below 20%, and unlatches when the accumulator reaches 90%.

The Power switch isolates the generator from the rest of the factory until = 1

### Belt only latch

- To make it work, 3 pieces of raw wood must be placed on the inside lane of the belt.
- It will have higher latency than the combinator version, but in most situations you will not notice the difference.

## Displays

### Numerical Display

- Each digit is driven by its own green wire , that wire holds 15 signals, one for each lamp used in the digit.
- constant combinators are used to define which lamp should light up for each value.

### Black and White Grid Display

- Each row has its own red wire connection and within that row each light has a numbered signal 0-9.
- We turn each light on by just setting or clearing the relevant signal.

### Multicolor Display by DaveMcW

- To understand how this works, you first need to understand how color lights choose which color to light up when there are multiple colored signals.
- The lamp will light up with the colored signal that is greater than zero and earliest in this list: red, green, blue, yellow, pink, cyan, white.
- We have a red wire per column, that wire has each of the colored signals on it at different values and a numbered signal for each row.
- There is a arithmetic combinator for each cell that subtracts the "row" value from each of the colored signals.
- And this enables us to choose the color for each cell.
- Simple!

## Setting Recipes

### Multiple Item Assembling Machine

- This Version 2 circuit design allows a user to have a single assembling machine produce several different items that all use mostly the same ingredients. This is a convenient way to avoid routing the same set of inputs to multiple assembly machines for items that need automated, but not constant production. For example, medium electric poles and big electric poles share the same ingredients, or the pumpjack , oil refinery , and chemical plant take mostly the same inputs.
- To use this, the player opens the constant combinator and selects which items and what quantities to make.
- This signal goes into the green wire input of the decider combinator , where it is compared to the quantity of items in the logistics chest connected to the combinator input on the red wire.
- The decider combinator uses the "each" signal, so each signal on the green wire is compared to each signal on the red wire, and if there are fewer of any item in the chest than are set by the constant combinator, the decider combinator will output a signal on that item's channel.
- The assembling machine then is configured to set the recipe based on incoming signals and so will produce whatever items are needed to fulfill the settings on the constant combinator.
- The assembly machine outputs items to the steel chest, which then loads them into the requester chest, which feeds back into the assembly machine. This is because when a new recipe is loaded, any extra input items of the previous recipe must be unloaded from the machine, and this loop will supply those unloaded items back into the assembly machine, otherwise input materials will fill up the output storage, preventing new items from being produced.

## Signal Switch

### Simple Signal Switch

- With the advent of complex conditionals, it is possible to have a single constant combinator + decider combinator output any arbitrary signal from any conditional block
- This relies the behavior of the each signal.  If the each signal is used in an input condition, then it can be used as the output signal as well.
- To start, we'll define all of the signals we may want to output in the constant combinator, and give them each a unique value.  If circumstances dictate that you cannot dedicate one of the decider's input wires to just the constant combinator, you may want to make the values negative and/or very large to ensure they stay unique.
- We can exploit the behavior of each to propagate any of our constant combinator signals when any arbitrary condition is true.
- The format is simple: Define the condition in which you want your signal sent, and then add `AND` each = `the signal in the constant combinator you want to send when that condition is true`.
- The condition can be simple, using only a single condition, or can have as many AND statements as you need.
- Because the each statement is only true - due to our constant combinator signals all having unique values - when each compares a signal to itself, and because we are using each as our output value, whenever the other conditions in each block are all true, the signal that is compared to each is sent as the output signal, as it is the only signal that passes that particular condition.
- In the example shown, the decider will output the "pipe" signal when there are fewer than 100 pipes in the chest. It will output the "underground pipe" signal when there are 100 or more pipes AND less than 100 underground pipes in the chest.
- It is important to set the each comparisons to use only the wire connected to the constant combinator, otherwise any other signals that share the same values might get passed through.

### Latching Signal Switch

- This type of circuit expands on the simple signal switch by making the decider act as an SR (set/reset) latch as well as a signal switch.
- Adding latching helps prevent machines from flickering on and off, and recipes from switching wildly due to changing conditions.
- For this, the decider's output is connected to its input via the wire NOT connected to the constant combinator. This allows us to use the decider's current output as part of our logic.
- Each separate recipe needs two blocks: the "set" conditions, or "when do we turn the latch on," and the "reset" conditions, or "when do we turn the latch off."
- For the example shown here, the latch for advanced metallic asteroid processing is set when there is less than 80 copper ore on the output belts ( < 80).
- The second group of conditionals keeps the latch on until the reset condition - ≥ 300 - is reached. Because the set condition makes the decider start outputting the signal, then that makes the second block of conditionals true until reaches 300.  Once there are 300 copper ore on the belt, neither of the conditions will be true, and the latch will reset .
- The next two blocks are a latch for basic metallic asteroid processing. In this case, the set condition is < 120 AND = 0. The check for ensures that we do not have both latches on at once. It's up to you to define the priority of possible output signals by adding similar checks. So for basic processing, the latch can be reset by two things: either reaching 500+, or by the latch turning on.
- Pay close attention to which wires you're using for each condition. Always be as restrictive as possible.

## See Also

- Arithmetic combinator
- Constant combinator
- Decider combinator
- Circuit network
