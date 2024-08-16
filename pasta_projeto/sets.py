set_inicial = {11, 12, 13, 14}
print("set1:", set_inicial)

set_inicial.add(15)

print("set2:", set_inicial)

set_inicial.update([1, 2, 3, 4, 5])

print("set3:", set_inicial)

set_inicial.discard(13)

print("set4:", set_inicial)

novo_set = {20, 21, 23, 1, 2}

print("set5:", novo_set)

uniao_sets = set_inicial.union(novo_set)
print("União:", uniao_sets)

interseccao_sets = set_inicial.intersection(novo_set)
print("Intersecção:", interseccao_sets)

diferenca_sets = set_inicial.difference(novo_set)
print("Diferença:", diferenca_sets)

diferenca_simetrica_sets = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica:", diferenca_simetrica_sets)
