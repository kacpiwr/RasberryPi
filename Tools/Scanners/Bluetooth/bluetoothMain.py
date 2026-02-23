import bluetoothScanner
import bluetoothDeep
import signalBluetooth

def main():
    print("Starting Bluetooth Scanner...")
    bluetoothScanner.main()

    adress = input("Enter the Bluetooth device address (MAC or UUID) for deep scan and signal analysis: ")    

    print("Starting Bluetooth Deep Scan...")
    bluetoothDeep.main(adress)

    # print("Starting Bluetooth Signal Analysis...")
    # signalBluetooth.start_signal_analysis()

if __name__ == "__main__":
    main()