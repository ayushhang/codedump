import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)

# Snake and food
snake_block = 20
initial_speed = 8
max_speed = 20
speed_increase = 0.5

# Initialize clock
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
button_font = pygame.font.SysFont(None, 30)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width/2, height/3))
    window.blit(mesg, text_rect)

def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, [10, 10])

def draw_pause_button():
    pygame.draw.rect(window, WHITE, [width - 60, 10, 50, 30])
    pause_text = score_font.render("||", True, BLACK)
    window.blit(pause_text, [width - 45, 15])

def draw_button(text, x, y, w, h, color, text_color):
    pygame.draw.rect(window, color, [x, y, w, h])
    text_surf = button_font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + w/2, y + h/2))
    window.blit(text_surf, text_rect)

def game_over_screen(score):
    window.fill(LIGHT_BLUE)
    message("Game Over!", RED)
    show_score(score)

    # Draw box
    box_width, box_height = 300, 150
    box_x = (width - box_width) // 2
    box_y = height // 2
    pygame.draw.rect(window, WHITE, [box_x, box_y, box_width, box_height])
    pygame.draw.rect(window, BLACK, [box_x, box_y, box_width, box_height], 2)

    # Draw buttons
    button_width, button_height = 120, 40
    restart_x = box_x + (box_width - 2*button_width - 20) // 2
    quit_x = restart_x + button_width + 20
    button_y = box_y + box_height - button_height - 20

    draw_button("Restart", restart_x, button_y, button_width, button_height, GRAY, BLACK)
    draw_button("Quit", quit_x, button_y, button_width, button_height, GRAY, BLACK)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_x <= mouse_pos[0] <= restart_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                    return "restart"
                elif quit_x <= mouse_pos[0] <= quit_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                    return "quit"

def gameLoop():
    game_over = False
    game_close = False
    game_paused = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    score = 0
    snake_speed = initial_speed

    while not game_over:

        if game_close:
            action = game_over_screen(score)
            if action == "quit":
                game_over = True
            elif action == "restart":
                return gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    game_paused = not game_paused
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if width - 60 < mouse_pos[0] < width - 10 and 10 < mouse_pos[1] < 40:
                    game_paused = not game_paused

        if game_paused:
            continue

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(LIGHT_BLUE)
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_score(score)
        draw_pause_button()

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10
            
            snake_speed = min(snake_speed + speed_increase, max_speed)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()