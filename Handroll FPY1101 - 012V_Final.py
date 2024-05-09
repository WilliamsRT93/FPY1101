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
cierre_boleta = 0
limpiar_pantalla = "cls"
os.system(limpiar_pantalla)
while cierre_app == 0:
    print("Delivery Handroll Otaku")
    while cierre_menu == 0:
        cantidad_handroll =0
        try:
            print("¿Que desea Tipo de Handroll desea agregar?")
            print("1. Pikachu Roll $4500, \n2. Otaku Roll $5000 \n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800:\n5. Salida ")
            handroll_seleccionado = int(input("Ingrese el tipo de handroll que desea: "))
            if handroll_seleccionado == 1:
                while cantidad_handroll >= 0:
                    try:
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        print("Ingreso opcion 1. Pikachu Roll $4500")
                        cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                        cantidad_total += cantidad_handroll*4500
                        opcion_1 += cantidad_handroll
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        break
                    except ValueError:
                        print("Valor erroneo")
            elif handroll_seleccionado == 2:
                while cantidad_handroll >= 0:
                    try:
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        print("Ingreso opcion 2. Otaku Roll $5000")
                        cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                        cantidad_total += cantidad_handroll*5000
                        opcion_2 += cantidad_handroll
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        break
                    except ValueError:
                        print("Valor erroneo")                
            elif handroll_seleccionado == 3:
                while cantidad_handroll >= 0:
                    try:
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        print("Ingreso opcion 3. Pulpo Venenoso Roll $5200")
                        cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                        cantidad_total += cantidad_handroll*5200
                        opcion_3 += cantidad_handroll
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        break
                    except ValueError:
                        print("Valor erroneo") 
            elif handroll_seleccionado == 4:
                while cantidad_handroll >= 0:
                    try:
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        print("Ingreso opcion 4. Anguila electrica $4800")
                        cantidad_handroll = int(input("Ingrese la cantidad de handroll que desea: "))
                        cantidad_total += cantidad_handroll*4800
                        opcion_4 += cantidad_handroll
                        time.sleep(2)
                        os.system(limpiar_pantalla)
                        break
                    except ValueError:
                        print("Valor erroneo") 
            elif handroll_seleccionado == 5:
                while cierre_boleta == 0:
                    time.sleep(2)
                    os.system(limpiar_pantalla)                    
                    try:
                        codigo_desc = str(input("¿Posee un codigo de descuento?\nNo posee ingrese NO.\nSi posee un codigo ingreselo: "))
                        codigo_desc = codigo_desc.upper()
                        if codigo_desc == "NO":
                            print(f"=====================\nTOTAL PRODUCTOS: {(opcion_1+opcion_2+opcion_3+opcion_4)} \n=====================")
                            print(f"Pikachu Roll = {opcion_1}")
                            print(f"Otaku Roll = {opcion_2}")
                            print(f"Pulpo Venenoso Roll = {opcion_3}")
                            print(f"Anguila electrica Roll = {opcion_4} ")
                            print(f"=====================\nTOTAL A PAGAR = {cantidad_total}\n=====================")
                            cierre_menu = 1
                            cierre_app = 1
                            cierre_boleta = 1
                            time.sleep(10)
                            os.system(limpiar_pantalla)    
                        elif codigo_desc == "SOYOTAKU":
                            print(f"=====================\nTOTAL PRODUCTOS: {(opcion_1+opcion_2+opcion_3+opcion_4)} \n=====================")
                            print(f"Pikachu Roll = {opcion_1}")
                            print(f"Otaku Roll = {opcion_2}")
                            print(f"Pulpo Venenoso Roll = {opcion_3}")
                            print(f"Anguila electrica Roll = {opcion_4} ")
                            print(f"Posee un codigo de descuento su descuento es de un 10%\nSu descuento es: {round(cantidad_total*0.1)}")
                            print(f"=====================\nTOTAL A PAGAR = {round((cantidad_total)*0.9)}\n=====================")
                            cierre_menu = 1
                            cierre_app = 1
                            cierre_boleta = 1
                            time.sleep(10)
                            os.system(limpiar_pantalla)
                        else:
                            cierre_boleta = 0
                            print("Ingrese una opcion valida")   
                    except ValueError:
                        print("Valor erroneo")
            else:
                print("ingrese una opcion valida")
                time.sleep(2)
                os.system(limpiar_pantalla)
        except ValueError:                
            print("ingrese un numero")
            time.sleep(2)
            os.system(limpiar_pantalla)