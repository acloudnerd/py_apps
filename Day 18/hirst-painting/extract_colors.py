import colorgram


rgbs = []
colors  = colorgram.extract('hirst_Painting.jpeg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    the_color = (r,g,b)
    rgbs.append(the_color)

print(rgbs)

