#Dia 14: Remover duplicados de uma lista e ordenar o resultado, sem set e depois com set
lista = [9,7,8,9,6,5,4,3,2,4,5,6,6,0,8]
novalista = [] #lista criada sem nd
for i in lista: #percorre itens da lista 
    numencontrado = False #variavel atribuida a false
    for num in novalista: #percorre numeros da nova lista
        if i == num : #compara num da lista com nova lista 
         numencontrado = True#se for igual fica verdadeiro
         break
    if not numencontrado: #se numero nao 
       novalista.append(i) #add na nova lista


    n = len(novalista) #leu a nova lista
    for i in range(n): #percorreu a lista de todos os numeros
       for j  in range(n-1):#percorreu a lista ate o penultimo 
          if novalista[j] > novalista[j + 1]: # se numero j for maior que oque esta na frente 
           troca = novalista[j] #variavel recebe esse numero 
           novalista[j] = novalista[j + 1] # o numero j agr é j +1 
           novalista[j + 1] = troca #e o j+1 agr esta na variavel q estava o j

print("lista sem estar ordenada e com duplicacoes: ")
print(lista)
print("lista ordenada e sem duplicacoes: ")
print(novalista)

#com set
lista01 = [1,2,2,2,3,3,34,45,5,5,5,5,6,6,6,6,6]
zeroduplicacoes = set(lista01)
listaordenada = sorted(zeroduplicacoes)
print("lista sem estar ordenada e com duplicacoes: ")
print(lista01)
print("lista ordenada e sem duplicacoes: ")
print(listaordenada)

