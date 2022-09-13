valor_monetario = input('Digite um valor: ')

while valor_monetario.isalpha():
    valor_monetario = input('Valor incorreto, digite novamente ')
else:
    valor_monetario.isnumeric( ) == True
    valor_monetario = float(valor_monetario)
    valor = float(valor_monetario - (15/100*valor_monetario))
    print(f'O novo valor é {valor}')