soma = 0
contador = 0
a = int(input("digite um numero: "))
while a != 0:
    soma += a
    contador += 1
    a = int(input("digite outro numero: "))
print("soma e", soma)
if contador > 0:
  media = (soma/contador)
  print("media e", media)
