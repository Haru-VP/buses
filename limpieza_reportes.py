import pandas as pd
import re

with open('reportes_buses.txt', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

data = []
for line in lines:
    ruta_match = re.search(r'Ruta (\d+)', line)
    if ruta_match:
        ruta = ruta_match.group(1)
    else:
        ruta = 'Todas'
    texto = line.lower()
    # Determinar concepto y estado
    if 'servicio normal' in texto:
        concepto = 'Servicio normal'
        estado = 'Servicio normal'
    elif 'operando normalmente' in texto or 'operativa sin contratiempos' in texto or 'operativa.' in texto:
        concepto = 'Operando'
        estado = 'Operativa'
    elif 'parcialmente operativa' in texto or 'abierta con ajustes' in texto or 'con retrasos' in texto:
        concepto = 'Parcial'
        estado = 'Parcial'
    elif 'suspendida' in texto or 'cerrada' in texto or 'en revisión' in texto:
        concepto = 'En arreglo'
        estado = 'Inactiva'
    else:
        concepto = 'Otro'
        estado = 'Otro'
    data.append({'ruta': ruta, 'concepto': concepto, 'estado': estado})

df = pd.DataFrame(data)

# Eliminar duplicados: solo el último reporte de cada ruta
df_limpio = df.drop_duplicates('ruta', keep='last')

# Guardar a CSV limpio
df_limpio.to_csv('reportes_buses_limpio.csv', index=False, encoding='utf-8')
print("Archivo limpio guardado como reportes_buses_limpio.csv")