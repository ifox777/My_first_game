import pygame
import controls
from gun2 import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gun2 = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)


    while True:
        controls.events(screen, gun2, bullets)
        if stats.run_game:
            gun2.update_gun()
            controls.update(bg_color, screen, stats, sc, gun2, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun2, inos, bullets)



run()




