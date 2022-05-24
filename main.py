from flask import Flask, render_template, request, redirect, session, flash
import os

from dao_projeto_interdisciplinar import AlimentoDao, UsuarioDao, EventoDao, Modalidade_RefeicaoDao, IngredienteDao, LocalDao, DiaDao, CategoriaDao, CardapioDao, RefeicaoDao
from flask_mysqldb import MySQL

from models_projeto_interdisciplinar import Alimentos, Usuario, Evento, Modalidade_Refeicao, Ingrediente, Local, Dia, Categoria, Cardapio, Refeicao

app=Flask(__name__)
app.secret_key='LP2'

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='projetointerdisciplinar'
app.config['MYSQL_PORT']=3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__))+'/uploads'
db=MySQL(app)
alimento_dao=AlimentoDao(db)
usuario_dao=UsuarioDao(db)
evento_dao=EventoDao(db)
modalidade_refeicao_dao=Modalidade_RefeicaoDao(db)
ingrediente_dao=IngredienteDao(db)
local_dao=LocalDao(db)
dia_dao=DiaDao(db)
categoria_dao=CategoriaDao(db)
cardapio_dao=CardapioDao(db)
refeicao_dao=RefeicaoDao(db)

#Criando uma página web com uma lista de alimentos de um restaurante estudantil
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login')
    return render_template('index_projeto_interdisciplinar.html')

#ALIMENTOS
@app.route('/lista_alimentos')
def lista_alimentos():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_alimentos')
    lista=alimento_dao.listar()
    return render_template('lista_alimentos.html', alimentos=lista)

#USUÁRIOS
@app.route('/lista_usuarios')
def lista_usuarios():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_usuarios')
    lista=usuario_dao.listar()
    return render_template('lista_usuarios.html', usuarios=lista)

#EVENTOS
@app.route('/lista_eventos')
def lista_eventos():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_eventos')
    lista=evento_dao.listar()
    return render_template('lista_eventos.html', eventos=lista)

#MODALIDADES
@app.route('/lista_modalidades_refeicoes')
def lista_modalidades_refeicoes():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_modalidades_refeicoes')
    lista=modalidade_refeicao_dao.listar()
    return render_template('lista_modalidades_refeicoes.html', modalidades=lista)

#INGREDIENTES
@app.route('/lista_ingredientes')
def lista_ingredientes():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_ingredientes')
    lista=ingrediente_dao.listar()
    return render_template('lista_ingredientes.html', ingredientes=lista)

#LOCAL
@app.route('/lista_locais')
def lista_locais():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_locais')
    lista=local_dao.listar()
    return render_template('lista_locais.html', locais=lista)

#DIAS
@app.route('/lista_dias')
def lista_dias():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_dias')
    lista=dia_dao.listar()
    return render_template('lista_dias.html', dias=lista)

#CATEGORIAS
@app.route('/lista_categorias')
def lista_categorias():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_categorias')
    lista=categoria_dao.listar()
    return render_template('lista_categorias.html', categorias=lista)

#Cardápios
@app.route('/lista_cardapios')
def lista_cardapios():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_cardapios')
    lista=cardapio_dao.listar()
    return render_template('lista_cardapios.html', cardapios=lista)

#REFEICOES
@app.route('/lista_refeicoes')
def lista_refeicoes():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=lista_refeicoes')
    lista=refeicao_dao.listar()
    return render_template('lista_refeicoes.html', refeicoes=lista)

#Criando a função de inserir alimentos na lista
@app.route('/novo_alimento')
def novo_alimento():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_alimento')
    lista=categoria_dao.listar()
    return render_template('novo_alimento.html', titulo="Inserindo novo Alimento", categorias=lista)

#Criando a função de inserir novos usuários
@app.route('/novo_usuario')
def novo_usuario():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_usuario')
    return render_template('novo_usuario.html', titulo="Inserindo novo Usuário")

#Criando a função de inserir eventos na lista
@app.route('/novo_evento')
def novo_evento():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_evento')
    return render_template('novo_evento.html', titulo="Inserindo novo Evento")

#Criando a função de inserir modalidades na lista
@app.route('/nova_modalidades_refeicoes')
def novo_modalidades_refeicoes():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_evento')
    return render_template('novo_modalidades_refeicoes.html', titulo="Inserindo nova Modalidade de Refeição")

#Criando a função de inserir ingredientes na lista
@app.route('/novo_ingrediente')
def novo_ingrediente():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_ingrediente')
    return render_template('novo_ingrediente.html', titulo="Inserindo novo Ingrediente")

#Criando a função de inserir locais na lista
@app.route('/novo_local')
def novo_local():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_local')
    return render_template('novo_local.html', titulo="Inserindo novo Local")

#Criando a função de inserir dias na lista
@app.route('/novo_dia')
def novo_dia():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_dia')
    return render_template('novo_dia.html', titulo="Inserindo novo Dia")

#Criando a função de inserir categorias na lista
@app.route('/novo_categoria')
def novo_categoria():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_categoria')
    return render_template('novo_categoria.html', titulo="Inserindo nova Categoria")

#Criando a função de inserir cardapios na lista
@app.route('/novo_cardapio')
def novo_cardapio():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_cardapio')
    return render_template('novo_cardapio.html', titulo="Inserindo novo Cardápio")

#Criando a função de inserir cardapios na lista
@app.route('/nova_refeicao')
def nova_refeicao():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=nova_refeicao')
    return render_template('nova_refeicao.html', titulo="Inserindo nova Refeição")

@app.route('/criar', methods=['POST',])
def criar():
    Descricao=request.form['Descricao']
    Categorias_ID_Categoria=request.form['Categoria']
    alimento=Alimentos(Descricao, Categorias_ID_Categoria, None)
    alimento_dao.salvar(alimento)

    flash('O alimento foi adicionado com sucesso!')
    return redirect('/lista_alimentos')

@app.route('/criar_usuario', methods=['POST',])
def criar_usuario():
    id=request.form['id']
    senha=request.form['senha']
    usuario=Usuario(id, senha)
    usuario_dao.salvar(usuario)

    flash('O usuário foi cadastrado com sucesso!')
    return redirect('/lista_usuarios')

#Função para a criação de um evento
@app.route('/criar_evento', methods=['POST',])
def criar_evento():
    Nome_Evento=request.form['Nome_Evento']
    evento=Evento(Nome_Evento)
    evento_dao.salvar(evento)

    flash('O evento foi adicionado com sucesso!')
    return redirect('/lista_eventos')

#Função para a criação de uma Modalidade De Refeição
@app.route('/criar_modalidades_refeicoes', methods=['POST',])
def criar_modalidades_refeicoes():
    Modalidade=request.form['Modalidade']
    modalidade=Modalidade_Refeicao(Modalidade)
    modalidade_refeicao_dao.salvar(modalidade)

    flash('A modalidade de refeição foi adicionado com sucesso!')
    return redirect('/lista_modalidades_refeicoes')

#Função para a criação de um Ingrediente
@app.route('/criar_ingrediente', methods=['POST',])
def criar_ingrediente():
    Descricao_Ingrediente=request.form['Descricao_Ingrediente']
    Quantidade_Ingrediente=request.form['Quantidade_Ingrediente']
    Unidade_Medida_Ingrediente=request.form['Unidade_Medida_Ingrediente']
    ingrediente=Ingrediente(Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente)
    ingrediente_dao.salvar(ingrediente)

    flash('O ingrediente foi adicionado com sucesso!')
    return redirect('/lista_ingredientes')

#Função para a criação de um local
@app.route('/criar_local', methods=['POST',])
def criar_local():
    Nome_RU=request.form['Nome_RU']
    Local_RU=request.form['Local_RU']
    local=Local(Nome_RU, Local_RU)
    local_dao.salvar(local)

    flash('O local foi adicionado com sucesso!')
    return redirect('/lista_locais')

#Função para a criação de um dia
@app.route('/criar_dia', methods=['POST',])
def criar_dia():
    Data=request.form['Data']
    Dia_Semana=request.form['Dia_Semana']
    Precipitacao=request.form['Precipitacao']
    Umidade=request.form['Umidade']
    Vento=request.form['Vento']
    Temperatura=request.form['Temperatura']
    dia=Dia(Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura)
    dia_dao.salvar(dia)

    flash('O dia foi adicionado com sucesso!')
    return redirect('/lista_dias')

#Função para a criação de uma categoria
@app.route('/criar_categoria', methods=['POST',])
def criar_categoria():
    Nome_Categoria=request.form['Nome_Categoria']
    categoria=Categoria(Nome_Categoria)
    categoria_dao.salvar(categoria)

    flash('A categoria foi adicionada com sucesso!')
    return redirect('/lista_categorias')

#Função para a criação de um cardápio
@app.route('/criar_cardapio', methods=['POST',])
def criar_cardapio():
    Descricao=request.form['Descricao']
    cardapio=Cardapio(Descricao)
    cardapio_dao.salvar(cardapio)

    flash('O cardapio foi adicionado com sucesso!')
    return redirect('/lista_cardapios')

#Função para a criação de uma refeição
@app.route('/criar_refeicao', methods=['POST',])
def criar_refeicao():
    Quantidade_por_pratos=request.form['Quantidade_por_pratos']
    refeicao=Refeicao(Quantidade_por_pratos)
    refeicao_dao.salvar(refeicao)

    flash('A refeição foi adicionada com sucesso!')
    return redirect('/lista_refeicoes')

#Criando Login
@app.route('/login')
def login():
    proxima=request.args.get('proxima')
    if proxima==None:
        proxima=''
    return render_template('login_plataforma_restaurante.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=usuario_dao.busca_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha==request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            flash(request.form['usuario'] + ' fez o login com sucesso na plataforma!')
            proxima_pagina=request.form['proxima']
            if proxima_pagina=='':
                return redirect('/')
            else:
                return redirect('/{}'.format(proxima_pagina))
    flash('Não logado, tente novamente')
    return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado']=None
    flash('Nenhum usuario logado')
    return redirect('/login')

@app.route('/editar/<int:ID_Alimento>')
def editar(ID_Alimento):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar')
    alimento=alimento_dao.busca_por_id(ID_Alimento)
    lista=categoria_dao.listar()
    print(alimento._Descricao)
    return render_template('editar_projeto_interdisciplinar.html', titulo="Modificando o alimento", alimento=alimento, categorias=lista)

#Função para editar evento
@app.route('/editar_evento/<int:ID_Eventos>')
def editar_evento(ID_Eventos):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_evento')
    evento=evento_dao.busca_por_id(ID_Eventos)
    return render_template('editar_evento_projetointerdisciplinar.html', titulo="Modificando o evento", evento=evento)

#Função para editar Modalidade de Refeições
@app.route('/editar_modalidades_refeicoes/<int:ID_Modalidade_Refeicao>')
def editar_modalidades_refeicoes(ID_Modalidade_Refeicao):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_modalidade_refeicoes')
    modalidade=modalidade_refeicao_dao.busca_por_id(ID_Modalidade_Refeicao)
    return render_template('editar_modalidades_refeicoes_projetointerdisciplinar.html', titulo="Modificando a Modalidade de Refeições", modalidade=modalidade)

#Função para editar ingrediente
@app.route('/editar_ingrediente/<int:ID_Ingrediente>')
def editar_ingrediente(ID_Ingrediente):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_ingrediente')
    ingrediente=ingrediente_dao.busca_por_id(ID_Ingrediente)
    return render_template('editar_ingrediente_projetointerdisciplinar.html', titulo="Modificando o Ingrediente", ingrediente=ingrediente)

#Função para editar local
@app.route('/editar_local/<int:ID_Local_RU>')
def editar_local(ID_Local_RU):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_local')
    local=local_dao.busca_por_id(ID_Local_RU)
    return render_template('editar_local_projetointerdisciplinar.html', titulo="Modificando o Local", local=local)

#Função para editar dia
@app.route('/editar_dia/<int:ID_Dia>')
def editar_dia(ID_Dia):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_dia')
    dia=dia_dao.busca_por_id(ID_Dia)
    return render_template('editar_dia_projetointerdisciplinar.html', titulo="Modificando o Dia", dia=dia)

#Função para editar categoria
@app.route('/editar_categoria/<int:ID_Categoria>')
def editar_categoria(ID_Categoria):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_categoria')
    categoria=categoria_dao.busca_por_id(ID_Categoria)
    return render_template('editar_categoria_projetointerdisciplinar.html', titulo="Modificando a Categoria", categoria=categoria)

#Função para editar cardápio
@app.route('/editar_cardapio/<int:ID_Cardapio>')
def editar_cardapio(ID_Cardapio):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_cardapio')
    cardapio=cardapio_dao.busca_por_id(ID_Cardapio)
    return render_template('editar_cardapio_projetointerdisciplinar.html', titulo="Modificando o Cardápio", cardapio=cardapio)

#Função para editar refeições
@app.route('/editar_refeicao/<int:ID_Refeicao>')
def editar_refeicao(ID_Refeicao):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_refeicao')
    refeicao=refeicao_dao.busca_por_id(ID_Refeicao)
    return render_template('editar_refeicao_projetointerdisciplinar.html', titulo="Modificando a Refeição", refeicao=refeicao)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    Descricao=request.form['Descricao']
    Categorias_ID_Categoria=request.form['Categoria']
    ID_Alimento = request.form['ID_Alimento']
    dictItens = request.form
    lista_ingredientes_aux=[]
    aux_ingrediente=[]
    aux_cont=0
    for key, value in dictItens.items():
        if key.startswith("TDIngrediente."):
            #print para auxiliar.. aquele key.startswith pega todos names que começam com TDIngrediente. que foram inseridos campos do tipo hidden no app6.js.
            #print(key, value)
            aux_ingrediente.append(value)
            #no nosso caso, são 4 campos recuperados: Descrição, Quantidade, Unidade e Id, por isso essa verificação = 3.
            if aux_cont==3:
                ingrediente=Ingrediente(aux_ingrediente[1],aux_ingrediente[2],aux_ingrediente[3],aux_ingrediente[0])
                lista_ingredientes_aux.append(ingrediente)
                aux_ingrediente=[]
                aux_cont=0
            else:
                aux_cont+=1
    #print para testar se a lista está preenchida com ingredientes, pode remover depois:
    #for i in lista_ingredientes_aux:
        #print(i.getIdIngrediente())
    alimento=Alimentos(Descricao, Categorias_ID_Categoria, None, lista_ingredientes_aux, ID_Alimento)
    alimento_dao.salvar(alimento)

    flash('O alimento foi editado com sucesso!')
    return redirect('/lista_alimentos')

#Função para atualizar dados dos usuários
@app.route('/atualizar_usuario', methods=['POST',])
def atualizar_usuario():
    id=request.form['id']
    nome=request.form['nome']
    senha=request.form['senha']
    usuario=Usuario(id, nome, senha)
    usuario_dao.salvar(usuario)

    flash('Os dados do usuário foram editados com sucesso!')
    return redirect('/lista_usuarios')

#Função para atualizar eventos
@app.route('/atualizar_eventos', methods=['POST',])
def atualizar_eventos():
    Nome_Evento=request.form['Nome_Evento']
    ID_Eventos=request.form['ID_Eventos']
    evento=Evento(Nome_Evento, ID_Eventos)
    evento_dao.salvar(evento)

    flash('O evento foi editado com sucesso!')
    return redirect('/lista_eventos')

#Função par atualizar Modalidades de Refeições
@app.route('/atualizar_modalidades_refeicoes', methods=['POST',])
def atualizar_modalidades_refeicoes():
    Modalidade=request.form['Modalidade']
    ID_Modalidade_Refeicao=request.form['ID_Modalidade_Refeicao']
    modalidade=Modalidade_Refeicao(Modalidade, ID_Modalidade_Refeicao)
    modalidade_refeicao_dao.salvar(modalidade)

    flash('A modalidade foi editada com sucesso!')
    return redirect('/lista_modalidades_refeicoes')

#Função par atualizar Modalidades de Refeições
@app.route('/atualizar_ingrediente', methods=['POST',])
def atualizar_ingrediente():
    Descricao_Ingrediente=request.form['Descricao_Ingrediente']
    Quantidade_Ingrediente=request.form['Quantidade_Ingrediente']
    Unidade_Medida_Ingrediente=request.form['Unidade_Medida_Ingrediente']
    ID_Ingrediente=request.form['ID_Ingrediente']
    ingrediente=Ingrediente(Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente, ID_Ingrediente)
    ingrediente_dao.salvar(ingrediente)

    flash('O ingrediente foi editado com sucesso!')
    return redirect('/lista_ingredientes')

#Função par atualizar Local
@app.route('/atualizar_local', methods=['POST',])
def atualizar_local():
    Nome_RU=request.form['Nome_RU']
    Local_RU=request.form['Local_RU']
    ID_Local_RU=request.form['ID_Local_RU']
    local=Local(Nome_RU, Local_RU, ID_Local_RU)
    local_dao.salvar(local)

    flash('O local foi editado com sucesso!')
    return redirect('/lista_locais')

#Função par atualizar Dia
@app.route('/atualizar_dia', methods=['POST',])
def atualizar_dia():
    Data=request.form['Data']
    Dia_Semana=request.form['Dia_Semana']
    Precipitacao=request.form['Precipitacao']
    Umidade=request.form['Umidade']
    Vento=request.form['Vento']
    Temperatura=request.form['Temperatura']
    ID_Dia=request.form['ID_Dia']
    dia=Dia(Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura, ID_Dia)
    dia_dao.salvar(dia)

    flash('O dia foi editado com sucesso!')
    return redirect('/lista_dias')

#Função para atualizar categorias
@app.route('/atualizar_categorias', methods=['POST',])
def atualizar_categorias():
    Nome_Categoria=request.form['Nome_Categoria']
    ID_Categoria=request.form['ID_Categoria']
    categoria=Categoria(Nome_Categoria, ID_Categoria)
    categoria_dao.salvar(categoria)

    flash('A categoria foi editada com sucesso!')
    return redirect('/lista_categorias')

#Função para atualizar cardápios
@app.route('/atualizar_cardapios', methods=['POST',])
def atualizar_cardapios():
    Descricao=request.form['Descricao']
    ID_Cardapio=request.form['ID_Cardapio']
    cardapio=Cardapio(Descricao, ID_Cardapio)
    cardapio_dao.salvar(cardapio)

    flash('O cardápio foi editado com sucesso!')
    return redirect('/lista_cardapios')

#Função para atualizar refeições
@app.route('/atualizar_refeicoes', methods=['POST',])
def atualizar_refeicoes():
    Quantidade_por_pratos=request.form['Quantidade_por_pratos']
    ID_Refeicao=request.form['ID_Refeicao']
    refeicao=Refeicao(Quantidade_por_pratos, ID_Refeicao)
    refeicao_dao.salvar(refeicao)

    flash('A refeição foi editada com sucesso!')
    return redirect('/lista_refeicoes')

@app.route('/deletar/<int:ID_Alimento>')
def deletar(ID_Alimento):
    alimento_dao.deletar(ID_Alimento)

    flash('O alimento foi removido com sucesso!')
    return redirect('/lista_alimentos')

@app.route('/deletar_usuario/<string:id>')
def deletar_usuario(id):
    usuario_dao.deletar(id)

    flash('O usuário foi removido com sucesso!')
    return redirect('/lista_usuarios')

#Função para deletar eventos
@app.route('/deletar_evento/<int:ID_Eventos>')
def deletar_evento(ID_Eventos):
    evento_dao.deletar(ID_Eventos)

    flash('O evento foi removido com sucesso!')
    return redirect('/lista_eventos')

#Função para deletar modaliades
@app.route('/deletar_modalidades_refeicoes/<int:ID_Modalidade_Refeicao>')
def deletar_modalidades_refeicoes(ID_Modalidade_Refeicao):
    modalidade_refeicao_dao.deletar(ID_Modalidade_Refeicao)

    flash('A modalidade foi removida com sucesso!')
    return redirect('/lista_modalidades_refeicoes')

#Função para deletar ingredientes
@app.route('/deletar_ingrediente/<int:ID_Ingrediente>')
def deletar_ingrediente(ID_Ingrediente):
    ingrediente_dao.deletar(ID_Ingrediente)

    flash('O ingrediente foi removido com sucesso!')
    return redirect('/lista_ingredientes')

#Função para deletar locais
@app.route('/deletar_local/<int:ID_Local_RU>')
def deletar_local(ID_Local_RU):
    local_dao.deletar(ID_Local_RU)

    flash('O local foi removido com sucesso!')
    return redirect('/lista_locais')

#Função para deletar dias
@app.route('/deletar_dia/<int:ID_Dia>')
def deletar_dia(ID_Dia):
    dia_dao.deletar(ID_Dia)

    flash('O dia foi removido com sucesso!')
    return redirect('/lista_dias')

#Função para deletar categorias
@app.route('/deletar_categoria/<int:ID_Categoria>')
def deletar_categoria(ID_Categoria):
    categoria_dao.deletar(ID_Categoria)

    flash('A categoria foi removida com sucesso!')
    return redirect('/lista_categorias')

#Função para deletar cardapios
@app.route('/deletar_cardapio/<int:ID_Cardapio>')
def deletar_cardapio(ID_Cardapio):
    cardapio_dao.deletar(ID_Cardapio)

    flash('O cardápio foi removido com sucesso!')
    return redirect('/lista_cardapios')

#Função para deletar refeições
@app.route('/deletar_refeicao/<int:ID_Refeicao>')
def deletar_refeicao(ID_Refeicao):
    refeicao_dao.deletar(ID_Refeicao)

    flash('A refeição foi removida com sucesso!')
    return redirect('/lista_refeicoes')

'''@app.route('/uploads/<nome_arquivo>')
def upload_file(nome_arquivo):
    return send_from_directory(app.config['UPLOAD_PATH'], nome_arquivo)
'''

if __name__== '__main__':
    app.run(debug=True)


