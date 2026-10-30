#Dia 15: Desenhar com asteriscos um triângulo e depois um losango, com altura lida do usuário

altura = int(input("digite um numero de altura: "))
for linha in range(1, altura + 1): #percorre a linha começa de 1 e vai somando a altura
    espaços = " " * (altura - linha) #espaços * a altura - menos a linhas é qtd de espaços
    asterisco = "*" * (2 * linha -1) #asteriscos numeros impares
    print(espaços + asterisco) 
for linha in range(altura - 1,0, -1):# percorre nova linha com altura -1, com intervalo de 0 ate -1 
    espaços = " " * (altura - linha)
    asterisco = "*" * (2 * linha - 1)
    print(espaços + asterisco)
    
