#Criar uma lista de 10 números; imprimir maior, menor, soma e média sem usar max/min
lista = [10,3,4,5,6,866,2,3,40,76] #fiz a lista com 10 num
soma = 0
media = 0
maior = lista[0] #variavel maior recebe o primeiro item da lista e considera ele como maior 
menor = lista[0]
#for i in lista: #percorre de i em toda lista 
 #   if i > maior: #se i que é o numero que ele percorre for maior que o numero do primeiro item 
  #      maior = i #a variavel maior recebe esse numero
#print(maior) #printa
#for a in lista:
 #   if a < menor:
  #      menor = a
#print(menor)
#for b in lista:
 #   soma += b
#print(soma)
#media = soma / 10
#print(media)
for i in lista:
    soma += i
    if i > maior:
        maior = i
        print(maior)
    if i < menor:
        menor = i
        print(menor)
#soma += i
print(soma)
media = soma /10
print(media)
    

        



