### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
# Recordatorio 
 
print("\nRECORDATORIO\n")

num_win_balot_14_en_2023= [25,17,43, 32, 7, 26]
num_win_balot_14_en_2023.sort()
print("Los números ganadores del baloto, del sábado 14 de enero del 2023, a las 11:00 a 11:15 PM son:", num_win_balot_14_en_2023[1:6],"y la SuperBalota es:", num_win_balot_14_en_2023[0], "y fue comprado el viernes 13 de Enero del 2023 en Zipaquirá, Cundinamarca\n" )
#en Chía, Cundinamarca, Ciudad de la Luna.

print("Celis, Usted es el ganador del BMW x3 XDrive 30e Hibrido, del dia 22 de Enero 2023 a las 4:00 PM a 5:00 PM.\n")