meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

meu_dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Manu', 'idade': 22, 'nacionalidade': 'angolana'}
})

print("Dicionário1:", meu_dicionario)

copia_dicionario = meu_dicionario.copy()

removido = meu_dicionario.pop(1)
print("dicionario2:", removido)
print("Dicionário3:", meu_dicionario)

ultimo_removido = meu_dicionario.popitem()
print("dicionario4:", ultimo_removido)
print("Dicionário5:", meu_dicionario)

meu_dicionario.clear()
copia_dicionario.clear()

chaves = [10, 20, 30]
novo_dicionario = dict.fromkeys(chaves, "valor padrão")

print("dicionário_new:", novo_dicionario.items())
print("dicionario_new_keys:", novo_dicionario.keys())
print("dicionario_new_values:", novo_dicionario.values())
