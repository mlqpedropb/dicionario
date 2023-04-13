votos={}

while True:
    candidato= input('digite o nome do candidato(ou "fim" para encerrar): ')
    if candidato == "fim":
        break
    #verifique se os candidatos ja receberam os votos antes
    if candidato in votos:
        votos[candidato]+=1
    else:
        votos[candidato]=1
        
#imprima o resultado da votaçao
print('resultados da votaçao: ')
for candidato , quantidade in votos.items():
    print(candidato, '-', quantidade, 'votos')
    
print(votos)