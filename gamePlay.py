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
            'resources/supt/suptStanding.png', #'resources/supt/suptStanding.png'
            'resources/acu/acuStanding.png'] #'resources/acu/acuStanding.png'

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
    def gameover_screen():
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
                    if event.key == K_q:
                        gameover = False
                        pygame.quit()
                        interface.Game("resume")

            text = font.render("PRESS 'R' TO PLAY AGAIN // PRESS 'Q' TO QUIT", True, BLACK)
            screen.blit(text, [WIDTH*1//6, HEIGHT//3])
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
    font = pygame.font.SysFont('comicsansms', 25)

    pygame.display.set_caption("Brigade Brawlers")
    display = pygame.display.set_mode((WIDTH,HEIGHT))

    player = Fighter(50,400,playerID-1)
    opponent = Fighter(800,400,opponentID-1)
    player.centerx = 0
    player.centery = 0
    opponent.centerx = pygame.display.get_surface().get_width()
    opponent.centery = pygame.display.get_surface().get_width()

    screen.fill((255, 255, 255))
    screen.blit(washingtonHall_BG, (0, 0))

    game_clock = pygame.time.Clock()
    FPS = 25

    pygame.key.set_repeat(10,10)
    score = 0
    score_font = pygame.font.SysFont(None,20)

    seconds = -1
    playerFacingRight = True
    opponentFacingRight = False
    strategy = random.randrange(0,2)

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
                        pass
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
            if playerFacingRight:
                display.blit(player.punching_image,player.fighter)
            else:
                display.blit(pygame.transform.flip(player.punching_image,True,False),player.fighter)

        """
        def opponentAI():
            ticks = pygame.time.get_ticks()
            if strategy == 0:
                while (ticks < 4000):
                    opponentFacingRight = False
                    opponent.move_left(25,display)
                    opponent.running_images.append(opponent.running_images.pop(0))
                    flipped_img = pygame.transform.flip(opponent.running_images[0],True,False)
                    display.blit(flipped_img,player.fighter)

            if strategy == 1:
                pass

        opponentAI()
        """




        if player.health <= 0 or opponent.health <= 0:
            gameover_screen()

        health_bars(player.health, opponent.health, display)

        pygame.display.update()
        screen.blit(washingtonHall_BG, (0,0))
        game_clock.tick(FPS)

if __name__=='__main__':
    play_game(1,2)
