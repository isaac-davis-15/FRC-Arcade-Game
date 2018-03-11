import pygame
from pygame.locals import *
import time 
import random
import os
import RPi.GPIO as GPIO
#game varibles screen size = 1280x1024

display_width = int(1280)
display_height = int(1024)

crashed = False

speed = 12

roboLength = 48

robot1X = display_width/4
robot1Y = display_height/2

robot2X = (display_width/8)*5
robot2Y = display_height/2

robot1Staged = 0
robot2Staged = 0

robot1StagedPos = random.sample(range(-20, 20), 6)
robot2StagedPos = random.sample(range(-20, 20), 6)

player1Rot = 0
player2Rot = 0

#ball varibles
ballX = []
ballY = []

ballX = random.sample(range(-200, 200), 50)
ballY = random.sample(range(-200, 200), 50)

#score varibles

score1 = 0
score2 = 0


def initReset():
	global speed
	global roboLength
	global robot1X
	global robot1Y
	global robot2X
	global robot2Y
	global robot1Staged
	global robot2Staged
	global robot1StagedPos
	global robot2StagedPos
	global player1Rot
	global player2Rot 
	global ballX
	global ballY
	global score1
	global score2
	
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
	ballX = []
	ballY = []
	
	ballX = random.sample(range(-200, 200), 50)
	ballY = random.sample(range(-200, 200), 50)

	#score varibles

	score1 = 0
	score2 = 0

#Pygame Init

pygame.init()

GPIO.setmode(GPIO.BCM)

pins = [4, 17, 27, 22, 5, 6, 13, 19, 18, 23, 24, 25, 12, 20]

for i in range(len(pins)):
        GPIO.setup(pins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('FRC Game')

os.environ["SDL_FBDEV"] = "/dev/fb0"

clock = pygame.time.Clock()

scoreFont = pygame.font.SysFont("monospace", 30)

crashed = False
crash = False

#make fullscreen

# screen = pygame.display.get_surface()
# tmp = screen.convert()
# caption = pygame.display.get_caption()
# cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
# w,h = screen.get_width(),screen.get_height()
# flags = screen.get_flags()
# bits = screen.get_bitsize()
    
# screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
# screen.blit(tmp,(0,0))
# pygame.display.set_caption(*caption)

# pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
# pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def checkGoalPlayerOne():
	global robot1Staged
	global score1
	
	if(robot1Staged > 0):
		robot1Staged -= 1
		score1 += 1
	
def checkGoalPlayerTwo(): 
	global robot2Staged
	global score2

	if(robot2Staged > 0):
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
			OneyArg = robot1Y < (display_height/2 + ballY[i]) - roboLength < (robot1Y + roboLength)
			
			TwoxArg = robot2X < (display_width/2 + ballX[i]) < (robot2X + roboLength) 
			TwoyArg = robot2Y < (display_height/2 + ballY[i]) - roboLength < (robot2Y + roboLength)

			if(OnexArg and OneyArg and stage1 and robot1Staged < 3):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				robot1Staged += 1
			if(TwoxArg and TwoyArg and stage2 and robot2Staged < 3):
				newX.remove(ballX[i])
				newY.remove(ballY[i])
				robot2Staged += 1
			i += 1
				
	else:
		pygame.quit()
		exit()
		
	ballX = newX
	ballY = newY
	
def drawStagedBalls(): 
	global robot1Staged
	global robot2Staged
	
	for i in range(robot1Staged):
		img = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/ball.png')
		gameDisplay.blit(img, ((robot1X + roboLength/2) + robot1StagedPos[i], (robot1Y + roboLength/2) + robot1StagedPos[i]))

	for i in range(robot2Staged):
		img = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/ball.png')
		gameDisplay.blit(img, ((robot2X + roboLength/2) + robot2StagedPos[i], (robot2Y + roboLength/2) + robot2StagedPos[i]))
	 
def backFrame():
	frame = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/bgFrame.bmp')
	gameDisplay.blit(frame,(0, 0))
	
def drawBall(xCorr, yCorr):
	frame = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/ball.png')
	for i in range(len(ballX)):
		gameDisplay.blit(frame, ((display_width/2) + xCorr[i], (display_height/2) + yCorr[i]))
	
def player1(x, y, rot):
	playerTex = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/robo_1.png')
	playerRot = pygame.transform.rotate(playerTex, rot)
	gameDisplay.blit(playerRot, (x, y))
	
def player2(x, y, rot):	
	playerTex = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/robo_2.png')
	playerRot = pygame.transform.rotate(playerTex, rot)
	gameDisplay.blit(playerRot, (x, y))
	
def displayScore():
	lable2 = scoreFont.render(str(score2), 1, (0, 0, 0))
	lable1 = scoreFont.render(str(score1), 1, (0, 0, 0))
	textWidth1 = lable1.get_width()
	textWidth2 = lable2.get_width()
	gameDisplay.blit(lable2, ((display_width/2 - textWidth1/2) + 75, 5))
	gameDisplay.blit(lable1, ((display_width/2 - textWidth2/2) - 75, 5))	
	
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

def showSecret():
	background = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/Secret.jpg')
	gameDisplay.blit(background, (0, 0))
	pygame.display.update()
	time.sleep(10)
			
def game():
	timer = pygame.time.get_ticks()
	
	global crashed
	global crash
	global robot1X
	global robot1Y
	global robot2X
	global robot2Y
	global player1Rot
	global player2Rot
	crash = True

	while not crashed:
		
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				crashed = True
			
		
		top_border = display_height/2 - 360
		bottom_border = display_height/2 + 360
		right_border = display_width/2 + 360
		left_border = display_width/2 - 360
		
		keyHandler = pygame.key.get_pressed()
		
		#Player 1 controls
		if(GPIO.input(4) != 1 and robot1Y >= top_border + speed): #Up
			robot1Y -= speed
			player1Rot = 180
		
		if(GPIO.input(17) != 1 and robot1Y <= (bottom_border - 2*(roboLength))): #Down
			robot1Y += speed
			player1Rot = 0
		
		if(GPIO.input(22) != 1 and robot1X <= (right_border - 2*(roboLength))): #Right
			robot1X += speed
			player1Rot = 90
		
		if(GPIO.input(27) != 1 and robot1X >= left_border + speed): #Left
			robot1X -= speed
			player1Rot = 270
			
		
		
		#Player 2 controls
		if(GPIO.input(23) != 1 and robot2X >= left_border + speed): #Left 
			robot2X -= speed
			player2Rot = 270
		if(GPIO.input(18) != 1 and robot2Y <= (bottom_border - roboLength) - speed): #Down
			robot2Y += speed
			player2Rot = 0
		if(GPIO.input(24) != 1 and robot2X <= (right_border - roboLength) - speed): #Right
			robot2X += speed
			player2Rot = 90
		if(GPIO.input(19) != 1 and robot2Y >= top_border + speed): #Up
			robot2Y -= speed
			player2Rot = 180
				
		# <= (display_width/2 - 360) + 100 
		# <= (display_height/2 - 360) + 100
		if(GPIO.input(6) != 1 and robot1X >= (display_width/2 + 360) - 150 and robot1Y >= (display_height/2 + 360) - 150):
			checkGoalPlayerOne()
			print("drop")
		
		if(GPIO.input(12) != 1 and robot2X <= (display_width/2 - 360) + 100 and robot2Y <= (display_height/2 - 360) + 100): 
			checkGoalPlayerTwo()
		
		print(str(robot1X) + ", " + str((display_width/2 + 360) - 150))
		print(str(robot1Y) + ", " + str((display_height/2 + 360) - 150))
		
		#This next if statment is for testing
			
		if(keyHandler[K_ESCAPE]):
			crashed = True
			crash = True



		if(robot1Staged < 3 and GPIO.input(5) != 1):
			can1PickUp = True
		else:
			can1PickUp = False
			
		if(robot2Staged < 3 and GPIO.input(20) != 1):
			can2PickUp = True
		else: 
			can2PickUp = False


		backFrame()
		displayScore()
		drawBall(ballX, ballY)
		player1(robot1X, robot1Y, player1Rot)
		player2(robot2X, robot2Y, player2Rot)
		ballCollision(can1PickUp, can2PickUp)
		drawStagedBalls()
		collideReset()
		
		if((pygame.time.get_ticks() - timer)/1000 >= 60):
			crashed = True
			menu()
			
		elapTime = 60 - int((pygame.time.get_ticks() - timer)/1000) 
		elapTimeRender = scoreFont.render(str(elapTime), 1, (255, 255, 255))
		gameDisplay.blit(elapTimeRender, (display_width/2, 50))
		
		pygame.display.update()
		clock.tick(60)
	
def menu():
	global crashed
	global pins
	global crash
	global robot1X
	global robot1Y
	global robot2X
	global robot2Y
	global score1
	global score2
	
	menuFont = pygame.font.SysFont('Comic Sans MS', 30)
	
	black = [0,0,0]
	white = [255,255,255]
	crash = False
	
	#setup for special code
	list = []
	target = [1, 1, 2, 2, 3, 4, 3, 4, 5, 6, 7]
	
	#Player Ready
	player1ReadyState = False
	player2ReadyState = False
	
	#Blinking stuff
	tick = 0 
	tickTime = 10
	
	while not crash:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				crash = True
		
		if(GPIO.input(4) != 1 or GPIO.input(19) != 1): #Up
			while(GPIO.input(4) != 1 or GPIO.input(19) != 1):
				time.sleep(.1)
			list.append(1)
		
		if(GPIO.input(17) != 1 or GPIO.input(18) != 1): #Down
			while(GPIO.input(17) != 1 or GPIO.input(18) != 1):
				time.sleep(.1)
			list.append(2)
			
		if(GPIO.input(27) != 1 or GPIO.input(23) != 1): #Left
			while(GPIO.input(27) != 1 or GPIO.input(23) != 1):
				time.sleep(.1)
			list.append(3)

		if(GPIO.input(22) != 1 or GPIO.input(24) != 1): #Right
			while(GPIO.input(22) != 1 or GPIO.input(24) != 1):
				time.sleep(.1)
			list.append(4)
			
		if(GPIO.input(6) != 1 or GPIO.input(12) != 1):
			while(GPIO.input(6) != 1 or GPIO.input(12) != 1):
				time.sleep(.1)
			list.append(5)
		
		if(GPIO.input(5) != 1 or GPIO.input(20) != 1):
			while(GPIO.input(5) != 1 or GPIO.input(20) != 1):
				time.sleep(.1)
			list.append(6)
			
		if(GPIO.input(13) != 1 or GPIO.input(25) != 1):
			while(GPIO.input(13) != 1 or GPIO.input(25) != 1):
				time.sleep(.1)
			list.append(7)
		
		while(len(list) > 11):
			list.pop(0)
		
		print(list)
		
		if(list == target):
			break
		
		time.sleep(.1)
			
		
		gameDisplay.fill(black)
		
		play = scoreFont.render(str("BOTH PLAYERS PRESS START KEY TO PLAY..."), 1, (255, 255, 255))
		player1Score = scoreFont.render(str(score1), 1, (255, 255, 255))
		player2Score = scoreFont.render(str(score2), 1, (255, 255, 255))
		player1Ready = scoreFont.render(str("Ready Player 1"), 1, (255, 255, 255))
		player2Ready = scoreFont.render(str("Ready Player 2"), 1, (255, 255, 255))
	
		
		playXCenter = play.get_width()/2
		player1XCenter = player1Score.get_width()/2
		player2XCenter = player2Score.get_width()/2
		player1ReadyCenter = player1Ready.get_width()/2
		player2ReadyCenter = player2Ready.get_width()/2
		
		gameDisplay.blit(player1Score, (display_width/3 - player1XCenter, display_height/2))
		gameDisplay.blit(player2Score, (display_width/3*2 - player2XCenter, display_height/2))
		
		#Draw player 1
		
		player1Tex = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/robo_1.png')
		gameDisplay.blit(player1Tex, (display_width/3 - player1XCenter - 45, display_height/2 + 100))
		
		#Draw player 2
		
		player2Tex = pygame.image.load('/home/pi/FRC-Arcade-Game/spr_FRC_game/robo_2.png')
		gameDisplay.blit(player2Tex, (display_width/3*2 - player2XCenter - 45, display_height/2 + 100))
		
		#Blink the Player start text
		tick += 1
		if(tick < tickTime/1.4):
			gameDisplay.blit(play, (display_width/2 - playXCenter, display_height/4))
		if(tick >= tickTime):
			tick = 0
		
		if(GPIO.input(13) != 1):
			player1ReadyState = True
		
		if(GPIO.input(25) != 1):
			player2ReadyState = True
		
		if(player1ReadyState == True):
			gameDisplay.blit(player1Ready, (display_width/3 - player1ReadyCenter, (display_height/4)*3))
			
		if(player2ReadyState == True):
			gameDisplay.blit(player2Ready, ((display_width/3)*2 - player2ReadyCenter, (display_height/4)*3))
			print("test")
		
		pygame.display.update()
		
		if(player1ReadyState == True and player2ReadyState == True):
			time.sleep(3)
			initReset()
			crashed = False
			player1ReadyState = False
			player2ReadyState = False
			game()
			time.sleep(1)
		clock.tick(60)
		
while 1 == 1:
	showSecret()
	menu()

