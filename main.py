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

speed = 6		
robot1X = display_width/4
robot1Y = display_height/2

robot2X = (display_width/4) * 3
robot2Y = display_height/2

def frame():
	frame = pygame.image.load('./spr_FRC_game/game_frame_large.png')
	gameDisplay.blit(frame,(0, 0))
	
def player1(x, y):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	gameDisplay.blit(playerTex, (x, y))
	
def player2(x, y):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	gameDisplay.blit(playerTex, (x, y))

while not crashed:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			crashed = True
	keyHandler = pygame.key.get_pressed()

	if(keyHandler[273]): #Up
		robot1Y -= speed
	elif(keyHandler[274]): #Down
		robot1Y += speed
	if(keyHandler[275]): #Right
		robot1X += speed
	elif(keyHandler[276]): #Left
		robot1X -= speed
	
	if(keyHandler[97]):
		robot2X -= speed
	if(keyHandler[115]):
		robot2Y += speed
	if(keyHandler[100]):
		robot2X += speed
	if(keyHandler[119]):
		robot2Y -= speed
	frame()		
	player1(robot1X, robot1Y)
	player2(robot2X, robot2Y)
	
	#check bounds
	#===============================================
	
	if(robot1X <= 0):
		robot1X = 0
	if(robot1X >= display_width - 24):
		robot1X = display_width - 24 #Acounting the size of the image 
	if(robot1Y <= 0):
		robot1Y = 0
	if(robot1Y >= display_height - 24):
		robot1Y = display_height - 24 #Acounting the size of the image 
	
	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()