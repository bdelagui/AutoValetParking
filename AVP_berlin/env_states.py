#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:53:47 2020

@author: berlindelaguila
"""
import numpy as np 
import time
 
# statusCar = 1: car sends message to supervisor asking for a parking spot
# statusCar = 2: car in process of going to destination
# statusCar = 3: car receives a message from supervisor
# statusCar = 4: waiting for response from supervisor 

#status_transitions = [(1,[4]),(2,[3]),(3,[2]),(4,[3,4])]
#---------------


#sup = 1: supervisor waits for message from car
#sup = 2: supervisor sends command to system to park in parking lot  
#sup = 3: supervisor tells car to leave the garage
#sup = 4: superevisor receives msg from car  



sup_transitions =[(1, [4]), (2, [1,4]), (3, [1,4]),(4,[2,3])]

#For peds: physical state 54= state1, 55=2, 39=3, 32=4, 56=5
# adjust list for ped to walk left as well 
list_peds = [(1,[1,2,5]),
              (2,[1,2,3]),
              (3,[2,3,4]),
              (4,[3.4,5]),
              (5,[4,5,1])]


list_peds_dict = dict(list_peds)
#print(list_peds_dict[3])


#supervisor cases
sys_vars = {}
sys_vars['carA'] = (1, 53)
sys_vars['carB'] = (1, 53)
sys_init = {'carA = 1', 'carB = 15'}

#sup functions: Tell car to where to park, exit parking lot, receive commands from auton car
# As a start, tell auton car to park in space 48, wait a little, then exit parking lot 
# How can I receive info from auton vehicle? 

list_sup = [(carA = 1, [1,2]),
            (carA = 2, [2,2]),
            (carA = 3, [3,4,9]),
            (carA = 4, [4,5,10]),
            (carA = 5, [5,6,11]),
            (carA = 6, [6,7,12]),
            (carA = 7, [7,8,13]),
            (carA = 8, [8,14]),
            (carA = 9, [9,10,15]),
            (carA = 10, [10,11,6]),        
            (carA = 11, [11,12,7]),
            (carA = 12, [12,13,8]),
            (carA = 13, [13,14]),         
            (carA = 14, [14,15,48]),
            time.sleep(3)
            (carA = 48, [14]),
            (carA = 14, [15]),
            (carA = 15, [16]),
            (carA = 16, [17,22]),
            (carA = 17, [18,23]),
            (carA = 18, [19,24]),
            (carA = 19, [20,25]),
            (carA = 20, [21,26]),
            (carA = 21, [27]),
            (carA = 22, [18,23]),
            (carA = 23, [19,24]),
            (carA = 24, [20,25]),
            (carA = 25, [21,26]),
            (carA = 26, [27]),
            (carA = 27, [28]),
            (carA = 28, [291,292]),
            (carA = 291, [292,37,30]),
            (carA = 292, [291,37,30]),            
            (carA = 37, [31,38]),
            (carA = 30, [31,38]),
            (carA = 31, [32]),
            (carA = 38, [39]),
            (carA = 39, [32]),
            (carA = 32, [56]),
            (carA = 56, [1])] #leaves lot and spawns back into first state
            
            
