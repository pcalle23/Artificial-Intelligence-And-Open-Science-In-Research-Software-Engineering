# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18960395.svg)](https://doi.org/10.5281/zenodo.18960395) 

Software para extraer y analizar automáticamente información de papers en formato PDF utilizando **Grobid**.

Características principales
* **Extracción automatizada**: Obtiene el *abstract*, cuenta el número de figuras y extrae todas las URLs válidas de los PDFs.
* **Visualización de datos**: Genera nubes de palabras y gráficos de barras a partir de los datos extraídos.
* **Reproducibilidad garantizada**: Entorno completamente dockerizado para ejecutarse en cualquier máquina sin conflictos de dependencias.
* **Tests integrados**: Validación automática de los resultados generados mediante `pytest`.

* Requisitos previos
Para ejecutar este proyecto de forma reproducible, se necesita instalar o tener instalado en su defecto:
* [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

*(Nota: Los archivos PDF a analizar deben colocarse dentro de la carpeta `Papers/pdf/` antes de la ejecución).*

## Ejecutar el software: (recomendado trabajarlo desde "venv")

1. Clonar el repositorio
2. Asegúrate de tener tus PDFs en Papers/pdf/ y ejecuta: docker-compose up --build (iniciara e instalara requirements.txt //puede tardar unos segundos//)

## Resultados generados
Una vez finalizada la ejecución, encontrarás los siguientes archivos en la raíz del proyecto:

datos_extraidos.json: Base de datos con toda la información extraída.

NubeDePalabras.png: Visualización de los términos más frecuentes en los abstracts.

figuras_por_articulo.png: Gráfico comparativo del número de figuras por paper.

lista_enlaces.md: Recopilación estructurada de todas las URLs encontradas.


## LICENCIA
Este proyecto está bajo la licencia Apache 2.0.
