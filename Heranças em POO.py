# # Herança Simples
#
# class Veiculo:
#     def __init__(self, cor, placa, numero_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.numero_rodas = numero_rodas
#
#     def ligar_motor(self):
#         print("Ligando Motor...")
#
# def __str__(self): return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,
# valor in self.__dict__.items()])}"
#
#
# class Motocicleta(Veiculo):
#     pass
#
#
# class Carro(Veiculo):
#     pass
#
#
# class Caminhao(Veiculo):
#     def __init__(self, cor, placa, numero_rodas, carregado):
#         super().__init__(cor, placa, numero_rodas)
#         self.carregado = carregado
#
#     def esta_carregado(self):
#         print(f"{'SIM' if self.carregado else 'Não'} estou carregado")
#
#
# Bis = Motocicleta('Vermelha', 'ABC1234', 2)
#
# Fiat_Uno = Carro('Prata', 'HTG035', 4)
#
# FH_540 = Caminhao('Preto', 'VLV540', 6, False)
#
#
# print(FH_540)
# print(Bis)
# print(Fiat_Uno)

# Herança Multipla


# class animal:
#     def __init__(self, numero_patas):
#         self.numero_patas = numero_patas
#
# def __str__(self): return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,
# valor in self.__dict__.items()])}"
#
#
# class mamifero(animal):
#     def __init__(self, nome, cor_do_pelo, tem_rabo, **kwargs):
#         self.nome = nome
#         self.cor_do_pelo = cor_do_pelo
#         self.tem_rabo = tem_rabo
#         super().__init__(**kwargs)
#         if tem_rabo:
#             self.tem_rabo = 'Tem rabo'
#         else:
#             self.tem_rabo = 'Não tem rabo'
#
#
# class ave(animal):
#     def __init__(self, cor_bico, **kwargs):
#         self.cor_bico = cor_bico
#         super().__init__(**kwargs)
#
#
# class cachorro(mamifero):
#     pass
#
#
# class felino(mamifero):
#     pass
#
#
# class leao(mamifero):
#     pass
#
#
# class ornitorrinco(mamifero, ave):
#     pass
#
#
# perry = ornitorrinco('Perry', 'Verde Claro', True, numero_patas=4, cor_bico='Laranja')
# print(perry)
# gato = felino('Aladdin', 'Mestiço', True, numero_patas=4)
# print(gato)
