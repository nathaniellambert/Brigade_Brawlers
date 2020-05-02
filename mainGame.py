from tkinter import *
from tkinter import messagebox as mBox
from PIL import ImageTk, Image
import os
import platform
import pygame, sys, random
from pygame.locals import *
import time

class Game(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        ############################ Colors ############################
        self.bg_main = "#%02x%02x%02x" % (247,219,151) #beige
        self.fg_main = "#%02x%02x%02x" % (241,127,19) #orange

        ############################ Root Setup ############################
        root = Toplevel()
        root.title("Brigade Brawlers")
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.geometry("990x570")

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
        root.geometry("+{}+{}".format(positionRight, positionDown))

        ############################ Commands ############################
        def doQuit(*args):
            #if mBox.askokcancel("Quit", "Are you sure you want to quit?"):
            pygame.quit()
            root.destroy()

        ############################ Menus ############################
        mainMenu = Menu(root)
        root.config(menu=mainMenu)
        fileMenu = Menu(mainMenu,tearoff=0)
        mainMenu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Quit",command=doQuit,accelerator="Ctrl+Q")

        ############################ Design ############################
        self.frames = {}
        for F in (MainScreen,ChoosePlayerScreen,ControlsScreen,ChoosePlayerScreen,
                  ChooseOpponentScreen,GameScreen):
            page_name = F.__name__
            frame = F(parent=root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainScreen")

        ############################ Main Loop ############################
        root.bind("<Control-q>",doQuit)
        root.mainloop()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class GameScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        bgMain = controller.bg_main
        self.config(bg=bgMain)

        ############################ Images ############################
        raw_gameBG = Image.open("resources/washingtonhall.png")
        raw_gameBG = raw_gameBG.resize((980,560))
        img_gameBG = ImageTk.PhotoImage(raw_gameBG)

        ############################ Frames ############################
        pygame_frame = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        pygame_frame.pack(expand=True)

        ############################ Widgets ############################
        background_label = Label(pygame_frame, image=img_gameBG)
        background_label.image = img_gameBG

        ############################ Design ############################
        background_label.pack()

        os.environ['SDL_WINDOWID'] = str(pygame_frame.winfo_id())
        system = platform.system()
        if system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
        elif system == "Linux":
            os.environ['SDL_VIDEODRIVER'] = 'x11'

        ############################ PyGame ############################
        screen = pygame.display.set_mode((200,200))
        pygame.display.init()

        pygame.display.update()

        """
        ############################ Widgets ############################
        return_button = Button(self, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("MainScreen"),activebackground=bgMain)

        ############################ Design ############################
        return_button.pack(side=BOTTOM)
        """


class MainScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        controller.withdraw()
        bgMain = controller.bg_main
        self.config(bg=bgMain)

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middle = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middle.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Images ############################
        raw_plebe1 = Image.open("resources/plebe/plebeReady.png")
        raw_plebe1 = raw_plebe1.resize((raw_plebe1.size[0]*3, raw_plebe1.size[1]*3))
        img_plebe1 = ImageTk.PhotoImage(raw_plebe1)

        ############################ Widgets ############################
        gameTitle_label = Label(frame_top,text="Brigade Brawlers",
            font="Helvetica 40 bold italic underline",bg=bgMain)
        menuFigure_label = Label(frame_middle,image=img_plebe1,bg=bgMain)
        menuFigure_label.image = img_plebe1
        play_button = Button(frame_bottom, text="Play",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("ChoosePlayerScreen"),activebackground=bgMain)
        controls_button = Button(frame_bottom, text="Controls",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("ControlsScreen"),activebackground=bgMain)

        ############################ Design ############################
        #frame_top Design Layout
        gameTitle_label.pack(expand=True)

        #frame_middle Design Layout
        menuFigure_label.pack(expand=True)

        #frame_bottom Design Layout
        play_button.pack(side=LEFT)
        controls_button.pack(side=RIGHT)

class ControlsScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        bgMain = controller.bg_main
        self.config(bg=bgMain)

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middle = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middle.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Images ############################
        raw_controls = Image.open("resources/controls.jpg")
        raw_controls = raw_controls.resize((700,400))
        img_controls = ImageTk.PhotoImage(raw_controls)

        ############################ Widgets ############################
        controlsTitle_label = Label(frame_top,text="Controls",
            font="Helvetica 40 bold italic underline",bg=bgMain)
        controls_label = Label(frame_middle,image=img_controls,bg=bgMain)
        controls_label.image = img_controls
        return_button = Button(frame_bottom, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("MainScreen"),activebackground=bgMain)

        ############################ Design ############################
        #frame_top Design Layout
        controlsTitle_label.pack(expand=True)

        #frame_middle Design Layout
        controls_label.pack(expand=True)

        #frame_bottom Design Layout
        return_button.pack(expand=True)

class ChoosePlayerScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        bgMain = controller.bg_main
        fgMain = controller.fg_main
        self.config(bg=bgMain)

        playerVar = IntVar()

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middleTop = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middleBottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middleTop.pack(expand=True)
        frame_middleBottom.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Images ############################
        raw_plebe1 = Image.open("resources/plebe/plebeStanding.png")
        raw_plebe1 = raw_plebe1.resize((200,240))
        img_plebe1 = ImageTk.PhotoImage(raw_plebe1)

        raw_dpe1 = Image.open("resources/dpe/dpeStanding.png")
        raw_dpe1 = raw_dpe1.resize((200,240))
        img_dpe1 = ImageTk.PhotoImage(raw_dpe1)

        raw_supt1 = Image.open("resources/supt/suptStanding.png")
        raw_supt1 = raw_supt1.resize((200,240))
        img_supt1 = ImageTk.PhotoImage(raw_supt1)

        raw_acu1 = Image.open("resources/acu/acuStanding.png")
        raw_acu1 = raw_acu1.resize((200,240))
        img_acu1 = ImageTk.PhotoImage(raw_acu1)

        ############################ Widgets ############################
        choosePlayer_label = Label(frame_top,text="Choose Your Brawler",
            font="Helvetica 40 bold italic underline",bg=bgMain,fg="blue")

        plebe1_label = Label(frame_middleTop,image=img_plebe1,bg=bgMain)
        plebe1_label.image = img_plebe1
        dpe1_label = Label(frame_middleTop,image=img_dpe1,bg=bgMain)
        dpe1_label.image = img_dpe1
        supt1_label = Label(frame_middleTop,image=img_supt1,bg=bgMain)
        supt1_label.image = img_supt1
        acu1_label = Label(frame_middleTop,image=img_acu1,bg=bgMain)
        acu1_label.image = img_acu1

        plebe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=playerVar,value=1,
            padx=65,activebackground="white",indicatoron=0,text="Plebe",font="Helvetica 20 bold")
        dpe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=playerVar,value=2,
            padx=65,activebackground="white",indicatoron=0,text="DPE",font="Helvetica 20 bold")
        supt1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=playerVar,value=3,
            padx=65,activebackground="white",indicatoron=0,text="SUPT",font="Helvetica 20 bold")
        acu1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=playerVar,value=4,
            padx=65,activebackground="white",indicatoron=0,text="ACU",font="Helvetica 20 bold")

        return_button = Button(frame_bottom, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("MainScreen"),activebackground=bgMain)
        next_button = Button(frame_bottom, text="Next",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("ChooseOpponentScreen"),activebackground=bgMain)

        ############################ Design ############################
        #frame_top Design Layout
        choosePlayer_label.pack(expand=True)

        #frame_middleTop Design Layout
        plebe1_label.grid(row=0,column=0)
        dpe1_label.grid(row=0,column=1)
        supt1_label.grid(row=0,column=2)
        acu1_label.grid(row=0,column=3)

        #frame_middleBottom Design Layout
        plebe1_radiobutton.grid(row=0,column=0)
        plebe1_radiobutton.select()
        dpe1_radiobutton.grid(row=0,column=1)
        supt1_radiobutton.grid(row=0,column=2)
        acu1_radiobutton.grid(row=0,column=3)

        #frame_bottom Design Layout
        return_button.pack(side=LEFT)
        next_button.pack(side=RIGHT)

class ChooseOpponentScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        bgMain = controller.bg_main
        fgMain = controller.fg_main
        self.config(bg=bgMain)

        opponentVar = IntVar()

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middleTop = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middleBottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middleTop.pack(expand=True)
        frame_middleBottom.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Images ############################
        raw_plebe1 = Image.open("resources/plebe/plebeStanding.png")
        raw_plebe1 = raw_plebe1.resize((200,240))
        img_plebe1 = ImageTk.PhotoImage(raw_plebe1)

        raw_dpe1 = Image.open("resources/dpe/dpeStanding.png")
        raw_dpe1 = raw_dpe1.resize((200,240))
        img_dpe1 = ImageTk.PhotoImage(raw_dpe1)

        raw_supt1 = Image.open("resources/supt/suptStanding.png")
        raw_supt1 = raw_supt1.resize((200,240))
        img_supt1 = ImageTk.PhotoImage(raw_supt1)

        raw_acu1 = Image.open("resources/acu/acuStanding.png")
        raw_acu1 = raw_acu1.resize((200,240))
        img_acu1 = ImageTk.PhotoImage(raw_acu1)

        ############################ Widgets ############################
        choosePlayer_label = Label(frame_top,text="Choose Your Opponent",
            font="Helvetica 40 bold italic underline",bg=bgMain,fg="red")

        plebe1_label = Label(frame_middleTop,image=img_plebe1,bg=bgMain)
        plebe1_label.image = img_plebe1
        dpe1_label = Label(frame_middleTop,image=img_dpe1,bg=bgMain)
        dpe1_label.image = img_dpe1
        supt1_label = Label(frame_middleTop,image=img_supt1,bg=bgMain)
        supt1_label.image = img_supt1
        acu1_label = Label(frame_middleTop,image=img_acu1,bg=bgMain)
        acu1_label.image = img_acu1

        plebe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=1,
            padx=65,activebackground="white",indicatoron=0,text="Plebe",font="Helvetica 20 bold")
        dpe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=2,
            padx=65,activebackground="white",indicatoron=0,text="DPE",font="Helvetica 20 bold")
        supt1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=3,
            padx=65,activebackground="white",indicatoron=0,text="SUPT",font="Helvetica 20 bold")
        acu1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=4,
            padx=65,activebackground="white",indicatoron=0,text="ACU",font="Helvetica 20 bold")

        return_button = Button(frame_bottom, text="Go Back",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("ChoosePlayerScreen"),activebackground=bgMain)
        next_button = Button(frame_bottom, text="Fight!",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("GameScreen"),activebackground=bgMain)

        ############################ Design ############################
        #frame_top Design Layout
        choosePlayer_label.pack(expand=True)

        #frame_middleTop Design Layout
        plebe1_label.grid(row=0,column=0)
        dpe1_label.grid(row=0,column=1)
        supt1_label.grid(row=0,column=2)
        acu1_label.grid(row=0,column=3)

        #frame_middleBottom Design Layout
        plebe1_radiobutton.grid(row=0,column=0)
        plebe1_radiobutton.select()
        dpe1_radiobutton.grid(row=0,column=1)
        supt1_radiobutton.grid(row=0,column=2)
        acu1_radiobutton.grid(row=0,column=3)

        #frame_bottom Design Layout
        return_button.pack(side=LEFT)
        next_button.pack(side=RIGHT)

if __name__ == "__main__":
    Game()


"""
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))
"""
