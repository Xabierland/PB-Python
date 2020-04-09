def escribir_vector(V):
    i=0
    print ('[', end='')
    while i<len(V)-1:
        print (V[i], end=', ')
        i=i+1
    print (V[i], end='')
    print (']')

def intercambiar(V,posA,posB):
    aux=0
    aux=V[posB]
    V[posB]=V[posA]
    V[posA]=aux
    
    return(V)

def buscar_posicion_del_minimo(V,posComienzo):
    minimo=-1
    while posComienzo<len(V):
        if V[posComienzo]<V[minimo]:
            minimo=posComienzo
        posComienzo=posComienzo+1
    return(minimo)

def ordenar_por_seleccion(V):
    i=0
    while i<len(V):
        posm=buscar_posicion_del_minimo(V,i)
        V=intercambiar(V, i, posm)
        i=i+1
    return(V)

def principal():
     #Caso 1 
     vector1 = [9, 5, 3, 4, 10, 8, 13, 24, 15, 11]
      
     print("El vector inicial es (9,5,3,4,10,8,13,24,15,11):")
     escribir_vector(vector1)

     vector1=ordenar_por_seleccion(vector1)
     print("El vector final deberia ser (3,4,5,8,9,10,11,13,15,24) y es:")
     escribir_vector(vector1)
     
     #Caso 2 
     vector1 = [8, 9 ,10, 3, 2, 1, 6, 5, 20, 18]
     
     print("El vector inicial es (8,9,10,3,2,1,6,5,20,18):")
     escribir_vector(vector1)

     vector1=ordenar_por_seleccion(vector1)
     print("El vector final deberia ser (1,2,3,5,6,8,9,10,18,20) y es:")
     escribir_vector(vector1)
     
     #Caso 3 
     vector1 = [2, 2, 2, 2, 1, 2, 2, 2, 2, 1]
     
     print("El vector inicial es (2,2,2,2,1,2,2,2,2,1):")
     escribir_vector(vector1)

     vector1=ordenar_por_seleccion(vector1)
     print("El vector final deberia ser (1,1,2,2,2,2,2,2,2,2) y es:")
     escribir_vector(vector1)


principal()
