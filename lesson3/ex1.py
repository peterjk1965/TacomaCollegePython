#!/usr/bin/python3

#The Saffir-Simpson Scale to classify the strength of hurricanes

#prompt user for wind speed in mph
wind_speed = input('How fast is the wind blowing in MPH: ')

# Convert the distance to an integer.
speed = int(wind_speed)

# Determine hurricane category.
if speed <= 25:
    category_of_hurricane = 'Fake'
elif speed <= 74:
    category_of_hurricane = 'Cat1'
elif speed <= 95:
    category_of_hurricane = 'Cat2'
elif speed <= 110:
    category_of_hurricane = 'Cat3'
elif speed <= 130:
    category_of_hurricane = 'Cat4'
else:
    category_of_hurricane = 'Cat5'

# display a message telling the user the hurricane's intensity
print('Looks like a {} hurricane.'.format(category_of_hurricane))    
