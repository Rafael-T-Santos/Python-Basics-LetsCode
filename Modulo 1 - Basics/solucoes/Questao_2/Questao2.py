numero = float(input('Digite um número: '))

intervalos = ['[0,25]','(25,50]','(50,75]','(75,100]']

if numero >= 0 and numero <= 25:
    print(f'Entrada: {numero} | Saída: {intervalos[0]}')
elif numero > 25 and numero <= 50:
    print(f'Entrada: {numero} | Saída: {intervalos[1]}')
elif numero > 50 and numero <= 75:
    print(f'Entrada: {numero} | Saída: {intervalos[2]}')
elif numero > 75 and numero <= 100:
    print(f'Entrada: {numero} | Saída: {intervalos[3]}')
else:
    print('Fora do intervalo.')