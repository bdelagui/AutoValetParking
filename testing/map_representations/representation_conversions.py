# Function that maps abstr_to_pixels and pixels_to_abstr
# Function mapping T&E abstraction of physical objects in the AVP to pixel map:
# Ex: Input: state = 1, object = "car" or "pedestrian" or "obstacle", Output: pixel_square = [[x_low, x_up], [y_low, y_up]], and midpoint = ((x_low+x_up)/2, (y_low+y_up)/2)
# For static_obstacles, if object is not present on the grid, state = 0, else state = 1. If state == 0, the pixel square returned would be empty

# Building dictionaries by hand:

def construct_abstraction_dictionaries(object_type):
    abstr_to_pixel_car = {1:((120,130),(60,60)),
                    2:((135,145),(60,60)),
                    3:((150,160),(60,60)),
                    4:((155,165),(60,60)),
                    5:((175,175),(65,75)),
                    6:((175,175),(80,90)),
                    7:((175,175),(95,105)),
                    8:((175,175),(110,120)),
                    9:((175,175),(125,135)),
                    10:((170,170),(65,75)),
                    11:((170,170),(80,90)),
                    12:((170,170),(95,105)),
                    13:((170,170),(110,120)),
                    14:((170,170),(125,135)),
                    15:((160,170),(140,150)),
                    16:((155,165),(140,150)),
                    17:((140,150),(150,150)),
                    18:((125,140),(150,150)),
                    19:((110,120),(150,150)),
                    20:((95,105),(150,150)),
                    21:((80,90),(150,150)),
                    22:((65,75),(150,150)),               
                    23:((50,60),(150,150)),
                    24:((35,45),(150,150)),
                    25:((20,30),(150,150)),
                    26:((10,20),(155,165)),
                    27:((10,10),(170,180)),
                    28:((10,10),(185,195)),
                    29:((10,10),(200,210)),
                    30:((15,25),(210,220)),
                    
                    31:((30,40),(220,220)),
                    32:((45,55),(220,220)),
                    33:((55,65),(220,220)),
                    34:((75,85),(220,220)),
                    35:((90,100),(220,220)),
                    36:((105,115),(220,220)),
                    37:((120,130),(220,220)),
                    38:((135,145),(220,220)),
                    39:((150,160),(220,220)),
                    40:((165,175),(220,220)),
                    41:((180,190),(220,220)),
                    
                    42:((195,205),(205,215)),
                    43:((190,200),(205,215)),
                    44:((200,200),(190,200)),
                    45:((200,200),(175,185)),
                    46:((200,200),(160,170)),
                    47:((200,200),(145,155)),
                    48:((200,200),(130,140)),
                    49:((200,200),(115,125)),
                    50:((200,200),(100,110)),
                    51:((200,200),(85,95)),
                    52:((200,200),(70,80)),
                    53:((205,215),(55,65)),
                    
                    54:((205,205),(190,200)),
                    55:((205,205),(175,190)),        
                    56:((205,205),(160,170)),
                    57:((205,205),(145,155)),
                    58:((205,205),(130,140)),
                    59:((205,205),(115,125)),
                    60:((205,205),(100,110)),
                    61:((205,205),(85,95)),
                    62:((205,205),(70,80)),
                    63:((210,215),(60,70)),                
                    64:((220,230),(55,55)),            
                    65:((235,245),(55,55)),
                    66:((250,260),(55,55))}

    abstr_to_pixel_ped = {1:((145,155),(175,180)),
                2:((160,170),(175,180)),
                3:((175,185),(175,180)),
                4:((190,200),(175,180)),
                5:((205,215),(175,180))}

    if object_type == "car":
        map = abstr_to_pixel_car.copy()
    elif object_type == "pedestrian":
        map = abstr_to_pixel_car.copy()
    return map

# Returns the pixel square and midpoint pixel corresponding to the abstraction state:
def abstr_to_pixel(state, object_type):
    map = construct_abstraction_dictionaries(object_type)
    pixel_square = map[state]
    pixel_square_list = [[pixel_square[0][0], pixel_square[0][1]], [pixel_square[1][0], pixel_square[1][1]]]
    midpoint_pixel = [(pixel_square[0][0] + pixel_square[0][1])/2, (pixel_square[1][0] + pixel_square[1][1])/2]
    return pixel_square_list, midpoint_pixel

# Function that returns the abstraction in T&E state for the object given the (x_pix, y_pix) location in terms of pixels (or every 10 pixels) 
# For static_obstacle, if pixel_loc is empty, then return state = 0
def pixel_to_abstr(pixel_loc, object_type):
    map = construct_abstraction_dictionaries(object_type)
    pixels_to_abstr = {v: k for k, v in map.items()} # Flip the pixel dictionary
    x_pix_bounds = dict()
    y_pix_bounds = dict()
    x_pix_loc = pixel_loc[0]
    y_pix_loc = pixel_loc[1]
    abstr_state = []
    for k,v in map.items():
        x_pix_bounds[k] = v[0]
        y_pix_bounds[k] = v[1]
        in_x_range = x_pix_bounds[k][0] <= x_pix_loc and x_pix_loc <= x_pix_bounds[k][1]
        in_y_range = y_pix_bounds[k][0] <= y_pix_loc and y_pix_loc <= y_pix_bounds[k][1]
        if (in_x_range and in_y_range):
            abstr_state = k
            break
    return abstr_state
