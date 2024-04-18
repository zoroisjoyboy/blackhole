import pygame
import pygame.freetype
import time
import grid

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
CELL_SIZE = 3
PADDING = 1

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # maybe have a map bigger than what is represented? 
    myfont = pygame.freetype.Font(None, CELL_SIZE + PADDING)
    clock = pygame.time.Clock()
    total_cell_size = CELL_SIZE + PADDING
    pixel_rows = WINDOW_HEIGHT // total_cell_size
    pixel_cols = WINDOW_WIDTH // total_cell_size
    center_sqr_x = WINDOW_WIDTH // 2
    center_sqr_y = WINDOW_HEIGHT // 2
    g = grid.Grid(pixel_rows, pixel_cols)
    running = True

    g.populate()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            center_sqr_y -= 1
        if keys[pygame.K_DOWN]:
            center_sqr_y += 1
        if keys[pygame.K_LEFT]:
            center_sqr_x -= 1
        if keys[pygame.K_RIGHT]:
            center_sqr_x += 1
    
        screen.fill("black")

        pygame.draw.rect(screen, (255, 255, 255), (center_sqr_x, center_sqr_y, CELL_SIZE + PADDING * 2, CELL_SIZE + PADDING * 2))

        for r in range(len(g.grid)):
            for c in range(len(g.grid[0])):
                x = c * (CELL_SIZE + PADDING) + PADDING
                y = r * (CELL_SIZE + PADDING) + PADDING     
                match g.grid[r][c]:
                    case 1:
                        myfont.render_to(screen, (x, y), g.random_ascii(), (255, 255, 255)) # maybe slow down the tickle        
                                                                                           
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

