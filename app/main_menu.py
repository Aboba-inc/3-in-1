import pygame
import sys
import os
from button import Button

os.environ['SDL_VIDEO_CENTERED'] = '0'
pygame.init()

BG = pygame.image.load("assets/backgrounds/3.png")
SCREEN = pygame.display.set_mode((900, 680))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size)


def play():
    while True:
        SCREEN.blit(BG, (0, 0))
        pygame.display.set_caption("Play Menu")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(65).render("PLAY MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 160))

        PONG_BUTTON = Button(image=None, pos=(450, 250),
                             text_input="Pong", font=get_font(60), base_color="#8ecae6", hovering_color="#bde2ff")
        TIC_TAC_TOE_BUTTON = Button(image=None, pos=(450, 350),
                                    text_input="Tic Tac Toe", font=get_font(60), base_color="#8ecae6", hovering_color="#bde2ff")
        PACMAN_BUTTON = Button(image=None, pos=(450, 450),
                               text_input="Pacman", font=get_font(60), base_color="#8ecae6", hovering_color="#bde2ff")
        BACK_BUTTON = Button(image=None, pos=(450, 550),
                             text_input="Back", font=get_font(60), base_color="#2A9D8F", hovering_color="#55c7b7")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PONG_BUTTON, TIC_TAC_TOE_BUTTON, PACMAN_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PONG_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 1
                if TIC_TAC_TOE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 2
                if PACMAN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 3
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 4

        pygame.display.update()


def main_menu():
    SCREEN = pygame.display.set_mode((900, 680))

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(65).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 160))

        PLAY_BUTTON = Button(image=None, pos=(450, 300),
                             text_input="Play", font=get_font(60), base_color="#8ecae6", hovering_color="#bde2ff")
        QUIT_BUTTON = Button(image=None, pos=(450, 450),
                             text_input="Quit", font=get_font(60), base_color="#8ecae6", hovering_color="#bde2ff")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    res = play()
                    if res != 4:
                        return res
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()