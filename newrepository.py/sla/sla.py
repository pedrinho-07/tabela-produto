while True:
    resposta = str(input('Vamos começar os desafios? ' "\n Sim ou Não? ")).lower().strip()

    if resposta  in ["não" , 'nao']:
       print("ENCERRANDO...") 
       exit()
    elif resposta == "sim":
        print ('Vamos lá' "\n # desafio 1")
        break
    else:
     print("apenas digite sim ou não. ")

#desafio 1
from random import randint
from time import sleep
computer = randint (0, 5)
print ("-=-" * 20)
print ("vou pensar em um número entre 0 e 5. Tente adivinhar...")
print ("-=-" * 20)
while True:
    try:
        jogador = int(input("Em que número eu pensei? "))
        print ("PROCESSANDO...")
    except ValueError:
        print("Erro: digite apenas números.")
        continue
    sleep (2)
    if jogador == computer:
        print ('PARABÉNS! Você é melhor do que eu imaginei.')
        break
    elif jogador >5 or jogador <0 :
        print ("Escolha de 0 a 5...")
    else: 
        print('Você perdeu!')

while True:
    print("-=-"*20)

    print('Vamos para o segundo desafio? ')
    
    resposta = str(input('simbora ou não? ')).lower().strip()

    if resposta in ['nao' , 'não' , 'n']:
     print ('Encerrando... Até mais.')
     exit()

    elif resposta in ["sim",'simbora','s']:
     print ('Melhor escolha!' "\n #2 desafio!")
     print("-=-"*20)
     break
    else: 
      print ("digite apenas sim ou não")

#desafio 2
velocidade = float(input("qual é a velocidade do carro? "))
if velocidade > 80:
    print ("multado! você excedeu o limite permitido.")
    multa = (velocidade-80) * 7 
    print ("você deve pagar uma multa de R${:.2f}!".format(multa))
print ('tenha um bom dia! Dirija com segurança')
print("-=-"*20)

while True:
    print('Vamos para o terceiro desafio? ')
    resposta = str(input('vamos ou não? '))
    if resposta in ['nao' , 'não' , 'n']:
     print ('Encerrando... Até mais.')
     exit()
    elif resposta in ["sim",'vamos','s']:
     print ('Imparável' "\n #3 desafio!")
     print("-=-"*20)
     break
    else:
        print("digite apenas sim ou não")

#desafio 3
numero = int(input("me diga um número qualquer: "))
resultado = numero % 2
if resultado == 0:
    print ("O número {} é par".format(numero))
else:
    print("O número {}é ímpar".format(numero))

    print("-=-"*20)

while True:
    print('Vamos para o quarto desafio? ')
    resposta = str(input("let's go ou não? "))
    if resposta in ['nao' , 'não' , 'n']:
     print ('Encerrando... Até mais.')
     exit()
    elif resposta in ["sim",'lets','s']:
     print ('O melhor!!!' "\n #4 desafio!")
     print("-=-"*20)
     break
    else:
       print("digite apenas sim ou não.")

#desafio 4
distancia = float(input("qual é a distância da sua viagem? "))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print ('E o preço da sua passagem será de R${:.2f}'.format(preço))
print("-=-"*20)
print("Acabou..." "\nEsse foi meu primeiro loop com desafios, obrigado!")