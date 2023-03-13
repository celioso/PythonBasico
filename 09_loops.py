### Loops ###

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")
 

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecuciónes")
        break
    print(my_condition)

print("La ejecución continúa\n")  

# For

my_list = [35, 24, 62, 52, 30, 30, 17] #guarda elementos en orden

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Mario", "Celis", "Mario") # no se puede modificar 
for element in my_tuple:
    print(element)

my_set = {"Mario", "Celis", 35} # no deja guardar elementos repetidos
for element in my_set:
    print(element)

my_dict = {"Nombre":"Mario", "Apellido":"Celis", "Edad":38, 1:"p"} # guarda clave valor
for element in my_dict:
    print(element)
    if element == "Edad":
        continue # break detiene el programa
    print("se ejecuta")
else:
    print("El blucle for para el diccionario ha terminado")

print("la ejecución continúa")
