# importing pygame

import pygame

pygame.mixer.init()


# To off music
def Music_Of():
    pygame.mixer.music.stop()


# TO on music
def Music_1():
    pygame.mixer.music.load("C:\\Users\\KATTAKART\\Desktop\\joseph\\musics & videos\\attitude music.mp3")
    pygame.mixer.music.play(loops=-1)
def Music_2():
    pygame.mixer.music.load("Doom0.mp3")
    pygame.mixer.music.play(loops=-1)