from Crypto.Cipher import DES3   # this package crypto library has inbulit encryption.
from Crypto.Random import get_random_bytes   # importing a random ket possible.

# next thing is to generate a key.
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))  # 3 keys 24 bytes. key generated.
        break
    except ValueError:
        pass
print(type(key))  # class with attribute byte
# encrypting function
def encrypt(msg):    # takes plane text and returns the cipher text.
    cipher = DES3.new(key, DES3.MODE_EAX)  # creating cipher object. takes key and mode.  eax means
    nonce = cipher.nonce   # Nonce is the number which can be used only once
    ciphertext = cipher.encrypt(msg.encode('ascii')) # we now have the cipher text
    return nonce, ciphertext
# decrypting function
def decrypt(nonce, ciphertext):  # taking in constant or nonce and cipher text as parameeters
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)  # taking in key and mode.
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

nonce, ciphertext = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext)
print(f'Cipher text: {ciphertext}')
print(f'Plain text: {plaintext}')
