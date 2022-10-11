from csv import *
from datetime import*
from collections import namedtuple
from itertools import count
from parsers import *

tuplatotal=namedtuple('tuplatotal','id,tsunami,latitude,longitude,focaldepth,magnitude,deaths,fecha,country,country_zone')


    
    

def abrirdatos(fichero):    
    '''Con esta función cuya entrada es la URL relativa del dataset realizamos varias operaciones:
    
    1.Abrir y leer el archivo csv,teniendo un registro por linea.
    
    2.Asignar valores a cada uno de los elementos de cada registro, en este caso, debido a la ausencia de elementos
    en algunas de las columnas, se han impuesto diversas condiciones para la asignación de estos mismos a través de las funciones situadas
    en el módulo parsers, teniendo así 2 valores de tipo cadena, 4 de tipo entero, 4 de tipo float, 1 de tipo fecha y 1 de tipo booleano.
    
    3.Crear una tupla por cada registro para luego agruparlas todas en una sola lista, devolviendola en la salida de la función.
    
    @param fichero: Ruta del fichero csv que se va a leer
    @type  fichero: str
    @return: Una lista de tuplas, en la que cada una de ellas es una línea del archivo csv
    @rtype: [listatotal(int,boolean,str,str,float,float,int,float,int,fecha)]
    
    '''
    with open(fichero,encoding='utf-8') as f: 
        lector=reader(f,delimiter=';')
        next(lector)
        listatotal=[]
        for id,tsunami,year,month,day,latitude,longitude,focaldepth,magnitude,deaths,country,country_zone in lector:
            
            #ID
            id=int(id)
        
            #DATE
            fecha=parsea_fecha(year,month,day)
            
            
            #TSUNAMI
            tsunami=parsea_booleano(tsunami)
                
            #COUNTRY   
            country=str(country)
            
            #COUNTRY ZONE
            country_zone=str(country_zone)
            
            #LATITUDE
            latitude=parsea_float(latitude)
                
            #LONGITUDE    
            longitude=parsea_float(longitude)
            
            
            #FOCALDEPTH
            focaldepth=parsea_int(focaldepth)
                
            #MAGNITUDE
            magnitude=parsea_float(magnitude)
            #DEATHS
            deaths=parsea_int(deaths)
            
            #CREAMOS LA TUPLA Y LA AÑADIMOS A LA LISTA
            tuplatotal=(id,tsunami,latitude,longitude,focaldepth,magnitude,deaths,fecha,country,country_zone)
            listatotal.append(tuplatotal)
    
        return listatotal
    
 






