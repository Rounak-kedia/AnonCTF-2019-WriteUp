from Crypto.Cipher import AES
import binascii, sys

KEY="9aF738g9AkI112#g"
IV="The message is p"

cipher1="9e128e7bc9ab9cc9d8b13ec77389436a"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,IV)
    return aes.decrypt(cipher)

print "decrypted data: " + binascii.hexlify(decrypt(binascii.unhexlify(cipher1), KEY))
