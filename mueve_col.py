import numpy as np
m = np.array([[1,5,9,13,17],[2,6,10,14,18],[3,7,11,15,19],[4,8,12,16,20]])
print(m)

a=int(input("indice columna a cambiar: "))
if a == 0:
    print(m[:,[1,2,3,4,0]])
    print("la columna",a,"se mueve al final")

if a == 1:
    print(m[:,[0,2,3,4,1]])
    print("la columna",a,"se mueve al final")

if a == 2:
    print(m[:,[0,1,3,4,2]])
    print("la columna",a,"se mueve al final")

if a == 3:
    print(m[:,[0,1,2,4,3]])
    print("la columna",a,"se mueve al final")

if a == 4:
    print(m[:,[0,1,2,3,4]])
    print("la columna",a,"ya estaba en el final",)

else:
    print("no hay una columna con ese indice")
    