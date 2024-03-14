from pwn import *
import random
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=10)

FLAG = '/app/flag'

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

def game(client: listen):
    CPT_GAMES = 0
    
    client.send(INTRO.encode('ascii'))

    try:
        while True:
            CPT_GAMES += 1
            client.sendline(b'\nROUND ' + str(CPT_GAMES).encode('ascii'))
            mySymbol = random.choice(SYMBOLS)
            client.send(b'MOI JE JOUE: ')
            client.sendline(mySymbol.name.encode('ascii'))
            client.send(b'VOTRE CHOIX: ')
            rep = client.recv()

            if not rep.decode('ascii').strip() == mySymbol.winner:
                client.sendline(b'YOU LOOSE!!!')
                client.close()
                break
            else:
                client.sendline(b'YOU WIN.')
            
            if CPT_GAMES == MAX_GAMES:
                CPT_GAMES = 0
                with open(FLAG, 'r') as f:
                    flag = f.readline()
                client.sendline(flag.encode('ascii'))
                client.close()
                break
    except Exception as err:
        client.close()
    
def run_server():
    while True:
        client = listen(8080).wait_for_connection()
        pool.submit(game, client)
            
run_server()

# pool.shutdown(wait=True)