# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presencas

@app.route('/')
def index():
    

     # mensagens = Mensagem.recupera_todas()
    presenca_posts = Presencas.recupera_todos_presenca()
 
    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/gabriel',
                'texto': 'Sobre - Gabriel'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'presenca_posts': presenca_posts}

    return render_template('index.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def presenca_gravar_post():
    email = request.form['email']
    presenca = request.form['presenca']
    resposta = request.form['resposta']
    comentario = request.form['comentario']
    post_presenca = Presencas(email, presenca, resposta, comentario)
    post_presenca.gravar()
    return redirect('/')

@app.route('/gabriel')
def gabriel():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': True,
                'href': '/gabriel',
                'texto': 'Sobre - Gabriel'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Sobre - Gabriel',
            'menu': menu}# oq define frase la em

    return render_template('gabriel.html', **context)


@app.route('/presenca')
def presenca():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/gabriel',
                'texto': 'Sobre - Gabriel'})
    menu.append({'active': True,
                'href': '/presenca',
                'texto': 'Presença'})

    context = {'titulo': 'Presença',
            'menu': menu}# oq define frase la em

    return render_template('presenca.html', **context)



app.run()
