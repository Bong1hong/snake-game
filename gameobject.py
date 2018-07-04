# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:18:26 2018

@author: Bong Jin Hong
"""

import enum

class GameObject(object):
    def __init__(self, pts, y, loc):
        self.interactable = y
        self.points = pts
        self.location = loc

class Location(object):
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        
    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False
    
class Direction(enum.Enum):
    l = "LEFT"
    r = "RIGHT"
    t = "TOP" 
    d = "DOWN"
    s = "STOP"
    

class Snake(GameObject):    
    def __init__(self, x, y):
        GameObject.__init__(self, 0, True, Location(x, y))
        self.speed = 20
        self.life = 3
        self.size = 20
        self.facing = Direction.s # default facing direction
        self.snake_body = []
        self.snake_body.append(snake_body_part(20, Location(x,y)))

    def move(self):
        self.change_body_location(len(self.snake_body) - 1)
    
        if self.facing == Direction.l:
            self.snake_body[0].location.x -= self.speed
        elif self.facing == Direction.r:
            self.snake_body[0].location.x += self.speed
        elif self.facing == Direction.t:
            self.snake_body[0].location.y -= self.speed
        elif self.facing == Direction.d:
            self.snake_body[0].location.y += self.speed
        elif self.facing == Direction.s:
            self.snake_body[0].location = self.snake_body[0].location

    def change_body_location(self, i):
        if i == 0:
            return True    
        else:
            self.snake_body[i].location = Location(self.snake_body[i-1].location.x, self.snake_body[i-1].location.y)
            self.change_body_location(i - 1)
            
    def dead(self):
        if self.life == 0:
            return True
        else:
            return False
    
    def eat(self, stuff):
        if type(stuff) is Fruit:
            self.points += stuff.points
            stuff.getate = True
            self.grow()
        else:
            self.life -= stuff.points
            stuff.getactivated = True
            
    def grow(self):
        self.snake_body.append(snake_body_part(20, Location(self.snake_body[-1].location.x, self.snake_body[-1].location.y)))
    
    
class snake_body_part(object):
    def __init__(self, sz, loc):
        self.size = sz
        self.location = loc
        
    
class ListOfFruit(object):
    def __init__(self):
        self.fruits = []
        
    # Add fruit object into the list
    def addfruit(self, fruit):
        self.fruits.append(fruit)
        
    # Remove fruit object from the list
    def removefruit(self, fruit):
        self.fruits.remove(fruit)
        
    # Remove fruit object from the list that get ate by the Snake object
    def filterfruit(self):
        for fruit in self.fruits:
            if fruit.getate == True:
                self.fruits.remove(fruit)
    
    
class ListOfBomb(object):
    def __init__(self):
        self.bombs = []
        
    # Add bomb object into the list
    def addbomb(self, bomb):
        self.bombs.append(bomb)
        
    # Add bomb object into the list
    def removebomb(self, bomb):
        self.bombs.remove(bomb)
        
    def filterbomb(self):
        for bomb in self.bombs:
            if bomb.getactivated == True:
                self.bombs.remove(bomb)


class Fruit(GameObject):    
    def __init__(self, pts, loc):
        GameObject.__init__(self, pts, True, loc)
        self.getate = False
    
    
class Bomb(GameObject):
    def __init__(self, loc):
        GameObject.__init__(self, 1, True, loc)
        self.getactivated = False
    