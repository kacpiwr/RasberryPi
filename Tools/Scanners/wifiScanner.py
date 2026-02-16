import pywifi
from pywifi import PyWiFi, const
import time

def scan_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # Pobranie pierwszego dostępnego interfejsu

    iface.scan()  # Uruchomienie skanowania
    print("Skanowanie w toku...")
    time.sleep(2)  # Czekamy chwilę na zebranie wyników

    results = iface.scan_results()

    print(f"{'SSID':<25} | {'Sygnał (dBm)':<12}")
    print("-" * 40)
    for network in results:
        print(f"{network.ssid:<25} | {network.signal:<12}")

if __name__ == "__main__":
    scan_wifi()