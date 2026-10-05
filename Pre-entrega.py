productos = ["pies de microfonos", "microfonos", "amplificadores", "cables","consolas"]
usuario = "FB798"
contrasena = "corbatta"
u_intentos = 0
max_uintentos = 10
c_intentos = 0
max_c_intentos = 3

#Inicio de sesion
#Usuario de ingreso: FB798
#Contraseña para ingreso: 12345
usuario = input("\nIngrese su usuario: ").strip()

while u_intentos < max_uintentos:
    if usuario != "FB798":
        print(input("\n\nIngrese nuevamente el nombre de usuario: ").strip())
        u_intentos += 1
        if u_intentos == max_uintentos:
            print("\n\n**Lo sentimos, se agotaron los intentos.\n\nintente más tarde**")
    if usuario == "FB798":
        print(f"\n\nHola {usuario}\n")
        break
        
    


#Bucle de contraseña

    
while c_intentos < max_c_intentos:
    
    contrasena = input("\nIngresa la contraseña: ").strip()
    
    if contrasena == "corbatta":
        print("**\n\n-------------------------\n\n Bienvenido FB798\n\n-------------------------\n\n")
        break
    if contrasena != "corbatta":
        print("***\nError en la contraseña\n***")
        c_intentos += 1
        resta = c_intentos - max_c_intentos
        print(f"\n** Te quedan {resta} intentos, antes que se bloquee la cuenta\n")
    if c_intentos == max_c_intentos:
        print("\n-------------------------\n\n***  Se agotaron los intentos, pruebe más tarde  ***\n\n")
    

#Bucle while true:
while True:
#Opciones para el usuario:
    opciones = input("*** Menu de opciones ***\n\nPara Agregar ingrese: A\n\nPara Buscar ingrese: B\n\nPara listar ingrese: L\n\nPara Remover ingrese: R\n\nPara salir ingrese: S\n-----------------------------------\n")


#Parte 1: menu de opciones
    if opciones.strip() == "S":
        print("\n\nCUBB")
        break
    elif opciones.strip() == "L":
        for producto in productos:
            print(producto)
        
    elif opciones.strip() == "B":#definicion de la busqueda.

        producto_buscar = input("\nQue equipo buscas: ").strip()
        
        if opciones.strip() == "":
            print("*Campo vacio*\n\nIngrese nuevamente:  ")
        
        if productos in producto_buscar.strip():
            print("\n\nProducto con stock\n\n****************\n")
        else:
            print("\n\nProducto sin stock\n\n***************\n")
        
    if opciones.strip() == "A":#definicion de agregar
    
        agregar = input("\n\nEquipo a ingresar: \n\n").strip()
        productos.append(agregar)
        print(f"\n\nAgregado con exito\n\n********************\n")
        
    elif opciones.strip() =="R":#Definicion de remover
        
        producto_remover = input("\n\nQue equipo desea remover: \n\n").strip()
        productos.remove(producto_remover)
        print("\n\nEl equipo se removio del stock\n\n******************\n")
