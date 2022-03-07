import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Gaem")
clock = pygame.time.Clock()

test_surface = pygame.Surface((300, 300))
test_surface.fill('Blue')
while True:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
       pygame.quit()
       exit()
  clock.tick(60)
  screen.blit(test_surface, (0,0))
  pygame.display.update()