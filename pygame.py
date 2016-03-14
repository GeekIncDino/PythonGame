#Platform game with a twist
#I stole a couple lines from pygame.org, but I labeled them all
#
#Released under the  GNU General Public License

import pygame as pg

pg.init()				#From pygame.org
screen = pg.display.set_mode((150, 50))	#From pygame.org, modified
done = False 				#From pygame.org

bkgrd = pg.Surface(screen.get_size())
bkgrd = bkgrd.convert()
bkgrd.fill((10, 15, 200))

font = pg.font.SysFont(Arial, 12)

def checkGood:
	pg.key.get.pressed()
	if 
def runLVL1:

def runLVL2:
	
def runLVL3:

def runLVL4:
	
def runLVL5:


def gameStart:									
	print "Starting Game %n"
	print "Choose a level: 1 2 3 4 5 %n"
	raw_input()
	if raw_input() == 1:
		runLVL1
	if raw_input() == 2:
		runLVL3
	if raw_input() == 3:
		runLVL3
	if raw_input() == 4:
		runLVL4
	if raw_input() == 5:
		runLVL5
	else:
		print "Your only options are 1 through 5"
		gameStart

if event.type == pg.KEYDOWN and event.key == pg.K_ENTER:
	gameStart

if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
        moveleft
        
if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
        moveright
        
if event.type == pg.KEYDOWN and event.key == pg.K_UP:
        moveup
        
if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
	movedown
