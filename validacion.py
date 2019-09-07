import valores as v

def calculadora():
    continuar = "si"
    while continuar != "no":
        if continuar == "si":
            datos = validarNumeros()
            if datos != "errorNum":
                a = datos[0]
                b = datos[1]
                menu()
                op = input("Indique operación: ")
                x = validarOperador(op)
                if x != "errorOp":
                    ejecutarOperacion(a, b, x)
                else:
                    print("Ingresar operación válida!")
            else:
                print("Ingresar solo datos numéricos!")
        else:
            print("Ingrese una respuesta válida, por favor.")
        continuar = input("¿Desea realizar otra operacion? [Si/No]: ")

def menu():
    print("""
¿Qué operación desea realizar con los números ingresados?
Suma: '+' o 'suma'
Resta: '-' o 'resta'
Producto: '*' o 'producto'
Divisón decimal: '/' o 'divdecimal'
Dvisión entera: '//' o 'diventera'
Residuo: '%' o 'residuo'
Potencia: '**' o '^' o 'potencia'""")

def validarNumeros():
    datos = v.solicitudValores()
    a = datos[0]
    b = datos[1]
    try:
        a = float(a)
        b = float(b)
        numeros = [a, b]
        return numeros
    except ValueError:
        return "errorNum"

def validarOperador(x):
    operadores = ['+', '-', '*', '/', '//', '%', '**', 'suma', 'resta', 'producto', 'divdecimal', 'diventera', 'residuo', 'potencia']
    if x in operadores:
        return x
    else:
        return "errorOp"

def ejecutarOperacion(a, b, x):
    if x == '+' or x == 'suma':
        resultado = a + b
        print("La suma de ", a, " y ", b, "es: ", resultado)
    elif x == '-' or x == 'resta':
        resultado = a - b
        print("La resta de ", a, " y ", b, "es: ", resultado)
    elif x == '*' or x == 'producto':
        resultado = a * b
        print("el producto de ", a, " y ", b, "es: ", resultado)
    elif x == '/' or x == 'divdecimal':
        try:
            resultado = a / b
            print("La división decimal de ", a, " y ", b, "es: ", resultado)
        except ZeroDivisionError:
            print("¡División por cero!")
    elif x == '//' or x == 'diventera':
        try:
            resultado = a // b
            print("La división entera de ", a, " y ", b, "es: ", resultado)
        except ZeroDivisionError:
            print("¡División por cero!")
    elif x == '%' or x == 'residuo':
        resultado = a % b
        print("El residuo de la división entera de ", a, " y ", b, "es: ", resultado)
    elif x == '**' or x == '^' or x == 'potencia':
        resultado = a ** b
        print(a, " elevado a ", b, "es: ", resultado)