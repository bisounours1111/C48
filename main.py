from flask import *
from data import Data

app = Flask(__name__)

@app.route('/')
def index():
    data = DATA.get_all_collections()
    return render_template('index.html', data=data, base_url='collection')

@app.route('/collection/<collection>/<file>')
def collection(collection, file):
    data = DATA.get_file(collection, file)
    records = data.get("records", [])
    
    if records:
        keys = list(records[0].keys())
    else:
        keys = []

    return render_template("collection.html", keys=keys, records=records)

if __name__ == '__main__':
    DATA = Data()
    app.run(debug=True, port=5000, host='0.0.0.0')
