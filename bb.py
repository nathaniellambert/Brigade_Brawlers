# import all modules
import pygame, sys, random
from pygame.locals import *

# initialize pygame and all its component functions and attributes
pygame.init()

# set all constant variables

# colors
GOLD = (212,175,55)
BLACK = (0,0,0)
RED = (181,16,16)
GREEN = (28, 206, 34)
AMBER = (226, 168, 31)

# display size
HEIGHT = 560
WIDTH = 980


################################################################################

# clock variables
game_clock = pygame.time.Clock()
FPS = 25

# screen variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

back1 = pygame.image.load('resources/wh.png')

font = pygame.font.SysFont('comicsansms', 25)

################################################################################
#good_table =[[] * 2 for row in range(2)]


################################################################################
# fighter class
class Fighter(object):
    def __init__(self, x, y, player_num, img_num):
        self.x = x
        self.y = y
        self.img_num = img_num
        self.player_num = player_num
        self.jumping = False
        self.jump_offset = 0
        self.fighter_images = self.load_fighter_images()
        self.health = 100
        self.fighter = self.fighter_images[self.player_num][self.img_num].get_rect(topleft = (0,int(HEIGHT/2)))

    def load_fighter_images(self):
        self.file_names = [['resources/plebe/plebeReady.png'],
                            ['resources/plebe/plebeReady.png']]
        self.fighter_images = [[] * 2 for row in range(2)]
        for player in range(len(self.file_names)):
            for file_name in range(len(self.file_names[player])):
                fighter_img = pygame.image.load(self.file_names[player][file_name])
                self.fighter_images[player].append(fighter_img)
        return(self.fighter_images)

    def move_right(self, event, dist, disp_surf):
        self.fighter.centerx = min(self.fighter.centerx+dist,disp_surf.get_width())
        if self.fighter.x < 0 : self.fighter.x = 0

    def move_left(self, event, dist, disp_surf):
        self.fighter.centerx = max(self.fighter.centerx-dist,0)
        if self.fighter.right > WIDTH : self.fighter.right = WIDTH

    def punch_right(self):
        pass

    def punch_left(self):
        pass

# Quit the game
def terminate():
    pygame.quit()
    sys.exit()

# print msg to screen
## will look prettier eventually
def msg_to_screen(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH*1//8, HEIGHT//2])


# Set up game window
def main_window(dimensions, caption):
    pygame.init()
    screen.fill((255, 255, 255))
    screen.blit(back1, (0,0))
    pygame.display.update()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)


# Start Screen
def start_screen():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_s:
                    run = False
                if event.key == K_q:
                    terminate()
        msg_to_screen("PRESS 'S' TO START GAME // PRESS 'Q' TO QUIT GAME", GOLD)
        pygame.display.update()
        screen.blit(back1, (0, 0))
        game_clock.tick(FPS)

def choose_player(player):
    icon_names = ['MalePlebeWalk00.png','MalePlebeWalkR0.png']
    icons = []
    for icon in icon_names:
        fighter_img = pygame.image.load(icon)
        icons.append(fighter_img)
    #icon0 = Fighter(50,50,0,0)
    #icon1 = Fighter(50,50,1,0)
    player_icon_num = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_0:
                    player_icon_num = 0
                    run = False
                    return player_icon_num
                if event.key == K_1:
                    player_icon_num = 1
                    run = False
                    return player_icon_num
        pygame.display.update()
        screen.blit(back1, (0, 0))
        game_clock.tick(FPS)
        #screen.blit(icon0.fighter_images[0][0],icon0.fighter)
        #screen.blit(icon1.fighter_images[1][0],icon1.fighter)
        screen.blit(icons[0], (50,150))
        screen.blit(icons[1], (600,150))
        icon0_txt = font.render('0', True, GOLD)
        screen.blit(icon0_txt, (250,500))
        icon1_txt = font.render('1', True, GOLD)
        screen.blit(icon1_txt, (700,500))
        if player == 1:
            txt = font.render('PLAYER 1: CHOOSE YOUR CHARACTER', True, GOLD)
            screen.blit(txt, (300, 50))
        if player == 2:
            txt = font.render('PLAYER 2: CHOOSE YOUR CHARACTER', True, GOLD)
            screen.blit(txt, (300, 50))


# Game Over Screen
## will give user option to quit, start rematch,
## or return to the start screen
def game_over_screen():
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    over = False
                if event.key == K_q:
                    terminate()
        msg_to_screen("PRESS 'R' TO PLAY AGAIN // PRESS 'Q' TO QUIT", GOLD)
        pygame.display.update()
        screen.blit(back1, (0, 0))
        game_clock.tick(FPS)
    if over == False:
        play_game()

# Health Bars
def health_bars(player1_health, player2_health, display):
    # player 1
    if 50 < player1_health <= 100:
        player1_health_color =GREEN
    elif 25 < player1_health <= 50:
        player1_health_color = AMBER
    else:
        player1_health_color = RED
    # player 2
    if 50 < player2_health <= 100:
        player2_health_color =GREEN
    elif 25 < player2_health <= 50:
        player2_health_color = AMBER
    else:
        player2_health_color = RED
    # drawing health bars
    pygame.draw.rect(display, player1_health_color, (20, 25, player1_health, 25))
    pygame.draw.rect(display, player2_health_color, (WIDTH-120, 25, player2_health, 25))




def play_game():
    player1_icon_num = 0
    player2_icon_num = 0
    # make display appear
    display = main_window((WIDTH,HEIGHT),"Brigade Brawlers")

    # load fighters
    player1 = Fighter(0,980,player1_icon_num,0)
    player2 = Fighter(0,0,player2_icon_num,0)
    player1.centerx = 0
    player1.centery = 0
    player2.centerx = pygame.display.get_surface().get_width()
    player2.centery = pygame.display.get_surface().get_width()


    # load standing images
    stand1 = [pygame.image.load('resources/plebe/plebeReady.png'),pygame.image.load('resources/plebe/plebeReady.png'),pygame.image.load('resources/plebe/plebeReady.png')]
    stand2 = [pygame.image.load('resources/plebe/plebeReady.png'),pygame.image.load('resources/plebe/plebeReady.png'),pygame.image.load('resources/plebe/plebeReady.png')]
    punch1 = [pygame.image.load('resources/plebe/CadetPTCross/CadetPTcross3.png')]
    punch2 = [pygame.image.load('resources/plebe/CadetPTCross/CadetPTcross3.png')]
    retreat1 = [pygame.image.load('resources/plebe/plebeReady.png')]
    retreat2 = [pygame.image.load('resources/plebe/plebeReady.png')]
    movement1 = [stand1,player1.fighter_images[player1_icon_num],punch1,retreat1]
    movement2 = [stand2,player2.fighter_images[player2_icon_num],punch2,retreat2]

    # load background
    screen.fill((255, 255, 255))
    screen.blit(back1, (0, 0))

    # set clock
    game_clock = pygame.time.Clock()
    FPS = 10

    # hold the keys down
    pygame.key.set_repeat(50,50)
    score = 0
    score_font = pygame.font.SysFont(None,20)

    # keep the game running
    while True:
        m = 0
        n = 0
        controls  = pygame.key.get_pressed()

        for event in pygame.event.get():
            ### game termination conditions ###
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

                #### move fighter conditions ###

                # move foward
                #Player 1
                if controls[K_RIGHT]:
                    player1.move_right(event,25,display)
                    m = 1
                #Player 2
                if controls[K_a]:
                    player2.move_left(event,25,display)
                    n = 1

                # move backwards
                #Player 1
                if controls[K_LEFT]:
                    player1.move_left(event,25,display)
                    m = 3

                #Player 2
                if controls[K_d]:
                    player2.move_right(event,25,display)
                    n = 3

                # punch
                #Player 1
                if controls[K_m]:
                    m = 2
                    if abs(player1.fighter.x - player2.fighter.x) <= 50:
                        if controls[K_e]:
                            pass
                        else:
                            player2.health -= 10
                    else:
                        pass


                #Player 2
                if controls[K_f]:
                    n = 2
                    if abs(player1.fighter.x - player2.fighter.x) <= 50:
                        if controls[K_n]:
                            pass
                        else:
                            player1.health -= 10
                    else:
                        pass


        # give display background color
        screen.blit(back1, (0, 0))

        # make fighter appear on surface
        display.blit(movement1[m][0],player1.fighter)
        display.blit(movement2[n][0],player2.fighter)
        movement1[m].append(movement1[m].pop(0))
        movement2[n].append(movement2[n].pop(0))

        if player1.health <= 0 or player2.health <=0:
            game_over_screen()

        # show health bars
        health_bars(player1.health, player2.health, display)
        # update display (MUST BE LAST)
        pygame.display.update()
        screen.blit(back1, (0, 0))

        # make clock tick
        game_clock.tick(FPS)










if __name__=='__main__':
    #start_screen()
    play_game()
