# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 13:52:20 2018

@author: Bong Jin Hong
"""

import unittest
import gameobject

class TestSnake(unittest.TestCase):
    def test_snake_init(self):
        snake1 = gameobject.Snake()
        self.assertEqual(snake1.speed, gameobject.Snake.SNAKE_SPEED)
        self.assertEqual(snake1.life, gameobject.Snake.SNAKE_LIFE)
        self.assertEqual(snake1.length, gameobject.Snake.SNAKE_START_LENGTH)
        self.assertEqual(snake1.facing, gameobject.Direction.l)
        self.assertEqual(snake1.location, gameobject.Location(gameobject.Snake.SNAKE_START_X_LOCATION, gameobject.Snake.SNAKE_START_Y_LOCATION))
        
    def test_snake_move(self):
        snake1 = gameobject.Snake()
        self.assertEqual(snake1.location.x, gameobject.Snake.SNAKE_START_X_LOCATION)
        snake1.move()
        self.assertEqual(snake1.location.x, gameobject.Snake.SNAKE_START_X_LOCATION - 1)
        
    def test_snake_dead(self):
        snake1 = gameobject.Snake()
        self.assertFalse(snake1.dead())
        
        snake1.life = 0
        self.assertTrue(snake1.dead())
        
    def test_snake_eat_grow(self):
        snake1 = gameobject.Snake()
        self.assertEqual(snake1.points, 0)
        self.assertEqual(snake1.length, gameobject.Snake.SNAKE_START_LENGTH)
        
        snake1.eat(gameobject.Fruit(gameobject.Location(1,1), 5))
        self.assertEqual(snake1.points, 5)
        self.assertEqual(snake1.length, gameobject.Snake.SNAKE_START_LENGTH + 1)


class TestFruit(unittest.TestCase):
    def test_fruit_init(self):
        fruit1 = gameobject.Fruit(gameobject.Location(1, 1), 2)
        self.assertEqual(fruit1.location, gameobject.Location(1, 1))
        self.assertEqual(fruit1.points, 2)
    
    def test_fruit_snake_eat(self):
        fruit1 = gameobject.Fruit(gameobject.Location(1, 1), 3)
        snake1 = gameobject.Snake()
        self.assertEqual(fruit1.getate, False)
        snake1.eat(fruit1)
        self.assertEqual(fruit1.getate, True)

        
class TestBomb(unittest.TestCase):
    def test_bomb_snake_init(self):
        bomb1 = gameobject.Bomb(gameobject.Location(2, 2))
        self.assertEqual(bomb1.location, gameobject.Location(2, 2))
        
    def test_bomb_snake_eat(self):
        bomb1 = gameobject.Bomb(gameobject.Location(2,2))
        snake1 = gameobject.Snake()
        self.assertEqual(bomb1.getactivated, False)
        snake1.eat(bomb1)
        self.assertEqual(bomb1.getactivated, True)
        

class TestListOfFruit(unittest.TestCase):
    def test_lof_init(self):
        lof1 = gameobject.ListOfFruit()
        self.assertEqual(len(lof1.fruits), 0)
        
    def test_lof_addfruit(self):
        lof1 = gameobject.ListOfFruit()
        self.assertEqual(len(lof1.fruits), 0)
        
        lof1.addfruit(gameobject.Fruit(gameobject.Location(1, 1), 5))
        self.assertEqual(len(lof1.fruits), 1)
    
    def test_lof_filterfruit(self):
        lof1 = gameobject.ListOfFruit()
        snake1 = gameobject.Snake()
        fruit1 = gameobject.Fruit(gameobject.Location(1, 1), 5)
        
        lof1.addfruit(fruit1)
        self.assertEqual(len(lof1.fruits), 1)
        
        snake1.eat(fruit1)
        self.assertEqual(len(lof1.fruits), 1)
        
        lof1.filterfruit()
        self.assertEqual(len(lof1.fruits), 0)
        

class TestListOfBomb(unittest.TestCase):
    def test_lob_init(self):
        lob1 = gameobject.ListOfBomb()
        self.assertEqual(len(lob1.bombs), 0)
        
    def test_lob_addbomb(self):
        lob1 = gameobject.ListOfBomb()
        self.assertEqual(len(lob1.bombs), 0)
        
        lob1.addbomb(gameobject.Bomb(gameobject.Location(1, 1)))
        self.assertEqual(len(lob1.bombs), 1)
        
    def test_lob_filterbomb(self):
        lob1 = gameobject.ListOfBomb()
        snake1 = gameobject.Snake()
        bomb1 = gameobject.Bomb(gameobject.Location(1, 1))
        
        lob1.addbomb(bomb1)
        self.assertEqual(len(lob1.bombs), 1)
        
        snake1.eat(bomb1)
        self.assertEqual(len(lob1.bombs), 1)
        
        lob1.filterbomb()
        self.assertEqual(len(lob1.bombs), 0)
        
    