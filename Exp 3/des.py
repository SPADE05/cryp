# pip3 uninstall crypto 
# pip3 uninstall pycrypto 
# pip3 install pycryptodome

# python3 -m venv .venv
# source .venv/bin/activate

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

key=get_random_bytes(8)
plaintext = b"Hello"

cipher = DES.new(key,DES.MODE_CBC)
ciphertext= cipher.encrypt(pad(plaintext,DES.block_size))

print(ciphertext)

cipher_decrypt = DES.new(key,DES.MODE_CBC,iv=cipher.iv)

print(unpad(cipher_decrypt.decrypt(ciphertext),DES.block_size).decode('utf-8'))