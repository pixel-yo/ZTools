from dhooks import Webhook
import os
import colorama
from colorama import Fore, init
import time
import threading
from threading import Thread

init()

os.system("title [BÊTA] - ZSpamer by Zelron - https://discord.gg/kmCJ25nPcY")

os.system ("@echo off")

loop = 1

data = "Webhook find by ZFinder - discord.gg/kmCJ25nPcY"



web = input(Fore.YELLOW + "[>] Entrez l'URL du webhook : ")

hook = Webhook(web)

data = input(Fore.YELLOW + "[>] Entrez un message à spam : ")

def stop():
    os.system("cls")
    print(Fore.BLUE + "Merci d'avoir utilisé le spameur et à bientôt !")
    
    time.sleep(3)


def t1():
    while loop < 2:

        hook.send(data)
        print(Fore.GREEN + "[>] Le message a été envoyé !")

print(Fore.RED + "[!] LE BOT VA S'APPRETER A SPAM, si vous êtes prêt, appuyez sur entrer (pour arrêter le programme, tapez 'exit')")

os.system("pause")

t1()

os.system("exit")