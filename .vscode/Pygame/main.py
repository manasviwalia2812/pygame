import pygame
import os

#defining the window dimensions 
WIDTH,HEIGHT= 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("first game")          #sets name of the window

WHITE = (255,255,255)
BLACK = (0,0,0)

BORDER= pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

FPS = 60              #frames per second. we use it to define how many times we want to run the while loop (update the screen) so the speed of the game remains constant on different computers
VEL=5           #Velocity of the spaceships
SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 55,40

YELLOW_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90 )


RED_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

def draw_window(red, yellow):
  WIN.fill(WHITE)
  pygame.draw.rect(WIN, BLACK, BORDER)
  WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))        #func we use to display things on the screen
  WIN.blit(RED_SPACESHIP,(red.x,red.y))
  pygame.display.update() #updates the display after we filled the window with white color

def yellow_handle_movement(keys_pressed, yellow):
  if keys_pressed[pygame.K_a] and yellow.x-VEL>0: #left
    yellow.x -= VEL
  if keys_pressed[pygame.K_d] and yellow.x+VEL+ yellow.width<BORDER.x+15: #right
    yellow.x += VEL
  if keys_pressed[pygame.K_w] and yellow.y -VEL>0: #up
    yellow.y -= VEL
  if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT-15: #down
      yellow.y += VEL
      
def red_handle_movement(keys_pressed, red):
  if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x + BORDER.width: #left
    red.x -= VEL
  if keys_pressed[pygame.K_RIGHT] and red.x+VEL+ red.width<WIDTH: #right
    red.x += VEL
  if keys_pressed[pygame.K_UP] and  red.y -VEL>0: #up
    red.y -= VEL
  if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT-15: #down
      red.y += VEL

def main():
  red= pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)              #pygame rectangle (x,y)
  yellow= pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

  clock= pygame.time.Clock()
  run=True
  while run:
    clock.tick(FPS)   #sets the FPS to 60
    for event in pygame.event.get():          #checks for all the possible events that can happen
      if event.type == pygame.QUIT:           #if the user quits the window
        run= False              #while loop (game) will end

    keys_pressed=pygame.key.get_pressed()       #it tells us what keys are currently being pressed down each time the while loop runs. so we can check if the key we want to use to run the game is being pressed down or not
    yellow_handle_movement(keys_pressed, yellow)
    red_handle_movement(keys_pressed, red)

    draw_window(red, yellow) #draws the window
    
  
  pygame.quit()

if __name__=="__main__":
  main()