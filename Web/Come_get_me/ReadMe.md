# AnonCTF_2019: Come get me

Category: Web
Points: 20

Problem Statement:

>John Doe has created a website. Like always he has only left the clues behind for the flag. Help Detective Mills get the 
>flag.
>
>[Start here](http://anonctf.000webhostapp.com/comeGetMe.php)

## Write-Up

All hints in the question point to a variable called flag in the backend php code being false by default

Change the variable flag to true as follows

url/?flag=true

Flag : `anonCTF{8oOLEAn_Fl4G}`
