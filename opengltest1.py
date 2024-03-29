import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

verticies = (
(1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, 1),(1, 1, 1),(-1, -1, 1),(-1, 1, 1)
)

edges = (
(0, 1),(0, 3),(0, 4),
(2, 1),(2, 3),(2, 7),
(6, 3),(6, 4),(6, 7),
(5, 1),(5, 4),(5, 7)
)

def Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv (verticies[vertex])
	glEnd()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -10)	

	glRotatef(0,0,0,0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		r = 0.0
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		r=r+1
		glRotatef(r,r/2,r/3,r/4)
		Cube()
		pygame.display.flip()
		pygame.time.wait(1)

main()