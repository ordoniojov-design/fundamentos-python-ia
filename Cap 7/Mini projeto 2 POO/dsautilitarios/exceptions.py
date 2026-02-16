# dsautilitarios/exceptions.py

class SaldoInsuficienteError(Exception):
    """Exceção levantada quando não há saldo suficiente para uma operação"""
    pass


class ContaInexistenteError(Exception):
    """Exceção levantada quando uma conta não é encontrada"""
    pass