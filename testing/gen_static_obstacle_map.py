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

from dynamic_environment.gridworld_classes.gridworld_class import GridWorld 
from dynamic_environment.gridworld_classes.Player_class import Player
from dynamic_environment.transitions_classes.General_Game_Graph_class import GeneralGameGraph
from static_environment.transitions.test_run_configuration_transitions import test_run_configuration 
from coverage_propositions.lamda_functions import construct_lambda_functions
from map_representations.representation_conversions import abstr_to_pixel, pixel_to_abstr
from map_representations.system_product import sys_to_product, sys_from_product, construct_sys_product_transition
from map_representations.environment_product import env_to_product, env_from_product, construct_env_product_transition

Tsys, Tsys_dict = construct_sys_product_transition()
Tenv, Tenv_dict = construct_env_product_transition()

