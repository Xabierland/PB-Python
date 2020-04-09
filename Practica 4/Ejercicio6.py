cont = 0
num = int(input("Escribe un numero: "))
while num != 0 :
    resto = num % 10
    num = num//10
    if resto % 2 != 0 :
        cont = cont + 1
print ("Su numero tiene")
print (cont)
print ("digito(s) impar(es)")