def escribir_vector(V):
    i=0
    print ('[', end='')
    while i<len(V)-1:
        print (V[i], end=', ')
        i=i+1
    print (V[i], end='')
    print (']')


def ordenar_por_insercion(V):
    i=1
    while i<len(V):
        if V[i]<V[i-1]:
            pos=buscar_posicion_de_insercion(V, i, V[i])
            desplazar_una_posicion_a_la_derecha(V,i,pos)
        i=i+1

    return(V)

def desplazar_una_posicion_a_la_derecha(V,posActual,posComienzo):
    elem=V[posActual]
    while posComienzo!=posActual:
        V[posActual]=V[posActual-1]
        posActual=posActual-1
    V[posComienzo]=elem
    return(V)


def buscar_posicion_de_insercion(V,posActual,elem):
    while posActual!=0:
        if elem<V[posActual-1]:
            pos=posActual-1
        posActual=posActual-1
    return(pos)

def principal():
     #Caso 1 
     vector1 = [9, 5, 3, 4, 10, 8, 13, 24, 15, 11]
     
     print("El vector inicial es (9,5,3,4,10,8,13,24,15,11):")
     escribir_vector(vector1)

     vector1=ordenar_por_insercion(vector1)
     print("El vector final deberia ser (3,4,5,8,9,10,11,13,15,24) y es:")
     escribir_vector(vector1)

     #Caso 2 
     vector1 = [8, 9 ,10, 3, 2, 1, 6, 5, 20, 18]
     
     print("El vector inicial es (8,9,10,3,2,1,6,5,20,18):")
     escribir_vector(vector1)

     vector1=ordenar_por_insercion(vector1)
     print("El vector final deberia ser (1,2,3,5,6,8,9,10,18,20) y es:")
     escribir_vector(vector1)
     
     #Caso 3 
     vector1 = [2, 2, 2, 2, 1, 2, 2, 2, 2, 1]
     
     print("El vector inicial es (2,2,2,2,1,2,2,2,2,1):")
     escribir_vector(vector1)

     vector1=ordenar_por_insercion(vector1)
     print("El vector final deberia ser (1,1,2,2,2,2,2,2,2,2) y es:")
     escribir_vector(vector1)

principal()
