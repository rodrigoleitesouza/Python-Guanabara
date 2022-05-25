import pygame

pygame.init()
pygame.mixer.music.load('exercises\\021-030\\music.mp3')
print("------------------------")
print("- YOUR SONG IS ROCKING -")
print("------------------------")
pygame.mixer.music.play()
input()
pygame.event.wait()
