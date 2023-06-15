from sqlalchemy import create_engine, text
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import (Flask, redirect,url_for, render_template, request)
import jsonify


url="postgresql+psycopg2://leiceswo:uToAdZce6aBxkF62X-EfwXudPDRM0F2U@horton.db.elephantsql.com/leiceswo"
engine=create_engine(url)
Session = sessionmaker(bind = engine)
session=Session()

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
#@login_required
def index():
    result=session.execute(text("SELECT * FROM api_sold"))
    results=result.fetchall()
    session.commit()
    return render_template("index.html", message = results)
    

@app.route('/delete/<int:id>')
#@login_required
def delete(id):
    result=session.execute(text("DELETE FROM api_sold WHERE id="+str(id)))
    session.commit()
    result_back=session.execute(text("SELECT * FROM api_sold WHERE id="+str(id)))
    results=result_back.fetchall()
    print(results)
    if results :
        return render_template("index.html", message = "The id= "+str(id)+" has been deleted")
    else :
        return render_template("index.html", message = "The id= "+str(id)+" n'a pas pu être supprimé")

app.run()