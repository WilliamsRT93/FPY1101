#handroll
import os, time
cantidad_total = 0
cantidad_handroll = 0
handroll_seleccionado = 0
opcion_1 = 0
opcion_2 = 0
opcion_3 = 0
opcion_4 = 0
codigo_desc = "soyotaku"
cierre_app = 0
cierre_menu = 0
limpiar_pantalla = "cls"
os.system(limpiar_pantalla)
while cierre_app == 0:

    print("Delivery Handroll Otaku")
    
    while cierre_menu == 0:
        try:
            print("¿Desea agregar otro Handroll?")
            print("1. Pikachu Roll $4500, \n2. Otaku Roll $5000 \n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800:\n5. Salida ")
            handroll_seleccionado = int(input("Ingrese el tipo de handroll que desea: "))
        except ValueError:
            if handroll_seleccionado == 1:
                print("Ingreso opcion 1. Pikachu Roll $4500")
                cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                cantidad_total += cantidad_handroll*4500
                opcion_1 += cantidad_handroll
                time.sleep(2)
                os.system(limpiar_pantalla)
            elif handroll_seleccionado == 2:
                print("Ingreso opcion 2. Otaku Roll $5000")
                cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                cantidad_total += cantidad_handroll*5000
                opcion_2 += cantidad_handroll
                time.sleep(2)
                os.system(limpiar_pantalla)
            elif handroll_seleccionado == 3:
                print("Ingreso opcion 3. Pulpo Venenoso Roll $5200")
                cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                cantidad_total += cantidad_handroll*5200
                opcion_3 += cantidad_handroll
                time.sleep(2)
                os.system(limpiar_pantalla)
            elif handroll_seleccionado == 4:
                print("Ingreso opcion 4. Anguila electrica $4800")
                cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                cantidad_total += cantidad_handroll*4800
                opcion_4 += cantidad_handroll
                time.sleep(2)
                os.system(limpiar_pantalla)
            elif handroll_seleccionado == 5:
                print(f"=====================\nTOTAL PRODUCTOS: {(opcion_1+opcion_2+opcion_3+opcion_4)} \n=====================")
                print(f"Pikachu Roll = {opcion_1}")
                print(f"Otaku Roll = {opcion_2}")
                print(f"Pulpo Venenoso Roll = {opcion_3}")
                print(f"Anguila electrica Roll = {opcion_4} ")
                print(f"=====================\nTOTAL A PAGAR = {cantidad_total}\n=====================")
                cierre_menu = 1
                cierre_app = 1
            else:
                print("ingrese una opcion valida")
                time.sleep(2)
                os.system(limpiar_pantalla)
