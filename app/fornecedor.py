
import pessoasjuridica


class Fornecedor:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.produtos = produtos

    def registrar_produto(self, nome, preco):
        self.produtos.append({"nome": nome, "preco": preco})

        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print("Produtos:")

      