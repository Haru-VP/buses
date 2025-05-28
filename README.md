# Proyecto de Reportes y Visualización de Rutas de Buses

Este proyecto procesa y visualiza reportes de rutas de buses, permitiendo limpieza de datos y visualización interactiva.

## Estructura de archivos

- `reportes_buses.txt` — Archivo original de reportes.
- `limpieza_reportes.py` — Limpia y normaliza los reportes, genera un CSV limpio.
- `reportes_buses_limpio.csv` — Archivo generado con los datos limpios.
- `visualizacion_reportes.py` — Visualización estática (matplotlib) de los conceptos.
- `tabla_interactiva_dash.py` — Visualización interactiva de conceptos y rutas (Dash).

## Instalación de dependencias

Instala las dependencias necesarias con:

- pip install pandas matplotlib dash


## Uso

1. Ejecuta la limpieza de datos:
    python limpieza_reportes.py
2. Visualización estática:
    python visualizacion_reportes.py
3. Visualización interactiva (abre en navegador):
    python tabla_interactiva_dash.py

## Notas

- El archivo `reportes_buses_limpio.csv` se genera automáticamente tras la limpieza.
- Para la visualización interactiva, abre [http://127.0.0.1:8050/](http://127.0.0.1:8050/) en tu navegador.

---