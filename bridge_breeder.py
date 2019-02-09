import pygame

from bridge import Bridge
import db

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_NAME = "Bridge Breeder"
DB_PATH = "/home/alex/Programs/Python/Bridge-Breeder/bridges.db"

def main():
	pygame.init()
	screen_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption(GAME_NAME)

	done = False
	clock = pygame.time.Clock()

	#TEST
	db.create_connection(DB_PATH)
	c = db.connect(DB_PATH)
	b = Bridge("b1", 1, 1, 1, 1, 1, 1, 1, 1)
	db.add_bridge(c, b)
	#/TEST
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		screen.fill((0, 0, 0))

		clock.tick(60)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
