from flask import Flask,request
import time
import json



app = Flask(__name__)

def adding(data):
    return data[0]['value1']+data[0]['value2']


@app.route('/getdata/',methods=['POST'])
def getdata():
    
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
    # Use the data here
    print(data)

    start = time.process_time()

    answer = adding(data)
    
    time_taken = time.process_time() - start
    
    print(time_taken)

    result = {"result" : answer , "time_taken" : time_taken}
    return json.dumps(result)
    

if __name__ == "__main__":
    app.run(debug = True ,port=8000)