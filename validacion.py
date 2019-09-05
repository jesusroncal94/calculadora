import valores as v

def calculadora():
    datos = validarNumeros()
    if datos != "error":
        a = int(datos[0])
        b = int(datos[1])
        x = input("""
CALCULADORA
SUMA: '+' o 'suma'
RESTA: '-' o 'resta'
PRODUCTO: '*' o 'producto'
DIVISIÓN DECIMAL: '/' o 'divdecimal'
DIVISIÓN ENTERA: '//' o 'diventera'
RESIDUO: '%' o 'residuo'
POTENCIA: '**' o '^' o 'potencia'

INDIQUE OPERACIÓN: """)
        if operaciones(a, b, x) == 0:
            print("")
        else:
            print("Seleccionar una operación correcta!")
            y = input("INDIQUE OPERACIÓN NUEVAMENTE: ")
            operaciones(a, b, y)
    else:
        print("Ingresar solo datos numéricos!")
        calculadora()

def validarNumeros():
    datos = v.solicitudValores()
    a = str(datos[0])
    b = str(datos[1])
    if a.isnumeric() and b.isnumeric():
        return datos
    else:
        return "error"

def operaciones(a, b, x):
    resultado = 0
    if x == '+' or x == 'suma':
        resultado = a + b
        print("La suma de ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '-' or x == 'resta':
        resultado = a - b
        print("La resta de ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '*' or x == 'producto':
        resultado = a * b
        print("el producto de ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '/' or x == 'divdecimal':
        resultado = a / b
        print("La división decimal de ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '//' or x == 'diventera':
        resultado = a // b
        print("La división entera de ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '%' or x == 'residuo':
        resultado = a % b
        print("El residuo de dividir ", a, " y ", b, "es: ", resultado)
        return 0
    elif x == '**' or x == '^' or x == 'potencia':
        resultado = a ** b
        print(a, " elevado a ", b, "es: ", resultado)
        return 0
    else:
        return 1