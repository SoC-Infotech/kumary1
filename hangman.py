#Import 2 libraries to our game 
import pygame
import random

#Initialize the pygame (game loop, game scene)
pygame.init()

#Declare some variables/constants
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Yash")

#Main program
# create a game loop to keep the window visible
inplay = True
while inplay:
    win.fill(GREEN) #Make backgroud color GREEN
    pygame.display.update()
    pygame.time.delay(100)



#Quit the pygame
pygame.quit()
