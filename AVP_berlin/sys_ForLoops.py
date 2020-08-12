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
            ( 3,[3,4]),
            (4,[4,5,10]),
            (5,[5,6,11]),
            ( 6,[6,7,12]),
            (7,[7,8,13]),
            (8,[8,9,14]),
            (9,[9,14,15]),
            (10,[10,11,6]),        
            (11,[11,12,7]),
            (12,[12,13,8]),
            (13,[13,14,9]),
            
            (14,[14,15]),
            (15,[15,16]),
            (16,[16,17]),
            
            
            (48,[48,14]),
            (49,[49,15]),
            (50,[50,16]),
            
          #17-26 is for status 2 also  
            (17,[17,18]),
            (18,[18,19,48]), #parking
            (19,[19,20,49]), #parking
            (20,[20,21]),
            (21,[21,22]),
            (22,[22,23]),
            (23,[23,24,50]), #parking
            (24,[24,25]),
            (25,[25,26]),
            (26,[26,27]),
            
            (27,[27,28]),
            (28,[28,29]),
            (29,[29,30]),
            (30,[30,31]),
    
            (31,[31,32]),
            (32,[32,33]),
            (33,[33,34,51]),#parking
            (34,[34,35]),
            (35,[35,36]),
            (36,[36,37,52]),#parking
            (37,[37,38]),
            
            (38,[38,39]),
            (39,[39,40,53]),#parking
            (40,[40,41]),
            (41,[41,42,43]),
            (42,[42,44,54]),
            (43,[43,44]),
            (44,[44,45,55]),
            (45,[45,46,56]),
            (46,[46,47,57]),
            (47,[47,48,58]),
            (48,[48,49,59]),
    
            (49,[49,50,60]),
            (50,[50,51,61]),
            (51,[51,52,62]),
            (52,[52,53]),
            (53,[53,64]),
            (54,[54,55,45]),
            (55,[55,56,46]),
            (56,[56,57,47]),
            (57,[57,58,48]),
            (58,[58,59,49]),
            (59,[59,60,50]),
            (60,[60,61,51]),
            (61,[61,62,52]),
            (62,[62,63,53]),
            (63,[63,64]),
            (64,[64,65]),
            (65,[65,66]),
            (66,[66])]

carA_transitions = sys_list
carA_transitions_dict = dict(carA_transitions)
product_trans_list= []

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
            product_trans_list.append((start_node, end_node))

      
print('product_trans_list= ', product_trans_list)
           
             
#Want an end node and start node for each status value 
