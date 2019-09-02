from Crypto.Cipher import AES
import binascii , sys

KEY="8cG926f6#anonCTF"
plain2 = "mbezzled by YOU!"
cipher2 = "bfa0d2bf4e53a55656b94734bb820a64"

def decrypt(cipher,passphrase):
	aes = AES.new(passphrase,AES.MODE_CBC,plain2)
	return aes.decrypt(cipher)

print "decrypted data:" + binascii.hexlify(decrypt(binascii.unhexlify(cipher2),KEY))