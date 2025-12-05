import os
import google.generativeai as genai
from dotenv import load_dotenv


class AISorter:
    """
    Clase encargada de comunicarse con el LLM para decidir
    la categoría de un archivo.
    """

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("❌ ERROR: No se encontró la GOOGLE_API_KEY en las variables de entorno.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-pro-latest')

    def decide_category(self, filename):
        """
        Envía el nombre del archivo a la IA y retorna una categoría.
        """
        prompt = f"""
        Actúa como un organizador de archivos inteligente.
        Tengo un archivo llamado: "{filename}".

        Clasifícalo en UNA de las siguientes carpetas: 
        [Imagenes, Documentos, Instaladores, Audio, Video, Codigo, Otros]

        Responde SOLO con el nombre de la carpeta. No des explicaciones.
        """

        try:
            response = self.model.generate_content(prompt)
            # Limpiamos la respuesta (quitamos espacios extra)
            category = response.text.strip()
            return category
        except Exception as e:
            print(f"⚠️ Error consultando a la IA: {e}")
            return "Otros"  # Fallback seguro