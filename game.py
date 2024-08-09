import random

# Configurações do baralho
naipes = ['♦', '♠', '♥', '♣']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
valores = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'J': 10,
    'Q': 10,
    'K': 10
}

def criar_baralho():
    """Cria um baralho de cartas"""
    cartas = []
    for naipe in naipes:
        for numero in numeros:
            cartas.append(f'{numero} {naipe}')
    return cartas

def calcular_pontos(mao):
    """Calcula a pontuação da mão do jogador"""
    pontos = 0
    ases = 0
    
    for carta in mao:
        numero = carta.split()[0]
        pontos += valores[numero]
        if numero == 'A':
            ases += 1
    
    while pontos <= 11 and ases > 0:
        pontos += 10
        ases -= 1
    
    return pontos



# ----------------------------------------------------------
#def criar_baralho():
#    """Cria um baralho de cartas."""
#    return [f'{numero} {naipe}' for naipe in naipes for numero in numeros]

#def calcular_pontos(cartas_jogador):
#    """Calcula a pontuação do jogador com base nas cartas na mão."""
#    pontos = 0
#    ases = 0
#    for carta in cartas_jogador:
#        numero = carta.split()[0]
#        pontos += valores[numero]
#        if numero == 'A':
#            ases += 1
    # Ajustar os pontos se houver ases e o total ultrapassar 21
#    while pontos + 10 <= 21 and ases:
#        pontos += 10
#        ases -= 1
#    return pontos
#-------------------------------------------------------------