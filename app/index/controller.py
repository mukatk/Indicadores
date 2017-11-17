from flask import Blueprint, render_template, jsonify, request
from .model import Indicador, db_indicador
import csv
import os

root_page = Blueprint(
	'root_page', 
	__name__, 
	template_folder='templates', 
	static_folder='static',
	static_url_path='/%s' % __name__
)

@root_page.route('/')
def index():
	return render_template('index.html')

@root_page.route('/BuscaIndicadores')
def buscaIndicadores():
    db = db_indicador()
    indicadores = db.busca_indicadores()
    return jsonify(result=[e.serialize() for e in indicadores])

@root_page.route('/AtualizaIndicador', methods=["POST"])
def atualizaIndicador():
    try:
        jsonObj = request.get_json()
        db = db_indicador()
        db.atualiza_indicador(int(jsonObj["Id"]), int(jsonObj["Porcentagem"]))
        return 'Registro atualizado com sucesso'
    except:
        return 'Erro ao atualizar'