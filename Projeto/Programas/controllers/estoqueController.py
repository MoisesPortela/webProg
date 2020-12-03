from BDDS.db.db import SQL
from BDDS.controllers.doadorController import doadorController
from BDDS.classes.doador import Doador



class estoqueController():

    def __init__(self):
        self.mysql = SQL("root", "", "test")

    def incluirNovaDoacao(self, doador, qtdDoado, idtDoador):
        print(doador)
        doador = Doador(doador[1], doador[2], doador[3], doador[4], doador[5], doador[6], doador[7], doador[8], doador[9])
        sangue = self.getSangueByTipoRh(doador.tipo, doador.rh)
        comando_updt_estoque = "UPDATE tb_estoque SET qtd_disponivel_litros=qtd_disponivel_litros+%s WHERE idt_sangue=%s;"
        comando_updt_doador = "UPDATE tb_doador SET qtd_doacoes = qtd_doacoes + 1, total_litros = total_litros + %s WHERE idt_doador = %s;"
        try:
            self.mysql.executar(comando_updt_estoque, (float(qtdDoado), sangue[0]))
            self.mysql.executar(comando_updt_doador, (float(qtdDoado), idtDoador))
        except Exception as e:
            print(e)

    def getSangueByTipoRh(self, tipo, rh):
        comando = "SELECT idt_sangue, qtd_disponivel_litros FROM tb_estoque WHERE tipo = %s AND rh = %s;"
        cs = self.mysql.consultar(comando, (tipo, rh))
        return cs.fetchone()
    
    def getAllSangue(self):
        comando = "SELECT * FROM tb_estoque;"
        cs = self.mysql.consultar(comando, ())
        return cs.fetchall()