students = {
    'joao':{
        'idade': 18,
        'cidade': 'sao paulo',
        'notas':[7.5, 8.0, 9.0]
    },
    'maria': {
        'idade': 20,
        'cidade': 'rio de janeiro',
        'notas':[6.5, 7.0, 8.5]
    },
    'pedro':{
        'idade': 19,
        'cidade': 'belo horizonte',
        'notas':[8.0, 8.5, 9.5]
    },
}
# imprima a idade de joao
print(' a idade de joao é: '+ str(students['joao']['idade']))
# add uma  nova nota para maria
students['maria']['notas'].append(9.0)
#imprimir tds as informaçoes dos alunos
for students, info in students.items():
    print(students+ ':')
    print('idade: '+ str(info['idade']))
    print('cidade: '+ info['cidade'])
    print('notas: '+ str(info['idade']))
    print('media: '+ str(sum(info['notas'])/ len(info['notas'])))