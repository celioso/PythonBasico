### Classes ###

class MyEmptyPerson: # Se escribe la clase CalmelCase Ej: MiBlogDeDesarrollador y el otro es snake_case Ej: mi_blog_de_desarrollador
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname) -> None:
        self.name =name
        self.surname = surname

my_person = Person("Mario","Celis")
print(my_person.name,my_person.surname)
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname, alias = "sin alias") -> None:
        self.full_name =f"{name} {surname} ({alias})" # propiedad publica
        self.__name = name # Propiedad privada
        self.__surname = name

    def get_name(self):
        return self.__name # Propiedad privada

    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Mario", "Celis")
print(my_person.full_name)
my_person.walk()
        
my_other_person = Person("Camilo", "Torres", "CelisCorp")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de león (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 25174332726
print(my_other_person.full_name)
