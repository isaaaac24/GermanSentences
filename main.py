import os

import sqlalchemy as db
from flask import Flask, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database
engine = db.create_engine('mysql://root:Password123_@localhost:3306/sentences')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# flask
app = Flask(__name__)

#establish secret key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# create database
# Base.metadata.create_all(engine)


@app.route('/')
def home():
    return render_template('home.html')


# main function, displays main menu
if __name__ == '__main__':
    from split.views import split_bp
    from search.views import search_bp

    app.register_blueprint(split_bp)
    app.register_blueprint(search_bp)
    app.run(debug=True)

