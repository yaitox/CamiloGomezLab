a=int(input("ingresa el numero"))
def primos():
  if a<1:
    print("no es primo")
  elif a>2:
   if a%2==0:
     print("no es primo")
   if a%a==1:
     print("ES PRIMO")
primos()