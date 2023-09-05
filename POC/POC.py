import pygame
import argparse
import cv2

def main():
    SIZE = 600
    surface = pygame.display.set_mode((SIZE,SIZE))
    running  = True
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, default="C:/Users/aulou/Desktop/Battle-Game/POC/Map_Uni.png",
	help="path to the input image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])

    while running:  
        color = (255, 0, 0)
 
# Changing surface color
        
        
  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                (b, g, r) = image[pos[1], pos[0]]
                print(b,g,r)
        # create a surface object, image is drawn on it.
        imp = pygame.image.load("C:\\Users\\aulou\\Desktop\\Battle-Game\\POC\\Map.png").convert()
 
# Using blit to copy content from one surface to other
        surface.blit(imp, (0, 0))
        pygame.display.flip()

main()