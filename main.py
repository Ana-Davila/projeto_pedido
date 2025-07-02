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

while True:
    while True: # sabor com teste de validação
        sabor = input('Entre com o pedido (BA/FF): ').upper()
        if (sabor== 'BA' or sabor == 'FF'):
            break
        else:
            print('Sabor inválido. Tente novamente. ')
            continue
    while True:
        tamanho = ('Entre com o tamanho escolhido (P/M/G): ')
        if(tamanho == 'P' or tamanho == 'M' or tamanho =='G'):
            break
        else:
            print('Tamanho inválido. Tente novamente: ')
            continue
    break

        

