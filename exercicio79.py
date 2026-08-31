lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado, não vou adicionar!!!')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
