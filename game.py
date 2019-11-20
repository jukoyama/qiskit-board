import color_type as color
import image_type as image

import keisan
import twoqubit

from typing import List,Dict,Tuple,Optional,Union,TypeVar,ClassVar,Generic,Sequence
import numpy as np
import sys
import copy
import pygame

# ゲームのタイトル
title : str = 'My Game'

##################### 定数 #####################

# 広さ
lines  : int = 4   # 上下の列数
rows   : int = 4   # 左右の列数
length : int = 125 # １マスの辺の長さ
margin : int = 5   # マスの間隔

# ゲーム画面の広さ
width  : int = 1000
height : int = 559

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
            #key : int,            # マスの量子ビット
            value : int,           # マスの値(古典ビット?)
            #gate : int,           # 作用させるゲート
            moveable : bool) -> cell_t:
        self.pos = pos
        # self.key = key
        self.value = value
        # self.gate = gate
        self.moveable = moveable

# 問題のマスを表す型
prob_t = TypeVar ("prob_t", bound="Prob_t")

class Prob_t:
    def __init__(self,
        pos : Tuple[int, int],   # 位置
        siki : image_t,
        prob1_iscorrect : bool,
        prob2_iscorrect : bool
        ) -> prob_t:
        self.pos = pos
        self.siki = siki
        self.prob1_iscorrect = prob1_iscorrect
        self.prob2_iscorrect = prob2_iscorrect
        # self.prob_cell = prob_cell

# Circuit を表す型
circuit_t = TypeVar ("circuit_t", bound="Circuit_t")

class Circuit_t:
    def __init__(self,
        pos : Tuple[int, int],   # 位置
        zu : image_t,
        #prob_cell : List[Cell_t] # 空欄になっているマス
        ) -> circuit_t:
        self.pos = pos
        self.zu = zu
        # self.prob_cell = prob_cell

# ゲームの状態を表す型
world_t = TypeVar ("world_t", bound="World_t")

class World_t:
    def __init__(self,
            prob : Prob_t,        # 問題
            circ : Circuit_t,     # 回路
            score : int,          # 点数
            message : str         # エラーメッセージ
            ) -> world_t:
        self.prob = prob
        self.circ = circ
        self.score = score
        self.message = message

# 世界を創る
class Universe_t:
    def __init__(self,
        name : str,        # ゲームのタイトル
        width : int,       # ゲーム画面の横幅
        height : int,      # ゲーム画面の縦幅
        to_draw : image_t, # ゲーム画面に表示する画像
        #on_key : image_t,     # キーボードのイベント処理
        stop_when : bool,  # ゲーム終了条件
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
black = color.black

##################### 画像  #####################

# 画像
background : image_t = image_t.empty_scene (width, height)

# 大門１の画像
prob1_img : image_t = image_t.read_image('Prob1Img/ques1.png', width, height)
ans1_img   = pygame.image.load('Prob1Img/ans1.png')
wrong1_img = pygame.image.load('Prob1Img/not1.png')

# 大門２の画像
prob2_img  = pygame.image.load('Prob2Img/ques2.png')
ans2_img   = pygame.image.load('Prob2Img/ans2_2.png')
wrong2_img = pygame.image.load('Prob2Img/not2.png')

siki1 : image_t = image_t.read_image('NotUseImg/sample1.png', 1000, 300)
zu1 : image_t   = image_t.read_image('NotUseImg/q1_c.png', 1000, 300)

##################### キーボード処理  #####################

def on_key (key : str, world : World_t, bg) -> image_t:
    prob : Prob_t = world.prob
    if prob.prob1_iscorrect == False:
        bool = keisan.kekka (key)
        print(bool)
        display_prob1_is_correct_change(bool, bg)
        prob.prob1_iscorrect = bool
    elif prob.prob2_iscorrect == False:
        bool = twoqubit.kekka (key)
        display_prob2_is_correct_change(bool, bg)
        prob.prob2_iscorrect = bool

def display_prob1_is_correct_change (b : bool, bg : image_t) -> image_t:
    if b == True :
        print("true so display_change!!")
        return bg.blit(ans1_img, (0, 0))
        # return background
    else :
        print("false so display_change!!")
        return bg.blit(wrong1_img, (0, 0))

def display_prob2_is_correct_change (b : bool, bg : image_t) -> image_t:
    if b == True :
        print("true so display_change!!")
        return bg.blit(ans2_img, (0, 0))
        # return background
    else :
        print("false so display_change!!")
        return bg.blit(wrong2_img, (0, 0))

def display_next (world : World_t, bg : image_t) -> image_t:
    prob : Prob_t = world.prob
    state : bool = prob.prob1_iscorrect
    if state :
        # display next image
        print("display next")
        bg.blit(prob2_img, (0, 0))
    else :
        # display the former question
        return bg.blit(prob1_img, (0, 0))

##################### 初期値  #####################

# 問題のマスを創る
def Make_initial_probcell (x : int , y : int) -> Prob_t:
    return Prob_t ((x,y), siki1, False, False)

# 回路のマスを創る
def Make_initial_circuitcell (x : int, y : int) -> Circuit_t:
    return Circuit_t ((x,y), zu1)

# マスを作る
# def Make_initial_cells (x : int, y : int) -> List[Cell_t]:
#     if rows < x:
#         return []
#     elif lines < y:
#         return Make_initial_cells (x + 1, 1)
#     else :
#         return [Cell_t ((x, y), 2, False)] + Make_initial_cells (x, y + 1)

# 世界の初期値
initial_world : World_t = World_t (Make_initial_probcell(0,0), Make_initial_circuitcell(0,(height/2)), 0, "")

##################### マス処理  #####################

# マスを受け取ってきてその画像を返す
# def cell_to_image (cell : Cell_t) -> image_t:
#     if cell.value == 0:
#         return image_t.empty_scene (length, length)
#     else :
#         return image_t.rectangle (length, length, red, False)

# 問題空間を画像にする
def prob_area_to_image (area : Prob_t) -> image_t:
    return image_t.rectangle (width, (height / 2), red, False)

# 回路空間を画像にする
def circ_area_to_image (area : Circuit_t) -> image_t:
    return image_t.rectangle (width, (height / 2), black, False)

# マスの座標を計算
# def cell_pos (x : int) -> int:
#     return margin * x + length * (x - 1)

##################### 描画  #####################

# 状態を受け取ってきて、ゲーム画面を返す
def draw_with_bg (world : World_t, bg : image_t) -> image_t:
    problem : Prob_t = world.prob
    circuit : Circuit_t = world.circ
    def images() -> List[image_t]:
        return [prob_area_to_image (problem), circ_area_to_image (circuit), problem.siki, circuit.zu]
    def poss()  -> List[Tuple[int, int]]:
        return [world.prob.pos, world.circ.pos, world.prob.pos, world.circ.pos]
    return image_t.place_images (images(), poss(), bg)

# 問題の画像と回路の画像を統合させる
def draw (world : World_t) -> image_t:
    # return draw_with_bg (world, background)
    return image_t.place_images ([prob1_img], [(0,0)], background)

##################### 開始・終了  #####################

# ゲームの終了条件 (未定)
def Stop_when (world : World_t) -> bool:
    return False

# 世界を創る
big_bang : Universe_t = Universe_t (title, width, height, draw(initial_world), Stop_when(initial_world))
