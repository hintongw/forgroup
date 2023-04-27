#Name:Team Jared Butler                                                   #
#email: halverhc@mail.uc.edu, hintongw@mail.uc.edu,Stewasu@mail.Uc.edu    #                                          #
#Assignment Title: Final Assignment                                       #
#Course: IS 4010                                                          #
#Semester/Year: Spring 2023                                               #
#Brief Description: Gets the image for the main                           #
#                                                                         #
#Anything else that's relevant: no                                        #
#Citations:  GPT3                                                         #
###########################################################################

import pygame
def display_photo(scale=1):
    image = pygame.image.load('IMG_4898.jpg')
    scaled_image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    return scaled_image