# testing kyou_mo_kawaii function

import numpy as np
import simplejson as json
import random

with open("colors.json", "r") as file:
    data = json.load(file)

colors = data["colors"]
length = len(colors)

def suisei_wa(a, b, c):
    r, g, b, = a, b, c
    n = 0
    matched_color_index = 0
    placeholder_r = 0
    placeholder_g = 0
    placeholder_b = 0

    while n < length:
        color = colors[n]
        rgb = np.array(color['rgb_array'])

        if abs(r - rgb[0]) < abs(placeholder_r - rgb[0]) and abs(g - rgb[1]) < abs(placeholder_g - rgb[1]) and abs(b - rgb[2]) < abs(placeholder_b - rgb[2]):
            placeholder_r = abs(r - rgb[0])
            placeholder_g = abs(g - rgb[1])
            placeholder_b = abs(b - rgb[2])
            matched_color_index = n

        n += 1

    return matched_color_index

def kyou_mo_kawaii(a):

    combinations = colors[a]['combinations']

    matching_color_index = 1000

    while matching_color_index > 157:
        matching_color_index = random.choice(combinations)

    return matching_color_index

print(colors[suisei_wa(256,78,90)]['name'])
print(colors[kyou_mo_kawaii(suisei_wa(256,78,90))]['name'])