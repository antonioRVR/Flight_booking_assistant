# los aviones operaros son 3 modelos diferentes de Airbus con las siguientes características:

# Airbus A500: destinado a vuelos internacionales 348 plazas totales, 50 plazas en clase business,
                #298 plazas en clase turista (10% plazas overbooking), alcance: 	12.300 km 

# Airbus A330: destinado a vuelos de zona euro  290 plazas totales, 40 plazas en clase business, 
                #250 plazas en clase turista (10% plazas overbooking), alcance: 8.800 kçm

# Airbus A320 Neo : destinado a zona euro y vuelos nacionales 180 plazas totales, 30 plazas clase business,
                # 150 plazas en clase turista (10% plazas overbooking), alcance: 3.500 km

class avion:
    def __init__(self, modelo, plazas_totales, plazas_business_totales, plazas_turista_totales,
                  plazas_overbooking_totales, alcance):
        self.modelo = modelo
        self.plazas_totales = plazas_totales
        self.plazas_business_totales = plazas_business_totales
        self.plazas_turista_totales = plazas_turista_totales
        self.plazas_overbooking_totales = plazas_overbooking_totales
        self.alcance = alcance

# Creamos una lista donde almacenamos los aviones operativos
        
flota = [avion("Airbus A500", 348, 50, 298, 20, 12300), avion("Airbus A330", 290, 40, 250, 15, 8800), avion("Airbus A320 Neo", 180, 30, 150, 10, 3.500)]




#VUELO 
#esta es la clase más importante, y contará con métodos que nos permitiran extraer la información y 
# convertirla en diccionario


# id, estado, hora de salida, hora prevista de llegada, aeropuerto de salida, aeropuerto de llegada, duración, tipo de vuelo, precio business, precio turista
# el vuelo tendrá un precio por defecto de 500 euros en clase business y 200 euros en clase turista


class Vuelo:
    def __init__(self, id_vuelo, estado, fecha, hora_salida, hora_llegada, aeropuerto_salida, 
                 aeropuerto_llegada, duracion, tipo_vuelo,  modelo, plazas_totales, 
                 plazas_disponibles, plazas_business_totales, plazas_busineess_disponibles,
                   plazas_turista_totales, plazas_turista_disponibles, 
                   plazas_overbooking_totales, plazas_overbooking_disponibles,
                   precio_business = 500, precio_turista = 200):
        self.id_vuelo= id_vuelo
        self.estado = estado
        self.fecha = fecha
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.aeropuerto_salida = aeropuerto_salida
        self.aeropuerto_llegada = aeropuerto_llegada
        self.duracion = duracion
        self.tipo_vuelo = tipo_vuelo
        self.modelo = modelo
        self.plazas_disponibles = plazas_disponibles
        self.plazas_busineess_disponibles = plazas_busineess_disponibles
        self.plazas_turista_disponibles = plazas_turista_disponibles
        self.precio_business = precio_business
        self.precio_turista = precio_turista
        self.plazas_totales = plazas_totales
        self.plazas_business_totales = plazas_business_totales
        self.plazas_turista_totales = plazas_turista_totales
        self.plazas_overbooking_totales = plazas_overbooking_totales
        self.plazas_overbooking_disponibles = plazas_overbooking_disponibles



        if modelo == "Airbus A500":
            self.plazas_totales = flota[0].plazas_totales
            self.plazas_business_totales = flota[0].plazas_business_totales
            self.plazas_turista_totales = flota[0].plazas_turista_totales
            self.plazas_overbooking_totales = flota[0].plazas_overbooking_totales

        elif modelo == "Airbus A330":

            self.plazas_totales = flota[1].plazas_totales
            self.plazas_business_totales = flota[1].plazas_business_totales
            self.plazas_turista_totales = flota[1].plazas_turista_totales
            self.plazas_overbooking_totales = flota[1].plazas_overbooking_totales 

        elif modelo == "Airbus A320 Neo":

            self.plazas_totales = flota[2].plazas_totales
            self.plazas_business_totales = flota[2].plazas_business_totales
            self.plazas_turista_totales = flota[2].plazas_turista_totales
            self.plazas_overbooking_totales = flota[2].plazas_overbooking_totales 


    #obteción del diccionario del vuelo con los datos solicitados
         
    def __diccionario__(self):
        return {"id": self.id_vuelo, "estado": self.estado,"fecha": self.fecha  , "hora_salida": self.hora_salida, "hora_llegada": self.hora_llegada, "aeropuerto_salida": self.aeropuerto_salida, "aeropuerto_llegada": self.aeropuerto_llegada, "duracion": self.duracion, "tipo_vuelo": self.tipo_vuelo, "modelo": self.modelo, "plazas_totales": self.plazas_totales, "plazas_disponibles": self.plazas_disponibles, "plazas_busisness_totales": self.plazas_business_totales,"plazas_business_disponibles": self.plazas_busineess_disponibles , "plazas_turista_totales": self.plazas_turista_totales, "plazas_turista_disponibles": self.plazas_turista_disponibles, "precio_business": self.precio_business, "precio_turista": self.precio_turista}
        #return {"id": self.id_vuelo, "estado": self.estado,"fecha":datetime.strptime(self.fecha, '%Y-%m-%d')  , "hora_salida": self.hora_salida, "hora_llegada": self.hora_llegada, "aeropuerto_salida": self.aeropuerto_salida, "aeropuerto_llegada": self.aeropuerto_llegada, "duracion": self.duracion, "tipo_vuelo": self.tipo_vuelo, "modelo": self.modelo, "plazas_totales": self.plazas_totales, "plazas_disponibles": self.plazas_disponibles, "plazas_busisness_totales": self.plazas_business_totales,"plazas_business_disponibles": self.plazas_busineess_disponibles , "plazas_turista_totales": self.plazas_turista_totales, "plazas_turista_disponibles": self.plazas_turista_disponibles, "precio_business": self.precio_business, "precio_turista": self.precio_turista}

    #obtención de la información del avion en un diccionario

    def __info_avion__(self):
        return {"modelo": self.modelo, "plazas_totales": self.plazas_totales, "plazas_disponibles": self.plazas_disponibles, "plazas_business_totales": self.plazas_business_totales, "plazas_busineess_disponibles": self.plazas_busineess_disponibles, "plazas_turista_totales": self.plazas_turista_totales, "plazas_turista_disponibles": self.plazas_turista_disponibles, "precio_business": self.precio_business, "precio_turista": self.precio_turista}



class IDterator:
    def __init__(self):
        self.current_id = 1362

    def __iter__(self):
        return self

    def __next__(self):
        current_id = self.current_id
        self.current_id += 1
        return current_id







