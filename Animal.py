#########################################
# Petie
# Assignment 1
# 9/25/2020
#
# Description: This program makes a picture of a whale that says, "Howdy, I'm a Whale!".
#########################################

from tkinter import *

#Setting up Window & Canvas
root = Tk()
root.geometry("300x250")
root.title("Petie was Here")
root.iconbitmap("./icon/petie.ico")
myCanvas = Canvas(root, width=300, height=250, bg="#31E8FF")

#Start Drawing...
myCanvas.create_line(50, 70, 40, 110, 50, 150, smooth="true")
myCanvas.create_line(50, 70, 110, 60, 170, 70, smooth="true")
myCanvas.create_line(50, 150, 120, 160, 180, 150, smooth="true")
myCanvas.create_line(180, 150, 200, 155, 220, 150, smooth="true")
myCanvas.create_line(220, 150, 230, 140, 240, 110, smooth="true")
myCanvas.create_line(210, 125, 230, 110, 200, 85, smooth="true")
myCanvas.create_line(240, 110, 250, 90, 270, 85, smooth="true")
myCanvas.create_line(200, 85, 235, 80, 270, 85, smooth="true")
myCanvas.create_line(170, 70, 180, 100, 210, 125, smooth="true")
myCanvas.create_line(47, 130, 80, 130, 100, 125, smooth="true")

#Make the Eyes
myCanvas.create_oval(65, 85, 75, 95, fill="black")

#Make a label
myCanvas.create_text(130, 180, fill="darkblue", font="Arial 15 bold",
                        text="Howdy, I'm a Whale!")

myCanvas.pack()
root.mainloop()
