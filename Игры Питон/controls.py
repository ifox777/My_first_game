import pygame
import sys
from bullet import Bullet

def events(screen, gun2, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun2.mright = True
            #влево
            elif event.key == pygame.K_a:
                gun2.mleft = True
            elif event.key == pygame.K_w:
                new_bullet = Bullet(screen, gun2)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun2.mright = False
            #влево
            elif event.key == pygame.K_a:
                gun2.mleft = False

def update(bg_color, screen, gun2, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun2.output()
    pygame.display.flip()

def update_bullets(bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)




