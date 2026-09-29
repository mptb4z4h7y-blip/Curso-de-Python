print("Detalle de acuerdo al mes, el valor ingresado ($)\n\n\n")

mes = 1
suma = 0

while mes < 7:
    ingreso = input (f"ingreso del mes {mes}: $ ")
    if float(ingreso) > 0:
        mes += 1
        suma += float(ingreso)
    else:
        print ("No se permiten ingresos negativos. Intente nuevamente.")

prom = (float(suma) / 6)

print (f"\n\nLa suma de los ingresos es: {suma}")
print (f"El promedio de los ingresos es: {prom}")    
    
    

