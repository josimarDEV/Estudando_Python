import pandas as pd

pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
pd.Series(data=5) # Cria uma Series com o valor a
pd.Series('Howard Ian Peter Jonah Kellie'.split()) # Cria uma Series com uma lista de nomes
listanomes = 'Howard Ian Peter Jonah Kellie'.split()
idade = [25, 18, 12, 35, 45]
dados = listanomes


print(pd.Series(dados))