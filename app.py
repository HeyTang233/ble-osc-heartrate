import asyncio
from bleak import BleakScanner
from pythonosc.udp_client import SimpleUDPClient

VRCHAT_IP = "127.0.0.1"
VRCHAT_PORT = 9000

TARGET_COMPANY_ID = 0x0157

client = SimpleUDPClient(VRCHAT_IP, VRCHAT_PORT)


async def handle_device(device, advertisement_data):
    manufacturer_data = advertisement_data.manufacturer_data
    for company_id, data in manufacturer_data.items():
        if company_id != TARGET_COMPANY_ID:
            continue

        name = device.name if device.name else "(unknown)"
        rssi = advertisement_data.rssi
        heart_rate = data[3] if len(data) > 3 else None

        if heart_rate is not None:
            print(f"{name} ({rssi}dBm) Heart Rate: {heart_rate}")

            floatHR = (heart_rate * 0.0078125) - 1.0

            data = [
                ("HR", heart_rate),
                ("onesHR", heart_rate % 10),
                ("tensHR", (heart_rate // 10) % 10),
                ("hundredsHR", (heart_rate // 100) % 10),
                ("floatHR", floatHR)
            ]

            try:
                for path, value in data:
                    client.send_message(f"/avatar/parameters/{path}", value)
            except Exception as e:
                print(f"Error sending OSC message: {e}")

        await asyncio.sleep(1)


async def main():
    print("Starting Bluetooth scan")
    scanner = BleakScanner(detection_callback=handle_device)

    await scanner.start()
    print("Scan started")

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Scan stopped manually")
    finally:
        await scanner.stop()


if __name__ == "__main__":
    asyncio.run(main())
