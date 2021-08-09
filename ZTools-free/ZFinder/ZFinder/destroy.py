import colorama
from colorama import Fore, init
import os
from os import system
import webbrowser
import time
import requests
import pyfiglet


init()

url = 'https://discord.gg/kmCJ25nPcY'

center = " "*51

def clear():
    os.system('cls')

def open_main():
    system("mode 125, 20")
    system("title [BÊTA] - ZDestroy by Zelron - https://discord.gg/kmCJ25nPcY")

def back():
    input(f"\n{Fore.YELLOW}Appuyez sur entrée pour allez au menu")
    main()

def quit():
    print(Fore.YELLOW + "\n[1] Discord\n[2] Menu\n[3] Détruire un webhook\n[4] Spam le webhook\n[0] Quitter\n\n")
    leave = int(input("sélectionnez : "))

    if leave == 0:
        logo()
        print(Fore.GREEN + "\nFermeture en cour\nMerci d'avoir utilisé le ZFinder a bientôt... ")

        time.sleep(3)
    
    if leave == 1:
        webbrowser.open(url)
        main()
    
    if leave ==2:
        main()

    if leave ==3:
	    os.system("python destroy.py")

    if leave ==4:
	    os.startfile("spam.py")
		
        
    
    else:
        logo()
        print(Fore.RED + "Le programe demandé n'est pas disponible")
        back()

def logo():
    clear()
    print(f"""

	
                        ███████╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
                        ╚══███╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
                          ███╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
                         ███╔╝  ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
                        ███████╗██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
                        ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                     
                               		    Par Zelron | {url}                        Beta 0.6
		""".replace('█', f'{Fore.YELLOW}█{Fore.WHITE}'))

def main():
    open_main()
    logo()
    filename = (input(str(f"{center}[>] Entrez le nom du fichier : ")))

banner = pyfiglet.figlet_format("Destroy")
print(banner)
hook = input("WebHook URL: ")
def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(Fore.GREEN + "\n [STATUS] Webhook détruit")
    elif check.status_code == 200:
        print(Fore.RED + "\n [STATUS] Erreur durant la suppression du webhook")

kingman_top = 1
if kingman_top == 1:
    delete(hook)

quit()