#Platform game with a twist
#
#I permanently borrowed a couple lines from various sources, but I labeled them all
#
#High School computer science project
#
#Released under the  GNU General Public License

import pygame as pg

pg.init()				#From pygame.org
screen = pg.display.set_mode((150, 50))	#From pygame.org, modified
done = False 				#From pygame.org
pg.display.set_caption('Goomba Adventure')

bkgrd = pg.Surface(screen.get_size())
bkgrd = bkgrd.convert()
bkgrd.fill((10, 15, 200))

clock = pg.time.Clock()

font = pg.font.SysFont(Arial, 12)

while not rip:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            rip = True

        print(event)

    pg.display.update()
    clock.tick(60)
    
def runLVL():
	

def gameStart:									
	print "Starting Game \n"
	print "Choose a level: 1 2 3 4 5 \n"
	raw_input()
	if raw_input() == 1:
		runLVL(1)
		levelChosen == 1
	if raw_input() == 2:
		runLVL(2)
		levelChosen == 2
	if raw_input() == 3:
		runLVL(3)
		levelChosen ==3
	if raw_input() == 4:
		runLVL(4)
		levelChosen == 4
	if raw_input() == 5:
		runLVL(5)
		levelChosen == 5
	else:
		print "Your only options are 1 through 5"
		gameStart
	print levelChosen
	
	
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
