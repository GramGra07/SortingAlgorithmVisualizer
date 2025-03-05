import math
from time import sleep

import pygame
from numpy import sort
from pygame import display

from isSorted import is_sorted


class Visualizer:
    name = ""
    array = []

    def __init__(self, algorithm):
        self.array = algorithm.arr
        self.name = algorithm.name
        pygame.init()
        self.window_width = self.calculate_window_width(len(self.array))
        self.window_height = 800
        self.screen = display.set_mode((self.window_width, self.window_height))
    def calculate_window_width(self, length):
        min_width = 800
        max_width = 1200
        width = max(min_width, min(max_width, (max_width // length) * length))
        return width
    def update(self, swap1=None, swap2=None, arr=None):
        if arr is not None:
            self.array = arr
        background_color = (255, 255, 255)
        default_bar_color = (0, 0, 0)
        sorted_color = (0, 255, 0)
        highlight_color = (255, 0, 0)
        outline_color = (0, 0, 0)
        self.screen.fill(background_color)
        pygame.display.set_caption(f"Algorithm: {self.name}")
        bar_width = self.window_width // len(self.array)
        max_value = max(self.array)
        for i, value in enumerate(self.array):
            color = default_bar_color
            if swap1 == i or swap2 == i:
                color = highlight_color
            if is_sorted(self.array):
                swap1 = None
                swap2 = None
                color = sorted_color
            bar_height = (value / max_value) * self.window_height
            pygame.draw.rect(self.screen, color, (i * bar_width, self.window_height - bar_height, bar_width, bar_height))
            if color == sorted_color:
                pygame.draw.rect(self.screen, outline_color,
                                 (i * bar_width, self.window_height - bar_height, bar_width, bar_height), 1)
        pygame.display.update()