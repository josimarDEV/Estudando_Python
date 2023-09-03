import matplotlib.pyplot as plt

# Defina um valor para S e crie uma lista de dados (exemplo com números aleatórios)
S = 10
dados = range(S)

# Crie a figura com duas subtramas
fig, ax = plt.subplots(1, 2)

# Plote os dados na primeira subtrama
ax[0].plot(dados)
ax[0].set_title('Subtrama 1')  # Adicione um título à primeira subtrama

# Plote os dados na segunda subtrama
ax[1].plot(dados)
ax[1].set_title('Subtrama 2')  # Adicione um título à segunda subtrama

# Mostre os gráficos para o usuário
plt.show()
