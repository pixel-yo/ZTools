import colorama
from colorama import Fore, init
import os
from os import system
import webbrowser
import time

init()

url = 'https://discord.gg/kmCJ25nPcY'

center = " "*51

def clear():
    os.system('cls')

def open_main():
    system("mode 125, 20")
    system("title [BÊTA] - ZFinder by Zelron - https://discord.gg/kmCJ25nPcY")

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
	    os.startfile("startspam.bat")
		
        
    
    else:
        logo()
        print(Fore.RED + "Le programe demandé est innacessible")
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
                                                     
                               		    Par Zelron | {url}                        Beta V0.1.1
		""".replace('█', f'{Fore.YELLOW}█{Fore.WHITE}'))

def main():
    open_main()
    logo()
    filename = (input(str(f"{center}[>] Nom du fichier : ")))

    os.system(f'cd ./exe && python ../extractor/pyinstxtractor.py "{filename}.exe"')
    pycfile  = ''
    try:
        for file in os.listdir(f'./exe/{filename}.exe_extracted/'):
            if '.exe.manifest' in file:
                pycfile = file.split('.exe.manifest')[0]
                if 'pyi-windows-manifest-filename' not in pycfile:
                    with open(f'./exe/{filename}.exe_extracted/{pycfile}.pyc', 'r+', encoding= 'utf-8', errors= 'ignore') as data_input:
                        for line in data_input:
                            if 'PYARMOR' in line:
                                logo()
                                print(Fore.RED + '\n[-] Error: Le fichier ne peux pas être décompilé cela arrivera dans une prochaine version')
                                back()

                            if '/api/webhooks/' in line:
                                hook = (line.split('/api/webhooks/')[1])[:87].split(')')[0]
                                logo()
                                webhook = (f'{Fore.YELLOW}[>] {Fore.GREEN}https://discord.com/api/webhooks/{hook}')
                                print(webhook)
                                print(f"\n{Fore.YELLOW}[>] Pour détruire le webhook, Tapez 3 : ")
                                quit()
                            
                            if '/api/v1/post/webhook' in line:
                                clear()
                                hook = (line.split('/api/v1/post/webhook/')[1])[:6].split(')')[0]
                                logo()
                                webhook = (f'{Fore.GREEN}[>] {Fore.WHITE}https://billy.loce.lt/api/v1/post/webhook/{hook}')
                                print(webhook)
                                print(f"\n{Fore.GREEN}[>]{Fore.WHITE} Pour détruire le webhook, Tapez 3, Pour spam le webhook, tapez 4 : ")
   
    except Exception as err:
        logo()
        print(f"{Fore.RED}[-] Error: {err}\n Si le fichier est en .py, le finder ne peut pas l'ouvrir pendant la beta")
        back()

main()
