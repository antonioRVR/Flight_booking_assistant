import pandas as pd
import os
from datetime import datetime
from common.Funciones_generacion import generar_vuelos

#creamos una lista de diccionarios con los vuelos que empezará vacia
#cada vuelo será un elemento de la lista y contendrá un diccionario con los datos del vuelo
vuelos = []

#llamamos a la función para generar los vuelos de los proximos x dias

fecha_inicio= datetime(2024, 3, 15)
fecha_sistema = datetime.now()

generar_vuelos(vuelos, fecha_inicio,fecha_sistema, 150)


df = pd.DataFrame(vuelos)
nombre_archivo = 'vuelos.csv'
df.to_csv(nombre_archivo, index=False)

print("\nEl archivo de vuelos ha sido generado \n")
directorio=os.getcwd()
print(nombre_archivo, " ha sido generado en el directorio del programa python: ", directorio)