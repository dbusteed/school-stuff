# quick intro to functional programming

Functional programming (FP) is a programming paradigm. It's a framework of patterns, standards, and suggestions that programmers use when writing code.
 
Despite the fairly unexciting nature of words like "paradigm" and "framework", understanding the basic principles of FP is extremely beneficial for all programmers. By implementing simple concepts like *pure functions* and *immutability* (just to name a few), complex problems become manageable, and the software development process is streamlined.
 
<br>
 
# 1. HISTORY OF FP
 
## 1.1 LAMBDA CALCULUS
 
The functional programming paradigm can be traced back to lambda calculus, a mathematical framework developed by Alonzo Church in the 1930s. Along with having a really cool name, lambda calculus is used to represent and evaluate functions.
 
Many programmers use lambda calculus in their programs unknowingly, or at least without a complete knowledge of the lambda calculus fundamentals. Because lambda calculus is one of the cornerstones of modern functional programming, let's take a look at some simple examples.
 
```
// function definition
//   1) parameters are marked with "λ"
//   2) function body listed after parameters
addOne = λx.x+1
 
// example of evaluation
addOne 5
 
// substitute function definition
(λx.x+1) 5
 
// plug-in function arguments
(5+1)
 
// evaluate function
6
```
 
Pretty simple, right? The basic rules of lambda calculus can be used to represent more interesting ideas, for example, the logical AND operator:
 
```
// basic definitions of booleans
TRUE = λx.λy.x
FALSE = λx.λy.y
 
// definition of logical AND
AND = λp.λq.p q FALSE
 
// evaluate
AND FALSE TRUE
(λp.λq.p q FALSE) FALSE TRUE
FALSE TRUE FALSE
(λx.λy.y) TRUE FALSE
(FALSE)
FALSE
```
 
The core concepts of the FP paradigm (pure functions, higher-order functions, etc) are found within lambda calculus. Modern programming languages can trace their functional aspects back to lambda calculus (for example, Python's `lambda` keyword).
 
## 1.2 EARLY FP LANGUAGES
 
Early programming languages were heavily influenced by mathematics, so it's not surprising that many languages incorporated lambda calculus and other functional concepts.
 
Lisp, for example, was developed in the late 1950s, and supported many features of functional programming. Branches of the Lisp language (such as Scheme and Clojure), continued this trend and helped shape our understanding of the FP paradigm.
 
## 1.3 RESURGENCE OF FP
 
"Resurgence" might not be the correct word, but it seems that the functional programming paradigm is becoming more well-known by all levels of programmers.
 
Modern programming languages such as Python and JavaScript are considered "multi-paradigm" languages, since they allow for Object-Oriented and Functional programming. Other languages such as Haskell are purely functional, and are mainly used for academic research.
 
It's hard to pinpoint the underlying trends of programming paradigm usage, but it seems that the shift towards service-based architecture and parallel programming has led to the increased interest in functional programming.
 
<br>
 
# 2. FP FUNDAMENTALS
 
## 2.1 PURE FUNCTIONS
 
Arguably, the most distinguishing feature of the FP paradigm is the use of **pure functions**. Most programmers are familiar with functions, but what are *pure* functions? [Professor Frisby's Mostly Adequate Guide to Functional Programming](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch03.html) gives this definition:
 
       A pure function is a function that, given the same input,
       will always return the same output and does not have any
       observable side effect.
 
Okay...so pure functions should **(1)** return the same output for a given input, and **(2)** not cause any *side effects*.
 
Let's illustrate the difference between an *impure* function and pure function.
 
```python
>>> # example of "IMPURE" function
>>> def x_plus_one():
       return x + 1
 
>>> x = 10
>>> x_plus_one()
11
>>> x = 5
>>> x_plus_one()
6
>>> # Because `x_plus_one` uses non-local variables,
>>> # it doesn't return the same output given the same input.
>>> # Although the function calls were identical,
>>> # the output was different (11 vs 6)
```
 
```python
>>> # example of PURE function
>>> def x_plus_one(x):
       return x + 1
 
>>> value = 10
>>> x_plus_one(value)
11
>>> x_plus_one(10)
11
>>> value
10
>>> # Because the update function longer uses values
>>> # from the global state, `x_plus_one` will return
>>> # consistent output for a given input. It is also important
>>> # to note that `value` is still equal to 10. Our function
>>> # didn't rely on the global state, and it didn't cause any
>>> # side effects by altering the global state.
```
 
Pure functions are crucial to many of the advantages inherent to the FP paradigm. For example, using pure functions can speed up the development process; pure functions are easier to debug, test, and maintain.
 
## 2.2 HIGHER ORDER FUNCTIONS
 
In most functional languages, functions are considered *first-class citizens*. This means that functions themselves can be passed as arguments to other functions, or can be returned from a function. Functions that receive another function as an argument are called **higher-order functions**.
 
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
scala> // or the logarithm of each item?
scala> // you can probably see where this is going...
```
 
Instead of defining a new function for each variant / transformation we want to perform before adding our numbers, we can create a higher-order function that receives a function as a parameter.
 
```scala
scala> val nums = List(1,2,3,4,5)
 
scala> // define 'addNums' as a higher-order function
scala> // note how we need to give 'func' a type signature
scala> def addNums(nums: List[Int], func: Int => Int) =
   nums.map(func).sum
 
scala> // let's test it out, first with a named function
scala> def square(x: Int) = x*x
scala> def addNums(nums, square)
res: Int = 55
 
scala> // we can also use lambda functions!
scala> def addNums(nums, x => x*x)
res: Int = 55
```
 
This example is not very practical (you could easily write `nums.map(func).sum` without using a function), but hopefully it helps you understand higher-order functions better.
 
Higher-order functions are one of the many reasons why functional programming results in flexible, easy-to-read code.
 
## 2.3 IMMUTABILITY
 
The last fundamental feature of functional programming is immutability. In computer programming, an immutable object is "an object whose state cannot be modified after it is created" ([from Wikipedia](https://en.wikipedia.org/wiki/Immutable_object)).
 
Popular programming languages sometimes use immutability to declare constant values (ex. Java's `final` keyword). The FP paradigm prioritizes the use of immutable variables.
 
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
 
The benefits of immutability are similar to those of using pure functions; it makes your code easier to debug, test, and maintain.
 
<br>
 
# 3. FUTURE OF FP
 
It's difficult to predict the future of functional programming. FP is a collection of ideas and theories, and isn't necessarily tied to a single technology / programming language.
 
That said, it does appear to be on the rise. As the industry continues to explore service-based architecture, AI, and 5th-gen programming languages, I believe that the concepts native to FP will play a big role.
 
<br>
 
# 4. CONCLUSION
 
Programming paradigms are similar to other technologies and processes in the IT world: there isn't a "one size fits all". The FP paradigm is extremely useful within the correct use cases, but that doesn't mean that it's the only correct way to write programs.
 
Rather, FP is another (powerful) tool in your "programming toolbox". Understanding FP will give you new insights when tackling difficult problems.
 
<br>
 
## THANKS!

*References / other stuff*
* [Lambda Calculus - Computerphile](https://www.youtube.com/watch?v=eis11j_iGMs)
* [Professor Frisby's Mostly Adequate Guide to Functional Programming](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch03.html)
* [My early attempt at explaining FP](https://github.com/dbusteed/functional-programming/blob/master/docs/what_and_why.md)
* [KNN algorithm using FP](https://github.com/dbusteed/knn-scala/blob/master/src/main/scala/Main.scala)