import kivy
import sqlite3
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

kivy.require('1.11.0')


base_dados = 'base_dados3.db'


def usando_sqlite3_gravando_nome(nome):
    conn = sqlite3.connect(base_dados)
    cursor = conn.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS base_dados(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT
                        );
                    ''')
    cursor.execute('''INSERT INTO base_dados (nome) VALUES (?)''', [nome])
    conn.commit()
    conn.close()


def usando_sqlite3_retornando_nome(base_dados, valor_pesquisado):
    try:
        # retorna o valor de Primary Key
        conn = sqlite3.connect(base_dados)
        cursor = conn.cursor()
        cursor.execute('''
                                SELECT *
                                FROM '{}'
                                WHERE (nome == '{}')    
                                '''.format(base_dados[:-4], valor_pesquisado))

        return str(cursor.fetchall()[0][0])
    except:
        return 'Valor não encontrado.'


def usando_sqlite3_deletar_tudo(base_dados):
    try:
        conn = sqlite3.connect(base_dados)
        cursor = conn.cursor()
        cursor.execute('''
                        DROP TABLE '{}'
                        '''.format(base_dados[:-4]))
    except:
        pass


class Tela(GridLayout):

    def salvar_nome(self):
        usando_sqlite3_gravando_nome(self.ids.caixa_texto.text)

    def exibir_numero(self):
        vl_pesq = self.ids.caixa_texto.text
        numero = usando_sqlite3_retornando_nome(base_dados, vl_pesq)
        self.ids.retorno.text = 'Seu numero de cadastro é : ' + numero

    def deletar_tudo(self):
        usando_sqlite3_deletar_tudo(base_dados)

class Tela2(GridLayout):
    pass

class TelaApp(App):
    def build(self):
        return Tela()


TelaApp().run()