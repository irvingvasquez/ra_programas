# Introducción a los Jupyter Notebooks

Un **Jupyter Notebook** es un entorno informático interactivo basado en la web que permite combinar en un solo documento:

* **Código ejecutable**: Generalmente escrito en Python, organizado en celdas independientes.
* **Texto enriquecido**: Uso de Markdown para explicaciones y ecuaciones en LaTeX.
* **Visualizaciones**: Gráficas de resultados, imágenes y videos integrados.

[cite_start]Esta herramienta es fundamental en robótica y aprendizaje profundo porque permite la ejecución **modular**, facilitando la depuración de algoritmos paso a paso[cite: 43, 87].

---

## Opciones para ejecutar Notebooks

Existen dos rutas principales para trabajar con estos archivos (`.ipynb`):

### i) Ejecución en la Nube (Google Colab)
Es la opción recomendada si no deseas realizar instalaciones complejas o si tu equipo personal tiene recursos limitados.

* **¿Qué es?**: Un servicio gratuito de Google que ejecuta los notebooks en sus propios servidores.
* **Ventajas**:
    * **Acceso a GPU**: Permite acelerar el entrenamiento de modelos pesados de forma gratuita.
    * **Cero Configuración**: Librerías como TensorFlow, PyTorch y OpenCV ya vienen instaladas.
    * **Portabilidad**: Tus avances se guardan en Google Drive.
* **Acceso**: [colab.research.google.com](https://colab.research.google.com)

### ii) Ejecución Local (PC Personal)
Ideal para desarrollar proyectos que requieren interactuar con hardware local o simuladores de robótica sin depender de internet.

* **Herramientas**:
    * **VS Code**: Recomendado por ser ligero; solo requiere la extensión "Jupyter".
    * **Anaconda**: Distribución que incluye JupyterLab y gestión de entornos.
* **Ventajas**:
    * **Privacidad**: Los datos no salen de tu computadora.
    * **Hardware Local**: Uso directo de periféricos como cámaras web o puertos seriales.
    * **Sin límites**: No hay restricciones de tiempo de sesión o desconexiones del servidor.

---

> **Nota para el curso:** Utilizaremos este repositorio como base para las prácticas: [github.com/irvingvasquez/ra_programas](https://github.com/irvingvasquez/ra_programas). Pueden clonarlo y ejecutarlo en la plataforma que prefieran.