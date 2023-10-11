class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor



class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b
    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)




class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha



class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False  #Depósito inválido

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False  #Valor inválido de saque



class Televisor:
    def __init__(self):
        self.canal = 1  #Canal inicial
        self.volume = 10  #Nível de volume inicial

    def alterarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Canal inválido")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo")



class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        return self.fome * 0.5 + self.saude * 0.5


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}!")

    def verBucho(self):
        if self.bucho:
            print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir.")


# Tentando fazer um macaco comer o outro
macaco1.comer(macaco2.nome)
macaco1.verBucho()



class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  #km/l
        self.combustivel = 0  #litros

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if consumo_total <= self.combustivel:
            self.combustivel -= consumo_total
            print(f"Carro percorreu {distancia} km.")
        else:
            print("Combustível insuficiente. Abasteça o carro.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade
        print(f"Tanque abastecido com {quantidade} litros.")



class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  #Convertendo a taxa para decimal

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxa_juros

    def obterSaldo(self):
        return self.saldo


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento
        print(f"Salário aumentado em {porcentualDeAumento}%. Novo salário: {self.salario}")



import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def mostrarStatus(self):
        print(f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}")

    def __str__(self):
        return f"{self.nome}: Fome={self.fome}, Tédio={self.tedio}"

class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionarBichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentarTodos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade_comida)

    def brincarTodos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo_brincadeira)

    def ouvirTodos(self):
        for bichinho in self.bichinhos:
            bichinho.mostrarStatus()



