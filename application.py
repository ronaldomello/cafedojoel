
#Render_template é uma função flask do Python. É uasda para gerar uma saída a partir de um arquivo modelo do aplicativo.

from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def main():
 	return render_template('index.html')
