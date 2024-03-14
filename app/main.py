import random

FLAG = "opt{Well_Done}"

INTRO = """
+---------+
| SHIFUMI |
+---------+
C'est un jeu de pierre / feuille / ciseaux
Le but est de gagner plusieurs fois
PIERRE gagne sur CISEAUX
CISEAUX gagne sur FEUILLE
FEUILLE gagne sur PIERRE
"""

class Symbol:
    def __init__(self, name, winner):
        self.name = name
        self.winner = winner

SYMBOLS = [
    Symbol("PIERRE", "FEUILLE"),
    Symbol("FEUILLE", "CISEAUX"),
    Symbol("CISEAUX", "PIERRE")
]

MAX_GAMES = 100
    
CPT_GAMES = 0

print(INTRO)

for _ in range(MAX_GAMES):
    CPT_GAMES += 1
    print(f'ROUND {CPT_GAMES}')
    mySymbol = random.choice(SYMBOLS)
    print(f'MOI JE JOUE: {mySymbol.name}')
    rep = input('VOTRE CHOIX: ')

    if not rep.strip() == mySymbol.winner:
        print('YOU LOOSE!!!')
        exit(0)
    else:
        print('YOU WIN.')

print(FLAG)
