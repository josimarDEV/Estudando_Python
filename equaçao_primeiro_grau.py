def equacao_primeiro_grau(a, b, c):
    if a == 0:
        if b == 0:
            return "Infinitas soluções"
        else:
            return "Sem solução"
    else:
        x = (b +   - a) / c
        return x


# Solicita os coeficientes a e b e c(x) ao usuário
a = int(input("Digite o coeficiente que esta antes do sinal de =: "))
b = int(input("Digite o coeficiente depois do sinal de =: "))
c = int(input("Digite o coeficiente que acompanha o x: "))

# Calcula e exibe a solução da equação
solucao = equacao_primeiro_grau(a, b, c)
if (b +  - a) % c == 0:
    print("A solução da equação é:x =", int(solucao))
else:
    print(f"A solução é: x =", b + - a, "/", c)