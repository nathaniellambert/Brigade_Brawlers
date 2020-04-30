#### Brigade Brawlers ###

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox as mBox
import os

############################ Functions ############################


############################ Root Setup ############################
root = Tk()
root.title("Brigade Brawlers")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.geometry("1050x750")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

############################ Variables ############################
bg_main = "#%02x%02x%02x" % (247,219,151) #beige
fg_main = "#%02x%02x%02x" % (241,127,19) #orange

############################ Images ############################
path = "resources/"
img_controls = ImageTk.PhotoImage(Image.open(path+"controls.jpg"))
raw_boxer1 = Image.open(path+"boxer1.png")
raw_boxer1 = raw_boxer1.resize((raw_boxer1.size[0]*3, raw_boxer1.size[1]*3))
img_boxer1 = ImageTk.PhotoImage(raw_boxer1)

############################ Commands ############################
def doQuit(*args):
    #if mBox.askokcancel("Quit", "Do you want to quit?"):
    root.destroy()

############################ Frames ############################
root.config(bg=bg_main)
frame_top = Frame(root,highlightbackground=bg_main,highlightthickness=1)
frame_middle = Frame(root,highlightbackground=bg_main,highlightthickness=1)
frame_bottom = Frame(root,highlightbackground=bg_main,highlightthickness=1)

frame_top.pack(expand=True)
frame_middle.pack(expand=True)
frame_bottom.pack(expand=True)

############################ Labels ############################
gameTitle_Label = Label(frame_top,text="Brigade Brawlers",font="Verdana 40 bold",bg=bg_main)
menuFigure_Label = Label(frame_middle,image=img_boxer1,bg=bg_main)

############################ Radiobuttons ############################


############################ Buttons ############################
play_Button = Button(frame_bottom,text="Play",cursor="hand2",bg=fg_main,
    font="Verdana 28 bold",borderwidth=5,padx=10,pady=6,width=20)
controls_Button = Button(frame_bottom,text="Controls",cursor="hand2",bg=fg_main,
    font="Verdana 28 bold",borderwidth=5,padx=10,pady=6,width=20)

############################ Entries ############################


############################ Design Layout ############################
#frame_top Design Layout
gameTitle_Label.pack(expand=True)

#frame_middle Design Layout
menuFigure_Label.pack(expand=True)

#frame_bottom Design Layout
play_Button.pack(side=LEFT)
controls_Button.pack(side=RIGHT)

############################ Main Loop ############################
root.bind("<Control-q>",doQuit)
root.protocol("WM_DELETE_WINDOW", doQuit)
root.mainloop()
