import pygame
import random
import keyboard
import sys

# dimensions = [1920, 1020] # Full Screen Windowed
# dimensions = [1920, 1080] # Full Screen
dimensions = [960, 510]
# randNos = []
# colorNos = []

nosDict = {'randNos': [], 
           'colorNos': []}

numRange = dimensions[0] // 21
maxNum = dimensions[1] // 5
swapStat = False
elemType = 'c'
running = True
keyChk = False

clock = pygame.time.Clock()