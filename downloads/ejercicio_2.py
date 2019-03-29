
def elevado(a,b):
 for i in range(0,2):
  a=int(input("ingrese el numero"))
  b=int(input("ingrese el segundo numero"))
  n=a**b
  print(n)
  if i==0:
   elevado_uno=elevado(a, b)
  else:
   elevado_dos=elevado(a, b)
    
if elevado_uno>elevado_2:
  print("es mayor ",elevado_1)
else:
  print("el mayor es",elevado_dos)

elevado()



