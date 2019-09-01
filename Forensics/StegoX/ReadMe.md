# AnonCTF_2019: StegoX

**Category:** Forensics

**Points:** 40

## Problem Statement:

>Looks like Thalaiva has something to say. "Naan oru thadave sonna nooru thadave sonna madhiri."
>
>Hint : odd number of 1's gives 1 else 0. Play around with network graphics.
>
>(Append final flag inside the usual format)

## Write-Up

Run strings on the pic.png filr to get the key : "not_here"

Convert the key into hex and XOR with the data in the question.txt file

Convert the hex into an image file to get a qr code

scan the qr code for the flag

Flag : `anonCTF{Y0ur_Br3atht4kinG}`
