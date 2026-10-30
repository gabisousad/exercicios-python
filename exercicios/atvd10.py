#Função que calcula o MDC de dois números; testar com 5 pares
#a = int(input("digite um numero: "))
#b = int(input("digite um numero: "))
def mdc(a,b):
  while b != 0: #para todo b diferente de 0 
     rest = a % b 
     a = b
     b = rest
  return(a)
pares = [(48, 18), (20, 8), (35, 14), (100, 25), (13, 7)] #lista dos numeros para o mdc
for a,b in pares: 
   print(mdc(a,b))

