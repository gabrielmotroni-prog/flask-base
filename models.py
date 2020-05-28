## models.py
from banco import bd


class Presencas:
    def __init__(self, email, presenca, resposta, comentario):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentario = comentario

    def gravar(self):
        sql = '''insert into presenca (email, presenca, resposta,comentario) values (?, ?, ?, ?)'''
        primeiro_interrogacao = self.email
        segundo_interrogacao = self.presenca
        terceiro_interrogacao = self.resposta
        quarta_interrogacao = self.comentario
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao, quarta_interrogacao])
        bd().commit()

    @staticmethod
    def recupera_todos_presenca():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''select email, presenca, resposta,comentario from presenca order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        posts = []
        for email, presenca, resposta, comentario in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            post = Presencas(email, presenca, resposta, comentario)
            posts.append(post)

        return posts
