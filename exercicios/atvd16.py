#A conversão de decimal para binário
n = (int(input("digite um numero: ")))
numero0 = n
binario = ""
if n == 0:
    binario = "0"
   
while n>0:
    resul1 = n % 2
    binario = str(resul1) + binario
    n = n //2
print (f"o numero {numero0} em binario e {binario}")