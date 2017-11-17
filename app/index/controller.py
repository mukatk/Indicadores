from flask import Blueprint, render_template, jsonify
from .model import Indicador
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
    indicadores = []
    with open(os.path.abspath('indicadores.csv'), 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            indicadores.append(Indicador(row["Nome"], row["Porcentagem"], row["Peso"]))
    return jsonify(result=[e.serialize() for e in indicadores])