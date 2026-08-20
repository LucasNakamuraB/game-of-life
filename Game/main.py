import pygame
from grid import *

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont("monospace", 25)

margin: int = 50

grid_size = 50
cell_size = 10

left_side = (margin * 2) + (grid_size * cell_size)
grid: CellGrid = CellGrid(grid_size)

def main():
    pygame.display.set_caption("Conway's Game of Life")
    run = True
    delay = 5
    paused = True
    ticks = 0
    draw_title()
    draw_instructions()
    killmode = False
    mb_down = False
    pygame.draw.line(screen, "white", (left_side, margin/2), (left_side, left_side - margin/2))
    draw_tickrate(delay)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    grid.update_all()
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_x:
                    grid.genocide()
                elif event.key == pygame.K_DOWN and delay > 1:
                    delay -= 1
                    draw_tickrate(delay)
                elif event.key == pygame.K_UP:
                    delay += 1
                    draw_tickrate(delay)
                elif event.key == pygame.K_r:
                    grid.generate_soup()
        if pygame.mouse.get_pressed()[0]:
            grid.revive_cell(get_cell_from_position(pygame.mouse.get_pos()))
        elif pygame.mouse.get_pressed()[2]:
            grid.kill_cell(get_cell_from_position(pygame.mouse.get_pos()))
        draw_all_cells()
        draw_grid()
        draw_paused(paused)
        
        #print(get_cell_from_position(pygame.mouse.get_pos()))
        #print(grid.is_cell_alive(get_cell_from_position(pygame.mouse.get_pos())))
        #print(grid.get_cell_neighbor_count(get_cell_from_position(pygame.mouse.get_pos())))
        clock.tick(60)
        #if paused:
        #    pygame.draw.rect(screen, "red", (0,0,50, 50))
        #else:
        #    pygame.draw.rect(screen, "green", (0,0,50, 50))
        ticks += 1
        if ticks >= delay and not paused:
            ticks = 0
            grid.update_all()
            draw_all_cells()
            draw_grid()
            pygame.display.flip()
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

def draw_paused(paused: bool):
    pygame.draw.rect(screen, "black", (margin + left_side,margin, left_side + margin, margin))
    if paused:
        paused = font.render("PAUSED", False, "white")
    else:
        paused = font.render("RUNNING", False, "white")
        
    screen.blit(paused, (margin + left_side,margin)) 

def draw_tickrate(delay: int):
    pygame.draw.rect(screen, "black", (margin + left_side,margin * 2, left_side + margin, margin))
    num = "TICK DELAY(60fps): " + str(delay)
    rate = font.render(num, False, "white")
    screen.blit(rate, (margin + left_side, margin * 2))

def draw_title():
    title = font.render("CONWAY'S GAME OF LIFE", False, "white")
    screen.blit(title, (margin,12))

def draw_instructions():
    inst = font.render("kill/revive cells:[RMB]/[LMB]\npause/unpause:[SPACE]\
        \nchange ticks:[UP]/[DOWN]\nforce update:[Q]\nmake soup:[R]\nclear:[X]", False, "#494949")
    screen.blit(inst,(margin + left_side, margin * 7))
    
    
main()
    