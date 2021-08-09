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

data = "Webhook find by ZFinder - discord.gg/kmCJ25nPcY"

web = input(Fore.YELLOW + "[>] Entrez l'URL du webhook : ")

hook = Webhook(web)

data = input(Fore.YELLOW + "[>] Entrez un message à spam : ")

loop = 1

def clear():
    os.system("cls")

def invalid():
    print(Fore.RED("[-] Choix invalide"))

def stop():
    clear()
    print(Fore.YELLOW + "[>] Spam terminé")
    
    time.sleep(3)

def pause():
    clear()
    print(Fore.YELLOW + "[>] Spam interrompu")
    rep = input("Entrez reppour reprendre le spam")
    if rep =="rep":
        t1()
    else:
        invalid()

def t1():
    while loop  1:
        hook.send(data)
        clear()
        print(Fore.GREEN + "[>] Spam en cours...")
        quit = input("Entrez "+"exit"+"pour finir le spam ou"+"pause"+"pour le mettre en pause")
        if quit =="exit":
            stop()
        elif quit =="pause":
            pause()
        else:
            invalid()

print(Fore.RED + "[!] LE BOT VA S'APPRETER A SPAM, si vous êtes prêt, appuyez sur entrer (pour arrêter le programme, tapez "+"exit"+")")

os.system("pause")

t1()

os.system("exit")