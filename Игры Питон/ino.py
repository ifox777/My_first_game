import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного прищельца"""

    def __init__(self, screen):
        """" инициализирцем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x) #преобразуем во float, чтобы двигалось плавно
        self.y = float(self.rect.y)


    def draw(self):
        """"вывод прищельца на жкран"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """перемещает прищельцев"""
        self.y += 0.1
        self.rect.y = self.y

