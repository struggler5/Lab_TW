from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def Transactions():

    return render_template("Transactions.html")

@app.route('/DB')
def DB():
    return render_template("DB.html")

@app.route('/DB/item')
def DB_item():
    return render_template("DB_item.html")

@app.route('/Stock')
def Stock():
    return render_template("Stock.html")

@app.route('/Stock/item')
def Stock_item():
    return render_template("Stock_item.html")
app.run(debug=True, host="0.0.0.0", port=5000)
