from Crypto.Cipher import AES
import binascii, sys

KEY="8cG926f6#anonCTF"
IV="The message is e"

cipher1="33e616929ba5a6ee8c8974338fbbf12e"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,IV)
    return aes.decrypt(cipher)

print "decrypted data: " + decrypt(binascii.unhexlify(cipher1), KEY)
