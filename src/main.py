import time
import os
from watchdog.observers import Observer
from event_handler import NewFileHandler

# Ruta dentro del contenedor
MONITORED_PATH = "/app/monitored_folder"


def start_monitoring():
    # 1. Verificar ruta
    if not os.path.exists(MONITORED_PATH):
        print(f"❌ Error: La ruta {MONITORED_PATH} no existe.")
        return

    print(f"--- INICIANDO MONITOR DE ARCHIVOS EN: {MONITORED_PATH} ---")

    # 2. Configurar el manejador de eventos (Nuestra clase)
    event_handler = NewFileHandler()

    # 3. Configurar el Observador (El "vigilante" de la librería watchdog)
    observer = Observer()
    observer.schedule(event_handler, MONITORED_PATH, recursive=False)

    # 4. Arrancar
    observer.start()
    print("✅ Sistema corriendo. Esperando archivos...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Deteniendo el sistema...")

    observer.join()


if __name__ == "__main__":
    start_monitoring()