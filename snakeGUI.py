import random
from Tkinter import *

WIDTH = 495
HEIGHT = 305

class Game:
    def __init__(self):

        # set up TKinter
        self.root = Tk()

        # main window
        self.frame1 = None

        # window
        self.w = None
        
        # scores
        self.scoreC = None
        self.score = 0

        #
        self.hor = True
        
        # direction
        self.upid = self.downid = self.rightid = self.leftid = 0
        
        # snake head
        self.head = -1
        
        # speed
        self.time = 700

    # start page
    def home(self):

        # set up main window
        self.frame1 = Frame(self.root, width=750, height=350,bg="black")
        
        # set up window
        self.root.wm_minsize(width=750, height=666)
        self.root.title("Snake")
        
        # set background
        self.root.configure(bg="black")
        
        # set up window
        self.frame1.pack_propagate(0)
        self.frame1.update()

        # start button
        start = Button(self.frame1, text="start", bg="black", command=lambda: self.callgame(100))

        start.grid(row=0, columnspan=2)
        self.H=Label(self.root, text="CS 408\nJimmy Chen, Hung Lay, Samantha Wu", bg="black", fg="white", pady=10)
        self.H.pack()
        self.frame1.pack(expand=True)
        self.root.mainloop()

    # start game    
    def callgame(self, time):
        # speed
        self.time = time

        # start game
        self.game()

    # down arrow
    def calldown(self, key):
        if self.hor:
            self.w.after_cancel(self.leftid)
            self.w.after_cancel(self.rightid)
            self.down(0)

    # up arrow
    def callup(self, key):
        if self.hor:
            self.w.after_cancel(self.leftid)
            self.w.after_cancel(self.rightid)
            self.up(0)

    # right arrow
    def callright(self, key):
        if not self.hor:
            self.w.after_cancel(self.upid)
            self.w.after_cancel(self.downid)
            self.right(0)

    # left arrow
    def callleft(self, key):
        if not self.hor:
            self.w.after_cancel(self.upid)
            self.w.after_cancel(self.downid)
            self.left(0)

    # game
    def game(self):

        # score
        self.score = 0

        # game window
        self.w = Canvas(self.root, width=750, height=500, relief="flat", highlightbackground="white", highlightthickness=10)

        # close start window
        self.frame1.destroy()

        # game window
        self.w.configure(background="black")
        self.w.pack(side="left")

        # snake
        self.w.create_line(300, 250, 350, 250, width=10, fill="white")

        # score text
        self.scoreC = Label(self.root, text="Score\n" + str(self.score), bg="black", fg="white")
        self.scoreC.pack(side="bottom")

        # arrow keys
        self.root.bind("<Up>", self.callup)
        self.root.bind("<Down>", self.calldown)
        self.root.bind("<Right>", self.callright)
        self.root.bind("<Left>", self.callleft)

        # generate food
        self.createFood()

        # initial movement
        self.right(0)

    def arrow(self, direction, i):

        # coordinates
        crd = self.w.coords(1)
        if len(crd) > 0:
            if crd[0] == crd[2]:
                if crd[1] > crd[3]:
                    # print("inside if1")
                    crd[1] -= 10
                if crd[1] < crd[3]:
                    # print("inside if2")
                    crd[1] += 10
            else:
                if crd[0] > crd[2]:
                    crd[0] -= 10
                if crd[0] < crd[2]:
                    crd[0] += 10

            if direction == 'down':
                crd[-1] += 10
            elif direction == 'up':
                crd[-1] -= 10
            elif direction == 'right':
                crd[-2] += 10
            elif direction == 'left':
                crd[-2] -= 10

            if i == 0:
                crd.append(crd[-2])
                crd.append(crd[-2])

                if direction == 'down':
                    crd[-3] -= 10
                elif direction == 'up':
                    crd[-3] += 10
                elif direction == 'right':
                    crd[-4] -= 10
                elif direction == 'left':
                    crd[-4] += 10
            
            if crd[0] == crd[2] and crd[1] == crd[3]:
                crd = crd[2:]
            self.w.coords(1, *crd)
            self.w.delete(self.head)

            if direction == 'down':
                self.head = self.w.create_line(crd[-2], crd[-1], crd[-2], crd[-1] + 5, width=10, fill="white")
            elif direction == 'up':
                self.head = self.w.create_line(crd[-2], crd[-1], crd[-2], crd[-1] + 5, width=10, fill="white")
            elif direction == 'right':
                self.head = self.w.create_line(crd[-2], crd[-1], crd[-2] + 5, crd[-1], width=10, fill="white")
            elif direction == 'left':
                self.head = self.w.create_line(crd[-2], crd[-1], crd[-2] - 5, crd[-1], width=10, fill="white")

            end = self.end()
            self.checkEaten()
            i += 1
            if direction == 'down' or direction == 'up':
                self.hor = False
            else:
                self.hor = True

            if not end:

                if direction == 'down':
                    self.downid = self.w.after(self.time, self.down, i)
                elif direction == 'up':
                    self.upid = self.w.after(self.time, self.up, i)
                elif direction == 'right':
                    self.rightid = self.w.after(self.time, self.right, i)
                elif direction == 'left':
                    self.leftid = self.w.after(self.time, self.left, i)

            else:
                self.w.delete(1)
                self.w.delete(self.head)
                self.w.delete(self.food)
                self.restart = Button(self.root, text="Restart", command=lambda: self.callhome())
                self.restart.pack(side="bottom", side="left")


    # down arrow
    def down(self, i):
        self.arrow('down', i)

    def up(self, i):
        self.arrow('up', i)

    def right(self, i):
        self.arrow('right', i)

    def left(self, i):
        self.arrow('left', i)

    def createFood(self):
        # self.w.delete(self.food) #deleting old food.
        crd = self.w.coords(1)
        ext = []
        for i in crd:
            ext.append(i)
            for j in range(-50, 50):
                ext.append(i + j)
        randx = random.randrange(20, 730)
        randy = random.randrange(20, 480)
        while randx not in ext and randy not in ext:
            randx = random.randrange(20, 730)
            randy = random.randrange(20, 480)
        self.food = self.w.create_line(randx, randy, randx + 12, randy, width=10, fill="white")

    def checkEaten(self):
        headcoords = self.w.coords(self.head)
        foodcoords = self.w.coords(self.food)
        flag = False
        if int(headcoords[-4]) in range(int(foodcoords[-4]) - 7, int(foodcoords[-2]) + 7) and int(
                headcoords[-3]) in range(int(foodcoords[-1]) - 10, int(foodcoords[-1] + 10)):
            flag = True
        if flag:
            self.grow()
            self.score += 10
            self.scoreC.configure(text="Score\n" + str(self.score), bg="black", fg="white")
            self.w.delete(self.food)
            if not self.time == 30:
                self.time = self.time - 10
            self.createFood()

    def grow(self):
        crd = self.w.coords(1)
        if crd[0] != crd[2]:  # horizontal condition
            if crd[0] < crd[2]:
                crd[0] -= 20
            else:
                crd[0] += 20
            self.w.coords(1, *crd)
        else:
            if crd[3] < crd[1]:
                crd[1] += 20
            else:
                crd[1] -= 20
            self.w.coords(1, *crd)

    def end(self):
        crd = self.w.coords(1)
        h = self.w.coords(self.head)
        a = 0
        while a < len(crd) - 2:
            if crd[a] == crd[a + 2]:
                if (h[0] == crd[a] and crd[a + 1] < h[1] < crd[a + 3]) or (
                        h[0] == crd[a]  and crd[a + 1] > h[1] > crd[a + 3]):
                    return True
            else:
                if (h[1] == crd[a + 1] and crd[a] < h[0] < crd[a + 2]) or (h[1] == crd[a + 1] and crd[a] > h[0] > crd[a + 2]):
                    return True
            a += 2
        if (h[0] == 0 and 0 < h[1] < 500) or (h[1] == 0 and 0 < h[0] < 750) or (h[1] == 510 and 0 < h[0] < 750) or (h[0] == 760 and 0<h[1]<500):
            return True
        return False

    def callhome(self):
        self.w.destroy()
        self.restart.destroy()
        self.H.destroy()
        self.scoreC.destroy()
        self.home()

g = Game()
g.home()