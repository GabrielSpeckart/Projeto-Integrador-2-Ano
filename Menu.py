import pygame, sys
 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu Principal')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 24)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Nome do Jogo', font, (255, 255, 255), screen, 190, 50)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(150, 150, 200, 50)
        button_2 = pygame.Rect(150, 250, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (96, 96, 96), button_1)
        pygame.draw.rect(screen, (96, 96, 96), button_2)
        screen.blit(font.render('Jogar', True, (255, 255, 255)), (228, 168))
        screen.blit(font.render('Opções', True, (255, 255, 255)), (222, 268))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        pygame.display.set_caption('Nome do Jogo')
        
        draw_text('Jogo', font, (255, 255, 255), screen, 225, 225)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.display.set_caption('Menu Principal')
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        pygame.display.set_caption('Opções')
 
        draw_text('Opções', font, (255, 255, 255), screen, 225, 225)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.display.set_caption('Menu Principal')
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()