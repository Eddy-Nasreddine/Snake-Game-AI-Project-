import pygame
import random
import time
import math
def main():
	background_colour = (255, 0, 0)
	screen = pygame.display.set_mode((995, 995))
	pygame.display.set_caption('Snake!')
	pygame.display.flip()
	background_image = pygame.image.load('995 grid.png').convert()
	x_pos = 500
	y_pos = 500

	snakey = Snake(screen, x_pos, y_pos)
	snakey.spawn_food()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.blit(background_image,(0,0))
		#snakey.Food(x,y)


		userinput = get_userinput()
		if userinput != 'none':
			snakey.change_direction(userinput)
		snakey.move_snake()
		snakey.draw_snake()
		snakey.food_collision()

		


		pygame.time.Clock().tick(60)
		pygame.display.flip()
		pass


class Snake:
	def __init__(self, screen, x, y):
		self.screen = screen
		self.thickness = 50
		self.food = pygame.Rect(0, 0, self.thickness, self.thickness)
		self.boarder_thickness = 5
		self.distance_between_squares = self.thickness + self.boarder_thickness
		self.snake_head = pygame.Rect(x, y, self.thickness, self.thickness)
		self.moving_direction = 'none'
		self.buffered_direction = 'none'
		self.x_velocity = 0
		self.y_velocity = 0
		self.speed = 10
		self.turning_forgivingness = 0
		self.snake_body = [self.snake_head]
		self.buffer = 55

	def draw_snake(self):
		pygame.draw.rect(self.screen, (255, 255, 255), self.snake_head)
		pygame.draw.rect(self.screen, (255, 0, 0), self.food)

		for i in range(len(self.snake_body)-1, 0, -1):
			if (abs(self.snake_body[i].x - self.snake_body[i - 1].x) >= 50 or abs(self.snake_body[i].y - self.snake_body[i - 1].y) >= 50):
				self.snake_body[i].x = self.snake_body[i - 1].x
				self.snake_body[i].y = self.snake_body[i - 1].y
				print("head: ",self.snake_body[i].x, ":", self.snake_body[i].y)
				print("tail: ", self.snake_body[i - 1].x, ":", self.snake_body[i - 1].y)

		for bodys in self.snake_body:
			pygame.draw.rect(self.screen, (255, 255, 255), bodys)

	def increase(self):
		self.snake_body.append(pygame.Rect(self.snake_head.x, self.snake_head.y, self.thickness, self.thickness))

	def food_collision(self):
		if (self.food.colliderect(self.snake_head)):
			self.increase()
			self.spawn_food()


	def spawn_food(self):
		x_pos = random.randrange(5, 995, 55)
		y_pos = random.randrange(5, 995, 55)
		self.food.x = x_pos
		self.food.y = y_pos
		if (self.food.colliderect(self.snake_head)):
			self.spawn_food()


	def move_snake(self):
		if self.buffered_direction != self.moving_direction:
			if self.buffered_direction == 'up':
				distance_to_turn = (round((self.snake_head.x - self.boarder_thickness) / self.distance_between_squares) * self.distance_between_squares) - (self.snake_head.x - self.boarder_thickness)
				if distance_to_turn <= self.turning_forgivingness:
					self.snake_head.x += distance_to_turn
					self.moving_direction = 'up'
					self.y_velocity = -self.speed
					self.x_velocity = 0
			elif self.buffered_direction == 'down':
				distance_to_turn = (round((self.snake_head.x - self.boarder_thickness) / self.distance_between_squares) * self.distance_between_squares) - (self.snake_head.x - self.boarder_thickness)
				if distance_to_turn <= self.turning_forgivingness:
					self.snake_head.x += distance_to_turn
					self.moving_direction = 'down'
					self.y_velocity = self.speed
					self.x_velocity = 0
			elif self.buffered_direction == 'left':
				distance_to_turn = (round((self.snake_head.y - self.boarder_thickness) / self.distance_between_squares) * self.distance_between_squares) - (self.snake_head.y - self.boarder_thickness)
				if distance_to_turn <= self.turning_forgivingness:
					self.snake_head.y += distance_to_turn
					self.moving_direction = 'left'
					self.x_velocity = -self.speed
					self.y_velocity = 0
			elif self.buffered_direction == 'right':
				distance_to_turn = (round((self.snake_head.y - self.boarder_thickness) / self.distance_between_squares) * self.distance_between_squares) - (self.snake_head.y - self.boarder_thickness)
				if distance_to_turn <= self.turning_forgivingness:
					self.snake_head.y += distance_to_turn
					self.moving_direction = 'right'
					self.x_velocity = self.speed
					self.y_velocity = 0

		self.snake_head.x += self.x_velocity
		self.snake_head.y += self.y_velocity
		# else:
		# 	if self.moving_direction == 'up':
		# 		y_velocity = -55
		# 		x_velocity = 0
		# 	elif self.moving_direction == 'down':
		# 		y_velocity = 55
		# 		x_velocity = 0
		# 	elif self.moving_direction == 'left':
		# 		x_velocity = -55
		# 		y_velocity = 0
		# 	elif self.moving_direction == 'right':
		# 		x_velocity = 55
		# 		y_velocity = 0
	

	def change_direction(self, direction):
		self.buffered_direction = direction



def get_userinput():
	userinput = pygame.key.get_pressed()
		
	if userinput[pygame.K_w]:
		return 'up'
	elif userinput[pygame.K_s]:
		return 'down'
	elif userinput[pygame.K_a]:
		return 'left'
	elif userinput[pygame.K_d]:
		return 'right'
	return 'none'




main()

