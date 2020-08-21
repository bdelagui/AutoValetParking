# Function that maps abstr_to_pixels and pixels_to_abstr
# Function mapping T&E abstraction of physical objects in the AVP to pixel map:
# Ex: Input: state = 1, object = "car" or "pedestrian" or "obstacle", Output: pixel_square = [[x_low, x_up], [y_low, y_up]], and midpoint = ((x_low+x_up)/2, (y_low+y_up)/2)
# For static_obstacles, if object is not present on the grid, state = 0, else state = 1. If state == 0, the pixel square returned would be empty

# Building dictionaries by hand:

def construct_abstraction_dictionaries(object_type):
    abstr_to_pixel_car = {1:((110,130),(55,70)),
                2:((130,145),(55,70)),
                3:((145,160),(55,70)),
                4:((160,175),(55,70)),
                5:((175,190),(55,70)),
                6:((175,190),(70,85)),
                7:((175,190),(85,100)),
                8:((175,190),(100,115)),
                9:((175,190),(115,130)),
                10:((175,190),(130,145)),
                11:((170,190),(145,165)),
                12:((160,175),(70,85)),
                13:((160,175),(85,100)),
                14:((160,175),(100,115)),
                15:((160,175),(115,130)),
                16:((160,175),(130,145)),
                17:((160,175),(145,165)),
                
                18:((145,160),(145,165)),
                19:((130,145),(145,165)),
                20:((115,130),(145,165)),
                21:((100,115),(145,165)),
                22:((85,100),(145,165)),
                23:((70,85),(145,165)),
                24:((55,70),(145,165)),
                25:((40,55),(145,165)),
                26:((25,40),(145,160)),
                
                27:((145,160),(130,145)),
                28:((130,145),(130,145)),
                29:((115,130),(130,145)),
                30:((100,115),(130,145)),
                31:((85,100),(130,145)),
                32:((70,85),(130,145)),
                33:((55,70),(130,145)),
                34:((40,55),(130,145)),
                35:((25,40),(130,145)),
                36:((5,25),(130,145)),
                
                37:((5,25),(145,160)),
                38:((5,25),(160,175)),
                39:((5,25),(190,205)),
                40:((5,25),(205,220)),
                41:((5,25),(220,235)),
                42:((5,25),(235,250)),
                
                43:((25,40),(160,175)),
                44:((25,40),(175,190)),
                45:((25,40),(190,205)),
                46:((25,40),(205,220)),
                47:((25,40),(220,235)),
                
                48:((135,145),(120,130)), #parking
                49:((95,105),(120,130)), #parking
                50:((55,65),(120,130)), #parking
                51:((70,80),(230,240)), #parking 
                52:((110,120),(230,240)), #parking
                53:((150,160),(230,240)), #parking
                
                54:((40,55),(205,220)),
                55:((55,70),(205,220)),
                56:((70,85),(205,220)),
                57:((85,100),(205,220)),
                58:((100,115),(205,220)),
                59:((115,130),(205,220)),
                60:((130,145),(205,220)),
                61:((145,160),(205,220)),
                62:((160,175),(205,220)),
                63:((175,190),(205,220)),                
                64:((190,210),(205,220)),
                
                
                65:((40,55),(220,230)),
                66:((55,70),(220,230)),
                67:((70,85),(220,230)),
                68:((85,100),(220,230)),
                69:((100,115),(220,230)),
                70:((115,130),(220,230)),
                71:((130,145),(220,230)),
                72:((145,160),(220,230)),
                73:((160,175),(220,230)),
                74:((175,190),(220,230)),
                75:((190,210),(220,230)),
                76:((205,225),(220,230)),
                77:((210,225),(205,220)),
                
                78:((210,225),(190,205)),
                79:((210,225),(175,190)), # ped state 5
                80:((210,225),(160,175)),
                81:((210,225),(145,160)),
                82:((210,225),(130,145)),
                83:((210,225),(115,130)),
                84:((210,225),(100,115)),
                85:((210,225),(85,100)),
                86:((210,225),(70,85)),
                87:((210,225),(50,70)),

                88:((190,210),(190,205)),
                89:((190,210),(175,190)), #ped state 4
                90:((190,210),(160,175)),
                91:((190,210),(145,160)),
                92:((190,210),(130,145)),
                93:((190,210),(115,130)),
                94:((190,210),(100,115)),
                95:((190,210),(85,100)),
                96:((190,210),(70,85)),
                97:((190,210),(55,70)),
                
                98:((225,240),(50,70)),
                99:((240,255),(50,70)),
                100:((255,270),(50,70))}

    abstr_to_pixel_ped = {1:((145,160),(175,190)),
                2:((160,175),(175,190)),
                3:((175,190),(175,190)),
                4:((190,210),(175,190)),
                5:((210,225),(175,190)),
                6:((225,240),(175,190))} 

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
    return rad/6 #divide by two bc it was originally computing diameter 
