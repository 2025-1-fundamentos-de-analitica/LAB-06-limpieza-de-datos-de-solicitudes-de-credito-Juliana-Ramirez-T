import pandas as pd
import os
"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

def pregunta_01():
    #Leer el archivo csv
    archivo = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

    #Procesar "fecha_de_beneficio"
    archivo["fecha_de_beneficio"] = pd.to_datetime(
        archivo["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(
        pd.to_datetime(archivo["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )

    #Procesar "comuna_ciudadano"
    archivo["comuna_ciudadano"] = archivo["comuna_ciudadano"].astype(int)

    #Procesar "línea_credito"
    archivo["línea_credito"] = archivo["línea_credito"].str.strip().str.lower().str.replace("-", " ").str.replace("_", " ").str.strip()
   
    #Procesar "tipo_de_emprendimiento"
    archivo["tipo_de_emprendimiento"] = archivo["tipo_de_emprendimiento"].str.strip().str.lower()
    
    #Procesar "idea_negocio"
    archivo["idea_negocio"] = archivo["idea_negocio"].str.lower().str.replace("-", " ").str.replace("_", " ").str.strip()
    
    #Procesar "barrio"
    archivo["barrio"] = archivo["barrio"].str.lower().str.replace("-", " ").str.replace("_", " ")
   
    #Procesar "monto_del_credito"
    archivo["monto_del_credito"] = archivo["monto_del_credito"].str.strip().str.replace(",", "").str.replace(".00", "").str.replace("$", "").astype(int)
   
    #Procesar "sexo"
    archivo["sexo"] = archivo["sexo"].str.lower()

    #elimina duplicados y nan
    def limpiar(df):
        return df.drop_duplicates().dropna()
    archivo = limpiar(archivo)

    if not os.path.exists("files/output"):
        os.makedirs("files/output")
    archivo.to_csv("files/output/solicitudes_de_credito.csv", sep=';', index=False)

if __name__ == "__main__":
    pregunta_01()


"""
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """