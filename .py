nome = input ('Qual seu nome?')
print ('Olá, ', nome, '.')
idade=int(input ('Qual sua idade?'))

if idade <16:
 votar = "Não pode votar."
elif idade <18 and idade >=16:
 votar = "Voto facultativo."
elif idade >=18 and idade <70:
  votar = "Voto obrigatório."
elif idade >=70:
  votar = "Voto facultativo."

print (votar)
