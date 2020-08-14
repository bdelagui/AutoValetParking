# File that converts individual states of system components to the product state and vice-versa
from TE_vars import global_vars
import sys
sys.path.append('/Users/berlindelaguila/AutoValetParking/testing/testing/map_representations')
import system_component_transitions

# Returns the transition dictionaries for individual system components
def get_sys_comp_trans():
    car_components = dict()
    car_components["pos"] = car_pos_transitions_list
    car_components["status"] = car_status_transitions_list
    return car_components

# Return parking spots in terms of system position values
def get_parking_spots():
    return parking_spots

# Returns product transitions both as a list and a dictionary
def construct_sys_product_transition():
    product_trans_list = []
    product_trans_dict = dict()
    car_status = dict(car_status_transitions_list)
    car_pos_transitions = dict(car_pos_transitions_list)
    Nstat = len(car_status_transitions_list)
    phi = lambda pos, status: Nstat * (pos - 1) + status
    for skey, sval in car_status.items():
        for pkey, pval in car_pos_transitions.items(): 
            start_node= phi(pkey, skey) 
            end_node_list = [] 
            # Turn-based transitions:
            for end_pos in pval:
                end_node = phi(end_pos, skey) # End transition in terms of position change node
                product_trans_list.append((start_node, end_node))
                if end_node not in end_node_list:
                    end_node_list.append(end_node)
            for end_status in sval:
                end_node = phi(pkey, end_status) # End transition in terms of status change
                product_trans_list.append((start_node, end_node))
                if end_node not in end_node_list:
                    end_node_list.append(end_node)
            # Concurrent transitions:
            for end_pos in pval:
                for end_status in sval:
                    end_node = phi(end_pos, end_status) # End transition in terms of both position and status change
                    product_trans_list.append((start_node, end_node))
                    if end_node not in end_node_list:
                        end_node_list.append(end_node)
            product_trans_dict[start_node] = end_node_list
    # Deleting duplicates:
    product_trans_list = list(dict.fromkeys(product_trans_list))
    return product_trans_list, product_trans_dict

def get_prod_conversion():
    Nstat = len(car_status_transitions_list)
    phi = lambda pos, status: Nstat * (pos - 1) + status
    return phi

# Converts to product state
def sys_to_product(car_pos, car_stat):
    phi = get_prod_conversion()
    product_state = phi(car_pos, car_stat)
    return product_state

# Takes product state and returns car_pos and car_status
def sys_from_product(state):
    car_pos = []
    car_stat = []
    Nstat = len(car_status_transitions_list)
    if state%Nstat == 0:
        car_stat = Nstat
        car_pos = state//Nstat
    else:
        car_stat = state%Nstat
        car_pos = state//Nstat + 1
    return car_pos, car_stat


# statusCar = 1: car sends message to supervisor asking for a parking spot
# statusCar = 2: car in process of going to parking spot
# statusCar = 3: car receives a message from supervisor
# statusCar = 4: waiting for response from supervisor 


