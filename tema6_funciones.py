import os

def funcion1(): 
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la suma de los dos numeros es: ", num1 + num2)

def funcion2(): 
    os.system('cls')
    print("Hola, Soy la funcion 2")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la resta de los dos numeros es: ", num1 - num2)

def funcion3(): 
    os.system('cls')
    print("Hola, Soy la funcion 3")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print("la multiplicacion de los dos numeros es: ", num1 * num2)

def funcion4(): 
    os.system('cls')
    print("Hola, Soy la funcion 4")
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    if num2 != 0:
        print("la division de los dos numeros es: ", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero.")

def run():
    while True:
        os.system('cls')
        print("menu de opciones: ")
        print("1.- suma")
        print("2.- resta")
        print("3.- multiplicar")
        print("4.- Dividir")
        print("5.- salir")
        opcion = int(input("Dame una opcion: "))
        
        if opcion == 1:
            funcion1()
        elif opcion == 2:
            funcion2()
        elif opcion == 3:
            funcion3()
        elif opcion == 4:
            funcion4()
        elif opcion == 5:
            print("...")
            break
        else:
            print(" elige una opción del menú.")
        
        input("Enter continuar...")  

if __name__ == "__main__":
    run()