#####################################################
def numero_de_digitos(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 5 o 9 digitos
   # Salida: un entero
   # Post: el numero de digitos del telefono
    num= tel
    cont=1
    while num//10 > 0:
        cont=cont+1
        num=num/10
    return cont

#################################################
def es_un_movil(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 6 o 7
    loes=False
    num= tel
    if (num // (10**8) == 6) or (num // (10**8) == 7) :
        loes=True
    return loes

    

##################################################
def es_numero_corto(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 5 o 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono tiene 5 digitos
    es=False
    if numero_de_digitos(tel)==5:
        es=True
    return es
    
    

##################################################
def es_de_coste_ampliado(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 803, 806, 807, 905 o 907
    num=tel
    es=False
    if (num // 10**6)==803 or (num // 10**6)==806 or (num // 10**6)==807 or (num // 10**6)==905 or (num // 10**6)==907 :
        es=True
    return es
##################################################
def es_de_coste_semiampliado(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 902
    num=tel
    es=False
    if (num // 10**6)==902 :
        es=True
    return es
   
   
##################################################
def es_de_coste_compartido(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 901
    num=tel
    es=False
    if (num // 10**6)==901 :
        es=True
    return es    
   
    
##################################################
def es_de_cobro_revertido(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 800 o 900
    num=tel
    es=False
    if (num // 10**6)==800 or (num // 10**6)==900 :
        es=True
    return es
   
##################################################
def es_fijo_local(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 9 digitos
   # Salida: un booleano
   # Post: true si el numero de telefono comienza por 943, 945, 948 o 94 (salvo 941, 942, 947, y 949)
    num=tel
    es=False
    if (num // 10**6)==940 or (num // 10**6)==943 or (num // 10**6)==944 or (num // 10**6)==945 or (num // 10**6)==946 or (num // 10**6)==948 :
        es=True
    return es
    
##################################################
def tipo_de_numero(tel):
   # Entrada: un numero de telefono
   # Pre: el numero tiene 5 o 9 digitos
   # Salida: un entero entre 1 y 8
   # Post: el tipo de llamada
      # 1 (numero corto)
      # 2 (movil)
      #	3 (fijo de cobro revertido)
      #	4 (fijo de coste semi-ampliado)
      #	5 (fijo de coste compartido)
      #	6 (fijo de coste ampliado)
      #	7 (fijo estandar local)
      #	8 (fijo estandar no local)
    tipo=0
    if es_numero_corto(tel)==True:
        tipo=1
    elif es_un_movil(tel)==True:
        tipo=2
    elif es_de_cobro_revertido(tel)==True:
        tipo=3  
    elif es_de_coste_semiampliado(tel)==True:
        tipo=4
    elif es_de_coste_compartido(tel)==True:
        tipo=5  
    elif es_de_coste_ampliado(tel)==True:
        tipo=6
    elif es_fijo_local(tel)==True:
        tipo=7 
    else:
        tipo=8
    return tipo
#########################################################
def coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos):
   # Entrada: 1. un numero de telefono
   #          2. la duracion de la llamada (en minutos)
   #          3. boolean: se dispone de tarifa plana a moviles 
   #          4. boolean: se dispone de tarifa plana a fijos
   # Pre: la duracion es >=1
   # Salida: dos valores numericos
   # Post: el tipo de llamada, entero entre 1 y 8
   #       el coste, valor real >=0
    tipo = tipo_de_numero(tel)
    coste= coste_de_llamada_por_tipo(tipo,min,tarifa_plana_moviles,tarifa_plana_fijos)
    return (tipo,coste)    
############################################################
def coste_de_llamada_por_tipo(tipo,min,tarifa_plana_moviles,tarifa_plana_fijos):
   #  Entrada: 1. el tipo de llamada
   #           2. la duracion de la llamada (en minutos)
   #           3. Boolean: se dispone de tarifa plana a moviles 
   #           4. Boolean: se dispone de tarifa plana a fijos 
   #  Pre: la duracion es >=1
   #       el tipo de llamada es un valor entre 1 y 8
   #  Salida: el coste de la llamada
   #  Post: el coste es >= 0
   #          tipo 1 : gratis 0
   #          tipo 2 : minutos*0,02 o gratis
   #          tipo 3 : gratis
   #          tipo 4 : minutos*0,025
   #          tipo 5 : minutos*0,012
   #          tipo 6 : minutos*0,3
   #          tipo 7 : minutos*0,004 o gratis
   #          tipo 8 : minutos*0,01 
    if tipo==1 or tipo==3 or (tipo==2 and tarifa_plana_moviles==True) or (tipo==7 and tarifa_plana_fijos==True) :
        coste=0.0
    if (tipo==2 and tarifa_plana_moviles== False):
        coste= min*0.02
    if tipo==4:
        coste= min*0.025
    if tipo==5:
        coste= min*0.012
    if tipo==6:
        coste= min*0.3
    if (tipo==7 and tarifa_plana_fijos== False):
        coste= min*0.004
    if tipo==8 :
        coste= min*0.01      
    return coste    
    
############################################################
def pruebas():
    tarifa_plana_moviles = False
    tarifa_plana_fijos = False

    # Caso de prueba 1. Numero corto y sin tarifas planas. Un minuto
    tel=11818
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 1: tel: 11818 y min:1")
    print("El coste deberia ser 0.000 y el tipo 1; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    #Caso de prueba 2. Numero movil y sin tarifas planas. Un minuto
    tel=656161244
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 2: tel: 656161244 y min:1 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.020 y el tipo 2; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 3. Numero movil y sin tarifas planas. Un minuto
    tel=800048484
    min=10
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 3: tel: 656161244 y min:10")
    print("El coste deberia ser 0.00 y el tipo 3; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 4. Numero movil y sin tarifas planas. Un minuto
    tel=902565656
    min=2
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 4: tel: 902565656 y min:2 ")
    print("El coste deberia ser 0.050 y el tipo 4; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 5. Numero movil y sin tarifas planas. Un minuto
    tel=901585858
    min=5
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 5: tel: 901585858 y min:5 ")
    print("El coste deberia ser 0.06 y el tipo 5; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 6. Numero movil y sin tarifas planas. Un minuto
    tel=803585956
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 6: tel: 803585956 y min:1 ")
    print("El coste deberia ser 0.3 y el tipo 6; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 7. Numero movil y sin tarifas planas. Un minuto
    tel=806585956
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 7: tel: 806585956 y min:1 ")
    print("El coste deberia ser 0.3 y el tipo 6; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 8. Numero movil y sin tarifas planas. Un minuto
    tel=807585956
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 8: tel: 807585956 y min:1 ")
    print("El coste deberia ser 0.3 y el tipo 6; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 9. Numero movil y sin tarifas planas. Un minuto
    tel=905585956
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 9: tel: 905585956 y min:1 ")
    print("El coste deberia ser 0.3 y el tipo 6; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 10. Numero movil y sin tarifas planas. Un minuto
    tel=907585956
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 10: tel: 907885956 y min:1 ")
    print("El coste deberia ser 0.3 y el tipo 6; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    
    
    #Caso de prueba 11. Numero movil y sin tarifas planas. Un minuto
    tel=945564589
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 11: tel: 945564589 y min:2 (sin tarifa plana a fijos)")
    print("El coste deberia ser 0.008 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 12. Numero movil y sin tarifas planas. Un minuto
    tel=943254240
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 12: tel: 943254240 y min:1 (sin tarifa plana a fijos)")
    print("El coste deberia ser 0.004 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 13. Numero movil y sin tarifas planas. Un minuto
    tel=948457878
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 13: tel: 948457878 y min:1 (sin tarifa plana a fijos)")
    print("El coste deberia ser 0.004 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 14. Numero movil y sin tarifas planas. Un minuto
    tel=940252589
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 14: tel: 940252589 y min:1 (sin tarifa plana a fijos)")
    print("El coste deberia ser 0.004 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 15. Numero movil y sin tarifas planas. Un minuto
    tel=944787896
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 15: tel: 944787896 y min:1 (sin tarifa plana a fijos)")
    print("El coste deberia ser 0.004 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    #Caso de prueba 16. Numero movil y sin tarifas planas. Un minuto
    tel=946989863
    min=2
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 16: tel: 946989863 y min:2 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.008 y el tipo 7; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
     
    #Caso de prueba 17. Numero movil y sin tarifas planas. Un minuto
    tel=941585963
    min=2
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 17: tel: 941585963 y min:2 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.0.02 y el tipo 8; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
     
    #Caso de prueba 18. Numero movil y sin tarifas planas. Un minuto
    tel=942584123
    min=96
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 18: tel: 942584123 y min:96 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.96 y el tipo 8; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
     
    #Caso de prueba 19. Numero movil y sin tarifas planas. Un minuto
    tel=947854125
    min=11
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 19: tel: 947854125 y min:11 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.11 y el tipo 8; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
     
    #Caso de prueba 20. Numero movil y sin tarifas planas. Un minuto
    tel=949852369
    min=10
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 20: tel: 949852369 y min:10 (sin tarifa plana a moviles)")
    print("El coste deberia ser 0.1 y el tipo 8; y segun tu programas sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("###################")
    
    
    # Caso de prueba 21. Numero movil con tarifa plana. Un minuto
    tarifa_plana_moviles = True
    tel=656161244
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 21: tel: 656161244 y min:1")
    print("El coste deberia ser 0.000 y el tipo 2; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
   

    # Caso de prueba 22. Numero movil con tarifa plana. Un minuto
    tarifa_plana_moviles = True
    tel=756161244
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 22: tel: 756161244 y min:1")
    print("El coste deberia ser 0.000 y el tipo 2; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    # Caso de prueba 23. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=940258965
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 23: tel: 940258965 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    # Caso de prueba 24. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=943254898
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 24: tel: 943254898 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    
    # Caso de prueba 25. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=944875896
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 25: tel: 944875896 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    # Caso de prueba 26. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=945821365
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 26: tel: 945821365 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    # Caso de prueba 27. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=946852036
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 27: tel: 946852036 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
    # Caso de prueba 28. Numero fijo estandar local con tarifa plana. Un minuto
    tarifa_plana_fijos = True
    tel=948520123
    min=1
    (coste,tipo)=coste_de_llamada(tel,min,tarifa_plana_moviles,tarifa_plana_fijos)
    print("Caso 28: tel: 948520123 y min:1")
    print("El coste deberia ser 0.000 y el tipo 7; y segun tu programa sus valores son: ")
    print("  ")
    print(coste)
    print(" y ")
    print(tipo)
    print("#################################")
    
pruebas()