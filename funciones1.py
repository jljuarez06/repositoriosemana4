#Leer la edad de una persona y decir si es mayor o menor de edad
age = 0
def readAge():
    print("Dime tu edad")
    global age
    age = int(input())

def avalAge(age):
    return age >= 18

def show():
    global age
    print("Mayor de edad" if avalAge(age) else "Menor de edad")

readAge()
show()