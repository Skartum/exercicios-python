print('='*15)
print('TABUADA'.center(15))
print('='*15)
n = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')