def esta_en_posicion(x,vec):
     i=0
     rst=False
     while rst==False and i<len(vec):
          if x==vec[i]:
               rst=True
          i=i+1
     return(rst,i)

def principal():
   Vector1 = [1, 3, 5, 17, 9, 11, 131, 15, 170, 19]
   print("Prueba 1:  el valor esta en medio")
   print(" esta_en_posicion(131, (1, 3, 5, 17, 9, 11, 131, 15, 170, 19))")
   print(" debe ser True y el resultado es ")
   rdo, posi=esta_en_posicion(131,Vector1)
   if rdo:
        print("el numero %d esta en la posicion %d " %(131,posi))
   else:
        print("El numero no esta")
   print ()

   Vector1 = [1, 3, 5, 17, 9, 11, 131, 15, 170, 19]
   print("Prueba 2:  el valor esta al final")
   print(" esta_en_posicion(19, (1, 3, 5, 17, 9, 11, 131, 15, 170, 19))")
   print(" debe ser True y el resultado es ")
   rdo, posi=esta_en_posicion(19,Vector1)
   if rdo:
        print("el numero %d esta en la posicion %d " %(19,posi))
   else:
        print("El numero no esta")
   print ()

   Vector1 = [1, 3, 5, 17, 9, 11, 131, 15, 170, 19]
   print("Prueba 3: el numero no esta ")
   print(" esta_en_posicion(1912, (1, 3, 5, 17, 9, 11, 131, 15, 170, 19))")
   print(" debe ser False y el resulta do es ")
   rdo, posi=esta_en_posicion(1912,Vector1)
   if rdo:
        print("el numero %d esta en la posicion %d " %(1912,posi))
   else:
        print("El numero no esta")
   print ()

   Vector1 = [1, 3, 5, 17, 9, 11, 131, 15, 11, 19]
   print("Prueba 4: el numero no esta ")
   print(" esta_en_posicion(11, (1, 3, 5, 17, 9, 11, 131, 15, 170, 19))")
   print(" debe ser False y el resulta do es ")
   rdo, posi=esta_en_posicion(11,Vector1)
   if rdo:
        print("el numero %d esta en la posicion %d " %(11,posi))
   else:
        print("El numero no esta")
   print ()
    
principal()
