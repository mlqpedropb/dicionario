agenda={}

while True:
    nome=input('digite o nome da pessoa: ')
    if nome =='':
        break
    
    telefone = input('digite o telefone: ')
    
    #add o telefone ao dicionario
    agenda[nome]=telefone
    
#pesquisa um telefone na agenda
nome_pesquisa = input('digite o nome para pesquisar: ')
if nome_pesquisa in agenda:
    print('telefone de', nome_pesquisa,':', agenda[nome_pesquisa])
else:
    print('nome nao encontrado na agenda. ')
    