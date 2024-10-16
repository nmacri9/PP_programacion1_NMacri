from funciones import *
"""
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

menu1=\
"""
1_ Obtener existencias. (provincia, tipo de artículo y cantidad.)
2_ Calcular por cada depósito.
3_ Obtener nombres de los articulos.
4_ Maxima cantidad de articulos almacenados de cada tipo.
5_ Funcion para corregir error.
6_ Cantidad de depositos almacenados.
7_ Porcentaje de artículos de cada tipo sobre el total de artículos almacenados.
8_ Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
9_ Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de artículo.

"""
provincias = ['PBA', 'Jujuy', 'Neuquen']
total_por_provincia = [0,0,0] 
menu = 0
existencias = []
respuesta = True
#punto 1
# seria : [PROVINCIA, ARTICULO, CANTIDAD]
existencias = [
        ['PBA','quimicos', 4000],
        ['PBA','trapos', 1500],
        ['Neuquen','escobas', 3000],
        ['Neuquen','cepillos', 2000],
        ['Neuquen','papel higiénico', 4500],
        ['Jujuy','jabón', 5000 ],
        ['Jujuy','pañuelos descartables', 4000],
]


while respuesta == True:
    menu = input(f'{menu1}')
    match menu:
        case '1':
            print(existencias)
            pass
        case '2':
            if existencias:
                total_por_provincia = calcular_total(existencias)
                for i in range (len(total_por_provincia)):
                    print(f'{provincias[i]}: {total_por_provincia[i]} unidades del total')
            pass
        case '3':
            reponer=reponer_articulos(existencias)
            print('Articulos a reponer: ')
            for i in reponer:
                print(f'Articulo {existencias[1]}, Cantidad: {existencias[2]}.')
            pass
        case '4':
            pass
        case '5':
            provincia = input('ingrese la provincia: ')
            tipo = input ('ingrese el articulo: ')
            nueva_cantidad = int(input('Ingrese la nueva cantidad: '))
            print ('El error ha sido corregido.')
            pass
        case '6':
            
            pass
        case '7':
            pass
        case '8':
            pass
        case '9':
            pass
        case '':
            print('La opcion ingresada no es válida.')
