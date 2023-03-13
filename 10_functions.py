### Function ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_number, secund_number):
    print(first_number + secund_number)

sum_two_values(5, 7)
sum_two_values(545845, 54878561)
sum_two_values("5","7")
sum_two_values(1.4,5.2)

def sum_two_values(first_value: int, secund_value):
    print(first_value + secund_value)

sum_two_values(5, 7)
sum_two_values(545845, 54878561)
sum_two_values("5","7")
sum_two_values(1.4,5.2)

def sum_two_values_with_return(first_value, secund_value):
    return first_value + secund_value

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Celis", name = "Mario")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Mario", "Celis", "Termicelis")
print_name_with_default("Mario", "Celis")

def print_texts(*text): # al colocar * crea textos dinamicos
    print(type(text))
    for text in text:
        print(text.upper())

print_texts("Hola","Python","Termicelis")
print_texts("Hola")


