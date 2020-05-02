import pygame, sys, random, os
from pygame.locals import *
import interface

os.environ['SDL_VIDEO_CENTERED'] = '1'

def play_game():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    activeGame = True

    is_blue = True
    while activeGame:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_blue = not is_blue
                if event.key == K_ESCAPE:
                    activeGame = False
                    pygame.quit()
                    interface.Game("resume")


        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)

        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

        pygame.display.flip()

if __name__=='__main__':
    play_game()
