def calcular_totales (matriz:list,depositos:list,camisetas:list, tipo:str):
    if tipo == "deposito":
        lista_retorno = [0] * len(depositos)
        lista_retorno2 = [0] * len(depositos)
        for i in range(len(matriz)):
            acumulador = 0
            for j in range(len(matriz[i])):
                acumulador += matriz[i][j]
            lista_retorno[i] = acumulador
            lista_retorno2 [i] = depositos[i]
        return lista_retorno, lista_retorno2
    else:
        lista_retorno = [0] * len(camisetas)
        lista_retorno2 = [0] * len(camisetas)
        for i in range(len(camisetas)):
            acumulador = 0
            for j in range(len(depositos)):
                acumulador += matriz[j][i]
            lista_retorno[i] = acumulador
            lista_retorno2 [i] = camisetas[i]
        return lista_retorno,lista_retorno2


def estimar_stock (lista2:list,totales:list,limite:int,tipo:str):

    for i in range(len(totales)):
        if totales[i] > limite:
            print(f"los {tipo} que tienen mas de {limite} en stock son {lista2[i]}")
    return

def calcular_maximo_camisetas (matriz:list, deposito:list,camisetas:list):
    
    for i in range(len(camisetas)):
        bandera = True
        for j in range(len(deposito)):
            if bandera == True:
                maximo_camisetas = matriz[j][i]
                maximo_deposito = deposito[j]
                bandera = False
            elif maximo_camisetas < matriz[j][i]:
                maximo_camisetas = matriz[j][i]
                maximo_deposito = deposito[j]
            else:
                pass
        print(f"el deposito con mas camisetas de {camisetas[i]} es {maximo_deposito}")
     
    return

def trasponer_matriz (matriz:list):
    
    "lo que hace esta funcion es trasponer una matriz"

    matriz_traspuesta=[0,0,0],[0,0,0],[0,0,0]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_traspuesta[j][i] = matriz [i][j]

    return matriz_traspuesta