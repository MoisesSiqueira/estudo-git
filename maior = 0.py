lista = []
maior = 0
menor = 0
for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para entras na lista {contador}: ')))
    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]
print('=-'  * 30)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for numero, caixa in enumerate(lista):
    if caixa == maior:
        print(f'{numero}...', end='')
print()
print(f' Menor valor digitado foi { menor } na posição ', end='')
for numero, caixa in enumerate(lista):
    if caixa == menor:
        print(f'{ numero } ...', end='')
        print()
    