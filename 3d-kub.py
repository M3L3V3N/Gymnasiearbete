import pygame
from math import sin, cos
import time

screenwidth = 1000
screenheight = 1000

nodes = [
			# nearest nodes
			(100, 100, -100),
 		   	(100, -100, -100),
    		(-100, -100, -100),
    		(-100, 100, -100),
    		(100, 100, 100),
    		(100, -100, 100),
    		(-100, -100, 100),
    		(-100, 100, 100)
		]

edges = [
			(0, 1),
    		(1, 2),
    		(2, 3),
    		(3, 0),
    		(4, 5),
    		(5, 6),
    		(6, 7),
    		(7, 4),
	    	(0, 4),
    		(1, 5),
    		(2, 6),
	    	(3, 7)
		]

# converts coordinates from top left to middle of screen
def convertCoord(coord):
	new_x = coord[0] + screenwidth / 2
	new_y = coord[1] + screenheight / 2
	
	return (int(new_x), int(new_y))

def rotate(coordinates, angle_x, angle_y, angle_z, depth):
	new_nodes = []
	for coord in coordinates:
		x = coord[0]
		y = coord[1]
		z = coord[2]

		#rotate around x-axis
		new_y = y * cos(angle_x) - z * sin(angle_x)
		new_z = y * sin(angle_x) + z * cos(angle_x)
	
		y = new_y
		z = new_z

		# rotate around y-axis
		new_x = x * cos(angle_y) - z * sin(angle_y)
		new_z = x * sin(angle_y) + z * cos(angle_y)
		x = new_x
		z = new_z
		# rotate around z-axis
		new_x = x * cos(angle_z) - y * sin(angle_z)
		new_y = x * sin(angle_z) + y * cos(angle_z)
		x = new_x
		y = new_y

		depth_scale = depth / (depth - z)
		x *= depth_scale
		y *= depth_scale

		new_nodes.append((x, y, z))

	return new_nodes


def main():

	angle_x = 0
	angle_y = 0
	angle_z = 0
	depth = 1000

	pygame.init()

	screen = pygame.display.set_mode((screenwidth, screenheight))
	
	FPS = 100 # frames per second setting
	fpsClock = pygame.time.Clock()

	running = True

	while running:
		screen.fill((0,0,0))
			
		angle_x += 0.01
		angle_y += 0.01
		angle_z += 0.01

		rotated_nodes = rotate(nodes, angle_x, angle_y, angle_z, depth)


		for edge in edges:
			
			start = rotated_nodes[edge[0]]
			end = rotated_nodes[edge[1]]

			start_screen = convertCoord(start)
			end_screen = convertCoord(end)
			pygame.draw.line(screen, [255,255,255], (start_screen[0], start_screen[1]), (end_screen[0], end_screen[1]))


		fpsClock.tick(FPS)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__=="__main__":
	main()