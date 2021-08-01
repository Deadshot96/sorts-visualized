import pygame
from pygame import Surface
from settings import *

class Box:
    def __init__(self, index: int, img: Surface):
        self.img = img
        self.absIndex = index
        self.currIndex = index
        self.row = index // COLS
        self.col = index % COLS
        self.size = SIZE
        self.x = self.col * self.size
        self.y = self.row * self.size
        
    def setCurrIndex(self, index: int) -> None:
        self.currIndex = index
        self.update_pos()
        
    def getCurrIndex(self) -> int:
        return self.currIndex
    
    def draw(self, win: Surface) -> None:
        win.blit(self.img, (self.x, self.y))
        
    def update_pos(self):
        self.row = self.currIndex // COLS
        self.col = self.currIndex % COLS
        self.x = self.col * self.size
        self.y = self.row * self.size
        
    def getAbsIndex(self) -> int:
        return self.absIndex
        
    def __lt__(self, box) -> bool:
        return self.absIndex < box.getAbsIndex()
    
    def __eq__(self, box) -> bool:
        return self.absIndex == box.getAbsIndex()
  