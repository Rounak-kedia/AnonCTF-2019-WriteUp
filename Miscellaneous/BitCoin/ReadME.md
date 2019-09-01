# AnonCTF_2019: BitCoin

**Category:** Miscellanous
**Points:** 20

**Problem Statement:**

>Tom and Jerry heard about the Crypto Currency BitCoin and its working and decided to move thier transactions to bitcoin. They created bitcoin addresses using WarpWallet and initiated a transaction. See if you could mine anything from this.
>
>Signature
>
>140065074eb29313700aa51bbfa2b535ddf126f8d00a1b211f64ea3578323336

# Write-Up

For getting the signatures for Tom and Jerry,use `WarpWallet` and use the public keys as sender and reciever signature.
Then only one unknown is left i.e nonce

Write a Script to find nonce by putting values for nonce encrypting the string with sha256 and checking with the signature given.
The nonce for which the signature matches is the flag.

>import hashlib<br/>
>
>for i in range(20000000,30000000):<br/>
> block="transaction_id:12\nreceiver_name:Jerry\nreceiver_key:17vt9QWGp59WkAGDMUHmSJpsCDowmhZeg5\nsender_name:Tom\nsender_key:1EkBXkf5BGCvLdFjNHQjZYz7XUhdmPdv2u\ntransaction_amount:10000\ntime_stamp:1536483609\ntransaction_signature:02487a9974eff50f5153c7511bc6331059e0e8f41926e0fe56680723125a675d\nnonce:"+str(i)"
> <br/>block1=block.encode('utf-8')<br/>
> sha=hashlib.sha256(block1).hexdigest()<br/>
> print(i)<br/>
> if sha =="140065074eb29313700aa51bbfa2b535ddf126f8d00a1b211f64ea3578323336":<br/>
>   print(block)<br/>
>   break

The Flag is `anonCTF{24343504}`
