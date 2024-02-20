a = 0
b = 0
print("Seleccione que funcion quiere ocupar:")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
Funcion = int(input("Seleciona que funcion quieres ocupar:"))




a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))


def add(a, b):
    return a + b

# Definir la función subtract para realizar la resta
def subtract(a, b):
    return a - b

# Definir la función multiply para realizar la multiplicación
def multiply(a, b):
    return a * b

# Definir la función divide para realizar la división
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
if Funcion == 1:
    print("Resultado:", add(a, b))
elif Funcion == 2:
    print("Resultado:", subtract(a, b))
elif Funcion == 3:
    print("Resultado:", multiply(a, b))
elif Funcion == 4:
    print("Resultado:", divide(a, b))
else:
    print("Selección no válida.")
    