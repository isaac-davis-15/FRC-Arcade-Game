import pygame
import time 
import random

display_width = 720
display_height = 600

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('FRC Game')

clock = pygame.time.Clock()
crashed = False

scoreFont = pygame.font.SysFont("monospace", 21)

roboLength = 48

"""
	Enviorment varibles for the code
"""
white = (255, 255, 255)

speed = 12		
robot1X = display_width/4
robot1Y = display_height/2
robot2X = (display_width/4) * 3
robot2Y = display_height/2
ballX = []
ballY = []
score1 = 0
score2 = 0

print("Balls:")

ballX = random.sample(range(-100, 100), 50)
ballY = random.sample(range(-100, 100), 50)



def ballCollision():
	global ballX
	global ballY
	
	newX = ballX
	newY = ballY
	
	if len(ballX) == len(ballY):
		i = 0 
		while i < len(ballX):
			xArg = robot1X < (display_width/2 + ballX[i]) < (robot1X + roboLength) 
			yArg = robot1Y < (display_width/2 + ballY[i]) - roboLength < (robot1Y + roboLength)
			if(xArg and yArg):
				print("test")
				newX.remove(ballX[i])
				newY.remove(ballY[i])
			i += 1
				
	else:
		print("BALL CORD. ERROR")
		pygame.quit()
		exit()
		
	ballX = newX
	ballY = newY
	
def scoreFrame():
	frame = pygame.image.load('./spr_FRC_game/game_frame_large.png')
	gameDisplay.blit(frame,(0, 0))
	
def cornFrame():  
	#240 x 240
	frame = pygame.image.load('./spr_FRC_game/corn_map.png')
	gameDisplay.blit(frame, ((display_width/2) - 240, (display_height/2) - 240))

def drawBall(xCorr, yCorr):
	frame = pygame.image.load('./spr_FRC_game/ball.png')
	for i in range(len(ballX)):
		gameDisplay.blit(frame, ((display_width/2) + xCorr[i], (display_height/2) + yCorr[i]))
	
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
	
def displayScore():
	lable1 = scoreFont.render(str(score1), 1, (0, 0, 0))
	textWidth1 = lable1.get_width()
	gameDisplay.blit(lable1, ((display_width/2 - textWidth1/2) - 125, 0))
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
	elif(keyHandler[274] and robot1Y <= (bottom_border - roboLength) - speed): #Down
		robot1Y += speed
	if(keyHandler[275] and robot1X <= (right_border - roboLength) - speed): #Right
		robot1X += speed
	elif(keyHandler[276] and robot1X >= left_border + speed): #Left
		robot1X -= speed
	
	if(keyHandler[97] and robot2X >= left_border + speed): #Left 
		robot2X -= speed
	elif(keyHandler[115] and robot2Y <= (bottom_border - roboLength) - speed): #Down
		robot2Y += speed
	if(keyHandler[100] and robot2X <= (right_border - roboLength) - speed): #Right
		robot2X += speed
	elif(keyHandler[119] and robot2Y >= top_border + speed): #Up
		robot2Y -= speed
		
	#Update frames and player cord. 
	#(the order of the code is the order at which the images are drawn)
	#===============================================
	scoreFrame()
	cornFrame()
	drawBlueGoal()
	drawRedGoal()
	displayScore()
	drawBall(ballX, ballY)
	player1(robot1X, robot1Y)
	player2(robot2X, robot2Y)
	ballCollision()
	
	#update the screen, and set clock time
	#===============================================
	pygame.display.update()
	clock.tick(60)
	
#exit if game loop is broken 
#===================================================	
pygame.quit()
exit()