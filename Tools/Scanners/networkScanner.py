from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    print(f"Skanowanie sieci: {ip_range}...")
    
    # 1. Tworzymy pakiet ARP (pytanie o adres MAC)
    arp = ARP(pdst=ip_range)
    
    # 2. Tworzymy ramkę Ethernet (rozgłoszenie do wszystkich - broadcast)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Łączymy je w jeden stos
    packet = ether/arp

    # 3. Wysyłamy pakiet i czekamy na odpowiedzi (timeout 2 sekundy)
    result = srp(packet, timeout=2, verbose=False)[0]

    # 4. Parsowanie wyników
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    # Zazwyczaj Twoja sieć to 192.168.1.0/24 lub 192.168.0.0/24
    # Możesz to sprawdzić wpisując 'ifconfig' w terminalu
    target_ip = "192.168.1.0/24" 
    
    list_of_devices = scan_network(target_ip)

    print(f"{'IP Adres':<15} | {'MAC Adres':<20}")
    print("-" * 40)
    for device in list_of_devices:
        print(f"{device['ip']:<15} | {device['mac']:<20}")