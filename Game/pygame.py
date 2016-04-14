#Platform game with a twist
#
#I permanently borrowed a couple lines from various sources, but I labeled them all
#
#High School computer science project
#
#Released under the  GNU General Public License
import time
import sys
import os
import pygame as pg
import random

rip = True
xa = 50
ya = 250
pg.init()				#From pygame.org
screen = pg.display.set_mode((1000, 500))	#From pygame.org, modified
done = False 				#From pygame.org
pg.display.set_caption('Goomba Adventure')
pg.key.set_repeat(10, 5)

bkgrd = pg.Surface(screen.get_size())
bkgrd = bkgrd.convert()
bkgrd.fill((10, 15, 200))

clock = pg.time.Clock()
inert = 0
font = pg.font.SysFont('Arial', 12)

monst = []

def end(x):
	if x == 1:
		pg.draw.rect(screen, (0,255,0), (0,0,1000,500),0)
		pg.display.update()	
		time.sleep(10)
		sys.exit("you won")
	if x == 0:
		pg.draw.rect(screen, (255,0,0), (0,0,1000,500),0)
		pg.display.update()	
		time.sleep(10)
		sys.exit("you lost")


class mush:
	def __init__ (self,x,num):
		self.x = x+num*300+200
		self.num=num
	
	def move(self):
		if self.x <= xa + 10 and self.x >= xa - 10:
			end(0)
		if self.x >= xa:		
			self.x -= 0.5
			return self.x
		if self.x < xa:
			self.x += 0.5
			return self.x





pg.display.update()
clock.tick(60)
    


def draw(x,y):
	pg.draw.rect(screen, (15,10,250), (0,0,1000,500),0)
	if y + 20 >= 250: 
		y = 230
	
	
	for n in monst:
		pg.draw.rect(screen, (250,0,0), (n.move(),230,20,20), 5)
	 
	pg.draw.rect(screen, (250,250,100), (x,y,20,20), 5)
	pg.draw.rect(screen, (0,250,100), (0,250,1000,250), 0)	
	pg.draw.rect(screen, (121,85,72), (0,270,1000,250), 0)	
	pg.draw.rect(screen, (250, 250, 0), (950, 50, 10, 200,), 0)	
	pg.display.update()
	
	return y



def jump(xa, ya):
	inert = 10
	for inert in range (20):
		ya = ya - inert
		inert = inert - 1
		
		for event in pg.event.get():
			if event.type  == pg.KEYDOWN and event.key == pg.K_LEFT:
				xa = xa - 10
			if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
				xa = xa + 10
		draw(xa, ya)
		time.sleep(.05)

	for inert in range (20):
		ya = ya + inert
		inert = inert + 1

		for event in pg.event.get():
			if event.type  == pg.KEYDOWN and event.key == pg.K_LEFT:
				xa = xa - 10
			if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
				xa = xa + 10	
		draw(xa, ya)
		time.sleep(.05)
	return xa


for x in range(3):
	monst.append(mush(30+x*10, x))
while True:
	
	for event in pg.event.get():
		if event.type  == pg.KEYDOWN and event.key == pg.K_LEFT:
			
			xa = xa - 3
		if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
			
			xa = xa + 3
		if event.type == pg.KEYDOWN and event.key == pg.K_UP:
			
			xa = jump(xa, ya)
		if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
			
			ya = ya + 3
	ya = draw(xa, ya)
	if xa >= 950:
		end(1)
