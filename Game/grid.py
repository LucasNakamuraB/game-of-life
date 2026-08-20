class Cell:
    pos: tuple
    alive: bool
    next_state: bool
    def __init__(self, pos: tuple):
            self.pos = pos
            self.alive = False
            self.next_state = True
    def update(self):
        self.alive = self.next_state
    
    def flip(self):
        self.alive = not self.alive
    
    def kill(self):
        self. alive = False
    
    def revive(self):
        self.alive = True

class CellGrid:
    grid_matrix: list[list[Cell]]
    size: int
    
    def __init__(self, size: int):
        self.size = size
        self.grid_matrix = []
        for x in range(self.size):
            collumn = []
            for y in range(self.size):
                collumn.append(Cell((x, y)))
            self.grid_matrix.append(collumn)
            
    def update_all(self):
        for x in range(self.size):
                for y in range(self.size):
                    n_neighbors = self.get_cell_neighbor_count((x, y))
                    cell = self.get_cell((x, y))
                    if n_neighbors < 2 and cell.alive:
                        cell.next_state = False
                    elif cell.alive and (n_neighbors == 2 or n_neighbors == 3):
                        cell.next_state = True
                    elif not cell.alive and n_neighbors == 3:
                        cell.next_state = True
                    elif cell.alive and n_neighbors > 3:
                        cell.next_state = False
                    else:
                        cell.next_state = False
        for x in range(self.size):
            for y in range(self.size):
                self.get_cell((x, y)).update()
    
    def genocide(self):
        for x in range(self.size):
            for y in range(self.size):
                self.get_cell((x, y)).kill()
                
        
    
    def get_cell(self, pos: tuple) -> Cell:
        return self.grid_matrix[pos[0]][pos[1]]
    
    def is_cell_alive(self, posit: tuple):
        pos = (posit[0]% self.size, posit[1]%self.size)
        if (pos[0] < 0) or (pos[1] < 0) or (pos[0] >= self.size) or (pos[1] >= self.size):
            return False
        else:
            return self.grid_matrix[pos[0]][pos[1]].alive
    
    def flip_cell(self, pos:tuple):
        if (pos[0] < 0) or (pos[1] < 0) or (pos[0] >= self.size) or (pos[1] >= self.size):
            return
        self.grid_matrix[pos[0]][pos[1]].flip()
        
    def kill_cell(self, pos:tuple):
        if (pos[0] < 0) or (pos[1] < 0) or (pos[0] >= self.size) or (pos[1] >= self.size):
            return
        self.grid_matrix[pos[0]][pos[1]].kill()
    def revive_cell(self, pos:tuple):
        if (pos[0] < 0) or (pos[1] < 0) or (pos[0] >= self.size) or (pos[1] >= self.size):
            return
        self.grid_matrix[pos[0]][pos[1]].revive()
    
    def get_cell_neighbor_count(self, pos: tuple) -> int:
        neighbors = 0
        for x in range(3):
            for y in range(3):
                if self.is_cell_alive((pos[0] + x - 1, pos[1] + y - 1)) and (pos[0] + x - 1, pos[1] + y - 1) != pos:
                    neighbors += 1
        return neighbors
