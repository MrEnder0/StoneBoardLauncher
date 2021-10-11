from config import *
from home import *
import pygame
import time

def startLauncher():
  pygame.init()
  pygame.display.set_caption('StoneBoard Launcher')
  (width, height) = (600, 450)
  screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
  launcher_background_colour = (250,250,250)
  screen.fill(launcher_background_colour)
  print("Launched Launcher")
  clock = pygame.time.Clock()
  run = True

  class Gif(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
      super().__init__()
      self.sprites = []
      self.sprites.append(pygame.image.load('artAssets/loading/loading1.png'))
      self.sprites.append(pygame.image.load('artAssets/loading/loading2.png'))
      self.sprites.append(pygame.image.load('artAssets/loading/loading3.png'))
      self.sprites.append(pygame.image.load('artAssets/loading/loading4.png'))
      self.sprites.append(pygame.image.load('artAssets/loading/loading5.png'))
      self.current_sprite = 0
      self.image = self.sprites[self.current_sprite]

      self.rect = self.image.get_rect()
      self.rect.topleft = [pos_x,pos_y]

    def draw(self):
      screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, scale):
      self.current_sprite += 0.006

      if self.current_sprite >= len(self.sprites):
        time.sleep(0.30)
        self.current_sprite = 0

      self.image = self.sprites[int(self.current_sprite)]
      width = self.image.get_width()
      height = self.image.get_height()
      self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))

  #Is experimental test
  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load('artAssets/stoneBoard_experimentalRelease.png').convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (80, 80))
    screen.blit(stoneBoard_experimentalRelease,(0,-25))

  #StoneBoard Logo Rectangle
  stoneBoard_logo_rectangle = pygame.image.load('artAssets/stoneBoard_logo_rectangle.png').convert_alpha()
  stoneBoard_logo_rectangle = pygame.transform.scale(stoneBoard_logo_rectangle, (300, 150))
  screen.blit(stoneBoard_logo_rectangle,(365,-105))

  #StoneBoard Logo
  stoneBoard_logo = pygame.image.load('artAssets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (216, 21))
  screen.blit(stoneBoard_logo,(378,5))

  time.sleep(0.30)

  loadingGif = Gif(256, 375)
  
  while run:
    current_time = pygame.time.get_ticks()
    screen.fill(launcher_background_colour)
    screen.blit(stoneBoard_logo_rectangle,(365, -105))
    screen.blit(stoneBoard_experimentalRelease,(0,-25))
    screen.blit(stoneBoard_logo,(378,5))
    loadingGif.draw()
    loadingGif.update(11)
    pygame.display.flip()

    if current_time > 8000:
      run = False

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
  time.sleep(0.5)
  pygame.quit()
