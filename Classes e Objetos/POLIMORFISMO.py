class passaro:
    def voar(self):
        print("Voando...")


class Pardal(passaro):
    def voar(self):
        super().voar()


class Avestruz(passaro):
    def voar(self):
        print("Avestruz não pode voar")


# FIXME: "exemplo ruim do uso de herança para ganhar o metodo voar"
class aviao(passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(aviao())
