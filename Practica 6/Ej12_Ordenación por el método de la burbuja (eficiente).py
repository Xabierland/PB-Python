def escribir_vector(V):
    print(V)


def ordenar_por_burbuja_eficiente(V):
    num_recorridos=0
    while num_recorridos<=ultimo(V):
        i=0
        while i<len(V)-1:
            if V[i] > V[i+1]:
                aux=V[i]
                V[i]=V[i+1]
                V[i+1]=aux
            i=i+1
        num_recorridos=num_recorridos+1
    return(V)

def ultimo(V):
    enc=False
    i=1
    j=0
    while enc==False and j>len(V):
        if V[-1-j]<V[-1-i]:
            enc=True
    return(V[-1-j])    

def principal():
    #Caso 1 
     vector1 = [9, 5, 3, 4, 10, 8, 13, 24, 15, 11]
     
     print("El vector inicial es (9,5,3,4,10,8,13,24,15,11):")
     escribir_vector(vector1)

     vector1=ordenar_por_burbuja_eficiente(vector1)
     print("El vector final deberia ser (3,4,5,8,9,10,11,13,15,24) y es:")
     escribir_vector(vector1)
     
     print("")
     
     #Caso 2 
     vector1 = [1,3,5,9,8,56,2,47]
     
     print("El vector inicial es (1,3,5,9,8,56,2,47):")
     escribir_vector(vector1)

     vector1=ordenar_por_burbuja_eficiente(vector1)
     print("El vector final deberia ser (1,2,3,5,8,9,47,56) y es:")
     escribir_vector(vector1)

     print("")

     #Caso 3
     vector1 = [1,1,1,1,2,1,1,1,1,2]
     
     print("El vector inicial es (1,1,1,1,2,1,1,1,1,2):")
     escribir_vector(vector1)

     vector1=ordenar_por_burbuja_eficiente(vector1)
     print("El vector final deberia ser (1,1,1,1,1,1,1,1,2,2) y es:")
     escribir_vector(vector1)
principal()
