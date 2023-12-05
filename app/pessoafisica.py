class PessoaJuridica:
    def __init__(self, cpf, nome, endereco, telefone, email):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        print("CPF:", self.cpf)
        print("Razão Social:", self.razao_social)
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)

    def realizar_pagamento(self, valor):
        # Lógica para realizar o pagamento da pessoa jurídica
        print("Realizando pagamento de R$", valor, "para", self.razao_social)