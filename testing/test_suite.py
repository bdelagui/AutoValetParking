# Automated Valet Parking - Test Suite - Main Testing Component (for T&E of car component)
# Josefine Graebener
# California Institute of Technology
# July, 2020

# import variables
from variables.geometries import UPPER_SPOTS, LOWER_SPOTS, MIDDLE_BOX
from variables.global_vars import MAX_NO_PARKING_SPOTS, TOW_TIME, DELAY_THRESH, start_walk_lane, end_walk_lane, start_walk_lane_2, end_walk_lane_2, SCALE_FACTOR_PLAN as SFP, START_X, START_Y, START_YAW
from variables.parking_data import test_spots as parking_spots
# import communication functions
from prepare.communication import get_current_time
# import packages
import trio
import random
from ipdb import set_trace as st
<<<<<<< HEAD
=======
import numpy as np
import sys
import pickle
>>>>>>> 54a0098b69bdcc8f14c720732d4585c81206d0d3
# import components
from prepare.boxcomponent import BoxComponent
from components.car import Car
# from testing.test_pedestrian import Pedestrian

class TestSuite(BoxComponent):
    def __init__(self, nursery):
        super().__init__()
        self.name = self.__class__.__name__
        self.nursery = nursery
        self.counter = 1
        self.cars = []
        self.spot_no = len(list(parking_spots.keys()))
        self.testpedlist = dict()
        self.parking_spots = dict([(i, ("Vacant", "None")) for i in list(parking_spots.keys())])
        self.Logger = None

    async def generate_car(self, start_time, park_time):
        print('TEST SUITE - Generating car')
        arrive_time = get_current_time(start_time)
        depart_time = arrive_time + park_time
        car = Car(arrive_time=arrive_time, depart_time=depart_time)
        car.id = self.counter
        self.counter=self.counter+1
        car.x = START_X
        car.y = START_Y
        car.yaw = START_YAW
        # update Game
        await self.out_channels['Game'].send(car)
        print("Car with Name {0} and ID {1} arrives at {2:.3f}".format(car.name,car.id, car.arrive_time))
        await self.out_channels['Planner'].send([car, ('Park', self.spot_no)])
        self.cars.append(car)

    async def send_car_to_spot(self,car,spot):
        await self.out_channels['Planner'].send([car, ('Park', spot)])

    async def request_car(self,car):
        now = trio.current_time()
        print('{0} is requested at {1:.3f}'.format(car.name,now))
        car.depart_time = now
        car.requested = True
        await self.out_channels['Planner'].send([car, 'Pickup'])

    async def fail_car(self,car, Game):
        car.failure()
        print('{0} / ID {1} Failing'.format(car.name, car.id))
        await self.failure(Game)

<<<<<<< HEAD
    async def start_ped(self,TestPed):
        # spawn the ped in loc A and save to ped list
        print('Spawning ped')

    async def stop_ped(self,TestPed):
=======
    async def start_ped(self, start_at, stop_at, ped_type):
        # spawn the ped in loc A and save to pedestrian list
        #print(ped_type)
        if not ped_type:
            ped_type=random.choice(['1','2','3','4','5','6'])
        dx = stop_at[0]-start_at[0]
        dy = stop_at[0]-start_at[0]
        heading = np.arctan2(-dy,dx)
        #print(ped_type)
        #st()
        ped = TestPed(init_state =(start_at[0],start_at[1],heading,0),pedestrian_type=ped_type)
        if dx >=0:
            ped.status = 'WalkE'
        else:
            ped.status = 'WalkW'
        self.nursery.start_soon(ped.run,start_at,stop_at)
        await self.out_channels['GameEnterPeds'].send(ped)
        self.peds.append(ped)
        print('TEST SUPERVISOR - Adding pedestrian to lower crosswalk')

    async def stop_ped(self):
>>>>>>> 54a0098b69bdcc8f14c720732d4585c81206d0d3
        print('Stop ped')

    async def ped_walk_west(self,TestPed):
        print('Ped walking west')

    async def ped_walk_east(self,TestPed):
        print('Ped walking east')

    def get_next_env_action(self, response):#, TestPed, TestObstacles):
        print('Read test script here')
        # read the script
        # call the actions from above here depending on sys state

    async def add_obs(self,obs):
        directive = ['Add',obs]
        print('Adding obstacle')
        await self.out_channels['Obstacles'].send(directive)
    # Try creating function to remove obstacles here???? -BD 
    async def receive_response(self, Planner):
        print('TEST SUITE - receiving response')
        async with self.in_channels['Planner']:
            async for response in self.in_channels['Planner']:
                car = response[0]
                print('Response received')
                self.get_next_env_action(response)
                await self.add_obs((70, 150, 0, 3))
                await trio.sleep(5)
                await self.request_car(car) # requesting car for test

    async def update_system_state(self):
<<<<<<< HEAD
        print('Updating the system state')
=======
        # print('Updating the system state')
        ped_started = False
        ped_stopped = False
        obs_added = False
        ped_walking_east = False
        ped_walking_west = False
        while self.garage_open:
            # These are just example actions
            # Here call the test script with the system state and env state
            # and call actions accordingly
            # Read system state
            car = self.cars[0]
            sys_state = [car.x, car.y]
            # generate env action here
            # self.get_next_env_action(sys_state)
            # example pedestrian actions
            if car.y > 20 and not ped_started: # generate pedestrian for the first time and walk towards east
                ped_started = True
                ped_walking_east = True
                ped_walking_west = False
                stop_at = (2700,2090)
                start_at = (1730,2090)
                await self.start_ped(start_at,stop_at,'3')
            if car.status == 'Completed' and not ped_stopped: # stop pedestrian when car is parked
                ped_stopped = True
                ped_walking_east = False
                ped_walking_west = False
                await self.stop_ped()
            if car.x < 15 and not car.status =='Completed' and ped_stopped: # turn around to walk west
                ped_stopped = False
                ped_walking_east = False
                ped_walking_west = True
                stop_at = (1730,2090)
                start_at = (2700,2090)
                await self.ped_walk(start_at,stop_at)
            # example obstacle action
            if car.status == 'Completed' and not obs_added:
                obs_added = True
                #await self.add_obs((100, 150, 0, 5))
            await trio.sleep(0)
>>>>>>> 54a0098b69bdcc8f14c720732d4585c81206d0d3

    async def run_test(self,Planner,Game):
        print('Testing')
        await self.receive_response(Planner)

    async def run(self,Planner,Game): #TestPed, TestSupervisor, TestObstacles
        print('TEST SUITE - started')
        now = trio.current_time()
<<<<<<< HEAD
        park_time = 300 #
=======
        park_time = 300
        self.sup_2_ped, self.ped_2_sup = trio.open_memory_channel(25)
        # read in the testing data
        # sys.path.append('../static_obstacle_test_data')
        with open('propositions.dat', 'rb') as f:
            self.propositions = pickle.load(f)
        with open('reachgoal.dat', 'rb') as f:
            self.reachgoal = pickle.load(f)
        # find which spot to park at from reachgoal test parking_data

>>>>>>> 54a0098b69bdcc8f14c720732d4585c81206d0d3
        await self.generate_car(now, park_time)
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.run_test,Planner,Game)


        

