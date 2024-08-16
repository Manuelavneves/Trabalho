from operacoes import calcular_media, verificar_reprovacao, identificar_alunos_reprovados

dados_alunos = {
    101: {'nome': 'Carlos', 'notas': [7, 6.5, 5.5, 6], 'media': 0},
    102: {'nome': 'Maria', 'notas': [5, 5.5, 6, 5.5], 'media': 0},
    103: {'nome': 'Ana', 'notas': [8, 7, 7.5, 8], 'media': 0},
}

for matricula, aluno in dados_alunos.items():
    media = calcular_media(aluno['notas'])
    dados_alunos[matricula]['media'] = media

matriculas_reprovados = [matricula for matricula, aluno in dados_alunos.items() if verificar_reprovacao(aluno['media'])]

alunos_reprovados = identificar_alunos_reprovados(dados_alunos, matriculas_reprovados)
for aluno_reprovado in alunos_reprovados:
    print(aluno_reprovado)