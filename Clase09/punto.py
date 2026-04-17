#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:52:47 2021

@author: salo
"""
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
class Rectangulo():
    def __init__(self, punto1, punto2):
        self.punto1 = Punto(x, y)
        self.punto2 = Punto(x, y)
        
    def base(self):
        return 
    
