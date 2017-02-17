import pygame
import random
import time


class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 2
        self.speed_y = 2

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    monster = pygame.image.load('images/monster.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    #locations
    monster_x = 200
    monster_y = 200
    x_dir = 0
    y_dir = 0
    monster_speed_x = 2
    monster_speed_y = 2


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic
        monster_x += x_dir
        monster_y += y_dir


        change_dir_countdown -= 1

        if change_dir_countdown == 0:
            change_dir_countdown = 120
            rand_direction = random.randint(0,3)


            if rand_direction == 0:   # top or north
                x_dir =0
                y_dir = -1

            elif rand_direction == 1:  #right or east
                x_dir = 1
                y_dir = 0

            elif rand_direction == 2:  #down or south
                x_dir =0
                y_dir = 1

            elif rand_direction == 3:  #left or west
                x_dir =-1
                y_dir = 0


        # monster_speed_x = rand_direction
        # monster_speed_y = rand_direction
            #
            # if monster_y < 0:      #top
            #     monster_y =  480
            # else:
            #     monster_y -= 5
            #
            # if monster_x > 512:    #right
            #     monster_x = 0
            # else:
            #     monster_x += 5
            #
            # if monster_y > 480:     #down
            #     monster_y =  0
            # else:
            #     monster_y += 5
            #
            # if monster_x < 0:       #left
            #     monster_x =  512
            # else:
            #     monster_x -= 5










        screen.fill(blue_color)

        screen.blit(background_image, (0,0))
        screen.blit(monster, (monster_x,monster_y))
        #screen.blit(monster, (x_dir,y_dir))
        screen.blit(hero, (256,240))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
