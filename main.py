# -*- coding: utf-8 -*-
"""
@author: Bong Jin Hong
@created date: 29 Jun 2018
@updated date: 4 July 2018
"""

import game
import gameobject
import hitbox
import render
import random

import time
import pygame

# Constants
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500
SCORE_DISPLAY_LOCATION = [400, 20]
LIFE_DISPLAY_LOCATION = [30, 20]
FONT_SIZE = 25
FRUIT_POINTS = [1, 2, 3, 4, 5]
HIT_BOX_RANGE = 20
BACKGROUND_COLOR = (255, 255, 255) # White

# Initialize the game window
pygame.init()

# Set Window size
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Window title
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, FONT_SIZE)

def message_to_screen(msg, location, color, center):
    if center == True:
        screen_text = font.render(msg, True, color)
        screen_text_rect = screen_text.get_rect(center=(SCREEN_WIDTH/2, location[1]))
        window.blit(screen_text, screen_text_rect)
    elif center == False:
        screen_text = font.render(msg, True, color)
        window.blit(screen_text, location)

def exitGame():
    window.fill(BACKGROUND_COLOR)
    message_to_screen("Game Over", [SCREEN_WIDTH/2, SCREEN_HEIGHT/2], (0, 0, 0), True)
    pygame.display.update()
    
    time.sleep(2)
    pygame.quit()
    quit()

def pause():
    paused = True
    while paused:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    return True
                elif event.key == pygame.K_q:
                    paused = False
                    return False
            
        window.fill(BACKGROUND_COLOR)
        message_to_screen("Paused", [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT/2) - FONT_SIZE],(0, 0, 0), True)
        message_to_screen("Press C to continue or Q to quit.", [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT/2)], (0, 0, 0), True)
        
        pygame.display.update()
        clock.tick(5)
            
    
def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return True
                if event.key == pygame.K_q:
                    return False
            if event.type == pygame.QUIT:
                return False
                    
        window.fill(BACKGROUND_COLOR)
        message_to_screen("Snake Game", [200, 150], (0, 0, 0), True)
        message_to_screen("Press S to start the Game, press Q to quit the Game", [50, 210], (0, 0, 0), True)
            
        pygame.display.update()
        clock.tick(5)

# Create all the game object
snake = gameobject.Snake(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
lof = gameobject.ListOfFruit()
lob = gameobject.ListOfBomb()
h_box = hitbox.hitbox()
g = game.Game(snake, lof, lob)
render_g = render.Render()

gameLoop = start()

while gameLoop:
    window.fill(BACKGROUND_COLOR)
    render_g.render_game(window, g)
    
    if snake.snake_body[0].location.x < 0 or snake.snake_body[0].location.y < 0 or snake.snake_body[0].location.x > SCREEN_WIDTH or snake.snake_body[0].location.y > SCREEN_HEIGHT:
        gameLoop = start()
        if gameLoop == True:
            snake = gameobject.Snake(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            lof = gameobject.ListOfFruit()
            lob = gameobject.ListOfBomb()
            h_box = hitbox.hitbox()
            g = game.Game(snake, lof, lob)
            render_g = render.Render()
    
    if snake.dead() == True:
        gameLoop = start()
        if gameLoop == True:
            snake = gameobject.Snake(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            lof = gameobject.ListOfFruit()
            lob = gameobject.ListOfBomb()
            h_box = hitbox.hitbox()
            g = game.Game(snake, lof, lob)
    
    for body in range(1, len(snake.snake_body)):
        if h_box.hitbox_object_object(snake.snake_body[body].location.x, snake.snake_body[0].location.x, HIT_BOX_RANGE-2) and h_box.hitbox_object_object(snake.snake_body[body].location.y, snake.snake_body[0].location.y, HIT_BOX_RANGE-2):
            gameLoop = start()
    
    for fruit in lof.fruits:
        if h_box.hitbox_object_object(fruit.location.x, snake.snake_body[0].location.x, HIT_BOX_RANGE) and h_box.hitbox_object_object(fruit.location.y, snake.snake_body[0].location.y, HIT_BOX_RANGE):
            snake.eat(fruit)
            fruit.getate = True
        
    for bomb in lob.bombs:
        if h_box.hitbox_object_object(bomb.location.x, snake.snake_body[0].location.x, HIT_BOX_RANGE) and h_box.hitbox_object_object(bomb.location.y, snake.snake_body[0].location.y, HIT_BOX_RANGE):
            snake.eat(bomb)                    
            bomb.getactivated = True
    
    if len(lof.fruits) == 0:
      lof.fruits.append(gameobject.Fruit(FRUIT_POINTS[random.randint(0, 4)], gameobject.Location(random.uniform(20, SCREEN_WIDTH-20), random.uniform(50, SCREEN_HEIGHT-20))))
      
    if len(lob.bombs) == 0:
      lob.bombs.append(gameobject.Bomb(gameobject.Location(random.randrange(20, SCREEN_WIDTH-20), random.randrange(50, SCREEN_HEIGHT-20))))

    # Move the snake and its body location
    snake.move()
        
    # Remove the fruit or bomb that get ate by the snake
    lof.filterfruit()
    lob.filterbomb()
    
    # Keep refresh the game since some event might occur
    g = game.Game(snake, lof, lob)
    
    message_to_screen("Score: " + str(snake.points), SCORE_DISPLAY_LOCATION,(0, 0, 0), False)
    message_to_screen("Life: " + str(snake.life), LIFE_DISPLAY_LOCATION,(0, 0, 0), False)
    
    pygame.display.update()
    clock.tick(10)
    
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            gameLoop = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == 273 and snake.facing != gameobject.Direction.d: # Up arrow
                snake.facing = gameobject.Direction.t
            elif event.key == 274 and snake.facing != gameobject.Direction.t: # Down arrow
                snake.facing = gameobject.Direction.d
            elif event.key == 275 and snake.facing != gameobject.Direction.l: # Right arrow
                snake.facing = gameobject.Direction.r
            elif event.key == 276 and snake.facing != gameobject.Direction.r: # Left arrow
                snake.facing = gameobject.Direction.l
            elif event.key == pygame.K_p:
                gameLoop = pause()

        if event.type == pygame.ACTIVEEVENT:
            if event.state == 2 and event.gain == 0:
                gameLoop = pause() 

exitGame()

