#Platform game with a twist
#
#I permanently borrowed a couple lines from various sources, but I labeled them all
#
#High School computer science project
#
#Released under the  GNU General Public License

import sys
import os
import pygame as pg

rip = True
xa = 50
ya = 30
pg.init()				#From pygame.org
screen = pg.display.set_mode((500, 500))	#From pygame.org, modified
done = False 				#From pygame.org
pg.display.set_caption('Goomba Adventure')

bkgrd = pg.Surface(screen.get_size())
bkgrd = bkgrd.convert()
bkgrd.fill((10, 15, 200))

clock = pg.time.Clock()

font = pg.font.SysFont('Arial', 12)

while not rip:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            rip = True

        print(event)

    pg.display.update()
    clock.tick(60)
    
def runLVL():
	return()	

def gameStart():									
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
		gameStart()
	print levelChosen
	
	
def draw(x,y):
	pg.draw.rect(screen, (250,250,250), (0,0,500,500),0)
	pg.draw.lines(screen, (255,0,0), False, [(0,250), (500,250)], 1)	
	if y + 20 >= 250: 
		y = 251
		
	pg.draw.rect(screen, (50,80,100), (x,y,20,20), 5)
	pg.display.update()
	return y



while True:
	pygame.key.set_repeat(10, 5)
	for event in pg.event.get():
		if event.type  == pg.KEYDOWN and event.key == pg.K_LEFT:
			print "It Worked"
			xa = xa - 5
		if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
			print "It Worked"
			xa = xa + 5
		if event.type == pg.KEYDOWN and event.key == pg.K_UP:
			print "It worked"
			ya = ya - 5
		if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
			print "Jack is scrub"
			ya = ya + 5
	ya = draw(xa, ya)

