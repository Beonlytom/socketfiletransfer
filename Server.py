import socket
import os
def inviafile(percorsofile, socketdestinazione):
    
    socketdestinazione.sendall(b"<RTF>" + str(os.path.getsize(percorsofile)).encode()) #richiesta trasmissione file
    print("RICHIESTA TRASMISSIONE INVIATA")
    if(socketdestinazione.recv(1024) == b"<PT>"):
        print("Trasmissione permessa")
        a = open(percorsofile, "br")
        socketdestinazione.sendall(os.path.basename(percorsofile).encode() + b"<B>" + a.read() +b"<B>" b"<ENDFILE>")
        print("FILE INVIATO CON SUCCESSO")

#il mio cazzo di socket
imcds = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # Indirizzo locale
port = 12345        # Porta da utilizzare
imcds.bind((host,port))

# dico che il socket deve aspettare (n) connessioni in coda
imcds.listen()
while True: 

    # accetta la connessione del socket 
    sockconnesso, indirizzo = imcds.accept()
    inviafile(r"INSERIRE INDIRIZZO FILE", sockconnesso)
    print("QUESTO IP" + str(indirizzo) + " SI è CONNESSO!")
    


