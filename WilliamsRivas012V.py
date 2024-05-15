#PruebaN2.
import time, os
clean = "cls"
nombre_usuario = ""
nombre_cliente = ""
validador_usuario = 0
telefono_contacto = 0
validador_telefono = 0
valor_5K = 0
cilindro_5k = 0
valor_15k = 0
cilindro_15k = 0
valor_45k = 0
cilindro_45k = 0
opcion_cilindro = 0
cierre_menu = 0
cierre_app = 0
opcion_compra = 0
cierre_opcion = 0
cierre_boleta = 0
cantidad_camiones = 1
pedido_estandar = 0
pedido_personalizado = 0
time.sleep(1)
os.system("cls")
while cierre_app == 0:
    print("Bienvenido a transportes de gas")
    
    while validador_usuario == 0:
        nombre_usuario = str(input("ingrese su nombre: "))
        nombre_cliente = nombre_usuario
        nombre_usuario = len(nombre_usuario)
        if nombre_usuario >=3:
            validador_usuario = 1
        else:
            print("ingrese un nombre superior a 3 letras")
            time.sleep(1)
            os.system("cls")

    while validador_telefono == 0:
        try:
            telefono_contacto = int(input("Ingrese su numero de contacto: "))
            validador_telefono = str(telefono_contacto)
            validador_telefono = len(validador_telefono)
            if validador_telefono >=8 and validador_telefono <=9:
                validador_telefono = 1
            else:
                print("ingrese un numero entre 8 y 9 digitos")
                validador_telefono = 0
                time.sleep(1)
                os.system("cls")
        except ValueError:
            print("ingrese un digito que no es numerico")
    
    while cierre_menu == 0:
        time.sleep(1)
        os.system("cls")
        cierre_opcion = 0
        try:
            print(f'''
El catalogo es el siguiente.
1 - Entrega camion estandar. (indique la cantidad de camiones)
    esta compra consiste en 12 cilindros de 5 kilos, 20 cilindros de 15 kilos y 2 cilindros de 45 kilos
    Esto tiene un valor de 765.000
2- Entrega personalizada, (debera indicar la cantidad de cilindros que desea cargar)
    Si un camion no se completa, pagara multa de 100.000
    Y 1.700 por kilo de gas
3- Cerrar pedido y visualizar boleta''')
            opcion_compra = int(input("ingrese la opcion que desea comprar: "))
            if opcion_compra == 1:
                while cierre_opcion ==0:
                    time.sleep(1)
                    os.system("cls")
                    try:
                        cantidad_camiones = int(input("ingrese la cantidad de camiones estandar que desea de este pedido: "))
                        pedido_estandar = cantidad_camiones
                        cierre_opcion = 1
                    except ValueError:
                        print("ingrese un caracter numerico")
            elif opcion_compra == 2:
                time.sleep(1)
                os.system("cls")
                print("escogio la opcion de entrega personalizada")
                while cierre_opcion == 0:
                    try:
                        opcion_cilindro = int(input('''
Eliga que su cilindro que desea agregar
Cada camion debera cargar 450 Kilos
1 - Cilindro de 5 kilos
2 - cilindro de 15 kilos
3 - cilindro de 45 kilos
4 - Cerrar pedido                                                
Ingrese la opcion que necesita : '''))
                        if opcion_cilindro == 1:
                            while True:
                                time.sleep(1)
                                os.system("cls")
                                try:
                                    cilindro_5k = int(input("ingrese la cantidad de cilindros de 5 kilos: "))
                                    if cilindro_5k <=0:
                                        print("ingrese un numero mayor que 0")
                                        continue
                                    else:
                                        time.sleep(1)
                                        os.system("cls")
                                        break
                                except ValueError:
                                    print("ingrese un caracter numerico")
                        elif opcion_cilindro == 2:
                            while True:
                                time.sleep(1)
                                os.system("cls")
                                try:
                                    cilindro_5k = int(input("ingrese la cantidad de cilindros de 15 kilos: "))
                                    if cilindro_15k <=0:
                                        print("ingrese un numero mayor que 0")
                                        continue
                                    else:
                                        time.sleep(1)
                                        os.system("cls")                                        
                                        break
                                except ValueError:
                                    print("ingrese un caracter numerico")
                        elif opcion_cilindro == 3:
                            while True:
                                time.sleep(1)
                                os.system("cls")
                                try:
                                    cilindro_45k = int(input("ingrese la cantidad de cilindros de 45 kilos: "))
                                    if cilindro_45k <=0:
                                        print("ingrese un numero mayor que 0")
                                        continue
                                    else:
                                        time.sleep(1)
                                        os.system("cls")                                        
                                        break
                                except ValueError:
                                    print("ingrese un caracter numerico")
                        elif opcion_cilindro == 4:
                            cierre_opcion = 1
                        else:
                            print("ingrese una opcion valida")
                            time.sleep(1)
                            os.system("cls")                            
                    except ValueError:  
                        print("ingrese un caracter numerico")
            elif opcion_compra == 3:
                time.sleep(1)
                os.system("cls")                  
                print("Visualizar pedido y boleta")
                print(f'''
Cliente : {nombre_cliente}
Numero telefonico : {telefono_contacto}
Cantidad de kilos:  {(pedido_estandar*450)+((cilindro_15k*15)+(cilindro_5k*5)+(cilindro_45k*45))}
Cantidad de camiones: {(int(((pedido_estandar*450)+(cilindro_15k*15)+(cilindro_5k*5)+(cilindro_45k*45))/450)+1)}
Valor total : {round((pedido_estandar*765000)+(((cilindro_5k+cilindro_15k+cilindro_45k)*1700))+100000)}''')
                while True:
                        cierre_boleta = input("¿Desea realizar otro pedido? (Si o No): ")
                        cierre_boleta = cierre_boleta.upper()
                        if cierre_boleta == "SI":
                            cierre_menu = 0
                            cierre_app = 0
                            nombre_usuario = ""
                            nombre_cliente = ""
                            validador_usuario = 0
                            telefono_contacto = 0
                            validador_telefono = 0
                            valor_5K = 0
                            cilindro_5k = 0
                            valor_15k = 0
                            cilindro_15k = 0
                            valor_45k = 0
                            cilindro_45k = 0
                            opcion_cilindro = 0
                            cierre_menu = 0
                            cierre_app = 0
                            opcion_compra = 0
                            cierre_opcion = 0
                            cierre_boleta = 0
                            cantidad_camiones = 1
                            pedido_estandar = 0
                            pedido_personalizado = 0
                            time.sleep(1)
                            os.system("cls")
                            break
                        elif cierre_boleta == "NO":
                            cierre_menu = 1
                            cierre_app = 1
                            print("Gracias por su preferencia")
                            time.sleep(1)
                            os.system("cls")
                            break
                        else:
                            print("ingrese una opcion valida")
                            continue
            else:
                print("ingrese una opcion valida")
        except ValueError:
            print("ingreso un caracter erroneo")
