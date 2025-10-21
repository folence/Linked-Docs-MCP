---
title: Tutorial:Combinator tutorial - Factorio Wiki
source: https://wiki.factorio.com/Tutorial:Combinator_tutorial
scraped_at: 2025-10-21 14:29:49
tags: [web, documentation]
---

# Tutorial:Combinator tutorial - Factorio Wiki

**Source:** [https://wiki.factorio.com/Tutorial:Combinator_tutorial](https://wiki.factorio.com/Tutorial:Combinator_tutorial)

This is an advanced tutorial. Beginners should refer to the Tutorial:Circuit network cookbook for examples and the Circuit network page for an overview over the circuit network. This tutorial assumes a basic understanding of circuits and covers more advanced topics like SR latches, memory cells and clocks.

## Contents

- 1 Introduction
- 2 Virtual signals 2.1 Logic signals 2.1.1 Everything wildcard 2.1.2 Anything wildcard 2.1.3 Each wildcard
- 3 Input insulator & gate
- 4 Set/Reset latching switch
- 5 Basic memory
- 6 Basic clocks
- 7 Pulse generators
- 8 Edge detectors
- 9 Counter
- 10 Memory cells 10.1 Simple latch 10.2 Positive cell 10.3 Positives and negatives cell
- 11 Multiplier and Dictionaries/Arrays
- 12 See Also

## Introduction

Combinator logic is achieved by cross-connecting outputs to inputs in such a way to achieve the desired logic. While advanced logic requires a multitude of combinators, some very useful basic logic can be achieved using only a handful of combinators. Combinator logic works because Factorio only updates at 60 times per second . Logically, each update tick is separated into two steps. In the first step, all combinators first read the input from the connected network(s), perform their computations. This produces an output value for every combinator. The tick update concludes with the second step, where the values of each network will be updated as the sum of all connected values.

When logic values are computed by combinators, the outputs are not recognized by the circuit network until the following step. So when a decider combinator is used to detect a certain input condition, its output value will not take effect on the circuit network until the next step. This behavior is important to remember and can result in sequencing errors and significant delays when multiple combinators are connected in series.

Circuit wires act like a wire bus in electronics; they carry information in the connected wires, meaning that if there are similar signals on a wire it will add them automatically. If the signal is different, it will be carried in that wire as well, but as a different signal.

When cross-connecting combinators, it is good practice to use the unused color to cross-connect, this will split the input and output networks and prevent unwanted inputs from accidentally connecting to a larger circuit network. Combinators will sum the red and green inputs prior to calculation, so either color can be used when wiring the output back to the input. In most cases however, it is more useful to use the opposing color of the wire so that it will not interfere with the resulting output and input.

When trying to understand combinators, your best friend is the in-game editor. You can pause the game and, with the "Tick once" keybinding, inspect nodes and networks as they go through different states.

## Virtual signals

In addition to the standard item signals, Factorio's circuit network also includes a set of signals that do not represent any particular game item. Instead, these virtual signals serve as user-definable channels for the circuit network; they hold whatever meaning the user wants them to. There are currently 102 virtual signals that can be sent over the circuit network (or 172 in Space Age ), split between the Signals, Enemies, Environment, and Unsorted tabs. They include but are not limited to:

- The 36 alphanumeric characters (A-Z, 0-9)
- 9 colors: red, green, blue, yellow, magenta, cyan, white, grey, and black
- 25 icons: several crosses, lines, and arrows
- All enemy varieties
- All environmental objects (trees, rocks, the player, and cliffs)
- The two wires, and spidertron, discharge, and artillery remotes

### Logic signals

There are three additional virtual signals known as logic signals . Unlike other signals, they cannot be sent over the circuit network; instead, they apply additional logic to combinators that modify their behavior. Specifically, these logic symbols act as wildcards, which are special signals that represent zero or more arbitrary signals instead of representing a single discrete signal.  Factorio's circuit network implements three types of wildcards.

#### Everything wildcard

The Everything wildcard is used with decider combinators. Its exact behavior depends on whether it is used as an input or an output:

- Input : Returns true if all input signals pass the condition, or if there are no input signals, otherwise it returns false.
- Output : Returns all non-zero input signals.

When used as an input, the everything wildcard can be thought of as a logical AND, or a universal quantifier . When used as an output, it acts as an 'echo' or 'dump' of input signals.

Note : Can be used as an output as long as the input is not an each wildcard.

#### Anything wildcard

The Anything wildcard is also used with decider combinators.

Given at least one input signal, it returns true if any input signal passes the condition. If no signal passes the condition, or there are no input signals, then it returns false. From this behavior, the anything wildcard can be thought of as a logical OR, or an existential quantifier .

When used in both the input and output of a decider combinator, anything will return one of the signals that matched.

#### Each wildcard

The Each wildcard is used with both decider combinators and arithmetic combinators , and behaves somewhat uniquely compared to the previous two. Generally speaking, it performs a combinator action on each signal individually , with the exact action depending on how it is used, and the type of combinator it is used in. It can be used as an input, and it can be used as an output, but only when it is used as input as well .

In a decider combinator , when used as an input, the each wildcard individually compares each input signal against the combinator condition, returning each signal that passes the condition. The manner that the each wildcard returns signals when used as input depends on whether or not it is also used as output:

- Input only : Sums each input signal that passed the condition, and depending on output settings returns either a count of the passed signals or a summation of their values as the desired output signal.
- Input and Output : Returns each signal that passed the condition, their values depending on the output settings.

In an arithmetic combinator , the designated arithmetic operation is applied individually to each input signal, and similar to the decider combinator, the signal that is returned depends on whether or not the each wildcard is used as output:

- Input only : The result of each operation on the input signals is summed and returned as the desired output signal.
- Input and Output : Each input signal is returned with the result of the specified operation applied to it.

The Each wildcard is therefore notably more complex than the other two wildcards, but offers a good deal of power in exchange for its complexity.

## Input insulator & gate

An arithmetic combinator set to (In: Each + 0, Out: Each) can be used to swap wire colors and as an insulator to prevent downstream logic from backfeeding into the circuit network's inputs.

A decider combinator set to (Out: Everything, Input-> Output) will also function as an insulator as long as the set logic condition is true. This can also selectively pass or 'gate' inputs only when desired. This could be used to sequentially poll remote train stations for their chest contents, and include only desired stations.

## Set/Reset latching switch

You want something to SET a trigger at some quantity, but then STAY on until that quantity hits some other value, the RESET value. You'll need one decider combinator and one arithmetic combinator. (Two decider combinators and a constant combinator can also be used for more complex multi-channel conditions.)

Setup the first decider combinator to the desired set conditional and to output a 1. Then connect the output to the input of an arithmetic combinator, and configure it to multiply by the bias value, which is the difference between the set and reset values, and wire the arithmetic output to the input of the decider. The arithmetic output channel must be set the same as the decider's input channel. Whenever the set conditional is reached, the decider will output a '1', and the bias of the arithmetic combinator will be applied. This will 'hold' the output true until the value goes back below the reset point.

In this specific example, the pump runs when light oil reaches 20000, and turns off when it reaches 5000:

A similar backup steam power example with detailed configuration and explanation can be found here: RS latch - single decider version

## Basic memory

A decider combinator can be used to store values, either for a counter or for more advanced logic (see below). The decider combinator is configured with

- input and output connected to the same network (typically each other),
- condition set to a signal > 0 for positive values or ≠ 0 to store both positive and negative values,
- output set to the input count of a specific input signal or .

As long as all inputs on the network are zero, it will hold the previously set value.

Remember the two step update process from above? If the network has value =5, the combinator will read this value from the network as its input, determine that it is > 0. It will then set the output to the input, which is =5. In the next step, the value of the network will be computed, which is the sum of all the connected outputs, which is =5, again.

A non-zero input held over time, e. g. the output of a constant combinator, will create a basic runaway clock. The stored value will be incremented by the sum of all connected input values every cycle. So e.g. with a constant combinator that produces =1 connected to the memory, the network will store the value 1 in the first tick, 2 in the second, etc., incrementing 60 times per second.

0eNqlU11rwzAM/C96TkuStWvqh8F+xyghH2orSOygyGWh5L/PjkcJJetW9hKQLd2d7pwrlI3FjkkLqCtQZXQP6uMKPZ100fgzGToEBSTYQgS6aH1VY0U18qoybUm6EMMwRkC6xk9QyRj9CuCJpNCyjJCOhwhQCwlh0DMVQ65tWyI7iodAEXSmd7NGe36Ht9sk620EA6jVNsvWW8fk5oRNk5d4Li7khlznkRpB/sGAC7FYd3JjDh2rd5jQrHcwiWcmHAKLxsor6T1U4j8nRtTzpah2G7te4sqSTKWfHr2Nd3unjxJYWPtu6Zo4qAmECxZ8w+burqab7iNxL/mfLcEL8iBn0qfgTUgIVOyLtit4kqvgzU0aK539B3Y35JP5+ZFNm5N2YKCELY7P2J/MvF6II53CTJ9Lzz3h6c2r2T8WgZPfhwCyZLPbp7vsdR+/xJtx/AJNbzZ8

Again, how does this work in detail? The network will start without any values set. As soon as the constant combinator becomes active, it will produce =1, and the decider combinator will produce 0 because no value is set yet. Step 2: The network will be set to the sum of all output, so =1. In the next update tick, the constant combinator produces =1 again, but now the decider sees =1, so it would also output [A]=1. Step 2: The network is set to the sum, which is =2. And so on.

Typically a constant combinator producing 1 will be used, but of course it could output other values, including negative values.
A negative value would decrease the stored value in the example below.
If the decider combinator uses > 0 as the condition, only positive values will be allowed, so the value will stop decreasing if 0 is reached.
If the condition is ≠ 0, negative values will also be allowed.

A single pulse of an input will cause a single increment by the pulsed value, creating a counter. In the following blueprint, place one item on the belt. Every time it is scanned by the connected belt, a pulse is generated that increments the stored value.

0eNqllMGO4jAMQP/F5zAqpaXQw/7IahWljQFLbVIlLtoK5d83aXdZEJ3DMBeQU+fFenZyg6YbcXBkGOobUGuNh/rnDTydjerSGk8DQg3E2IMAo/oUsVPGD9bxpsGOIQggo/E31NvwSwAaJiZcSHMwSTP2DbqY8BlDwGB93GZNOjWiqqL8KAVMUG/KQ/ZRhiBeaPl7tG2kCdDksF1S8hX27gvs/XOlT+xCQNTKznaywYu6knVpX0uuHYklGtV0KDX59A/1SXUexf2zQ6XlRRktEySWGK2yGx8y/q0vqb3VEZKF+VCz1ODTedv0c3aI5rEtpKEu/7NSGFsY1lwX7/l4cV2ssMs7W2NLGt2mtX1DRnGUtcI/fmo7X7f9F5tkabo7OZHzLF9m/UqOx7hyL2rJ2OAV3cQXMmdY/HpW6eJkKegH5eZya/gRd9qRh/Eb7GGKtY6G5cnZXpKJsKXx4Sut3T24Xml1HlstIP/uZOzfuoXVcf1OV2/N2Ux7moR9eormZ6t+eOUERNF+GZXDtqiOeXXYH7NdVoTwB9igtjA=

A stored value is cleared if the condition is no longer met, which makes the decider clear its output. This only works if the value is also not output elsewhere in the network. A stored value can also be reset to zero if a negative pulse equal to the input occurs. The latter can also happen while other inputs are still connected.

## Basic clocks

Clocks are constructed by having the output of a combinator tied back to its own input, such that every cycle advances its own count. Either the arithmetic combinator or the decider combinator can be used.

An arithmetic combinator tied to itself is fun to watch and will happily run-away, but requires additional control logic to reset.

With a single decider combinator, a self-resetting clock can be built. Wire output to input and configure with less than (<) with a specific number, and Input → Output. When a constant combinator is then connected to the input, every cycle it will count up by the output of the constant combinator until the number is reached. The decider will then clear its output, only the constant combinator will contribute to the value in the network, which resets the clock.

This means that the clock sequence will not include zero. It will begin at the value set in the constant combinator. Furthermore, it will include the number value that causes the conditional to become false. An arithmetic combinator can modify the clock sequence, but remember that its outputs will occur one cycle later than the clock cycle values.

The constant combinator can be dispensed with by adding the constant 1 as an additional output. Note that this version will set the signal value equal to the threshold for one tick, so with the same thresholds it will count for 1 more tick (analogous to the difference between 1-based and 0-based counting in computer programming). If the exact period is important, the threshold must be lowered by 1 (e.g. to repeat every second (60 ticks), the threshold must be 59).

A clock that only counts once can be built using the following setup. The clock can get reset by enabling and disabling the constant combinator that outputs .

0eNq1VdtugzAM/Rc/p1Wh9BZtPzHtaVOFKLidJUhQSKpVFf8+B6oK9QrT9oJI4hzb5xzDETa5w9KQsiCPQKlWFcjPI1S0U0nu9+yhRJBAFgsQoJLCrzJMKUMzSnWxIZVYbaAWQCrDb5BBLZ4C+EQ2UfY2QlivBaCyZAnbeprFIVau2KDhFI8qEVDqiq9q5dMz3GI2E3AAOZqtgvGM02RkMG0D5sLXYo3O4w1+JXtiAL51go35LGugKr+7JVPZ+Kq1PRnreOdcVBsxevctVegx+l/68Je4mzIxTTcSXjhGO1u6oalTXR64A6dsvDW6iEkxBshtkldYN+dKtTw03QX+YTDrEk68ijiSTOrINstGnJ1BVJeBfMKoYT+YgINr75QLacOHHrmh7WI8WN0t5RbNHac/Ecb5UQmWk47d13e4vElS0I+G6VAawjMNy9V/0vDWpaFLAr9Xsc/W+msAJT2dEf1y6K/5CP9x6E/8tJqBnFwM8+sfD7M1bsgsB31nedoR4PZH4MGoX3tcDFDeO8n/LGTn5yRgz05txVsG0WIVLpbz1WQ6ier6B+n0TYg=

## Pulse generators

Connecting an additional (=) decider combinator to the output of a basic clock will create a pulse generator, and will pulse a single output every time the clock cycles through the set condition. Any output value can be used, either directly from the clock sequence (input->output), a 1, or some value on a separate logic channel on the circuit network, such as set by a constant combinator. or by the circuit network.

- The value 1 can be written as any positive integer, so long as it is within the cap or ceiling of your timer.
- As an example from the above timer, this light will pulse every 1st tick after the timer reaches 30 ticks, making it pulse 1/30th of a second, as Factorio updates at 60 times per second.

## Edge detectors

The computation delay of combinators can be used to generate a one-tick pulse when a signal changes, e. g. from 0 to 1.

Connect an output of a combinator with red to the input, and with green to the output of an arithmetic combinator that multiplies by -1. When the red circuit changes a signal from 0 to 1, the arithmetic combinator gets input 1, but the output is still 0. So the green wire has value 1 for this one tick. In the next tick, the arithmetic combinator updates, so the output switches to -1. The green wire now has two inputs that cancel each other out. The same happens if the red input signal changes from 1 to 0, but in this case the green wire becomes -1 for one tick.

If you're only interested in generating a pulse if the signal changes from 0 to 1, a decider combinator set to >0 can be used to filter out the negative pulses. This mechanic can e. g. be used to count the numbers of trains that enter a station.

## Counter

A counter is used to count the number of input events, and output the sum of that count. Any pulsing input into a decider combinator configured input -> output and wired between output and input will create a counter, but this input must be zero at all other times or else the combinator will run away like a clock. A pulse generator is normally used to accomplish this. Combining several gating decider isolators set with sequential conditionals, a clock, and a pulse generator to the input of a counter will allow remote polling and counting of each isolator's contents.

## Memory cells

### Simple latch

When looping the combinator to itself, use a different color of wire from your main inputs or outputs.

Truth Table:

| Output 1 | Input 1 | Input 2 | Output 1 (t+1) |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 (2) |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 (2) |

Output 1 is the green wire loop seen in the picture, it carries the value to latch.

Input 1 is Set, while Input 2 is Reset.

### Positive cell

Cell for storing a positive value, with reset support:

Connect the desired value as signal I on the right side to set the memory cell and connect a negative value as signal I to reset the cell.

- The output of the memory cell is 2 mutually exclusive signals. In case input signal I > 0 then signal I is passed to the other side. In case input signal I is interrupted, then signal M is passed instead as a memory of previous input value.
- When input signal I is interrupted, it takes 2 ticks to switch to memory signal M.
- In case input I signal lasts only one tick then memory cell starts to cycle between the 2 previous values, tick by tick. Indefinitely.
- Switching is seamless, e.g. there are no ticks with empty signal.

### Positives and negatives cell

This cell can store negatives or positives. Reset is done on a dedicated line. Additionally, a 1-tick burst is handled properly. Forum post .

- The output M (memory) is the last non-zero input I (Input).
- A non zero R (reset) signal sets the output to zero.
- 1-tick bursts of R or I are handled properly.
- Negatives are handled properly.

## Multiplier and Dictionaries/Arrays

- Multiplying two signals together is simple and requires only a single combinator, however multiplying a set of signals is more complicated.
- A proof is shown below for the equation and why it works.
- A dictionary is a system that allows a value on a specific signal to be accessed. For example, A can contain many signals (either from a constant combinator or memory cell) and B can contain 1 of a specific signal (such as blue signal). What remains is the blue-signal value from A. This is because all the other signals are multiplied by 0.
- Arrays are similar to dictionaries, but instead of using a signal as a key, we use a number. Constant combinators are placed mapping each signal to a unique number (such as 1 yellow belt, 2 red belt, 3 blue belt, 4 burner inserter, etc). Then, use a combinator of "each = index OUTPUT 1 of each" and plug that in as the input to a dictionary.

```
((A+B)^2 - (A-B)^2)/4 = AB
   (A+B)^2 - (A-B)^2 = 4AB
   (A^2 + 2AB + B^2) - (A^2 - 2AB + B^2) = 4AB
   4AB = 4AB
```

## See Also

- Combinators 101 (Tutorial)
- Tutorial:Circuit network cookbook
- Circuit network
- Arithmetic combinator
- Constant combinator
- Decider combinator
