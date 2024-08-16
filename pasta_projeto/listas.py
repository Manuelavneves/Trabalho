lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print("lista1:", lista_mesclada)

lista_mesclada.append(["Lista aninhada"])
print("lista2:", lista_mesclada)

lista_mesclada.insert(4, 5)
print("lista3:", lista_mesclada)
print("Tamanho_lista:", len(lista_mesclada))

lista_mesclada.pop(1)
print("lista4:", lista_mesclada)

nova_lista_mesclada = lista_mesclada[:4]
print("lista5:", nova_lista_mesclada)
