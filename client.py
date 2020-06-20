import socket
import image
 


def Main():
        host = '192.168.10.36'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        pad = image.pad_export
        message = image.img_enc+pad
        #rec_data=""
        
        #mySocket.send(pad.encode())
         
        for i in range(0,len(message),1024) :
                limit = min(i+1024,len(message))
                chunk = message[i:limit]
                mySocket.send(chunk.encode())
                
                #rec_data = rec_data + mySocket.recv(1024).decode()
                 
                #print ('Received from server: ' + data)
                 
                #message = input(" -> ")
                 
        print("All Data sent to server")
        mySocket.close()
 
if __name__ == '__main__':
    Main()
