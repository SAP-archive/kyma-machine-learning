#import the packages your need for your model
import pickle
import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request

# Load the trained model from your working directory
with open('rf.pkl', 'rb') as model_pickle:
    rf = pickle.load(model_pickle)

# Initialise the flask app
app = Flask(__name__)

# start the app route for the predictions
@app.route('/predict')
def predict_bl():
    # First, we transform the data out of the Get request
    #class of the transaction 
    c = request.args.get('c')
    #amount of the transaction
    a = request.args.get('a')
    #old balance of the origin account before the transaction
    obo = request.args.get('obo')
    #new balance of the origin account after the transaction
    nbo = request.args.get('nbo')
    #old balance of the destination account after the transaction
    obd = request.args.get('obd')
    #new balance of the destination account after the transaction
    nbd = request.args.get('nbd')
    #created feature of the destination variable classifiying different destination accounts
    dl = request.args.get('dl')

    #combine the data
    observation = np.array([[c, a, obo, nbo, obd, nbd, dl]])
    #create prediction for the new observation
    prediction = rf.predict(observation)
    
    # return the result back
    return 'The predicted result for the observation ' + str(observation) + ' is: ' + str(prediction)

#run the app on local host and port 8001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
