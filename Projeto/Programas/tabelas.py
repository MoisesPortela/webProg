from BDDS.db import db

mysql =db.SQL("root", "", "test")

comando = "create table tb_usuario(id_usuario int primary key auto_increment not null,nome varchar(50) not null," \
          "senha varchar(50) not null);"

if mysql.executar(comando, ()):
   print ("Tabela de usuarios com sucesso!")


comando = "CREATE TABLE tb_pessoa(idt_pessoa INT PRIMARY KEY AUTO_INCREMENT," \
          "cpf VARCHAR(14)NOT NULL,nome VARCHAR(50)NOT NULL,peso FLOAT NOT NULL," \
          "idade INT NOT NULL ,sexo VARCHAR(10)NOT NULL,endereco TEXT NOT NULL ," \
          "tipo VARCHAR(3),rh CHAR(1) NOT NULL);"


if mysql.executar(comando, ()):
   print ("Tabela de pessoas criado com sucesso!")

comando = "CREATE TABLE tb_doador(idt_doador INT PRIMARY KEY AUTO_INCREMENT,cod_pessoa int not null," \
          "qtd_doacoes int not null,total_litros float not null,CONSTRAINT fk_doador_pessoa FOREIGN KEY (cod_pessoa)" \
          "REFERENCES tb_pessoa(idt_pessoa));"


if mysql.executar(comando, ()):
   print ("Tabela de doadores criado com sucesso!")

comando = "CREATE TABLE tb_paciente(idt_paciente INT PRIMARY KEY AUTO_INCREMENT,cod_pessoa int not null," \
          "sts_necessidade bool not null,CONSTRAINT fk_paciente_pessoa FOREIGN KEY " \
          "(cod_pessoa) REFERENCES tb_pessoa(idt_pessoa));"


if mysql.executar(comando, ()):
   print ("Tabela de paciente criado com sucesso!")

comando = "CREATE TABLE tb_estoque(idt_sangue INT PRIMARY KEY AUTO_INCREMENT," \
          "tipo VARCHAR(3) not null,rh CHAR(1) not null,qtd_disponivel_litros float not null);"


if mysql.executar(comando, ()):
   print ("Tabela de estoques criado com sucesso!")

comando = "insert into tb_estoque (tipo, rh, qtd_disponivel_litros) values ('A', '-', 0), ('A', '+', 0), " \
          "('B', '-', 0), ('B', '+', 0),('AB', '-', 0), ('AB', '+', 0),('O', '-', 0), ('O', '+', 0);"



if mysql.executar(comando, ()):
   print ("Tabela de estoques criado com sucesso!")


