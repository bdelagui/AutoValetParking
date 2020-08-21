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
import pickle
import random
from ipdb import set_trace as st
# import components
from prepare.boxcomponent import BoxComponent
from components.car import Car
# from testing.test_pedestrian import Pedestrian
import pdb

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
    #pdb.set_trace()
    async def generate_car(self, start_time, park_time):
        self.garage_open = True

    async def generate_car(self, start_time, park_time, parking_spot_number):
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
        await self.out_channels['Planner'].send([car, ('Park', parking_spot_number)])
        self.cars.append(car)
   # pdb.set_trace()

    async def send_car_to_spot(self,car,spot):
        await self.out_channels['Planner'].send([car, ('Park', spot)])
        
    #pdb.set_trace()

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

    async def start_ped(self,TestPed):
        # spawn the ped in loc A and save to ped list
        print('Spawning ped')

    async def stop_ped(self,TestPed):
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
        

        
    async def receive_response(self, Planner): 
        print('TEST SUITE - receiving response')
        async with self.in_channels['Planner']:
            async for response in self.in_channels['Planner']:
                car = response[0]
                print('Response received')
                self.get_next_env_action(response)
                #await self.add_obs((200,212.5,0,3)) #The new obstacle being added
                #await trio.sleep(5)
                await self.request_car(car) # requesting car for test
               

    async def update_system_state(self):
        print('Updating the system state')

    async def run_test(self,Planner,Game):
        print('Testing')
        await self.receive_response(Planner)

    async def run(self,Planner,Game): #TestPed, TestSupervisor, TestObstacles
        print('TEST SUITE - started')
        now = trio.current_time()
        park_time = 300 #
        parking_spot_number = 2 
        await self.generate_car(now, park_time, parking_spot_number)
        park_time = 300
        self.sup_2_ped, self.ped_2_sup = trio.open_memory_channel(25)
        # read in the testing data
        # sys.path.append('../static_obstacle_test_data')
       # with open(sys.path[0]+'/../testing/static_obstacle_test_data/propositions.dat', 'rb') as f:
        with open('../testing/static_obstacle_test_data/propositions.dat', 'rb') as f:
           self.propositions = pickle.load(f)
        #with open(sys.path[0]+'/../testing/static_obstacle_test_data/reachgoal.dat', 'rb') as f:
        with open('../testing/static_obstacle_test_data/reachgoal.dat', 'rb') as f:
            self.reachgoal = pickle.load(f)
        # find which spot to park at from reachgoal test parking_data
        parking_spot_number = random.sample(self.parking_spots.keys(),1)[0]
        await self.generate_car(now, park_time, parking_spot_number)
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.run_test,Planner,Game)

   # pdb.set_trace()
        

