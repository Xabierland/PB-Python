def escribir_vector(V):
    i=0
    while i<len(V)-1:
        print (V[i], end=', ')
        i=i+1
    print (V[i], end='')
       


def rotar_derecha(V):
    aux=V[len(V)-1]    
    i=1
    j=0
    while i < len(V):        
        V[len(V)-1-j]=V[len(V)-1-i]
        i=i+1
        j=j+1
    V[0]=aux
    
    return [V]
   

def principal(): 
    #inicializar
    vector1=[1,2,3,4,5,6,7,8,9,10]
 
    print("un vector de diez elementos: \n [1,2,3,4,5,6,7,8,9,10]")
    print(" Los elementos del vector inicial son: ")
    escribir_vector(vector1)

    print(" al rotar los elementos el resultado es:\n [10,1,2,3,4,5,6,7,8,9] ")
    vector1=rotar_derecha(vector1)
    escribir_vector(vector1)

    print('')

    vector1=[34,67,45,23,78,12,40,55,24,89]
 
    print("un vector de diez elementos: \n [34,67,45,23,78,12,40,55,24,89]")
    print(" Los elementos del vector inicial son: ")
    escribir_vector(vector1)

    print(" al rotar los elementos el resultado es:\n [89,34,67,45,23,78,12,40,55,24] ")
    vector1=rotar_derecha(vector1)
    escribir_vector(vector1)

    vector1=[1,1,1,1,1,1,1,1,1,2]
 
    print("un vector de diez elementos: \n [1,1,1,1,1,1,1,1,1,2]")
    print(" Los elementos del vector inicial son: ")
    escribir_vector(vector1)

    print(" al rotar los elementos el resultado es:\n [2,1,1,1,1,1,1,1,1,1]")
    vector1=rotar_derecha(vector1)
    escribir_vector(vector1)

principal()
