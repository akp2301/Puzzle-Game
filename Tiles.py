#Tiles.py

import pygame
from config import TILE_SIZE, GRID_SIZE, CURRENT_THEME, FONT_NAME, FONT_SIZE

class Tile:
    def __init__(self,number,x,y):
        self.number = number
        self.rect = pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, CURRENT_THEME["tile"], self.rect)
        font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        text = font.render(str(self.number), True, CURRENT_THEME["text"])
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
