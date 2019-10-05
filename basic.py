#for printing 
print("hello")

#its the correct order to put if satement
if 5>2:

    print("five is greater the 2")

# if this like its wrong
 #  if 5>2:
 # print ("hello")

#this write sytax mutiple line
if 5>2:

    print("Five is greater than two!")
    print("Five is greater than two!")
"""
 wrong
if >2:

   print("Five is greater than two!")
     print("Five is greater than two!")

"""
"""
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""
x=5
y="john"

print(x)
print(y)
#Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)


#string varblies can be declared both " "or' '

x="john"
x='john'
print(x)

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

#Python allows you to assign values to multiple variables in one line:
x,y,z="orange","apple","banana"

print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:

X=Y=Z="orange"

print(X)
print(Y)
print(Z)

"""
Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

"""
x="orange"
print("orange in "+ x+ " color")
