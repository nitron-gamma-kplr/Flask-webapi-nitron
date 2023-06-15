import flask
from flask import request, jsonify
import psycopg2



app = flask.Flask(__name__)
app.config["DEBUG"] = True

print('Connecting to the PostgreSQL database...')
DB_host='horton.db.elephantsql.com'
DB_name='leiceswo'
DB_user='leiceswo'
DB_pass='uToAdZce6aBxkF62X-EfwXudPDRM0F2U'

conn=psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_pass,host=DB_host)
cur=conn.cursor()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Annuaire des employés</h1>
<p>Prototype d'une API d'accès à la table employees de la base de données.</p>'''


@app.route('/all', methods=['GET'])
def api_all():
    all_employees = cur.execute('SELECT * FROM data')
    all_employees = cur.fetchall()
    return jsonify(all_employees)


@app.route('/select', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    value = query_parameters.get('value')

    query = "SELECT * FROM data WHERE"
    to_filter = []

    if id:
        query += " id='%s'" %id
        to_filter.append(id)
    if name:
        query += " name='%s'" %name
        to_filter.append(name)
    if value:
        query += " value='%s'" %value
        to_filter.append(value)
    if not (id or name or value):
        return page_not_found(404)

    query = query[:] + ';'

    cur = conn.cursor()
    results = cur.execute(query, to_filter)
    results = cur.fetchall()
    return jsonify(results)


@app.route('/insert', methods=['POST'])
def api_insert():

    data = request.get_json()
    cur.execute("INSERT INTO data (id, name, value) VALUES (%s, %s, %s)", (data['id'],data['name'],data['value']))
    conn.commit()
   

    chaine="SELECT * FROM data WHERE id="+ str(data['id']) + " AND name='" + data['name'] + "' AND value='"+ data['value']+"'"
    print(chaine)
    cur.execute(chaine)
        
    if cur.fetchall():
        return "tout est OK"
    else:
        return "ca n'a pas marché"
    
         
app.run()
