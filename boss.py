import pygame.image

class Boss:
    def __init__(self, level):
        self.level = level
        self.health = level *100
        self.gold = level * 2

        self.font = pygame.font.SysFont('arial', 30)
        self.block_picture = self.font.render('World Мир', False, (0,0, 225))

        self.picture = pygame.image.load('img/boss.png')
        self.pos = (100, 100)

    def draw_block(self, screen):
        screen.blit(self.block_picture, self.pos)
