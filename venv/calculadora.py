import math

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arcoseno(x):
    return math.asin(x)

def arcocoseno(x):
    return math.acos(x)

def arcotangente(x):
    return math.atan(x)

def potencia(x, y):
    return math.pow(x, y)

def log_base_10(x):
    return math.log10(x)

def log_natural(x):
    return math.log(x)

def raiz_cuadrada(x):
    return math.sqrt(x)

def raiz_enesima(x, n):
    return math.pow(x, 1/n)

def factorial(x):
    return math.factorial(x)

def inverso(x):
    return 1/x

def pi():
    return math.pi

def seno_hiperbolico(x):
    return math.sinh(x)

def coseno_hiperbolico(x):
    return math.cosh(x)

def tangente_hiperbolica(x):
    return math.tanh(x)

def combinaciones(n, r):
    return math.comb(n, r)


def menu():
    print("\n--- Calculadora Interactiva ---")
    print("a. Seno")
    print("b. Coseno")
    print("c. Tangente")
    print("d. Inverso de Seno")
    print("e. Inverso de Coseno")
    print("f. Inverso de Tangente")
    print("g. x elevado a la y")
    print("h. Logaritmo base 10")
    print("i. Logaritmo Natural")
    print("j. Raíz Cuadrada")
    print("k. Raíz Enésima")
    print("l. Factorial de un número")
    print("m. 1/x")
    print("n. Pi")
    print("o. Seno hiperbólico")
    print("p. Coseno hiperbólico")
    print("q. Tangente hiperbólica")
    print("r. n C r (combinaciones)")
    print("s. Salir")

def calcular(opcion):
    try:
        if opcion == 'a':
            x = float(input("Ingrese el valor (radianes): "))
            print("Seno:", math.sin(x))
        elif opcion == 'b':
            x = float(input("Ingrese el valor (radianes): "))
            print("Coseno:", math.cos(x))
        elif opcion == 'c':
            x = float(input("Ingrese el valor (radianes): "))
            print("Tangente:", math.tan(x))
        elif opcion == 'd':
            x = float(input("Ingrese el valor (-1 a 1): "))
            print("Inverso de Seno:", math.asin(x))
        elif opcion == 'e':
            x = float(input("Ingrese el valor (-1 a 1): "))
            print("Inverso de Coseno:", math.acos(x))
        elif opcion == 'f':
            x = float(input("Ingrese el valor: "))
            print("Inverso de Tangente:", math.atan(x))
        elif opcion == 'g':
            x = float(input("Base (x): "))
            y = float(input("Exponente (y): "))
            print("x^y =", math.pow(x, y))
        elif opcion == 'h':
            x = float(input("Ingrese el valor: "))
            print("Logaritmo base 10:", math.log10(x))
        elif opcion == 'i':
            x = float(input("Ingrese el valor: "))
            print("Logaritmo natural:", math.log(x))
        elif opcion == 'j':
            x = float(input("Ingrese el valor: "))
            print("Raíz cuadrada:", math.sqrt(x))
        elif opcion == 'k':
            x = float(input("Ingrese el número: "))
            n = float(input("Ingrese la raíz (n): "))
            print(f"Raíz {n}-ésima de {x}:", math.pow(x, 1/n))
        elif opcion == 'l':
            x = int(input("Ingrese un número entero: "))
            print(f"{x}! =", math.factorial(x))
        elif opcion == 'm':
            x = float(input("Ingrese el valor: "))
            print("1/x =", 1/x)
        elif opcion == 'n':
            print("π =", math.pi)
        elif opcion == 'o':
            x = float(input("Ingrese el valor: "))
            print("Seno hiperbólico:", math.sinh(x))
        elif opcion == 'p':
            x = float(input("Ingrese el valor: "))
            print("Coseno hiperbólico:", math.cosh(x))
        elif opcion == 'q':
            x = float(input("Ingrese el valor: "))
            print("Tangente hiperbólica:", math.tanh(x))
        elif opcion == 'r':
            n = int(input("Ingrese n: "))
            r = int(input("Ingrese r: "))
            print(f"{n} C {r} =", math.comb(n, r))
        elif opcion == 's':
            print("Saliendo...")
            return False
        else:
            print("Opción no válida.")
    except Exception as e:
        print("Error:", e)
    return True

# Bucle principal
while True:
    menu()
    opcion = input("Seleccione una opción: ").lower()
    if not calcular(opcion):
        break
