#Prueba Nº3
import os
import time
import random
import csv
limpieza_pantalla = "cls"
os.system(limpieza_pantalla)

def registrar_pedido():
    validador_datos = 1
    sacos_10KG = 0
    sacos_20KG = 0
    sacos_5KG = 0
    while validador_datos == 1:
        nombre_cliente = input("Ingrese su nombre: ")
        if nombre_cliente.isalpha() == True:
            validador_datos = 0
        else:
            print("ingrese un nombre con caracteres\nReintente...")
            time.sleep(1)
            os.system(limpieza_pantalla)
            validador_datos = 1

    while validador_datos == 0:
        apellido_cliente = input("ingrese su apellido: ")
        if apellido_cliente.isalpha() == True:
            validador_datos = 1
        else:
            print("ingrese un nombre con caracteres\nReintente...")
            validador_datos = 0
            time.sleep(1)
            os.system(limpieza_pantalla)

    while validador_datos == 1:
        sector_cliente = input("ingrese su comuna de residencia: ")
        if sector_cliente.isalpha() == True:
           validador_datos = 0
        else:
            print("ingrese caracteres\nReintente...")
            time.sleep(1)
            os.system(limpieza_pantalla)
    
        direccion_cliente = input("Ingrese la direccion de entrega: ")

    while True:
        opcion_de_saco = input("Ingrese que saco de alimento desea (5KG, 10KG, 20KG): ").upper()
        if opcion_de_saco == "5KG":
            sacos_5KG = int(input("Ingrese la cantidad de sacos de 5KG que desea: "))
            sacos_5KG =+ sacos_5KG
            break
        elif opcion_de_saco == "10KG":
            sacos_10KG = int(input("Ingrese la cantidad de saco de 10KG que desea: "))
            sacos_10KG =+ sacos_10KG
            break
        elif opcion_de_saco == "20KG":
            sacos_20KG = int(input("ingrese la cantidad de sacos de 20KG que desea: "))
            sacos_20KG =+ sacos_20KG
            break
        else:
            print("ingrese una opcion valida\nReintente...")
            time.sleep(1)
            os.system(limpieza_pantalla)

    numero_pedido = (random.randint(0,100))

    pedido = {
        "numero_pedido":numero_pedido,
        "nombre":nombre_cliente,
        "apellido":apellido_cliente,
        "sector": sector_cliente,
        "direccion": direccion_cliente,
        "saco5kg": sacos_5KG,
        "sacos10kg":sacos_10KG,
        "sacos20kg":sacos_20KG}
    hoja_pedido.append(pedido)
    print("Pedido registrado con exito\nVolviendo al menu...")

def listar_pedido(hoja_pedido):
    hoja_pedido = [pedido for pedido in hoja_pedido]
    print(hoja_pedido)
    return hoja_pedido

def imprimir_ruta(hoja_pedido):
    with open("lista_pedido.txt","w") as pedido_txt:
            pedido_txt.write(f"{hoja_pedido}")
            print(hoja_pedido)

def salir_programa():
    with open("ruta.csv","a",newline="") as archivo_pedido:
        escritor_csv = csv.writer(archivo_pedido)
        escritor_csv.writerow(hoja_pedido)

hoja_pedido = []

while True:
    print("""1. registrar pedido 
2. listar todos los pedidos
3. imprimir hoja de ruta
4. salir del programa""")
    opcion_menu = str(input("Ingrese una opcion: "))
    if opcion_menu == "1":
        registrar_pedido()
    elif opcion_menu == "2":
        listar_pedido(hoja_pedido)
    elif opcion_menu == "3":
        imprimir_ruta(hoja_pedido)
    elif opcion_menu == "4":
        salir_programa()
        break
    else:
        print("ingrese una opcion valida.")
