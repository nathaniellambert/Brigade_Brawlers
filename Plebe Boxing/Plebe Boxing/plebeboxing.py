# import all modules
import pygame, sys, random
from pygame.locals import *

# set all constant variables

# colors
GOLD = (212,175,55)
BLACK = (0,0,0)
RED = (181,16,16)

# display size
displayh = 600
displayw = 1200





# Set up game window
def main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)

# Quit the game
def terminate():
    pygame.quit()
    sys.exit()

# Load the Fighters
def load_fighter_images():
    file_names = ['fighter1.gif']
    fighter_images = []
    for file_name in file_names:
        fighter_img = pygame.image.load(file_name)
        fighter_images.append(fighter_img)
    return(fighter_images)

# Move a fighter
def move_fighter(fighter,event,dist,disp_surf):
    if event.key == K_RIGHT: fighter.centerx = min(fighter.centerx+dist,disp_surf.get_width())
    if fighter.x < 0 : fighter.x = 0
    if event.key == K_LEFT: fighter.centerx = max(fighter.centerx-dist,0)
    if fighter.right > displayw : fighter.right = displayw



def play_game():
# make display appear
    display = main_window((displayw,displayh),"PE117")
# load in fighters
    fighter_images = load_fighter_images()
    fighter = fighter_images[0].get_rect(topleft = (0,int(displayh/2)))
# set clock
    game_clock = pygame.time.Clock()
    FPS = 25
# hold the keys down
    pygame.key.set_repeat(50,50)
    score = 0
    font = pygame.font.SysFont(None,20)

# keep the game running
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
# move fighter1 in game
                move_fighter(fighter,event,10,display)
# give display background color
        display.fill(GOLD)
# make fighter appear on surface
        display.blit(fighter_images[0],fighter)
        fighter_images.append(fighter_images.pop(0))
# update display (MUST BE LAST)
        pygame.display.update()
# make clock tick
        game_clock.tick(FPS)










if __name__=='__main__':
    play_game()
