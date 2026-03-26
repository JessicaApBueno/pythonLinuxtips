#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade."""
__version__ = "0.1.0"

sala1 = ["Erick", "Natasha", "Luana", "Higor"]
sala2 = ["Ludmila", "Vera", "Luan", "James"]

aula_ingles = ["Natasha", "Luana"]
aula_musica = ["Vera", "Luan", "Ludmila"]
aula_danca = ["Erick", "Higor", "James"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Dança", aula_danca), 
    ("Música", aula_musica)
]

for nome_atividade, atividade in atividades:

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"Atividade: {nome_atividade}")
    print(f"Sala 1: {atividade_sala1}")
    print(f"Sala 2: {atividade_sala2}")
    print("-" * 50)