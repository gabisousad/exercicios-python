# VALIDAR CPF
"""A lógica para validar um Cadastro de Pessoa Física (CPF)
 baseia-se em um algoritmo matemático de cálculo de dois dígitos verificadores (os dois últimos números do CPF).
 O processo utiliza pesos decrescentes para validar se a combinação numérica é autêntica.
Antes de aplicar a matemática, a primeira regra é verificar se o CPF possui 11 dígitos e 
se eles não são todos iguais (como 111.111.111-11), 
pois o algoritmo validaria esses números falsos, 
mas a Receita Federal os considera inválidos."""
# str() transforma o valor recebido em uma string (texto)
cpf = str(input("digite seu cpf: "))
# replace() substitui um caractere por outro
# Nesse caso, remove os pontos e o hífen do CPF
cpfnova = cpf.replace("-", "").replace(".", "")
# isdigit() verifica se todos os caracteres são números
if not cpfnova.isdigit():
    print("digite somente numeros") 
    exit()  # exit() encerra a execução do programa
# if verifica se o tamanho do CPF é diferente de 11
# len() conta a quantidade de caracteres de uma string
if len(cpfnova) != 11:
    print("tem q ter 11 digitos")
    exit()
# elif significa "senão, se": verifica outra condição
# set() elimina os caracteres repetidos
# len() conta quantos caracteres diferentes sobraram
# Se sobrar apenas um, significa que todos os números eram iguais
elif len(set(cpfnova)) == 1:
    print("cpf invalido")
    exit()
else:
    # Os índices de uma string começam em 0
    # [0:9] seleciona os caracteres do índice 0 até o 8
    novedigitos = cpfnova[0:9]
    #acumular os resultados das multiplicações
    somatotal = 0
    for i in range(0, 9):
        # Acessa o caractere da posição i
        # int() transforma o caractere de texto em número inteiro
        digito = int(novedigitos[i])
        # Calcula o peso de cada dígito
        # Os pesos serão 10, 9, 8, 7... até 2
        peso = 10 - i
        # Multiplica o dígito pelo peso
        # O resultado é somado ao valor anterior de somatotal
        somatotal = somatotal + (digito * peso)
    print(somatotal)
    resto = somatotal % 11
    if resto < 2:
        digito1 = 0  # Se for, o primeiro dígito será zero
    else:
        digito1 = 11 - resto
    # str() transforma o primeiro dígito em texto
    # O operador + junta as duas strings
    decimodigito = novedigitos + str(digito1)
    # Cria uma variável para acumular a segunda soma
    somatotal2 = 0
    # O laço será executado 10 vezes
    for i in range(0, 10):
        # Calcula os pesos de 11 até 2
        peso = 11 - i
        # Acessa cada caractere e transforma em número inteiro
        digito = int(decimodigito[i])
        # Multiplica o dígito pelo peso e acumula o resultado
        somatotal2 = somatotal2 + (digito * peso)
    # Calcula o resto da segunda divisão por 11
    resul = somatotal2 % 11
    # Verifica se o resto é menor que 2
    if resul < 2:
        digito2 = 0
    else:
        # Se não for menor que 2, calcula o segundo dígito
        digito2 = 11 - resul
    # str() transforma os dois dígitos em texto
    # + junta os dois dígitos verificadores em uma string
    digitosultimos = str(digito1) + str(digito2)
    # [9:] seleciona os caracteres a partir do índice 9 até o final
    # Assim, pegamos os dois últimos números do CPF informado
    dois_ultimos_reais = cpfnova[9:]
    # if compara se os dois dígitos calculados são iguais aos informados
    if digitosultimos == dois_ultimos_reais:
        # f-string permite inserir o valor de uma variável dentro do texto
        print(f"cpf: {cpfnova} é um cpf valido")
    else:
        # Executa quando os dois dígitos são diferentes
        print("nao e um cpf valido")
"""Dicionário dos comandos que você utilizou
Comando	Para que serve
input()	Receber dados do usuário
str()	Converter para texto
int()	Converter para inteiro
if	Verificar uma condição
elif	Verificar outra condição
else	Executar quando as condições anteriores são falsas
for	Repetir instruções
range()	Gerar uma sequência de números
len()	Contar caracteres ou elementos
set()	Eliminar elementos repetidos
replace()	Substituir partes de uma string
isdigit()	Verificar se contém somente números
exit()	Encerrar o programa
print()	Exibir informações
%	Obter o resto da divisão
not	Inverter o resultado lógico
+	Somar números ou juntar strings
==	Comparar se dois valores são iguais
!=	Comparar se dois valores são diferentes"""