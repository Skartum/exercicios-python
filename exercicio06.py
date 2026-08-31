s = 0
cont = 0
for c in range (1,5):
        n = int(input(f'Digite o {c}º número: '))
        s += n
        cont+=1
        m = s/cont
print(f'A soma é {s}, a media é {m}') 