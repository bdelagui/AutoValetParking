#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:03:12 2020

@author: berlindelaguila
"""

#sup = 1: supervisor waits for message from car
#sup = 2: supervisor sends command to system to park in parking lot 48
#sup = 3: supervisor sends command to system to park in parking lot 49
#sup = 4: supervisor sends command to system to park in parking lot 50 
#sup = 5: supervisor sends command to system to park in parking lot  51
#sup = 6: supervisor sends command to system to park in parking lot  52
#sup = 7: supervisor sends command to system to park in parking lot  53
#sup = 8: supervisor tells car to leave the garage
#sup = 9: supervisor receives msg from car  



sup_status_transitions = [(1, [9]), (2, [1,9]), (3, [1,9]),(4, [1,9]),
                        (5, [1,9]),(6, [1,9]),(7, [1,9]),
                        (9,[2,3,4,5,6,7,8])]
                                             
#For peds: physical state 54= state1, 55=2, 39=3, 32=4, 56=5
peds_list = [(1,[1,2,5]),
              (2,[1,2,3]),
              (3,[2,3,4]),
              (4,[3,4,5]),
              (5,[4,5,1])]


sup_status_transitions_dict = dict(sup_status_transitions)
peds_list_dict = dict(peds_list)
env_trans_list = []
ns = len(sup_status_transitions)

alpha = lambda ped_key, sup_key: ns * (ped_key - 1) + sup_key
gamma = lambda ped_val, sup_key: ns * (ped_val - 1) + sup_key

    
for sup_key, sup_val in sup_status_transitions:
   # print(sup_key, sup_val)
    for ped_key, ped_val in peds_list:
    #    print(ped_key,ped_val)
        start_node = alpha(ped_key,sup_key)
        print('\n','ped_key, sup_key: ',ped_key ,',',sup_key)
        print('start_node= ',start_node)
         
        for ped_val_elem in ped_val:
            #print(end_carA_transitions)
             end_node = gamma(ped_val_elem, sup_key)
             print('ped_val_elem, sup_key: ', ped_val_elem, sup_key)
             print('end_node= ', end_node)              
             env_trans_list.append((start_node, end_node))
print('env_trans_list, ',env_trans_list)

