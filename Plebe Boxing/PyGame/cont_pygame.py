
# File: pygame_example.py
# Starter code for pygame lessons.

import pygame, sys, random
from pygame.locals import *


# Constant color definitions
           #R    G    B
ORANGE =   (255, 128, 0)
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)

# Set up initial game board (window) for the game
def init_main_window(dimensions, caption):
	pygame.init()
	pygame.display.set_caption(caption)
	return pygame.display.set_mode(dimensions)

# Load the cat images
def load_cat_images():
	file_names = ['images/nyan-1.gif','images/nyan-2.gif','images/nyan-3.gif','images/nyan-4.gif','images/nyan-5.gif','images/nyan-6.gif']
	cat_images = []
	for file_name in file_names:
		cat_img = pygame.image.load(file_name)
		cat_images.append(cat_img)
	return cat_images

def move_cat(cat,event,dist,disp_surf):
	if event.key == K_RIGHT:
		cat.centerx = min(cat.centerx+dist,disp_surf.get_width())
	elif event.key == K_DOWN:
		cat.centery = min(cat.centery+dist,disp_surf.get_height())
	elif event.key == K_LEFT:
		cat.centerx = max(cat.centerx-dist,0)
	elif event.key == K_UP:
		cat.centery = max(cat.centery-dist,0)
	elif event.key == K_RIGHT and event.key == K_UP:
		cat.centerx = min(cat.centerx+dist,disp_surf.get_width())
		cat.centery = max(cat.centery-dist,0)

#determine if the cat collides with cupcake and hence eats it
def eats_cupcake(cat,cup):
	if cat.colliderect(cup):
			#cat eats the cupcake, respawn a new cupcake
		cup.centerx = random.randrange(pygame.display.get_surface().get_width())
		cup.centery = random.randrange(pygame.display.get_surface().get_height())
		return True
	else:
		return False

#determin if the cat collides with the broccoli and hence eats it
def eats_broccoli(cat,broc):
	if cat.colliderect(broc):
		#cat eats the broc, respawn a new broc
		broc.centerx = random.randrange(pygame.display.get_surface().get_width())
		broc.centery = random.randrange(pygame.display.get_surface().get_height())
		return True
	else:
		return False

#Write text onto screen/game_board
def draw_text(text,font,surface,x,y):
	textobj = font.render(text,1,WHITE)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj,textrect)

def terminate():
	pygame.quit()
	sys.exit()


def play_game():
	DISPLAYSURF = init_main_window((400,300),"Nyan Cat!")

	# Load the cat image
	#cat_img = pygame.image.load("smallNyan.gif")
	#cat = cat_img.get_rect()
	cat_images = load_cat_images()
	cat = cat_images[0].get_rect()

	#Add a broccoli image
	broccoli = pygame.image.load('images/broccoli.gif')
	broc = broccoli.get_rect()
	broc.move_ip(50,50)

	# Add a cupcake image
	cupcake = pygame.image.load('images/cupcake.gif')
	cup = cupcake.get_rect()
	cup.move_ip(100,50)

	# Set up the clock
	fps_clock = pygame.time.Clock()
	FPS = 25

	#optional key holding
	pygame.key.set_repeat(50,50)
	score = 0
	font = pygame.font.SysFont(None,20)

	# While game is in play, process the events
	while True:
		#####
		# Process events in the event queue
		#####
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()

				move_cat(cat,event,10,DISPLAYSURF)
		#####
		# Make changes to the display parameters
		#####
		DISPLAYSURF.fill(NAVYBLUE)
		# DISPLAYSURF.blit(cat_img, cat)
		DISPLAYSURF.blit(cat_images[0],cat)
		cat_images.append(cat_images.pop(0))

		if eats_cupcake(cat,cup):
			score+=1

		if eats_broccoli(cat,broc):
			score-=1
			#print(score)
		draw_text("Score: " + str(score), font, DISPLAYSURF, 10, 0)

		# DISPLAY and move cupcake
		DISPLAYSURF.blit(cupcake,cup)
		cup.x = cup.x+5 if cup.x < DISPLAYSURF.get_width() else -cupcake.get_width()

		#DISPLAY and move broccoli
		DISPLAYSURF.blit(broccoli,broc)
		broc.x = broc.x+5 if broc.x < DISPLAYSURF.get_width() else -broccoli.get_width()

		# Update the display
		pygame.display.update()

		fps_clock.tick(FPS)

if __name__=='__main__':
    play_game()
