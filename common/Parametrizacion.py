from datetime import timedelta, time
import random

# Función para generar el calculo de plazas turista y business disponibles en un vuelo dependiendo 
#de la fecha de salida del vuelo y la fecha actual


#ahora calculamos el número de plazas disponibles, tanto para turista como para business
        # debemos tener en cuenta que mientras más cerca de la fecha estemos más asientos
        #deben estar ocupados, para esto podemos crear una función de aleatorización
        # que aumente la probabilidad conforme más cerca estemos a la fecha

def calculo_plazas(fecha_sistema, fecha_vuelo, plazas_totales):

    diferencia = (fecha_vuelo - fecha_sistema).days

    if diferencia > 300:
        plazas_disponibles = plazas_totales - random.randint(0, 5)
    elif diferencia > 230:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.05), int(plazas_totales*0.10))
    elif diferencia > 180:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.10), int(plazas_totales*0.15))
    elif diferencia > 120:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.15), int(plazas_totales*0.35))
    elif diferencia > 60:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.35), int(plazas_totales*0.55))
    elif diferencia > 30:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.55), int(plazas_totales*0.80))
    elif diferencia > 15:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.80), int(plazas_totales*0.925))
    elif diferencia > 4 :
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.925), plazas_totales)
    elif diferencia > 0: 
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.94), plazas_totales)
    else:
        plazas_disponibles = plazas_totales - random.randint(int(plazas_totales*0.98), plazas_totales)

    return plazas_disponibles




#Función para generar el numero de plazas disponibles.
 
    # 1º Se calcula la posibilidad de que exista overbooking. Esto es, que se vendan más asientos que el 
    # número total de plazas (tactica frecuentemente utilizada por las aerolinias y que les permite ganar
    # más dinero).
    
    # 2º Si existe overbooking, todos los asientos turista deben estar ocupados además, se asigna una
    # cantidad de asientos extra vendidos de forma aleatoria
    
    # 3º Si no hay overbooking, se cálcula el número de asientos de la forma usual, con la función definida
    # anteriormente
    
def generar_plazas_disponibles(fecha_sistema, fecha_vuelo, plazas_totales, plazas_disponibles, plazas_business_totales, 
                               plazas_busineess_disponibles, plazas_turista_totales, 
                               plazas_turista_disponibles, plazas_overbooking_totales, 
                               plazas_overbooking_disponibles):
    
    
    dias_hasta_salida = (fecha_vuelo - fecha_sistema).days


    overbooking=False
    # si faltan menos de 3 dias para la salida del vuelo hay un 30% de probabilidad de overbooking
    # también si el vuelo ya ha salido
    if dias_hasta_salida < 3:
        probabilidad_overbooking= random.random()
        overbooking = probabilidad_overbooking < 0.3
    # si faltan menos de una semana para la salida del vuelo hay un 15% de probabilidad de overbooking
    elif dias_hasta_salida < 7:
        probabilidad_overbooking= random.random()
        overbooking = probabilidad_overbooking < 0.15
    # si faltan menos de dos semanas para la salida del vuelo hay un 5% de probabilidad de overbooking
    elif dias_hasta_salida < 14:
        probabilidad_overbooking= random.random()
        overbooking = probabilidad_overbooking < 0.05





    plazas_busineess_disponibles = calculo_plazas(fecha_sistema, fecha_vuelo, plazas_business_totales)

    #Si hay overbooking, todas las plazas turistas están ocupadas. Si no, se deben calcular
    if overbooking:
        
        plazas_turista_disponibles = 0

        # generamos un porcentaje aleatorio de plazas con overbooking ocupadas teniendo en 
        #cuenta que al menos un asiento de overbooking está ocupado. 
        plazas_overbooking = random.randint(1, plazas_overbooking_totales)
        plazas_overbooking_disponibles = plazas_overbooking_totales - plazas_overbooking

    else:
        plazas_turista_disponibles = calculo_plazas(fecha_sistema, fecha_vuelo, plazas_turista_totales)


    plazas_disponibles  = plazas_busineess_disponibles + plazas_turista_disponibles

    return plazas_busineess_disponibles, plazas_turista_disponibles, plazas_overbooking_disponibles, plazas_disponibles



# Función para modificar el precio de un vuelo dependiendo de la distancia al destino, la demanda y 
#la antelación de la reserva del vuelo con respecto a la fecha de salida.  es importante el orden en 
#el que pongamos las modificaciones de precio porque si la fecha de compra es superior a 200 dias y 
#primero evalua si es superior a 90 dias, no se cumpliria la condicion de 200 dias y no se aplicaria
# el descuento del 40% que deberia aplicarse
def modificar_precio(precio_business, precio_turista, fecha_sistema, fecha_vuelo,
                     plazas_totales, plazas_disponibles, 
                     plazas_business_totales, plazas_business_disponibles, 
                     plazas_turista_totales, plazas_turista_disponibles, 
                     plazas_overbooking_totales, plazas_overbooking_disponibles,distancia):
    
    
    #modificar precio inicialemente segun la fecha

    precio_business, precio_turista = modificar_precio_fecha(precio_business, precio_turista,fecha_sistema, fecha_vuelo)

    # Segundo ajuste del precio teniendo en cuenta el número de plazas ocupadas y la fecha
    # La fecha y el numero de asientos están interrelacionados porque a veces las compañia tienen más
    # interres en bajar los precios si el avion está casi lleno y teminar de llenarlo cerca de la fecha
    # del vuelo

    # Los precios se deben modificar teniendo en cuenta el total de plazas ocupadas, para evitar
    # que el precio business pueda ser más barato que el precio turista
    precio_business, precio_turista = modificar_precio_demanda(precio_business, precio_turista,plazas_totales, plazas_disponibles, fecha_vuelo, fecha_sistema)



    #modificar precio segun la distancia del vuelo

    precio_business, precio_turista= modificar_precio_distancia(precio_business, precio_turista, distancia)
    
    precio_business = round(precio_business, 2)
    precio_turista = round(precio_turista,2)


    return precio_business, precio_turista


#Modificacion del precio según la fecha

# Fechas alejadas -> más barato
# Fechas cercanas -> más caro

def modificar_precio_fecha(precio_business, precio_turista, fecha_sistema, fecha_vuelo):


    if (fecha_vuelo - fecha_sistema).days > 300:
        precio_business = precio_business * 0.6
        precio_turista = precio_turista * 0.6
    elif (fecha_vuelo - fecha_sistema).days > 270:
        precio_business = precio_business * 0.7
        precio_turista = precio_turista * 0.7
    elif (fecha_vuelo - fecha_sistema).days > 180:
        precio_business = precio_business * 0.8
        precio_turista = precio_turista * 0.8
    elif (fecha_vuelo - fecha_sistema).days > 90:
        precio_business = precio_business * 0.9
        precio_turista = precio_turista * 0.9


    if (fecha_vuelo - fecha_sistema).days < 7:
        precio_business = precio_business * 1.4
        precio_turista = precio_turista * 1.4

    elif (fecha_vuelo - fecha_sistema).days < 14:
        precio_business = precio_business * 1.3
        precio_turista = precio_turista * 1.3

    elif (fecha_vuelo - fecha_sistema).days < 30:
        precio_business = precio_business * 1.2
        precio_turista = precio_turista * 1.2

    elif (fecha_vuelo - fecha_sistema).days < 45:
        precio_business = precio_business * 1.1
        precio_turista = precio_turista * 1.1


    return precio_business, precio_turista





#Modificación del precio segun la distancia de vuelo

def modificar_precio_distancia(precio_business,precio_turista, distancia):

    if distancia > 5000:
        precio_business = precio_business + 0.03 * distancia
        precio_turista = precio_turista  +0.03 * distancia

    elif distancia > 3000:
        precio_business = precio_business   + 0.025 * distancia
        precio_turista = precio_turista  + 0.025 * distancia

    elif distancia > 1000:
        precio_business = precio_business + 0.020 * distancia
        precio_turista = precio_turista  + 0.020 * distancia
    elif distancia > 500:
        precio_business = precio_business  + 0.015 * distancia
        precio_turista = precio_turista + 0.015 * distancia

    return precio_business, precio_turista



#Modificación de vuelo segun la demanda y la fecha:
    
#Si todos los asientos estan ocupados -> Overbooking, el precio se cuadriplica
#Si hay menor demanda -> precio más bajo

#Si se acerca la fecha del vuelo y el avión todavía tiene baja ocupación -> se reduce el precio

def modificar_precio_demanda(precio_business, precio_turista, plazas_totales, plazas_disponibles , fecha_vuelo, fecha_sistema):

    
    demanda = (plazas_totales - plazas_disponibles) / plazas_totales * 100

        
#AUMENTOS DE PRECIO 

    if demanda > 100:
        precio_business = precio_business * 4
        precio_turista = precio_turista * 4
    elif demanda > 85:
        precio_business = precio_business * 1.6
        precio_turista = precio_turista * 1.6
    elif demanda > 50:
        precio_business = precio_business * 1.3
        precio_turista = precio_turista * 1.3
    elif demanda > 35:
        precio_business = precio_business * 1.2
        precio_turista = precio_turista * 1.2
    elif demanda > 15:
        precio_business = precio_business * 1.15
        precio_turista = precio_turista * 1.15


# REDUCCIONES DE PRECIO

    if demanda < 5:
        precio_business = precio_business * 0.6
        precio_turista = precio_turista * 0.6
    elif demanda < 50 and (fecha_vuelo - fecha_sistema).days > 45 and (fecha_vuelo - fecha_sistema).days < 90:
        precio_business = precio_business * 0.55
        precio_turista = precio_turista * 0.55
    elif demanda < 70 and (fecha_vuelo - fecha_sistema).days > 30 and (fecha_vuelo - fecha_sistema).days < 45:
        precio_business = precio_business * 0.7
        precio_turista = precio_turista * 0.7
    elif demanda < 80 and (fecha_vuelo - fecha_sistema).days > 14 and (fecha_vuelo - fecha_sistema).days < 30:
        precio_business = precio_business * 0.55
        precio_turista = precio_turista * 0.55
    
    
    return precio_business, precio_turista



#Modificación del estado del vuelo según la demanda.

# Poca demanda -> es más probable que se cancele el vuelo

# Avion completo -> vuelo completo

# Mismo dia del vuelo -> pendiente de salida

# Avion en el aire -> En curso

# El avion ha aterrizado -> Realizado

# Otros casos -> programado

def modificar_estado_vuelo_demanda(plazas_totales, plazas_disponibles , fecha_vuelo, fecha_sistema, hora_salida, duracion ):

    demanda = (plazas_totales - plazas_disponibles) / plazas_totales * 100

# Extraer el número de horas de la cadena de texto
    duracion = int(duracion.split()[0])  # Obtener el primer elemento después de dividir por espacio

    # Crear un objeto de hora
    duracion = time(hour=duracion).hour


    if (fecha_sistema).day == (fecha_vuelo).day and fecha_sistema.hour >= hora_salida.hour and fecha_sistema.hour < (hora_salida.hour + duracion): 

        estado = "En curso"
        
    elif (fecha_sistema).day == (fecha_vuelo).day and fecha_sistema.hour < hora_salida.hour:
            
        estado = "Pendiente de salida"

    elif (fecha_sistema).day == (fecha_vuelo).day and fecha_sistema >= (fecha_vuelo + timedelta(hours=duracion)):
    
        estado = "Realizado"

    elif fecha_sistema >= fecha_vuelo:

        estado = "Realizado"

    elif (fecha_sistema).day == (fecha_vuelo).day:
        estado = "Pendiente de salida"
        
        
        #cancelaciones

    elif demanda < 36 and (fecha_vuelo - fecha_sistema).days > 60 and (fecha_vuelo - fecha_sistema).days < 90:
        estado = "cancelado"
    elif demanda < 57 and (fecha_vuelo - fecha_sistema).days > 30 and (fecha_vuelo - fecha_sistema).days < 60:
        estado = "cancelado"
    elif demanda < 82 and (fecha_vuelo - fecha_sistema).days > 15 and (fecha_vuelo - fecha_sistema).days < 30:
        estado = "cancelado"
    elif demanda < 95 and (fecha_vuelo - fecha_sistema).days > 0 and (fecha_vuelo - fecha_sistema).days < 7:
        estado = "cancelado"
        
        
    #Vuelo completo

    elif plazas_disponibles == 0:
        estado = "Completo"

    #Vuelo progamado

    else:
        estado = "Programado"

    return estado



