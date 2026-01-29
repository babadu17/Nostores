from flask import *
import os

app = Flask(__name__)
app.secret_key = "une_cle_secrete"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/Stores-bannes')
def stores_bannes():
  return render_template("Stores-bannes.html")

@app.route('/Savanna')
def savanna():
  return render_template("Savanna.html")
  
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
