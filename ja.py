import random

def rolar_dado(lados):
    return random.randint(1, lados)

def todos_na_maior_face():
    tentativas = 0
    while True:
        tentativas += 1
        if (rolar_dado(4) == 4 and
            rolar_dado(6) == 6 and
            rolar_dado(8) == 8 and
            rolar_dado(10) == 10 and
            rolar_dado(12) == 12 and
            rolar_dado(20) == 20):
            return tentativas

# Rodar múltiplas simulações
simulacoes = 100
resultados = []

for _ in range(simulacoes):
    tentativas = todos_na_maior_face()
    resultados.append(tentativas)
    print(f"Simulação {_ + 1}: {tentativas} tentativas")

media = sum(resultados) / simulacoes
print(f"\nMédia de tentativas em {simulacoes} simulações: {int(media)}")