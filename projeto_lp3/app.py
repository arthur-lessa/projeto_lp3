from flask import Flask, render_template, request 

lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Mata a sede"},
        {"nome": "Doritos", "descricao": "Suja a mão"},
        {"nome": "Chocolate", "descricao": "Bom"}
    ]

# template = arquivo HTML passado

app = Flask("__name__")

# rota + função

# GET /produtos/cadastro devolver o form
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

# POST /produtos que vai lidar com os dados enviados pelo form
# acessar o objeto request
@app.route("/produtos", methods=['POST'])
def salvar_produtos():
    # pegando os valores digitados no form
    # que estão no request    
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    
    # crio um novo produto (novo dict)
    produto = { "nome" : nome, "descricao" : descricao, "imagem" : "" }
    
    # adiciona o novo produto na lista
    lista_produtos.append(produto)
    
    # devolvo o template COM o novo produto
    return render_template("produtos.html", produtos = lista_produtos)


# / - home page
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# /produtos - página com alguns produtos
@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos)

    