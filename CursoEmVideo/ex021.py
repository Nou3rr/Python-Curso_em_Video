#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import vlc

p = vlc.MediaPlayer("ex021.mp3")
p.play()

for i in range(1):
    input("Aperte enter para parar de reproduzir\n")
