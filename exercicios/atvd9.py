#Dia 9: Função fatorial(n) com laço e outra para Fibonacci (primeiros 15 termos)
def fatorial(n):
  mult = 1
  for i in range(1, n+1):
        mult *= i
  return mult
print("fatorial do numero 5: ")
print(fatorial(5))

def fibonati(n):
    f = 0
    b = 1
    for i in range(0, 15):
       print(f)
       novo = f + b # novo recebe soma de f e b
       f = b #f recebe o numero de b
       b = novo # b recebe o numero do novo, o numero da soma
print("fibonati 15 primeiros numeros: ")
(fibonati(15))
