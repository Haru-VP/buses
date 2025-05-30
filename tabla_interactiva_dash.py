import dash
from dash import dash_table, dcc, html, Input, Output
import pandas as pd

# Leer el archivo limpio generado previamente
df = pd.read_csv('reportes_buses_limpios.csv', encoding='utf-8')

# Agrupar rutas por concepto (guardamos rutas aparte para la interacción)
conceptos = df.groupby('concepto')['ruta'].apply(list).reset_index()
conceptos['Cantidad de rutas'] = conceptos['ruta'].apply(len)

# Creamos un DataFrame solo con las columnas que acepta la tabla
conceptos_tabla = conceptos[['concepto', 'Cantidad de rutas']]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Tabla interactiva de conceptos de rutas", style={'textAlign': 'center'}),
    dash_table.DataTable(
        id='tabla-conceptos',
        columns=[
            {'name': 'Concepto', 'id': 'concepto'},
            {'name': 'Cantidad de rutas', 'id': 'Cantidad de rutas'}
        ],
        data=conceptos_tabla.to_dict('records'),
        row_selectable='single',
        style_cell={'fontSize':16, 'textAlign':'center'},
        style_table={'width':'60%', 'margin':'auto'}
    ),
    html.Div(id='detalle-rutas', style={'marginTop': 30, 'fontSize':18, 'textAlign':'center'})
])

@app.callback(
    Output('detalle-rutas', 'children'),
    Input('tabla-conceptos', 'selected_rows')
)
def mostrar_rutas(selected_rows):
    if selected_rows is None or len(selected_rows) == 0:
        return "Selecciona un concepto para ver las rutas asociadas."
    rutas = conceptos.iloc[selected_rows[0]]['ruta']
    return html.Div([
        html.B("Rutas con este concepto:"),
        html.Br(),
        ', '.join(str(r) for r in rutas)
    ])

if __name__ == '__main__':
    app.run()