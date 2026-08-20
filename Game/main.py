import pygame
from grid import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

margin: int = 50

grid_size = 50
cell_size = 10

grid: CellGrid = CellGrid(grid_size)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid.flip_cell(get_cell_from_position(pygame.mouse.get_pos()))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    grid.update_all()
                    
        draw_all_cells()
        draw_grid()
        #print(get_cell_from_position(pygame.mouse.get_pos()))
        #print(grid.is_cell_alive(get_cell_from_position(pygame.mouse.get_pos())))
        print(grid.get_cell_neighbor_count(get_cell_from_position(pygame.mouse.get_pos())))
        
        pygame.display.flip()

def update_grid():
    pass

def draw_all_cells():
    for x in range(grid_size):
        for y in range(grid_size):
            if grid.is_cell_alive((x, y)):
                draw_cell((x,y), "white")
            else:
                draw_cell((x, y), "black")

def draw_grid():

    for offset in range(0, ((grid_size + 1) * cell_size), cell_size):
        pygame.draw.line(screen, "#1f1f1f", (margin + offset, margin), (margin + offset, (grid_size * cell_size) + margin)) # vertical
        pygame.draw.line(screen, "#1f1f1f", (margin, margin + offset), (margin + (grid_size * cell_size), margin + offset)) #horizontal
        
def draw_cell(pos: tuple, color):
    pygame.draw.rect(screen, color, (margin + pos[0] * cell_size,margin + pos[1] *cell_size,cell_size, cell_size))

def get_cell_from_position(pos):
    return ((pos[0] - margin)//cell_size, (pos[1] - margin)//cell_size)

    
main()
    