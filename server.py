from flask import Flask,request
import json



app = Flask(__name__)



@app.route('/getdata/',methods=['POST'])
def getdata():
    
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
    # Use the data here
    
    print(data)
    
    
    
    result = {"data" : data}
    return json.dumps(result)
    

if __name__ == "__main__":
    app.run(debug = True ,port=8000)