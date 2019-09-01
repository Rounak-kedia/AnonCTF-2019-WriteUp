# AnonCTF_2019: Lost in the server

**Category:** Web

**Points:** 50

## Problem Statement:

>After a trip to the server with her pets, Coco found one of them to be missing. She doesn't exactly remember which one it is. 
>
>Can you help her?
>
>[Start here](https://anonctf.000webhostapp.com/)

## Write-Up

This is an enumeration question 

The needed operation is url/animal_name where animal_name is the name of an animal given in the animals.txt file

use tools like wfuzz or dirb to launch a dictionary attack on the given url with the animals.txt file

Flag : `anonCTF{PE7_det3cTiVe}`
