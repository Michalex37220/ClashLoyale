import pygame
import os

def sound_init():
    """Initialize the mixer."""
    pygame.mixer.init()

def start_music(filename):
    """Load and play a music file once."""
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "themes", filename)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()  # joue une fois
    return path  # retourne le path si besoin

def loop_music():
    """Loop the currently loaded music infinitely."""
    pygame.mixer.music.play(loops=-1)

def stop_music():
    """Stop the currently playing music."""
    pygame.mixer.music.stop()

def rewind_music():
    """Rewind the currently playing music."""
    if not pygame.mixer.get_busy():
        print("Music is not playing!")
    else:
        pygame.mixer.music.rewind()

# Thèmes spécifiques
def combat_theme():
    start_music("combat.mp3")
    loop_music()  # boucle le combat theme

def deck_theme():
    start_music("deck.mp3")  # joue une fois

