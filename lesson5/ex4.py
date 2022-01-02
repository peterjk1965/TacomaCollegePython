#!/usr/bin/python3

#change values passed in

#defining a function, passing in a value
def change_value(value):
    """This function changes the value passed in to 1"""
    print ("Inside, value is:", value)
    #changing the value of of the function
    value = 1
    print ("Inside, value is changed to:", value)

number = 5
print ("Outside, number is:", number)
change_value(number)
print ("Outside, number is now:", number)
    