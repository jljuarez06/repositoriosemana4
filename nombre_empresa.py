#ejercicio1
nombre_empresa = "Mi empresa"

def mostrar_empresa():
    print(nombre_empresa)

mostrar_empresa()

#ejercicio2
def calcular_total():
    total = 100
    print("dentro de la funcion:", total)

calcular_total()

print("fuera de la funcion:", total)

#el error es porque total es una variable local: solamente existe dentro de calcular_total().