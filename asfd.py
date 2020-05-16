import sys
import json
import requests

from phe import paillier
from phe.paillier import PaillierPublicKey, EncryptedNumber

value1 = 1
value2 = 2

public_key ,private_key = paillier.generate_paillier_keypair()

encrp_data1 = public_key.encrypt(value1)
encrp_data2 = public_key.encrypt(value2)

data = {
	'n': public_key.n,
	'cipher_texts': [
						encrp_data1.ciphertext(),
						encrp_data2.ciphertext()
					]}

jsonData = json.dumps(data)
# sending request
res = requests.post("http://127.0.0.1:8000/getdata/", json=jsonData).json()

# evaluating response
sum_cipher_text = EncryptedNumber(public_key, res['sum_cipher_text'])
ret_value = private_key.decrypt(sum_cipher_text)

print(
	"Sum of "
	+ str(value1)
	+ " and "
	+ str(value2)
	+ " is "
	+ str(ret_value)
)
