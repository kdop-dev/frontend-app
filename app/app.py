import os
from flask import render_template, request, send_file, abort, url_for
from flask import Flask
from flask_bootstrap import Bootstrap
import requests
import json
from pathlib import Path

app = Flask(__name__)
Bootstrap(app)

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/cert')
def cert():
    try:
        url = os.environ.get('URL_CERT')
        r=requests.get(url)
        if r.status_code == requests.codes.ok:
            return render_template('cert.html', title='Certificado')
        else:
            return render_template('erro.html', title='Erro')

    except Exception as e:
        return render_template('erro.html', title='Erro')


@app.route('/get', methods=["POST"])
def get():
    yourname=request.form.get("yourname")
    return send_file(f'/tmp/inovacao/front-app/{yourname}-cert.pdf', as_attachment=True)

@app.route('/end', methods=["POST"])
def end():
    try:
        yourname=request.form.get("yourname")

        filename = Path(f'/tmp/inovacao/front-app/{yourname}-cert.pdf')        

        url = f"{os.environ.get('URL_CERT')}get-cert?p={yourname}"
        response=requests.get(url)
        filename.write_bytes(response.content)

        return render_template('end.html', title='End', yourname=yourname)

    except FileNotFoundError:
        abort(404)

@app.route('/cadastro', methods=["POST"])
def cadastro():
    try:
        obj = {
            'nome' : request.form.get("name"),
            'email' : request.form.get("email")
        }

        url = f"{os.environ.get('URL_BACK')}insert"
        response=requests.post(url, data = obj)
        alunos=json.loads(response.text)['aluno']

        return render_template('cadastro.html', title='Home', alunos=alunos)

    except FileNotFoundError:
        abort(404)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

# @app.route('/backhealth')
# def backhealth():
#     url = f"{os.environ.get('URL_BACK')}health"
#     response=requests.get(url)
#     return render_template(response.content)

@app.route("/health")
def health():
    try:
        url = f"{os.environ.get('URL_BACK')}health"
        response=requests.get(url)
        return f"Front-app in ns {os.environ.get('ambiente')}: Ok!"
    except FileNotFoundError:
        abort(404)

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)