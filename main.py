from pickle import GET

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',pageTitle='Ailen\'s Products' )

@app.route('/market', methods=['GET', 'POST'])
def market_page():
    items= Item.query.all()

    if request.method == "POST":
        product_name = request.form['name']
        new_product = Item(name=product_name)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect('/market')
        except:
            return "There was an error adding your product"

    else:
            return render_template('market.html',items=items)



