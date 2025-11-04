import simplejson as json

while True:
    r = int(input("Enter a red value (0-255): "))
    if r < 0 or r > 255:
        print("Invalid value entered. Please try again.")
    else:
        break
while True:
    g = int(input("Enter a green value (0-255): "))
    if g < 0 or g > 255:
        print("Invalid value entered. Please try again.")
    else:
        break

while True:
    b = int(input("Enter a blue value (0-255): "))
    if b < 0 or b > 255:
        print("Invalid value entered. Please try again.")
    else:
        break

color_data = {'r': r, 'g': g, 'b': b}
print(color_data)

matched_color = 'Unknown'

with open('colors.json', 'r') as file:
    data = json.load(file)
for color in data:
    rgb = color['rgb']
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