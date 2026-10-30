#Dia 13: Função que conta as vogais de uma frase; função que verifica palíndromo
def conta_vogais(frase):
    contaa = 0
    contae = 0
    contai = 0
    contao = 0
    contau = 0
    vogalcontagem = 0 
    for i in frase:
     if i == "a"   or i == "A" :
        contaa += 1
     elif i == "e" or i == "E" :
        contae += 1
     elif i == "i" or i == "I" :
        contai += 1
     elif i == "o" or i == "O" :
        contao += 1
     elif i == "u" or i == "U":
        contau += 1

    print(f"o a quantidade das vogais a é", contaa)
    print(f"o a quantidade das vogais e é", contae)
    print(f"o a quantidade das vogais i é", contai)
    print(f"o a quantidade das vogais o é", contao)
    print(f"o a quantidade das vogais u é", contau)

    return conta_vogais
a = str(input("digite uma frase: "))
resul = conta_vogais(a)
print(resul)

def palindromo(palavra):
   inicio = 0
   fim = len(palavra) - 1
   while inicio < fim:
     if palavra[inicio] != palavra[fim]:
       return False
     
     inicio += 1
     fim -= 1
   return True

palavra = str(input("digite novamente a palavra: "))
result = palindromo(palavra)
print(f"palavra = {palavra} é palindromo? {result}")
