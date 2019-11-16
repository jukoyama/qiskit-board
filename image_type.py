from typing import List,Tuple,Type,TypeVar,Generic,NewType,ClassVar
import color_type as color
import pygame

# 色の型
color_t = color.Color_t

# 画像の型
image_t = TypeVar ("image_t", bound="Image_t")

class Image_t:
    def empty_scene (x : int, y : int) -> image_t:
        return pygame.Surface((x,y))

    def rectangle (width : int, height : int, color : color_t, fill : bool) -> image_t:
        screen : image_t = pygame.Surface((width,height))
        pygame.draw.rect(screen, color, (0, 0, width, height))
        return screen

    def line (start : Tuple[int, int], end : Tuple[int, int], color : color_t, size : int, scene : image_t) -> image_t:
        return pygame.draw.line(scene, color, start, end, size)

    def circle (width : int, height : int, color: color_t, fill : bool, scene : image_t) -> image_t:
        return pygame.draw.circle(scene, color, (width, height), 20, 0)

    def place_image (image : image_t, posn : Tuple[int, int], background : image_t) -> image_t:
        return background.blit(image, posn)

    def place_images (images: List[image_t], poss: List[Tuple[int, int]], background: image_t) -> image_t:
        if images == [] and poss == []:
            return background
        elif images == [] and len(poss) > 0:
            raise ValueError
        elif len(images) > 0 and poss == []:
            raise ValueError
        else :
            image_first, image_rest = images[0], images[1:]
            pos_first, pos_rest = poss[0], poss[1:]
            background.blit(image_first, pos_first)
            return Image_t.place_images (image_rest, pos_rest, background)
