import asyncio
from bleak import BleakScanner

COMPANY_IDS = {
    76: "Apple",
    6: "Microsoft",
    409: "Segway/Ninebot",
    208: "Xiaomi",
    117: "Samsung"
}

async def run():
    print("Skanowanie urządzeń Bluetooth (BLE)...")
    
    # discover() zwraca teraz krotki: (BLEDevice, AdvertisementData)
    devices_data = await BleakScanner.discover(return_adv=True)
    
    print(f"{'Nazwa':<30} | {'Adres MAC / UUID':<40} | {'RSSI':<10}")
    print("-" * 85)
    
    # Iterujemy po wartościach słownika (device to BLEDevice, adv to AdvertisementData)
    for device, adv in devices_data.values():
        name = device.name or "Nieznane"
        
        # Sprawdzamy ID producenta
        m_data = "Brak"
        if adv.manufacturer_data:
            # Wyświetlamy ID producenta (np. 76 dla Apple, 6 dla Microsoft)
            m_data = ", ".join([f"ID: {k} (Dane: {v.hex()})" for k, v in adv.manufacturer_data.items()])
        
        # Sprawdzamy UUID usług
        services = ", ".join(adv.service_uuids) if adv.service_uuids else "Brak"

        vendor = "Nieznany"
        if adv.manufacturer_data:
            for company_id in adv.manufacturer_data.keys():
                vendor = COMPANY_IDS.get(company_id, f"Inny ({company_id})")

        print(f"--- Urządzenie: {device.address} ---")
        print(f"Nazwa: {name}")
        print(f"RSSI: {adv.rssi} dBm")
        print(f"Producent: {vendor}")
        print(f"Usługi: {services}")
        print("-" * 40)
    
def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()