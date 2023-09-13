# Functional Programming (FP)

**DISCLAIMER**: This "article" is basically my notes as I've learned about FP, and might be helpful for people who are looking for a simple intro to the topic. If you want to learn FP in great detail, check out some of the resources I have linked throughout the file. Thanks!

<br>

# WHAT IS FP?

Functional programming is programming paradigm. Depending on your programming experience, you may not understand exactly what a *paradigm* is, so let's start there.

## 1.1 What's a Paradigm?

All computer programs can be classified by the *paradigms* they use. Paradigms are basically "the way we get work done". This includes the theoretical approach we take to solving problems and the tools we use when implementing our solution.

Now that we have a general understanding of what paradigms are, it's easy to view Functional Programming (FP) as just another programming paradigm. In fact, Dr. Kurt Nørmark lists FP as one of the four main programming paradigms of computer programming (see below).

## 1.2 The Big Four

Borrowing from Nørmark's [lecture notes](http://people.cs.aau.dk/~normark/prog3-03/html/notes/paradigms_themes-paradigm-overview-section.html), let's look at the "goals" of these four paradigms.

| Programming Paradigm 	| Goal / Approach                                                                                   	|
|----------------------	|---------------------------------------------------------------------------------------------------	|
| Functional           	| Evaluate an expression and use the resulting value for something                                  	|
| Imperative           	| First do this and next do that                                                                    	|
| Object-oriented      	| Send messages between objects to simulate the temporal evolution of a set of real world phenomena 	|
| Logic                	| Answer a question via search for a solution                                                       	|

Depending on your background, you have most likely worked with a combination of these paradigms (maybe without even knowing it).

## 1.3 The FP Paradigm

Since we are focusing on FP, let's take a better look at it's goal:

    Evaluate an expression and use the resulting value for something

If you haven't already guessed that *functional* programming has something to do with *functions*, I'd hope the above definition brought functions to your mind. Functions are really good at evaluating expressions and returning their value, so they are at the core of the FP paradigm.

The second "tenet" of FP is *immutability*. This goes hand-in-hand with using functions within our programs.

These two features of FP are explained below:

### 1.3.1 Pure Functions

Functions can be implementing in many programming paradigms, but FP focuses on using **pure functions**. Time for another definition, this time from [a nifty book about FP](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch03.html):

    A pure function is a function that, given the same input, will always return the same output and does not have any observable side effect. -

Okay...so pure functions should **(1)** return the same output for a given input, and **(2)** not cause any *side effects*.

Makes sense, but let's look at some simple examples to make sure we get it!

**Example of an impure function**

```python
>>> def x_plus_one():
        return x + 1

>>> x = 10
>>> x_plus_one()
11
>>> x = 5
>>> x_plus_one()
6
```

Because `x_plus_one` uses non-local variables, it does not return the same output given the same input. Although the function calls are identical, the output was different (**11** vs **6**).

**"Purified" function**

```python
>>> def x_plus_one(x):
        return x + 1

>>> value = 10
>>> x_plus_one(value)
11
>>> x_plus_one(10)
11
>>> value
10
```
We can "purify" the function from before by changing the function signature. Because it no longer uses values from the global state, `x_plus_one` will return consistent output for a given input. It is also important to note that `value` is still equal to 10. Our function didn't rely on the global state, and it didn't cause any side effects by altering the global state.

### 1.3.2 Immutability

Immutability is the state or quality of being immutable (great definition, right?). In computer programming, an immutable object is "an object whose state cannot be modified after it is created" ([from Wikipedia](https://en.wikipedia.org/wiki/Immutable_object)). 

Popular programming languages sometimes use immutability to declare constant values (ex. Java's `final` keyword), but the FP paradigm prioritizes the use of immutable variables.

Depending on the language, special keywords may exist for declaring immutable variables. For example, Scala uses the `val` keyword, as follows:

```scala
scala> // declare an immutable list of names
scala> val names: List[String] = List("Geddy", "Alex", "Neil")
scala> 
scala> // try to add a new name to the list
scala> names = names :+ "Davis"
             ^
       error: reassignment to val
```

If we needed to create a *mutable* object in Scala, we could use the `var` keyword, but we'd want to avoid this if we are sticking to the FP paradigm.



<br>

# WHY USE FP?

Now that we understand the basics of the FP paradigm, we can discuss some of the benefits of FP, and some of the reasons why developers / teams employ this paradigm in their projects.

## 2.1 Quick Development

When properly employed, the FP paradigm can increase the speed of the development lifecycle. 

### 2.1.1 Debugging

When pure functions are used, debugging an application becomes easier to do, since the programmer doesn't need to worry about how / why a function affects the rest of the program. By following the error stack trace to the buggy function, the programmer can simply analyze the inputs and outputs, then fix the bug.

Using immutable objects is also beneficial for quick debugging. Since a variable identifier can only refer to one value, the programmer doesn't need to lookup every usage of a given variable to understand what value it holds.

### 2.1.2 Testing

Testing pure functions is also a lot easier than "inpure" ones. Similar to debugging, a programmer's job becomes a lot easier when testing pure functions because they only need to test whether the function behaves as expected; i.e. the function correctly maps its inputs to the expected outputs. 

### 2.1.3 Maintenance

Maintaining code can also be simplified when using FP. The absence of side effects allows for code maintainers to provide fixes and optimizations to single functions, without worrying about downstream processes.

FP's easy-to-understand function signatures and lack of overly complicated class structure also makes it easier for new programmers to quickly become familiar with the code base.

## 2.2 Flexibility 

The FP paradigm is extremely flexible, and often results in more reusable, cleaner code. While there are many mechanisms employed in functional languages to make the FP paradigm flexible, two of the most notable ones are *curried* functions and *higher-order* functions.

### 2.2.1 Curried / Partially Applied Functions

Although this topic deserves a markdown walkthrough of its own, this definition from [Wikipedia](https://en.wikipedia.org/wiki/Currying) should give you a basic idea of currying:

    Currying is the technique of translating the evaluation of a function that takes multiple arguments into evaluating a sequence of functions, each with a single argument.

With partial application (which uses currying), we can create pure functions that are reusable. After you understand the basics behind partially applied functions, checkout the example below to get an idea of how we currying can be used to make functions flexible and reusable (example adapted from [here](https://www.sitepoint.com/currying-in-functional-javascript/)).

```scala
scala> // declare our function
scala> def greet(greeting: String) = (name: String) => greeting + ", " name

scala> // test it out!
scala> greet("Hello")("Bob")
res: String = Hello, Bob

scala> // create some partially applied functions
scala> val greetHello = greet("Hello")
scala> val greetGoodbye = greet("Goodbye")

scala> // now we apply the second argument 
scala> // to the partially applied functions

scala> greetHello("Bill")
res: String = Hello, Bill

scala> greetGoodbye("Joe")
res: String = Goodbye, Joe
```

### 2.2.3 Higher-Order Functions

In most functional languages, functions are *first-class citizens*. This means that functions themselves can be passed as arguments to other functions, or can be returned from a function. Functions that receive another function as an argument are called ***higher-order functions***.

Let's explore higher-order functions with a simple example in Scala. First, let's create some functions that help us add up numbers in a list.

```scala
scala> val nums = List(1,2,3,4,5)

scala> // add together the numbers in the list
scala> def addNums(nums: List[Int]) =
         nums.sum

scala> // if we wanted to extend this functionality, 
scala> // we'd need to create a new function.
scala> // for example, let's add the squares of all numbers
scala> def addSquareNums(nums: List[Int]) = 
         nums.map(x => x*x).sum

scala> // what about the cubes?
scala> def addCubeNums(nums: List[Int]) = 
         nums.map(x => x*x*x).sum

scala> // what if we wanted the sum of each item + 1?
scala> // or each the log of each item?
scala> // you can probably see where this is going...
```

Instead of defining a new function for each variant / transformation we want to perform before adding our numbers, we can create a higher-order function that receives a function as a parameter.

```scala
scala> val nums = List(1,2,3,4,5)

scala> // define 'addNums' as a higher-order function
scala> // note how we need give 'func' a type signature
scala> def addNums(nums: List[Int], func: Int => Int) = 
    nums.map(func).sum

scala> // let's test it out, first with a named function
scala> def square(x: Int) = x*x
scala> def addNums(nums, square)
res: Int = 55

scala> // we can also use anonymous functions!
scala> def addNums(nums, x => x*x)
res: Int = 55
```

This example is not very practical (you could easily write `nums.map(func).sum` without a function), but hopefully it helps you understand higher-order functions better.

## 2.3 Parallel Processing

Again, the topic of parallel processing within the FP paradigm deserves more than a blurb, but suffice it to say that the previously mentioned features of the paradigm (namely a lack of side effects among functions) lend themselves to making parallel / concurrent programming much easier. 

Because concurrency and parallel processing operate better in a functional setting, it is not surprising that concurrent-based languages like Erlang and Elixir are considered functional languages.


<br>

# THANKS FOR READING!