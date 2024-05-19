import pygame, pygame.freetype
import os, sys
import cv2
import grid, blackhole
from button import Button
from slider import Slider

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.mixer.init()

INFO = pygame.display.Info()
WIDTH, HEIGHT = INFO.current_w, INFO.current_h
WINDOWED_WIDTH, WINDOWED_HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WINDOWED_WIDTH, WINDOWED_HEIGHT)) 
MASS = 1/15
CELL_SIZE = 7
PADDING = 1

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.display.set_caption("Warphole")
icon_path = resource_path("assets\\icon.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
shapes_path = resource_path("assets\\shapes\\rect.png")

def get_font(size):
    font_path = resource_path("assets\\fonts\\MinecraftBold-nMK1.otf")
    return pygame.font.Font(font_path, size)

def adjust_font_size(font_size, font_rev):
    if font_size == 150 or font_rev:
        font_size -= 1
        font_rev = True
        if font_size == 90:
            font_rev = False
    else:
        font_size += 1
    return font_size, font_rev

def play():
    def generate_objects(screen, grid):
        for r in range(len(grid)):
                for c in range(len(grid[0])):
                    x = c * (CELL_SIZE + PADDING) + PADDING
                    y = r * (CELL_SIZE + PADDING) + PADDING  
                    match grid[r][c]:
                        case 1:
                            myfont.render_to(screen, (x, y), chr(115), (255, 236, 236)) 
                            if b.space_time_range(x, y): 
                                copied_x, copied_y = b.copied_object(x, y)
                                myfont.render_to(screen, (copied_x, copied_y), chr(115), (255, 236, 236))
                                rev_copied_x, rev_copied_y = b.copied_object(copied_x, copied_y)
                                myfont.render_to(screen, (rev_copied_x, rev_copied_y), chr(115), (255, 236, 236))

                        case 2:
                            myfont.render_to(screen, (x, y), chr(103), (255, 236, 236))
                            if b.space_time_range(x, y):
                                copied_x, copied_y = b.copied_object(x, y)
                                myfont.render_to(screen, (copied_x, copied_y), chr(103), (255, 236, 236))
                                rev_copied_x, rev_copied_y = b.copied_object(copied_x, copied_y)
                                myfont.render_to(screen, (rev_copied_x, rev_copied_y), chr(103), (255, 236, 236))

    def move(keys):
        if keys[pygame.K_UP]:
                g.update(1)
        if keys[pygame.K_DOWN]:
            g.update(-1)
        if keys[pygame.K_LEFT]:
            g.update(2)
        if keys[pygame.K_RIGHT]:
            g.update(-2)
    
    def toggle_fullscreen():
        nonlocal fullscreen
        if fullscreen:
            b.x, b.y = WINDOWED_WIDTH // 2, WINDOWED_HEIGHT // 2
            pygame.display.set_mode((WINDOWED_WIDTH, WINDOWED_HEIGHT))
        else:
            b.x, b.y = WIDTH // 2, HEIGHT // 2
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fullscreen = not fullscreen

    myfont = pygame.freetype.Font(None, CELL_SIZE + PADDING)
    clock = pygame.time.Clock()
    total_cell_size = CELL_SIZE + PADDING
    pixel_rows = HEIGHT // total_cell_size
    pixel_cols = WIDTH // total_cell_size
    g = grid.Grid(pixel_rows, pixel_cols)
    b = blackhole.BlackHole(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT // 2, MASS)
    fullscreen = False
    running = True

    g.populate()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()
                running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                toggle_fullscreen()

        keys = pygame.key.get_pressed()
        move(keys)

        SCREEN.fill("black")
        generate_objects(SCREEN, g.grid)

        pygame.draw.circle(SCREEN, "black", (b.x, b.y), b.radius)
                                                             
        pygame.display.flip()
        clock.tick(60)

        pygame.display.update()
    
    pygame.quit()

def main_menu():    
    video_path = resource_path("assets\\menu_clip.mp4") 
    video = cv2.VideoCapture(video_path)
    music_path = resource_path("assets\\music\\invincible_theme_8bit.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    clock = pygame.time.Clock()
    font_size = 90
    font_rev = False
    font = get_font(90)
    run = success

    while run: 
        clock.tick(fps)
        SCREEN.fill("black")
        menu_mouse_pos = pygame.mouse.get_pos()

        success, video_image = video.read()
        if not success:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, video_image = video.read()

        if success:
            video_image = cv2.resize(video_image, (WINDOWED_WIDTH, WINDOWED_HEIGHT))
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
            SCREEN.blit(video_surf, (0, 0))

            title_surf = font.render('Warphole', True, (255, 255, 255))
            title_rect = title_surf.get_rect(center=(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT // 5))
            SCREEN.blit(title_surf, title_rect)

            play_button = Button(image=pygame.image.load(shapes_path), pos=(WINDOWED_WIDTH // 2, 700), 
                            text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            options_button = Button(image=pygame.image.load(shapes_path), pos=(WINDOWED_WIDTH // 2, 800), 
                                text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=pygame.image.load(shapes_path), pos=(WINDOWED_WIDTH // 2, 900), 
                                text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(SCREEN)

            font_size, font_rev = adjust_font_size(font_size, font_rev)
            font = get_font(font_size)
                
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        pygame.mixer.music.stop()
                        play()
                        run = False
                    if options_button.checkForInput(menu_mouse_pos):
                        options()
                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
        
    pygame.quit()
    sys.exit()

def exit():
    SCREEN = pygame.display.set_mode((WINDOWED_WIDTH, WINDOWED_HEIGHT)) 
    while True:
        SCREEN.fill("black")
        font = get_font(90)

        menu_mouse_pos = pygame.mouse.get_pos()
        title_surf = font.render('Leave?', True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT // 5))
        SCREEN.blit(title_surf, title_rect)

        main_menu_button = Button(image=pygame.image.load(shapes_path), pos=(WINDOWED_WIDTH // 2, 700), 
                            text_input="Return to Menu", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        
        for button in [main_menu_button]:
                button.changeColor(menu_mouse_pos)
                button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(menu_mouse_pos):
                    main_menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                play()
        
        pygame.display.update()

def options():
    global MASS
    b = blackhole.BlackHole(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT * 0.65, MASS)
    slider = Slider(WINDOWED_WIDTH // 2 - 150, WINDOWED_HEIGHT // 2.5, 300, 40, 30, 10, 20)
    clock = pygame.time.Clock()
    font_rev = False
    font_size = 90
    font = get_font(font_size)
    while True:
        SCREEN.fill("black")
        clock.tick(30)
        menu_mouse_pos = pygame.mouse.get_pos()
        title_surf = font.render('Warphole Settings', True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT // 5))
        SCREEN.blit(title_surf, title_rect)

        font_size, font_rev = adjust_font_size(font_size, font_rev)
        font = get_font(font_size)

        slider.draw(SCREEN)
        new_mass = slider.get_value()
        b = blackhole.BlackHole(WINDOWED_WIDTH // 2, WINDOWED_HEIGHT * 0.65, 1/new_mass)

        pygame.draw.circle(SCREEN, "White", (b.x, b.y), b.curve)
        pygame.draw.circle(SCREEN, "black", (b.x, b.y), b.radius)

        save_button = Button(image=pygame.image.load(shapes_path), pos=(WINDOWED_WIDTH // 2, 900), 
                            text_input="Save", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        for button in [save_button]:
                button.changeColor(menu_mouse_pos)
                button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if save_button.checkForInput(menu_mouse_pos):
                    MASS = 1/new_mass
                    main_menu()
            slider.handle_event(event)
        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    


