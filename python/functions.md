---
layout: default
published: true
---
# Methods - Defining functions

## What?

Functions, also referred to as methods, are a named piece of logic which performs a specific task. Typically they are used to 'do a thing' or return a value or object.

## Why?

Functions allow us to wrap up a useful piece of code into something that is re-usable, concise and able to be tested - which increases reliability. They make maintenance and future code changes (refactoring) easier and isolate logic from other parts of the code.

## How?

    def double(number):
        doubled_number = number * 2
        return doubled_number

The above defines a function called `double`, it has the input argument: `number` and returns the value of `doubled_number`.

To call the function, run:

    double(number=5)

You can use multiple input arguments:

    def add_two_numbers(number_1, number_2):
        sum = number_1 + number_2
        return sum

### Type hints and docstrings

To give the user information on what data type a function expects, you can use type hints, these are not enforced but __hints__ to what is expected and what is returned.

    def double(number: float) -> float:
        doubled_number = number * 2
        return doubled_number

Here the function expects an argument called `number` to be given as a float (a floating point number, similar to what we know as decimals), and return a float.

We can include information as a docstring to instruct the user how to operate the method:

    def double(number: float) -> float:
        '''This function doubles the input and returns this new object.'''
        doubled_number = number * 2
        return doubled_number


To call this information within a Python interpreter, wrap the method with the `help` function.

    help(double)

It will return:

    Signature: double(number: float) -> float
    Docstring: This function doubles the input and returns this new object
    File:      ~/data-engineering-101/<ipython-input-43-14722429ea66>
    Type:      function

To return this information in iPython, alternatively you can use:

    double?

### A warning on type hints

Type hints do not enforce the argument's type. For our example of `double()`, providing the input is a valid Python statement, it will run:

    double("hello world")

will return:

    "hello worldhello world"

It has indeed executed and returned the expected result of multiplying the object by two; though we expected it to work for numbers it will multiple any valid Python object by two, so long as it is a correct Python statement - in this case, multiplying and concatenating a string.

Generally, Python is not a type-safe language.

## Scoping

Objects are loaded into the computers memory for us to reuse later; Python is pretty smart and when an object is not needed anymore it goes to the garbage collector which frees up the memory allocations, this ensures we're only holding onto what we need and do not fill our computer's RAM with unnecessary objects.

An interpreter, or executed python program, has a global scope, this contains references to all of the objects that are stored in memory. Methods (functions) have a local scope and only return the specific objects we tell it to and add them to the global scope, the rest go to the garbage collector.

## Recommended approach

Methods are useful to abstract logic into reusable functions. It is important to name them appropriately so a future user understands exactly what that piece of code does, just from reading its name.

Typically it is better to have well named variables and clean code to act as documentation, as docstrings are often not updated by engineers as methods develop and change.  That said, I do appreciate and use type hints as they require minimal maintenance over time and give useful insight to new engineers on what the function should receive as an input and what it outputs.

I would be happy to see a function like this:

    def double(number: float) -> float:
        return number * 2

Since we are only returning a simple math operation, we do not need to assign the value to `doubled_number`, only for it to be cleared by the garbage after the function has run as it is no longer scoped, it's local scope collapses and only the returned value is surfaced from the function.

In the above method we have included the input argument's, and returned output's expected type. The function and argument's names are simple and should convey what is does and what it receives.
