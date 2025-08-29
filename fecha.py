#!/usr/bin/env python3
from datetime import datetime

def main():
    # Obtener la fecha y hora actual
    ahora = datetime.now()
    # Formatear en el formato Y-m-d H:i:s
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fecha y Hora: {fecha_hora}")

if __name__ == "__main__":
    main()
