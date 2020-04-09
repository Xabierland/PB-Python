def suma_binaria(binario1,binario2):
    bin1=binario1
    bin2=binario2
    peso=0
    llevada=0
    sumaBin=0
    resto1=0
    resto2=0
    aux=0
    end=False
    while end==False:
        if (bin1==0 and bin2==0):
            end=True
        resto1=bin1 % 10
        resto2=bin2 % 10
        bin1=bin1//10
        bin2=bin2//10
        aux=resto1+resto2+llevada
        llevada=0
        if aux==2:
            aux=0
            llevada=1
        if aux==3:
            aux=1
            llevada=1
        sumaBin= sumaBin+(aux*10**peso)
        peso=peso+1
    return(sumaBin)

def prueba():
    binario1=0
    binario2=0
    resultado=suma_binaria(binario1,binario2)
    print("0 + 0 en binario es 0 y segun tu programa es %d." %resultado)
        
    binario1=0
    binario2=1
    resultado=suma_binaria(binario1,binario2)
    print("0 + 1 en binario es 1 y segun tu programa es %d." %resultado)

    binario1=1
    binario2=0
    resultado=suma_binaria(binario1,binario2)
    print("1 + 0 en binario es 1 y segun tu programa es %d." %resultado)

    binario1=1
    binario2=1
    resultado=suma_binaria(binario1,binario2)
    print("1 + 1 en binario es 10 y segun tu programa es %d." %resultado)

    binario1=11
    binario2=11
    resultado=suma_binaria(binario1,binario2)
    print("11 + 11 en binario es 110 y segun tu programa es %d." %resultado)
    
    binario1=111
    binario2=100
    resultado=suma_binaria(binario1,binario2)
    print("111 + 100 en binario es  y 1011 segun tu programa es %d." %resultado)

    binario1=101
    binario2=100
    resultado=suma_binaria(binario1,binario2)
    print("101 + 100 en binario es 1001 y segun tu programa es %d." %resultado)
prueba()
