# Program do zmiany adresu MAC napisany przez tomektiger

#Importujemy moduly
import subprocess

#Funkcja pobierajaca input
print("Zmiana Adresu MAC: ")
print("Przed przystąpieniem do zmiany adresu MAC, odłącz się od wszystkich sieci WI-FI")
interface = input("PODAJ INTERFEJS ----> ")
new_mac = input("PODAJ NOWY ADRES MAC ----> ")

#Funkcja zmieniajaca adres MAC
def change_mac(interface,new_mac):
    print("[+] Zmieniam adres MAC dla interfejsu " + interface + " na "+ new_mac + "\n")
    subprocess.call(["ifconfig", interface, "ether", new_mac])


#Zmieniamy adres MAC
change_mac(interface, new_mac)
