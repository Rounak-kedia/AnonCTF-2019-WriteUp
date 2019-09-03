# AnonCTF_2019: DouBle Trouble

**Category:** Web

**Points:** 50

**Problem Statement:**

>Well, I'm proud of my web application. However, the experts are calling the effort lazy. They say that sensitive information 
>can be leaked out. I wonder....
>
>[My amazing web application ](https://anonctf.000webhostapp.com/DouBletrouble.php)

## Write-Up

This is an SQL injection problem

When the input is of the form <' or 1=1#> all the data in the current table is displayed

The last entry confirms the existence of a table named queer

Exploit the table queer as follows

Use the input <' union select * from queer#>

Flag : `anonCTF{5qL_InJecT3D}`
