#going to open and create the publisher for the data
import time
try:
    # for Python2
    from Tkinter import * 
    import Tkinter as tk  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import * 
    import tkinter as tk

from multiprocessing import Process
#trying this, i think this will work. i need that shared memory bad
from thread import start_new_thread


# file = open("simulation.csv", "r")

# for line in file:
#     if line == "---\n":
#         time.sleep(1)
#     print line.split(',')


class Subscriber():
    def __init__(self, name):
        self.name = name
    def update(self, data):
        print self.name , ":" , data


class guiTicker(Subscriber):

    def __init__(self, name, canvas, xcoord, ycoord, jerseynumber, totaldistance, totalwindowsize):
        self.name = name
        self.canvas = canvas
        self.shape = canvas.create_rectangle(xcoord, ycoord, 20, 5, fill = "blue")
        self.jerseynumber = jerseynumber
        self.totaldistance = totaldistance
        self.totalwindowsize = totalwindowsize
        self.movementList = [0]

    def calculateMovement(self, currentPosition):
        x = (self.totalwindowsize*currentPosition)/self.totaldistance
        return x - self.movementList[-1]

    def update(self,data): 
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            print self.name , ":" , data
            if (self.calculateMovement(int(float(data[3]))) + self.movementList[-1]) < self.totalwindowsize:
                self.canvas.move(self.shape, self.calculateMovement(int(float(data[3]))), 0)
                self.movementList.append(self.movementList[-1] + self.calculateMovement(int(float(data[3]))))

class Subject:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)
    
    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)

    def dataSimulate(self):
        file = open("simulation.csv", "r")

        for line in file:
            if line == "---\n":
                time.sleep(0.25)
            #print line.split(',')
            self.dispatch(line.rstrip('\n').split(','))
    
    def threadedSimFunc(self):
        start_new_thread(self.dataSimulate, ())
        #self.p = Process(target=self.dataSimulate,)
        #self.p.start()
        #self.p.join()
 

#i need to spin up a thread for the simulation to be running in the background.
#if that will work
#moving these inside the application
# sub = Subject() 
# test = Subscriber('test')
# sub.register(test)

# sub.threadedSimFunc()


class MainApp:
    def __init__(self, master):
        self.raceName = StringVar()
        self.raceDist = IntVar()
        self.raceTitle = StringVar()
        self.raceTime = IntVar()
        self.personNumber = IntVar()


        master.minsize(width=400, height=200)
        frame = Frame(master, width=200,  height=100)
        master.wm_title("Race Observer Generator")
        frame.pack()

        l = Label(frame, text="Enter a race name: ").pack()
        e = Entry(frame, textvariable=self.raceName)
        e.pack()

        l = Label(frame, text="Enter race total distance: ").pack()
        e = Entry(frame, textvariable=self.raceDist)
        e.pack()

        l = Label(frame, text="Enter race title: ").pack()
        e = Entry(frame, textvariable=self.raceTitle)
        e.pack()

        l = Label(frame, text="Enter race starting time: ").pack()
        e = Entry(frame, textvariable=self.raceTime)
        e.pack()


        
        self.startRace = Button(frame, text="Start Race", command=self.startRace)
        self.startRace.pack()
        self.quitbutton = Button(frame, text="Quit", fg = "red", command = frame.quit)
        self.quitbutton.pack()

    def startRace(self):
        #moving these to here so that the start race can happen:
        self.sub = Subject() 
        test = Subscriber('test')
        self.sub.register(test)

        self.sub.threadedSimFunc()

        self.observerWindow = tk.Toplevel(root)
        self.observerWindow.wm_title("Graphical Updates")
        self.observerWindow.minsize(width=1000, height=300)

        self.checkVarsList = []
        
        self.observerNameList = ["Email Observer","List Observer","Gui Observer","MileStone Times Observer"]
        for i in self.observerNameList:
            self.checkVar = IntVar()
            c = Checkbutton(self.observerWindow, text = i , variable = self.checkVar)
            c.pack()
            self.checkVarsList.append(self.checkVar)
        

        l = Label(self.observerWindow, text="Enter number of person you wish to observe: ").pack()
        e = Entry(self.observerWindow, textvariable=self.personNumber)
        e.pack()
        self.generate = Button(self.observerWindow, text="Generate Observers", command=self.generateObservers)
        self.generate.pack()



    def generateObservers(self):
        print "You clicked the button!!!!"
        print self.personNumber.get()
        for i in self.checkVarsList:
            print i.get()
        print "\n"

        if self.checkVarsList[2].get() == 1:
            print 'generating gui'
            # guiSub = guiTicker("GUI")
            # sub.register(guiSub)
            #print sub.subscribers
            width = 1000
            height = 300
            self.windowGui = tk.Toplevel(root)
            self.windowGui.wm_title("Graphical Updates")
            self.windowGui.minsize(width=1000, height=300)

            canvas = Canvas(self.windowGui, width=1000, height=300, bg="black")
            self.windowGui.title("Tracking Jersey #: "+str(self.personNumber.get()))
            canvas.pack()
            shape = canvas.create_line(10,height/2, width, height/2 ,fill="red")
            guiSub = guiTicker("GUI", canvas, 10, height/2, self.personNumber.get(), self.raceDist.get(), width)
            self.sub.register(guiSub)


            





root = Tk()
#root.resizable(width=FALSE, height=FALSE)
app = MainApp(root)

root.mainloop()
root.destroy()