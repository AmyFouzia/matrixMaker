from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 158, 96, 144 ]
matrix = new_matrix()

for i in range(XRES):
    add_point(matrix, i, YRES - i)
    add_point(matrix, YRES - i, i)

draw_lines(matrix, screen, color)
display(screen)
