from funciones.auxiliares import *
from funciones.funciones import *
'''Ejercicio 1:
Se debe modularizar correctamente, utilizar parámetros opcionales y cumplir reglas de estilo.
No puede haber código repetido, ni funciones que realicen múltiples tareas. No se puede
utilizar sets, diccionarios, ni tuplas.
Una empresa se dedica al almacenamiento y posterior distribución de camisetas de fútbol en
todo el país. Para ello cuentan con 6 depósitos: Tierra del Fuego, Tucumán, Mendoza, BsAs, Misiones y Santa Fé.
Los depósitos almacenan camisetas de 5 equipos que son las que más se venden:
Barcelona, Inter Miami, PSG, Manchester City y Real Madrid.
Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
cuál es el límite que debe tomar para informar.
Realizar un menú de opciones:

1

1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.

Ejercicio 2:
En este ejercicio deberán programar funciones para realizar operaciones sobre matrices
cuadradas. Por ello se debe validar que las matrices que se reciben tengan la misma cantidad
de filas y columnas.
1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
cuadrada.
2. Generar una función que calcule la suma de las diagonales principal y secundaria de una
matriz.
Ejemplo:
1 2 3
4 5 6
7 8 9
Devuelve 30.
3. Generar una función que reciba una matriz y devuelva su transpuesta.
4. A la función del ejercicio 2 agregar un parámetro que permita seleccionar si lo que se
pretende recibir como retorno es la suma de ambas diagonales, solo la de la diagonal
principal o solo la de la diagonal secundaria.'''

menu1=\
'''
1- Obtener existencias
2- Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3- Mostrar equipos que hay en stock más de 5.000 camisetas.
4- Maxima cantidad de camisetas
5- Cargar ventas
6- Generar una función que calcule la media geométrica
7- Generar una función que calcule la suma de las diagonales de una matriz
8- muestra la matriz traspuesta
9- elegir ver la suma de las dos diagonales o por separado
10- salir

ingrese el numero: '''

depositos = ["Tierra del Fuego", "Tucumán", "Mendoza", "BsAs", "Misiones" , "Santa Fé"]
camisetas = ["Barcelona", "Inter Miami", "PSG", "Manchester City" ,"Real Madrid"]
res = True
carga = True
#matriz_general = [[10000,2,3,1,2],[1,10,1,10000,1],[1,1,1000,1,2],[1,2,10,4,5000],[6000,5,3,1,4],[0,9,8,4,3]]
while res == True:

    menu = input(menu1)
    match menu:
        case "1":
            if carga == True:
                matriz_general = crar_matriz(len(depositos),len(camisetas),0)
                matriz_general = pedir_matriz(matriz_general,depositos,camisetas,menu)
                carga=False
            else:
                print(f"{mostrar_matriz(matriz_general)}la carga ya fue hecha")
        case "2":
            total , lista2 = calcular_totales(matriz_general,depositos,camisetas,"deposito")
            estimar_stock(lista2,total,10000,"deposito")

        case "3":
            total,lista2 = calcular_totales(matriz_general,depositos,camisetas,"camisetas")
            estimar_stock(lista2,total,5000,"camisetas")
        case "4":
            calcular_maximo_camisetas(matriz_general,depositos,camisetas)
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            matriz_sin_trasponer = [[1,2,3,],
                                    [2,3,4,],
                                    [7,9,2,]]
            matris_traspuesta = trasponer_matriz(matriz_sin_trasponer)
            print(f"la matris traspuesta seria:")
            mostrar_matriz(matris_traspuesta)
        case "9":
            pass
        case "10":
            res = False
