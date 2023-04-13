dicionario={'gato':'chat','cachorro':'chien','cavalo':'chavel'}
palavras=['gato','lion','cavalo']

for palavra in palavras:
    if palavra in dicionario:
        print(palavra,"->", dicionario[palavra])
    else:
        print(palavra,'nao esta no dicionario')