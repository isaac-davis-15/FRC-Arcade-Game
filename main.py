import pygame
import time 

display_width = 720
display_height = 600

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('FRC Game')

clock = pygame.time.Clock()
crashed = False

"""
	Enviorment varibles for the code
"""
white = (255, 255, 255)

speed = 12		
robot1X = display_width/4
robot1Y = display_height/2
robot2X = (display_width/4) * 3
robot2Y = display_height/2
balls = []

def scoreFrame():
	frame = pygame.image.load('./spr_FRC_game/game_frame_large.png')
	gameDisplay.blit(frame,(0, 0))
	
def cornFrame():  
	#240 x 240
	frame = pygame.image.load('./spr_FRC_game/corn_map.png')
	gameDisplay.blit(frame, ((display_width/2) - 240, (display_height/2) - 240))

def ballFrame() :
	frame = pygame.image.load('./spr_FRC_game/ball.png')
	gameDisplay.blit(frame, ((display_width/2), (display_height/2)))
	
def player1(x, y):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	gameDisplay.blit(playerTex, (x, y))
	
def player2(x, y):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	gameDisplay.blit(playerTex, (x, y))

def drawRedGoal():
	tex = pygame.image.load('./spr_FRC_game/read_goal.png')
	gameDisplay.blit(tex, (display_width/2 + (240 - 50), display_height/2 + (240 - 50)))
	
def drawBlueGoal():
	tex = pygame.image.load('./spr_FRC_game/blue_goal.png')
	gameDisplay.blit(tex, (display_width/2 - 240, display_height/2 - 240))
	
while not crashed:
	#Check if the game is trying to be closed
	#==============================================
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			crashed = True
			
	#Check keyboard and change the cord.
	#==============================================
	
	top_border = display_height/2 - 240
	bottom_border = display_height/2 + 240
	right_border = display_width/2 + 240
	left_border = display_width/2 - 240
	
	keyHandler = pygame.key.get_pressed()
	if(keyHandler[273] and robot1Y >= top_border + speed): #Up
		robot1Y -= speed
	elif(keyHandler[274] and robot1Y <= (bottom_border - 24) - speed): #Down
		robot1Y += speed
	if(keyHandler[275] and robot1X <= (right_border - 24) - speed): #Right
		robot1X += speed
	elif(keyHandler[276] and robot1X >= left_border + speed): #Left
		robot1X -= speed
	
	if(keyHandler[97] and robot2X >= left_border + speed): 
		print("LEFT")
		robot2X -= speed
	elif(keyHandler[115] and robot2Y <= (bottom_border - 24) - speed):
		print("DOWN")
		robot2Y += speed
	if(keyHandler[100] and robot2X <= (right_border - 24) - speed): 
		print("RIGHT")
		robot2X += speed
	elif(keyHandler[119] and robot2Y >= top_border + speed):
		print("UP")
		robot2Y -= speed
	
	#if(keyHandler[97]):
	#	print("lEFT")
	#	robot2X -= speed
	#if(keyHandler[115]):
	#	print("DOWN")
	#	robot2Y += speed
	#if(keyHandler[100]):
	#	print("RIGHT")
	#	robot2X += speed
	#if(keyHandler[119]):
	#	print("UP")
	#	robot2Y -= speed
		

	#Update frames and player cord. 
	#(the order of the code is the order at which the images are drawn)
	#===============================================
	scoreFrame()
	cornFrame()
	drawBlueGoal()
	drawRedGoal()
	ballFrame()
	player1(robot1X, robot1Y)
	player2(robot2X, robot2Y)
	
	
	#check bounds
	#===============================================
	
	if():
		robot1X = left_border
	if():
		robot1X = right_border - 24 #Acounting the size of the image 
	if():
		robot1Y = top_border
	if():
		robot1Y = bottom_border - 24 #Acounting the size of the image 
	
	if(robot2X <= left_border):
		robot2X = left_border
	if(robot2X >= right_border - 24):
		robot2X = right_border - 24 #Acounting the size of the image 
	if(robot2Y <= top_border):
		robot2Y = top_border
	if(robot2Y >= bottom_border - 24):
		robot2Y = bottom_border - 24 #Acounting the size of the image 
	
	#update the screen, flip the display, and set clock time
	#===============================================
	pygame.display.update()
	clock.tick(60)
	
#exit if game loop is broken 
#===================================================	
pygame.quit()
exit()