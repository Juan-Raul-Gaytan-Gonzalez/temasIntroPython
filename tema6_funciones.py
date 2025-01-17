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
    print("la resxta de los dos numeros es: ", num1 - num2)



def run():
    os.system('cls')
    print("menu de opciones: ")
    print("1.-suma")
    print("2.-resta")
    print("3.-salir")
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        funcion1()
    if opcion == 2:
        funcion2()


if __name__ == "__main__":
    run()