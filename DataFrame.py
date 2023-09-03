import pandas as pd

pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

pd.DataFrame('Howard Ian Peter Jonah Kellie'.split(), columns=['nome'])
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpf = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = ('risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org '
                'non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk').split()
lista_idades = [32, 22, 25, 29, 38]
dados = list(zip(lista_nomes, lista_cpf, lista_idades,
                 lista_emails))  # cria uma lista de tuplas # Cria um DataFrame a partir de uma lista de tuplas
pd.DataFrame(dados, columns=['nome', 'cpf', 'idade', 'email'])

print(pd.DataFrame(dados, columns=['nome', 'cpf', 'idade', 'email']))

