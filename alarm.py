import explorerhat as eh
from time import sleep
import pygame

pygame.mixer.init()
while True:
    a = (eh.analog.four.read())
    if a > 3.0:
        print("SCANNING")
        eh.light.green.on()
        eh.light.red.off()
    else:
        print("ALERT")
        eh.light.green.off()
        eh.light.red.on()
        pygame.mixer.music.load("./alert.mp3")
        pygame.mixer.music.play(1)
