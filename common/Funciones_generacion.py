from common.Clases import Vuelo, IDterator
from common.Parametrizacion import *
from datetime import datetime, timedelta


# Funciones para generar los vuelos de la compañía aérea. Las plazas de los vuelos se generan aleatoriamente,
# pero se tiene en cuenta que las plazas más cercanas a la fecha de salida del vuelo tengan menos plazas
# disponibles. Además, se añade la posibilidad de que haya overbooking.

# los vuelos se almacenarán en una lista de diccionarios, cada diccionario representará un vuelo con los 
# siguientes campos: id, estado, hora de salida, hora prevista de llegada, aeropuerto de salida,
#  aeropuerto de llegada, duración, tipo de vuelo, precio business, precio turista modelo, plazas totales,
#  plazas  disponibles, plazas totales en clase turista, plazas disponibles en clase turista


def generar_vuelos(vuelos, fecha_inicio,fecha_sistema, dias):

    
    # Para la generación de ID hemos tenido que crear un iterador definido en Clases.py que nos 
    # permita generar un id para cada vuelo

    contador_id = IDterator()

    # generamos los vuelos para cada dia
    for i in range(dias):
        # generamos un id para cada vuelo
        # generamos la fecha del vuelo
        fecha = fecha_inicio + timedelta(days = i)
         # generamos los vuelos de ese dia
        generar_vuelos_dia(vuelos, fecha, fecha_inicio, fecha_sistema ,contador_id)

    return vuelos


#GENERACION DE VUELOS DIARIOS
# Generamos los vuelos en función del dia de la semana. Los vuelos tienen una planificación estructurada
# de forma que semanalmente tendremos los mismos vuelos asociados a cada dia de la semana

#Para cada dia de la semana tendremos que pasar la infomación del vuelo, que será escrita a mano
# y la de fecha, que estará automatizada, ya que determinados campos como el precio o el numero de asientos
# disponibles son variables dependientes del tiempo

def generar_vuelos_dia(vuelos, fecha, fecha_inicio, fecha_sistema ,contador_id):

    # LUNES
    
#   internacionales:                 zona euro:                 nacional:
# 10:00 (Madrid - Tokio)          8:00 (Malaga - Varsovia)    18:00 (Madrid - Tenerife)
# 15:00 (Madrid - Nueva York)    12:00 (Barcelona - Roma)    06:00 (Barcelona - Sevilla)

    if fecha.weekday() == 0:
        # Internacionales

        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "10:00", "10:00", "Madrid", "Tokio", 10789, "15 horas", tipo_vuelo, modelo, 500, 200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "15:00", "20:00", "Madrid", "Nueva York",5782, "9 horas", tipo_vuelo, modelo,500, 200)

        # Zona euro

        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "8:00", "12:00", "Malaga", "Varsovia",2633, "4 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "12:00", "14:00", "Barcelona", "Roma",859, "2 horas", tipo_vuelo, modelo, 500,200)

        # Nacional

        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "18:00", "21:00", "Madrid", "Tenerife",1790, "3 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "06:00", "08:00", "Barcelona", "Sevilla",831, "2 horas", tipo_vuelo, modelo, 500,200)

    # MARTES
        
#   internacionales:                 zona euro:                 nacional:
# 06:00 (Barcelona - Moscu)        9:00 (Madrid - Paris)       16:00 (Barcelona - Bilbao)
# 22:00 (Málaga - Pekin)
        
    elif fecha.weekday() == 1:
        # Internacionales

        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "06:00", "14:00", "Barcelona", "Moscu",3011, "5 horas", tipo_vuelo, modelo, 500, 200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "22:00", "16:00", "Malaga", "Pekin", 9592, "10 horas", tipo_vuelo, modelo, 500,200)

        # Zona euro

        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "9:00", "11:00", "Madrid", "Paris",1052, "2 horas", tipo_vuelo, modelo, 500,200)

        # Nacional

        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "16:00", "17:00", "Barcelona", "Bilbao",470, "1 horas", tipo_vuelo, modelo, 500,200)

    # MIERCOLES
        
#   internacionales:                 zona euro:                 nacional:
# 11:00 (Madrid - Sidney)          13:00 (Barcelona - Berlin)  17:00 (Sevilla - Bilbao)
#                                   19:00 (Madrid - Berlin)     15:00 (sevilla - Barcelona)
        
    elif fecha.weekday() == 2:

        # Internacionales

        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "11:00", "11:00", "Madrid", "Sidney",  17687, "13 horas", tipo_vuelo, modelo, 500,200)

        # Zona euro

        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "13:00", "17:00", "Barcelona", "Berlin",1499, "4 horas", tipo_vuelo, modelo,500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "19:00", "23:00", "Madrid", "Berlin", 1870, "4 horas", tipo_vuelo, modelo, 500,200)

        # Nacional

        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "17:00", "19:00", "Sevilla", "Bilbao",702, "2 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "15:00", "17:00", "Sevilla", "Barcelona", 831, "2 horas", tipo_vuelo, modelo, 500,200)

    # JUEVES
        
#   internacionales:                 zona euro:                 nacional:
# 10:00 (Nueva York - Madrid)      22:00 (Varsovia - Malaga)   18:00 (Tenerife - Madrid)
#                                   20:00 (Roma - Barcelona)
        
    elif fecha.weekday() == 3:

        # Internacionales
        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "10:00", "23:00", "Nueva York", "Madrid",5782, "7 horas", tipo_vuelo, modelo, 500,200)

        # Zona euro
        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "22:00", "02:00", "Varsovia", "Malaga",2633, "4 horas", tipo_vuelo, modelo,500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "20:00", "22:00", "Roma", "Barcelona", 859, "2 horas", tipo_vuelo, modelo, 500,200)

        # Nacional
        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "18:00", "20:00", "Tenerife", "Madrid", 1790, "2 horas", tipo_vuelo, modelo, 500,200)

    # VIERNES
        
#   internacionales:                 zona euro:                 nacional:
# 15:00 (Moscu - Barcelona)        12:00 (Paris - Madrid)      16:00 (Bilbao - Barcelona)
        
    elif fecha.weekday() == 4:
            
        # Internacionales

        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "15:00", "17:00", "Moscu", "Barcelona",3011, "5 horas", tipo_vuelo, modelo,500,200)

        # Zona euro

        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "12:00", "14:00", "Paris", "Madrid",1052, "2 horas", tipo_vuelo, modelo,500,200)

        # Nacional

        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "16:00", "17:00", "Bilbao", "Barcelona",470, "1 horas", tipo_vuelo, modelo,500,200)

    # SABADO
            
#   internacionales:                 zona euro:                 nacional:
# 15:00 (Tokio - Madrid)           12:00 (Berlin - Madrid)     18:00 (Bilbao - Sevilla)
# 8:00 (Bilbao- Nueva delhi)       16:00 (Berlin - Barcelona)
            
    elif fecha.weekday() == 5:
        
        # Internacionales
    
        modelo= "Airbus A500"
        tipo_vuelo = "internacional"
    
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "15:00", "19:00", "Tokio", "Madrid", 10789,"13 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "8:00", "21:00", "Bilbao", "Nueva delhi",  7136,"7 horas", tipo_vuelo, modelo,500,200)
    
        # Zona euro
    
        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"
    
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "12:00", "16:00", "Berlin", "Madrid",1870, "4 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "16:00", "20:00", "Berlin", "Barcelona",1499, "4 horas", tipo_vuelo, modelo,500,200)
    
        # Nacional
    
        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"
    
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "18:00", "20:00", "Bilbao", "Sevilla",702, "2 horas", tipo_vuelo, modelo,500,200)

    # DOMINGO

#   internacionales:                 zona euro:                 nacional:
# 15:00 (Pekin - Málaga)           12:00 (Paris - Madrid)      16:00 (Barcelona - Bilbao)
# 22:00 (Sidney - Madrid)          16:00 (Nueva delhi - Bilbao)
# 16:00 (Nueva delhi - Bilbao)

    elif fecha.weekday() == 6:

        # Internacionales

        modelo= "Airbus A500"
        tipo_vuelo = "internacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "15:00", "20:00", "Pekin", "Malaga",9592,"12 horas", tipo_vuelo, modelo, 500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "22:00", "02:00", "Sidney", "Madrid",17687, "15 horas", tipo_vuelo, modelo,500,200)
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "16:00", "18:00", "Nueva delhi", "Bilbao",7136, "7 horas", tipo_vuelo, modelo, 500,200)

        # Zona euro

        modelo= "Airbus A330"
        tipo_vuelo = "zona euro"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "12:00", "14:00", "Paris", "Madrid",1052, "2 horas", tipo_vuelo, modelo, 500,200)

        # Nacional

        modelo= "Airbus A320 Neo"
        tipo_vuelo = "nacional"

        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "programado", fecha, "16:00", "18:00", "Barcelona", "Bilbao",470, "2 horas", tipo_vuelo, modelo,500,200)


    else:
        
        modelo= "Escoba magica"
        tipo_vuelo = "interdimensional"
        
        generar_vuelo(fecha_inicio,fecha_sistema, vuelos, contador_id, "Yo si que voy volao ",fecha, "10:00", "14:14", "Monte del destino", "Narnia",123456789, "300000 horas", tipo_vuelo, modelo, 50000,31414024)


    return



#GENERACIÓN DE CADA VUELO ESPECIFICO

#En esta función se transmitiran los parametros necesarios para el calculo de las diferentes variables del
# vuelo. Estos parametros son dependientes de los vuelos diarios programados en la funcion generar_vuelos_dia

# 1º Lo primero de todo será definir los parametros definidos por el modelo del avión.

# 2º Una vez tenemos la información del avión y la fecha del vuelo, podemos calcular el resto de variables
# mediante las funciones especificadas en parametrización

def generar_vuelo(fecha_inicio, fecha_sistema, vuelos, contador_id , estado, fecha, hora_salida, 
                  hora_llegada, aeropuerto_salida, aeropuerto_llegada,distancia, duracion, 
                  tipo_vuelo,  modelo, precio_business, precio_turista):
    

    hora_salida= datetime.strptime(hora_salida, '%H:%M').time()


    if modelo == "Airbus A500":
        plazas_totales = 348
        plazas_disponibles= 348
        plazas_business_totales = 50
        plazas_business_disponibles= 50
        plazas_turista_totales = 298
        plazas_turista_disponibles= 298
        plazas_overbooking_totales = 20
        plazas_overbooking_disponibles= 20

    elif modelo == "Airbus A330":
        plazas_totales = 290
        plazas_disponibles= 290
        plazas_business_totales = 40
        plazas_business_disponibles= 40
        plazas_turista_totales = 250
        plazas_turista_disponibles= 250
        plazas_overbooking_totales = 15
        plazas_overbooking_disponibles= 15

    elif modelo == "Airbus A320 Neo":

        plazas_totales = 180
        plazas_disponibles= 180
        plazas_business_totales = 30
        plazas_business_disponibles= 30
        plazas_turista_totales = 150
        plazas_turista_disponibles= 150
        plazas_overbooking_totales = 10
        plazas_overbooking_disponibles= 10




    #añadimos la parametrización de los asientos según la distancia a la fecha de salida
    
#   generamos las plazas disponibles
    plazas_business_disponibles, plazas_turista_disponibles, plazas_overbooking_disponibles, plazas_disponibles = generar_plazas_disponibles(fecha_sistema, fecha, plazas_totales, plazas_disponibles, plazas_business_totales, 
                               plazas_business_disponibles, plazas_turista_totales, 
                               plazas_turista_disponibles, plazas_overbooking_totales, 
                               plazas_overbooking_disponibles)
    
    
    #generamos los precios segun la cantidad de asientos y fecha

    precio_business, precio_turista = modificar_precio(precio_business, precio_turista, fecha_sistema,
                     fecha, plazas_totales, plazas_disponibles,
                     plazas_business_totales, plazas_business_disponibles, 
                     plazas_turista_totales, plazas_turista_disponibles, 
                     plazas_overbooking_totales, plazas_overbooking_disponibles,distancia)


    
    #Generamos el estado del vuelo

    estado = modificar_estado_vuelo_demanda(plazas_totales, plazas_disponibles , fecha, fecha_sistema, hora_salida, duracion)

    
    # modificamos el valor de ID para el siguiente vuelo
    
    contador_id= next(contador_id)


    # Generamos el objeto Vuelo mediante la clase definida en clases
    vuelo = Vuelo(contador_id, estado, fecha, hora_salida, hora_llegada, aeropuerto_salida, aeropuerto_llegada, duracion, tipo_vuelo,  modelo,
                  plazas_totales, plazas_disponibles, plazas_business_totales, plazas_business_disponibles, plazas_turista_totales, plazas_turista_disponibles, plazas_overbooking_totales, plazas_overbooking_disponibles, precio_business, precio_turista)
    




    # Convertimos los datos del vuelo a diccionario y los añadimos a la lista de vuelos
    vuelo_dicionario= vuelo.__diccionario__()

    vuelos.append(vuelo_dicionario)
