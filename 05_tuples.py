### tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Mario", "Celis")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
'''print(my_tuple[4])  indexError
print(my_tuple[-6])'''

print(my_tuple.count("CelisCorp"))
print(my_tuple.index("Mario"))
print(my_tuple.index("Celis"))

#my_tuple[5]=1.80

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "CelisCorp"
my_tuple.insert(1,"Blue")
my_tuple = tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

del my_tuple
#print(my_tuple)


