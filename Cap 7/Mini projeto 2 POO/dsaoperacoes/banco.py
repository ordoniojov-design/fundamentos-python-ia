# dsaoperacoes/banco.py
from dsautilitarios.exceptions import ContaInexistenteError, SaldoInsuficienteError
from datetime import datetime

class Cliente:
    """Classe que representa um cliente do banco"""
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []  # Lista de contas do cliente
    
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"


class Conta:
    """Classe base para contas bancárias"""
    
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self._transacoes = []  # Histórico de transações
        cliente.contas.append(self)  # Vincula a conta ao cliente
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        """Método para depositar valor na conta"""
        if valor <= 0:
            print("Erro: Valor de depósito deve ser positivo.")
            return False
        
        self._saldo += valor
        self._transacoes.append({
            'data': datetime.now(),
            'tipo': 'DEPÓSITO',
            'valor': valor,
            'saldo_apos': self._saldo
        })
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        return True
    
    def sacar(self, valor):
        """Método base para saque (será sobrescrito)"""
        raise NotImplementedError("Método deve ser implementado pela subclasse")
    
    def extrato(self):
        """Exibe o extrato da conta"""
        print(f"\n=== EXTRATO DA CONTA {self._numero} ===")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("\nTransações:")
        
        if not self._transacoes:
            print("Nenhuma transação realizada.")
        else:
            for t in self._transacoes:
                data = t['data'].strftime("%d/%m/%Y %H:%M")
                print(f"{data} | {t['tipo']} | R${t['valor']:.2f} | Saldo: R${t['saldo_apos']:.2f}")
        print("=" * 40)


class ContaCorrente(Conta):
    """Conta Corrente que permite saque com limite"""
    
    def __init__(self, numero, cliente, limite=500.0):
        super().__init__(numero, cliente)
        self._limite = limite
    
    def sacar(self, valor):
        """Saque com limite da conta corrente"""
        if valor <= 0:
            print("Erro: Valor de saque deve ser positivo.")
            return False
        
        # Verifica se há saldo + limite suficiente
        if valor > (self._saldo + self._limite):
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Saldo: R${self._saldo:.2f}, Limite: R${self._limite:.2f}"
            )
        
        self._saldo -= valor
        self._transacoes.append({
            'data': datetime.now(),
            'tipo': 'SAQUE',
            'valor': valor,
            'saldo_apos': self._saldo
        })
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
        return True


class ContaPoupanca(Conta):
    """Conta Poupança que não permite saldo negativo"""
    
    def __init__(self, numero, cliente, rendimento=0.5):
        super().__init__(numero, cliente)
        self._rendimento = rendimento  # Percentual de rendimento mensal
    
    def sacar(self, valor):
        """Saque sem possibilidade de saldo negativo"""
        if valor <= 0:
            print("Erro: Valor de saque deve ser positivo.")
            return False
        
        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Saldo disponível: R${self._saldo:.2f}"
            )
        
        self._saldo -= valor
        self._transacoes.append({
            'data': datetime.now(),
            'tipo': 'SAQUE',
            'valor': valor,
            'saldo_apos': self._saldo
        })
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
        return True
    
    def aplicar_rendimento(self):
        """Aplica rendimento à poupança"""
        if self._saldo > 0:
            rend = self._saldo * (self._rendimento / 100)
            self._saldo += rend
            self._transacoes.append({
                'data': datetime.now(),
                'tipo': 'RENDIMENTO',
                'valor': rend,
                'saldo_apos': self._saldo
            })
            print(f"Rendimento de R${rend:.2f} aplicado!")


class Banco:
    """Classe principal que gerencia clientes e contas"""
    
    def __init__(self, nome):
        self.nome = nome
        self._clientes = {}  # CPF -> Cliente
        self._contas = {}    # Número -> Conta
        self._proximo_numero_conta = 1000  # Número inicial para contas
    
    def adicionar_cliente(self, nome, cpf):
        """Adiciona um novo cliente ao banco"""
        if cpf in self._clientes:
            print(f"Erro: CPF {cpf} já cadastrado.")
            return False
        
        cliente = Cliente(nome, cpf)
        self._clientes[cpf] = cliente
        print(f"Cliente {nome} cadastrado com sucesso!")
        return True
    
    def criar_conta(self, cliente, tipo_conta):
        """Cria uma nova conta para um cliente"""
        if cliente.cpf not in self._clientes:
            print("Erro: Cliente não encontrado no sistema.")
            return False
        
        numero = self._proximo_numero_conta
        self._proximo_numero_conta += 1
        
        if tipo_conta.lower() == 'corrente':
            conta = ContaCorrente(numero, cliente)
        elif tipo_conta.lower() == 'poupanca':
            conta = ContaPoupanca(numero, cliente)
        else:
            print("Erro: Tipo de conta inválido. Use 'corrente' ou 'poupanca'")
            return False
        
        self._contas[numero] = conta
        print(f"Conta {tipo_conta} número {numero} criada para {cliente.nome}!")
        return conta
    
    def buscar_conta(self, numero):
        """Busca uma conta pelo número"""
        conta = self._contas.get(numero)
        if not conta:
            raise ContaInexistenteError(f"Conta número {numero} não encontrada.")
        return conta
    
    def listar_clientes(self):
        """Lista todos os clientes do banco"""
        print(f"\n=== CLIENTES DO {self.nome} ===")
        if not self._clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cpf, cliente in self._clientes.items():
                print(f"CPF: {cpf} | {cliente.nome} | Contas: {len(cliente.contas)}")
        print("=" * 30)
    
    def listar_contas(self):
        """Lista todas as contas do banco"""
        print(f"\n=== CONTAS DO {self.nome} ===")
        if not self._contas:
            print("Nenhuma conta cadastrada.")
        else:
            for num, conta in self._contas.items():
                tipo = "Corrente" if isinstance(conta, ContaCorrente) else "Poupança"
                print(f"Conta {num} | {tipo} | Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
        print("=" * 30)