from config import *
from home import *
import pygame
import time

done = False

def startLauncher():
  pygame.init()
  pygame.display.set_caption('StoneBoard Launcher')
  (width, height) = (600, 450)
  screen = pygame.display.set_mode((width, height))
  launcher_background_colour = (41,60,57)
  screen.fill(launcher_background_colour)
  print("Launched Launcher")
  done = False
  
  #Is experimental test
  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load('artAssets/stoneBoard_experimentalRelease.png').convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))

  #Bone Icon
  boneIcon = pygame.image.load('artAssets/bone.png').convert_alpha()
  boneIcon = pygame.transform.scale(boneIcon, (236, 236))
  screen.blit(boneIcon,(182,40))
  #StoneBoard Logo
  stoneBoard_logo = pygame.image.load('artAssets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (250, 250))
  screen.blit(stoneBoard_logo,(175,180))
  pygame.display.flip()
  time.sleep(3)
  boneIcon = pygame.transform.scale(boneIcon, (0, 0))
  pygame.quit()
