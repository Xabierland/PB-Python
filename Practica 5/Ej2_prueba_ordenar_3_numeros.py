def intercambiar (n1,n2):
    
    aux = n1
    n1 = n2
    n2 = aux
    
    return n1,n2

def ordenar_dos_numeros (n1,n2):
    
    if n1 < n2 :
        n1,n2 = intercambiar(n1,n2)
    
    return n1,n2

def ordenar_tres_numeros (n1,n2,n3):
    n1,n2=ordenar_dos_numeros(n1,n2)
    n1,n3=ordenar_dos_numeros(n1,n3)
    n2,n3=ordenar_dos_numeros(n2,n3)
    
    return n1,n2,n3

def prueba():
    #totalmente desordenados
    # 2, 5, 7
    n1=2
    n2=5
    n3=7
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print("2,5,7 Tu programa deberia escribir 7 5 2 y escribe: %d %d %d" %(n1,n2,n3))
    
    # 2, 7, 5
    n1=2
    n2=7
    n3=5
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print("2,7,5 Tu programa deberia escribir 7 5 2 y escribe: %d %d %d" %(n1,n2,n3))

    # 7, 2, 5
    n1=7
    n2=2
    n3=5
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print ("7,2,5 Tu programa deberia escribir 7 5 2 y escribe: %d %d %d" %(n1,n2,n3))
    
    # 7, 5, 2
    n1=7
    n2=5
    n3=2
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print("7,5,2 Tu programa deberia escribir 7 5 2 y escribe: %d %d %d" %(n1,n2,n3))
    # 5, 5, 5
    n1=5
    n2=5
    n3=5
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print("5,5,5 Tu programa deberia escribir 5 5 5 y escribe: %d %d %d" %(n1,n2,n3))
    # 5, 5, 5
    n1=0
    n2=2
    n3=1
    n1,n2,n3=ordenar_tres_numeros(n1,n2,n3)
    print("0,2,1 Tu programa deberia escribir 2 1 0 y escribe: %d %d %d" %(n1,n2,n3))

prueba()
