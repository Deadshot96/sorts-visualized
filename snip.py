import pygame
import os
from settings import *
import send2trash

surface = pygame.image.load(IMG_FILE_NAME)

for filename in os.listdir(DIRNAME):
    path = os.path.join(DIRNAME, filename)
    send2trash.send2trash(path)

for row in range(ROWS):
    for col in range(COLS):
        x = col * SIZE
        y = row * SIZE
        index = row * COLS + col
        sub = surface.subsurface((x, y, SIZE, SIZE))
        path = os.path.join(DIRNAME, f"{index}.jpg")
        pygame.image.save(sub, path)
