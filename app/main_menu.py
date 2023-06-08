import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((900, 680))
pygame.display.set_caption("3 IN 1")

BG = pygame.image.load("assets/backgrounds/3.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        MENU_TEXT = get_font(65).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 160))

        PONG_BUTTON = Button(image=None, pos=(450, 300), 
                            text_input="Play", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        TIC_TAC_TOE_BUTTON = Button(image=None, pos=(450, 450), 
                            text_input="Quit", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        PACMAN_BUTTON = Button(image=None, pos=(450, 450), 
                            text_input="Quit", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=None, pos=(450, 450), 
                            text_input="Quit", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        SCREEN = pygame.display.set_mode((900, 684))
        pygame.display.set_caption("Games Menu")

        BG = pygame.image.load("assets/backgrounds/3.png")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(65).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 160))

        PLAY_BUTTON = Button(image=None, pos=(450, 300), 
                            text_input="Play", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(450, 450), 
                            text_input="Quit", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

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
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()