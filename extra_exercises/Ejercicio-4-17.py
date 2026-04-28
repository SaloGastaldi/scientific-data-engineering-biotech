#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:19:01 2021

@author: salo
"""
#Ejercicio 4.17: Fijando ideas
import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
#print(headers)
#print(row)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func,val in zip(types,row)]
record = dict(zip(headers, converted))
print(record)
print(record['name'])
print(record['price'])
print(record['date'])

