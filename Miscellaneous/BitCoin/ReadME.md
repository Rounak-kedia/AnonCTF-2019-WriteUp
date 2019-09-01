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

Write a [Script](Script.py) to find nonce by putting values for nonce encrypting the string with sha256 and checking with the signature given.
The nonce for which the signature matches is the flag.

The Flag is `anonCTF{24343504}`
