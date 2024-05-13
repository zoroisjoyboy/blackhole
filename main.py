import pygame
import pygame.freetype
import time
import math
import grid
import blackhole

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
CELL_SIZE = 7
PADDING = 1

def generate_objects(screen, grid):
     for r in range(len(grid)):
            for c in range(len(grid[0])):
                x = c * (CELL_SIZE + PADDING) + PADDING
                y = r * (CELL_SIZE + PADDING) + PADDING  
                match grid[r][c]:
                    case 1:
                        myfont.render_to(screen, (x, y), chr(115), (255, 236, 236)) # color changes based off red shift or blue shift
                        if b.space_time_range(x, y): # if any coord is in space time enters, then copy once and recopy (removing prior copies) as the object moves closer to event horizon
                            # if before reaching event horizon, we change directions, particlar object and its copy moves away (removing prior copies) until object leaves space time curve which removes fully copy
                            # when reaching event horizon, original and copied flip, and as moving apart in space time range, both move apart until existing space time where copied is removed and original is now on the other side of the blackhole
                            opposite_x = -(math.floor(x - b.x) * 2) + x
                            opposite_y = -(math.floor(y - b.y) * 2) + y
                            myfont.render_to(screen, (opposite_x, opposite_y), chr(115), (255, 236, 236)) # copy others to mimic original and have them to warped and other side warped depending on angle from center 
                    case 2:
                        myfont.render_to(screen, (x, y), chr(103), (255, 236, 236))
                        if b.space_time_range(x, y):
                            opposite_x = -(math.floor(x - b.x) * 2) + x
                            opposite_y = -(math.floor(y - b.y) * 2) + y
                            myfont.render_to(screen, (opposite_x, opposite_y), chr(103), (255, 236, 236))

def move(keys):
    if keys[pygame.K_UP]:
            g.update(1)
    if keys[pygame.K_DOWN]:
        g.update(-1)
    if keys[pygame.K_LEFT]:
        g.update(2)
    if keys[pygame.K_RIGHT]:
        g.update(-2)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE) # fill screen, dynamic window implement
    myfont = pygame.freetype.Font(None, CELL_SIZE + PADDING)
    clock = pygame.time.Clock()
    total_cell_size = CELL_SIZE + PADDING
    pixel_rows = WINDOW_HEIGHT // total_cell_size
    pixel_cols = WINDOW_WIDTH // total_cell_size
    g = grid.Grid(pixel_rows, pixel_cols)
    b = blackhole.BlackHole(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 1/15)
    running = True

    g.populate()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        keys = pygame.key.get_pressed()
        move(keys)

        screen.fill("black")
        generate_objects(screen, g.grid)

        # if b.event_horizon_range(x, y):
        #     print("Coordinate ({}, {}) is within the event horizon range of the black hole.".format(x, y))  
                        
        # pygame.draw.circle(screen, "white", (b.x, b.y), b.curve)
        pygame.draw.circle(screen, "black", (b.x, b.y), b.radius)
                                                             
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

