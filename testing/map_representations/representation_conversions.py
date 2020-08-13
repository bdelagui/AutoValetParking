# Function that maps abstr_to_pixels and pixels_to_abstr
# Function mapping T&E abstraction of physical objects in the AVP to pixel map:
# Ex: Input: state = 1, object = "car" or "pedestrian" or "obstacle", Output: pixel_square = [[x_low, x_up], [y_low, y_up]], and midpoint = ((x_low+x_up)/2, (y_low+y_up)/2)
# For static_obstacles, if object is not present on the grid, state = 0, else state = 1. If state == 0, the pixel square returned would be empty

# Building dictionaries by hand:

def construct_abstraction_dictionaries(object_type):
    abstr_to_pixel_car = {1:((120,130),(60,65)),
                2:((135,145),(60,65)),
                3:((150,160),(60,65)),
                4:((155,165),(60,65)),
                5:((175,180),(65,75)),
                6:((175,180),(80,90)),
                7:((175,180),(95,105)),
                8:((175,180),(110,120)),
                9:((175,180),(125,135)),
                10:((170,175),(65,75)),
                11:((170,175),(80,90)),
                12:((170,175),(95,105)),
                13:((170,175),(110,120)),
                14:((170,175),(125,135)),
                15:((170,175),(140,150)),
                16:((155,165),(140,150)),
                17:((140,150),(140,155)),
                18:((125,140),(140,155)),
                19:((110,120),(140,155)),
                20:((95,105),(140,155)),
                21:((80,90),(140,155)),
                22:((65,75),(140,155)),
                23:((50,60),(140,155)),
                24:((35,45),(140,155)),
                25:((20,30),(140,155)),
                26:((10,20),(155,165)),
                27:((10,15),(170,180)),
                28:((10,15),(185,195)),
                29:((10,15),(200,210)),
                30:((15,25),(210,220)),
                
                31:((30,40),(220,225)),
                32:((45,55),(220,225)),
                33:((55,65),(220,225)),
                34:((75,85),(220,225)),
                35:((90,100),(220,225)),
                36:((105,115),(220,225)),
                37:((120,130),(220,225)),
                38:((135,145),(220,225)),
                39:((150,160),(220,225)),
                40:((165,175),(220,225)),
                41:((180,190),(220,225)),
                
                42:((195,205),(205,215)),
                43:((190,200),(205,215)),
                44:((200,205),(190,200)),
                45:((200,205),(175,185)),
                46:((200,205),(160,170)),
                47:((200,205),(145,155)),
                48:((200,205),(130,140)),
                49:((200,205),(115,125)),
                50:((200,205),(100,110)),
                51:((200,205),(85,95)),
                52:((200,205),(70,80)),
                53:((200,205),(55,65)),
                
                54:((205,210),(190,200)),
                55:((205,210),(175,190)),
                56:((205,210),(160,170)),
                57:((205,210),(145,155)),
                58:((205,210),(130,140)),
                59:((205,210),(115,125)),
                60:((205,210),(100,110)),
                61:((205,210),(85,95)),
                62:((205,210),(70,80)),
                63:((210,215),(60,70)),                
                64:((220,230),(55,60)),
                65:((235,245),(55,60)),
                66:((250,260),(55,60))}

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

# Returning radius of a certain pixel square
def get_pixel_radius(pixel_square):
    xlen = pixel_square[0][1]-pixel_square[0][0]
    ylen = pixel_square[1][1]-pixel_square[1][0]
    rad = min(xlen, ylen)
    return rad