# Image-Encryption
This module enable us send image in DES-encrypted form in server client network

This module lets one user send image to other user in encrypted form. Other user receives encrypted image and decrypt it using shared key and DES algorithm

## Working
1. des.py has encrypt() and decrypt() function which encrypt and decrypt given hexadecimal data.
2. On client side image is convert to binary form and then encrypted using DES.
3. This encrypted data is sent to server using Socket programming
4. On server side encrypted data is received.
5. Received data is decrypted and then converted to binary form.
6. Binary data converted to Byte form and then finally converted to Image file.
7. We can see that image received on server matched exactly to image sent by client.

## Steps
#### On Server-Side
1. Choose K as key for encryption and decryption, share this key with Client.
2. Choose location where received image will be stored
3. Input host as ip address of server.
4. Run server.py and wait for response from client

#### On Client-Side
1. Input key K as same as server K
2. input host as ip address(LAN) of server 
3. Choose location of image to be sent.
4. Run client.py and image will be sent to server in encrypted form

### Encryption
DES is implemented from scrach

Language used: Python3

des.py file contain encrypt() and decrypt() functions which encrypt and decrypt given hexadecimal input and key.

### Server Client 
Server-Client structure enables us to send/receive data between both parties.

Socket Programming is used to achieve Server-Client Structure.
