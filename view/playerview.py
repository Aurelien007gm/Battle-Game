import pygame
import argparse
import cv2

import sys
 
# setting path
sys.path.append('c:\\Users\\aulou\\Desktop\\Battle-Game')
print(sys.path)

from action import Action, ActionHandler
from actionmanager import ActionManager


def main():
    pygame.init()
    colorToAct = {}
    for i in range(16):
        colorToAct[(0,0,100+10*i)] = i
    colorToAct[(0,25,0)] = "Validate"
    colorToAct[(0,50,0)] = "Deploy"
    colorToAct[(0,75,0)] = "Transfer"
    colorToAct[(0,100,0)] = "DiscardCard"
    colorToAct[(0,125,0)] = "Attack"
    colorToAct[(0,150,0)] = "Para"
    colorToAct[(0,175,0)] = "Navy"
    colorToAct[(0,200,0)] = "Field"
    colorToAct[(0,225,0)] = "Run"

    colorToAct[(255,0,0)] = "Player1"
    colorToAct[(0,255,0)] = "Player2"
    colorToAct[(0,0,255)] = "Player3"
    colorToAct[(0,255,255)] = "Player4"
    colorToAct[(100,0,0)] = "Effect"
    actHandler = ActionHandler()
    am = ActionManager()
    am.print()


    SIZE = 600
    surface = pygame.display.set_mode((SIZE,SIZE))
    running  = True
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, default="C:/Users/aulou/Desktop/Battle-Game/view/Map_Uni.png",
	help="path to the input image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])
    effect = False

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
                command = colorToAct.get((b,g,r))
                print(command)
                act = None
                if(not command is None):
                    if(command == "Run"):
                        am.Run()
                        am.print()
                    elif(command == "Effect"):
                        effect = True
                    elif(isinstance(command,int) and effect):
                        effect = False
                        am.cm.tm.territories[command].ShowEffect()

                    else:
                        act = actHandler.Add(command)
                if(act):
                    am.Call(act)
                    act.print()
                    act = None
        # create a surface object, image is drawn on it.
        imp = pygame.image.load("C:\\Users\\aulou\\Desktop\\Battle-Game\\view\\Map.png").convert()
 
# Using blit to copy content from one surface to other
        surface.blit(imp, (0, 0))

        #Displaying all the number and the associated player
        coordFromTerr = {}

        coordFromTerr[0] = [34,340]
        coordFromTerr[1] = [35,453]
        coordFromTerr[2] = [151,421]
        coordFromTerr[3] = [241,329]
        coordFromTerr[4] = [244,460]
        coordFromTerr[5] = [336,332]
        coordFromTerr[6] = [359,492]
        coordFromTerr[7] = [419,328]
        coordFromTerr[8] = [414,226]
        coordFromTerr[9] = [511,223]
        coordFromTerr[10] = [527,116]
        coordFromTerr[11] = [437,121]
        coordFromTerr[12] = [237,187]
        coordFromTerr[13] = [134,187]
        coordFromTerr[14] = [111,102]
        coordFromTerr[15] = [219,103]
        player = am.players

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(actHandler.field), 1, (0,0,0))
        surface.blit(score_surf, [173,572])

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(actHandler.navy), 1, (0,0,0))
        surface.blit(score_surf, [204,572])
        
        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(actHandler.para), 1, (0,0,0))
        surface.blit(score_surf, [229,572])

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(player[0].money), 1, (0,0,0))
        surface.blit(score_surf, [280,547])

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(player[1].money), 1, (0,0,0))
        surface.blit(score_surf, [327,547])

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(player[2].money), 1, (0,0,0))
        surface.blit(score_surf, [370,547])

        score_font = pygame.font.Font(None, 20)
        score_surf = score_font.render(str(player[3].money), 1, (0,0,0))
        surface.blit(score_surf, [420,547])
        
        for territory in am.cm.tm.territories:
            id = territory.id
            troop = territory.troop
            pos = coordFromTerr.get(id) or [0,0]
            col = territory.owner.color

            score_font = pygame.font.Font(None, 20)
            score_surf = score_font.render(str(troop["field"]), 1, col)
            surface.blit(score_surf, [pos[0],pos[1]])

            score_font = pygame.font.Font(None, 20)
            score_surf = score_font.render(str(troop["navy"]), 1, col)
            surface.blit(score_surf, [pos[0]+10,pos[1]])

            score_font = pygame.font.Font(None, 20)
            score_surf = score_font.render(str(troop["para"]), 1, col)
            surface.blit(score_surf, [pos[0]+20,pos[1]])

            score_font = pygame.font.Font(None, 20)
            score_surf = score_font.render(str(troop["animals"]), 1, col)
            surface.blit(score_surf, [pos[0]+35,pos[1]])


        pygame.display.flip()

main()