# Desenhe um retângulo de algum caracter digitado pelo usuário, sendo a altura e a largura também determinada pelo usuário.
# o o o o o o o

# o o o o o o o

# o o o o o o o

# Este é um exemplo de retângulo 3 x 7 costruído com a letra o

caracter = input('Digite caracter: ')
altura = int(input('Digite altura: '))
largura = int(input('Digite largura: '))

if altura == largura:
    print('Falha')
else:
    for i in range(altura):
        print(largura*caracter)