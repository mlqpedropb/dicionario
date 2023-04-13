cadastro={}
while True:
    nome=input('digite o nome completo: ')
    if nome =='':
        break
            
    idade= int(input('digite sua idade; '))
    cidade= input(' digite a cidade: ')
    
    #add os dados ao dicionario
    
    cadastro[nome]={'idade':idade, 'cidade':cidade}
    
#imprima o cadastro completo
print('cadastro: ')
print(cadastro)
for nome, dados in cadastro.items():
    print('- nome: ', nome)
    print(' idade: ', dados['idade'])
    print('cidade: ', dados['cidade'])
