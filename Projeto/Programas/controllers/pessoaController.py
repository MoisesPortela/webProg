from BDDS.db.db import SQL



class pessoaController():

    def __init__(self):
        self.mysql = SQL("root", "", "test")

    def getPessoaByName(self, nome):
        comando = "SELECT idt_pessoa FROM tb_pessoa WHERE nome = %s;"
        cs = self.mysql.consultar(comando, [nome])
        pessoa = cs.fetchone()
        return pessoa
    
    def incluirPessoa(self, pessoa):
        comando_ins_pessoa = "INSERT INTO tb_pessoa (cpf, nome, peso, idade, sexo, endereco, tipo, rh) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        self.mysql.executar(comando_ins_pessoa, [pessoa.cpf, pessoa.nome, pessoa.peso, pessoa.idade, 
                                                pessoa.sexo, pessoa.endereco, pessoa.tipo, pessoa.rh])