#Una evaluación condicional puedd estar dentro de otra.por ejemplo:
name =input("Hola, cúal es tu nombre")
age = int(input("dime tu edad"))

print("Hola",name,"!")

if(age >= 18):
  drink = input("¿Quieres una cerveza o vino?")
  if(drink) == "cerveza":
     print("Aqui tienes tu cervaza")
  else:
     print("Acá está tu vino")

else:
   juice = input("¿quiers jugo de frutilla o naranja?")
   if (juice == "frutilla" or juice == "frutillas"):
      print("acá está tu jugo de fresas")
   else: 
      print("toma tu jugo de naranajas")        


