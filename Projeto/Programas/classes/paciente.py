from BDDS.controllers.pacienteController import pacienteController
from BDDS.classes.pessoa import Pessoa


class Paciente(Pessoa):

    def __init__(self, cpf, nome, peso, idade, sexo, endereco, tipo, rh, stsNecessidade):
        super().__init__(cpf, nome, peso, idade, sexo, endereco, tipo, rh)
        self.stsNecessidade = stsNecessidade

    def alterarPaciente(self, idt):
        pacienteController().alterarPaciente(self, idt)

    def getAllPacientes(self):
        pacienteController().getAllPacientes()

    def getPacienteByIdt(self, idt):
        pacienteController().getPacienteByIdt()

    def excluirPaciente(self, idt):
        pacienteController().excluirPaciente()

    def incluirPaciente(self):
        pacienteController().incluirPaciente()



