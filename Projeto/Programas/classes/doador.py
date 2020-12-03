from BDDS.controllers.doadorController import doadorController
from BDDS.classes.pessoa import Pessoa



class Doador(Pessoa):

    def __init__(self, cpf, nome, peso, idade, sexo, endereco, tipo, rh, qtdDoacoes):
        super().__init__(cpf, nome, peso, idade, sexo, endereco, tipo, rh)
        self.qtdDoacoes = qtdDoacoes
        
    def alterarDoador(self, idt):
        doadorController().alterarDoador(self, idt)

    def getDoadorByIdt(self, idt):
        doadorController().getDoadorByIdt(self, idt)

    def excluirDoador(self, idt):
        doadorController().excluirDoador(idt)

    def getAllDoadores(self):
        doadorController().getAllDoadores()



