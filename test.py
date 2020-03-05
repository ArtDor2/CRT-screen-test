# Made by Artur Dorovskikh
# CRT-screen-test v0.2 2020-03-02
# This app is primarily for calibrating CRT computer monitors

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
width_half = width/2
height_half = height/2

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

def draw_with_dots(line_color):
    for x in range(round(width/spacing)):
        pygame.draw.line(screen, line_color, (x*spacing, 0), (x*spacing, height))
    for y in range(round(height/spacing)):
        pygame.draw.line(screen, line_color, (0, y*spacing), (width, y*spacing))

    pygame.draw.line(screen, line_color, (width-1, 0), (width-1, height))
    pygame.draw.line(screen, line_color, (0, height-1), (width, height-1))

    # draw the dots in the middle of the squares
    for x in range(round(width/spacing)):
        for y in range(round(height/spacing)):
            x1 = x*spacing + spacing/2
            y1 = y*spacing + spacing/2
            pygame.draw.line(screen, line_color, (x1, y1), (x1, y1))

    pygame.display.flip()

def draw_convergence(back_color):
    # TODO add also white, along with red, gree, blue
    # draw each color line part vertical induvidually, easier, rather than have the loop alternate colors, 

    # vertical lines
    color = 0 # 0 = red, 1 = green, 2 = blue, 3 = repeat last color
    color_repeat = 1
    edge = 0
    edge_y = round(height/spacing) # TODO adding +1 to both for loops fixes adjes rightmost and bottommost displaying, but the pattern shifts
    for y in range(round(width/spacing)):
        for x in range(round(width/spacing)):
            if color == 0:
                color_draw = c_red
            elif color == 1:
                color_draw = c_green
            elif color == 2:
                color_draw = c_blue

            if x == edge_y:
                edge = 1
            pygame.draw.line(screen, color_draw, (x*spacing - edge, y*spacing - spacing/2), (x*spacing - edge, y*spacing + spacing/2))
            
            if color_repeat == 3:
                color_repeat = 1
            else:
                color = (color + 1) % 3
                color_repeat += 1

    # horizontal lines
    color = 0 # 0 = red, 1 = green, 2 = blue, 3 = repeat last color
    color_repeat = 1
    edge = 0
    edge_x = round(width/spacing)
    for y in range(round(width/spacing)):
        for x in range(round(width/spacing)):
            if color == 0:
                color_draw = c_red
            elif color == 1:
                color_draw = c_green
            elif color == 2:
                color_draw = c_blue

            if x == edge_x:
                edge = 1
            pygame.draw.line(screen, color_draw, (x*spacing - spacing/2, y*spacing - edge), (x*spacing + spacing/2, y*spacing -edge))
            
            if color_repeat == 3:
                color_repeat = 1
            else:
                color = (color + 1) % 3
                color_repeat += 1

    pygame.display.flip()

def draw_dots():
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
    # draw a rectangle r red is left add, g green is right add, b blue is down add
    for r in range(256):
        for g in range(256):
            for b in range(1):
                # x1 = width_half-r
                # y1 = height_half-g
                # pygame.draw.line(screen, (r, g, b), (x1, y1), (x1, y1))
                x1 = r
                y1 = g
                pygame.draw.line(screen, (r, g, b), (x1, y1), (x1, y1))
    # for x in width:
    #     for y in height:
    #         surface.fill((r, g, b), ())
    

    pygame.display.flip()

def draw_motion_response():
    # test motion response of the display
    # TODO function to draw moving image/pattern to test motion clarity
    pygame.display.flip()

def draw_test_high_voltage():
    # test high voltage response for CRT monitors
    # TODO function to draw white rectangle slightly smaller than the screen with black background, toggling every second
    pygame.display.flip()

def draw_black_level():
    # TODO draws squares of different brightness to test black levels and black crush
    brightness = 1
    scale = 100
    # TODO center the rectangles
    for x in range(5):
        for y in range(3):
            pygame.draw.rect(screen, (brightness, brightness, brightness), (scale*(x-1), scale*(y-1), scale*x, scale*y))
            brightness += 1
    pygame.display.flip()

def draw_contrast():
    # TODO draws colors to test contrast
    pygame.display.flip()

def change_pattern(amount):  # change the patterns
    global pattern_number
    pattern_number = (pattern_number + amount) % 12
    screen.fill(c_black) # clear last pattern

    # TODO implement switch statement using dictionaries, also use the names for menu labeling to reduce redundancy
    # TODO briefly (5 seconds) show the title of the pattern and its short explanation in bottom right
    if pattern_number == 0:
        draw_with_dots(c_white)
    if pattern_number == 1:
        draw_with_dots(c_red)
    if pattern_number == 2:
        draw_with_dots(c_green)
    if pattern_number == 3:
        draw_with_dots(c_blue)
    if pattern_number == 4:
        screen.fill(c_white)
        draw_with_dots(c_black)
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
    change_pattern(0)  # starter image white lines grid
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
    
