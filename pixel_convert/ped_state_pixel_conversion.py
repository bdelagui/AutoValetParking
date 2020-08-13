#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:39:16 2020

@author: berlindelaguila
"""


abstr_to_pixel = {1:((145,155),(175,180)),
                2:((160,170),(175,180)),
                3:((175,185),(175,180)),
                4:((190,200),(175,180)),
                5:((205,215),(175,180))}

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
    
print(convert_to_abstr(((205,215),(175,180))))

    