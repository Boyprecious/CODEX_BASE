import string
import CEASER
import qrcode


plain_text = input(CEASER.type_effect("enter message with letters only:", 0.1))
shifted_key = 7
sh = shifted_key
shifted_key = shifted_key % 26

alphabet = string.ascii_lowercase

shifted = alphabet[shifted_key:] + alphabet[:shifted_key]

table = str.maketrans(alphabet, shifted)

encrypted_message = plain_text.translate(table)

print(CEASER.type_effect("encryption is :", 0.1))
print(CEASER.type_effect(encrypted_message, 0.1))

print(CEASER.type_effect("generating qr code", 0.1))

image = qrcode.make(encrypted_message)
image.save('code.png')
image.show('code.png')




# print("now decrypting message after encryption")



# shift_decrypt = 26 - sh

# shift_decrypt = shift_decrypt % 26

# alphabet = string.ascii_lowercase

# shifted_new = alphabet[shift_decrypt:] + alphabet[:shift_decrypt]

# table = str.maketrans(alphabet, shifted_new)

# decrypted_message = encrypted_message.translate(table)

# print(decrypted_message)