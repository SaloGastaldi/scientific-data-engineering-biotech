#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:23:11 2021

@author: salo
"""
rng = np.random.RandomState(42)
steps = 1024
runs = 32
numbers = rng.randint(-9, 10, (runs, steps))
sums = numbers.cumsum(axis=1)
plt.figure(figsize=(14, 6))
plt.plot(sums.T);