# dots

for every horizontal position x (11) in grid:
    tell gridDrawer to go to top left of the column (offset by x)
    for every vertical position y (10) in grid:
        when gridDrawer is not on top of barrier:
            draw a dot at that space
        move down one space