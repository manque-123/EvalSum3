import os
import time
import csv
acceso=1

def menu():
    time.sleep(0.7)
    print(' Bienvenido a reparto catpremium')
    time.sleep(1)
    print(''' Aqui podra ver nuestro menu:
        1- Registrar pedido
        2- Lista de todos los pedidos
        3- imprimir hoja de ruta
        4- salir del programa ''')
    time.sleep(1)
    opc=int(input('que operacion desea realizar:   '))
    while acceso==1:
            if opc==1:
                print('ingrese los siguientes datos:  ')
                nombre_apellido=input('Nombre y pellido: ')
                comuna=input('Ingrese comuna:   ')
                direccion=input('Ingrese direccion:   ')
                sector=input('ingrese sector:  ')
                time.sleep(1)
            menu2()
def menu2():
    sacos=int(input('''Estos sacos tenemos disponibles 
                            1- 5kg
                            2- 10kg
                            3- 20kg   
                            Que sacos desea comprar:  '''))
    if sacos==1:
        print('usted a elegido el saco de 5kg')
        otrosaco=int(input('deseas agregar otro saco: 1-Si  2-No:   '))
    if sacos==2:
        print('usted a elegido el saco de 10kg')
        otrosaco=int(input('deseas agregar otro saco: 1-Si  2-No:   '))
    if sacos==3:
        print('usted a elegido el saco de 20kg')
        otrosaco=int(input('deseas agregar otro saco: 1-Si  2-No:   '))
        if menu2==2:
            menu2()
        elif menu2==1:
            menu2()
    menu()
def lista_pedidos():
    if lista_pedidos ==2:
        print(lista_pedidos)
        with open ('archivo.csv', 'r', newline='') as lista_trabajadores:
            archivo.csv.read()
            lista_pedidos=['nombre_apellido', 'comuna', 'direccion']

def opciones():
    if opcion==1:
        registrar_pedido()
    if opcion==2:
        lista_pedidos()
    if opcion==3:
        imprimir_hojaderuta()
    if opcion==4:
        slair_programa()

def salir_programa():
    if salir_programa ==4:
        print('Saliendo del programa Hasta pronto!')

menu()