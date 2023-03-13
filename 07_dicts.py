### Doctionaries ###

my_dict= dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Mario", "Apellido":"Celis", "Edad":38, 1:"Python"}
print(my_other_dict)
my_dict = {
"Nombre":"Mario",
"Apellido":"Celis", 
"Edad":38, 
"Lenguajes":{"Python", "Swift", "kotlin"},
1:1.82
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] ="Calle 9 # 8 37"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print(my_dict["Lenguajes"])

print("Mario" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict= dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict= dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict, ["Camilo", "Torres"]) # Duplica todos los valores en values
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values)
#print(list(my_new_dict.values()))
print(list(dict.fromkeys(list(my_new_dict.keys()))))
print(tuple(my_new_dict))
print(set(my_new_dict))

'''print(my_dict.fromkeys(("Nombre",1)))
my_new_dict = my_other_dict.fromkeys(("Nombre",1, "Piso"))
print(my_new_dict)'''