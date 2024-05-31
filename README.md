# Cyber Game

Cyber Game es un juego interactivo de toma de decisiones centrado en la ciberseguridad. El objetivo es simular escenarios y decisiones críticas para mejorar la comprensión y la respuesta ante amenazas cibernéticas.

## Características

- **Pantalla Inicial**: Comienza el juego desde una interfaz moderna.
- **Configuración de Empresa**: Define las características de tu empresa (nombre, industria, tamaño, presupuesto de seguridad, etc.).
- **Configuración de Jugador**: Configura tu personaje con roles y habilidades específicas.
- **Resumen de Configuración**: Revisa y modifica la configuración antes de iniciar el juego.
- **Toma de Decisiones**: Enfrenta diferentes escenarios y toma decisiones que afectarán el resultado del juego.
- **Conclusión**: Visualiza el resumen de tus decisiones y su impacto.

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/fedequark/cyber-game.git
   cd cyber-game
   ```

2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```sh
   python app.py
   ```

4. Accede al juego en tu navegador:
   ```sh
   http://127.0.0.1:5000/
   ```

## Estructura del Proyecto

- `app.py`: Archivo principal que maneja las rutas y la lógica del juego.
- `tree_data_loader.py`: Script para cargar datos del árbol de decisiones.
- `static/`: Archivos estáticos (CSS, JS, imágenes).
- `templates/`: Plantillas HTML.
  - `index.html`: Pantalla inicial.
  - `setup.html`: Configuración de la empresa.
  - `player_setup.html`: Configuración del jugador.
  - `summary.html`: Resumen de configuración.
  - `decision.html`: Pantalla de toma de decisiones.
  - `conclusion.html`: Conclusión del juego.
- `company_config.json`: Configuración de la empresa.
- `decision_tree.json`: Árbol de decisiones del juego.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejorar el juego.
