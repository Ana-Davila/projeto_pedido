#mensagem de boas-vindas
print('------ Bem-vindo a Loja de Marmitas da Dona Ana Davila Kulek -----------')
print('---------------------------Cardápio-------------------------------------')
print('------------------------------------------------------------------------')
print('-----|  Tamanho |   Bife Acebolado(BA)    |   Filé de Frango(FF)  |-----')
print('-----|    P     |        R$16.00          |         R$15.00       |-----')
print('-----|    M     |        R$18.00          |         R$17.00       |-----')
print('-----|    G     |        R$22.00          |         R$21.00       |-----')
print('------------------------------------------------------------------------')
acumulador = 0 #variável que acumula-rá o total dos pedidos

while True: # Loop principal

    while True: # sabor com teste de validação
        sabor = input('Entre com o pedido (BA/FF): ')
        if (sabor== 'BA' or sabor == 'FF'):
            break
        else:
            print('Sabor inválido. Tente novamente. ')
            continue

    while True: # tamanho com teste de validação
        tamanho = input('Entre com o tamanho escolhido (P/M/G): ')
        if(tamanho == 'P' or tamanho == 'M' or tamanho =='G'):
            break
        else:
            print('Tamanho inválido. Tente novamente: ')
            continue

    if( sabor == 'BA'): # Modelo aninhado para combinação de sabor Bife acebolado com possíveis tamanhos.
        if (tamanho == 'P'):
            preco = 16.0
            print(f'Você pediu um Bife Acebolado no tamanho P: R${preco}')
        elif (tamanho == 'M'):
            preco = 18.0
            print(f'Você pediu um Bife Acebolado no tamanho M: R${preco}')
        else:
            preco = 22.0
            print(f'Você pediu um Bife Acebolado no tamanho G: R${preco}')

    elif( sabor == 'FF'): # Modelo aninhado para combinação de sabor do Filé de frango com possíveis tamanhos.
        if(tamanho == 'P'):
            preco = 15.0
            print(f'Você pediu um Filé de Frango no tamanho P: R${preco}')
        elif(tamanho == 'M'):
            preco = 17.0
            print(f'Você pediu um Filé de Frango no tamanho M: R${preco}')
        else:
            preco = 21.0
            print(f'Você pediu um Filé de Frango no tamanho G: R${preco}')


    acumulador += preco #Atualiza o acumulador

    while True:
        continuar= input('Deseja continuar? (S/N): ')
        if (continuar == 'S'):
            break
        else:
            print(f'O valor total a ser pago é: R${acumulador:.2f}')
            exit()