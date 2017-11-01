# Jake Felzien
# a02019985
# sample code for python

# from Tkinter import *
#
# canvas_width = 500
# canvas_height = 150
#
# def paint( event ):
#    python_green = "#476042"
#    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
#    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
#    w.create_oval( x1, y1, x2, y2, fill = python_green )
#
# master = Tk()
# master.title( "Painting using Ovals" )
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w.pack(expand = YES, fill = BOTH)
# w.bind( "<B1-Motion>", paint )
#
# message = Label( master, text = "Press and Drag the mouse to draw" )
# message.pack( side = BOTTOM )
#
# mainloop()

#
# root = Tk()
#
# def hello():
#     print "hello!"
#
# menubar = Menu(root)
#
# # create a pulldown menu, and add it to the menu bar
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Open", command=hello)
# filemenu.add_command(label="Save", command=hello)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
#
# # create more pulldown menus
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Cut", command=hello)
# editmenu.add_command(label="Copy", command=hello)
# editmenu.add_command(label="Paste", command=hello)
# menubar.add_cascade(label="Edit", menu=editmenu)
#
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="About", command=hello)
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# mainloop()
#
#
# from Tkinter import *
# from tkColorChooser import askcolor
# __author__ = 'Chuntao Lu'
#
#
# class Paint(object):
#
#     DEFAULT_PEN_SIZE = 5.0
#     DEFAULT_COLOR = 'black'
#
#     def __init__(self):
#         self.root = Tk()
#
#         self.pen_button = Button(self.root, text='pen', command=self.use_pen)
#         self.pen_button.grid(row=0, column=0)
#
#         self.brush_button = Button(self.root, text='brush', command=self.use_brush)
#         self.brush_button.grid(row=0, column=1)
#
#         self.color_button = Button(self.root, text='color', command=self.choose_color)
#         self.color_button.grid(row=0, column=2)
#
#         self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
#         self.eraser_button.grid(row=0, column=3)
#
#         self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
#         self.choose_size_button.grid(row=0, column=4)
#
#         self.c = Canvas(self.root, bg='white', width=600, height=600)
#         self.c.grid(row=1, columnspan=5)
#
#         self.setup()
#         self.root.mainloop()
#
#     def setup(self):
#         self.old_x = None
#         self.old_y = None
#         self.line_width = self.choose_size_button.get()
#         self.color = self.DEFAULT_COLOR
#         self.eraser_on = False
#         self.active_button = self.pen_button
#         self.c.bind('<B1-Motion>', self.paint)
#         self.c.bind('<ButtonRelease-1>', self.reset)
#
#     def use_pen(self):
#         self.activate_button(self.pen_button)
#
#     def use_brush(self):
#         self.activate_button(self.brush_button)
#
#     def choose_color(self):
#         self.eraser_on = False
#         self.color = askcolor(color=self.color)[1]
#
#     def use_eraser(self):
#         self.activate_button(self.eraser_button, eraser_mode=True)
#
#     #TODO: reset canvas
#     #TODO: undo and redo
#     #TODO: draw triangle, rectangle, oval, text
#
#     def activate_button(self, some_button, eraser_mode=False):
#         self.active_button.config(relief=RAISED)
#         some_button.config(relief=SUNKEN)
#         self.active_button = some_button
#         self.eraser_on = eraser_mode
#
#     def paint(self, event):
#         self.line_width = self.choose_size_button.get()
#         paint_color = 'white' if self.eraser_on else self.color
#         if self.old_x and self.old_y:
#             self.c.create_line(self.old_x, self.old_y, event.x, event.y,
#                                width=self.line_width, fill=paint_color,
#                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
#         self.old_x = event.x
#         self.old_y = event.y
#
#     def reset(self, event):
#         self.old_x, self.old_y = None, None
#
#
# if __name__ == '__main__':
#     ge = Paint()

class Command():
    def __init__(self):
        pass


class Class_Box(Command):
    def __init__(self, a, b, c, d, canvasObject):
        # we may actually only need two points for this rectangle (because it is just the upper left corner and the bottom corner)
        #can we do all of the algorithmic stuff off of this... we should
        self.x0 = a
        self.y0 = b
        self.x1 = c
        self.y1 = d
        self.canvasObject = canvasObject
        # we actually don't need this because the coordinate system essentially houses our four points, and thus what everything is conatined within
        # self.x3 = 0
        # self.y3 = 0
        # self.x4 = 0
        # self.y4 = 0
        self.connections = []

class Binary_Association(Command):
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.connections = []

#we need a command class for every one (adding this as we progress forward)

import Tkinter as tk
from Tkinter import *

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=700, height=700)
        self.x = self.y = 0
        self.drawingObjectArray = [0, 0, 0, 0, 0, 0, 0]

        self.valid_move = False
        self.moving_box = None

        #starting to prototype out some basic data structures (lists) for the main stack
        # and then i think we will make a command object class or something of the sort

        self.stackList = []
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
        self.pen_button = Button(self, text='AGGREGATION', command=self.create_class)
        self.pen_button.grid(row=4, column=0)

        #closed diamond solid line
        self.pen_button = Button(self, text='COMPOSITION', command=self.create_class)
        self.pen_button.grid(row=5, column=0)

        #open triangle solid line
        self.pen_button = Button(self, text='GENERALIZATION/\nSPECIALIZATION', command=self.create_class)
        self.pen_button.grid(row=6, column=0)

        #dotted line with arrow arrow
        self.dependency_button = Button(self, text='DEPENDENCY', command=self.create_dependency)
        self.dependency_button.grid(row=7, column=0)

        self.pen_button = Button(self, text='CLEAR WORKSPACE', command=self.clear_canvas)
        self.pen_button.grid(row=8, column=0)

        self.pen_button = Button(self, text='LOAD WORKSPACE', command=self.clear_canvas)
        self.pen_button.grid(row=0, column=1)

        self.save_button = Button(self, text='SAVE WORKSPACE', command=self.save_canvas)
        self.save_button.grid(row=0  , column=2)

        self.save_file_entry = Entry(self, foreground='grey')
        self.save_file_entry.grid(row=0, column = 3)
        self.save_file_entry.insert(0, "Enter a File Save Name...Click Save Button")
        self.save_file_entry.bind("<ButtonPress-1>", self.save_file_name_user)

        self.canvas = tk.Canvas(self, width=400, height=400, cursor="cross",borderwidth=3,background='white')
        self.canvas.grid(row=2,rowspan=20,column=1, columnspan=20,sticky=SW)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)



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
            classCanvas = self.canvas.create_rectangle(x0,y0,x1,y1)
            print classCanvas
            # we need to pass in our canvas object
            classBox = Class_Box(x0,y0,x1,y1,classCanvas)
            #this will be the job of the invoker to store all of the commands and then execute them all if any changes occur (with a clear_canvas())
            # this will also be really nice because rather than doing the complicated coordinate changing, you would simply change the object and then when everything is re-drawn, it is just moved to the new location. easy. piece of cake
            self.stackList.append(classBox)
            print self.stackList
            for i in self.stackList:
                #ok so with this we can check the type of our classes (which is awesome)
                print isinstance(i, Class_Box)
        elif self.drawingObjectArray[1] == 1:
            if not self.valid_move:
                self.x = event.x
                self.y = event.y
                #now wanting to check if it is within any object
                for index, i in enumerate(self.stackList):
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
                self.canvas.coords(self.stackList[self.moving_box_index].canvasObject, x0, y0, x1, y1)
                self.stackList[self.moving_box_index].x0 = x0
                self.stackList[self.moving_box_index].y0 = y0
                self.stackList[self.moving_box_index].x1 = x1
                self.stackList[self.moving_box_index].y1 = y1
                self.valid_move = False
                #need to reset stuff as well

        elif self.drawingObjectArray[2] == 1 or self.drawingObjectArray[6] == 1:
            self.x = event.x
            self.y = event.y

    def on_button_release(self, event):
        if self.drawingObjectArray[0]!=1 and self.drawingObjectArray[1]!=1 and self.drawingObjectArray[2] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            self.canvas.create_line(x0,y0,x1,y1)
            for i in self.stackList:
                if isinstance(i, Class_Box):
                    self.canvas.itemconfig(i.canvasObject,fill='white')
                    self.canvas.tag_raise(i.canvasObject)
                    print 'made it here'
            #possible use for an arrow, but it doesn't look anthing like the arrow we need so likely we won't be using this
            #arrow="last")
            #simply add this when we want a dashed line
            #dash=(2,4))

        elif self.drawingObjectArray[6] == 1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            self.canvas.create_line(x0,y0,x1,y1, dash=(2,4))
            for i in self.stackList:
                if isinstance(i, Class_Box):
                    self.canvas.itemconfig(i.canvasObject,fill='white')
                    self.canvas.tag_raise(i.canvasObject)
                    print 'made it here'

    def check_bound(self, x0, y0, classObject):
        print "point:", x0, y0
        print "square:", classObject.x0, classObject.y0, classObject.x1, classObject.y1
        if (x0 > classObject.x0 and x0 < classObject.x1) and (y0 > classObject.y0 and y0 < classObject.y1):
            return True
        else:
            return False

    def create_class(self):
        self.clear_array()
        self.drawingObjectArray[0]=1

    def create_binary_association(self):
        self.clear_array()
        self.drawingObjectArray[2]=1

    def move_class_bit(self):
        self.clear_array()
        self.drawingObjectArray[1] = 1

    def create_dependency(self):
        self.clear_array()
        self.drawingObjectArray[6] = 1




if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
