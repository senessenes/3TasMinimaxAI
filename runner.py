import time

import pygame
import sys
import math
from uctas import *

game=UcTas()
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("3 Taş")
clock=pygame.time.Clock()
board_surface=pygame.image.load("Assets/background.jpg")
white_piece_surface=pygame.image.load("Assets/white_stone.png")
black_piece_surface=pygame.image.load("Assets/black_stone.png")
is_selected=False
turn_text="Beyaz"
piece_positions=[
    [(50,50),(315,50),(550,50)],
    [(50,315),(315,315),(550,315)],
    [(50,580),(315,580),(550,580)]
]
test_font=pygame.font.Font(None, 50)
text_surface=test_font.render(f"Sıra:{turn_text}",True,"Red")
text_rect=text_surface.get_rect(midbottom=(350,40))

white_pieces=[]
black_pieces=[]
selected_piece = None
turn_text="Beyaz"
class Pul():
    def __init__(self,color,pos):
        self.color=color
        self.pos=pos
        self.image_pos=piece_positions[pos[0]][pos[1]]
        if(self.color=="b"):
            self.image=white_piece_surface
        else:
            self.image=black_piece_surface
DEPTH=8
def draw_screen():
    screen.blit(board_surface,(0,0))
    screen.blit(text_surface,text_rect)
    for piece in white_pieces:
        screen.blit(piece.image,piece.image_pos)
    for piece in black_pieces:
        screen.blit(piece.image,piece.image_pos)


while True:
    if(game.winner()=="s"):
        text_surface = test_font.render("Bilgisayar Kazandı", True, "Red")
        text_rect = text_surface.get_rect(midbottom=(350, 40))
    elif(game.winner()=="b"):
        text_surface = test_font.render("Tebrikler Siz Kazandınız", True, "Red")
        text_rect = text_surface.get_rect(midbottom=(350, 40))




    else:
        if (game.turn == "s"):
            time.sleep(0.5)


            if (game.num_played_moves < 6):
                piece, move = game.minimax(DEPTH)[1]
                game.play_move(piece, move)
                black_pieces.append(Pul("s", move))
                text_surface = test_font.render("Sıra:Beyaz", True, "Red")

            else:
                piece, move = game.minimax(DEPTH)[1]
                game.play_move(piece, move)
                for black_piece in black_pieces:
                    if(black_piece.pos==piece):
                        black_piece.pos=move
                        black_piece.image_pos=piece_positions[move[0]][move[1]]

                text_surface = test_font.render("Sıra:Beyaz", True, "Red")
                draw_screen()




    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
            pygame.quit()

        left, middle, right = pygame.mouse.get_pressed()

        if(right==True):
            is_selected=False
            selected_piece=None

        if(left==True):




            if (game.winner() == False):
                 closest = [0, 0]
                 for i in range(0, len(piece_positions)):
                     for j in range(0, len(piece_positions[i])):
                         if math.dist(piece_positions[i][j], list(pygame.mouse.get_pos())) < math.dist(
                                 piece_positions[closest[0]][closest[1]], list(pygame.mouse.get_pos())):
                             closest = (i, j)

                 if(game.num_played_moves<6):
                     if(game.turn=="b"):
                         if(game.board[closest[0]][closest[1]]=="_"):


                             game.play_move(None,closest)
                             white_pieces.append(Pul("b",closest))
                             text_surface=test_font.render("Sıra:Siyah",True,"Red")

                             draw_screen()


                         else:
                             print("MÜMKÜN OLMAYAN TAŞ SEÇİMİ")
                             break
                 else:
                     if(game.turn=="b"):

                         if (is_selected) == False:




                             piece = closest
                             for white_piece in white_pieces:
                                 if (white_piece.pos == piece):
                                     selected_piece=white_piece

                             is_selected = True
                         else:
                             move = closest
                             if(game.board[move[0]][move[1]]=="b"):
                                 piece=move
                                 move=None
                                 is_selected=True
                                 break

                             elif not (game.is_move_possible(piece,move)):
                                 piece=None
                                 move=None
                                 closest=None
                                 is_selected=False
                                 break

                             game.play_move(selected_piece.pos, move)
                             selected_piece.pos=move
                             selected_piece.image_pos = piece_positions[selected_piece.pos[0]][selected_piece.pos[1]]
                             text_surface=test_font.render("Sıra:Siyah",True,"Red")
                             draw_screen()


                             selected_piece=None
                             is_selected=False

















    draw_screen()

    pygame.display.update()
    clock.tick(60)
