# AnonCTF_2019: Roman Meets Italian

**Category:** Cryptography
**Points:** 20

**Problem Statement:**

>A Roman Dictator (Who was fixated with the day he died) gives a flag which he has specially encoded to a particular Italian Cryptologist who, on top of the encoded flag, placed a spell using a golden key. Then he hands it back to the Roman dictator, who again encodes it. This exchage happens 7 times and you are given the result of this process:
>
>F -> R -> I -> R -> I -> R -> I -> R -> I -> R -> I -> R -> I -> R -> I -> Y
>F - Flag
>R - Roman Dictator
>I - Italian Cryptologist
>Y - You
>
>riojFHW{xAaVoIqIchb}

## Write-Up

The Roman refers to Caesar Cipher with shift = 15 (Date of Julius Caesar's Death)
The Italian refers to Vigenere Cipher (With key = golden)
The flag can be obtained by decryption of Vigenere and Caesar ciphers alternately, 7 times.

Flag: `anonCTF{cAeSaRvIgen}`
