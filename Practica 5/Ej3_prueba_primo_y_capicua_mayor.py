def es_capicua(num):
    capicua=False
    N_aux1=num
    N_aux2=num
    Digito=0

    if num==1 or num==2 or num==3 or num==4 or num==6 or num==8 or num==9 or num==5 or num==7:
       capicua=True
   
    while capicua==False and N_aux1 >= 10:
        N_aux1= N_aux1 // 10
        Digito= Digito + 1
  
    N_Inverso=N_aux1
    
    while capicua==False and N_aux2 >= 10:
        Resto_Digitos= N_aux2 % 10
        N_aux2= N_aux2 // 10
        N_Inverso= N_Inverso + Resto_Digitos*(10**Digito)
        Digito= Digito - 1
   
    if N_Inverso==num:
        capicua=True
   
    return capicua

def es_primo(num):
    Primo=True
    posible_Divisor=2

  

    while  Primo!=False and posible_Divisor!=num:
        if num % posible_Divisor == 0:
            Primo=False
        else:
            posible_Divisor= posible_Divisor + 1
     

   
    if num == 2 or num == 3 or num == 5 or num == 7:
        Primo= True
   
    return Primo


def primo_y_capicua_mayor(num):
    n= num + 1
    chivato=False
    while chivato != True:
        if es_capicua(n)==True and es_primo(n)==True:
          chivato=True
        else:
          n = n + 1

   
    return n


def prueba():
    #prueba 1
    print('El valor de entrada es 1, tu programa debe devolver 2.')
    resultado=primo_y_capicua_mayor(1)
    print('Y devuelve %d.' %resultado)
    print('')
    #prueba 2
    print('El valor de entrada es 7, tu programa debe devolver 11.')
    resultado=primo_y_capicua_mayor(7)
    print('Y devuelve %d.' %resultado)   
    print('')
    #prueba 3
    print('El valor de entrada es 32, tu programa debe devolver 101.')
    resultado=primo_y_capicua_mayor(100)
    print('Y devuelve %d.' %resultado)   
    print('')
    #prueba 4
    print('El valor de entrada es 453, tu programa debe devolver 727.')
    resultado=primo_y_capicua_mayor(453)
    print('Y devuelve %d.' %resultado)
    print('')
     #prueba 5
    print('El valor de entrada es 3000000, tu programa debe devolver 3001003.')
    resultado=primo_y_capicua_mayor(3000000)
    print('Y devuelve %d.' %resultado)
    print('')
    
prueba()
   
#Falta hacer la llamada al programa de pruebas