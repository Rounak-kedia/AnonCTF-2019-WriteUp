# AnonCTF_2019: Square

**Category:** Miscellanous
**Points:** 20

**Problem Statement:**

>Arya and Sansa argued for hours over whether a square can be called a rectangle or not. Sansa stressed that "a square is a square not a rectangle" but Arya insisted "every square is a rectangle". They couldn't find a common ground on the rectangle part of the debate. But both agreed to one thing that "It's a Square".

## Write-Up

The File given was actually a zip file(found by using file/binwalk command on linux,for windows you can check using a online site called [Check File type](http://checkfiletype.com/))

Extracting the file gives us another file which again has its extension changed.
Extracting that gives us another file which also has its extension changed.
Extracting that gives us a Folder `This is Secret` which contains 400 .mp4 files.
Actually all these files are png files.
So we need to change the extension of all these.
We can do it by writing a Script on Linux or,by using a tool found [here](https://www.advancedrenamer.com/download)

After doing that we observe that these images have been spiltted from a bigger image into smaller parts.

Also in the question it was mentioned that `its a square` which was a hint to indicate that the final image is a square(20*20=400).
We can join the images using image magick or an online [tool](https://www.filesmerge.com/merge-images).
But this tool takes a limited no of image files at time.
So we upload 80 images at time,we merge them horizontally with a column limit of 20.
We do this 5 times to get all the five parts.(The Website stores cookies which limit us to 2 free uses.Simply clear cookies to continue)

Now we merge those 5 images vertically and obtain the original image which is a `Qr Code`
Scan it and download the file(Secret.png) it directs to.

This file also has its extension changed.
Its a .wav file

Which on playing seems like a morse audio.
Decrypt it using [Morse Audio Decryptor](https://morsecode.scphillips.com/labs/audio-decoder-adaptive/)

The message was `EXTEN510N5AREL1E5`
Append the flag to the flag format.

The Flag is `anonCTF{EXTEN510N5AREL1E5}`
