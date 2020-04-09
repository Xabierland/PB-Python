def escribir_vector(V):
    i=0
    while i<len(V)-1:
        print(V[i], end=',')
        i=i+1
    print(V[i])

def ordenar_pares_e_impares(V):
    i=0
    j=0
    while i<len(V):
        if V[i]%2!=0:
            j = buscar_siguiente_par (V, i)
            if j<len(V):
                V = intercambiar (V, i, j)
        i=i+1
        
    return(V)

def buscar_siguiente_par (V, pos):
    par=False
    pos= pos+1
    while pos<len(V) and par==False:
        if V[pos]%2==0:
            par=True
        else:
            pos=pos+1
    return(pos)

def intercambiar (V, i, j):
    aux=V[i]
    V[i]=V[j]
    V[j]=aux
    return(V)


def principal():
    #Caso 1 
    vector1 = [10, 3, 13, 4, 6, 3, 5, 2, 9, 7, 8, 18, 12, 2]
     
    print("El vector inicial es (10,3,13,4,6,3,5,2,9,7,8,18,12,2):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (10,4,6,2,8,18,12,2, 3,13,3,5,9,7)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)
        
    print("")

    #Caso 2 
    vector1 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
     
    print("El vector inicial es (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 3 
    vector1 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37]
     
    print("El vector inicial es (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 4
    vector1 = [1,3,5,7,9,11,13,15,17,2,4,6,8,10,12,14,16,18]
     
    print("El vector inicial es (1,3,5,7,9,11,13,15,17,2,4,6,8,10,12,14,16,18):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2,4,6,8,10,12,14,16,18,1,3,5,7,9,11,13,15,17)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 5
    vector1 = [2,4,6,8,10,12,14,16,18,1,3,5,7,9,11,13,15,17]
     
    print("El vector inicial es (2,4,6,8,10,12,14,16,18,1,3,5,7,9,11,13,15,17):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2,4,6,8,10,12,14,16,18,1,3,5,7,9,11,13,15,17)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)
    
    print("")

    #Caso 6
    vector1 = [1]
     
    print("El vector inicial es (1):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (1)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 7
    vector1 = [2]
     
    print("El vector inicial es (2):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 8
    vector1 = [0]
     
    print("El vector inicial es (0):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (0)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")
    
    #Caso 9
    vector1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
     
    print("El vector inicial es (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2,4,6,8,10,12,14,16,1,3,5,7,9,11,13,15)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

    #Caso 10
    vector1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     
    print("El vector inicial es (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):")
    escribir_vector(vector1)

    vector1=ordenar_pares_e_impares(vector1)
    print("El vector final deberia ser (2,4,6,8,10,12,14,16,1,3,5,7,9,11,13,15)")
    print("SIN IMPORTAR EL ORDEN de los pares entre si, ni de los impares entre si")
    print("y segun vuestro programa es:")
    escribir_vector(vector1)

    print("")

principal()
