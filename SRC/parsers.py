from datetime import datetime

def parsea_fecha(year,month,day):
    '''
    Con esta función creamos el valor de tipo fecha para luego tratarlo en el modulo principal
    @param year,month,day: Datos situados en el archivo csv con el fin de crear un dato de tipo fecha
    @param type: str,str,str
    @return: El valor de tipo fecha ya creado
    @rtype: fecha
    '''
    if year=='':
        year='1850'
        
    if month=='':
        month='1'
        
    if day=='':
        day='1'
   
    str_fecha=str(year)+'/'+str(month)+'/'+str(day)
    
    return datetime.strptime(str_fecha, '%Y/%m/%d').date()


def parsea_booleano(str_bool):
    '''
    Con esta función creamos el valor de tipo boolean a través de condiciones para luego tratarlo en el modulo principal
    @param str_bool: Dato situado en el archivo csv con el fin de transformarlo en tipo bool
    @param type: bool
    @return: El valor de tipo bool ya creado
    @rtupe: boolean
    '''
    if str_bool == 'Yes':
        res=True
    else:
        res=False
        
    return res

def parsea_float(num_float):
    '''
    Con esta función creamos el valor de tipo float a través de condiciones para luego tratarlo en el modulo principal
    @param str_float: Dato situado en el archivo csv con el fin de transformarlo en tipo float
    @param type: float
    @return: El valor de tipo float ya creado
    @rtype: float
    
    '''
    if num_float=='':
        num_float=0.0
    else:
        num_float=float(num_float) 
    return num_float

def parsea_int(num_int):
    '''
    Con esta función creamos el valor de tipo entero a través de condiciones para luego tratarlo en el modulo principal
    @param str_f: Dato situado en el archivo csv con el fin de transformarlo en tipo entero
    @param type: int
    @return: El valor de tipo int ya creado
    @rtype: int
    
    '''
    if num_int=='':
        num_int=0
    else:
        num_int=int(num_int) 
    return num_int

