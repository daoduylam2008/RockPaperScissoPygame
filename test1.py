import pygame
import sys

screen = pygame.display.set_mode((900, 700))


def ts(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            print(123)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ts(event)

    pygame.display.flip()
    pygame.display.update()
