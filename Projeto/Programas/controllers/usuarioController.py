from BDDS.db.db import SQL



class usuarioController():

    def __init__(self):
        self.mysql = SQL("root", "", "test")

    def getLogin(self, usuario):
        nome = usuario.getNome()
        senha = usuario.getSenha()
        comando = "SELECT nome FROM tb_usuario WHERE nome=%s and senha=%s;"
        cs = self.mysql.consultar(comando, [nome, senha])
        if cs.fetchone() is not None:
            return True
        else:
            return False

    def setLogin(self, usuario):
        nome = usuario.getNome()
        senha = usuario.getSenha()
        comando = "INSERT INTO tb_usuario (nome, senha) VALUES(%s, %s);"
        self.mysql.executar(comando, [nome, senha])