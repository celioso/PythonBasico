# Este es un comentario:
# Nuestro Hola, Mundo
print('Hola mundo con Python')
print("Hola mundo con Python")

"""
Este es un
comentario
en varias lineas
"""

'''
Este tambien es un
comentario
en varias lineas
'''
#Consultar el tipo de dato

print(type('Hola mundo')) #Tipo 'str'
print(type(5)) # Tipo 'int'
print(type(1.5)) # Tipo 'float'
print(type(3 + 1j)) # Tipo complex
print(type(True)) # Tipo 'bool'

print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

print(type(print('My texto'))) # Tipo 'NoneType'
