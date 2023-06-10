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

    def tick(self, in_fps: int):
        black = (0, 0, 0)

        while not self._done:
            for game_object in self._game_objects:
                game_object.tick()
                game_object.draw()

            pygame.display.flip()
            self._clock.tick(in_fps)
            self._screen.fill(black)
            self._handle_events()
        print("Game Over")

    def add_game_object(self, obj: GameObject):
        self._game_objects.append(obj)          #append() =Add object to end of list
    
    def add_wall(self, obj: Wall):
        self.add_game_object(obj)
        self._walls.append(obj)

    def _handel_events(self):
        pass #!Implement later


class GameObject:
    def __init__(self, in_surface, x, y, in_size: int, in_color=(255, 0, 0), is_circle: bool = False):
        self._size = in_size
        self._renderer: GameRender = in_surface
        self._surface = in_surface._screen
        self.y = y
        self.x = x
        self._color = in_color
        self._circle = is_circle
        self._shape = pygame.Rect(self.x, self.y, in_size, in_size)

    def draw(self):
        if self._circle:
            pygame.draw.circle(self._surface, self._color, self.x, self.y, self._size)
        else:
            rect_object = pygame.Rect(self.x, self.y, self._size, self._size)
            pygame.draw.rect(self._surface, self._color, rect_object, border_radius=4)

    def tick(self):
        pass

            
    