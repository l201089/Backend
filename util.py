__locations=None
__data_columns=None
__model=None
import json
import pickle
import pandas as pd
import numpy as np

def predict_price(location, area, bedrooms, baths):
    # Load the saved model columns
    #model_columns = pickle.load(open('model_columns.pkl', 'rb'))
    with open("./artifacts/model_columns.pkl", 'rb') as f:
        model_columns = pickle.load(f)



    # Load the saved model
    #model = pickle.load(open('house_price_prediction_model.pkl', 'rb'))
    with open("./artifacts/house_price_prediction_model.pkl", 'rb') as f:
        model = pickle.load(f)
    # Create a new dataframe with the user input
    user_input = pd.DataFrame([[location, area, bedrooms, baths]],
                              columns=['location', 'area', 'bedrooms', 'bathrooms'])

    # Convert the user input to a one-hot encoded array
    user_input_encoded = pd.get_dummies(user_input, columns=['location'])

    # Align the columns of the user input with the model columns
    user_input_encoded = user_input_encoded.reindex(columns=model_columns, fill_value=0)

    # Make predictions using the model
    prediction = model.predict(user_input_encoded)

    # Return the prediction
    prediction[0]=prediction[0]+ 0.5* prediction[0]
    return prediction[0]


def get_location_names():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/model_columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/house_price_prediction_model.pkl", 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")
    print(__locations)
    return __locations


if __name__=="__main__":
   get_location_names()
   # predict_price('Bahria Town',1000, 4, 4)