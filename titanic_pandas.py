import pandas as pd
import seaborn as sns

# Lê o arquivo CSV 'titanic.csv' e armazena os dados em um DataFrame chamado df_titanic
df_titanic = pd.read_csv('titanic.csv')

# Remove linhas duplicadas do DataFrame, mantendo a última ocorrência
df_titanic.drop_duplicates(keep='last', inplace=True)

# Converte os valores da coluna 'Sex' para maiúsculas
df_titanic['Sex'] = df_titanic['Sex'].str.upper()

# Converte os valores da coluna 'Age' para o tipo de dados inteiro
df_titanic['Age'] = df_titanic['Age'].astype(int)

# Adiciona uma nova coluna 'n_relatives' que é a soma das colunas 'Siblings/Spouses Aboard' e 'Siblings/Spouses Aboard'
df_titanic['n_relatives'] = df_titanic['Siblings/Spouses Aboard'] + df_titanic["Siblings/Spouses Aboard"]

# Define intervalos de idade e rótulos para categorizar as idades
idade_min = df_titanic['Age'].min()
idade_max = df_titanic['Age'].max()
intervalos = [idade_min-1, 10, 18, 65, idade_max]
rotulos = ['Criança', 'Adolescente', 'Adulto', 'Idoso']

# Cria uma nova coluna 'faixa_idade' que categoriza as idades com base nos intervalos e rótulos definidos
df_titanic['faixa_idade'] = pd.cut(x=df_titanic['Age'], bins=intervalos, labels=rotulos)

# Exibe informações sobre o DataFrame, incluindo estatísticas descritivas da coluna 'faixa_idade'
print(df_titanic.info())

# Remove as colunas 'Siblings/Spouses Aboard' e 'Parents/Children Aboard' do DataFrame
df_titanic.drop(columns=['Siblings/Spouses Aboard', 'Parents/Children Aboard'], inplace=True)

# Encontra os valores únicos na coluna 'Pclass' (classe dos passageiros)
classes_distintas = df_titanic['Pclass'].unique()
print(classes_distintas)

# Filtra os passageiros que sobreviveram e os que não sobreviveram
filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_nao_sobreviventes = df_titanic['Survived'] == 0

# Conta a quantidade de sobreviventes e não sobreviventes
qtde_sobreviventes = df_titanic.loc[filtro_sobreviventes].shape[0]
qtde_nao_sobreviventes = df_titanic.loc[filtro_nao_sobreviventes].shape[0]

# Exibe a quantidade de sobreviventes e não sobreviventes
print('\nQuantidade de sobreviventes = ', qtde_sobreviventes)
print('Quantidade de não sobreviventes = ', qtde_nao_sobreviventes)

# Filtra os passageiros idosos
filtro_idoso = df_titanic['faixa_idade'] == 'Idoso'

# Conta a quantidade de passageiros idosos a bordo e quantos sobreviveram
qtde_idosos = df_titanic.loc[filtro_idoso].shape[0]
qtde_idosos_sobreviventes = df_titanic.loc[filtro_sobreviventes & filtro_idoso].shape[0]

# Exibe a quantidade de idosos a bordo e quantos sobreviveram
print("\nQuantidade de idosos a bordo = ", qtde_idosos)
print("Quantidade de idosos que sobreviveram = ", qtde_idosos_sobreviventes)

# Calcula a quantidade de homens e mulheres sobreviventes
filtro_homem = df_titanic['Sex'] == 'MALE'
filtro_mulher = df_titanic['Sex'] != 'MALE'

qtde_homens_sobreviventes = df_titanic.loc[filtro_sobreviventes & filtro_homem].shape[0]
qtde_mulheres_sobreviventes = df_titanic.loc[filtro_sobreviventes & filtro_mulher].shape[0]

# Calcula a taxa de sobrevivência entre homens e mulheres
qtde_passageiros_sobreviventes = df_titanic[filtro_sobreviventes].shape[0]
taxa_homens = (qtde_homens_sobreviventes / qtde_passageiros_sobreviventes) * 100
taxa_mulheres = (qtde_mulheres_sobreviventes / qtde_passageiros_sobreviventes) * 100

# Exibe as taxas de sobrevivência entre homens e mulheres
print("\nTaxa de sobrevivência entre homens = {:.2f}%".format(taxa_homens))
print("Taxa de sobrevivência entre mulheres = {:.2f}%".format(taxa_mulheres))

# Calcula o valor médio da passagem para sobreviventes e não sobreviventes
valor_medio_sobreviventes = df_titanic.loc[filtro_sobreviventes, 'Fare'].mean()
valor_medio_nao_sobreviventes = df_titanic.loc[filtro_nao_sobreviventes, 'Fare'].mean()

# Exibe o valor médio das passagens para sobreviventes e não sobreviventes
print(f'\nValor médio das passagens dos sobreviventes = {valor_medio_sobreviventes:.2f}')
print(f'Valor médio das passagens dos não sobreviventes = {valor_medio_nao_sobreviventes:.2f}')

df = sns.load_dataset('titanic')
sns.countplot(x=df['class'])
print(df)