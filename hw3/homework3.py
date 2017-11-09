#Jake Felzien
#homework 3
# final version designed from UML refined diagram
import math

class UndoStack():
    def __init__(self):
        self.stack = []
        #self.currentExecutionChain = []

    def addExecutionChainCommand(self, executionChain):
        # if len(self.stack) > 0:
        #     currentExecutionChain = self.stack[-1][:]
        # else:
        #     currentExecutionChain = []
        # currentExecutionChain.append(execution)

        self.stack.append(executionChain)

    def popOffExecutionChain(self):
        self.stack.pop()


#this is essentially my invoker class
class CommandStack():

    #array/stack to store the commands as they come in
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    #method to call and execute the commands
    def execute_commands(self):
        for command in self.commands:
            command.execute()

#abstract command class that all other commands will inherit from
class Command():
    def __init__(self):
        pass
    def execute(self):
        pass


#first command class for drawing a square on our canvasObject
# here im going to want to pass in the canvas object as well, but i think im going to want to do it differently than first iteration

class Class_Box(Command):
    def __init__(self, a, b, c, d, canvasObject, classNameString):
        # we may actually only need two points for this rectangle (because it is just the upper left corner and the bottom corner)
        #can we do all of the algorithmic stuff off of this... we should
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.classNameString = classNameString
        # we actually don't need this because the coordinate system essentially houses our four points, and thus what everything is conatined within
        # self.x3 = 0
        # self.y3 = 0
        # self.x4 = 0
        # self.y4 = 0
        self.connections = []

    def execute(self):
        self.drawingSave = self.canvasObject.create_rectangle(self.x0, self.y0, self.x1, self.y1)+self.canvasObject.create_rectangle(self.x0, self.y0, self.x1, self.y1-50)+self.canvasObject.create_text(self.x0+40,self.y0+10,fill="darkblue",font="Times 10 italic bold",
                        text=self.classNameString)


#need a class for modifying previous classes (move execution process)
#how in the world to implement this....
# class Move_Class(Command):
#     def __init__(self, )



#i think this will be virtually the same again
class Binary_Association(Command):
    def __init__(self, a, b, c, d, canvasObject):
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.connections = []

    def execute(self):
        self.drawingSave = self.canvasObject.create_line(self.x0, self.y0, self.x1, self.y1)


#class Dependency

class Dependency_Association(Command):
    def __init__(self, a,b,c,d,canvasObject):
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.diagPointX = self.x0
        self.diagPointY = self.y0
        self.otherX = 0
        self.otherY = 0
        self.otherX2 = 0
        self.otherY2 = 0
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.connections = []

    def getSlope(self):
        return float(self.y1-self.y0)/float(self.x1-self.x0)

    def getInterceptB(self):
        return self.y1 - (self.getSlope()*self.x1)

    def distance(self, x0, x1, y0, y1):
        return math.sqrt(math.pow((x0-x1),2)+math.pow((y0-y1),2))

    def getDiagonalPointFromStart(self):
        # diagPointX = self.x0
        # diagPointY = self.y0
        while distance(diagPointX, self.x0, diagPointY, self.y0)  < 10:
            diagPointX += 1
            diagPointY = self.getSlope()*diagPointX+self.getInterceptB()

    def getOtherSquarePoints(self):
        tempxc = (self.x0+ self.diagPointX)/2
        tempyc = (self.y0+self.diagPointY)/2
        tempxd = (self.x0 - self.diagPointX)/2
        tempyd = (self.y0 - self.diagPointY)/2

        self.otherX = tempxc - tempyd
        self.otherY = tempyc + tempxd
        self.otherX2 = tempxc + tempyd
        self.otherY2 = tempyc - tempxd

    def execute(self):
        self.drawingSave = self.canvasObject.create_line(self.x0, self.y0, self.x1, self.y1, dash=(2,4))

class Aggregation_Association(Command):
    def __init__(self,a,b,c,d,canvasObject):
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.diagPointX = self.x0
        self.diagPointY = self.y0
        self.otherX = 0
        self.otherY = 0
        self.otherX2 = 0
        self.otherY2 = 0
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.connections = []

    def getSlope(self):
        return float(self.y1-self.y0)/float(self.x1-self.x0)

    def getInterceptB(self):
        return self.y1 - (self.getSlope()*self.x1)

    def distance(self, x0, x1, y0, y1):
        return math.sqrt(math.pow((x0-x1),2)+math.pow((y0-y1),2))

    def getDiagonalPointFromStart(self):
        # diagPointX = self.x0
        # diagPointY = self.y0
        while self.distance(self.diagPointX, self.x0, self.diagPointY, self.y0)  < 10:
            if self.getSlope() < 0 and self.y0 < self.y1:
                self.diagPointX -= 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() < 0 and self.y0 > self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 < self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 > self.y1:
                self.diagPointX -=1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()

    def getOtherSquarePoints(self):
        tempxc = (self.x0+ self.diagPointX)/2
        tempyc = (self.y0+self.diagPointY)/2
        tempxd = (self.x0 - self.diagPointX)/2
        tempyd = (self.y0 - self.diagPointY)/2

        self.otherX = tempxc - tempyd
        self.otherY = tempyc + tempxd
        self.otherX2 = tempxc + tempyd
        self.otherY2 = tempyc - tempxd


    def execute(self):
        print "here is slope:", self.getSlope()

        self.getDiagonalPointFromStart()
        self.getOtherSquarePoints()
        self.drawingSave = self.canvasObject.create_line(self.x0, self.y0, self.x1, self.y1)
        self.canvasObject.create_polygon(self.x0, self.y0, self.otherX, self.otherY, self.diagPointX, self.diagPointY, self.otherX2, self.otherY2, fill='white',outline='black')

#class for COMPOSITION
class Composition_Association(Command):
    def __init__(self,a,b,c,d,canvasObject):
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.diagPointX = self.x0
        self.diagPointY = self.y0
        self.otherX = 0
        self.otherY = 0
        self.otherX2 = 0
        self.otherY2 = 0
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.connections = []

    def getSlope(self):
        return float(self.y1-self.y0)/float(self.x1-self.x0)

    def getInterceptB(self):
        return self.y1 - (self.getSlope()*self.x1)

    def distance(self, x0, x1, y0, y1):
        return math.sqrt(math.pow((x0-x1),2)+math.pow((y0-y1),2))

    def getDiagonalPointFromStart(self):
        # diagPointX = self.x0
        # diagPointY = self.y0
        while self.distance(self.diagPointX, self.x0, self.diagPointY, self.y0)  < 10:
            if self.getSlope() < 0 and self.y0 < self.y1:
                self.diagPointX -= 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() < 0 and self.y0 > self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 < self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 > self.y1:
                self.diagPointX -=1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()

    def getOtherSquarePoints(self):
        tempxc = (self.x0+ self.diagPointX)/2
        tempyc = (self.y0+self.diagPointY)/2
        tempxd = (self.x0 - self.diagPointX)/2
        tempyd = (self.y0 - self.diagPointY)/2

        self.otherX = tempxc - tempyd
        self.otherY = tempyc + tempxd
        self.otherX2 = tempxc + tempyd
        self.otherY2 = tempyc - tempxd


    def execute(self):
        self.getDiagonalPointFromStart()
        self.getOtherSquarePoints()
        self.drawingSave = self.canvasObject.create_line(self.x0, self.y0, self.x1, self.y1)
        self.canvasObject.create_polygon(self.x0, self.y0, self.otherX, self.otherY, self.diagPointX, self.diagPointY, self.otherX2, self.otherY2, fill='black',outline='black')


#now for the GENERALIZATION class
class Generalization_Association(Command):
    def __init__(self,a,b,c,d,canvasObject):
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.diagPointX = self.x0
        self.diagPointY = self.y0
        self.otherX = 0
        self.otherY = 0
        self.otherX2 = 0
        self.otherY2 = 0
        self.canvasObject = canvasObject
        self.drawingSave = None
        self.connections = []

    def getSlope(self):
        return float(self.y1-self.y0)/float(self.x1-self.x0)

    def getInterceptB(self):
        return self.y1 - (self.getSlope()*self.x1)

    def distance(self, x0, x1, y0, y1):
        return math.sqrt(math.pow((x0-x1),2)+math.pow((y0-y1),2))

    def getDiagonalPointFromStart(self):
        # diagPointX = self.x0
        # diagPointY = self.y0
        while self.distance(self.diagPointX, self.x0, self.diagPointY, self.y0)  < 20:
            if self.getSlope() < 0 and self.y0 < self.y1:
                self.diagPointX -= 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() < 0 and self.y0 > self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 < self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 > self.y1:
                self.diagPointX -=1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()

    def getDiagonalPointFromEnd(self):
        # diagPointX = self.x0
        # diagPointY = self.y0
        while self.distance(self.diagPointX, self.x0, self.diagPointY, self.y0)  > 10:
            if self.getSlope() < 0 and self.y0 < self.y1:
                self.diagPointX += 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() < 0 and self.y0 > self.y1:
                self.diagPointX -= 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 < self.y1:
                self.diagPointX -= 1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()
            elif self.getSlope() > 0 and self.y0 > self.y1:
                self.diagPointX +=1
                self.diagPointY = self.getSlope()*self.diagPointX+self.getInterceptB()

    def getOtherSquarePoints(self):
        tempxc = (self.x0+ self.diagPointX)/2
        tempyc = (self.y0+self.diagPointY)/2
        tempxd = (self.x0 - self.diagPointX)/2
        tempyd = (self.y0 - self.diagPointY)/2

        self.otherX = tempxc - tempyd
        self.otherY = tempyc + tempxd
        self.otherX2 = tempxc + tempyd
        self.otherY2 = tempyc - tempxd


    def execute(self):
        self.getDiagonalPointFromStart()
        self.getOtherSquarePoints()
        self.getDiagonalPointFromEnd()
        self.drawingSave = self.canvasObject.create_line(self.x0, self.y0, self.x1, self.y1)
        if self.getSlope() > 0:
            self.canvasObject.create_polygon(self.x0, self.y0, self.otherX, self.otherY, self.diagPointX, self.diagPointY, self.otherX2, self.otherY2, fill='white',outline='black')
        else:
            self.canvasObject.create_polygon(self.x0, self.y0, self.otherX2, self.otherY2, self.diagPointX, self.diagPointY, self.otherX, self.otherY, fill='white',outline='black')
#we need a command class for every one (adding this as we progress forward)

import Tkinter as tk
from Tkinter import *

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=800, height=700)
        self.x = self.y = 0
        self.drawingObjectArray = [0, 0, 0, 0, 0, 0, 0]

        self.valid_move = False
        self.moving_box = None
        self.classNameString = "default"

        #starting to prototype out some basic data structures (lists) for the main stack
        # and then i think we will make a command object class or something of the sort

        self.stackList = CommandStack()

        #the one that will support the undo
        self.realStackList = UndoStack()


        #list.pop() will remove the last thing form the list
        #list.append() will add to the stack


        self.diagram_name = Entry(self, foreground='grey')
        self.diagram_name.grid(row=0, column = 0)
        self.diagram_name.insert(0, "Enter a Diagram Name")
        self.diagram_name.bind("<ButtonPress-1>", self.diagram_name_user)

        self.class_button = Button(self, text='CLASS', command=self.create_class)
        self.class_button.grid(row=1, column=0)

        self.class_button_move = Button(self, text='MOVE CLASS', command=self.move_class_bit)
        self.class_button_move.grid(row=2, column=0)

        self.binary_association_button = Button(self, text='BINARY ASSOCIATION', command=self.create_binary_association)
        self.binary_association_button.grid(row=3, column=0)

        #open diamond solid line
        self.aggregation_button = Button(self, text='AGGREGATION', command=self.create_aggregation)
        self.aggregation_button.grid(row=4, column=0)

        #closed diamond solid line
        self.composition_button = Button(self, text='COMPOSITION', command=self.create_composition)
        self.composition_button.grid(row=5, column=0)

        #open triangle solid line
        self.generalization_button = Button(self, text='GENERALIZATION/\nSPECIALIZATION', command=self.create_generalization)
        self.generalization_button.grid(row=6, column=0)

        #dotted line with arrow arrow
        self.dependency_button = Button(self, text='DEPENDENCY', command=self.create_dependency)
        self.dependency_button.grid(row=7, column=0)

        self.pen_button = Button(self, text='CLEAR WORKSPACE', command=self.clear_canvas)
        self.pen_button.grid(row=8, column=0)

        self.undo_button = Button(self, text='UNDO', fg= 'red', command=self.undo_command)
        self.undo_button.grid(row=9, column=0)


        self.pen_button = Button(self, text='LOAD WORKSPACE', command=self.clear_canvas)
        self.pen_button.grid(row=0, column=1)

        self.save_button = Button(self, text='SAVE WORKSPACE', command=self.save_canvas)
        self.save_button.grid(row=0  , column=2)

        self.save_file_entry = Entry(self, foreground='grey')
        self.save_file_entry.grid(row=0, column = 3)
        self.save_file_entry.insert(0, "Enter a File Save Name...Click Save Button")
        self.save_file_entry.bind("<ButtonPress-1>", self.save_file_name_user)

        self.canvas = tk.Canvas(self, width=600, height=600, cursor="cross",borderwidth=3,background='white')
        self.canvas.grid(row=2,rowspan=20,column=1, columnspan=20,sticky=SW)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)


    def undo_command(self):
        self.realStackList.popOffExecutionChain()
        print 'checking undo button removes element correctly:'
        for i in self.realStackList.stack:
                print len(i.commands)
        print 'check complete'

        self.clear_canvas()
        self.realStackList.stack[-1].execute_commands()

    def save_file_name_user(self, event):
        self.save_file_entry.config(fg='black')
        self.save_file_entry.delete(0, "end")

    def save_canvas(self):
        text = self.save_button.get() + " " + e1.get() + "\n"
        with open("text.txt", "a") as f:
            f.write(text)

    def diagram_name_user(self, event):
        self.diagram_name.config(fg='black')
        self.diagram_name.delete(0, "end")

    def clear_canvas(self):
        self.canvas.delete("all")

    def clear_array(self):
        for i in range(0, len(self.drawingObjectArray)):
            self.drawingObjectArray[i] = 0

    def on_button_press(self, event):
        #self.x = event.x
        if self.drawingObjectArray[0] == 1:
            self.x = 80
            #self.y = event.y
            self.y = 80
            x0,y0 = (event.x, event.y)
            x1,y1 = (event.x+self.x, event.y+self.y)
            #this should be completely moved to within the execution portion of the class
            #classCanvas = self.canvas.create_rectangle(x0,y0,x1,y1)
            #print classCanvas
            # we need to pass in our canvas object
            classBox = Class_Box(x0,y0,x1,y1,self.canvas,self.classNameString)
            self.add_stack_push_sequence(classBox)
            #this will be the job of the invoker to store all of the commands and then execute them all if any changes occur (with a clear_canvas())
            # this will also be really nice because rather than doing the complicated coordinate changing, you would simply change the object and then when everything is re-drawn, it is just moved to the new location. easy. piece of cake


            #checking this is 2d for our simple squares
            for i in self.realStackList.stack:
                print len(i.commands)
            print self.stackList
            for i in self.stackList.commands:
                #ok so with this we can check the type of our classes (which is awesome)
                print isinstance(i, Class_Box)

        elif self.drawingObjectArray[1] == 1:
            if not self.valid_move:
                self.x = event.x
                self.y = event.y
                #now wanting to check if it is within any object
                for index, i in enumerate(self.stackList.commands):
                    if isinstance(i, Class_Box):
                        if self.check_bound(self.x, self.y, i):
                            print "You are in something!!!!"
                            self.valid_move = True
                            #this needs to be changed to an index value on the stack of commands
                            #so that editing it in the future is much much easier....
                            #because moving something twice won't work since i can't change the specific spot at which i need it to change and update
                            self.moving_box = i
                            self.moving_box_index = index
            elif self.valid_move:
                self.x = 80
                #self.y = event.y
                self.y = 80
                x0,y0 = (event.x, event.y)
                x1,y1 = (event.x+self.x, event.y+self.y)
                #need to update the commands and their parameters
                #hypothetically it should be pretty straight forward to pass this all into another class
                #which  will allow for the undo of moves as well (we need to add that button)
                self.canvas.coords(self.stackList.commands[self.moving_box_index].drawingSave, x0, y0, x1, y1)
                self.stackList.commands[self.moving_box_index].x0 = x0
                self.stackList.commands[self.moving_box_index].y0 = y0
                self.stackList.commands[self.moving_box_index].x1 = x1
                self.stackList.commands[self.moving_box_index].y1 = y1
                self.valid_move = False
                #need to reset stuff as well

        elif self.drawingObjectArray[2] == 1 or self.drawingObjectArray[6] == 1 or self.drawingObjectArray[3]==1 or self.drawingObjectArray[4]==1 or self.drawingObjectArray[5] == 1:
            self.x = event.x
            self.y = event.y

        # this can be put in a better spot, but making sure squares can be drawn right now
        # self.clear_canvas()
        # self.realStackList.stack[-1].execute_commands()

        #this needs to be better resolved for the flow of refreshing. it gets called too often here
    #self.refresh_canvas()
        #self.stackList.execute_commands()

    def on_button_release(self, event):
        if self.drawingObjectArray[0]!=1 and self.drawingObjectArray[1]!=1 and self.drawingObjectArray[2] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            #generating new command class
            binaryLine = Binary_Association(x0,y0,x1,y1,self.canvas)
            self.add_stack_push_sequence(binaryLine)

            # this is no longer needed:
            #self.canvas.create_line(x0,y0,x1,y1)
            for i in self.stackList.commands:
                if isinstance(i, Class_Box):
                    self.canvas.itemconfig(i.drawingSave,fill='white')
                    self.canvas.tag_raise(i.drawingSave)
                    print 'made it here'
            #possible use for an arrow, but it doesn't look anthing like the arrow we need so likely we won't be using this
            #arrow="last")
            #simply add this when we want a dashed line
            #dash=(2,4))

        elif self.drawingObjectArray[3] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)

            #adding lock to edge logic
            for index, i in enumerate(self.stackList.commands):
                if isinstance(i, Class_Box):
                    if self.check_bound(self.x, self.y, i):
                        print "You are in a box"
                        if y1 < i.y0:
                            y0 = i.y0
                        elif x1 > i.x1:
                            x0 = i.x1
                        elif y1 > i.y1:
                            y0 = i.y1
                        elif x1 < i.x0:
                            x0 = i.x0
                    if self.check_bound(x1,y1,i):
                        #one final sequence for the connections
                        if y0 < i.y0:
                            y1 = i.y0
                        elif x0 > i.x1:
                            x1 = i.x1
                        elif y0 > i.y1:
                            y1 = i.y1
                        elif x0 < i.x0:
                            x1 = i.x0

            #generating new command class
            aggregationLine = Aggregation_Association(x0,y0,x1,y1,self.canvas)
            self.add_stack_push_sequence(aggregationLine)

        elif self.drawingObjectArray[4] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            #adding lock to edge logic
            for index, i in enumerate(self.stackList.commands):
                if isinstance(i, Class_Box):
                    if self.check_bound(self.x, self.y, i):
                        print "You are in a box"
                        if y1 < i.y0:
                            y0 = i.y0
                        elif x1 > i.x1:
                            x0 = i.x1
                        elif y1 > i.y1:
                            y0 = i.y1
                        elif x1 < i.x0:
                            x0 = i.x0
                    if self.check_bound(x1,y1,i):
                        #one final sequence for the connections
                        if y0 < i.y0:
                            y1 = i.y0
                        elif x0 > i.x1:
                            x1 = i.x1
                        elif y0 > i.y1:
                            y1 = i.y1
                        elif x0 < i.x0:
                            x1 = i.x0
            #generating new command class
            compositionLine = Composition_Association(x0,y0,x1,y1,self.canvas)
            self.add_stack_push_sequence(compositionLine)

        elif self.drawingObjectArray[5] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            #adding lock to edge logic
            for index, i in enumerate(self.stackList.commands):
                if isinstance(i, Class_Box):
                    if self.check_bound(self.x, self.y, i):
                        print "You are in a box"
                        if y1 < i.y0:
                            y0 = i.y0
                        elif x1 > i.x1:
                            x0 = i.x1
                        elif y1 > i.y1:
                            y0 = i.y1
                        elif x1 < i.x0:
                            x0 = i.x0
                    if self.check_bound(x1,y1,i):
                        #one final sequence for the connections
                        if y0 < i.y0:
                            y1 = i.y0
                        elif x0 > i.x1:
                            x1 = i.x1
                        elif y0 > i.y1:
                            y1 = i.y1
                        elif x0 < i.x0:
                            x1 = i.x0
            #generating new command class
            generalizationLine = Generalization_Association(x0,y0,x1,y1,self.canvas)
            self.add_stack_push_sequence(generalizationLine)

        elif self.drawingObjectArray[6] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            #adding lock to edge logic
            for index, i in enumerate(self.stackList.commands):
                if isinstance(i, Class_Box):
                    if self.check_bound(self.x, self.y, i):
                        print "You are in a box"
                        if y1 < i.y0:
                            y0 = i.y0
                        elif x1 > i.x1:
                            x0 = i.x1
                        elif y1 > i.y1:
                            y0 = i.y1
                        elif x1 < i.x0:
                            x0 = i.x0
                    if self.check_bound(x1,y1,i):
                        #one final sequence for the connections
                        if y0 < i.y0:
                            y1 = i.y0
                        elif x0 > i.x1:
                            x1 = i.x1
                        elif y0 > i.y1:
                            y1 = i.y1
                        elif x0 < i.x0:
                            x1 = i.x0
            dashLine = Dependency_Association(x0, y0, x1, y1, self.canvas)
            self.add_stack_push_sequence(dashLine)
            #self.stackList.add_command(dashLine)

        self.refresh_canvas()
        # self.clear_canvas()
        # self.realStackList.stack[-1].execute_commands()
        #self.stackList.execute_commands()
        #so this is needed after every clear to make sure the stuff is on top which i don't like....
        #need to figure out how to encapsulate this
        for i in self.stackList.commands:
            if isinstance(i, Class_Box):
                self.canvas.itemconfig(i.drawingSave,fill='white')
                self.canvas.tag_raise(i.drawingSave)
                print 'made it here'


    def add_stack_push_sequence(self, command):
        self.stackList.add_command(command)
        #addition = self.stackList
        tempStackList = CommandStack()
        if len(self.realStackList.stack) > 0:
            for i in self.realStackList.stack[-1].commands:
                tempStackList.add_command(i)
        tempStackList.add_command(command)
        self.realStackList.addExecutionChainCommand(tempStackList)


    def refresh_canvas(self):
        self.clear_canvas()
        self.realStackList.stack[-1].execute_commands()
        for i in self.realStackList.stack[-1].commands:
            if isinstance(i, Class_Box):
                self.canvas.itemconfig(i.drawingSave,fill='white')
                self.canvas.tag_raise(i.drawingSave)

    def check_bound(self, x0, y0, classObject):
        print "point:", x0, y0
        print "square:", classObject.x0, classObject.y0, classObject.x1, classObject.y1
        if (x0 > classObject.x0 and x0 < classObject.x1) and (y0 > classObject.y0 and y0 < classObject.y1):
            return True
        else:
            return False

    def create_class(self):
        self.top = Toplevel()
        self.top.title("Class Creation...")
        msg = Message(self.top, text="Please enter a class name:")
        msg.pack()
        self.classEntry = Entry(self.top)
        self.classEntry.pack()
        enterButton = Button(self.top, text="ENTER", command=self.close_window)
        enterButton.pack()

        self.clear_array()
        self.drawingObjectArray[0]=1

    def move_class_bit(self):
        self.clear_array()
        self.drawingObjectArray[1] = 1

    def create_binary_association(self):
        self.clear_array()
        self.drawingObjectArray[2]=1

    def create_aggregation(self):
        self.clear_array()
        self.drawingObjectArray[3]=1

    def create_composition(self):
        self.clear_array()
        self.drawingObjectArray[4]=1

    def create_generalization(self):
        self.clear_array()
        self.drawingObjectArray[5]=1

    def create_dependency(self):
        self.clear_array()
        self.drawingObjectArray[6] = 1


    def close_window(self):
        self.classNameString = self.classEntry.get()
        self.top.destroy()



if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
