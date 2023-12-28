import pygame
import sys
import test2 as rps

pygame.init()

width = 900
height = 700

screen = pygame.display.set_mode((width, height))
multi_view = rps.MultiPlayerView(screen)

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    multi_view.create_widgets()
    multi_view.update(events)

    pygame.display.update()
    pygame.display.flip()
