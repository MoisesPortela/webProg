from BDDS.classes.usuario import Usuario
from BDDS.classes.doador import Doador
from BDDS.classes.paciente import Paciente
from BDDS.controllers.doadorController import doadorController
from BDDS.controllers.usuarioController import usuarioController
from BDDS.controllers.pacienteController import pacienteController
from BDDS.controllers.estoqueController import estoqueController
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('formLogin.html')


@app.route('/loginUsuario', methods=['POST', 'GET'])
def loginUsuario():
    nome = request.form['nome']
    senha = request.form['senha']
    usuario = Usuario(nome, senha)
    if usuario.getLogin():
        return render_template('menu.html')
    else:
        return render_template('formLogin.html', msg="Nome ou senha invalidos!.")

@app.route('/menu', methods=['POST'])
def menu():
    return render_template('menu.html')

@app.route('/formCadastroUsuario', methods=['POST', 'GET'])
def formCadastroUsuario():
    return render_template('formCadastroUsuario.html')


@app.route('/incluirUsuario', methods=['POST'])
def incluirUsuario():
    nome = request.form['nome']
    senha = request.form['senha']
    usuario = Usuario(nome,senha)
    usuario.setLogin()
    return render_template('formLogin.html')


@app.route('/doador', methods=['POST'])
def doadorView():
    allDoadores = doadorController().getAllDoadores()
    doadores = ""
    print(allDoadores)
    for [idt, CPF, nome, peso, idade, sexo, local, tipo, rh, qtdDoacoes, totalLitros] in allDoadores:
        doadores += "<TR>"
        doadores += "<TD>" + CPF + "</TD>"
        doadores += "<TD>" + nome + "</TD>"
        doadores += "<TD>" + str(peso) + "</TD>"
        doadores += "<TD>" + str(idade) + "</TD>"
        doadores += "<TD>" + sexo + "</TD>"
        doadores += "<TD>" + local + "</TD>"
        doadores += "<TD>" + tipo + "</TD>"
        doadores += "<TD>" + rh + "</TD>"
        doadores += "<TD>" + str(qtdDoacoes) + "</TD>"
        doadores += "<TD>" + str(totalLitros) + "</TD>"
        doadores += "<TD><form action=\"/formAlterarDoador?idt={}\" method=\"POST\"><button " \
                    "type=\"submit\">Alterar</button></form></TD>".format(idt)
        doadores += "<TD><form action=\"/excluirDoador?idt={}\" method=\"POST\"><button " \
                    "type=\"submit\">Excluir</button></form></TD>".format(idt)
        doadores += "<TD><form action=\"/formNovaDoacao?idt={}\" method=\"POST\"><button " \
                    "type=\"submit\">Nova doação</button></form></TD>".format(idt)
        doadores += "</TR>"
    return render_template('doador.html', doadores=doadores)


@app.route('/formAlterarDoador', methods=['POST'])
def formAlterarDoador():
    idt = request.args.get('idt')
    doador = doadorController().getDoadorByIdt(idt)
    return render_template('formAlterarDoador.html', doador=doador)


@app.route('/alterarDoador', methods=['POST'])
def alterarDoador():
    idt = request.form['idt']
    cpf = request.form['CPF']
    nome = request.form['nome']
    peso = float(request.form['peso'])
    idade = int(request.form['idade'])
    sexo = request.form['sexo']
    endereco = request.form['endereco']
    doador = Doador(cpf, nome, peso, idade, sexo, endereco, "", "", "")
    doador.alterarDoador(idt)
    return redirect(url_for('doadorView'),307)


@app.route('/excluirDoador', methods=['POST'])
def excluirDoador():
    idt = request.args.get('idt')
    doadorController().excluirDoador(idt)
    return redirect(url_for('doadorView'),307)


@app.route('/formCadastrarDoador', methods=['POST'])
def formCadastroDoador():
    return render_template('formCadastrarDoador.html')


@app.route('/cadastrarDoador', methods=['POST'])
def cadastrarDoador():
    cpf = request.form['CPF']
    nome = request.form['nome']
    peso = request.form['peso']
    idade = request.form['idade']
    sexo = request.form['sexo']
    endereco = request.form['endereco']
    rh = request.form['rh']
    tipo = request.form['tipo']
    doador = Doador(cpf, nome, peso, idade, sexo, endereco, tipo, rh, 0)
    doadorController().incluirDoador(doador)

    return redirect(url_for('doadorView'),307)


@app.route('/paciente', methods=['POST'])
def pacienteView():
    allPacientes = pacienteController().getAllPacientes()
    pacientes = ""
    print(allPacientes)
    for [idt, CPF, nome, peso, idade, sexo, local, tipo, rh, stsNecessidade] in allPacientes:
        pacientes += "<TR>"
        pacientes += "<TD>" + CPF + "</TD>"
        pacientes += "<TD>" + nome + "</TD>"
        pacientes += "<TD>" + str(peso) + "</TD>"
        pacientes += "<TD>" + str(idade) + "</TD>"
        pacientes += "<TD>" + sexo + "</TD>"
        pacientes += "<TD>" + local + "</TD>"
        pacientes += "<TD>" + tipo + "</TD>"
        pacientes += "<TD>" + rh + "</TD>"
        if(str(stsNecessidade) == "0"):
            stsNecessidade = "Não"
        else:
            stsNecessidade = "Sim"
        pacientes += "<TD>" + stsNecessidade + "</TD>"
        pacientes += "<TD><form action=\"/formAlterarPaciente?idt={}\" method=\"POST\"><button " \
                    "type=\"submit\">Alterar</button></form></TD>".format(idt)
        pacientes += "<TD><form action=\"/excluirPaciente?idt={}\" method=\"POST\"><button " \
                    "type=\"submit\">Excluir</button></form></TD>".format(idt)
        pacientes += "</TR>"
    return render_template('paciente.html', pacientes=pacientes)


@app.route('/formAlterarPaciente', methods=['POST'])
def formAlterarPaciente():
    idt = request.args.get('idt')
    paciente = pacienteController().getPacienteByIdt(idt)
    return render_template('formAlterarPaciente.html', paciente=paciente)


@app.route('/alterarPaciente', methods=['POST'])
def alterarPaciente():
    idt = request.form['idt']
    cpf = request.form['CPF']
    nome = request.form['nome']
    peso = float(request.form['peso'])
    idade = int(request.form['idade'])
    sexo = request.form['sexo']
    endereco = request.form['endereco']
    stsNecessidade = request.form['necessidade']
    paciente = Paciente(cpf, nome, peso, idade, sexo, endereco, "", "", stsNecessidade)
    paciente.alterarPaciente(idt)
    return redirect(url_for('pacienteView'),307)


@app.route('/excluirPaciente', methods=['POST'])
def excluirPaciente():
    idt = request.args.get('idt')
    pacienteController().excluirPaciente(idt)
    return redirect(url_for('pacienteView'),307)


@app.route('/formCadastrarPaciente', methods=['POST'])
def formCadastroPaciente():
    return render_template('formCadastrarPaciente.html')


@app.route('/cadastrarPaciente', methods=['POST'])
def cadastrarPaciente():
    cpf = request.form['CPF']
    nome = request.form['nome']
    peso = request.form['peso']
    idade = request.form['idade']
    sexo = request.form['sexo']
    endereco = request.form['endereco']
    rh = request.form['rh']
    tipo = request.form['tipo']
    paciente = Paciente(cpf, nome, peso, idade, sexo, endereco, tipo, rh, 0)
    pacienteController().incluirPaciente(paciente)

    return redirect(url_for('pacienteView'),307)


@app.route('/formNovaDoacao', methods=['POST'])
def formNovaDoacao():
    idt = request.args.get('idt')
    doador = doadorController().getDoadorByIdt(idt)
    return render_template('formNovaDoacao.html', doador=doador, idt=idt)

@app.route('/novaDoacao', methods=['POST'])
def novaDoacao():
    idt = request.form['idt']
    qtdDoado = float(request.form['qtdDoado'])
    doador = doadorController().getDoadorByIdt(idt)
    qtdDoado=qtdDoado/1000
    str(qtdDoado)
    estoqueController().incluirNovaDoacao(doador, qtdDoado, idt)
    return redirect(url_for('doadorView'), 307)
    
@app.route('/estoque', methods=['POST'])
def estoque():
    allSangue = estoqueController().getAllSangue()
    estoque = ""
    for [idt, tipo, rh, qtdDisponivel] in allSangue:
        estoque += "<TR>"
        estoque += "<TD>" + tipo + "</TD>"
        estoque += "<TD>" + rh + "</TD>"
        estoque += "<TD>" + str(qtdDisponivel) + " Litros </TD>"
        estoque += "</TR>"
    return render_template('estoque.html', estoque=estoque  )

if __name__ == '__main__':
    app.run(debug=True)