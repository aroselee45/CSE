print("Hello world")
# This is a new line

# Autumn

a = 4
b = 3

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print()
print("Try to figure out how this works")
print( 15 % 12 )

# the "%
" sign is a modulus. It finds the remainder"

car_name = "The Wiebe Moble"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order

# Here is where we get a little fancy
print("What is your name?")
name = input(">_ ")
print("Hello %s." % name)

input("How old are you?")
print("%s?! That's really old. You belong in a retirement home")


'''Write a function called "happy_bday"
that "sings" (prints) Happy birthday

It must take one parameter called "name"
 '''


def happy_bday(name):
    print("Happy Birthday to you"  )
    print("Happy Birthday to you" )
    print("Happy Birthday dear " + name )
    print("Happy Birthday to you")

    happy_bday("John")



# Loops



for num in range (100000000):
    print(num)




'''Write a function called "happy_bday"
that "sings" (prints) Happy birthday

It must take one parameter
'''

a = 1
while a < 10:
    print(a)
    a += 1


# Random Numbers
import random # This should be on line 1
print(random.randint(0, 1000))