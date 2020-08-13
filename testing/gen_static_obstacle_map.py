# Function call to synthesize static obstacles for the AutoValetParking grid:

import numpy as np
import random
from random import randrange
import importlib
import itertools
import pickle
import os
import math
import networkx as nx
import pdb
from time import gmtime, strftime

from dynamic_environment.gridworld_classes.gridworld_class import GridWorld 
from dynamic_environment.gridworld_classes.Player_class import Player
from dynamic_environment.transitions_classes.General_Game_Graph_class import GeneralGameGraph
from static_environment.transitions.test_run_configuration_transitions import test_run_configuration as trc
from coverage_propositions.lamda_functions import construct_lambda_functions
from map_representations.representation_conversions import abstr_to_pixel, pixel_to_abstr, get_pixel_radius
from map_representations.system_product import sys_to_product, sys_from_product, construct_sys_product_transition, get_sys_comp_trans, get_parking_spots
from map_representations.environment_product import env_to_product, env_from_product, construct_env_product_transition

# Filename to save location and radius of static_obstacle:
file_path = "static_obstacle_test_data/"
fname_static_obs = file_path + "static_obstacle_matrix_#.dat"
fname_static_obs = fname_static_obs.replace("#", strftime("%Y_%m_%d_%H_%M_%S", gmtime()))
fname_props = file_path + "propositions_#.dat"
fname_props = fname_props.replace("#", strftime("%Y_%m_%d_%H_%M_%S", gmtime()))
fname_reach_goal = file_path + "reachgoal_#.dat"
fname_reach_goal = fname_reach_goal.replace("#", strftime("%Y_%m_%d_%H_%M_%S", gmtime()))
pkl_obs = open(fname_static_obs,"wb")
pkl_prop = open(fname_props, "wb")
pkl_goal = open(fname_reach_goal,"wb")

# Transitions dictionaries:
Tsys, Tsys_dict = construct_sys_product_transition()
Tenv, Tenv_dict = construct_env_product_transition()

Tsys_components = get_sys_comp_trans()
Tsys_pos_dict = dict(Tsys_components["pos"])

# Set sys reach goal:
park_spots = get_parking_spots() # Getting system parking spots in terms of system position nodes
sys_reach_goal = [park_spots[0]] # Suppose we're interested in the first parking spot
pickle.dump(sys_reach_goal, pkl_goal)
pkl_goal.close()

# Set propositions:
propositions = [[23]]
Nprop = len(propositions)
pickle.dump(propositions, pkl_prop)
pkl_prop.close()

# Collect static obstacles for propositions:
test_config = trc(Tsys_pos_dict)
test_config.set_final_reach_goal(sys_reach_goal)
test_config.set_propositions(propositions)
via = "ValueFunc"
if via == "ValueFunc":
        cut_transitions, static_obstacles = test_config.generate_static_obstacles(propositions, sys_reach_goal)
if via == "Labels":
    static_obstacles = test_config.generate_static_obstacles_via_labels(propositions, sys_reach_goal)

# Convert static obstacles to a pixel map:
print("------------- Converting Static Obstacles to pixels --------------")
static_obs_pixels = [] # List of pixel location of obstacles and radius of static obs: examples: [[(120,50), 3], [(40, 50), 4]]
for prop_idx in range(Nprop):
    obstacles = static_obstacles[prop_idx]
    for obs in obstacles:
        pix_square, midpoint = abstr_to_pixel(obs, "car")
        obs_rad = get_pixel_radius(pix_square)
        static_obs_pixels.append([tuple(midpoint), obs_rad])

# Save in .pkl file:
pickle.dump(static_obs_pixels, pkl_obs)
pkl_obs.close()
