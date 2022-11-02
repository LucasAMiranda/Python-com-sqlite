import email
import sqlite3
from datetime import date
import os

conexao = sqlite3.connect('brinquei.db')
cursor = conexao.cursor()

print("SEJA BEM VINDO AO BRINQUEI, DEVOLVI.")

class Sistema():
    def __init__(self):
        self.nome = None
        self.telefone = None
        self.email = None
        self.senha = None
        self.cpf = None

    def menu(self):
        opcao = input('''Escolha uma das opções abaixo:
        1 - CADASTRO
        2 - LOGIN 
        3 - LOCALIZAR
        4 - LOCALIZAR BRINQUEDO NO SISTEMA   
        5 - RENOVAR BRINQUEDO
        6 - EXCLUIR
        7 - SAIR DO SISTEMA
        ''')

        if opcao == '1':
            self.cadastroSistema()
        elif opcao == '2':
            self.loginSistema()
        elif opcao == '3':
            self.localizarSistema()
        elif opcao == '4':
            self.localizarSistemaBrinquedo()
        elif opcao == '5':
            self.renovarSistema()
        elif opcao == '6':
            self.excluirSistema()
        elif opcao == '7':
            self.sairSistema()
        else:
            print("Opção inválida,retornando ao menu!")

    def cadastroSistema(self):
        self.nome = str(input("Digite seu nome: "))
        self.telefone = int(input("Digite seu numero de telefone:"))
        self.email = str(input("Digite seu email:"))
        self.senha = int(input("cadastre sua senha:"))
        self.cpf = int(input("Digite seu cpf: "))
        cursor.execute(f"INSERT INTO clientes (NOME, TELEFONE, EMAIL, SENHA, CPF) VALUES (?,?,?,?,?)",(self.nome, self.telefone,self.email, self.senha, self.cpf))
        conexao.commit()

    def loginSistema(self):
        self.usuario = str(input("Digite seu nome: ")).strip()
        self.senha = int(input("Digite sua senha:"))
        cursor.execute(
            f"SELECT nome,senha FROM clientes WHERE nome = '{self.usuario}' and senha = {self.senha} ")
        for linha in cursor.fetchall():
            nome, senha = linha
            if self.usuario == nome and self.senha == senha:
                print("Login efetuado com sucesso!")
                print(f"Olá, {self.usuario}. O que você deseja fazer?")

        # Else não esta trazendo o erro. ver se acrescenta mais condicionais.
        # criar uma variavel  pra locar brinquedo, data da locação e mais importante a renovação que será de 7 dias
        # colocar a função renovar dentro do login,
    def localizarSistema(self):
        self.nome = str(input("Digite o nome do briquedo para locação: "))
        cursor.execute(f"SELECT nome FROM clientes where nome == '{self.nome}' ")
        for linha in cursor.fetchall():
            print(linha)

    # criar opção para locação de briquedo , escolhendo o brinquedo.
    # pegar a data atual e devolver 7 dias depois . No caso dia 14.
    '''
        def emprestimoSistema(self):
            cursor.execute()
    '''

    def localizarSistemaBrinquedo(self):
        self.nome_brinquedo = str(input("Escolha o nome do brinquedo: "))
        cursor.execute(
            f"SELECT BRINQUEDO, DATA_LOCAÇÃO FROM brinquedos where BRINQUEDO == '{self.nome_brinquedo}' ")
        for linha in cursor.fetchall():
            print(linha)

    # aqui quando localizar passar sempre a data que será devolvido o brinquedo além do nome cliente e brinquedo locado
    def renovarSistema(self): 
        self.localizarSistemaBrinquedo 
        self.nome = str(input("Digite o seu nome(cliente): "))
        cursor.execute(f"SELECT BRINQUEDO, DATA_LOCAÇÃO FROM brinquedos where nome, DATA_LOCAÇÃO  == '{self.nome}, {self.data_devolvido}' ")
        conexao.commit()

        data_devolvido = date.today + 7
        print(data_devolvido)
        # quero colocar a data do aluguel aqui e renovar por mais 7 dias chamar função pelo datetime e acrescentar dias
        # colocar select e update, mas seria melhor se essa opção estivesse sendo chamada quando logar.

    def excluirSistema(self):
        self.usuario = str(input("Digite nome do usuario:"))
        cursor.execute(f"DELETE FROM clientes WHERE nome = '{self.usuario}'")
        conexao.commit()
        print("Excluido com sucesso!")

        #opcao para realte deslogar do sistema para ele não ficar rodando
    def sairSistema(self):
        print("Você não esta mais logado.")
    '''
        def coresTerminal(self, Estilo, Cor, Fundo):
            match Estilo:
                case 0:
                    estilo = "0"  # Padrão
                case 1:
                    estilo = "1"  # Negrito
                case 2:
                    estilo = "4"  # Sublinhado
                case 3:
                    estilo = "7"  # Negativo
            match Cor:
                case 0:
                    cor = "37"  # Padrão
                case 1:
                    cor = "30"  # Cinza
                case 2:
                    cor = "31"  # Vermelho
                case 3:
                    cor = "32"  # Verde
                case 4:
                    cor = "33"  # Amarelo
                case 5:
                    cor = "34"  # Roxo
                case 6:
                    cor = "35"  # Rosa
                case 7:
                    cor = "36"  # Azul
            match Fundo:
                case 0:
                    fundo = "40"  # Padrão
                case 1:
                    fundo = "47"  # Cinza
                case 2:
                    fundo = "41"  # Vermelho
                case 3:
                    fundo = "42"  # Verde
                case 4:
                    fundo = "43"  # Amarelo
                case 5:
                    fundo = "44"  # Roxo
                case 6:
                    fundo = "45"  # Rosa
                case 7:
                    fundo = "46"  # Azul
            base = "\033[0;37;40m"
            padrão = (f"\033[{estilo};{cor};{fundo}m")

        return padrão, base
        '''

while True:
    sistema = Sistema()
    sistema.menu()