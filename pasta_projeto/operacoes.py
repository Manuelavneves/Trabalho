

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def identificar_alunos_reprovados(dados_alunos, matriculas_reprovados):
    resultado = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno['nome']
            media_final = aluno['media']
            resultado.append(f'Aluno Reprovado - {nome} - Matrícula: {matricula} - Média final: {media_final}')
    return resultado

