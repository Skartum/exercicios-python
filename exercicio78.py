lista = []
for c in range(0,5):
    num = int(input(f'Digite um valor na posição {c}: '))
    lista.append(num)
min = min(lista)
max = max(lista)
posicoes = [f'{i}º' for i, v in enumerate(lista) if v == max]
posicoesm = [f'{i}º' for i, v in enumerate(lista) if v == min]
print(f'os numeros armazenado na lista foi, {lista}')
print(f'O numero maior foi {max} nas posições {", ".join(posicoes)}')
print(f'O numero menor foi {min} nas posições {", ".join(posicoesm)}') 