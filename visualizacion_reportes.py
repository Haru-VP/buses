import pandas as pd
import matplotlib.pyplot as plt

# Leer datos limpios
df = pd.read_csv('reportes_buses_limpios.csv', encoding='utf-8')

# Conteo de conceptos
conteo_conceptos = df['concepto'].value_counts().sort_index()
porcentajes = conteo_conceptos / conteo_conceptos.sum() * 100

# Gráfica circular y tabla
fig, ax = plt.subplots(figsize=(12, 7))
wedges, texts, autotexts = ax.pie(
    conteo_conceptos, 
    labels=conteo_conceptos.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=plt.cm.Paired.colors,
    textprops={'fontsize': 14}
)
ax.set_title('Porcentaje de rutas por concepto (únicas, todas las rutas)', fontsize=18)
ax.axis('equal')

# Tabla grande al lado derecho (por concepto)
tabla_data = {
    'Concepto': conteo_conceptos.index,
    'Cantidad de rutas': conteo_conceptos.values,
    'Porcentaje': [f"{p:.1f}%" for p in porcentajes.values]
}
tabla_df = pd.DataFrame(tabla_data)
tabla = plt.table(
    cellText=tabla_df.values,
    colLabels=tabla_df.columns,
    cellLoc='center',
    loc='right',
    bbox=[1.08, 0.1, 0.4, 0.8],
    colColours=["#cccccc"]*3
)
tabla.auto_set_font_size(False)
tabla.set_fontsize(14)

plt.tight_layout()
plt.show()