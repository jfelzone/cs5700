#going to open and create the publisher for the data
import time
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import * 

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
                time.sleep(1)
            #print line.split(',')
            self.dispatch(line)
    
    def threadedSimFunc(self):
        start_new_thread(self.dataSimulate, ())
        #self.p = Process(target=self.dataSimulate,)
        #self.p.start()
        #self.p.join()
 

#i need to spin up a thread for the simulation to be running in the background.
#if that will work
sub = Subject() 
test = Subscriber('test')
sub.register(test)

sub.threadedSimFunc()


class MainApp:
    def __init__(self, master):
        self.checkVarsList = []

        master.minsize(width=400, height=200)
        frame = Frame(master, width=200,  height=100)
        master.wm_title("Race Observer Generator")
        frame.pack()

        self.observerNameList = ["Email Observer","List Observer","Gui Observer","MileStone Times Observer"]
        for i in self.observerNameList:
            self.checkVar = IntVar()
            c = Checkbutton(frame, text = i , variable = self.checkVar)
            c.pack()
            self.checkVarsList.append(self.checkVar)

        self.generate = Button(frame, text="Generate Observers", command=self.generateObservers)
        self.generate.pack(side=LEFT)

        self.quitbutton = Button(frame, text="Quit", fg = "red", command = frame.quit)
        self.quitbutton.pack()

    def generateObservers(self):
        print "You clicked the button!!!!"
        for i in self.checkVarsList:
            print i.get()
        print "\n"

        if self.checkVarsList[2].get() == 1:
            print 'generating gui'
            guiSub = Subscriber("GUI")
            sub.register(guiSub)
            print sub.subscribers




root = Tk()
#root.resizable(width=FALSE, height=FALSE)
app = MainApp(root)

root.mainloop()
root.destroy()