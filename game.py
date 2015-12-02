from meet import *
ball1={"radius":20,"x":7,"y":60,"dy":1,"dx":1}
cells=[]
circle1=create_cell(ball1)
cells.append(circle1)

def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x > width):
			cell.set_dx(-cell.get_dx())
		if (y > height):
			cell.set_dy(-cell.get_dy())
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=-cell.xcor()
		y=-cell.ycor()
		if (x < width):
			cell.set_dx(-cell.get_dx())
		if (y < height):
			cell.set_dy(-cell.get_dy())
		

while(True):
	move_cells(cells)
	borders(cells)
