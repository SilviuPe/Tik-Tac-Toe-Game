import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text with Stroke Example")

# Set colors
text_color = (255, 255, 255)  # White text color
stroke_color = (0, 5, 0)      # Black stroke color

# Set font and size
font = pygame.font.Font(None, 36)

# Create a surface with the text
text_surface = font.render("Hello, Pygame!", True, text_color)
text_surface_stroke = font.render("Hello, Pygame!", True, stroke_color)
# Get the rectangle of the text surface
text_rect = text_surface.get_rect(center=(width // 2, height // 2))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background (optional)
    screen.fill((255,255,255))  # White background

    # Render the text with a stroke
    for offset in range(1, 5):  # Adjust the range to change the thickness of the stroke
        text_rect.x = width // 2 - text_surface.get_width() // 2 + offset
        text_rect.y = height // 2 - text_surface.get_height() // 2 + offset
        screen.blit(text_surface_stroke, text_rect)

    # Render the text without a stroke in the center
    text_rect.x = width // 2 - text_surface.get_width() // 2
    text_rect.y = height // 2 - text_surface.get_height() // 2
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()