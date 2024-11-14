def crar_matriz (filas:int,columnas:int,valor_predeterminado:any):
    matriz = []

    for _ in range(filas):
        fila=[valor_predeterminado] * columnas
        matriz+=[fila]
    return matriz

def mostrar_matriz (matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print (matriz[i][j] , end = " ")
        print (" ")
    return
def pedir_matriz (matriz:list,filas:list,columas:list,menu:int):

    for i in range(len(filas)):
        for j in range(len(columas)):
            if menu == "1":    
                cantidad = int(input(f"ingrese la cantidad de camisetas del {columas[j]} del deposito {filas[i]}"))
                matriz[i][j] = cantidad 
            else:
                pass
    print(matriz)
    return matriz
    
                    