import pygame

pygame.init()

screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

cell_size = 20
nofcellsinrow = screen_width // cell_size
nofcellsincol = screen_height // cell_size

grid = [[0]*nofcellsinrow for i in range(nofcellsincol)]


def neighbour_counter(grid,row,col):
    count = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            if (i == 0 and j == 0) or (row == 0 and i == -1) or (row == nofcellsincol-1 and i == 1) or (col == 0 and j == -1) or (col == nofcellsinrow-1 and j == 1):
                continue
            else:
                if grid[row+i][col+j] == 1:
                    count += 1
    return count

def next_gen(grid):
    new_grid = [[0]*nofcellsinrow for i in range(nofcellsincol)]
    for row in range(nofcellsincol):
        for col in range(nofcellsinrow):
            if grid[row][col] == 1:
                if neighbour_counter(grid,row,col) == 3 or  neighbour_counter(grid,row,col) == 2:
                    new_grid[row][col] = 1
                else:
                    continue
            else:
                if neighbour_counter(grid,row,col) == 3:
                    new_grid[row][col] = 1 
    return new_grid

speed = 5
playing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    playing = False
                else:
                    playing = True
            elif event.key == pygame.K_UP:
                speed += 1
                print(speed) 
            elif event.key == pygame.K_DOWN:
                if speed > 1:
                    speed -= 1
                    print(speed)
                else:
                    print("speed Can't be equal to zero")
            elif event.key == pygame.K_0:
                speed = 1
            elif event.key == pygame.K_1:
                speed = 60
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_m,y_m = event.pos
            col = x_m //cell_size
            row = y_m // cell_size
            grid[row][col] = 1 - grid[row][col]
        
    if playing:
        grid = next_gen(grid)
    screen.fill((70, 80, 110))

    for row in range(nofcellsincol):
        for col in range(nofcellsinrow):
            if grid[row][col] == 1:
                pygame.draw.rect(screen,(80, 250, 123),(col*cell_size,row*cell_size,cell_size-1,cell_size-1))
            else:
                pygame.draw.rect(screen,(30, 36, 54),(col*cell_size,row*cell_size,cell_size-1,cell_size-1))
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()