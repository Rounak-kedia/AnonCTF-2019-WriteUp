from Crypto.Cipher import AES
from operator import xor
import binascii , sys

KEY_first = "8cG926f6#anon"
plain1 ="The message is e"
plain2 = "mbezzled by YOU!"

cipher1 = "3300000000000000000000000000f12e"
cipher2 = "bfa0d2bf4e53a55656b94734bb820a64"

def decrypt(cipher , passphrase):
	aes = AES.new(passphrase,AES.MODE_CBC,binascii.unhexlify(cipher1))
	return aes.decrypt(cipher)

for i in range(32,126):
	for j in range(32,126):
		for k in range(32,126):
			key = KEY_first + chr(i) + chr(j) + chr(k)
			dec_plain2 = decrypt(binascii.unhexlify(cipher2),key)
			if str(dec_plain2).startswith("m") and str(dec_plain2).endswith('U!'):
				print "decrypted plain2 :"  + dec_plain2 + " with key:" +key