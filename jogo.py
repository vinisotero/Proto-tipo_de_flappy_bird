import pygame


press = False
gravity = 30
running = True
background_color = (135, 206, 235)
color = (0,255,0)
ground = (0,255,0)
width_square = 60
height_square = 60
width_ground = 640
height_ground = 60
width_screen = 640
height_screen = 480
left_square = 30
left_ground = 0
top_ground = 420
surface = pygame.display.set_mode((width_screen, height_screen))


def push_down(gravity):
    gravity += 0.4
    return gravity


def jump_verif(press, gravity, color, surface):

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == 769 or 770 or 768 or 771:
                return True

    return False

def run(press, gravity, running, color ,ground, width_square, height_square, width_ground, height_ground, left_square, left_ground, top_ground, surface):

    while running:
        pygame.init()
        surface.fill(background_color)
        pygame.draw.rect(surface, color, pygame.Rect(left_square, gravity, width_square, height_square))
        pygame.draw.rect(surface, ground, pygame.Rect(left_ground, top_ground, width_ground, height_ground))
        gravity = push_down(gravity)
        press = jump_verif(press, gravity, color, surface)
        if press == True:

            press = False
            for i in range(60):

                gravity -= 2
                pygame.init()
                surface.fill(background_color)
                pygame.draw.rect(surface, ground, pygame.Rect(left_ground, top_ground, width_ground, height_ground))
                pygame.draw.rect(surface, color, pygame.Rect(left_square, gravity, width_square, height_square))
                pygame.display.flip()

        pygame.display.flip()

run(press, gravity, running, color ,ground, width_square, height_square, width_ground, height_ground, left_square, left_ground, top_ground, surface)