import os
from watchdog.events import FileSystemEventHandler
from ai_service import AISorter  # Importamos nuestra nueva clase


class NewFileHandler(FileSystemEventHandler):
    def __init__(self):
        # Inicializamos la IA una sola vez cuando arranca el programa
        self.ai_sorter = AISorter()

    def on_created(self, event):
        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)
        print(f"\n👀 Nuevo archivo detectado: {filename}")
        print("🤖 Consultando a la IA...")

        # Le preguntamos a la IA
        categoria = self.ai_sorter.decide_category(filename)

        print(f"✅ La IA sugiere moverlo a: 📂 [{categoria}]")
        print("------------------------------------------------")