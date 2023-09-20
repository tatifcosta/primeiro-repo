fruta = "mugangsssso"
lista1 = ["abacaxi", "mugango", "macaco", "pera", "goabis"]
lista2 = ["abacaxi", "mugangsssso", "macaco", "pera", "goabis"]

lista = [lista1, lista2]
for item in lista:
  if fruta in item:
    indice = item.index(fruta)
    print(f" o indice eh {indice}")
  else:
    print(  )
    print("nao encontrado")



