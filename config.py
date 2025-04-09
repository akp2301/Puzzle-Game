# config.py
import pygame

TILE_SIZE = 80
GRID_SIZE = 4
WINDOW_WIDTH = TILE_SIZE * GRID_SIZE
WINDOW_HEIGHT = TILE_SIZE * GRID_SIZE + 50  # space for UI

# Color themes
COLOR_THEMES = {
    "light": {
        "bg": (255, 255, 255),
        "tile": (0, 122, 204),
        "text": (0, 0, 0),
    },
    "dark": {
        "bg": (30, 30, 30),
        "tile": (200, 200, 200),
        "text": (255, 255, 255),
    },
    "retro": {
        "bg": (240, 224, 160),
        "tile": (80, 48, 48),
        "text": (255, 255, 255),
    }
}

CURRENT_THEME = COLOR_THEMES["light"]
FONT_NAME = pygame.font.get_default_font()
FONT_SIZE = 36

# Sound Settings
SOUND_ENABLED = True
MOVE_SOUND_PATH = "assets/move.wav"
WIN_SOUND_PATH = "assets/win.wav"