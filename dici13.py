products= {
    'banana':2.50,
    'maça': 3.00,
    'laranja': 2.75,
    'abacaxi': 4.50,
    'manga':3.50
}

#imprimir im novo produto
print(' o preço de uma maça é: R$'+ str(products['maça']))

# add um novo produto
products['melancia']=6.00

#imprimir todos os produtos e seus preços
for products, price in products.items():
    print(products + '; R$'+ str(price))