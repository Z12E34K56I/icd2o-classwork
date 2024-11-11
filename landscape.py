import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

sun_radius = 40
sun_x = WIDTH // 3.5
sun_y = HEIGHT // 1.4 
mountain_top = HEIGHT // 2 


background_color = [0, 0, 255]

clock = pygame.time.Clock()



running = True
sun_direction = 1 
sun_speed = -1


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
    background_color[0]= min(220, background_color[0]+1)
    background_color[1] = min(165, background_color[1] + 1)
    background_color[2] = max(0, background_color[2] - 1)

    sun_y += sun_speed
    
    screen.fill(background_color)

    
    pygame.draw.polygon(screen, (50, 50, 50), [(0, HEIGHT), (WIDTH // 2, mountain_top), (WIDTH, HEIGHT)])

    
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)

    
    
        


    pygame.display.flip()

    clock.tick(30)
