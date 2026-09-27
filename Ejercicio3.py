
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad_str = input("Ingrese su edad: ")
edad = int(edad_str)
email = input("ingrese su email: ")

if nombre == "":
    print("Error en el nombre")
else:
    print(nombre)

if apellido =="":
    print("Error en el apellido")
else:
    print(apellido)

if edad_str == "":
    print("Error en la edad")
else:
    print(edad_str)

if edad >= 18:
    print("Es mayor")
else:
    print("No es mayor")

if email == "":
    print("Error en el email")
else:
    print(email)

