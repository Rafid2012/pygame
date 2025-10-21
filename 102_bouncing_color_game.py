import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

YELLOW = pygame.Color("yellow")
RED = pygame.Color("red")
MAGENTA = pygame.Color("magenta")
WHITE = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.surface([height,width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice(-1,1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right <= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom <= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def color_change(self):
        self.image.fill(random.choice([YELLOW,RED,MAGENTA,WHITE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([DARKBLUE,BLUE,LIGHTBLUE])

all_sprites_list = pygame.sprite.Group()
spl = Sprite(WHITE,20,30)
spl.rect.x = random.randint(0,480)
spl.rect.x = random.randint(0,370)
all_sprites_list.add(spl)

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("COLORFUL BOUNCE")
bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            spl.color_change()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            spl.change_background_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()






