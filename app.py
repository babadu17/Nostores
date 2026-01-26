from flask import *
import os

app = Flask(__name__)
app.secret_key = "une_cle_secrete"

@app.route('/')
def index():
  return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
