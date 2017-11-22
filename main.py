import pygame
import time 

display_width = 720
display_height = 600

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Test me')

clock = pygame.time.Clock()
crashed = False

"""
	Enviorment varibles for the code
"""
white = (255, 255, 255)
		
robotX = display_width/2
robotY = display_height/2

def frame():
	frame = pygame.image.load('game_frame_large.png')
	gameDisplay.blit(frame,(0, 0))
	
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		else:	
			pygame.display.update()
			clock.tick(60)
	frame()		

pygame.quit()
quit()