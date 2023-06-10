import pygame
import numpy as np
import tcod

class GameRender:
    def __init__(self, in_width: int, in_height: int):
        pygame.init()
        self._width = in_width
        self._height = in_height
        self.screen = pygame.display.set_mode((in_width, in_height))
        pygame.display.set_caption("Pacman")
        self._clock = pygame.time.Clock()
        self._done = False
        self._game_objects = []
        self._walls = []
        self._cookies = []
        self._hero: Hero = None

    


            
    