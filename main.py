#main.py
import pygame
import sys
import random
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CURRENT_THEME, TILE_SIZE, GRID_SIZE, SOUND_ENABLED, MOVE_SOUND_PATH, WIN_SOUND_PATH
from Tiles import Tile
from score_manager import load_best_score, save_best_score

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Puzzle Game")
clock = pygame.time.Clock()
numbers = list(range(1, GRID_SIZE * GRID_SIZE))  # 1 to 15 for 4x4 grid
random.shuffle(numbers)

# Load sounds
#if SOUND_ENABLED:
    #move_sound = pygame.mixer.Sound(MOVE_SOUND_PATH)
    #win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)
# Shuffle puzzle (you can improve this later)

# Create a grid of tiles
def create_tiles():
    
    tiles = []
    for i, number in enumerate(numbers):
        x = (i % GRID_SIZE) * TILE_SIZE
        y = (i // GRID_SIZE) * TILE_SIZE
        tile = Tile(number, x, y)
        tiles.append(tile)
    return tiles

tiles = create_tiles()
# Add an empty space
empty_rect = pygame.Rect((GRID_SIZE - 1) * TILE_SIZE, (GRID_SIZE - 1) * TILE_SIZE, TILE_SIZE, TILE_SIZE)

moves = 0
best_score = load_best_score()

def draw():
    screen.fill(CURRENT_THEME["bg"])
    for tile in tiles:
        tile.draw(screen)
    font = pygame.font.Font(None, 28)
    move_text = font.render(f"Moves: {moves}", True, CURRENT_THEME["text"])
    screen.blit(move_text, (10, WINDOW_HEIGHT - 40))
    if best_score is not None:
        best_text = font.render(f"Best: {best_score}", True, CURRENT_THEME["text"])
        screen.blit(best_text, (150, WINDOW_HEIGHT - 40))
    pygame.display.flip()

def check_win():
    for i, tile in enumerate(tiles):
        correct_x = (i % GRID_SIZE) * TILE_SIZE
        correct_y = (i // GRID_SIZE) * TILE_SIZE
        if tile.rect.x != correct_x or tile.rect.y != correct_y:
            return False
    return True

running = True
while running:
    # Placeholder for logic to move tiles
    # You'd implement tile dragging/clicking here and play move sound
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for tile in tiles:
                if tile.rect.collidepoint(pos):
                    # Check if tile is adjacent to the empty space
                    dx = abs(tile.rect.x - empty_rect.x)
                    dy = abs(tile.rect.y - empty_rect.y)
                    if (dx == TILE_SIZE and dy == 0) or (dy == TILE_SIZE and dx == 0):
                        # Swap tile and empty space
                        tile.rect, empty_rect = empty_rect.copy(), tile.rect.copy()
                        moves += 1
                        #if SOUND_ENABLED:
                            #move_sound.play()
                    break

    # Example of win check
    if check_win():
        #if SOUND_ENABLED:
            #win_sound.play()
        if best_score is None or moves < best_score:
            save_best_score(moves)
        pygame.time.wait(2000)
        tiles = create_tiles()
        moves = 0

    draw()
    clock.tick(30)

pygame.quit()
sys.exit()