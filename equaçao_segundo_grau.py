def equacao_segundo_grau(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinitas soluções"
            else:
                return "Sem solução"
        else:
            x = -c / b
            return x
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Sem solução real"
        elif delta == 0:
            x = -b / (2 * a)
            return x
        else:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            return x1, x2

# Solicita os coeficientes a, b e c ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula e exibe a solução da equação
solucao = equacao_segundo_grau(a, b, c)
print("A(s) solução(ões) da equação é(são):", solucao)