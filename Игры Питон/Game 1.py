import pygame
import controls
from gun2 import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gun2 = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun2, bullets)
        gun2.update_gun()
        controls.update(bg_color, screen, gun2, bullets)
        controls.update_bullets(bullets)



run()





