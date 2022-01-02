#!/usr/bin/python3

#compute the average of some numbers

#First, I'll prompt the user for the number of numbers that he or she wants to average.
input_num = eval(input('How many numbers do you want to average?: '))

#Once the user enters the appropriate number of values,
# I'll stop looping, compute the average, and then display the result. 

sum = 0.0

for count in range(input_num):
    value = eval(input('enter a value: '))
    sum = sum + value

average = sum / input_num
print('The average is: ',average)



