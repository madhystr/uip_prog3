l= "LISTA DE SUPERMERCADO"
lista=["pan","leche","azucar","sal","arroz","huevo","cereal","javon","poroto","lenteja"]
print (l, lista)
print ("¿Que desea hacer?")
a= int (input("1 = agregar articulo ó  2 = borrar articulo"))
if a==1:
	for i in range(1):
		arti= input("inserte nombre de articulo que desea agregar")
		lista.append(arti)
	print (l, lista)
else: 
	print ("¿que articulo deseas eliminar?")
	del lista[int(input("indica la posicion de articulo a eliminar"))]
print (l, lista)
