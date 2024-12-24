import csv
import pandas as pd


# Guardar el dataframe en un archivo CSV
def dataframe_to_csv(dataframe, archivo):
    
    dataframe.to_csv(archivo, index=False)
    
    print("DataFrame guardado correctamente en: ", archivo)


# Escribir datos en el archivo CSV
def escribir_datos(archivo, datos):
    
    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datos)
        
        
# Cargar datos del archivo CSV
def cargar_datos(archivo):
    datos = []
    with open(archivo, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            datos.append(row)
    return datos


