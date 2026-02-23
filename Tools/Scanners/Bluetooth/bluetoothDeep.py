import asyncio
from bleak import BleakClient

# TUTAJ WKLEJ UUID LUB ADRES MAC URZĄDZENIA
# Na przykład to, które miało usługi 180a:
ADDRESS = "C0645146-E036-B4C4-3743-C07F7D8A6BED"

async def explore_device(address):
    print(f"Próba połączenia z {address}...")
    
    try:
        async with BleakClient(address) as client:
            if not client.is_connected:
                print("Nie udało się nawiązać połączenia.")
                return

            print(f"✅ Połączono! Pobieram usługi dla: {address}")
            print("-" * 60)

            # Przechodzimy przez wszystkie dostępne usługi (Services)
            for service in client.services:
                print(f"\n[Usługa] {service.uuid} ({service.description})")
                
                # W każdej usłudze sprawdzamy jej charakterystyki (Characteristics)
                for char in service.characteristics:
                    props = ", ".join(char.properties)
                    value_str = ""
                    
                    # Jeśli charakterystyka pozwala na odczyt (Read), spróbujmy pobrać dane
                    if "read" in char.properties:
                        try:
                            value = await client.read_gatt_char(char.uuid)
                            # Próbujemy zdekodować jako tekst, jeśli się nie da - pokazujemy hex
                            try:
                                value_str = f" | Wartość: {value.decode('utf-8')}"
                            except:
                                value_str = f" | Wartość (hex): {value.hex()}"
                        except Exception as e:
                            value_str = f" | Błąd odczytu: {e}"
                    
                    print(f"  └─ [Charakterystyka] {char.uuid} ({char.description}) | Uprawnienia: [{props}]{value_str}")

    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")

def main(adress):
    asyncio.run(explore_device(adress))

if __name__ == "__main__":
    main(ADDRESS)