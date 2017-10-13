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

class emailObserver(Subscriber):
    def __init__(self, name, jerseynumber, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(email, password)
        self.jerseynumber = jerseynumber

    def update(self, data):
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            self.server.sendmail("App", "2089546530@vtext.com", str(data[1])+","+str(data[0])+","+str(data[3]))
            #+", "+str(data[1])+", "+str(data[2])+", "+str(data[3]))
            print self.name , ":" , data[0], data[1] , data[2], data[3]

class listObserver(Subscriber):
    def __init__(self, name, listbox, jerseynumber):
        self.name = name
        self.listbox = listbox
        self.jerseynumber = jerseynumber

    def update(self,data):
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            print self.name , ":" , data
            string = str(data[1])+", "+str(data[0])+", "+str(data[2])+", "+str(data[3])
            self.listbox.insert(0, string)


#so baseline without decorator will just desplay the top 10 guys' number
class topRacersObserver(Subscriber):
    def __init__(self, name, listbox):

        self.name = name
        self.data = []
        self.topTen = []
        self.topTenDist = []
        self.listbox = listbox

    def updateTopTen(self):
        if len(self.topTen) < 10:
            self.topTen.append(self.data)
            self.topTenDist.append(self.data[3])
            self.topTenDist.sort(reverse=True)
        elif len(self.topTen) >= 10 and self.data[3] > self.topTenDist[0]:
            tracker = 0
            for index, x in enumerate(self.topTen):
                if x[3] == self.data[3]:
                    tracker = index
            del self.topTen[tracker]
            self.topTenDist.pop(0)

            self.topTen.append(self.data)
            self.topTenDist.append(self.data[3])
            self.topTenDist.sort(reverse=True)


    def update(self, data):
        if data[0] == "OnCourse": 
            self.data = data
            self.updateTopTen()
            self.listbox.delete(0,END)
            for i in self.topTen: 
                #keep in mind the order on this guy and how we are going to have to sort
                self.listbox.insert(0, i[1])


#
# this got too complex, will try a simpler decorator, and then if i have time get this guy working

# class topRacersObserverDecorator(topRacersObserver):
#     def __init__(self, decorated):
#         self.decorated = decorated
#         # self.name = name
#         # self.data = []
#         # self.topTen = []
#         # self.topTenDist = []
#         # self.listbox = listbox
    
#     def __getattr__(self, name):
#         return getattr(self.decorated, name)

#     def updateTopTen(self):
#         if len(self.topTen) < 10:
#             self.topTen.append(self.data)
#             self.topTenDist.append(self.data[3])
#             self.topTenDist.sort(reverse=True)
#         elif len(self.topTen) >= 10 and self.data[3] > self.topTenDist[0]:
#             tracker = 0
#             for index, x in enumerate(self.topTen):
#                 if x[3] == self.data[3]:
#                     tracker = index
#             del self.topTen[tracker]
#             self.topTenDist.pop(0)

#             self.topTen.append(self.data)
#             self.topTenDist.append(self.data[3])
#             self.topTenDist.sort(reverse=True)


#     def update(self, data):
#         if data[0] == "OnCourse": 
#             self.data = data
#             self.updateTopTen()
#             self.listbox.delete(0,END)
#             for i in self.topTen: 
#                 #keep in mind the order on this guy and how we are going to have to sort
#                 self.listbox.insert(0, self.generateString(data))

#     def generateString(self, inputer):
#         return inputer[1]+', '+inputer[2]

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
        
        self.observerNameList = ["Email Observer","List Observer","Gui Observer","Athlete Comparison Observer", "Top Racers"]
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

            self.additionsList = ["Add Time","Add Distance"]
            for i in self.additionsList:
                self.checkVar = IntVar()
                c = Checkbutton(self.toptenwindow, text = i , variable = self.checkVar, command= lambda: self.decorate(toptensub))
                c.pack()
                self.checkVarsListTopTen.append(self.checkVar)

            self.toptenwindow.protocol('WM_DELETE_WINDOW', self.doNothing)
            button = Button (self.toptenwindow, text = "Unsubscribe.", command = lambda: self.unsubscribe(toptensub, self.toptenwindow))
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

    def decorate(self, readytodecorate):
        readytodecorate = topRacersObserverDecorator(readytodecorate)






root = Tk()
#root.resizable(width=FALSE, height=FALSE)
app = MainApp(root)

root.mainloop()
root.destroy()