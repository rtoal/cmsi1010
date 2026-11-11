import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SHAPE_WIDTH = 500
SHAPE_HEIGHT = 50
BORDER_THICKNESS = 10
SHAPE_FILL_COLOR = (255, 0, 200)
SHAPE_BORDER_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 192, 203)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle')


def draw_scene():
    screen.fill(BACKGROUND_COLOR)
    the_rectangle = (
        (SCREEN_WIDTH-SHAPE_WIDTH)/2,    # upper-left x
        (SCREEN_HEIGHT-SHAPE_HEIGHT)/2,  # upper-left y
        SHAPE_WIDTH,     # width
        SHAPE_HEIGHT     # height
    )
    pygame.draw.rect(screen, SHAPE_FILL_COLOR, the_rectangle)
    pygame.draw.rect(screen, SHAPE_BORDER_COLOR, the_rectangle,
                     BORDER_THICKNESS)
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
