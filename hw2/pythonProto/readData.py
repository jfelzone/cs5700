#going to open and create the publisher for the data
import time
try:
    # for Python2
    from Tkinter import * 
    import Tkinter as tk  ## notice capitalized T in Tkinter 
    from tkMessageBox import *
except ImportError:
    # for Python3
    from tkinter import * 
    import tkinter as tk
    from tkinter import messagebox

from multiprocessing import Process
#trying this, i think this will work. i need that shared memory bad
from thread import start_new_thread
#for the text notifications
import smtplib

#my classes being imported:
#from subscriber import Subscriber
from observers import *


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
            print subscriber.name

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
        self.email = StringVar()
        self.password = StringVar()
        self.athleteOne = StringVar()
        self.athleteTwo = StringVar()


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
        self.checkVarsListTopTen = []
        self.checkVarsListStream = []
        
        self.observerNameList = ["Email Observer","List Observer","Gui Observer","Athlete Comparison Observer", "Top Racers", "Stream Updater"]
        for i in self.observerNameList:
            self.checkVar = IntVar()
            c = Checkbutton(self.observerWindow, text = i , variable = self.checkVar, font=("Helvetica", 24),bg="light blue")
            c.pack(fill=X)
            if i == "Email Observer":
                l = Label(self.observerWindow, text="Enter your email address: ").pack()
                e = Entry(self.observerWindow, textvariable=self.email)
                e.pack()

                l = Label(self.observerWindow, text="Enter your password: ").pack()
                e = Entry(self.observerWindow, show="*",textvariable=self.password)
                e.pack()

            if i == "List Observer" or i == "Gui Observer" or i == "Email Observer":
                l = Label(self.observerWindow, text="Enter jersey number of the person you wish to observe: ").pack()
                e = Entry(self.observerWindow, textvariable=self.personNumber)
                e.pack()
            
            if i == "Athlete Comparison Observer":
                l = Label(self.observerWindow, text="Enter first athlete to monitor: ").pack()
                e = Entry(self.observerWindow, textvariable=self.athleteOne)
                e.pack()

                l = Label(self.observerWindow, text="Enter second athlete to monitor: ").pack()
                e = Entry(self.observerWindow,textvariable=self.athleteTwo)
                e.pack()
            

            self.checkVarsList.append(self.checkVar)
        

        # l = Label(self.observerWindow, text="Enter jersey number of the person you wish to observe: ").pack()
        # e = Entry(self.observerWindow, textvariable=self.personNumber)
        # e.pack()

        # l = Label(self.observerWindow, text="Enter your email address: ").pack()
        # e = Entry(self.observerWindow, textvariable=self.email)
        # e.pack()

        # l = Label(self.observerWindow, text="Enter your password: ").pack()
        # e = Entry(self.observerWindow, show="*",textvariable=self.password)
        # e.pack()

        self.generate = Button(self.observerWindow, text="Generate Observers", command=self.generateObservers)
        self.generate.pack()



    def generateObservers(self):
        print "You clicked the button!!!!"
        print self.personNumber.get()
        for i in self.checkVarsList:
            print i.get()
        print "\n"

        if self.checkVarsList[0].get() == 1:
            print 'generating gui'
            # guiSub = guiTicker("GUI")
            # sub.register(guiSub)
            #print sub.subscribers
            if self.email.get() == "" and self.password.get() == "" and self.personNumber.get() == 0:
                showerror("Error", "Sorry, enter email and password please")
            else:
                width = 1000
                height = 300
                self.windowEmail = tk.Toplevel(root)
                self.windowEmail.wm_title("Graphical Updates")
                self.windowEmail.minsize(width=width, height=height)
                l = Label(self.windowEmail, text="Email Observer Created. ",font=("Helvetica", 24))
                l.pack()
                emailSub = emailObserver("email", self.personNumber.get(), self.email.get(), self.password.get())
                self.sub.register(emailSub)

                self.windowEmail.protocol('WM_DELETE_WINDOW', self.doNothing)
                button = Button (self.windowEmail, text = "Unsubscribe.", command = lambda: self.unsubscribe(emailSub, self.windowEmail))
                button.pack()

        if self.checkVarsList[1].get() == 1:
            width = 1000
            height = 500
            if self.personNumber.get() == 0:
                showerror("Error", "Sorry, enter jersey number")                
            else:
                self.listWindow = tk.Toplevel(root)
                self.listWindow.wm_title("Tracking Jersey #: " + str(self.personNumber.get())+" Through List Window")
                self.listWindow.minsize(width=width, height=height)
                listbox = Listbox(self.listWindow)
                listbox.config(width=100)
                listbox.pack()

                listboxsub = listObserver("listbox", listbox, self.personNumber.get())
                self.sub.register(listboxsub)

                self.listWindow.protocol('WM_DELETE_WINDOW', self.doNothing)
                button = Button (self.listWindow, text = "Unsubscribe.", command = lambda: self.unsubscribe(listboxsub, self.listWindow))
                button.pack()

            # this gets moved to the subscriber class =>> listbox.insert(END, "a list entry")

        if self.checkVarsList[2].get() == 1:
            print 'generating gui'
            # guiSub = guiTicker("GUI")
            # sub.register(guiSub)
            #print sub.subscribers
            width = 1000
            height = 300
            if self.personNumber.get() == 0:
                showerror("Error", "Sorry, enter jersey number")                
            else:
                self.windowGui = tk.Toplevel(root)
                self.windowGui.wm_title("Tracking Jersey #: " + str(self.personNumber.get())+" Through Text Notifications")
                self.windowGui.minsize(width=1000, height=300)

                canvas = Canvas(self.windowGui, width=1000, height=300, bg="black")
                self.windowGui.title("Tracking Jersey #: "+str(self.personNumber.get()))
                canvas.pack()
                shape = canvas.create_line(10,height/2, width, height/2 ,fill="red")
                guiSub = guiTicker("GUI", canvas, 10, height/2, self.personNumber.get(), self.raceDist.get(), width)
                self.sub.register(guiSub)

                self.windowGui.protocol('WM_DELETE_WINDOW', self.doNothing)
                button = Button (self.windowGui, text = "Unsubscribe.", command = lambda: self.unsubscribe(guiSub, self.windowGui))
                button.pack()

        
        if self.checkVarsList[3].get() == 1:
            width = 1000
            height = 500
            if self.athleteOne.get() == 0 or self.athleteTwo.get() == 0:
                showerror("Error", "Sorry, enter jersey number")                
            else:
                self.listWindowComp = tk.Toplevel(root)
                self.listWindowComp.wm_title("Tracking Jersey #: " + str(self.athleteOne.get())+ " " + str(self.athleteTwo.get())+" Through List Window")
                self.listWindowComp.minsize(width=width, height=height)

                l = Label(self.listWindowComp, text="Athlete #: "+str(self.athleteOne.get())).pack()
                listboxOne = Listbox(self.listWindowComp)
                listboxOne.config(width=100)
                listboxOne.pack()

                listboxsubOne = listObserver("listbox", listboxOne, self.athleteOne.get())
                self.sub.register(listboxsubOne)

                l = Label(self.listWindowComp, text="Athlete #: "+str(self.athleteTwo.get())).pack()                
                listboxTwo = Listbox(self.listWindowComp)
                listboxTwo.config(width=100)
                listboxTwo.pack()

                listboxsubTwo = listObserver("listbox", listboxTwo, self.athleteTwo.get())
                self.sub.register(listboxsubTwo)

                self.listWindowComp.protocol('WM_DELETE_WINDOW', self.doNothing)
                button = Button (self.listWindowComp, text = "Unsubscribe.", command = lambda: self.unsubscribeTwo(listboxsubOne,listboxsubTwo, self.listWindowComp))
                button.pack()

        if self.checkVarsList[4].get() == 1:
            width = 1000
            height = 500
            self.toptenwindow = tk.Toplevel(root)
            self.toptenwindow.wm_title("Tracking Top Ten Based On Distance")
            self.toptenwindow.minsize(width=width, height=height)
            listbox = Listbox(self.toptenwindow)
            listbox.config(width=100)
            listbox.pack()

            toptensub = topRacersObserver("topten", listbox)
            self.sub.register(toptensub)

            # self.additionsList = ["Add Time","Add Distance"]
            # for i in self.additionsList:
            #     self.checkVar = IntVar()
            #     c = Checkbutton(self.toptenwindow, text = i , variable = self.checkVar, command= lambda: self.decorate(toptensub))
            #     c.pack()
            #     self.checkVarsListTopTen.append(self.checkVar)

            self.toptenwindow.protocol('WM_DELETE_WINDOW', self.doNothing)
            button = Button (self.toptenwindow, text = "Unsubscribe.", command = lambda: self.unsubscribe(toptensub, self.toptenwindow))
            button.pack()
        
        if self.checkVarsList[5].get() == 1:
            width = 1000
            height = 500
            self.streamWindow = tk.Toplevel(root)
            self.streamWindow.wm_title("Real Time Stream Updates")
            self.streamWindow.minsize(width=width, height=height)
            listbox = Listbox(self.streamWindow)
            listbox.config(width=100)
            listbox.pack()

            self.streamsub = streamer('streamer', listbox)
            self.sub.register(self.streamsub)

            self.additionsList = ["Add Second Column","Add Third Column"]
            self.checkVar = IntVar()
            c = Checkbutton(self.streamWindow, text = self.additionsList[0] , variable = self.checkVar, command= lambda: self.decorating())
                # c = Checkbutton(self.streamWindow, text = i , variable = self.checkVar)
            c.pack()
            self.checkVarsListStream.append(self.checkVar)

            self.checkVar = IntVar()
            c = Checkbutton(self.streamWindow, text = self.additionsList[1] , variable = self.checkVar, command= lambda: self.decoratingTwo())
                # c = Checkbutton(self.streamWindow, text = i , variable = self.checkVar)
            c.pack()
            self.checkVarsListStream.append(self.checkVar)

            # self.decorate = Button(self.streamWindow, text="Generate Decorations", command=self.decorateCommand)
            # self.decorate.pack()

            print self.checkVarsListStream


            self.streamWindow.protocol('WM_DELETE_WINDOW', self.doNothing)
            button = Button (self.streamWindow, text = "Unsubscribe.", command = lambda: self.unsubscribe(self.streamsub, self.streamWindow))
            button.pack()


    def unsubscribe(self, observer, window):
        self.sub.unregister(observer)
        window.destroy()
    
    def unsubscribeTwo(self, observerOne, observerTwo, window):
        self.sub.unregister(observerOne)
        self.sub.unregister(observerTwo)
        window.destroy()

    def doNothing(self):
        print "im not exiting"

    def decorating(self):
        print "made it here"
        self.sub.unregister(self.streamsub)
        self.streamsub = decorator(self.streamsub)
        self.sub.register(self.streamsub)
        #return readytodecorate

    def decoratingTwo(self):
        print "made it here"
        self.sub.unregister(self.streamsub)
        self.streamsub = decoratorTwo(self.streamsub)
        self.sub.register(self.streamsub)
        #return readytodecorate

    def decorateCommand(self):
        return 0





root = Tk()
#root.resizable(width=FALSE, height=FALSE)
app = MainApp(root)

root.mainloop()
root.destroy()