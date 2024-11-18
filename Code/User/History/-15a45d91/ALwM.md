# Big data and functional programming

## Data sets are distrusted

- When data volumes are too large, the data sets must be distrusted across more than one machine

- The solution to this is functional programming

## 3 main benefits of functional programming

### Statelessness

Nothing about a functional program relies on how often it is called, or in what order other functions are called.

This results in code being easier to write correctly, and it is easier for the programmer to understand and predict how the program will behave

### High-order functions

A function that takes one or more functions as input and or outputs a function.

Higher order functions are easily parallelized, meaning more than one core in the processor can work on different sets of the large data set simultaneously. This is more time efficient. 

### Immutable data structures

Objects in functional programming languages cannot be modified once they have been created. 

This allows parallel processing to be very easy, the same function will always return the same result and functions can be executed in any order. If the functions share parameters, the programmer doesn't need to worry about the parameter being altered due to the order of execution of the functions. 
