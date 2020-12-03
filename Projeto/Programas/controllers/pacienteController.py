from BDDS.db.db import SQL
from BDDS.controllers.pessoaController import pessoaController




class pacienteController():

    def __init__(self):
        self.mysql = SQL("root", "", "test")

    def getAllPacientes(self):
        comando = "SELECT idt_paciente, cpf, nome, peso, idade, sexo, endereco, tipo, rh, sts_necessidade FROM tb_paciente " \
                  "INNER JOIN tb_pessoa ON cod_pessoa = idt_pessoa;"
        cs = self.mysql.consultar(comando, ())
        paciente = cs.fetchall()
        print(paciente)
        return paciente

    def getPacienteByIdt(self, idt):
        comando =  "SELECT idt_paciente, cpf, nome, peso, idade, sexo, endereco, tipo, rh, sts_necessidade FROM tb_paciente " \
                  "INNER JOIN tb_pessoa ON cod_pessoa = idt_pessoa WHERE idt_paciente = %s;"
        cs = self.mysql.consultar(comando, [idt])
        paciente = cs.fetchone()
        print(paciente)
        return paciente

    def excluirPaciente(self, idt):
        comando = "DELETE FROM tb_paciente WHERE idt_paciente=%s;"
        try:
            self.mysql.executar(comando, [idt])
        except Exception as e:
            print(e)

    def incluirPaciente(self,paciente):
        pessoaController().incluirPessoa(paciente)
        codPessoa = pessoaController().getPessoaByName(paciente.nome)
        comando = "INSERT INTO tb_paciente (cod_pessoa, sts_necessidade) VALUES (%s, %s);"
        try:
            print(codPessoa)
            self.mysql.executar(comando, [codPessoa[0], 0])
        except Exception as e:
            print(e)
        return self

    def alterarPaciente(self, paciente, idt):
        codPessoa = self.getIdtPessoaByIdtPaciente(idt)
        comando_updt_pessoa = "UPDATE tb_pessoa SET cpf=%s, nome=%s, peso=%s, idade=%s, sexo=%s, endereco=%s WHERE idt_pessoa=%s;"
        comando_updt_necessidade = "UPDATE tb_paciente SET sts_necessidade = %s WHERE idt_paciente = %s;"
        try:
            self.mysql.executar(comando_updt_pessoa,
                                [paciente.cpf,paciente.nome, paciente.peso, paciente.idade,
                                paciente.sexo, paciente.endereco, codPessoa[0]])
            self.mysql.executar(comando_updt_necessidade,
                                [paciente.stsNecessidade, idt])
        except Exception as e:
            print(e)
            
    def getIdtPessoaByIdtPaciente(self,idt):
        comando= "SELECT cod_pessoa FROM tb_paciente WHERE idt_paciente = %s;"
        cs = self.mysql.consultar(comando,[idt])
        pessoa = cs.fetchone()
        return pessoa
    
