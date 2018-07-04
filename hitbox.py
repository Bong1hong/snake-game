# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:48:36 2018

@author: Bong Jin Hong
"""

class hitbox(object):
    def hitbox_object_object(self, obj1, obj2, hitbox):
        if (obj1 - obj2) >= 0:
            if (obj1 - obj2) <= hitbox:
                return True
        else:
            if -(obj1 - obj2) <= hitbox:
                return True                