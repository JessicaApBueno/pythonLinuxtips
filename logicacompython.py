import requests
from datetime import datetime

# === CONFIGURAÇÕES ===
api_key = "4640a559e4d429d0af68ec163810fb44"
cidade = "Cotia"
feriados = ["01/01/2026", "25/12/2026", "01/05/2026", "07/09/2026"]

traducao_dias = {
    "Monday": "segunda-feira", "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira", "Thursday": "quinta-feira",
    "Friday": "sexta-feira", "Saturday": "sábado", "Sunday": "domingo"
}

# === ENTRADA DE DADOS ===
print("--- Assistente da Padaria & Clima ---")
data_input = input("Que dia é hoje? (dd/mm/aaaa): ").strip()

try:
    hora_raw = input("Que horas são? (0-23): ").strip()
    # Pega apenas a hora antes de qualquer ':' e converte para número
    hora_input = int(hora_raw.split(':')[0])

    # 1. Processamento da Data
    data_obj = datetime.strptime(data_input, "%d/%m/%Y")
    indice_dia = data_obj.weekday() 
    dia_semana_en = data_obj.strftime('%A')
    dia_semana_pt = traducao_dias[dia_semana_en]

    print(f"\n📅 Analisando: {data_input} ({dia_semana_pt}) às {hora_input}h")

    # 2. Lógica da Padaria
   # LÓGICA DA PADARIA (Exemplo: Semana até as 20h, Fim de semana até as 12h)
    aberta = True
    if data_input in feriados:
        print("🚩 Status: FECHADA! Hoje é feriado.")
        aberta = False
    elif indice_dia < 5 and (hora_input < 6 or hora_input >= 20):
        print("😴 Status: FECHADA! Abrimos das 06:00 às 20:00 nos dias de semana.")
        aberta = False
    elif indice_dia >= 5 and (hora_input < 6 or hora_input >= 12):
        print("😴 Status: FECHADA! No fim de semana abrimos apenas das 06:00 às 12:00.")
        aberta = False
    else:
        print("🥖 Status: ABERTA! Pode ir buscar seu pão.")

    # 3. Consulta à API de Clima (Somente se estiver aberta)
    if aberta:
        print(f"\n☁️  Verificando o clima em {cidade}...")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
        
        resp = requests.get(url).json()

        if resp.get("cod") != 200:
            # Isso vai nos mostrar o erro real que a API está devolvendo
            print(f"⚠️ Erro da API: {resp.get('message')}")
        else:
            temp = resp['main']['temp']
            condicao = resp['weather'][0]['main']
            desc = resp['weather'][0]['description']

            print(f"🌡️  Temperatura atual: {temp}°C ({desc.capitalize()})")

            # Avisos
            if condicao == "Rain" or "chuva" in desc.lower():
                print("☔ DICA: Leve um guarda-chuva!")
            elif temp > 28:
                print("💧 DICA: Está calor, leve água!")
            else:
                print("👟 DICA: Sem avisos, boa caminhada!")

except ValueError:
    print("\n❌ Erro: Formato de data ou hora inválido!")
except Exception as e:
    print(f"\n❌ Erro inesperado: {e}")