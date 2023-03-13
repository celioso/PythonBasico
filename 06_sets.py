### Sets ##

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  #Inicialmente es un diccionario

my_other_set = {"Mario", "Celis", 38}
print(type(my_other_set))

print(len(my_other_set))

print(my_other_set)

my_other_set.add("CelisCorp")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("CelisCorp") # Un set no admite repetidos

print(my_other_set)

print("Mario" in my_other_set)
print("marii" in my_other_set)

my_other_set.remove("Mario")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Mario", "Celis", 38}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Jave","C#"}))

print(my_new_set.difference(my_set))