from phe import paillier



public_key ,private_key = paillier.generate_paillier_keypair()



data = [100,200,60]
encrp_data = [public_key.encrypt(x) for x in data]

adding = encrp_data[0]+encrp_data[1]+encrp_data[2]

print("result after decrypting the encrypted data: ",end='')
print(private_key.decrypt(adding))