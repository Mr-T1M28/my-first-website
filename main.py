from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
  return render_template("homepage.html")

@app.route('/buy/<name>/<price>')
def buy(name, price):
  return render_template("buyingpage.html", name=name, price=price)

if __name__ == "__main__":
  app.run(debug=True, port=7000)
