from tkinter import *
from Data import *
from tkinter import *
from Data import *


class WindMillPlayGame:
    def __init__(self):
        self.state= "Progreso"

    def posicionandoFicha(self, object, event):
        if object.change:
            for i in position_list:
                if i.in_the_radio(event.x, event.y) and i.empty:
                    i.empty = False
                    object.a = PhotoImage(file="piece.png")
                    object.id = object.canvas.create_image(event.x, event.y, image=object.a)
                    object.lista.append([object.id,event.x,event.y])
                    object.change = False
                    object.a.name = object.a.name + "1"
                    object.count += 1
                    print(object.count)
        else:
            for i in position_list:
                if i.in_the_radio(event.x, event.y) and i.empty:
                    i.empty = False
                    if object.count >= 4:
                        object.change = True
                        object.window.bind('<Button-1>', object.moviendoFicha)
                        object.a = PhotoImage(file="piece2.png")
                        object.id = object.canvas.create_image(event.x, event.y, image=object.a)
                        object.lista.append([object.id,event.x,event.y])
                        object.a.name = object.a.name + "1"

                    else:
                        object.a = PhotoImage(file="piece2.png")
                        object.id = object.canvas.create_image(event.x, event.y, image=object.a)
                        object.lista.append([object.id,event.x,event.y])
                        object.change = True
                        object.a.name = object.a.name + "1"
                        object.count += 1
                    print(object.count)


