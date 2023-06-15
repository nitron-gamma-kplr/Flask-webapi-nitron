from flask import Flask, jsonify, request, make_response
import psycopg2
​
app = Flask(__name__)
​
conn = psycopg2.connect(database="mibpkeop", user="mibpkeop", 
        password="u-diLaFGNx44lf9GTDT5nt1JCs5EkVsw", host="snuffleupagus.db.elephantsql.com", port="5432")
​
cur = conn.cursor()
​
cur.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, name VARCHAR(255), value INTEGER)")
​
# cur.execute("INSERT INTO data (name, value) VALUES ('donnée 1', 100), ('donnée 2', 200)")
​
conn.commit()
​
​
@app.route('/data', methods=['GET'])
def get_data():
    cur.execute("SELECT * FROM data")
    lignes = cur.fetchall()
    print(lignes)
    result = []
​
    for ligne in lignes:
        result.append({'id': ligne[0], 'name': ligne[1], 'value': ligne[2]})
    
    return jsonify(result)
​
@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    cur.execute("INSERT INTO data (name, value) VALUES (%s, %s)", (data['name'], data['value']))
    conn.commit()
​
    return jsonify({'message': "Data added successfully"})
​
@app.route('/data/<int:id>')
def get_data_by_id(id):
    cur.execute("SELECT * FROM data WHERE id=%s", (id,))
    ligne = cur.fetchone()
​
    if ligne:
        result = {'id': ligne[0], 'name': ligne[1], 'value': ligne[2]}
        return jsonify(result)
    else:
        return make_response(jsonify({'message': 'Not found'}), 404)
​
@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    try:
        cur.execute("UPDATE data SET name=%s, value=%s WHERE id=%s", (data['name'], data['value'], id))
        conn.commit()
        return jsonify({'message': 'Data updated successfully'})
    except:
        return jsonify({'message': 'Error'})
​
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur.execute("DELETE FROM data WHERE id=%s", (id,))
    conn.commit()
    return jsonify({'message': 'Data deleted successfully'})
​
​
​
app.run(debug=True)