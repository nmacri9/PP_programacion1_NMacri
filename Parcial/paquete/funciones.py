
"""Una empresa se dedica al almacenamiento y posterior distribución de artículos de limpieza
en el interior del país. Para ello cuentan con 3 depósitos distribuidos en diferentes
provincias (PBA, Jujuy y Neuquén).
Los depósitos pueden almacenar 7 tipos diferentes de artículos: químicos, trapos, escobas,
cepillos, papel higiénico, jabón y pañuelos descartables.
La oficina central, recibe mensualmente una planilla de existencias donde se indican las
existencias de cada juguete para cada depósito.

Realizar un menú de opciones:
1. Obtener existencias: para ello deberá cargar en el main la existencia de cada artículo
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de artículo y cantidad.
2. Calcular por cada depósito la cantidad total de artículos almacenados entre todos los
tipos.
3. Obtener los nombres de los artículos que es necesario reponer en cada depósito.
Crear una función que devuelva todos los juguetes con menos de 3000 unidades.
4. Máxima cantidad de artículos almacenados de cada tipo. Devolver en qué provincia se
encuentran por si es necesario redistribuir.
5. Generar una función que permita corregir un error de carga mediante carga aleatoria o
distribuida de matrices.
6. Cantidad de depósitos que hayan almacenado más de 3.000.000 de unidades entre
los 7 artículos. Mostrar provincias.
7. Porcentaje de artículos de cada tipo sobre el total de artículos almacenados. Realizar
una función que muestre el porcentaje de cada uno.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
usando bubble sort o selection sort. Justificar la elección del algoritmo. Para ello la
función deberá recibir una matriz de ventas, y una lista de precios.
9. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de artículo. Esto se debe hacer con una función que reciba
la lista de precios por parámetro para poder actualizarlos frente a la inflación.
"""
#punto 2 2. Calcular por cada depósito la cantidad total de artículos almacenados entre todos los tipos.
def calcular_total(existencias: list) -> list :
    total_por_provincia = [0,0,0]
    provincias = ['PBA', 'Jujuy', 'Neuquen']
    for existencia in existencias:
        if existencia[0] == provincias[0]:
            total_por_provincia[0] += existencia[2]
        elif existencia[1] == provincias[1]:
            total_por_provincia[1] += existencia[2]
        elif existencia[0] == provincias[2]:
            total_por_provincia[2] += existencia[2]
    return total_por_provincia

#punto 3. 3. Obtener los nombres de los artículos que es necesario reponer en cada depósito.
 #Crear una función que devuelva todos los juguetes con menos de 3000 unidades.

def reponer_articulos (existencias):
    reponer = []
    for existencia in existencias:
        if existencia[2] < 3001:
            reponer += existencia
    return reponer

#punto 5

def corregir_error (existencias, provincia, tipo, nueva_cantidad):
    for existencia in existencias:
        if existencia[0] == provincia and existencia [1] == tipo:
            existencia[2] == nueva_cantidad
            break
