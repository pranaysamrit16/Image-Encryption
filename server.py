import socket
import des
import base64


def Main():
    host = "127.0.0.1"
    port = 5000
    #    
    K = '133457799BBCDFF1'
    imageReceived = "imagesReceived/image_1.jpg"
    #
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    
    rec_data = ""
    
    while True:
            data = conn.recv(1024).decode()
            rec_data = rec_data + data
            if not data:
                    break
             
            #data = str(data).upper()
            #print ("sending: " + str(data))
            #conn.send(data.encode())
             
    print ("from connected  user: Data received")
    #print(len(rec_data))
    rec_img = rec_data[0:len(rec_data)-2]
    pad=rec_data[len(rec_data)-2:]
    pad_len = int(pad)
    #print(rec_img)
    #print(pad)
    
    
    #
    rec_img_dec=""
    for i in range(0,len(rec_img),16):
        rec_img_dec = rec_img_dec + des.decrypt(rec_img[i:i+16],K)

    rec_img_bin=bin(int(rec_img_dec, 16))[2:].zfill(len(rec_img_dec)*4)
   
    rec_img_bin = rec_img_bin[0:-pad_len]

    rec_img_byte = ""
    for i in range(0,len(rec_img_bin),7):
        rec_img_byte += chr(int((rec_img_bin[i:i+7]),2))   

    rec_img_byte_utf = rec_img_byte.encode("utf-8")

    image_data = rec_img_byte_utf
    fh = open(imageReceived, "wb")
    fh.write(base64.decodebytes(image_data))
    fh.close()
    
    
    #
    conn.close()
     
if __name__ == '__main__':
    Main()
