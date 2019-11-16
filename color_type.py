from typing import Tuple,Type,TypeVar,Generic,NewType,ClassVar
import pygame

# 色の型
color_t = TypeVar ("color_t", bound="Color_t")

class Color_t:
    def make_color (r : int, g : int, b : int) -> color_t:
        return pygame.Color(r, g, b)

white : Color_t = Color_t.make_color (255, 255, 255)
black : Color_t = Color_t.make_color (  0,   0,   0)
red   : Color_t = Color_t.make_color (255,   0,   0)
