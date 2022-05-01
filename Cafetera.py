#Variables cafe      Carlos Medrano--21578987-k  Eduardo Aguero 25627692-5
moca="1"
expresso="2"
latte="3"
capuchino="4"
italiano="5"

#Bucle
reinicio="1"

#Funciones
def pago():
    global cafe

    pagado=0
    while True:
        dinero=input("Ingrese El dinero: ")
        
        if (dinero == "500" or dinero == "100"):
            dinero=int(dinero)
            pagado=pagado+dinero
            dinero=str(dinero)
            print("Pagado:",pagado)
            if (pagado >= precio):
                vuelto=pagado-precio
                preparacion_de_cafe()
                print("Su vuelto es $"+str(vuelto))
                break
        else:
            print("Ingrese Una Moneda correcta")
def seleccion_cafe():
    global cafe,moca,expresso,latte,capuchino,italiano,precio
    
    while True:
        cafe=input("--->  ")
        if (cafe == moca):
            precio = 600
            cafe="Moca"
            break
        elif (cafe == expresso):
            precio = 800
            cafe="Expresso"
            break 
        elif (cafe == latte):
            precio = 500
            cafe="Latte"
            break 
        elif (cafe == capuchino):
            precio = 1000
            cafe="Capuchino"
            break 
        elif (cafe == italiano):
            precio = 1200
            cafe="Italiano"
            break
        else:
            print("seleccione una opcion valida.")
    lista_de_pedido.append(cafe)
    


   
    print("El precio es de $"+str(precio), "pesos")
    print("Recuerde que solo puede pagar con $500 o $100")
def preparacion_de_cafe():
    for i in range(6):
        print (".")
    print ("Aqui esta su cafe ☕")
def lista_de_cafe():
    print("Cafe 1 - Moca ---> 600",)
    print("Cafe 2 - Expresso ---> 800")
    print("Cafe 3 - Latte ---> 500 ")
    print("Cafe 4 - Capuchino ---> 1000")
    print("Cafe 5 - Italiano --->1200")          

#codigo principal

lista_de_pedido=[]
while (reinicio=="1"):
    print("Bienvenido a la Maquina de cafe")
    print("Por favor Ingrese el cafe de su preferencia")
    lista_de_cafe()
    seleccion_cafe()
    pago()
    print("1. Si desea pedir otro cafe \n2. Terminar porgrama y mostrar lista de pedidos ")
    while True:
        reinicio = input("---> ")
        if reinicio != "1" and reinicio != "2":
            print("Ingrese una opcion valida")
        else:
            print("⬇Estos Fueron Sus Pedidos⬇")
            print(lista_de_pedido)
            break
print("Gracias Por Preferirinos")
 