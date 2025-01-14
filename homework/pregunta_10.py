"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    import pandas as pd

    path_tbl0 = 'files/input/tbl0.tsv'
    path_tbl2 = 'files/input/tbl2.tsv'

    df_tbl0 = pd.read_csv(path_tbl0, sep='\t')
    df_tbl2 = pd.read_csv(path_tbl2, sep='\t')
    merged_df = pd.merge(df_tbl0, df_tbl2, on='c0')

    result = merged_df.groupby('c1')['c5b'].sum()

    return result
