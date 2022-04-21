import numpy as np
from flask import Flask, request,jsonify,make_response
import sklearn
import numpy
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('P3.pkl', 'rb'))
model1 = pickle.load(open('P4.pkl', 'rb'))

# Opening JSON file
#f = open("data.json")

# returns JSON object as
# a dictionary



@app.route('/json',methods=['POST'])
def json():
    # if request.method == 'POST':
    data = request.get_json()
    RC=float(data['RC'])
    LLP=float(data['LLP'])
    LM=float(data['LM'])
    LSDO=float(data['LSDO'])
    LSDT=float(data['LSDT'])
    LSDTH=float(data['LSDTH'])
    LSDF=float(data['LSDF'])
    LSDFI=float(data['LSDFI'])
    NDI=float(data['NDI'])
    IFW=float(data['IFW'])
    UB=float(data['UB'])
    #print(data['IFW'])
    array = np.array([[RC, LLP, LM, LSDO, LSDT, LSDTH, LSDF, LSDFI, NDI, IFW, UB]])
    pre=model.predict(array)
    fpre=int(pre)
    array1 = np.array([[RC, LLP, LM, LSDO, LSDT, LSDTH, LSDF, LSDFI, NDI, IFW, UB,fpre]])
    pre1 = model1.predict(array1)
    fpre1 = int(pre1)
    jpre={'pre':fpre,'pre1':fpre1}
    print(pre)
    r = make_response(jpre)
    r.mimetype = 'application/json'
    return r


if __name__=='__main__':
    app.run(debug=True)

