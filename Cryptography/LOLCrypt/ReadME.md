# AnonCTF_2019: LOLCrypt

**Category:** Cryptography
**Points:** 30

**Problem Statement:**

>Elliot was recently selected as an Cyber Security Agent for the Department of Defence.He recently intercepted an encrypted transmission but could not decrypt it.Head <a href="https://lol-crypt.000webhostapp.com/" target="_blank">here</a> and see if you could help him decrypt the message.

## Write-Up

The link directs us to a page which gives the encryptor for Lolcrypt.
When we send a single letter `a` as input,it return 4 nos. `41 65 38 14` which is random each time.
Sending `aa` gives 8 random nos.

The sum of the 4 nos gives us 158 incase of 'a'
For 'b' it gives us 4 nos. that sum up to 157
If we Keep on repeating this we notice that the sum value decreases by 1 for every next letter.

Also if you be a little observant you notice that the sum is actually 255(i.e 0xff) - AscII of the letter sent
eg. for `a` ascii value is 97 then 255-97=158(sum)

Hence, the algorithm is simply taking a letter subtracting its ascii value from 255 and randomly splitting that no in 4.

Now, as we know how the algo works we can break the code using a simple [script](Solution.py) or you can solve it by hand.

The Flag is  `anonCTF{Cu5t0m_Cr7pt0_@r6_Fun}` 
