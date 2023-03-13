### Strings ###

my_string = "Mi string" 
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string +" "+ my_other_string+'\n')

my_new_line_string = "Este es un String \ncon salto de lines"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \nescapado "
print(my_scape_string)

# Formateo

name, surname, age = "Mario", "Celis", 38

print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name +" "+ surname +" y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


# Reversed

Reversed_language = language[::-1]
print(Reversed_language)

# Funciones 
print("Función\n")
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print("1".capitalize())
print(language.lower())
print(language.lower().isupper())
print(language.startswith('Py'))
