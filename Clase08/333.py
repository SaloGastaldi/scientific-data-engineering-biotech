#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 08:09:43 2021

@author: salo
"""

#%%
import sys
import os

def listar_imgs(directorio):
    print([file for file in os.listdir(directorio+'/un_directorio') if '.png' in file])


def main(argv):
    if len(argv)!=2:
        print(f'Uso adecuado: {sys.argv[0]}' ' directorio')
    else:
        listar_imgs(argv[1])
        
if __name__ == '__main__':
    main(sys.argv)


