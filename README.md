[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assig**nment_repo_id=8750742&assignment_repo_type=AssignmentRepo)
# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  22\23)
**Autor/a:** Jose Luis Moraza Vergara   **uvus:** josmorver@alum.us.es

Este proyecto tiene como finalidad el análisis de los datos acerca de los terremotos originados en los últimos siglos. Estos estan disponibles en el siguiente dataset cuya URL es:(https://www.kaggle.com/datasets/shekpaul/major-earthquakes-noaa?resource=download&select=NOAA+Earthquaqe+since+1600.csv).

Este dataset contiene 12 columnas en total tras la eliminación de 4 de ellas debido a la falta de valores en estas y la creación de una más de tipo cadena.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **modulo1.py**: En este módulo encontramos las funciones que analizan y realizan diversas operaciones con cada uno de los datos del dataset.
  * **modulo1_test.py**: Este módulo contiene las funciones de test para probar cada una de las implementaciones realizadas en el módulo descrito anteriormente `modulo1.py`
  * **parsers.py**: Contiene funciones de parseo usadas en el módulo principal `modulo1.py` que convierten algunos de los datos en enteros, reales o de tipo boolean,estableciendo algunas condiciones para aquellos valores que se encuentran ausentes en el dataset.

* **/data**: Contiene el dataset o datasets del proyecto
    * **dataset1.csv**: Dataset con los datos sobre terremotos que van a ser tratados 
   
    
## Estructura del *dataset*

El dataset contiene diversos datos acerca de la mayoría de los terremotos registrados hasta el día de hoy. Por ejemplo nos aporta información sobre la magnitud, las muertes causadas o la zona del país en la que ocurrieron.

El dataset está compuesto por 12 columnas, con la siguiente descripción:

* **id**: de tipo int, representa la posición que ocupa los datos del terremoto en el dataset.
* **tsunami**: de tipo boolean, representa si el terremoto ocasionó o no un tsunami.
* **year**: de tipo str,representa el año en el que ocurrió el terremoto, esta columna ha sido utilizada para crear el valor de tipo fecha
* **month**: de tipo str, representa el mes en el que ocurrió el terremoto, esta columna ha sido utilizada para crear el valor de tipo 
* **day**: de tipo str, representa el día en el que ocurrió el terremoto, esta columna ha sido utilizada para crear el valor de tipo fecha
* **latitude**: de tipo float, representa la latitud a la que ocurrió el terremoto.
* **longitude**: de tipo float, representa la longitud a la que ocurrió el terremoto.
* **focaldepth**: de tipo int, representa la profundidad del foco del terremoto.
* **magnitude**: de tipo float, representa la magnitud del terremoto según la escala de Richter.
* **deaths**: de tipo int, representa el número de muertes ocasionadas por el terremoto.
* **country**: de tipo str, indica el país en el que se originó el terremoto.
* **country_zone**: de tipo str, indica en que zona del país se ha originado el terremoto, esta columna es inventada por lo que sus datos no serán reales.

## **Tipos implementados**
Para agrupar los elementos de una manera más eficiente he definido la siguiente tupla con nombre:

`tuplatotal=namedtuple('tuplatotal','id,tsunami,latitude,longitude,focaldepth,magnitude,deaths,fecha,country,country_zone')`

Cuyos tipos son:

`tuplatotal=namedtuple('tuplatotal','int,boolean,float,float,int,float,int,fecha,str,str')`

**Decisiones de diseño**:
  * Las columnas **year**,**month** y **day** sirven para crear el valor de tipo fecha
  * La columna **tsunami** en vez de ser de tipo cadena, ha sido utilizada para crear un valor de tipo bool, estableciendo **Yes** como **True** y **No** o la ausencia de un valor como **False**

## **Funciones implementadas**
Para la trata de los datos, se han implementado diversas funciones en los distintos módulos del proyecto, siendo `modulo1` el principal,  `modulo1_test` el módulo con funciones de testeo que comprueban la funcionalidad de lo implementado en el `modulo1` y el módulo `parsers` el que contiene las funciones de parseo.

### **modulo1**

* **abrirdatos(fichero)**: Con esta función se realiza la apertura y lectura de los datos, además de almacenar cada elemento en una variable según el tipo de dato que sea para luego agruparlos, teniendo como salida una lista de tuplas llamada **listatotal** , en la que cada tupla representa una línea del dataset


### **modulo1_test**

* **mostrardatos(fichero)**: Con esta función testeamos el código del `modulo1`, mostrando el número total de registros leídos así como los tres primeros y los tres últimos de ellos. Para realizar esto se invoca a su vez la función abrirdatos.

* **main()**: Invoca a la función **mostrardatos** al iniciar el programa, obteniendo así lo requerido para la primera entrega.


### **parsers**

* **parsea_fecha(year,month,day)**: Esta función consigue crear un valor de tipo fecha al introducirle tres parámetros, provenientes de 3 de las columnas del archivo csv , en este caso, las columnas **year**,**month** y **day**.

* **parsea_booleano(str_bool)**: Con esta función conseguimos crear un valor de tipo bool con los datos del archivo csv, en concreto de la columna **tsunami**

* **parsea_float(num_float)**: Crea valores de tipo float con los datos situados en las columnas **latitude**,**longitude** y **magnitude**, estableciendo una condición para los valores ausentes.

* **parsea_int(num_int)**: Crea valores de tipo entero con datos en las columnas **deaths** y **focaldepth**, estableciendo también condiciones para aquellas filas que no tienen valores