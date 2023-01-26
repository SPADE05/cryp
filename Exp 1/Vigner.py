def vigenere(key, message):
    message = message.lower()
    message = message.replace(' ','')
    m = len(key)  
    cipher_text = ''
    
    for i in range(len(message)):
        letter = message[i]
        k= key[i % m] 
        cipher_text = cipher_text + chr ((ord(letter) - 97 + k ) % 26 + 97)

    return cipher_text

if __name__=='__main__':

    print ('Encripting')
    key = 'key'

    key = [ord(letter)-97 for letter in key]
    print("Key", key)
		

    cipher_text = vigenere(key, 'hello')
    print ('cipher text: ',cipher_text)
    
    print ('Decrypting')
    key = [-1*k for k in key]
    plain_text =  vigenere(key, cipher_text)
    print ('Plain text: ', plain_text)