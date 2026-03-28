print('E-COMMERCE X ')

login = input('login: ')

produtos = ['hd', 'memoria ram','teclado','pendrive',] 
valores = [1000.99,2000.0,500.55,150.25]
print('----' * 10)
print(f'''
 1    {produtos[0]} R$ valores [valores[0]]
 2   {produtos[1]} R$ valores [valores[1]]      
 3  {produtos[2]} R$ valores [valores[2]]
 4 {produtos[3]} R$ valores [valores[3]]
    ''')


prod_1 = int(input('produto: '))
prod_2 = int(input('produto: '))
prod_3 = int(input('produto: '))

carrinho = []
valor = []

carrinho.append(produtos[prod_1])
print('no seu carrinho: ', carrinho)
carrinho.append(produtos[prod_2])
print('no seu carrinho: ', carrinho)
carrinho.append(produtos[prod_3])
print('no seu carrinho: ', carrinho)

valor.extend([valores[prod_1], valores[prod_2], valores[prod_3]])

soma  =  sum(valor)

print(carrinho)
print('R$', soma)

