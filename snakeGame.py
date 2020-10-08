import pygame,os
import random
from pygame.locals import *

pygame.init()

gameWindow = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None,50)
clock = pygame.time.Clock()
end = False

def plot_snake(snake_list,size):
    for x,y in snake_list:
        pygame.draw.circle(gameWindow, (0, 0, 255), (x, y), size, size)

def gameloop():
    exit_game = False
    game_over = False
    global end
    snake_x = 70
    snake_y = 50
    food_x = random.randint(50, 550)
    food_y = random.randint(50, 550)
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    fps = 70
    score = 0
    snake_speed = 3
    snake_len = 1
    snake_list = []
    lastkeypress = ["temp"]
    with open("highScore.txt", "r") as f:
        highScore = f.read()

    while True:
        if end:
            img1 = pygame.image.load(os.path.join('data', 'centiback.gif'))
            gameWindow.blit(img1.convert(), (0, 0))

            gameWindow.blit(font.render(f"HIGHEST SCORE : {highScore}", True, (255, 0, 0)), [120, 50])
            pygame.draw.line(gameWindow, (0, 0, 255), (110, 90), (520, 90), 3)
            gameWindow.blit(font.render(f"YOUR SCORE : {score}", True, (255, 0, 0)), [174, 100])
            gameWindow.blit(pygame.font.Font("freesansbold.ttf", 20).render("(Press any key to continue)", True, (Color('maroon'))),[170, 500])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    end = False
                    gameloop()
            pygame.display.update()
            clock.tick(fps)
        elif game_over:
            img1 = pygame.image.load(os.path.join('data', 'centiback.gif'))
            gameWindow.blit(img1.convert(), (0, 0))

            gameWindow.blit(font.render("GAME OVER", True, (255, 0, 0)), [190, 250])
            gameWindow.blit(pygame.font.Font("freesansbold.ttf", 20).render("(Press any key to continue)", True, (Color('maroon'))), [165, 300])

            if score>int(highScore):
                with open("highScore.txt", "w") as f:
                    f.write(str(score))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    end = True
                    gameloop()
            pygame.display.update()
            clock.tick(fps)
        elif exit_game:
            quit()
        else:
            img1 = pygame.image.load(os.path.join('data', 'centiback.gif'))
            gameWindow.blit(img1.convert(), (0, 0))

            snake_list.append([snake_x, snake_y])

            plot_snake(snake_list,snake_size)
            pygame.draw.circle(gameWindow, (255, 0, 0), (food_x, food_y), 5, 5)

            if len(snake_list)>snake_len:
                del snake_list[0]

            snake_x += velocity_x
            snake_y += velocity_y

            if snake_x<50 or snake_x>550 or snake_y<50 or snake_y>550 or [snake_x,snake_y] in snake_list[:-1]:
                pygame.mixer.Sound(os.path.join('data', 'foghorn.wav')).play()
                game_over = True

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                pygame.mixer.Sound(os.path.join('data', 'yipee.wav')).play()
                food_x = random.randint(50, 550)
                food_y = random.randint(50, 550)
                score+=10
                if score%50==0:
                    snake_speed+=1
                snake_len+=5

            screen_txt = pygame.font.Font("freesansbold.ttf", 25).render(f"Score : {score}", True, (255, 255, 255))
            gameWindow.blit(screen_txt, [5, 5])

            pygame.display.update()
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (lastkeypress[0]=="temp" or lastkeypress[0]=="up" or lastkeypress[0]=="down"):
                        velocity_x = snake_speed
                        velocity_y = 0
                        del lastkeypress[0]
                        lastkeypress.append("right")
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and (lastkeypress[0]=="temp" or lastkeypress[0]=="up" or lastkeypress[0]=="down"):
                        velocity_x = -snake_speed
                        velocity_y = 0
                        del lastkeypress[0]
                        lastkeypress.append("left")
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and (lastkeypress[0]=="temp" or lastkeypress[0]=="right" or lastkeypress[0]=="left"):
                        velocity_x = 0
                        velocity_y = snake_speed
                        del lastkeypress[0]
                        lastkeypress.append("down")
                    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and  (lastkeypress[0]=="temp" or lastkeypress[0]=="right" or lastkeypress[0]=="left"):
                        velocity_x = 0
                        velocity_y = -snake_speed
                        del lastkeypress[0]
                        lastkeypress.append("up")
while True:
    img1 = pygame.image.load(os.path.join('data', 'centiback.gif'))
    gameWindow.blit(img1.convert(), (0, 0))
    img2 = pygame.image.load(os.path.join('data', 'MainSnake.gif'))
    gameWindow.blit(img2.convert(), (30, 30))
    gameWindow.blit(pygame.font.Font("freesansbold.ttf", 20).render("Welcome!! Press any key to start....", True, (Color('maroon'))), [200, 300])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            gameloop()
    pygame.display.update()
    clock.tick(70)