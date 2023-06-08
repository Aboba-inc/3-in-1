import pygame
import sys
from pacman import pacman
from pong import pong
from tic_tac_toe import tic_tac_toe
from main_menu import main_menu


def main():
    pygame.mixer.init()

    pygame.display.set_caption("3 IN 1")
    icon = pygame.image.load('assets/icons/menu.png')
    pygame.display.set_icon(icon)

    menu_sound = pygame.mixer.Sound(f'assets/music/Mega Man X3 - Ending.mp3')
    pacman_sound = pygame.mixer.Sound(
        f'assets/music/Pac-man theme remix - By Arsenic1987.mp3')

    while True:
        menu_sound.play(loops=1)
        game = main_menu()

        if game == 0:
            pygame.quit()
            sys.exit()
        elif game == 1:
            menu_sound.stop()
            pong()
        elif game == 2:
            menu_sound.stop()
            tic_tac_toe()
        elif game == 3:
            menu_sound.stop()
            pacman_sound.play(loops=1)
            pacman()
            pacman_sound.stop()


if __name__ == "__main__":
    main()
