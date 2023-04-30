from flask import Flask , request, jsonify
from flask_cors import CORS
import util

app=Flask(__name__)
CORS(app)


@app.route('/hello')
def hello():
    return "hi"

#my locations are in model_columns.pkl so take all locations from there
@app.route('/locations', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    location = request.form['location']
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    baths = int(request.form['baths'])

    response = jsonify({
        'estimated_price': util.predict_price(location, area, bedrooms, baths)
    })

    return response


if __name__=="__main__":
    print("starting flask")
    app.run()


