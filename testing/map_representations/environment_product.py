# File consisting of functions that map from the product state to the individual states of the components
from TE_vars import global_vars
from .environment_component_transitions import *

# Returns product transitions both as a list and a dictionary
def construct_env_product_transition():
    product_trans_list = []
    product_trans_dict = dict()
    ped_status = dict(pedestrian_transitions_list)
    sup_status = dict(sup_status_transitions_list)
    Nstat = len(sup_status_transitions_list)
    phi = lambda ped_key, sup_key: Nstat * (ped_key - 1) + sup_key

    for skey, sval in sup_status.items(): # supervisor
        for pkey, pval in ped_status.items(): # pedestrian
            start_node= phi(pkey, skey)  
            end_node_list = [] 
            # Turn-based transitions:
            for end_ped in pval:
                end_node = phi(end_ped, skey) # End transition in terms of position change node
                product_trans_list.append((start_node, end_node))
                if end_node not in end_node_list:
                    end_node_list.append(end_node)
            for end_sup in sval:
                end_node = phi(pkey, end_sup) # End transition in terms of status change
                product_trans_list.append((start_node, end_node))
                if end_node not in end_node_list:
                    end_node_list.append(end_node)
            # Concurrent transitions:
            for end_ped in pval:
                for end_sup in sval:
                    end_node = phi(end_ped, end_sup) # End transition in terms of both position and status change
                    product_trans_list.append((start_node, end_node))
                    if end_node not in end_node_list:
                        end_node_list.append(end_node)
            product_trans_dict[start_node] = end_node_list
    # Deleting duplicates:
    product_trans_list = list(dict.fromkeys(product_trans_list))
    return product_trans_list, product_trans_dict

def get_prod_conversion():
    Nstat = len(sup_status_transitions_list)
    phi = lambda ped_key, sup_key: Nstat * (ped_key - 1) + sup_key
    return phi

# Converts to product state from individual environment states
def env_to_product(ped, sup):
    phi = get_prod_conversion()
    product_state = phi(ped, sup)
    return product_state

# Computes component states from product states
def env_from_product(state):
    ped = []
    sup = []
    Nstat = len(sup_status_transitions_list)
    if state%Nstat == 0:
        sup = Nstat
        ped = state//Nstat
    else:
        sup = state%Nstat
        ped = state//Nstat + 1
    return ped, sup