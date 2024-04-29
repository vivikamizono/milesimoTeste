from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('formulario.html')

@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    cargo = request.form['cargo']
    residencia = request.form['residencia']
    
    # Aqui você pode processar os dados do formulário como quiser
    # Por exemplo, você pode salvar os dados em um banco de dados
    
    return f'Dados recebidos: Nome: {nome}, CPF: {cpf}, RG: {rg}, Cargo: {cargo}, Residência: {residencia}'

if __name__ == '__main__':
    app.run(debug=True)
