import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_NAME = "Bridge Breeder"

def main():
	pygame.init()
	screen_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption(GAME_NAME)

	done = False
	clock = pygame.time.Clock()
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
