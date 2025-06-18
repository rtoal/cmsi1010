import pygame

# Always begin with initialization, sizing, and captioning
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Just a Simple Rectangle')

# Not strictly necessary, but good practice for readability
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# A best practice is to do the drawing in its own function
# A good draw function ususally does three things:
# 1. Clear the screen
# 2. Draw the shapes
# 3. Update the display
def draw_scene():
    screen.fill(WHITE)  # "Clear the screen"
    the_rectangle = (300, 225, 200, 150)  # (x, y, width, height)
    pygame.draw.rect(screen, RED, the_rectangle)  # filled
    pygame.draw.rect(screen, BLACK, the_rectangle, 5)  # outlined
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene
draw_scene()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

