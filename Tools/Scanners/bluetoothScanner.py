import asyncio
from bleak import BleakScanner

async def run():
    print("Skanowanie urządzeń Bluetooth (BLE)...")
    
    # discover() zwraca teraz krotki: (BLEDevice, AdvertisementData)
    devices_data = await BleakScanner.discover(return_adv=True)
    
    print(f"{'Nazwa':<30} | {'Adres MAC / UUID':<40} | {'RSSI':<10}")
    print("-" * 85)
    
    # Iterujemy po wartościach słownika (device to BLEDevice, adv to AdvertisementData)
    for device, adv in devices_data.values():
        name = device.name if device.name else "Nieznane"
        # RSSI wyciągamy teraz z obiektu adv
        print(f"{name:<30} | {device.address:<40} | {adv.rssi} dBm")

if __name__ == "__main__":
    asyncio.run(run())