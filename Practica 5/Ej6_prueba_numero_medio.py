def numero_medio(num):
   # Entrada: un numero 
   # Pre: numero entero positivo
   # Salida: un entero
   # Post: el numero
    num_aux=num
    menores=0
    mayores=0
    es=False   
    cont=1
    cant=1

    while cont<num_aux :
        menores=menores+cont
        cont=cont+1
    
    
    while mayores<=menores :    
        mayores=mayores+(num_aux+cant)
        if mayores==menores:
            es=True
        cant=cant+1 
    return es
#    if es ==False:
#        print("el numero introducido no es un numero medio")
#    else:
#        print("el numero introducido es un numero medio")
        
        
def pruebas():
   # Caso de prueba 1. Numero = 0
    num=0
    print("Caso 1: num:0")
    print("El programa deberia dar False ; y segun tu programa es: ")
    print("  ")
    print(numero_medio(0))
    
    print("#################################")
    
   # Caso de prueba 2. Numero = 6
    num=6
    
    print("Caso 2: num:6")
    print("El programa deberia dar True ; y segun tu programa es: ")
    print("  ")
    print(numero_medio(6))
    
    print("#################################")


    # Caso de prueba 3. Numero = 8
    num=6
    
    print("Caso 3: num:8")
    print("El programa deberia dar False ; y segun tu programa es: ")
    print("  ")
    print(numero_medio(8))
    
    print("#################################")

    # Caso de prueba 4. Numero = 35
    num=35
    
    print("Caso 4: num:35")
    print("El programa deberia dar True ; y segun tu programa es: ")
    print("  ")
    print(numero_medio(35))
    
    print("#################################")
    
    # Caso de prueba 5. Numero = 654895
    num=654895
    
    print("Caso 5: num:654895")
    print("El programa deberia dar False ; y segun tu programa es: ")
    print("  ")
    print(numero_medio(654895))
    
    print("#################################")
pruebas()