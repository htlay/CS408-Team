import random
from Tkinter import Label, Tk, Frame, Button, PhotoImage, Canvas, Entry
from tkFont import Font


class Game:
    def __init__(self):
        self.root = Tk()
        self.frame1 = None
        self.frame2 = None
        self.w = None
        self.scoreC = None
        self.score = 0
        self.hor = True
        self.upid = self.downid = self.rightid = self.leftid = 0
        self.head = -1
        self.time = 700

    def home(self):
        self.frame1 = Frame(self.root, width=750, height=350, padx=250, bg="black")
        self.frame2 = Frame(self.root, height=250, width=750, bg="black", padx=25)
        self.root.wm_minsize(width=750, height=666)
        self.root.configure(bg="black")
        self.frame1.pack_propagate(0)
        self.frame1.update()
        self.frame1.configure(pady=self.frame1.cget("height") / 2.5)
        start = Button(self.frame1, text="Begin", bg="orange", padx=25, pady=5,
                        font=Font(family="comic sans MS", size=10),
                        command=lambda: self.callgame(75))
        self.frame2.pack_propagate(0)
        exp = """        This is a game in which
        the arrow keys are used
        to move the snake around
        and to get points"""
        exf = Font(family="comic sans MS", size=20)
        Label(self.frame2, bg="black", text=exp, padx=10).pack(side="right")
        Label(self.frame2, fg="white", bg="black", text=exp, justify="left", font=exf).pack(side="left")
        start.grid(row=0, columnspan=2)
        head = Font(family="comic sans MS", size=30)
        self.H=Label(self.root, text="SNAKES", font=head, fg="orange", bg="black", pady=10)
        self.H.pack()
        self.frame2.pack(expand=True)
        self.frame1.pack(expand=True)
        self.root.mainloop()

    def callgame(self, time):
        self.time = time
        self.game()

    def calldown(self, key):
        if self.hor:
            self.w.after_cancel(self.leftid)
            self.w.after_cancel(self.rightid)
            self.down(0)

    def callup(self, key):
        if self.hor:
            self.w.after_cancel(self.leftid)
            self.w.after_cancel(self.rightid)
            self.up(0)

    def callright(self, key):
        if not self.hor:
            self.w.after_cancel(self.upid)
            self.w.after_cancel(self.downid)
            self.right(0)

    def callleft(self, key):
        if not self.hor:
            self.w.after_cancel(self.upid)
            self.w.after_cancel(self.downid)
            self.left(0)

    def game(self):
        self.score = 0
        self.w = Canvas(self.root, width=750, height=500, relief="flat", highlightbackground="grey",
                        highlightthickness=10)
        self.frame1.destroy()
        self.frame2.destroy()
        self.root.configure(width=1000, padx=10)
        self.root.pack_propagate(0)
        self.w.configure(background="black")
        self.w.pack(side="left")
        self.w.create_line(300, 250, 450, 250, width=10, fill="blue")
        self.scoreC = Label(self.root, text="Score\n" + str(self.score), bg="black", fg="white", padx=25, pady=35,
                            font=Font(family="comic sans MS", size=25))
        self.head = self.w.create_line(450, 250, 455, 250, width=10, fill="white")
        self.scoreC.pack(side="top")
        self.root.bind("<Up>", self.callup)
        self.root.bind("<Down>", self.calldown)
        self.root.bind("<Right>", self.callright)
        self.root.bind("<Left>", self.callleft)
        self.createFood()
        self.right(0)

    def down(self, i):
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

            crd[-1] += 10

            if i == 0:
                crd.append(crd[-2])
                crd.append(crd[-2])
                crd[-3] -= 10
            if crd[0] == crd[2] and crd[1] == crd[3]:
                crd = crd[2:]
            self.w.coords(1, *crd)
            self.w.delete(self.head)
            self.head = self.w.create_line(crd[-2], crd[-1], crd[-2], crd[-1] + 5, width=10, fill="blue")
            end = self.end()
            self.checkEaten()
            i += 1
            self.hor = False
            if not end:
                self.downid = self.w.after(self.time, self.down, i)
            else:
                self.w.delete(1)
                self.w.delete(self.head)
                self.w.delete(self.food)
                self.start = Button(self.root, text="Start", bg="blue", padx=25, pady=25,
                                font=Font(family="comic sans MS", size=15),
                                command=lambda: self.callhome())
                self.start.pack(side="bottom")

    def up(self, i):
        crd = self.w.coords(1)
        if len(crd)>0:
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

            crd[-1] -= 10

            if i == 0:
                crd.append(crd[-2])
                crd.append(crd[-2])
                crd[-3] += 10
            if crd[0] == crd[2] and crd[1] == crd[3]:
                crd = crd[2:]
            self.w.coords(1, *crd)
            self.w.delete(self.head)
            self.head = self.w.create_line(crd[-2], crd[-1], crd[-2], crd[-1] - 5, width=10, fill="blue")
            end = self.end()
            self.checkEaten()
            i += 1
            self.hor = False
            if not end:
                self.upid = self.w.after(self.time, self.up, i)
            else:
                self.w.delete(1)
                self.w.delete(self.head)
                self.w.delete(self.food)
                self.start = Button(self.root, text="Start", bg="blue", padx=25, pady=25,
                                font=Font(family="comic sans MS", size=15),
                                command=lambda: self.callhome())
                self.start.pack(side="bottom")

    def right(self, i):
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

            crd[-2] += 10

            if i == 0:
                crd.append(crd[-2])
                crd.append(crd[-2])
                crd[-4] -= 10
            if crd[0] == crd[2] and crd[1] == crd[3]:
                crd = crd[2:]
            self.w.coords(1, *crd)
            self.w.delete(self.head)
            self.head = self.w.create_line(crd[-2], crd[-1], crd[-2] + 5, crd[-1], width=10, fill="blue")
            end = self.end()
            self.checkEaten()
            i += 1
            self.hor = True
            if not end:
                self.rightid = self.w.after(self.time, self.right, i)
            else:
                self.w.delete(1)
                self.w.delete(self.head)
                self.w.delete(self.food)
                self.start = Button(self.root, text="Start", bg="blue", padx=25, pady=25,
                                font=Font(family="comic sans MS", size=15),
                                command=lambda: self.callhome())
                self.start.pack(side="bottom")

    def left(self, i):
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

            crd[-2] -= 10

            if i == 0:
                crd.append(crd[-2])
                crd.append(crd[-2])
                crd[-4] += 10
            if crd[0] == crd[2] and crd[1] == crd[3]:
                crd = crd[2:]
            self.w.coords(1, *crd)
            self.w.delete(self.head)
            self.head = self.w.create_line(crd[-2], crd[-1], crd[-2] - 5, crd[-1], width=10, fill="blue")
            end = self.end()
            self.checkEaten()
            i += 1
            self.hor = True
            if not end:
                self.leftid = self.w.after(self.time, self.left, i)
            else:

                self.w.delete(1)
                self.w.delete(self.head)
                self.w.delete(self.food)
                self.start = Button(self.root, text="Start", bg="blue", padx=25, pady=25,
                                font=Font(family="comic sans MS", size=15),
                                command=lambda: self.callhome())
                self.start.pack(side="bottom")

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
        self.food = self.w.create_line(randx, randy, randx + 12, randy, width=10, fill="yellow")

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
            self.scoreC.configure(text="Score\n" + str(self.score), bg="black", fg="blue", padx=25, pady=35,
                                  font=Font(family="comic sans MS", size=25))
            self.w.delete(self.food)
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
        self.start.destroy()
        self.H.destroy()
        self.scoreC.destroy()
        self.home()


g = Game()
g.home()