def run_langton(rules, size):
    antx = size // 2
    anty = size // 2
    angle = 90
    count = 0
    color_values = []  # this list describes the color value of each cell
    grid = []  # only used to print out and visualize coordinates, not used in actual code

    def create_grid():
        for row in range(size):
            color_values.append([])
            for col in range(size):
                color_values[row].append(0)
                grid.append((col, row))

    def change_color():
        color_values[anty][antx] += 1
        color_values[anty][antx] %= len(rules)

    create_grid()
    change_color()
    count += 1
    anty -= 1
    while (size - 1) >= antx >= 0 and (size - 1) >= anty >= 0:
        # change angle depending on rules
        color = color_values[anty][antx]
        if rules[color] == 'R':
            angle -= 90 % 360
            angle = angle % 360
        if rules[color] == 'L':
            angle += 90
            angle = angle % 360
        # change color
        change_color()
        # move according to angle
        if angle == 0:
            antx += 1
        if angle == 90:
            anty -= 1
        if angle == 180:
            antx -= 1
        if angle == 270:
            anty += 1
        count += 1
    return (count, color_values)