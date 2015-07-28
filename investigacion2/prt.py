import serial
import sys


try:
    s = serial.Serial(1)
    s.timeout=2;
except serial.SerialException:
    print ("Error al abrir el puerto.")
    sys.exit()
    

texto = "Texto a enviar"
s.write(texto)


respuesta=s.read(10);

if len(respuesta)>0 :
    print ("Respuesta: " + respuesta)
else:
    print ("Tiempo de espera agotado.")