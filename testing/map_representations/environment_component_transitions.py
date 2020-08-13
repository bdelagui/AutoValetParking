## Environment consists of the supervisor:

#sup = 1: supervisor waits for message from car
#sup = 2: supervisor sends command to system to park in parking lot 48
#sup = 3: supervisor sends command to system to park in parking lot 49
#sup = 4: supervisor sends command to system to park in parking lot 50 
#sup = 5: supervisor sends command to system to park in parking lot  51
#sup = 6: supervisor sends command to system to park in parking lot  52
#sup = 7: supervisor sends command to system to park in parking lot  53
#sup = 8: supervisor tells car to leave the garage
#sup = 9: supervisor receives msg from car  

sup_status_transitions_list = [(1, [9]), (2, [1,9]), (3, [1,9]),(4, [1,9]),
                        (5, [1,9]),(6, [1,9]),(7, [1,9]),
                        (9,[2,3,4,5,6,7,8])]
                                             
pedestrian_transitions_list = [(1,[1,2,5]),
              (2,[1,2,3]),
              (3,[2,3,4]),
              (4,[3,4,5]),
              (5,[4,5,1])]