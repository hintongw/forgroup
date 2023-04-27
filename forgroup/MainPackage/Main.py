#Name:Team Jared Butler                                                   #
#email: halverhc@mail.uc.edu, hintongw@mail.uc.edu,Stewasu@mail.Uc.edu    #                                          #
#Assignment Title: Final Assignment                                       #
#Course: IS 4010                                                          #
#Semester/Year: Spring 2023                                               #
#Brief Description: Decoding encryptions with JSON                        #
#                                                                         #
#Anything else that's relevant: no                                        #
#Citations:  GPT3                                                         #
###########################################################################
import pygame
from Decryption import *
from Photo import *
from BadDecrypt import *
import json


# Set up the menu options
menu_options = ["Correct Decryption", "First Attempt", "Photo", "Quit"]

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Team Jared Butler")

# Set up the fonts
menu_font = pygame.font.Font(None, 40)
output_font = pygame.font.Font(None, 30)

# Set up the circle colors and positions
circle_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
circle_positions = [(200, 150), (600, 150), (200, 450), (600, 450)]

# Function to handle the menu selection
def handle_menu_selection(selection):
    if selection == 1:
        output_text = decrypt_location()
    elif selection == 2:
        output_text = BADdecrypt_location()
    elif selection == 3:
        output_photo = display_photo(scale=0.2)
        screen.blit(output_photo, (0, 0))  # blit the photo onto the screen
        pygame.display.update()
        pygame.time.delay(3000)  # Wait for 3 seconds before returning to the menu
        return
    elif selection == 4:
        pygame.quit()
        quit()
    else:
        output_text = "Invalid selection"
        
    # Display the output text on the screen
    screen.fill((255, 255, 255))
    text_surface = output_font.render(output_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(400, 300))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(9000)  # Wait for 3 seconds before returning to the menu



# Main game loop
def main():
    # Draw the title above the circles
    title_font = pygame.font.Font(None, 50)
    title_text = title_font.render("Team Jared Butler", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(400, 50))
    screen.blit(title_text, title_rect)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(circle_positions)):
                    if ((mouse_pos[0] - circle_positions[i][0]) ** 2 +
                            (mouse_pos[1] - circle_positions[i][1]) ** 2) <= 50 ** 2:
                        handle_menu_selection(i + 1)

        # Draw the circles and text on the screen
        screen.fill((255, 255, 255))
        screen.blit(title_text, title_rect)  # Draw the title again to avoid erasing it
        for i in range(len(circle_positions)):
            pygame.draw.circle(screen, circle_colors[i], circle_positions[i], 90)
            text = menu_font.render(str(i + 1) + ". " + menu_options[i], True, (0, 0, 0))
            text_rect = text.get_rect(center=circle_positions[i])
            screen.blit(text, text_rect)

        # Update the display
        pygame.display.update()


if __name__ == '__main__':
    main()