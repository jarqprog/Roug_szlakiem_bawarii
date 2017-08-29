from msvcrt import getch
with open('mapa_forest.txt', 'r') as myfile:
    mapa = myfile.read()
mapa = list(mapa)
position_horizontal = 1
position_vertical = 18
lenght_of_the_map_plus_one = 81
map_copy = mapa[:]
map_copy[position_horizontal + position_vertical * 81] = "@"
print("".join(map_copy))
while True:
    print("Press w, s, d or a:")
    input_char = getch()
    print(input_char)
    if input_char == b'w': 
        map_copy[position_horizontal + position_vertical * 81] = "."
        position_vertical -= 1
        map_copy[position_horizontal + position_vertical * 81] = "@"
        print("".join(map_copy))
    elif input_char == b's': 
        map_copy[position_horizontal + position_vertical * 81] = "."
        position_vertical += 1
        map_copy[position_horizontal + position_vertical * 81] = "@"
        print("".join(map_copy))
    elif input_char == b'd': 
        map_copy[position_horizontal + position_vertical * 81] = "."
        position_horizontal += 1
        map_copy[position_horizontal + position_vertical * 81] = "@"
        print("".join(map_copy))
    elif input_char == b'a': 
        map_copy[position_horizontal + position_vertical * 81] = "."
        position_horizontal -= 1
        map_copy[position_horizontal + position_vertical * 81] = "@"
        print("".join(map_copy))
    else:
        continue

