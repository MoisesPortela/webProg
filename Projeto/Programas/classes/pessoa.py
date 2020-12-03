from BDDS.controllers.pessoaController import pessoaController



class Pessoa():

    def __init__(self, cpf, nome, peso, idade, sexo, endereco, tipo, rh):
        self.cpf = cpf
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        self.tipo = tipo
        self.rh = rh

    def getPessoaByName(nome):
        pessoaController().getPessoaByName(nome)
    
    def incluirPessoa(pessoa):
        pessoaController().incluirPessoa(pessoa)