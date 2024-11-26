from pwn import *

p = remote("localhost", 1337)

WINNERS = {
    "PIERRE": "FEUILLE",
    "FEUILLE": "CISEAUX",
    "CISEAUX": "PIERRE"
}

try:
    i = 0
    while True:
        i += 1
        rep = p.recvline_contains(b'MOI JE JOUE')
        reponse = rep.decode('ascii').split(":")[1].strip()
        p.info(f"{i}: {reponse}")
        p.recv()
        p.sendline(WINNERS[reponse].encode('ascii'))
except:
    p.warn(p.recv().decode('ascii'))