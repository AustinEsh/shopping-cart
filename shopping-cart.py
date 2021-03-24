from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

cart = []

@app.route('/', methods=["POST", "GET"])
def index():
   return render_template("index.html")

@app.route('/add', methods=["POST"])
def test():
   cart.append(request.form['item-name'])
   return render_template("index.html", cart = cart)

@app.route('/cart', methods=["POST"])
def go_to_cart():
   return render_template("cart.html", cart = cart)

@app.route('/clear', methods=["POST"])
def clear():
   global cart
   cart = []
   return render_template("index.html")

@app.route('/checkout', methods=["POST"])
def checkout():
   global cart
   cart = []
   return render_template("checkout.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if (request.form.get("nm1")):
      return redirect(url_for('success',name = 'Austin'))
   else:
      return redirect(url_for('test'))

if __name__ == '__main__':
   app.run(debug = True)