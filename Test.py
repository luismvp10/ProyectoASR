import time

print("Bienvenido a la calculadora")

while True:
    print("Estas son las operaciones que puedes realizar")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicación")
    print("4.-División")
    print("5.-Salir")

    opc =4

    def realizar_operacion(opc, num1, num2):
        if opc == 1:
            return  num1 + num2
        elif opc == 2:
            res = num1 - num2
        elif opc == 3:
            return  num1 * num2
        else:
            return  num1 / num2



    try:
        opc = int(input("Introduce el número de la opción a realizar: "))
        print("\n")
        a = int(input("Dame un número: "))
        b = int(input("Dame otro número: "))

    except ValueError:
        print("Solo se permiten números")
        time.sleep(2)

    else:
        if opc < 1 or opc > 4:
            print("Esta no es una opción válida")
            time.sleep(2)
            continue

        resultado = realizar_operacion(opc, a, b)
        print("El resultado es : " +str(resultado))
        continuar = input("Desea continuar si/no : ")
        if continuar != "si":
            break
print("Hasta luego! :'(")
