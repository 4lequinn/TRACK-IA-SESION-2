vTrue= True
while(vTrue==True):
    try:
        print("Ingrese una opción: ")
        print("1)Ingresar producto")
        print("2)Ver productos")
        print("3)Salir.")
        try:
            decision = int(input("Opción: "))
            if decision==1: 
                nuevoproducto = input("Ingrese nuevo producto: ")
                listaproductos.append(nuevoproducto)
            elif decision==2:
                vFalse = False
                while vFalse == False:
                    try:
                        print("Ingrese una opción: ")
                        print("1)Ver producto")
                        print("2)Salir")
                        des1 = int(input("Opción: "))
                        if des1 == 1:
                            busqueda = input("Ingrese el nombre del producto que busca: ")
                            for x in range(0, len(listaproductos), 1):
                                if listaproductos[x]==busqueda:
                                    print(f"Se ha encontrado el producto que busca: {listaproductos[x]} y cuesta tanto...")
                                    break
                                elif (x<len(listaproductos)):
                                    print("Buscando en la bd...")
                                elif (listaproductos[x]!=listaproductos[-1]):
                                    print("No se encontró su producto.")
                        elif des1 == 2:
                            print("Volviendo al menú anterior...")
                            vFalse = True
                        else:
                            print("Ingresa opción válida.")
                    except:
                        print("Ingresa caracter válido.")
            else: 
                vTrue= False
        except:
            print("Ingresa caracter válido.")
    except:
        print('Antes debes ingresar alguna cosa en la lista vacia.')
ciclo = 1
while ciclo < 2:
    print("MENU PRINCIPAL")
    print("1) Sumar")
    print("2) Restar")
    print("3) Cerrar")
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        print("SUMA")
        num1 = int(input("Ingrese número: "))
        num2 = int(input("Ingrese un segundo número: "))
        suma = num1+num2
        print(f"El resultado de la suma es {suma}")
    elif opcion == 2:
        print("RESTA")
        num1 = int(input("Ingrese número: "))
        num2 = int(input("Ingrese un segundo número: "))
        resta = num1-num2
        print(f"El resultado de la suma es {resta}")
    else:
        ciclo = 3