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

player1_blue_id = 0
player1_red_id = 1
player2_blue_id = 2
player2_red_id = 3
		

def frame(x, y):
	frame = pygame.image.load('game_frame_large.png')
	gameDisplay.blit(frame, (x, y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    frame(0, 0)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()