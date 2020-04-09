def posicion_en_matriz(M,num):
#entrada:una matriz M
#pre: M tiene al menos una fila y al menos una columna llena de enteros
#salida: dos enteros PosF y PosC
#post: si num esta en la matriz entonces PosF contiene el valor de la fila en la que est�
#      y PosC la posici�n de la columna. Si Num aparece varias veces, se devuelve los valores
#      PosF y PosC relativos a su primera aparicion. Si no esta, ambas PosF y PosC valdran -1

    numFilas = 	len(M)
    numCols = len(M[0])
    PosF = 0
    PosC = 0
    rst=False
    while rst==False and PosF<numFilas:
        while rst==False and PosC<numCols:
            if num == M[PosF][PosC]:
                rst=True
            else:
                PosC= PosC+1
        if rst==False:
            PosC=0
            PosF= PosF+1
    if rst==False:
        PosF=-1
        PosC=-1
    return (PosF,PosC)
    
    
def principal():
    cols=[None]*9
    Matriz=[cols]*10
    
    #el elemento esta al comienzo
    print("La matriz es: ")
    Matriz[0]=[1,2,3,4,5,6,7,8,9]
    Matriz[1]=[11,12,13,14,15,16,17,18,19]
    Matriz[2]=[21,22,23,24,25,26,27,28,29]
    Matriz[3]=[31,32,33,34,35,36,37,38,39]
    Matriz[4]=[41,2,3,4,55,6,7,8,9]
    Matriz[5]=[51,2,3,4,5,67,7,8,9]
    Matriz[6]=[61,2,3,4,5,6,79,8,9]
    Matriz[7]=[71,2,3,4,5,6,7,83,9]
    Matriz[8]=[81,2,3,4,5,6,73,8,93]
    Matriz[9]=[91,2,3,4,5,6,7,85,93]
    for fila in range(0,10):
        print(Matriz[fila])
    print("posicion_en_matriz(Matriz,1)  deberia devolver (0,0)")
    print("y el resultado es:")
    fila, cols=posicion_en_matriz(Matriz,1)
    print(fila, cols)
    
    #el elemento esta en la mitad de la matriz
    print("La matriz es: ")
    Matriz[0]=[1,2,3,4,5,6,7,8,9]
    Matriz[1]=[11,12,13,14,15,16,17,18,19]
    Matriz[2]=[21,22,23,24,25,26,27,28,29]
    Matriz[3]=[31,32,33,34,35,36,37,38,39]
    Matriz[4]=[41,2,3,4,55,6,7,8,9]
    Matriz[5]=[51,2,3,4,5,67,7,8,9]
    Matriz[6]=[61,2,3,4,5,6,79,8,9]
    Matriz[7]=[71,2,3,4,5,6,7,83,9]
    Matriz[8]=[81,2,3,4,5,6,73,8,93]
    Matriz[9]=[91,2,3,4,5,6,7,85,93]
    for fila in range(0,10):
        print(Matriz[fila])
    print("posicion_en_matriz(Matriz,21) deberia devolver (2,0)")
    print("y el resultado es:")
    fila, cols=posicion_en_matriz(Matriz,21)
    print(fila, cols)
    
    #el elemento esta al final
    print("La matriz es: ")
    Matriz[0]=[1,2,3,4,5,6,7,8,9]
    Matriz[1]=[11,12,13,14,15,16,17,18,19]
    Matriz[2]=[21,22,23,24,25,26,27,28,29]
    Matriz[3]=[31,32,33,34,35,36,37,38,39]
    Matriz[4]=[41,2,3,4,55,6,7,8,9]
    Matriz[5]=[51,2,3,4,5,67,7,8,9]
    Matriz[6]=[61,2,3,4,5,6,79,8,9]
    Matriz[7]=[71,2,3,4,5,6,7,83,9]
    Matriz[8]=[81,2,3,4,5,6,73,8,93]
    Matriz[9]=[91,2,3,4,5,6,7,85,100]
    for fila in range(0,10):
        print(Matriz[fila])
        
    print("posicion_en_matriz(Matriz,100)  deberia devolver (9,8)")
    print("y el resultado es:")
    fila, cols=posicion_en_matriz(Matriz,100)
    print(fila, cols)
    
    #el elemento no esta
    print("La matriz es: ")
    Matriz[0]=[1,2,3,4,5,6,7,8,9]
    Matriz[1]=[11,12,13,14,15,16,17,18,19]
    Matriz[2]=[21,22,23,24,25,26,27,28,29]
    Matriz[3]=[31,32,33,34,35,36,37,38,39]
    Matriz[4]=[41,2,3,4,55,6,7,8,9]
    Matriz[5]=[51,2,3,4,5,67,7,8,9]
    Matriz[6]=[61,2,3,4,5,6,79,8,9]
    Matriz[7]=[71,2,3,4,5,6,7,83,9]
    Matriz[8]=[81,2,3,4,5,6,73,8,93]
    Matriz[9]=[91,2,3,4,5,6,7,85,93]
    for fila in range(0,10):
        print(Matriz[fila])
        
    print("posicion_en_matriz(Matriz,200)  deberia devolver (-1,-1)")
    print("y el resultado es:")
    fila, cols=posicion_en_matriz(Matriz,200)
    print(fila, cols)
  
principal()
