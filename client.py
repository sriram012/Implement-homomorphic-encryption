import sys
import json
import requests
from phe import paillier
value1=[1,2,3,4,5,6]
value2=[1,2,3,4,5,6]

public_key ,private_key = paillier.generate_paillier_keypair()

no_of_requests = 10

avg_time = 0

for i in range(0,10):
    encrp_data1 = [public_key.encrypt(x) for x in value1]
    encrp_data2 = [public_key.encrypt(x) for x in value2]

    conv = [{'value1': 1,'value2':2}]

    s = json.dumps(conv)
    res = requests.post("http://127.0.0.1:8000/getdata/", json=s).json()
    
    avg_time= (avg_time+res["time_taken"])/2
    print(res['result'] , res["time_taken"])

print("Avg Time Taken : " + str(avg_time))