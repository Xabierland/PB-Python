#inicializaciones
num=int(input("Introduce un numero binario que comience en 1: "))

exp=0
suma=0
#descomponer el numero binario y crear el decimal
while(num>0):
    suma=suma + (num % 10)*2**(exp)
    exp=exp+1
    num=num//10
    
    
print("el numero en decimal es: ",  + suma)