def eh_primo(n):
    if n <= 1: #se n for negativo ou 0 ja nao tem como ser primo falso
        return False
    for i in range(2,n): #começa por dois pq todo numero é divisivel por 1 
       if n % i == 0: #se resto da divisao de n por i for igual a 0, ele tem divisores 
          return False
   
       else:
          return True
#for primos in range(0,100): #for de 1 ate 100 
 #   if eh_primo(primos):
  #      print(primos)
for n in range(0,100):
   if eh_primo(n):
      print(n)
    
   
