# Import de bibliothèques

import flask
from flask import request, jsonify
import psycopg2


# Création de l'objet Flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# Quelques données tests pour l’annuaire sous la forme d’une liste de dictionnaires

employees = [

{'id': 0,

'Nom': 'Dupont',

'Prénom': 'Jean',

'Fonction': 'Développeur',

'Ancienneté': '5'},

{'id': 1,

'Nom': 'Durand',

'Prénom': 'Elodie',

'Fonction': 'Directrice Commerciale',

'Ancienneté': '4'},

{'id': 2,

'Nom': 'Lucas',

'Prénom': 'Jérémie',

'Fonction': 'DRH',

'Ancienneté': '4'}

]

@app.route('/', methods=['GET'])
def home():

        return '''<h1>Annuaire Internet</h1>

<p>Ce site est le prototype d’une API mettant à disposition des données sur les employés d’une entreprise.</p>'''

@app.route('/api/v1/resources/employees/all', methods=['GET'])
def api_all():

        return jsonify(employees)

@app.route('/api/v1/resources/employees/<id>', methods=['GET'])
def api_id(id):
    # Vérifie si un ID est fourni dans une URL.
    if int(id)=="":
        return "pas bon !"
    # Si un ID est fourni, il est affecté à une variable.
    else:
        id_emp=int(id)
    # Si aucun ID n’est fourni, un message d’erreur est affiché dans le navigateur.
        
    # Crée une liste vide pour stocker les résultats
        empl=[]
        
    # Boucle sur les données pour obtenir les résultats correspondant à l’ID fourni.
        results=employees[id_emp]
        return jsonify(results) 

    # Les IDs sont uniques, mais les autres champs peuvent renvoyer plusieurs résultats
        

# La fonction jsonify de Flask convertit notre liste de dictionnaires Python

# au format JSON return jsonify(results)

app.run()