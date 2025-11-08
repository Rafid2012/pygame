import pygame, sys, random

pygame.init()

# Window setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
BROWN = (200, 100, 50)

# Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# Bird
bird_surface = pygame.Surface((34, 24))
bird_surface.fill((255, 255, 0))
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))

# Pipes
pipe_surface = pygame.Surface((70, 400))
pipe_surface.fill(GREEN)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 400, 500]

# Floor
floor_surface = pygame.Surface((WIDTH, 100))
floor_surface.fill(BROWN)
floor_y = HEIGHT - 100

# Font
game_font = pygame.font.Font(None, 40)

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= floor_y:
        return False
    return True

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

def create_pipe():
    random_pipe_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(450, random_pipe_height - 150))
    return bottom_pipe, top_pipe

def display_score(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
    elif game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, WHITE)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, WHITE)
        high_score_rect = high_score_surface.get_rect(center=(WIDTH // 2, 150))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collision(pipe_list)

        # Score
        score += 0.01
        display_score('main_game')
    else:
        high_score = update_score(score, high_score)
        display_score('game_over')

    # Floor
    screen.blit(floor_surface, (0, floor_y))

    pygame.display.update()
    clock.tick(60)
