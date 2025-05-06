mt = []
df = []
print('CRIADOR DE CICLO DE ESTUDO')
while True:
  x = input('Quais matérias deseja adicionar (Digite "Continuar" quando finalizar):')
  if x.lower().strip() == 'continuar':
    break
  else:
    mt.append(x)
hd = int(input('Diga uma quantidade de horas ideal para estudar por dia:'))
for i in mt:
  x = int(input(f'Qual é sua dificuldade em {i}?(de 1 a 5):'))
  df.append(x)
print('\nSeu Ciclo de Estudo será:')
for j in range(len(mt)):
  ar = round((df[j]*(hd*7/sum(df))))
  if ar < 2:
    print(f'- {mt[j]}: 2 horas')
  else:
    print(f'- {mt[j]}: {ar} horas')