import math
# 

def sq():

    width = int(input('Enter the Width'))

    length = int(input('Enter the Length'))

    area = width * length

    print(f'the square footage of a house is {area} ')


# Circumference of circle
def cir():

    radius = float(input('Enter the raduis of your circle'))

    C = 2*math.pi*radius

    print(f'Cirumference of circle is {C}')
