"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    import pandas as pd

    path_tbl0 = 'files/input/tbl0.tsv'
    path_tbl2 = 'files/input/tbl2.tsv'

    df_tbl0 = pd.read_csv(path_tbl0, sep='\t')
    df_tbl2 = pd.read_csv(path_tbl2, sep='\t')
    merged_df = pd.merge(df_tbl0, df_tbl2, on='c0')

    result = merged_df.groupby('c1')['c5b'].sum()

    return result
