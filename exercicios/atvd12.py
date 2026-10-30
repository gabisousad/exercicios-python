#Dia 12: Inverter uma lista de duas formas (laço e fatiamento)
lista = [1,2,3,4,5,6,7,8,9,10] #lista
novalista = lista[::-1] #para inverter no fatiamento usamos essa maestria lista[inicio:fim:intervalo] fim é exclusivo
print(novalista)
#laço
nova_lista = []
for i in range(9,-1,-1):#o número do meio (o fim) NUNCA entra na contagem, o laço para um passo ANTES dele.
    nova_lista += [lista[i]] #Transforma esse número em uma lista para poder juntar com a nova_lista usando +=.
print(nova_lista)
# nova_lista += [lista[i]] funciona assim:
# 1. lista[i] busca o número na posição i (ex: 10).
# 2. [lista[i]] transforma esse número em lista ([10]).
# 3. += junta essa nova lista com a nova_lista (lista + lista).
# Sem os [], o Python tenta somar lista com número inteiro e dá erro.