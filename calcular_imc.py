def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc


peso = float(input("Digite seu peso em quilos:"))
altura = float(input("Digite sua altura em metros:"))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("\033[34mAbaixo do peso!")

elif imc == 18.5 or imc <= 24.9:
    print("\033[32mPeso Normal")

elif imc == 25 or imc <= 29.9:
    print("\033[33mAcima do peso!")

elif imc == 30 or imc <= 34.9:
    print("\033[31mOBESIDADE 1")

elif imc == 35 or imc <= 39.9:
    print("\033[31mOBESIDADE 2")

else:
    print("\033[31mOBESIDADE 3")
