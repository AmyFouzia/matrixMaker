from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 158, 96, 144 ]
matrix = new_matrix()

add_edge(matrix, 50, 350, 50, 100, 400, 100)
add_edge(matrix, 50, 350, 50, 90, 320, 100)
add_edge(matrix, 100, 400, 50, 130, 350, 100)
add_edge(matrix, 90, 320, 50, 130, 350, 100)

draw_lines(matrix, screen, color)
display(screen)
