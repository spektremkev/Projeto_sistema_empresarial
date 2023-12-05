class PessoaJuridica:
    def __init__(self, cnpj, razao_social, endereco, telefone, email,atividade_economica,nome_fantasia):
        
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.atividade_economica = atividade_economica

    def exibir_dados(self):
        print("CNPJ:", self.cnpj)
        print("Razão Social:", self.razao_social)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        print(f"Atividade Econômica: {self.atividade_economica}")
        print(f"Nome Fantasia: {self.nome_fantasia}")

    def realizar_pagamento(self, valor):
        # Lógica para realizar o pagamento da pessoa jurídica
        print("Realizando pagamento de R$", valor, "para", self.razao_social)