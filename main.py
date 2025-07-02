print('------ Bem-vindo a Loja de Marmitas da Dona Ana Davila Kulek -----------')
print('---------------------------Cardápio-------------------------------------')
print('------------------------------------------------------------------------')
print('-----|  Tamanho |   Bife Acebolado(BA)    |   Filé de Frango(FF)  |-----')
print('-----|    P     |        R$16.00          |         R$15.00       |-----')
print('-----|    M     |        R$18.00          |         R$17.00       |-----')
print('-----|    G     |        R$22.00          |         R$21.00       |-----')
print('------------------------------------------------------------------------')

while( sabor != 'BA' and sabor != 'FF'):
    sabor = input('Entre com o sabor desejado (BA/FF): ')
    print('Sabor inválido. Tente novamente.')
    continue
