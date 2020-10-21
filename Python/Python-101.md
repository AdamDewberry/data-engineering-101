##Defining Functions

In Python we define our own Functions to save time and speed up our own process.

A Function is a block of code which only runs when it is called upon. As a result of this, the function can return data.

a function is defined using the 'def' keyword:

def my_name():
    print("My name is")

##Calling a Function

To call a function, use the fuction name followed by a parenthesis:

my_name()

##Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (Name). When the function is called, we pass along a name, which is used inside the function to print the name.

def my_name(name):
    print("My name is" + name)    