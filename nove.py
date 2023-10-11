class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def imprimirMenu():
    print("\nMenu:")
    print("1. Criar retângulo")
    print("2. Alterar retângulo")
    print("3. Imprimir centro do retângulo")
    print("0. Sair")


# Função principal
def main():
    retangulo = None

    while True:
        imprimirMenu()
        escolha = input("Escolha uma opção (0-3): ")

        if escolha == "1":
            x = float(input("Digite a coordenada x do ponto inicial: "))
            y = float(input("Digite a coordenada y do ponto inicial: "))
            ponto_inicial = Ponto(x, y)
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            retangulo = Retangulo(ponto_inicial, largura, altura)
            print("Retângulo criado com sucesso!")

        elif escolha == "2":
            if retangulo:
                x = float(input("Digite a nova coordenada x do ponto inicial: "))
                y = float(input("Digite a nova coordenada y do ponto inicial: "))
                ponto_inicial = Ponto(x, y)
                largura = float(input("Digite a nova largura do retângulo: "))
                altura = float(input("Digite a nova altura do retângulo: "))
                retangulo.ponto_inicial = ponto_inicial
                retangulo.largura = largura
                retangulo.altura = altura
                print("Retângulo alterado com sucesso!")
            else:
                print("Crie um retângulo primeiro!")

        elif escolha == "3":
            if retangulo:
                centro = retangulo.encontrarCentro()
                print("Centro do retângulo:")
                centro.imprimir()
            else:
                print("Crie um retângulo primeiro!")

        elif escolha == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
