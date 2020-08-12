#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:40:15 2020

@author: berlindelaguila
"""
from collections import OrderedDict 

# statusCar = 1: car sends message to supervisor asking for a parking spot
# statusCar = 2: car in process of going to parking spot
# statusCar = 3: car receives a message from supervisor
# statusCar = 4: waiting for response from supervisor 


status_car = [(1,[4]),(2,[2,3]),(3,[2]),(4,[3,4])]
status_car_dict= dict(status_car)

#parking_spots = [48,49,50,51,52,53]

sys_list = [(1,[1,2]),
            ( 2,[2,3]),
            ( 3,[3,4,9]),
            (4,[4,5,10])]

carA_transitions = sys_list
carA_transitions_dict = dict(carA_transitions)
system_trans_list= []

ns= len(status_car)

#index of (carA_key, status) is determined by phi
phi = lambda carA_key, status: ns * (carA_key - 1) + status

#index of (end_carA_transitions, status) is determined by psi
psi = lambda end_carA_transitions, status: ns * (end_carA_transitions - 1) + status

for status, status_val in status_car:
    #print(status,status_val)
    for carA_key, carA_val in carA_transitions: 
      
        #print(carA_val, status)
        start_node= phi(carA_key, status)  
        #print('\n','carA_key,status: ',carA_key ,',',status)
        #print('start_node= ',start_node)
          
        for end_carA_transitions in carA_val:
           #print(end_carA_transitions)
            end_node = psi(end_carA_transitions, status)
            #print('end_carA_transitions, status: ', end_carA_transitions,status)
            #print('end_node= ', end_node)
            system_trans_list.append((start_node, end_node))

      
print('system_trans_list= ', system_trans_list)
           
             
#Want an end node and start node for each status value 
