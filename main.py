import pygame
import  subprocess

pygame.init()

monitor = pygame.display.set_mode((480, 600))

photo = pygame.image.load('/Users/zeinaddinzurgambayev/Desktop/nFac/Era.png')
class Button:
    def __init__(self):
        self.rect_level1 = pygame.Rect(480 / 4 - 10 , 135, 268, 134)
        self.rect_level2 = pygame.Rect(480 / 4 - 10 , 240, 40, 40)
        self.image_level1 = pygame.image.load(r'/Users/zeinaddinzurgambayev/Desktop/nFac/Untitled (2).png')
        self.image_level2 = pygame.image.load(r'/Users/zeinaddinzurgambayev/Desktop/nFac/Untitled.png')


    def draw(self):
        self.level1 = monitor.blit(self.image_level1, self.rect_level1)
        self.level2 = monitor.blit(self.image_level2, self.rect_level2)

clock = pygame.time.Clock()

button = Button()
flRunning = True
while flRunning:
    monitor.blit(photo,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if button.level1.collidepoint(pygame.mouse.get_pos()): 
                with open('/Users/zeinaddinzurgambayev/Desktop/nFac/level1.py') as f:
                    code = compile(f.read(), '/Users/zeinaddinzurgambayev/Desktop/nFac/level1.py', 'exec')
                    exec(code)
            elif button.level2.collidepoint(pygame.mouse.get_pos()): 
                with open('/Users/zeinaddinzurgambayev/Desktop/nFac/level2.py') as f:
                    code = compile(f.read(), '/Users/zeinaddinzurgambayev/Desktop/nFac/level2.py', 'exec')
                    exec(code)
    
    button.draw()
    pygame.display.update()
    clock.tick(60)
