### Projeto CountDown
### Contar de 10 até 0

### Variavel que carrega o número de contagem
contagem = 11


### Loop for que vai de até 11 para incluir o número 0 no final da contagem
for i in range(11):

    ### A cada vez que rodas o FOR, irá subtrair um número da variavel contagem
    contagem = contagem - 1

    ### E irá printar o atual número guardado na variavel
    print(contagem)

### Mensagem para ser exibida quando for concluído o loop
print('Contagem regressiva concluída!!')
