import pygame
import sys
import random

BOARD_SIZE_Y = 30            # Size of the board, in block
BOARD_SIZE_X = 50
BLOCK_SIZE = 20             # Size of 1 block, in pixel
HEAD_COLOR = (0, 100, 0)    # Dark Green
BODY_COLOR = (0, 200, 0)    # Light Green
FOOD_COLOR = [(200, 0, 0),(200,100,0),(200,200,0)]
SPEED = 15

class Snake():
	def __init__(self):
		#self.position = [int(BOARD_SIZE_X/4), int(BOARD_SIZE_Y/4)]
		self.position = [2,2]
		self.body = [[self.position[0], self.position[1]],
                     [self.position[0]-1, self.position[1]],
                     [self.position[0]-2, self.position[1]]
                    ]
		self.direction = "RIGHT"

	def changeDirTo(self, dir):
		if dir == "RIGHT" and not self.direction == "LEFT":
			self.direction = "RIGHT"
		if dir == "LEFT" and not self.direction == "RIGHT":
			self.direction = "LEFT"
		if dir == "UP" and not self.direction == "DOWN":
			self.direction = "UP"
		if dir == "DOWN" and not self.direction == "UP":
			self.direction = "DOWN"
	
	def move(self, foodPos):
		if self.direction == "RIGHT":
			self.position[0] = (self.position[0]+ 1)%BOARD_SIZE_X
		if self.direction == "LEFT":
			self.position[0] = (self.position[0]- 1)%BOARD_SIZE_X
		if self.direction == "UP":
			self.position[1] = (self.position[1]- 1)%BOARD_SIZE_Y
		if self.direction == "DOWN":
			self.position[1] = (self.position[1] + 1)%BOARD_SIZE_Y

		self.body.insert(0, list(self.position))
		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def checkCollision(self):
		#if self.position[0] >= BOARD_SIZE_X or self.position[0] < 0:
		#	return 1
		#elif self.position[1] >= BOARD_SIZE_Y or self.position[1] < 0:
		#	return 1
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		for block in barrier.elements:
			if self.position[0]==block[0] and self.position[1]==block[1]:
				return 1
		return 0

	def getHeadPos(self):
		return self.position

	def getBody(self):
		return self.body
class Barrier():
	def __init__(self):
		self.elements = []
		if paternNumber == 1 or paternNumber==3:
			for i in range(0,BOARD_SIZE_Y):
				if not ( (BOARD_SIZE_Y/2-4)< i <(BOARD_SIZE_Y/2+4)):
					self.elements.insert(0,(BOARD_SIZE_X/2,i))

			for i in range(0,BOARD_SIZE_X):
				if not ( (BOARD_SIZE_X/2-4) < i < (BOARD_SIZE_X/2+4)):
					self.elements.insert(0,(i,BOARD_SIZE_Y/2))
		if paternNumber==2 or paternNumber==3:
			for i in range(0,BOARD_SIZE_Y):
				self.elements.insert(0,(BOARD_SIZE_X-1,i))
				self.elements.insert(0,(0,i))
			for i in range(0,BOARD_SIZE_X):
				self.elements.insert(0,(i,BOARD_SIZE_Y-1))
				self.elements.insert(0,(i,0))
		if paternNumber==4:
			for i in range(0,BOARD_SIZE_Y):
				self.elements.insert(0,(BOARD_SIZE_X/2,i))

			for i in range(0,BOARD_SIZE_X):
				self.elements.insert(0,(i,BOARD_SIZE_Y/2))


class FoodSpawner():
	def __init__(self):
		###
		self.isFoodOnScreen = False
		self.spawnFood()
		"Doc"

	def spawnFood(self):
		if self.isFoodOnScreen == False:
			flag = 0
			while not flag:
				flag = 1
				self.position = [random.randrange(1, BOARD_SIZE_X), random.randrange(1, BOARD_SIZE_Y)]
				for pos in snake.getBody():
					if pos[0]==self.position[0] and pos[1]==self.position[1]:
						flag = 0
				for pos in barrier.elements:
					if pos[0]==self.position[0] and pos[1]==self.position[1]:
						flag = 0

			aux = random.randrange(0,110)%11
			if 0 <= aux <= 5:#1*6 
				self.type = 0
			elif 6 <= aux <= 8:#2*3 
				self.type = 1
			elif 9 <= aux <= 10: #3*2
				self.type = 2
			self.isFoodOnScreen = True
		return self.position

	def setFoodOnScreen(self, bool_value):
		self.isFoodOnScreen = bool_value


def gameOver():
	pygame.display.set_caption("SNAKE GAME  |  Score: " + str(score) + "  |  GAME OVER. Press any key to quit ...")
	while True:
		event = pygame.event.wait()
		if event.type == pygame.KEYDOWN:
			break
	pygame.quit()
	#sys.exit()

print("introduce level 1 to 10: ")
level = int(input())
SPEED = level*5
print("introduce pattern number 0 to 4:")
paternNumber = int(input())
window = pygame.display.set_mode((BOARD_SIZE_X*BLOCK_SIZE, BOARD_SIZE_Y*BLOCK_SIZE))
pygame.display.set_caption("Snake Game")

fps = pygame.time.Clock()

score = 0
snake = Snake()
barrier = Barrier()
foodSpawner = FoodSpawner()
foodPos = foodSpawner.spawnFood()
changeSpeed = False

pygame.time.wait(2000) #for not to start at the same moment that you run the snake.py

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				snake.changeDirTo("RIGHT")
			if event.key == pygame.K_UP:
				snake.changeDirTo("UP")
			if event.key == pygame.K_DOWN:
				snake.changeDirTo("DOWN")
			if event.key == pygame.K_LEFT:
				snake.changeDirTo("LEFT")
	foodPos = foodSpawner.spawnFood()
	if snake.move(foodPos) == 1:
		score =score + foodSpawner.type +1 
		foodSpawner.setFoodOnScreen(False)


	window.fill(pygame.Color(225, 225, 225))

	head = 1
	for block in barrier.elements:
		pygame.draw.rect(window, (0,0,0), pygame.Rect(block[0]*BLOCK_SIZE,block[1]*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))
	for pos in snake.getBody():
		if head == 1:
			pygame.draw.rect(window, HEAD_COLOR, pygame.Rect(pos[0]*BLOCK_SIZE, pos[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
			head = 0
		else:
			pygame.draw.rect(window, BODY_COLOR, pygame.Rect(pos[0]*BLOCK_SIZE, pos[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
	# Draw food
	pygame.draw.rect(window, FOOD_COLOR[foodSpawner.type], pygame.Rect(foodPos[0]*BLOCK_SIZE, foodPos[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
	
	if snake.checkCollision() == 1:
		pygame.time.wait(2000)		
		gameOver()
		print("Game Over:")
		print("Final Score:"+str(score))
		sys.exit()

	pygame.display.set_caption("Snake game | Score: "+ str(score))

	pygame.display.flip()

	fps.tick(SPEED)





















