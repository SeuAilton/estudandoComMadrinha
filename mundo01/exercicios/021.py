#DESAFIO 021
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from playsound3 import playsound
import multiprocessing
import pygame


play = multiprocessing.Process(target=playsound, args=("/home/ailton/Documentos/estudandoComMadrinha/mundo01/exercicios",))
play.start()
input("Enter pra parar")
play.terminate()

'''
if __name__ == '__main__':
  play = multiprocessing.Process(target=playsound, args=("/home/ailton/Documentos/estudandoComMadrinha/mundo01/exercicios",))
  play.start()
  input("Enter pra parar")
  play.terminate()

'''
'''
pygame.init()
pygame.mixer.music.load("/home/ailton/Documentos/estudandoComMadrinha/mundo01/exercicios")
pygame.mixer.music.play()
input()
pygame.event.wait()

'''