#encoding: UTF-8
# Autor: David Salvador Ruiz Roa
# Reproductor de musica a base de beeps  
# Canción: TWINLE TWINKLE LITTLE STAR
# Partitura: http://www.unimusica-peru.com/partit1.gif

from Myro import *

# Notas
DO = 523.251
RE = 587.33
MI = 659.255
FA = 698.456
SOL = 783.991
LA = 880
SI = 987.767
SILENCIO = 0

#Primer Compás
def Uno(duracion):
    beep(duracion/2,DO)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,DO)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)

#Segundo Compás
def Dos(duracion):
    beep(duracion/2,LA)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,LA)
    beep(duracion/5,SILENCIO)
    beep(duracion,SOL)
    beep(duracion/2,SILENCIO)

#Tercer Compás
def Tres(duracion):
    beep(duracion/2,FA)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,FA)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    
#Cuarto Compás
def Cuatro(duracion):
    beep(duracion/2,RE)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,RE)
    beep(duracion/5,SILENCIO)
    beep(duracion,DO)
    beep(duracion/2,SILENCIO)
 
#Quinto Compás
def Cinco(duracion):
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,FA)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,FA)
    beep(duracion/3,SILENCIO)

#Sexto Compás
def Seis(duracion):
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    beep(duracion,RE)
    beep(duracion/2,SILENCIO)

#Septimo Compás
def Siete(duracion):
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,SOL)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,FA)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,FA)
    beep(duracion/5,SILENCIO)
    
#Octavo Compás
def Ocho(duracion):
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    beep(duracion/2,MI)
    beep(duracion/5,SILENCIO)
    beep(duracion,RE)
    beep(duracion,SILENCIO)
    


# Llamando las fucniones

tiempo = 1

Uno(tiempo)
Dos(tiempo)
Tres(tiempo)
Cuatro(tiempo)
Cinco(tiempo)
Seis(tiempo)
Siete(tiempo)
Ocho(tiempo)
Uno(tiempo)
Dos(tiempo)
Tres(tiempo)
Cuatro(tiempo)
