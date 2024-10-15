import socket
import os
from tqdm import tqdm

a = socket.socket()

def filedownloading(downlloadsize):
    sds = int(downlloadsize)
    a.sendall(b"<PT>") #permetti trasmissione
    transmissionended = False
    filedidestinazione = open("filetemporaneo", "bw")
    tempstr = b""
    bs = 0
    tbar = tqdm(total = sds, desc = "DOWNLOAD IN CORSO...", colour='#00ff00', unit= "b", unit_scale= True)
    while transmissionended == False:
        bs += 1
        tbar.update(2048)
        tempstr += (a.recv(2048))
        if tempstr[-9:] == b"<ENDFILE>":
            transmissionended = True
    
    z = tempstr.split(b"<B>")
    print("COPIA IN CORSO DEL FILE: '"+ z[0].decode() + "' DI " +  downlloadsize + " BYTES")
    filedidestinazione.write(z[2])
    print("FILE SCARICATO CON SUCCESSO")
    filedidestinazione.close()
    os.rename("filetemporaneo",z[0].decode())



def listening():
    while True:
        brecv = a.recv(1025)
        if brecv[:5] == b"<RTF>":
            print("RICHIESTA TRASMISSIONE FILE RICEVUTA")
            filedownloading(brecv[5:].decode())

host = '127.0.0.1'  # Indirizzo locale
port = 12345        # Porta da utilizzare

a.connect((host,port))

listening()
