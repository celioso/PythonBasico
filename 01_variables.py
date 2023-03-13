# Variables

from operator import le

my_variable = 'My String Variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenación de variables en un print
print(type(print(my_variable, my_int_to_str_variable, my_bool_variable)))
print("este es el valor de : ", my_bool_variable)

# Funciones del sistema 
print(len(my_variable))

# Variables en una sola línea. ¡ Cuidado con abusar de esta sintexis
name, surname, alias ,age ="Mario", "Celis", "Termicelis", float(38.5)
print("Me llamo: ",name, surname,". Mi edad es:", age,".Y mi alias es: ",alias)

# Inputs
"""first_name = input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')

print(first_name)
print(age)"""

# Cambiamos su tipo
name = 35
age = 'mario'

print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(type(address))

