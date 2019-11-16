from typing import List,Tuple,Type,TypeVar,Generic,NewType,ClassVar
import pygame

# キーボードのイベント処理
def key_event (on_key : pygame.event) -> str:
    if on_key.type == pygame.KEYUP:
        return "up"
    elif on_key.type == pygame.DOWN:
        return "down"
    elif on_key.type == pygame.LEFT:
        return "left"
    elif on_key.type == pygame.RIGHT:
        return "right"
    elif on_key.type == pygame.K_q:
        return "quit"
