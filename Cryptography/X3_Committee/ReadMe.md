# AnonCTF_2019: X3 Committee

**Category:** Cryptography
**Points:** 20

**Problem Statement:**

>The X3 Committee (1963) had two members, Jack & Jill. Jack loved his letters simple and plain, while Jill loved to transform her letters. They had a habit of taking turns while playing with words.
>But soon enough they got bored of this and decided to transmute the word completely after playing with it. You are currently in a hurry to get the flag from them, but they being in a playful mood give you the transformed flag in a locked zip file along with this: 
>
>34087fda8b254d4947fb551a9b76f52d3cd37e90

## Write-Up

Decrypt given SHA-1 string to unlock the zip. In the zip, there is a document with the encrypted flag.
Every alternate character is in its ASCII equivalent. By reversing it, we get the flag.

Flag: `anonCTF{AscIiCryptO}`
