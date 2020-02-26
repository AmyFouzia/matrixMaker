from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 158, 96, 144 ]
matrix = new_matrix()

add_edge(matrix, 50, 50, 50, 100, 100, 100)

draw_lines(matrix, screen, color)
display(screen)
