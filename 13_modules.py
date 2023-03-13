### Modules ###
"""num1 = input("Ingresa el 1 número: ")
num2 = input("Ingresa el 2 número: ")
def sum_two_values(first_values: int, second_values):
    print(int(first_values) + int(second_values))

sum_two_values(num1, num2)"""

import my_module

my_module.sumValue(5, 5, 1)
my_module.printValue("Hola Python")

from my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola Python")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_value

print(PI_value)