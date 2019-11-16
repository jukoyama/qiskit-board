import color_type as color
import image_type as image

from typing import List,Dict,Tuple,Optional,Union,TypeVar,ClassVar,Generic,Sequence
import numpy as np
import sys
import copy
import pygame

# ゲームのタイトル
title : str = 'My Game'

##################### 定数 #####################

# 広さ
lines  : int = 4 # 上下の列数
rows   : int = 4 # 左右の列数
length : int = 125 # １マスの辺の長さ
margin : int = 5   # マスの間隔

# ゲーム画面の広さ
width : int = rows * length + rows * margin
height : int = lines * length + lines * margin

##################### 型定義 #####################

# 色を表す型
color_t = color.Color_t

# 画像を表す型
image_t = image.Image_t

# １マスを表す型
cell_t = TypeVar ("cell_t", bound="Cell_t")

class Cell_t:
    def __init__(self,
            pos : Tuple[int, int], # 位置
            #key : int, # マスの量子ビット
            value : int,
            #gate : int, # 作用させるゲート
            moveable : bool) -> cell_t:
        self.pos = pos
        # self.key = key
        self.value = value
        # self.gate = gate
        self.moveable = moveable

# ゲームの状態を表す型
world_t = TypeVar ("world_t", bound="World_t")

class World_t:
    def __init__(self,
            cells : List[cell_t], # マスのリスト
            score : int,          # 点数
            message : str         # エラーメッセージ
            ) -> world_t:
        self.cells = cells
        self.score = score
        self.message = message

# 世界を創る
class Universe_t:
    def __init__(self,
        name : str,
        width : int,
        height : int,
        to_draw : image_t,
        on_key : None,
        stop_when : bool,
        ):
        self.name = name
        self.width = width
        self.height = height
        self.to_draw = to_draw
        self.on_key = on_key
        self.stop_when = stop_when

##################### 色  #####################

# 色
white = color.white
red = color.red

##################### 画像  #####################

# 画像
background : image_t = image_t.empty_scene (width, height)

##################### 初期値  #####################

def Make_cell () -> Cell_t:
    return Cell_t ((10, 10), 2, False)

# マスを作る
def Make_initial_cells (x : int, y : int) -> List[Cell_t]:
    if rows < x:
        return []
    elif lines < y:
        return Make_initial_cells (x + 1, 1)
    else :
        return [Cell_t ((x, y), 2, False)] + Make_initial_cells (x, y + 1)

# 世界の初期値
initial_world : World_t = World_t (Make_initial_cells (1, 1), 0, "")

##################### マス処理  #####################

# マスを受け取ってきてその画像を返す
# TODO: マスの値(value)によって色を変えた方が良い
def cell_to_image (cell : Cell_t) -> image_t:
    if cell.value == 0:
        return image_t.empty_scene (length, length)
    else :
        return image_t.rectangle (length, length, red, False)

# マスの座標を計算
def cell_pos (x : int) -> int:
    return margin * x + length * (x - 1)

##################### 描画  #####################

# 状態を受け取ってきて、ゲーム画面を返す
def draw_with_bg (world : World_t, bg : image_t) -> image_t:
    def images() -> List[image_t]:
        return list ( map (lambda cell : cell_to_image (cell), world.cells) )
    def poss() -> List[Tuple[int, int]]:
        return list ( map (lambda cell : (cell_pos (cell.pos[0]), cell_pos (cell.pos[1])), world.cells) )
    return image_t.place_images (images(), poss(), bg)

def draw(world : World_t) -> image_t:
    return draw_with_bg (world, background)

##################### 開始・終了  #####################

# ゲームの終了条件 (未定)
def Stop_when (world : World_t) -> bool:
    return False

# 世界を創る
big_bang : Universe_t = Universe_t (title, width, height, draw(initial_world), None, False)
