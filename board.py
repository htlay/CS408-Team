import Tkinter

class Board(Frame):
	h = 640
	w = 480

def __init__(self, parent):
	Frame.__init__(self, parent, background = "black")

	self.parent = parent

	self.initUI()

def placeApple(self):
	import random
	apple_h = random.randomInt(0, 640)
	apple_w = random.randomInt(0, 480)