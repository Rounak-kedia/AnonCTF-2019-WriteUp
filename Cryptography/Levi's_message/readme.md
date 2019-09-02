# AnonCTF_2019: Levi's Message

**Category:** Cryptography
**Points:** 50

**Problem Statement:**

>To intercept his message from the titans,Levi encrypted the message by using RSA algorithm to send it to Reckon Corps.
><p>Levi's very clever but Eren is not!</p>
><p>Eren recieved the message but didn't understand a thing!Can you help Eren decrypt the message?</p>

<A href="https://drive.google.com/open?id=1XF7suMTDKOpM59NEGVKNxDYh3Kx2W1Ut">Beast Titan</A>

## Write-Up
used the same value for d three times? can we calculate p's and q's from this? assume e=65537? bruteforceable? maybe a math problem? Those values are all interrelated, set of linear equations?<br>

what we know about RSA:<br>

>->A public key is composed of the pair (N,e) - the modulus N and the public exponent e<br>
>->A private key is composed of the pair (N,d) - the modulus N and the private exponent d<br>
>->Decrypting a ciphertext is taking the integer value of a ciphertext to the private exponent and applying modulo N to it - c^d mod N = m<br>
>->Encrypting a message is taking the integer value of a message to the public exponent and applying modulo N to it - m^e mod N = c<br>
>->A modulus N is composed of a multiplication of two (large) prime numbers p and q<br>
>->This multiplication is a trapdoor - easy in one way (multiplication), difficult in the other (factoring)<br>
>->The totien phi(N) can be calculated as follows: phi(N) = phi(p*q) = (p-1)*(q-1)<br>
>->The public exponent e is chosen in the range [3,phi(N)[, often 65537 as it is in this case<br>
>->The private exponent d is calculated using the phi(N) modular multiplicative inverse of e so that e*d = 1 mod phi(N)<br>
>->Private components are therefore p, q, d and phi(N)<br>
>->Public components are therefore e and N<br>

One can write a python script for the <b>chinese remainder theorem</b></br> to find the orignal message in less time.
>The orignal message is: https://anonctfsare-cool.000webhostapp.com/

Visit the site to get the flag as :<br>
<b>anonCTF{R$4-!s>>>NoT_ea5y}</b>
