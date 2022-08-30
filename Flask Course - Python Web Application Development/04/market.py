from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Kolczyk', 'barcode': '893212299897', 'price': 699},
        {'id': 2, 'name': 'Wino', 'barcode': '123985473165', 'price': 89},
        {'id': 3, 'name': 'Poduszka', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)