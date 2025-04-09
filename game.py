import pygame
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Sliding Puzzle")

# Constants
TILE_SIZE = 100
GRID_SIZE = 4
FONT = pygame.font.Font(None, 60)

# Create the tile numbers (1-15) and one blank (None)
tiles = list(range(1, GRID_SIZE * GRID_SIZE))
tiles.append(None)  # None is the blank tile

# Shuffle puzzle (you can improve this later)
random.shuffle(tiles)

def draw_tiles():
    for i, val in enumerate(tiles):
        x = (i % GRID_SIZE) * TILE_SIZE
        y = (i // GRID_SIZE) * TILE_SIZE
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

        if val is not None:
            pygame.draw.rect(screen, (100, 150, 250), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            text = FONT.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, (30, 30, 30), rect)  # Blank tile

def get_blank_index():
    return tiles.index(None)

def swap_tiles(i, j):
    tiles[i], tiles[j] = tiles[j], tiles[i]

def is_adjacent(i1, i2):
    row1, col1 = divmod(i1, GRID_SIZE)
    row2, col2 = divmod(i2, GRID_SIZE)
    return abs(row1 - row2) + abs(col1 - col2) == 1

def is_solved():
    return tiles[:-1] == list(range(1, GRID_SIZE * GRID_SIZE))

# Main loop
running = True
moves = 0
win = False

while running:
    screen.fill((50, 50, 50))
    draw_tiles()

    if win:
        win_text = FONT.render("You Win!", True, (255, 255, 0))
        screen.blit(win_text, (120, 170))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not win and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // TILE_SIZE
            row = pos[1] // TILE_SIZE
            index = row * GRID_SIZE + col
            blank_index = get_blank_index()

            if is_adjacent(index, blank_index):
                swap_tiles(index, blank_index)
                moves += 1
                if is_solved():
                    win = True

    # Move counter
    move_text = pygame.font.Font(None, 28).render(f"Moves: {moves}", True, (255, 255, 255))
    screen.blit(move_text, (10, 370))

    pygame.display.flip()
