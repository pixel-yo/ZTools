from os import system
from colorama import Fore, init

init()

system("title pixel.loca.lt")

print(Fore.GREEN + "Appuyez sur entrer pour lancer le serveur")

system("pause")

system("cls")
system("node server")
system("cls")
print(Fore.CYAN + "serveur lancé avec succès !")