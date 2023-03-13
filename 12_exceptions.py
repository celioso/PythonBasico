### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("se ha producido un error")

# try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("se ha producido un error")
else: # Opcional
    # se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("se ha producido un ValueError")
except TypeError:
    # Se ejecuta si se produce una excepción
    print("se ha producido un TypeError")

# Captura d ela información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
