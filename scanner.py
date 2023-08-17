import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Mengambil antarmuka WiFi pertama

    iface.scan()  # Memulai pemindaian

    scan_results = iface.scan_results()
    
    print("Daftar jaringan WiFi yang ditemukan:")
    for result in scan_results:
        print(f"SSID: {result.ssid}, Signal Strength: {result.signal}")
    
if __name__ == "__main__":
    scan_wifi()
