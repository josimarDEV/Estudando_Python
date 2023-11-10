class conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

    @property
    def saldo(self):
        return self._saldo


conta = conta("0001", 100)
conta.depositar(100)
print(conta.saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
