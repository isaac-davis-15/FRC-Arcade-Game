import pygame
from pygame.locals import *
import time 
import random
import os

#game varibles screen size = 1280x1024

display_width = int(1280)
display_height = int(1024)

crashed = False

#Player varibles

speed = 12		

roboLength = 48

robot1X = (display_width/4) * 3
robot1Y = display_height/2

robot2X = display_width/4
robot2Y = display_height/2

robot1Staged = 0
robot2Staged = 0

robot1StagedPos = random.sample(range(-20, 20), 6)
robot2StagedPos = random.sample(range(-20, 20), 6)

player1Rot = 0
player2Rot = 0

#ball varibles

ballX = random.sample(range(-200, 200), 50)
ballY = random.sample(range(-200, 200), 50)

#score varibles

score1 = 0
score2 = 0

#init

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('FRC Game')

clock = pygame.time.Clock()

scoreFont = pygame.font.SysFont("monospace", 21)

#make fullscreen

screen = pygame.display.get_surface()
tmp = screen.convert()
caption = pygame.display.get_caption()
cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
w,h = screen.get_width(),screen.get_height()
flags = screen.get_flags()
bits = screen.get_bitsize()
    
screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
screen.blit(tmp,(0,0))
pygame.display.set_caption(*caption)

pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def checkGoal():
	global robot1Staged
	global robot2Staged
	global score1
	global score2

	goal1Rect = pygame.Rect(display_width/2 - 360, display_height/2 - 360, 100, 100) #blue
	goal2Rect = pygame.Rect((display_width/2 + 360) - 100, (display_height/2 + 360) - 100, 100, 100) #red
	
	robotRect1 = pygame.Rect(robot1X, robot1Y, roboLength, roboLength)
	robotRect2 = pygame.Rect(robot2X, robot2Y, roboLength, roboLength)
	
	print(str(robot1Staged) + ", " + str(robot2Staged))
	
	if(robotRect1.colliderect(goal1Rect) and 1 <= robot1Staged <= 4):
		robot1Staged -= 1
		score1 += 1
	if(robotRect2.colliderect(goal2Rect) and 1 <= robot2Staged <= 4):
		print("Colo")
		robot2Staged -= 1
		score2 += 1
		
def ballCollision(stage1, stage2):
	global ballX
	global ballY
	global robot1Staged
	global robot2Staged
	
	newX = ballX
	newY = ballY
	
	if len(ballX) == len(ballY):
		i = 0 
		while i < len(ballX):
			OnexArg = robot1X < (display_width/2 + ballX[i]) < (robot1X + roboLength) 
			OneyArg = robot1Y < (display_width/2 + ballY[i]) - roboLength < (robot1Y + roboLength)
			
			TwoxArg = robot2X < (display_width/2 + ballX[i]) < (robot2X + roboLength) 
			TwoyArg = robot2Y < (display_width/2 + ballY[i]) - roboLength < (robot2Y + roboLength)

			if(OnexArg and OneyArg and stage1 and robot1Staged < 3):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				robot1Staged += 1
			elif(TwoxArg and TwoyArg and stage2 and robot2Staged < 3):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				robot2Staged += 1
			i += 1
				
	else:
		print("BALL CORD. ERROR")
		pygame.quit()
		exit()
		
	ballX = newX
	ballY = newY
	
def drawStagedBalls(): 
	global robot1Staged
	global robot2Staged
	
	for i in range(robot1Staged):
		img = pygame.image.load('./spr_FRC_game/ball.png')
		gameDisplay.blit(img, ((robot1X + roboLength/2) + robot1StagedPos[i], (robot1Y + roboLength/2) + robot1StagedPos[i]))

	for i in range(robot2Staged):
		img = pygame.image.load('./spr_FRC_game/ball.png')
		gameDisplay.blit(img, ((robot2X + roboLength/2) + robot2StagedPos[i], (robot2Y + roboLength/2) + robot2StagedPos[i]))
	 
def scoreFrame():
	frame = pygame.image.load('./spr_FRC_game/game_frame_large.png')
	gameDisplay.blit(frame,(0, 0))
	
def cornFrame():  
	#180 x 180
	frame = pygame.image.load('./spr_FRC_game/corn_map.png')
	gameDisplay.blit(frame, ((display_width/2) - 360, (display_height/2) - 360))

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
	gameDisplay.blit(tex, (display_width/2 + (360 - 50), display_height/2 + (360 - 50)))
	
def drawBlueGoal():
	tex = pygame.image.load('./spr_FRC_game/blue_goal.png')
	gameDisplay.blit(tex, (display_width/2 - 360, display_height/2 - 360))
	
def displayScore():
	lable2 = scoreFont.render(str(score2), 1, (0, 0, 0))
	lable1 = scoreFont.render(str(score1), 1, (0, 0, 0))
	elapTime = int(120 - (pygame.time.get_ticks()/1000)) 
	elapTimeRender = scoreFont.render(str(elapTime), 1, (255, 255, 255))
	textWidth1 = lable1.get_width()
	textWidth2 = lable2.get_width()
	gameDisplay.blit(lable2, ((display_width/2 - textWidth1/2) - 75, 0))
	gameDisplay.blit(lable1, ((display_width/2 - textWidth2/2) + 75, 0))	
	gameDisplay.blit(elapTimeRender, (display_width/2, 50))
	return elapTime
	
def collideReset():
	global robot1X
	global robot1Y
	global robot2X
	global robot2Y

	p1CenterX = robot1X + roboLength/2
	p1CenterY = robot1Y + roboLength/2
	
	Rect1 = pygame.Rect(robot1X, robot1Y, roboLength, roboLength)
	Rect2 = pygame.Rect(robot2X, robot2Y, roboLength, roboLength)
	
	if(Rect1.colliderect(Rect2)):
		print("COLLIDE")
		if(robot2X < p1CenterX < robot2X + roboLength and robot1Y < robot2Y):
			robot1Y -= speed/2
			robot2Y += speed/2
		elif(robot2X < p1CenterX < robot2X + roboLength and robot1Y > robot2Y):
			robot1Y += speed/2
			robot2Y -= speed/2
		elif(robot2Y < p1CenterY < robot2Y + roboLength and robot1X < robot2X):
			robot1X -= speed/2
			robot2X += speed/2
		elif(robot2Y < p1CenterY < robot2Y + roboLength and robot1X > robot2X):
			robot1X += speed/2
			robot2X -= speed/2
scoreFrame()

while not crashed:
	#Check if the game is trying to be closed
	#==============================================
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			crashed = True
			
	#Check keyboard and change the cord.
	#==============================================
	
	top_border = display_height/2 - 360
	bottom_border = display_height/2 + 360
	right_border = display_width/2 + 360
	left_border = display_width/2 - 360
	
	keyHandler = pygame.key.get_pressed()
	
	#spacer
	
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
		
	#Check if players can pickup balls
	if(robot1Staged < 3):
		can1PickUp = True
	else:
		can1PickUp = False
		
	if(robot2Staged < 3):
		can2PickUp = True
	else: 
		can2PickUp = False
	
	#Update frames and player cord. 
	#(the order of the code is the order at which the images are drawn)
	#==============================================
	cornFrame()
	drawBlueGoal()
	drawRedGoal()
	elap = displayScore()
	drawBall(ballX, ballY)
	player1(robot1X, robot1Y, player1Rot)
	player2(robot2X, robot2Y, player2Rot)
	ballCollision(can1PickUp, can2PickUp)
	checkGoal()
	drawStagedBalls()
	collideReset()
	
	#if the timer is 0 then crashed it True
	if(elap == 0):
		crashed = True
	
	#update the screen, and set clock time
	#===============================================
	pygame.display.update()
	clock.tick(60)
	
#exit if game loop is broken 
#===================================================	
pygame.quit()
exit()
