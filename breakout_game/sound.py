import pygame


# Pygame'i başlat
pygame.mixer.init()

# Ses efektlerini yükle
hit_sound = pygame.mixer.Sound("hit_sound.wav")
bounce_sound = pygame.mixer.Sound("bounce_sound.wav")
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")

def play_hit_sound():
    hit_sound.play()

def play_bounce_sound():
    bounce_sound.play()

def play_game_over_sound():
    game_over_sound.play()
