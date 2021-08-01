import pygame
import time
import random
import os
from settings import *
from colors import *
from typing import Tuple
from Box import Box
from sorts import bubbleSort, selectionSort, insertionSort, shellSort

class Main:
    
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.size = SIZE
        self.fps = FPS
        self.win = None
        self.main_width = MAIN_WIDTH
        self.main_height = MAIN_HEIGHT
        self.width = WIDTH
        self.height = HEIGHT
        self.xoff = X_OFF
        self.yoff = Y_OFF
        self.clock = None
        self.font = None
        self.main_win = None
        self.win = None
        
        self.array = list()
        self.sortFlag = False
        self.sort = bubbleSort
        self.sortIter = None
        
    def win_init(self):
        pygame.init()
        pygame.font.init()
        
        self.main_win = pygame.display.set_mode((self.main_width, self.main_height))
        pygame.display.set_caption("Sorts Visualized")
        
        rect = pygame.Rect((self.xoff, self.yoff, self.width, self.height))
        self.win = self.main_win.subsurface(rect)
        self.main_win.fill(MID_BLACK)
        self.win.fill(SKYBLUE)
        
        self.clock = pygame.time.Clock()
        
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.set_title("Sorting Visualized", GOLD)
        
        pygame.display.update()
        
        if len(self.array) == 0:
            self.array_init()
        

    def set_title(self, title: str, color: Tuple[int]) -> None:
        render = self.font.render(title, 1, color)
        w, h = render.get_size()
        x = (self.main_width - w) // 2
        y = (self.yoff - h) // 2
        self.main_win.blit(render, (x, y))
        
    def array_init(self):
        self.array.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                index = row * self.cols + col
                filename = os.path.join(DIRNAME, f"{index}.jpg")
                file = pygame.image.load(filename)
                self.array.append(Box(index, file))
        
        self.sortIter = iter(self.sort(self.array))
    
    def shuffle_array(self):
        random.shuffle(self.array)
        for index, box in enumerate(self.array):
            box.setCurrIndex(index)
            
        self.sortIter = iter(self.sort(self.array))
            
    def update_indices(self):
        for index, box in enumerate(self.array):
            box.setCurrIndex(index)
        
    def quit(self):
        pygame.font.quit()
        pygame.quit()
        
    def draw(self):
        if self.sortFlag:
            try:
                self.array = next(self.sortIter)
                self.update_indices()
            except StopIteration as e:
                self.sortFlag = False
                
        for box in self.array:
            box.draw(self.win)
    
    def run(self):
        if not pygame.display.init():
            self.win_init()
            
        run = True
        drawFlag = False
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                        
                    if keys[pygame.K_s]:
                        self.shuffle_array()
                        self.update_indices()
                        
                    if keys[pygame.K_RETURN]:
                        self.array.sort(key=lambda x: x.getAbsIndex())
                        self.update_indices()
                    
                    if keys[pygame.K_SPACE]:
                        self.sortFlag = not self.sortFlag
                        
            self.draw()                           
            pygame.display.update()                    
            
        self.quit()
        

        
if __name__ == "__main__":
    X = Main()
    X.run()
