import random

##Listas de elementos para gerar a missão.
missoes = [
    "Infiltração",
    "Resgate",
    "Reconhecimento",
    "Sabotagem",
    "Extração"
]

ambientes = [
    "Data center abandonado",
    "Base militar secreta",
    "Cidade Cyberpunk",
    "Complexo Industrial"
]

riscos = [
    "Baixo",
    "Médio",
    "Alto",
    "Extremo"
]

estilos = [
    "RPG",
    "Cyberpunk",
    "Militar"
]

##Função para gerar uma missão.
def gerar_missao():
    missao = random.choice(missoes)
    ambiente = random.choice(ambientes)
    risco = random.choice(riscos)
    estilo = random.choice(estilos)

    print("\n🎯 Cenário Gerado! ")
    print("---------------------")
    print(f"Missão: {missao}")
    print(f"Ambiente: {ambiente}")
    print(f"Nível de Risco: {risco}")
    print(f"Estilo: {estilo}")
    print("---------------------")
    print("Boa sorte, agente!")

##execução do gerador de missões.
if __name__ == "__main__":
    gerar_missao()