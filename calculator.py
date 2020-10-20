# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:49:50 2020

@author: diego
"""


def main_calculator():
    salir = ""
    res = None
    ans = None
    while(salir != "e"):
        operation = int(input(
            "Seleccione 1:Suma, 2:Resta, 3:Multiplicación, 4: Division, 5:Potenciacion, 6:Raiz Y-esima \n"))
        if res != None:
            ans = input(
                "Desea seguir operando con el resultado anterior [y/n] \n").lower()
            if(ans == "y"):
                x = res
            else:
                x = input("Ingrese el primer valor \n")
        else:
            x = input("Ingrese el primer valor \n")

        y = input("Ingrese el segundo valor \n")
        res = switch(operation, x, y)
        print("El resultado de la operación es: ", res)
        salir = input("Si desea salir presione la tecla e. \n").lower()


def switch(case, a, b):
    try:
        a = float(a)
        b = float(b)
    except:
        if isinstance(a, str) or isinstance(b, str):
            return "Sólo se deben ingresar numeros"
    sw = {
        1: suma(a, b),
        2: resta(a, b),
        3: multiplicacion(a, b),
        4: division(a, b),
        5: potenciacion(a, b),
        6: raiz(a, b),
    }

    return sw.get(case, default())


def default():
    return "Opcion Invalida"


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def potenciacion(a, b):
    return a ** b


def raiz(a, b):
    if b == 0 or a < 0:
        return "Error matematico"
    if b % 2 == 0 and a <= 0:
        return "Error matematico"
    return a**(1/b)


def division(a, b):
    if b == 0:
        return "Error: Division entre cero..."
    else:
        return a / b

# main_calculator()
