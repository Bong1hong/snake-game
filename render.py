    # -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:16:49 2018

@author: Bong Jin Hong
"""

import pygame
import gameobject

# Snake head img
snakeImg = pygame.image.load("snake head.png")
snakeImg = pygame.transform.scale(snakeImg, (20, 20))

orig = snakeImg    
left = pygame.transform.rotate(snakeImg, 90)
right = pygame.transform.rotate(snakeImg, -90)
down = pygame.transform.rotate(snakeImg, 180)

# Fruit Image
fruitImg = pygame.image.load("apple.png")
fruitImg = pygame.transform.scale(fruitImg, (20, 20))

# Bomb Image
bombImg = pygame.image.load("bomb.png")
bombImg = pygame.transform.scale(bombImg, (20, 20))

class Render(object):
    def render_game(self, window, g):
       self.render_snake(window, g.snake)
       self.render_lof(window, g.lof)
       self.render_lob(window, g.lob)

    def render_snake(self, window, snake):
        if snake.facing == gameobject.Direction.t:
            snake_head_img = orig
        elif snake.facing == gameobject.Direction.l:
            snake_head_img = left
        elif snake.facing == gameobject.Direction.r:
            snake_head_img = right
        elif snake.facing == gameobject.Direction.d:
            snake_head_img = down
        elif snake.facing == gameobject.Direction.s:
            snake_head_img = down
        
        snake_rect = snake_head_img.get_rect()
        snake_rect.center = (snake.snake_body[0].location.x, snake.snake_body[0].location.y)
        window.blit(snake_head_img, snake_rect)
            
        for i in range(1, len(snake.snake_body)):   
            snake_body = pygame.Rect(snake.snake_body[i].location.x, snake.snake_body[i].location.y, snake.snake_body[i].size, snake.snake_body[i].size)
            snake_body.center = (snake.snake_body[i].location.x, snake.snake_body[i].location.y)
            pygame.draw.rect(window, (25, 229, 25), snake_body)
                
    
    def render_lof(self, window, lof):
       for fruit in lof.fruits:
           #fruit_image = pygame.Rect(fruit.location.x, fruit.location.y, 10, 10)
           fruit_rect = fruitImg.get_rect()
           fruit_rect.center = (fruit.location.x, fruit.location.y)
           #pygame.draw.rect(window, (0, 255, 0), fruit_image)
           window.blit(fruitImg, fruit_rect)
    
    def render_lob(self, window, lob):   
       for bomb in lob.bombs:
           #bomb_image = pygame.Rect(bomb.location.x, bomb.location.y, 10, 10)
           bomb_rect = bombImg.get_rect()
           bomb_rect.center = (bomb.location.x, bomb.location.y)
           #pygame.draw.rect(window, (0, 0, 255), bomb_image)
           window.blit(bombImg, bomb_rect)