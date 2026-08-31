lista = []
for c in range(0,6):
    num = int(input(f'Digite  um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1
print(f'Os valores digitado na lista foi {lista}')
