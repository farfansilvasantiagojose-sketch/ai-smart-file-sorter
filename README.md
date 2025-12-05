# AI Smart File Sorter 🤖📂

Un agente inteligente de organización de archivos que monitorea tus carpetas y categoriza documentos automáticamente utilizando Modelos de Lenguaje (LLMs).

Este proyecto está construido con **Python** y **Docker**, aplicando estrictamente principios de arquitectura de software **SOLID**.

## 🚀 Características
- **Monitoreo en Tiempo Real:** Detecta archivos nuevos instantáneamente al caer en la carpeta de descargas.
- **Inteligencia Artificial:** Utiliza LLMs para "entender" el nombre o contenido del archivo y decidir su mejor ubicación.
- **Entorno Aislado:** Ejecución contenerizada con Docker para portabilidad y seguridad.
- **Arquitectura Limpia:** Código modular, escalable y fácil de mantener.

## 🛠️ Tech Stack
- **Lenguaje:** Python 3.11
- **Infraestructura:** Docker & Docker Compose
- **Librerías Clave:** Watchdog (Eventos del sistema), OpenAI/LangChain (Próximamente).

## 🏃‍♂️ Cómo ejecutar (Modo Desarrollo)

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/farfansilvasantiagojose-sketch/ai-smart-file-sorter.git
   cd ai-smart-file-sorter