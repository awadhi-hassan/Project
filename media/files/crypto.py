from cryptography.fernet import Fernet

with open('key', 'rb') as key:
    key = key.read()

frt = Fernet(key)
def encrypt():
    with open('manage.py', 'rb') as file:
        data = file.read()
    enc_data = frt.encrypt(data)
    with open('manage.py', 'wb') as file:
        file.write(enc_data)
#encrypt()
def decrypt():
    with open('manage.py', 'rb') as f:
        enc_data = f.read()

    dec_data = frt.decrypt(enc_data)
    with open('manage.py', 'wb') as f:
        f.write(dec_data)
decrypt()