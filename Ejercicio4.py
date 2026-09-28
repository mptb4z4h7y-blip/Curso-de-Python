# 1.Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.
# 2.Asegure que el correo electrónico no tenga espacios y contenga solo una “@”.
# 3.Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años).


nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
edad_str = input("Ingrese su Edad: ")
edad = int(edad_str)
email = input ("Ingrese su email: ")

if nombre == "":
    print ("\n\nPor favor complete el campo ´Nombre´")

if apellido== "":
    print ("\nPor favor complete el campo ´Apellido´")

if edad == 0:
    print("\nPor favor complete el campo ´edad´ correctamente")
    
if edad >0 and edad <= 15:
    print ("\nEtapa de la vida: Es un niño/a")

elif edad > 15 and edad <= 17:
    print ("\nEtapa de la vida: Es un adolescente")

elif edad >= 18:
    print ("\nEtapa de la vida: Es un adulto")

if email.find("@") == -1:
    print("\nEmail:Lo que indicas no es un email")
if nombre != "" and apellido != "" and edad_str != "" and email != -1:
    print(f"\nNombre completo: {nombre.capitalize()} {apellido.capitalize()}\nEdad: {edad}     Email: {email.lower()} ")
else:
    print("\nCompleta la información de manera correcta para optener tu credencial ")

