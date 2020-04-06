def encrypt(data):
    encrypt_data=""
    for char in data:
        encrypt_data+=chr(ord(char)+5)
    return  encrypt_data

def dencrypt(data):
    dencrypt_data=""
    for char in data:
        dencrypt_data+=chr(ord(char)-5)
    return dencrypt_data

