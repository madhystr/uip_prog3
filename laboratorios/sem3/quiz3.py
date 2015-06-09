
nombre= input("Nombre del Vendedor")

venta1= int(input("ingerese venta 1: "))
venta2= int(input("ingerese venta 2: "))
venta3= int(input("ingerese venta 3: "))

ventatotal=venta1+venta2+venta3

comision=(ventatotal*12.5)/100

print("INFORME DE COMICIONES\nVENDEDOR\t\t\tVENTAS\t\t\tCOMISION\n\n"+ nombre +"\t\t\t" + str(ventatotal) + "\t\t\t" + str(comision)) 

