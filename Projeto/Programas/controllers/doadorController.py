from BDDS.db.db import SQL
from BDDS.controllers.pessoaController import pessoaController




class doadorController():

    def __init__(self):
        self.mysql = SQL("root", "", "test")

    def alterarDoador(self, doador, idt):
        codPessoa = self.getIdtPessoaByIdtDoador(idt)
        print(codPessoa[0])
        comando = "UPDATE tb_pessoa SET cpf=%s, nome=%s, peso=%s, idade=%s, sexo=%s, endereco=%s " \
                  "WHERE idt_pessoa=%s;"
        print(doador.nome)
        try:
            self.mysql.executar(comando,
                                [doador.cpf,doador.nome, doador.peso, doador.idade,
                                doador.sexo, doador.endereco, codPessoa[0]])

        except Exception as e:
            print(e)


    def getDoadorByIdt(self, idt):
        comando = "SELECT idt_doador, cpf, nome, peso, idade, sexo, endereco, tipo, rh, qtd_doacoes FROM tb_doador " \
                  "INNER JOIN tb_pessoa ON cod_pessoa = idt_pessoa WHERE idt_doador = %s;"
        cs = self.mysql.consultar(comando, [idt])
        doador = cs.fetchone()
        return doador

    def excluirDoador(self, idt):
        comando = "DELETE FROM tb_doador WHERE idt_doador=%s;"
        try:
            self.mysql.executar(comando, [idt])
        except Exception as e:
            print(e)

    def incluirDoador(self, doador):
        pessoaController().incluirPessoa(doador)
        codPessoa = pessoaController().getPessoaByName(doador.nome)
        comando = "INSERT INTO tb_doador (cod_pessoa, qtd_doacoes, total_litros) VALUES (%s, %s, %s);"
        try:
            print("EU ESTOU AQUI")
            print(codPessoa)
            self.mysql.executar(comando, [codPessoa[0], 0, 0])
        except Exception as e:
            print(e)
        return self

    def getAllDoadores(self):
        comando = "SELECT idt_doador, cpf, nome, peso, idade, sexo, endereco, tipo, rh, qtd_doacoes, total_litros FROM tb_doador " \
                  "INNER JOIN tb_pessoa ON cod_pessoa = idt_pessoa;"
        cs = self.mysql.consultar(comando, ())
        doadores = cs.fetchall()
        print(doadores)
        return doadores    

    def getIdtPessoaByIdtDoador(self,idt):
        comando= "SELECT cod_pessoa FROM tb_doador WHERE idt_doador = %s;"
        cs = self.mysql.consultar(comando,[idt])
        pessoa = cs.fetchone()
        return pessoa