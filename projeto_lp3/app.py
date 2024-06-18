from flask import Flask, render_template 

# template = arquivo HTML passado

app = Flask("__name__")

# rota + função

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
    lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Mata a sede"},
        {"nome": "Doritos", "descricao": "Suja a mão"},
        {"nome": "Chocolate", "descricao": "Bom"}


    ]

    return render_template("produtos.html", produtos = lista_produtos)




