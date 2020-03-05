# Made by Artur Dorovskikh
# Version 0.2 2020-03-02
# This app is primarily for calibrating CRT monitors

# TODO make spacing with commas neater
# TODO add folders with done images at various rezolutions
# TODO merge all color line types with dots (in middle of square)

import sys
import pygame
import ctypes

pygame.init()
ctypes.windll.user32.SetProcessDPIAware() #disable windows scaling for this app
# TODO: make borderless fulscreen so leaving app does not minimize it for more than one monitor systems, for when running windas and connecting the crt on the same computer 

c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_red = (255, 0, 0)
c_green = (0, 255, 0)
c_blue = (0, 0, 255)

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
spacing = 40
width_spacing = round(width/spacing)
height_spacing = round(height/spacing)

line_color = c_white
back_color = c_black

pattern_number = 0  # for keeping track of the pattern for switching it

def draw(back_color, line_color):
    screen.fill(back_color)

    for x in range(round(width/spacing)):
        pygame.draw.line(screen,line_color,(x*spacing,0),(x*spacing,height))
    for y in range(round(height/spacing)):
        pygame.draw.line(screen,line_color,(0,y*spacing),(width,y*spacing))

    pygame.draw.line(screen,line_color,(width-1,0),(width-1,height))
    pygame.draw.line(screen,line_color,(0,height-1),(width,height-1))

    pygame.display.flip()

def draw_convergence(back_color):
    # TODO add also white, along with red, gree, blue
    # draw each color line part vertical induvidually, easier, rather than have the loop alternate colors, 






    x, y = 0, 0
    color_n = 0
    # color_n_repeat = 2
    count = 1
    while x < width:
        while y < height:
            if color_n == 0:
                line_color = c_red
            elif color_n == 1:
                line_color = c_green
            elif color_n == 2:
                line_color = c_blue

            if count != 3:
                color_n = (color_n + 1) % 3
                count += 1
            else:
                count = 1

            # if color_n == color_n_repeat:
            #     color_n_repeat = (color_n_repeat + 1) % 3
            # else:
            #     color_n = (color_n + 1) % 3

            # if color_n == 3:
            #     color_n = 2
            #     color_n_skip = True
            # else:
            #     color_n = 3
            #     color_n_skip = False

            pygame.draw.line(screen, line_color, (x, y), (x + spacing, y + spacing))
            y += spacing
        x += spacing

    # pygame.draw.line(screen,line_color,(width-1,0),(width-1,height))
    # pygame.draw.line(screen,line_color,(0,height-1),(width,height-1))
    pygame.display.flip()

def draw_dots():
    # draw dots
    for x in range(width_spacing+1):
        for y in range(height_spacing+1):
            pygame.draw.line(screen,c_white,(x*spacing, y*spacing),(x*spacing, y*spacing))
            
    for x in range(width_spacing+1):
        pygame.draw.line(screen,c_white,(x*spacing, height-1),(x*spacing, height-1))
    for y in range(height_spacing+1):
        pygame.draw.line(screen,c_white,(width-1, y*spacing),(width-1, y*spacing))
    pygame.draw.line(screen,c_white,(width-1, height-1),(width-1, height-1))
    pygame.display.flip()

def draw_lines_vertical(scale):
    # draw white black lines alternating 1 pixel vertically
    for x in range(round(width/scale)):
        pygame.draw.line(screen,c_white,(x*scale,0),(x*scale,height))
    pygame.display.flip()

def draw_lines_horizontal(scale):
    # draw white black lines alternating 1 pixel horizontally
    for y in range(round(height/scale)):
        pygame.draw.line(screen,c_white,(0,y*scale),(width,y*scale))
    pygame.display.flip()

def draw_grid_moving():
    # draw grid moving vertically down
    pygame.display.flip()

def draw_reference_pixel_image():
    # draw a reference pixel image to check if the pattern is resolved at a given resolution

    # draw the pattern several time on the screen
    for off_y in range(height_spacing):
        for off_x in range(width_spacing):
            # draw 3 groups of the 2 top horizontal lines
            # pattern_top_line_spacing = 6 # spacing for the top lines spacings
            spacing_x = 0
            spacing_y = 0
            pygame.draw.line(screen, c_white, (off_x + spacing_x, off_y + spacing_y), (off_x + spacing_x + 5, off_y + spacing_y))
            # TODO finish pixel reference image

    pygame.display.flip()

def draw_color_gradient():
    # draw a color gradient from across the screen horizontally
    # TODO function to draw color gradient across the screen
    return

def draw_motion_response():
    # test motion response of the display
    # TODO function to draw moving image/pattern to test motion clarity
    return

def draw_test_high_voltage():
    # test high voltage response for CRT monitors
    # TODO function to draw white rectangle slightly smaller than the screen with black background, toggling every second
    return

def draw_black_level():
    # TODO draws squares of different brightness to test black levels and black crush
    return

def draw_contrast():
    # TODO draws colors to test contrast
    return

def change_pattern(amount):  # change the patterns
    global pattern_number
    pattern_number = (pattern_number + amount) % 9
    screen.fill(c_black) # clear last pattern

    # TODO implement switch statement using dictionaries, also use the names for menu labeling to reduce redundancy
    # TODO briefly (5 seconds) show the title of the pattern and its short explanation in bottom right
    if pattern_number == 0:
        draw(c_black, c_white)
    if pattern_number == 1:
        draw(c_black, c_red)
    if pattern_number == 2:
        draw(c_black, c_green)
    if pattern_number == 3:
        draw(c_black, c_blue)
    if pattern_number == 4:
        draw(c_white, c_black)
    if pattern_number == 5:
        draw_convergence(c_black)
    if pattern_number == 6:
        draw_lines_vertical(2)
    if pattern_number == 7:
        draw_lines_horizontal(2)
    if pattern_number == 8:
        draw_dots()
    if pattern_number == 9:
        draw_reference_pixel_image()
    if pattern_number == 10:
        draw_black_level()
    if pattern_number == 11:
        draw_color_gradient()

def draw_menu():
    # TODO add a menu GUI to make navigation between patterns easier
    return

def main():
    draw(c_black, c_white)  # starter image white lines grid
    # TODO briefly (5 seconds) show the controls (left and right for switching patterns, esc to exit, up and down for size) bottom right

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    # TODO check if this is the correct way to exit pygame
                    return
                if event.key == pygame.K_LEFT:
                    change_pattern(-1)
                if event.key == pygame.K_RIGHT:
                    change_pattern(1)

main()
    