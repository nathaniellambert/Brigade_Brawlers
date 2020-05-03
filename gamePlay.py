import pygame, random, os
from pygame.locals import *
import interface

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0,0,0)
RED = (181,16,16)
GREEN = (28, 206, 34)
AMBER = (226, 168, 31)
HEIGHT = 560
WIDTH = 980

class Fighter(object):
    def __init__(self, x, y, fighterID):
        self.x = x
        self.y = y
        self.fighterID = fighterID
        self.standing_image = self.load_standing_images()
        self.running_images = self.load_running_images()
        self.punching_image = self.load_punching_images()
        self.health = 400
        self.fighter = self.running_images[self.fighterID].get_rect(topleft=(self.x,self.y))

    def load_standing_images(self):
        standingImages = [
            'resources/plebe/plebeStanding.png',
            'resources/dpe/dpeStanding.png',
            'resources/supt/suptStanding.png',
            'resources/acu/acuStanding.png']

        standImg = pygame.image.load(standingImages[self.fighterID])
        return standImg

    def load_punching_images(self):
        punchingImages = [
            'resources/plebe/plebePunch.png',
            'resources/dpe/dpePunch.png',
            'resources/plebe/plebePunch.png', #'resources/supt/suptPunch.png'
            'resources/plebe/plebePunch.png'] #'resources/acu/acuPunch.png'

        punchImg = pygame.image.load(punchingImages[self.fighterID])
        return punchImg

    def load_running_images(self):
        runningAnimations = [
            ['resources/plebe/plebeRun/0.png','resources/plebe/plebeRun/1.png',
             'resources/plebe/plebeRun/2.png','resources/plebe/plebeRun/3.png',
             'resources/plebe/plebeRun/4.png','resources/plebe/plebeRun/5.png',
             'resources/plebe/plebeRun/6.png'],
            ['resources/dpe/dpeRun/0.png','resources/dpe/dpeRun/1.png',
             'resources/dpe/dpeRun/2.png','resources/dpe/dpeRun/3.png',
             'resources/dpe/dpeRun/4.png','resources/dpe/dpeRun/5.png',
             'resources/dpe/dpeRun/6.png'],
            ['resources/supt/suptRun/0.png','resources/supt/suptRun/1.png',
             'resources/supt/suptRun/2.png','resources/supt/suptRun/3.png',
             'resources/supt/suptRun/4.png','resources/supt/suptRun/5.png',
             'resources/supt/suptRun/6.png'],
            ['resources/acu/acuRun/0.png','resources/acu/acuRun/1.png',
             'resources/acu/acuRun/2.png','resources/acu/acuRun/3.png',
             'resources/acu/acuRun/4.png','resources/acu/acuRun/5.png',
             'resources/acu/acuRun/6.png']]

        running_images = []
        for animation in runningAnimations[self.fighterID]:
            runImg = pygame.image.load(animation)
            running_images.append(runImg)
        return running_images

    def move_right(self, dist, disp_surf):
        self.fighter.centerx = min(self.fighter.centerx+dist,disp_surf.get_width())

    def move_left(self, dist, disp_surf):
        self.fighter.centerx = max(self.fighter.centerx-dist,0)

def health_bars(playerHealth, opponentHealth, display):
    if 200 < playerHealth <= 400:
        playerHealth_color =GREEN
    elif 75 < playerHealth <= 200:
        playerHealth_color = AMBER
    else:
        playerHealth_color = RED

    if 200 < opponentHealth <= 400:
        opponentHealth_color =GREEN
    elif 80 < opponentHealth <= 200:
        opponentHealth_color = AMBER
    else:
        opponentHealth_color = RED

    pygame.draw.rect(display, playerHealth_color, (20, 25, playerHealth, 25))
    pygame.draw.rect(display, opponentHealth_color, (WIDTH-430, 25, opponentHealth, 25))

def play_game(playerID,opponentID):
    def gameover_screen(playerWon):
        gameover = True
        while gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    pygame.quit()
                    interface.Game("resume")
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        gameover = False
                    if event.key == K_q or event.key == K_ESCAPE:
                        gameover = False
                        pygame.quit()
                        interface.Game("resume")
            if playerWon:
                screen.blit(font2.render("You won!",True,GREEN),[330,150])
            else:
                screen.blit(font2.render("You lost!",True,RED),[330,150])
            screen.blit(font1.render("PRESS 'R' TO PLAY AGAIN", True, BLACK),
                [330,290])
            screen.blit(font1.render("PRESS 'Q' TO QUIT", True, BLACK),
                [375,320])
            pygame.display.update()
            screen.blit(washingtonHall_BG, (0, 0))
            game_clock.tick(FPS)

        if gameover == False:
            play_game(playerID,opponentID)
    #############################################################
    pygame.init()
    game_clock = pygame.time.Clock()
    FPS = 25

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 255))
    washingtonHall_BG = pygame.image.load('resources/wh.png')
    font1 = pygame.font.SysFont('comicsansms', 25)
    font2 = pygame.font.SysFont('comicsansms', 80)

    pygame.display.set_caption("Brigade Brawlers")
    display = pygame.display.set_mode((WIDTH,HEIGHT))

    player = Fighter(50,400,playerID-1)
    opponent = Fighter(800,400,opponentID-1)

    screen.fill((255, 255, 255))
    screen.blit(washingtonHall_BG, (0, 0))

    game_clock = pygame.time.Clock()
    FPS = 25

    pygame.key.set_repeat(10,10)
    score = 0
    score_font = pygame.font.SysFont(None,20)

    punching_PlayerImages = [player.standing_image,player.standing_image,
        player.punching_image,player.punching_image]
    punching_OpponentImages = [opponent.standing_image,opponent.standing_image,
        opponent.punching_image,opponent.punching_image]

    seconds = -1
    playerFacingRight = True
    opponentFacingRight = False

    strategy = random.randrange(0,3)
    oppRetreat = False
    activeGame = True
    while activeGame:
        playerMove = 0

        controls = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                activeGame = False
                pygame.quit()
                interface.Game("resume")
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    activeGame = False
                    pygame.quit()
                    interface.Game("resume")
                if controls[K_LEFT]:
                    playerFacingRight = False
                    player.move_left(25,display)
                    playerMove = 1
                if controls[K_RIGHT]:
                    playerFacingRight = True
                    player.move_right(25,display)
                    playerMove = 2
                if controls[K_SPACE]:
                    playerMove = 3
                    if abs(player.fighter.x - opponent.fighter.x) <= 60:
                        opponent.health -= 10
            else:
                playerMove = 0

        screen.blit(washingtonHall_BG, (0,0))

        if playerMove == 0:
            if playerFacingRight:
                display.blit(player.standing_image,player.fighter)
            else:
                display.blit(pygame.transform.flip(player.standing_image,True,False),player.fighter)
        if playerMove == 1:
            player.running_images.append(player.running_images.pop(0))
            flipped_img = pygame.transform.flip(player.running_images[0],True,False)
            display.blit(flipped_img,player.fighter)
        if playerMove == 2:
            player.running_images.append(player.running_images.pop(0))
            display.blit(player.running_images[0],player.fighter)
        if playerMove == 3:
            punching_PlayerImages.append(punching_PlayerImages.pop(0))
            puncing_img = punching_PlayerImages[0]
            if playerFacingRight:
                display.blit(puncing_img,player.fighter)
            else:
                display.blit(pygame.transform.flip(puncing_img,True,False),player.fighter)

        dist = opponent.fighter.centerx-player.fighter.centerx
        oppOnRight = True
        oppInRange = False
        if (dist < 0):
            oppOnRight = False
        if (abs(dist) <= 60):
            oppInRange = True

        oppMove = 0

        if strategy == 0:
            if opponent.health > 350:
                if oppInRange:
                    oppMove = 3
                else:
                    oppMove = 0
            elif opponent.health > 250:
                if oppInRange and opponent.health < 300:
                    oppMove = 3
                elif opponent.fighter.centerx < 100:
                    opponentFacingRight = True
                    oppMove = 0
                else:
                    oppMove = 1
            elif opponent.health > 60:
                if oppInRange and opponent.health > 150:
                    oppMove = 3
                elif opponent.fighter.centerx > 700:
                    opponentFacingRight = False
                    oppMove = 0
                else:
                    oppMove = 2
            else:
                oppMove = 3
        elif strategy == 1:
            if oppRetreat:
                if opponent.fighter.centerx > 100:
                    oppMove = 1
                elif oppInRange:
                    oppMove = 3
                else:
                    opponentFacingRight = True
                    oppMove = 0
            elif opponent.health > 80:
                if oppInRange:
                    oppMove = 3
                elif oppOnRight:
                    oppMove = 1
                else:
                    oppMove = 2
            else:
                if oppOnRight:
                    if opponent.fighter.centerx < 900:
                        oppMove = 2
                    elif abs(dist < 130):
                        oppRetreat = True
                else:
                    oppRetreat = True
        else:
            if opponent.health > 300 and opponent.health < 370:
                oppMove = 3
            elif opponent.health <= 300:
                if opponent.health < 70:
                    if opponent.fighter.centerx > 930:
                        if oppInRange:
                            oppMove = 3
                        else:
                            opponentFacingRight = False
                            oppMove = 0
                    else:
                        oppMove = 2
                elif opponent.fighter.centerx > 50:
                    oppMove = 1
                elif oppInRange:
                    oppMove = 3
                else:
                    opponentFacingRight = True
                    oppMove = 0
            elif opponent.fighter.centerx > 900 and oppInRange == False:
                opponentFacingRight = False
                oppMove = 0
            elif oppOnRight and oppRetreat == False:
                if oppInRange:
                    oppRetreat = True
                    oppMove = 2
                elif opponent.fighter.centerx > 320:
                    oppMove = 1
                else:
                    oppMove = 0
            else:
                oppMove = 2

        if oppMove == 0:
            if opponentFacingRight:
                display.blit(opponent.standing_image,opponent.fighter)
            else:
                display.blit(pygame.transform.flip(opponent.standing_image,True,False),opponent.fighter)
        if oppMove == 1:
            opponentFacingRight = False
            opponent.move_left(25,display)
            opponent.running_images.append(opponent.running_images.pop(0))
            flipped_img = pygame.transform.flip(opponent.running_images[0],True,False)
            display.blit(flipped_img,opponent.fighter)
        if oppMove == 2:
            opponentFacingRight = True
            opponent.move_right(25,display)
            opponent.running_images.append(opponent.running_images.pop(0))
            flipped_img = opponent.running_images[0]
            display.blit(flipped_img,opponent.fighter)
        if oppMove == 3:
            if abs(player.fighter.x - opponent.fighter.x) <= 60:
                player.health -= 10
            punching_OpponentImages.append(punching_OpponentImages.pop(0))
            puncing_img = punching_OpponentImages[0]
            if opponentFacingRight:
                display.blit(puncing_img,opponent.fighter)
            else:
                display.blit(pygame.transform.flip(puncing_img,True,False),opponent.fighter)

        if player.health <= 0 or opponent.health <= 0:
            gameover_screen(player.health > opponent.health)

        health_bars(player.health, opponent.health, display)

        pygame.display.update()
        screen.blit(washingtonHall_BG, (0,0))
        game_clock.tick(FPS)

if __name__=='__main__':
    play_game(1,2)
