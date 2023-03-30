import main

def ripeti():

    print("Scrivi una frase e io la ripeterò...\nscrivi exit per uscire!")

    cmd = input("\nripeti:> ").lower()

    if cmd == "exit":
        main.Main()

    main.say(frase=cmd)

    ripeti()