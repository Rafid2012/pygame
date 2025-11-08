import pygame
import random
import os

pygame.init()

WIDTH,HEIGHT = 900,550
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock,Paper,scissors - Rafid bin hasan")

#colors
BG_TOP = (245,245,255)
BG_BOTTOM = (210,220,255)
HEADER_COLOR = (30,40,80)
WHITE = (255,255,255)
TEXT = (40,40,40)
GREEN = (60,200,90)
RED = (220,70,70)
BLUE = (60,120,230)
GREY = (180,180,200)

# FONTS

TITLE_FONT = pygame.font.SysFont("arialblack",40)
LABEL_FONT = pygame.font.SysFont("arial",26)
SCORE_FONT = pygame.font.SysFont("arial",28, bold = True)
RESULT_FONT = pygame.font.SysFont("arial",28)

#Load Images

PLAYER_IMAGES = {
    "rock": pygame.image.load("rock.png"),
    "paper": pygame.image.load("paper.png"),
    "scissors": pygame.image.load("scissors.png")
}

PC_IMAGES = {
    "rock": pygame.image.load("pc_rock.png"),
    "paper": pygame.image.load("pc_paper.png"),
    "scissors": pygame.image.load("pc_scissors.png")
}

#resize images
for k in PLAYER_IMAGES:
    PLAYER_IMAGES[k] = pygame.transform.scale(PLAYER_IMAGES[k], (180,180))
for k in PC_IMAGES:
    PC_IMAGES[k] = pygame.transform.scale(PC_IMAGES[k], (180,180))

#Button Class
class Button:
    def __init__(self,x,y,text,color,hover_color,width=170,height=55):
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self,screen,mouse_pos):
        clr = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen,clr,self.rect,border_radius=12)
        text_surface = LABEL_FONT.render(self.text,True,WHITE)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface,text_rect)

    def clicked(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
#UI buttons
buttons = {
    Button(130,420,"Rock",BLUE,(100,150,255)),
    Button(370,420,"Paper",GREEN,(120,220,120)),
    Button(610,420,"Scissors",RED,(255,100,100)),
    Button(WIDTH-160,20, "Reset",GRAY,(150,150,120),120,45)
}

#Game state
player_score = 0
pc_score = 0
high_score = 0
round_winner = ""
player_choice = ""
pc_choice = ""

#Load High Score

if os.path.exists("highscore.txt"):
    with open("highscore.txt","r") as f:
        try:
            high_score = int(f.read().strip())
        except:
            high_score = 0

def save_high_score(score):
    with open("highscore.txt","w") as f:
        f.write(str(score))

def get_winner(player,pc):
    if player == pc:
        return "Draw"
    elif(player == "rock" and pc == "scissors") or \
        (player == "paper" and pc == "rock") or \
        (player == "scissors" and pc == "paper"):
        return "Player"
    else:
        return "Computer"
    
#Gradient Background
def draw_gradient():
    for i in range(HEIGHT):
        color = (
            BG_TOP[0] + (BG_BOTTOM[0] + BG_BOTTOM[0]) * i // HEIGHT,
            BG_TOP[1] + (BG_BOTTOM[1] + BG_BOTTOM[1]) * i // HEIGHT,
            BG_TOP[2] + (BG_BOTTOM[2] + BG_BOTTOM[2]) * i // HEIGHT
        )
        pygame.draw.line(SCREEN,color,(0,i),(WIDTH,i))

#Main Loop
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    draw_gradient()

    #Header Bar
    

