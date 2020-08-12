#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 08:57:45 2020

@author: berlindelaguila
"""
import numpy as np 

#Physical states for sys are same as states in visual abstraction 

#Need two for loops: 
   # One loop will iterate through the four statuses of the car and the other will iterate through all the possible physical states 

# statusCar = 1: car sends message to supervisor asking for a parking spot
# statusCar = 2: car in process of going to parking spot
# statusCar = 3: car receives a message from supervisor
# statusCar = 4: waiting for response from supervisor 
#variables modeling the environment and the behaviors they can take 
    #peds, sup,
status_car_list = [1,2,3,4]
parking_spots = [48,49,50,51,52,53]
status_transitions = [(1,[4]),(2,[3]),(3,[2]),(4,[3,4])]


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



#sys_list_dict = dict(sys_list)
#print(sys_list_dict[i]) 
       
car_transitions = sys_list

i = int 
for i in status_car_list:
   def construct_state():
       result = 4*(carA-1) + status
       print(result)
       i+=1
#For construct_state: key = iterator in the dictionary, s = value associated w/ that key        
   for key, val in car_transitions[0].items(): # Looping through key and values in dictionary
       start_sys = construct_state(key, s) 
       print(start_sys)
       
     #  end_sys = [construct_state(s, k), for k in val]
       sys_trans.append(start_sys)
       

         
 
"""
if statusCar == 2: 
    sys_list = ((1,[1,2]),
            (2,[2,3]),
            (3,[3,4,9]),
            (4,[4,5,10]),
            (5,[5,6,11]),
            (6,[6,7,12]),
            (7,[7,8,13]),
            (8,[8,14]),
            (9,[9,10,15]),
            (10,[10,11,6]),        
            (11,[11,12,7]),
            (12,[12,13,8]),
            (13,[13,14]),         
           
            (14,[14,15]),
            (15,[15,16]),
            (16,[16,17,22]),
            
            
            (48,[48,14]),
            (49,[49,15]),
            (50,[50,16]),
            
            (17,[17,18,23]),
            (18,[18,19,24]),
            (19,[19,20,25]),
            (20,[20,21,26]),
            (21,[21,27]),
            (22,[22,18,23]),
            (23,[23,19,24]),
            (24,[24,20,25]),
            (25,[25,21,26]),
            (26,[26,27]),
            
            (27,[27,28]),
            (28,[28,291,292]),
            (291,[291,292,37,30]),
            (292,[291,292,37,30]),
            
            (51,[51,27]),
            (52,[52,28]),
            (53,[53,292]),
            (30,[30,31,38]),
            (31,[31,32,39]),
            (32,[32,33,40]),
            (33,[33,34,41]),
            (34,[34,35,42]),
            (35,[35,36,43]),
            (36,[36,44]),
            (37,[37,31,38]),
            
            (38,[38,32,39]),
            (31,[31]),
            (39,[39,33,40]),
            (40,[40,34,41]),
            (41,[41,35,42]),
            (42,[42,36,43]),
            (43,[43,44]),
            (44,[44,45]),
            (45,[45,46]),
            (46,[46]),
            (36,[36,44]),
            (37,[37,31,38]))
    sys_list_dict = dict(sys_list)
    print(sys_list_dict[16])  
                       
"""
             

#For stausCar=3:           
# CarA=CarA
#For stausCar=4: 
#(46,[46,47])
    
