import pygame
import random
import colorsys
from collections import namedtuple


coordinate = namedtuple("point", "x, y")

def main():
	pygame.init()
	screen = pygame.display.set_mode((995, 995))
	pygame.display.set_caption('Snake!')
	pygame.display.flip()
	background_image = pygame.image.load('995 grid.png').convert()
	snake_death_sound = pygame.mixer.Sound("snakedie.mp3")
	snake_death_sound.set_volume(0.1)

	snakey = Snake(screen, 500, 500)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					snakey.change_direction('up')
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
					snakey.change_direction('down')
				elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
					snakey.change_direction('left')
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					snakey.change_direction('right')

		screen.blit(background_image, (0, 0))
		snakey.update_body()
		snakey.move_snake()
		snakey.draw_snake()
		snakey.face()
		dead_snake = snakey.endgame()
		if dead_snake is True:
			snake_death_sound.play()
			snakey = Snake(screen, 500, 500)
		snakey.food_collision()
		pygame.time.Clock().tick(10)
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
		self.speed = 55
		self.turning_forgivingness = 0
		self.snake_body = [self.snake_head]
		self.buffer = 55
		self.coordinates = []
		self.spawn_food()
		self.apple_sprite = pygame.image.load("apple.png").convert_alpha()

	def face(self):
		pygame.draw.circle(self.screen, (0, 0, 0), [self.snake_head.x + 11, self.snake_head.y + 11], 7)
		pygame.draw.circle(self.screen, (0, 0, 0), [self.snake_head.x + 39, self.snake_head.y + 11], 7)

	def draw_snake(self):
		pygame.draw.rect(self.screen, (255, 255, 255), self.snake_head)
		self.screen.blit(self.apple_sprite, self.food)
		x = 0
		for bodys in self.snake_body:
			x += 0.01
			if x > 1:
				x = 0
			hls_color = colorsys.hls_to_rgb(x, 0.45, 1)
			rgb = (hls_color[0]*255, hls_color[1]*255, hls_color[2]*255)
			pygame.draw.rect(self.screen, rgb, bodys)

	def update_body(self):
		for i in range(len(self.snake_body)-1, 0, -1):
			self.snake_body[i].y = self.snake_body[i - 1].y
			self.snake_body[i].x = self.snake_body[i - 1].x

	def increase(self):
		self.snake_body.append(pygame.Rect(self.snake_head.x, self.snake_head.y, self.thickness, self.thickness))

	def food_collision(self):
		if self.food.colliderect(self.snake_head):
			self.increase()
			self.spawn_food()

	def endgame(self):
		for j in range(1, len(self.snake_body)):
			if self.snake_body[j].colliderect(self.snake_head):
				return True
		if self.snake_head.x < 5 or self.snake_head.x > 990:
			return True
		if self.snake_head.y < 5 or self.snake_head.y > 990:
			return True

	def spawn_food(self):
		self.food = pygame.Rect(0, 0, self.thickness, self.thickness)
		self.food.x = random.randrange(5, 995, 55)
		self.food.y = random.randrange(5, 995, 55)
		if self.food.colliderect(self.snake_head):
			self.spawn_food()
		for bodys in self.snake_body:
			if self.food.colliderect(bodys):
				self.spawn_food()

	def move_snake(self):
		if self.buffered_direction != self.moving_direction:
			if self.buffered_direction == 'up':
				self.moving_direction = 'up'
				self.y_velocity = -self.speed
				self.x_velocity = 0
			elif self.buffered_direction == 'down':
				self.moving_direction = 'down'
				self.y_velocity = self.speed
				self.x_velocity = 0
			elif self.buffered_direction == 'left':
				self.moving_direction = 'left'
				self.x_velocity = -self.speed
				self.y_velocity = 0
			elif self.buffered_direction == 'right':
				self.moving_direction = 'right'
				self.x_velocity = self.speed
				self.y_velocity = 0

		self.snake_head.x += self.x_velocity
		self.snake_head.y += self.y_velocity

	def change_direction(self, direction):
		if len(self.snake_body) > 1:
			if self.moving_direction == "up" and direction == "down":
				return
			elif self.moving_direction == "down" and direction == "up":
				return
			elif self.moving_direction == "left" and direction == "right":
				return
			elif self.moving_direction == "right" and direction == "left":
				return
		self.buffered_direction = direction


main()
