l= "LISTA DE SUPERMERCADO"
lista=["pan","leche","azucar","sal","arroz","huevo","cereal","javon","poroto","lenteja"]
print (l)
print (lista)
a = input("¿Desea agregar un articulo a la lista?" )
lista.append(input("Inserte el nombre del articulo: "))
print (l)
print (lista)
b = input("¿Desea borrar un articulo de la lista?")
del lista[int(input("insete la posicion en que se encuentra el articulo: "))]
print (l)
print (lista)