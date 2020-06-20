# Image-Encryption
This codes enable us send image in DES-encrypted form in server client network

This module lets one user send image to other user in encrypted form. Other user receives encrypted image and decrypt it using shared key and DES algorithm

## Working


### Encryption
DES is implemented from scrach

Language used: Python3

des.py file contain encrypt() and decrypt() functions which encrypt and decrypt given hexadecimal input and key.

### Server Client 
Server-Client structure enables us to send/receive data between both parties.

Socket Programming is used to achieve Server-Client Structure.
