from tkinter import *
from Data import *

def moviendoFichita(object, event):
    if  object.change:
        print(object.lista)
        print(event.x, event.y)
    else:
        print(event.x, event.y)

def posicionandoFicha(object, event):
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

    else:
        for i in position_list:
            if i.in_the_radio(event.x, event.y) and i.empty:
                i.empty = False
                if object.count >= 16:
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
