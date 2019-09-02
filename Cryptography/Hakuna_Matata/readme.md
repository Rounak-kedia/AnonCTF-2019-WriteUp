# AnonCTF_2019: Hakuna Matata

**Category:** Cryptography
**Points:** 30


**Problem Statement:**
>Timon & Pumba wanted to convey an intel to Simba about the Scar's Plan to kill Mufasa but their intel has been intercepted by Shenzi-'The Hyena'.

>He blurred some important text in the image which are useful for decrypting the intel.
Assist Simba to find Scar's Plan.
>![image](https://s3.amazonaws.com/hr-assets/0/1565550733-ef3758c476-Capture.PNG)

## Write-Up

We are given a image where clearly AES CBC cipher has been implemented.In case you don't know what AES CBS is visit : <BR>
    - [AES read](AES_read)
  
 We are given only partial part of key and IV is hidden.<br>
 <h4>What do we know?</h4> 
 -key is <b>"8cG926f6#anonXXX"</b> i.e. 13 characters of 16 characters  and IV should be 16 bit long say   "XXXXXXXXXXXXXXXX".
 <br>
-The plaintext ("The message is embezzled by YOU!")<br>
-The complete second block and parts of the first ciphertext block.<br>



 <h5>Step 1: Get the AES key</h5>
 
 <p>We know the second ciphertext block, the plaintext and parts of the first block of ciphertext. Therefore we can brute force the key's last three characters by decrypting the second block of ciphertext with all possible keys, xoring with the first block of ciphertext (the unknown parts padded by zeros) and see, for which key the first letter and last three letters of the result match to the original plaintext.</P>

```python
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
```

>The output of the above snippet of code is -> decrypted plain2: ��U! with key:8cG926f6#anonCTF

<h5>Step 2: Get the first ciphertext block</h5>
Remember: After decrypting the block number n it will be xored with block number n-1 to produce the plaintext.
Scince xor is revertable a ⊕ b = c ⇔ c ⊕ b = a <br>
and we now know the key, we can simply change the role of the first cipher text block and second plaintext block and do AES decryption on the second ciphertext block with the second plaintext block as IV (instead of the first cipher text block), which leads to the first ciphertext block as "decrypted paintext".

```python
from Crypto.Cipher import AES
import binascii , sys

KEY="8cG926f6#anonCTF"
plain2 = "mbezzled by YOU!"
cipher2 = "bfa0d2bf4e53a55656b94734bb820a64"

def decrypt(cipher,passphrase):
	aes = AES.new(passphrase,AES.MODE_CBC,plain2)
	return aes.decrypt(cipher)

print "decrypted data:" + binascii.hexlify(decrypt(binascii.unhexlify(cipher2),KEY))
```
> Output : decrypted data:33e616929ba5a6ee8c8974338fbbf12e
 
<h5>Step 3 : Get the IV</h5>
We can do the trick with changing roles again:
This time we change the role of first plaintext block and IV when doing decryption on the first ciphertext block, which leads to the IV as decrypted plaintext.

```python
from Crypto.Cipher import AES
import binascii, sys

KEY="8cG926f6#anonCTF"
IV="The message is e"

cipher1="33e616929ba5a6ee8c8974338fbbf12e"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,IV)
    return aes.decrypt(cipher)

print "decrypted data: " + decrypt(binascii.unhexlify(cipher1), KEY)
```
> Output : decrypted data: {CBC_-B3_<<fuck>p00R<this>>}
  
The flag is hence , <b>anonCTF{CBC_-B3_<<fuck>p00R<this>>}</b>.
