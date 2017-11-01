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




import Tkinter as tk
from Tkinter import *

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.drawingObjectArray = [0, 0, 0, 0, 0, 0]
        self.class_button = Button(self, text='CLASS', command=self.create_class)
        self.class_button.grid(row=0, column=0)

        self.binary_association_button = Button(self, text='BINARY ASSOCIATION', command=self.create_binary_association)
        self.binary_association_button.grid(row=1, column=0)

        self.pen_button = Button(self, text='AGGREGATION', command=self.create_class)
        self.pen_button.grid(row=2, column=0)

        self.pen_button = Button(self, text='COMPOSITION', command=self.create_class)
        self.pen_button.grid(row=3, column=0)

        self.pen_button = Button(self, text='GENERALIZATION/\nSPECIALIZATION', command=self.create_class)
        self.pen_button.grid(row=4, column=0)

        self.pen_button = Button(self, text='DEPENDENCY', command=self.create_class)
        self.pen_button.grid(row=5, column=0)

        self.pen_button = Button(self, text='CLEAR WORKSPACE', command=self.clear_canvas)
        self.pen_button.grid(row=6, column=0)

        self.canvas = tk.Canvas(self, width=400, height=400, cursor="cross")
        self.canvas.grid(row=0,rowspan=10,column=1)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)


    def clear_canvas(self):
        self.canvas.delete("all")

    def clear_array(self):
        for i in range(0, len(self.drawingObjectArray)):
            self.drawingObjectArray[i] = 0

    def on_button_press(self, event):
        #self.x = event.x
        if self.drawingObjectArray[0] == 1:
            self.x = 40
            #self.y = event.y
            self.y = 40
            x0,y0 = (event.x+self.x, event.y+self.y)
            x1,y1 = (event.x, event.y)
            self.canvas.create_rectangle(x0,y0,x1,y1)

        elif self.drawingObjectArray[1] == 1:
            self.x = event.x
            self.y = event.y

    def on_button_release(self, event):
        if self.drawingObjectArray[0]!=1:
            x0,y0 = (self.x, self.y)
            x1,y1 = (event.x, event.y)
            self.canvas.create_line(x0,y0,x1,y1)

    def create_class(self):
        self.clear_array()
        self.drawingObjectArray[0]=1

    def create_binary_association(self):
        self.clear_array()
        self.drawingObjectArray[1]=1




if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
