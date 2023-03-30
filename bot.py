import cfs
from random import randint
import ripeti
import main
import compiti
import webbrowser
import sys

comandi = ["lancia una moneta", "cfs", "ripeti", "compiti", "cerca", "exit"]

def get_res(cmdn):

    global comandi

    cmd = cmdn.lower()

    res = ""

    if "testa" in cmd and "croce" in cmd or "lancia" in cmd and "moneta" in cmd:

        print("Lancio una moneta...")

        main.say("Lancio una moneta...")

        results = ["testa", "croce"]
        res = f'è uscito {results[randint(0, 1)]}'
    
    elif "cfs" in cmd:

        cfs.cfs()

    elif "ripeti" in cmd:

        ripeti.ripeti()

    elif "compiti" in cmd:

        compiti.compiti()

    if cmd.startswith("cerca"):

        if "youtube" in cmd:
            text = cmd.replace("youtube", "").replace("su", "").replace(" ", "+").replace("cerca", "")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={text}")
            textts = text.replace("+", " ")
            res = f"Cerco {textts} su youtube..."

        if "wikipedia" in cmd:
            text = cmd.replace("wikipedia", "").replace("su", "").replace(" ", "_").replace("cerca", "")
            webbrowser.open_new_tab(f"https://it.wikipedia.org/wiki/{text}")
            textts = text.replace("_", " ")
            res = f"Cerco {textts} su wikipedia..."

        else:
            if not "youtube" in cmd:
                text = cmd.replace(" ", "+").replace("cerca", "")
                webbrowser.open_new_tab(f"https://duckduckgo.com/?q={text}&t=chromentp&ia=web")
                textts = text.replace("+", " ")
                res = f"Cerco {textts} su internet..."

    if cmd == "exit" or cmd == "esci":
        sys.exit()

    if "comandi" in cmd or cmd == "help":
        res = "Lista comandi: "
        for comando in comandi:
            if comando == comandi[len(comandi) - 1]:
                res = res + f"{comando}"
            else:
                res = res + f"{comando}, "

    if "timer" in cmd:

        args = cmd.split(" ")
        time = 0
        for arg in args:
            try:
                time = int(arg)
                break
            except ValueError:
                if arg == args[len(args) - 1]:
                    print("Inserisci un numero valido!")
                    main.say("Inserisci un numero valido!")
                    main.Main()
                continue

        seconds = 0
        if "minuti" in cmd or "minuto" in cmd:
            seconds = time * 60
        elif "secondi" in cmd or "secondo" in cmd:
            seconds = time
        elif "ore" in cmd or "ora" in cmd:
            seconds = time * 3600

        res = "Metto il timer!"

    return res