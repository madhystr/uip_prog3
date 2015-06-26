directorio = {"Maria":3997665,"Jose":2333837,"Juan":3995984}
print ("DIRECTORIO TELEFONICO")
print ("Que desea hacer?  " "1: agregar, 2: buscar, 3: eliminar, 4: Imprimir")
x= int (input("ingrese el numero de lo que desea realizar"))
if x==1:
    print ("ingrese los datos correctos")
    directorio[input("ingrese el nombre")]= input("ingrese el numero telefonico")
    print (directorio)
elif x==2:
    print ("ingrese los datos correctos de la persona que desea buscar")
    dic= input("Ingrese el nombre: ")
    print (directorio[dic])
elif x==3:
    print ("ingrese datos correctos que desea eliminar")
    eli= input ("Ingrese el nombre") 
    del directorio [eli]
    print (directorio)
else:
    print ("La informacion de su directorio es:  " )
    print (directorio)