import asyncio
import os
from bleak import BleakClient

# Wstaw UUID urządzenia, które chcesz "pogonić" do grania
ADDRESS = "C0645146-E036-B4C4-3743-C07F7D8A6BED"

# Standardowe UUID dla Immediate Alert
ALERT_SERVICE_UUID = "00001802-0000-1000-8000-00805f9b34fb"
ALERT_CHAR_UUID = "00002a06-0000-1000-8000-00805f9b34fb"

async def make_some_noise(address):
    print(f"Łączenie z {address} w celu wywołania dźwięku...")
    
    try:
        async with BleakClient(address) as client:
            if client.is_connected:
                print("✅ Połączono!")
                
                print("Wysyłanie komendy: High Alert...")
                os.system("afplay /System/Library/Sounds/Ping.aiff")
                
                print("🔔 Komenda wysłana! Sprawdź czy urządzenie wydaje dźwięk.")
                await asyncio.sleep(2) # Dajmy mu chwilę na reakcję
            else:
                print("❌ Nie udało się połączyć.")
    except Exception as e:
        print(f"❌ Błąd: {e}")
        print("\nPodpowiedź: Jeśli dostajesz błąd 'Characteristic not found', "
              "to urządzenie nie obsługuje standardowego alarmu BLE.")

if __name__ == "__main__":
    asyncio.run(make_some_noise(ADDRESS))