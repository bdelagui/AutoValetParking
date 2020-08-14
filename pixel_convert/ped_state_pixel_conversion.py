#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:39:16 2020

@author: berlindelaguila
"""


abstr_to_pixel = {1:((145,160),(175,190)),
                2:((160,175),(175,190)),
                3:((175,190),(175,190)),
                4:((190,210),(175,190)),
                5:((210,225),(175,190))} 
                6:((225,240),(175,190))} 

# pixels to abstract 
pixels_to_abstr = {v: k for k, v in abstr_to_pixel.items()}
#print(pixels_to_abstr)

x_bounds = dict()
y_bounds = dict()
midpoint = dict()
for keys, vals in abstr_to_pixel.items():
    x_bounds[keys] = vals[0]
    y_bounds[keys] = vals[1]
    midpoint[keys] = ((vals[0][0] + vals[0][1])/2, (vals[1][0] + vals[1][1])/2) # stores (xmid, ymid) for each abstract state
    #print(x_bounds,'\n')
    #print(y_bounds,'\n')
    #print(midpoint,'\n')

def convert_to_pixels(keys):    
   return (keys, midpoint[keys])

print(convert_to_pixels(4))

pixel_range = dict()

for pixel_keys, state_vals in pixels_to_abstr.items():
    pixel_range[pixel_keys] = state_vals 


def convert_to_abstr(pixel_keys):
    return(pixel_range[pixel_keys])
    
print(convert_to_abstr(((225,240),(175,190))))

    