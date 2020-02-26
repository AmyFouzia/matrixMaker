from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 158, 96, 144 ]
matrix = new_matrix()

add_edge(matrix, 50, 250, 50, 100, 270, 100)
add_edge(matrix, 50, 250, 50, 90, 220, 100)
add_edge(matrix, 100, 270, 50, 130, 250, 100)
add_edge(matrix, 90, 220, 50, 130, 250, 100)
add_edge(matrix, 90, 220, 50, 100, 200, 100)
add_edge(matrix, 70, 190, 50, 100, 200, 100)
add_edge(matrix, 130, 190, 50, 100, 200, 100)
add_edge(matrix, 100, 150, 50, 100, 200, 100)
add_edge(matrix, 100, 150, 50, 70, 130, 100)
add_edge(matrix, 100, 150, 50, 130, 130, 100)

add_edge(matrix, 105, 275, 50, 95, 285, 100)
add_edge(matrix, 110, 290, 50, 95, 285, 100)
add_edge(matrix, 110, 290, 50, 170, 275, 100)
add_edge(matrix, 105, 275, 50, 170, 275, 100)

add_edge(matrix, 210, 295, 50, 170, 275, 100)
add_edge(matrix, 215, 295, 50, 170, 275, 100)

draw_lines(matrix, screen, color)
display(screen)
