from meet import *
import random

num_cells=0

cells=[]
colors=["pink","blue","purple","green","yellow","red","orange"]

while(num_cells <15):
	ball1 = {"radius":random.randint (5,60),"x":random.randint(0,100),"y":random.randint(0,100),"dy":random.uniform(0.3,1),"dx":random.uniform(0.3,1), "color":random.choice(colors)}

	circle1=create_cell(ball1)
	cells.append(circle1)
	num_cells+=1

user_cell={"radius":random.randint (7,100),"x":50,"y":50,"dy":random.uniform(0.4,1),"dx":random.uniform(0.4,1)}
t=create_cell(user_cell)
cells.append(t)

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

		if (x < -width):
			cell.set_dx(-cell.get_dx())
		if (y < -height):
			cell.set_dy(-cell.get_dy())

		
while (True):
	move_cells(cells)
	borders(cells)
	dx,dy=get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	for i in cells:
		r=i.get_radius()
		x=i.xcor()
		y=i.ycor()
		for g in cells:
			r2=g.get_radius()
			x2=g.xcor()
			y2=g.ycor()
			if ((x-x2)**2+(y-y2)**2)**0.5<(r-r2):
				if (r>r2):
					g.goto(get_random_x(),get_random_y())
					i.set_radius(r+r2*0.3)
					if (g==user_cell):
						g.bye()
				if (r<r2):
					i.goto(get_random_x(),get_random_y())
					g.set_radius(r+r2*0.3)
					if (i==user_cell):
						i.bye()
meet.mainloop()
	
