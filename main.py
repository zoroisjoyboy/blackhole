import pygame
import pygame.freetype
import time
import grid
import blackhole

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
CELL_SIZE = 7
PADDING = 1

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
        
        if keys[pygame.K_UP]:
            g.update(1)
        if keys[pygame.K_DOWN]:
            g.update(-1)
        if keys[pygame.K_LEFT]:
            g.update(2)
        if keys[pygame.K_RIGHT]:
            g.update(-2)
    
        screen.fill("black")

        for r in range(len(g.grid)):
            for c in range(len(g.grid[0])):
                x = c * (CELL_SIZE + PADDING) + PADDING
                y = r * (CELL_SIZE + PADDING) + PADDING     
                match g.grid[r][c]:
                    case 1:
                        myfont.render_to(screen, (x, y), chr(115), (255, 236, 236)) # color changes based off red shift or blue shift
                    case 2:
                        myfont.render_to(screen, (x, y), chr(103), (255, 236, 236))
                        
        pygame.draw.circle(screen, "black", (b.x, b.y), b.radius)
                                                                                           
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

