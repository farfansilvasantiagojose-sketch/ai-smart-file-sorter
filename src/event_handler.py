import os
from watchdog.events import FileSystemEventHandler


class NewFileHandler(FileSystemEventHandler):
    """
    Clase encargada exclusivamente de manejar los eventos del sistema de archivos.
    Cumple con SRP: Solo le importa 'qué pasa' cuando hay cambios, no 'cómo' se procesan después.
    """

    def on_created(self, event):
        """
        Se ejecuta automáticamente cuando se crea un archivo o carpeta.
        """
        # Ignoramos si es una carpeta, solo nos interesan archivos
        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)
        print(f"👀 ¡Nuevo archivo detectado!: {filename}")

        # Aquí, en la Fase 3, llamaremos a la Inteligencia Artificial.
        # Por ahora, solo confirmamos la detección.