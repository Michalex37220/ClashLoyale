import pygame
import os

pygame.init()
pygame.mixer.init()

def start_sfx(filename):
    """Play a SFX once or use loop() to loop it."""
    base_dir = os.path.dirname(__file__)
    sound_path = os.path.join(base_dir, "..", "sounds", filename)
    sound = pygame.mixer.Sound(sound_path)
    sound.play()  # joue une fois
    return sound  # retourne l'objet Sound pour pouvoir le boucler plus tard

def loop(sound):
    """Loop a sound infinitely."""
    sound.play(loops=-1)

def hog_rider_sfx():
    hog_sfx = start_sfx("spawn_hog_rider.mp3")
    # loop(hog_sfx) ne décommenter pas c'est insuportable
