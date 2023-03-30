import bot
from gtts import gTTS
import os
import playsound

def say(frase):

    myobj = gTTS(text=frase, lang="it", slow=False)
    myobj.save("text.mp3")

    playsound.playsound('text.mp3', True)

    os.remove("text.mp3")

def play_audio(path):

    playsound.playsound(path, True)

def Main():

    cmd = input("cmd:> ")

    res = bot.get_res(cmd)

    if res == "":

        print("Non ho capito!")
        say("Non ho capito!")

        Main()

    print(res)

    say(frase=res)

    Main()

if __name__ == "__main__":
    Main()