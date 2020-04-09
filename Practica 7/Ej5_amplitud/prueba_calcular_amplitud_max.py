def escribir_lista(L):
    print("[ ", end="")
    for i in range(0,len(L)):
        print(str(L[i]) + " ", end="")        
    print("]", end="")
    
def calcular_amplitud_max (L): 
    # Pre: Lista tiene al menos dos elementos y comienza con una
    #      subsecuencia ascendente 
    #      La lista no tiene dos elementos iguales consecutivos
    # Post: Devuelve la longitud del segmento de mayor amplitud
    #       En caso de que no haya ningun segmento el resultado sera cero
    i=1
    contA=1
    contD=0
    cont=0
    contMax=0
    while i<len(L):
        while i<len(L) and L[i-1]<L[i]:
            contA=contA+1
            i=i+1
        while i<len(L) and L[i-1]>L[i]:
            contD=contD+1
            i=i+1
        cont=contA+contD
        if cont>contMax and contA!=0 and contD!= 0:
            contMax=cont
        contA=1
        contD=0
    return(contMax)

def prueba_calcular_amplitud_max(): 
   # Este programa hace llamadas a la funcion calcular_amplitud_max y  
   # permite comprobar si su funcionamiento es correcto
    L = [12, 16]
   
    print("Prueba 1: Solo ascendente, dos elementos")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 0 y es: ")
    print(calcular_amplitud_max(L))
    print()

    L = [1,2,3,4,5,6,7,8,9]
   
    print("Prueba 2: Solo ascendente, muchos elementos")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 0 y es: ")
    print(calcular_amplitud_max(L))
    print()

    L = [1,4,3,2]
   
    print("Prueba 3: Ascendente y descendente, 4 elementos")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 4 y es: ")
    print(calcular_amplitud_max(L))
    print()

    L = [1,4,3,2,4,5,6,7,6,5,4,3]
   
    print("Prueba 4: Ascendente y descendente, 2 casos de diferentes longitudes")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 9 y es: ")
    print(calcular_amplitud_max(L))
    print()

    L = [1,3,4,6,5,4,3,4,5,6,7,8,9,7,3,1,4,5,7,9]
   
    print("Prueba 5: Ascendentes y descendentes, 3 casos de diferentes longitudes")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 10 y es: ")
    print(calcular_amplitud_max(L))
    print()

    L = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,3,5,7,9,8,6,4,2]
   
    print("Prueba 5: Ascendentes y descendentes, 2 casos de diferentes longitudes largos")
    print("La entrada es ", end="")
    escribir_lista(L)
    print(". El resultado deberia ser 17 y es: ")
    print(calcular_amplitud_max(L))
    print()


prueba_calcular_amplitud_max()