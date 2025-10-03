import socket

# Puertos comunes a escanear
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

def scan_ports(target):
    abiertos = []
    for port in COMMON_PORTS:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            abiertos.append(port)
            s.close()
        except:
            pass
    return abiertos

if __name__ == "__main__":
    objetivo = input("Introduce IP o URL: ")
    abiertos = scan_ports(objetivo)
    print(f"Puertos abiertos en {objetivo}: {abiertos if abiertos else 'Ninguno encontrado'}")
