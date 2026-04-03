carrinho = str(input('Digite o nome do produto: ')).lower()
qntd = int(input('Digite a quantidade: '))
tabela = {'alface': 2.50,
           'banana': 1.50,
            'laranja': 3.00,
           'tomate': 4.00}
x =  tabela [carrinho] * qntd
while True:
    resposta = (input("você quer adicionar algo mais? "))
    if resposta == 'sim':
        carrinhoadd = str(input('Digite o nome do produto: '))
        qntdadd = int(input("adicione o valor deste item:"))
        x += tabela [carrinhoadd] * qntdadd
        print("o valor total da compra é: {}".format(x))
    elif resposta == 'não':
        print("o valor total da compra é: {}".format(x))
        break