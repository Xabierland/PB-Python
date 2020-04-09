def esta_en_vector(x,vec):
   rs=False
   for i in range(0,len(vec)):
      if x == vec[i]:
         rs=True
   return(rs)

def principal():
   Vector1 = [1, 13, 55, 27, 99, 111, 133, 150, 17, 6]
   print("Prueba1: el valor esta en medio")
   print(" esta_en_vector(111, (1, 13, 55, 27, 99, 111, 133, 150, 17, 6))")
   print(" debe ser True y el resultado es ")
   rdo=esta_en_vector(111,Vector1)
   print(rdo)
   print()

   Vector1 = [16, 33, 567, 73, 9, 111, 153, 15, 197, 1]
   print("Prueba2: el valor esta al final")
   print(" esta_en_vector(1, (16, 33, 567, 73, 9, 111, 153, 15, 197, 1))")
   print(" debe ser True y el resultado es ")
   rdo=esta_en_vector(1,Vector1)
   print(rdo)
   print()

   Vector1 = [19, 3, 556, 72, 91, 11, 1, 15, 817, 199]
   print("Prueba3: el valor no esta")
   print(" esta_en_vector(45, (19, 3, 556, 72, 91, 11, 1, 15, 817, 199))")
   print(" debe ser False y el resultado es ")
   rdo=esta_en_vector(45,Vector1)
   print(rdo)
   print()

   Vector1 = [19, 19, 556, 72, 91, 11, 1, 15, 817, 199]
   print("Prueba3: el valor esta al principio")
   print(" esta_en_vector(19, (19, 3, 556, 72, 91, 11, 1, 15, 817, 199))")
   print(" debe ser True y el resultado es ")
   rdo=esta_en_vector(19,Vector1)
   print(rdo)
   print()
principal()
