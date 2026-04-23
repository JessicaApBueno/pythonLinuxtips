from datetime import datetime

# 1. Definimos os dados auxiliares primeiro
traducao_dias = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

# 2. Entrada de dados
data_usuario = input("Que dia é hoje? (dd/mm/aaaa): ")

# 3. Processamento com segurança
try:
    data_obj = datetime.strptime(data_usuario, "%d/%m/%Y")
    dia_ingles = data_obj.strftime('%A')
    dia_pt = traducao_dias[dia_ingles]
    print(f"Hoje é {dia_pt}!")

except ValueError:
    print("Erro: Digite uma data válida no formato dd/mm/aaaa")

# Lista de feriados (Strings)
feriados = ["01/01/2026", "25/12/2026", "01/05/2026", "07/09/2026"]

try:
    data_obj = datetime.strptime(data_usuario, "%d/%m/%Y")
    indice_dia = data_obj.weekday() 
    
    # Pergunta a hora (aceita apenas o número da hora)
    hora_usuario = int(input("Que horas são? (Apenas a hora 0-23): "))

    # Lógica de decisão
    if data_usuario in feriados:
        print("Fechada! Hoje é feriado, a padaria não abre. 🚩")
    elif indice_dia >= 5 and hora_usuario >= 12:
        print("Fechada! Sábado e domingo a padaria fecha após o meio-dia. 😴")
    else:
        print("Pode ir! A padaria está aberta. 🥖")

except ValueError:
    print("Erro: Digite a data em dd/mm/aaaa e a hora apenas como um número inteiro.")