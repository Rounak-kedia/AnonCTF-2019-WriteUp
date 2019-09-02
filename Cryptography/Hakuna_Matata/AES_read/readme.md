<H2>What is AES?</H2>
<p>AES (Advanced Encryption Standard), also known as Rijndael cipher, is a block cipher for symmetric cryptography.
For this challenge we do not need to understand how AES itself works, there happens a lot of math magic with substitutions and permutations. If you are interested in the details, have a look at <A href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">wikipedia</A>.</p>

<H2>What is CBC, what is an IV?</H2>
<p>Cipher Block Chaining (CBC) is a mode of operation for AES.
The plaintext and ciphertext are divide into blocks of a defined length (remember: AES is a block cipher). Before encrypting the plaintext block number n with AES, it becomes xored with the ciphertext block n-1. Because the first plaintext block has no cipher text befor itself to xor with, there is an initialisation vector (IV) for this</p>

> ![Attached Image](CBC_encryption..png)

