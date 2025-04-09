#sounds.py
import pygame

def load_sounds():
    pygame.mixer.music.load("assets/sounds/background.mp3")
    pygame.mixer.music.play(-1)

def play_click():
    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
    click_sound.play()
