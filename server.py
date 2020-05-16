from flask import Flask,request
import json
from phe import paillier


app = Flask(__name__)

public_key ,private_key = paillier.generate_paillier_keypair()


@app.route('/getdata/',methods=['POST'])
def getdata():
    
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
    # Use the data here
    
    print(data)
    encrp_data1 = [public_key.encrypt(x) for x in data['value1']]

    encrp_data2 = [public_key.encrypt(x) for x in data['value2']]

    adding = encrp_data1+encrp_data2
    
    
    result = {"data" : adding}
    return json.dumps(result)
    

if __name__ == "__main__":
    app.run(debug = True ,port=8000)