import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    def launch(self):
        while True:
         self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0