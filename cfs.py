from random import randint
import main

def cfs():

    print("\nCarta Forbici Sasso...\nscrivi exit per uscire!\nScrivi c per carta, f per forbici e s per sasso")
    cmd = input("\ncarta_forbici_sasso:> ").lower()

    if cmd == "exit":
        main.Main()

    mosse = ["c", "f", "s"]

    mossa_pc = mosse[randint(0, 2)]

    if not cmd in mosse:
        cfs()

    vincitore = ""

    if cmd == "f" and mossa_pc == "c":
        vincitore = "giocatore"
    elif cmd == "c" and mossa_pc == "s":
        vincitore = "giocatore"
    elif cmd == "s" and mossa_pc == "f":
        vincitore = "giocatore"
    elif cmd == mossa_pc:
        vincitore = "pareggio"
    else:
        vincitore = "pc"

    print(f"\nMossa giocatore: {cmd}")
    print(f"Mossa PC: {mossa_pc}")

    if vincitore == "giocatore":
        print("\nHai vinto tu!")
        main.say("Hai vinto tu!")
    elif vincitore == "pareggio":
        print("\nPareggio!")
        main.say("Pareggio!")
    else:
        print("\nHa vinto il pc!")
        main.say("Ha vinto il pc!")

    cfs()