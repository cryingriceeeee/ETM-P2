import simplejson as json

r, g ,b = 255, 121, 12

matched_color = 'Unknown'

with open('colors.json', 'r') as file:
    data = json.load(file)
for color in data:
    rgb = color['rgb_array']
    placeholder_r = 0
    placeholder_g = 0
    placeholder_b = 0
    if abs(r - rgb[0]) < abs(placeholder_r - rgb[0]) and abs(g - rgb[1]) < abs(placeholder_g - rgb[1]) and abs(b - rgb[2]) < abs(placeholder_b - rgb[2]):
        placeholder_r = abs(r - rgb[0])
        placeholder_g = abs(g - rgb[1])
        placeholder_b = abs(b - rgb[2])
        matched_color = color['name']

if matched_color == 'Unknown':
    print('Could not find matching/similar color')
else:
    print(f"The matched color is: {matched_color}")