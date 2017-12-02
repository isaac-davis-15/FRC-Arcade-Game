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
	Player varibles
"""
white = (255, 255, 255)

speed = 12		
robot1X = (display_width/4) * 3
robot1Y = display_height/2
robot2X = display_width/4
robot2Y = display_height/2
ballX = []
ballY = []
score1 = 0
score2 = 0

ballX = random.sample(range(-100, 100), 50)
ballY = random.sample(range(-100, 100), 50)

player1Rot = 0
player2Rot = 0

def ballCollision():
	global ballX
	global ballY
	global score1
	global score2
	
	newX = ballX
	newY = ballY
	
	if len(ballX) == len(ballY):
		i = 0 
		while i < len(ballX):
			OnexArg = robot1X < (display_width/2 + ballX[i]) < (robot1X + roboLength) 
			OneyArg = robot1Y < (display_width/2 + ballY[i]) - roboLength < (robot1Y + roboLength)
			
			TwoxArg = robot2X < (display_width/2 + ballX[i]) < (robot2X + roboLength) 
			TwoyArg = robot2Y < (display_width/2 + ballY[i]) - roboLength < (robot2Y + roboLength)

			if(OnexArg and OneyArg):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				score1+=1
			elif(TwoxArg and TwoyArg):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				score2+=1
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
	
def player1(x, y, rot):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	playerRot = pygame.transform.rotate(playerTex, rot)
	gameDisplay.blit(playerRot, (x, y))
	
def player2(x, y, rot):
	playerTex = pygame.image.load('./spr_FRC_game/robo_1.png')
	playerRot = pygame.transform.rotate(playerTex, rot)
	gameDisplay.blit(playerRot, (x, y))

def drawRedGoal():
	tex = pygame.image.load('./spr_FRC_game/read_goal.png')
	gameDisplay.blit(tex, (display_width/2 + (240 - 50), display_height/2 + (240 - 50)))
	
def drawBlueGoal():
	tex = pygame.image.load('./spr_FRC_game/blue_goal.png')
	gameDisplay.blit(tex, (display_width/2 - 240, display_height/2 - 240))
	
def displayScore():
	lable2 = scoreFont.render(str(score2), 1, (0, 0, 0))
	lable1 = scoreFont.render(str(score1), 1, (0, 0, 0))
	textWidth1 = lable1.get_width()
	textWidth2 = lable2.get_width()
	gameDisplay.blit(lable1, ((display_width/2 - textWidth1/2) - 125, 0))
	gameDisplay.blit(lable2, ((display_width/2 - textWidth2/2) + 125, 0))	
	
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
		player1Rot = 180
	elif(keyHandler[274] and robot1Y <= (bottom_border - roboLength) - speed): #Down
		robot1Y += speed
		player1Rot = 0
	if(keyHandler[275] and robot1X <= (right_border - roboLength) - speed): #Right
		robot1X += speed
		player1Rot = 90
	elif(keyHandler[276] and robot1X >= left_border + speed): #Left
		robot1X -= speed
		player1Rot = 270
	
	if(keyHandler[97] and robot2X >= left_border + speed): #Left 
		robot2X -= speed
		player2Rot = 270
	elif(keyHandler[115] and robot2Y <= (bottom_border - roboLength) - speed): #Down
		robot2Y += speed
		player2Rot = 0
	if(keyHandler[100] and robot2X <= (right_border - roboLength) - speed): #Right
		robot2X += speed
		player2Rot = 90
	elif(keyHandler[119] and robot2Y >= top_border + speed): #Up
		robot2Y -= speed
		player2Rot = 180
		
	#Update frames and player cord. 
	#(the order of the code is the order at which the images are drawn)
	#===============================================
	scoreFrame()
	cornFrame()
	drawBlueGoal()
	drawRedGoal()
	displayScore()
	drawBall(ballX, ballY)
	player1(robot1X, robot1Y, player1Rot)
	player2(robot2X, robot2Y, player2Rot)
	ballCollision()
	
	#update the screen, and set clock time
	#===============================================
	pygame.display.update()
	clock.tick(60)
	
#exit if game loop is broken 
#===================================================	
pygame.quit()
exit()