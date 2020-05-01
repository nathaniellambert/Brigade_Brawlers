from tkinter import *
from tkinter import messagebox as mBox
from PIL import ImageTk, Image
import os

class Game(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.bg_main = "#%02x%02x%02x" % (247,219,151) #beige
        self.fg_main = "#%02x%02x%02x" % (241,127,19) #orange

        ############################ Root Setup ############################
        root = Toplevel()
        root.title("Brigade Brawlers")
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.geometry("990x595")

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
        root.geometry("+{}+{}".format(positionRight, positionDown))

        ############################ Commands ############################
        def doQuit(*args):
            #if mBox.askokcancel("Quit", "Are you sure you want to quit?"):
            root.destroy()

        ############################ Menus ############################
        mainMenu = Menu(root)
        root.config(menu=mainMenu)
        fileMenu = Menu(mainMenu,tearoff=0)
        mainMenu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Quit",command=doQuit,accelerator="Ctrl+Q")

        ############################ Design ############################
        self.frames = {}
        for F in (MainMenu, PlayerChooser, ControlsMenu):
            page_name = F.__name__
            frame = F(parent=root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainMenu")

        ############################ Main Loop ############################
        root.bind("<Control-q>",doQuit)
        root.mainloop()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        controller.withdraw()
        self.config(bg=controller.bg_main)

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=controller.bg_main,highlightthickness=1)
        frame_middle = Frame(self,highlightbackground=controller.bg_main,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=controller.bg_main,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middle.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Images ############################
        raw_boxer1 = Image.open("resources/boxer1.png")
        raw_boxer1 = raw_boxer1.resize((raw_boxer1.size[0]*3, raw_boxer1.size[1]*3))
        img_boxer1 = ImageTk.PhotoImage(raw_boxer1)

        ############################ Widgets ############################
        gameTitle_Label = Label(frame_top,text="Brigade Brawlers",
            font="Helvetica 40 bold italic underline",bg=controller.bg_main)
        menuFigure_Label = Label(frame_middle,image=img_boxer1,bg=controller.bg_main)
        menuFigure_Label.image = img_boxer1
        play_Button = Button(frame_bottom, text="Play",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("PlayerChooser"))
        controls_Button = Button(frame_bottom, text="Controls",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("ControlsMenu"))

        ############################ Design ############################
        #frame_top Design Layout
        gameTitle_Label.pack(expand=True)

        #frame_middle Design Layout
        menuFigure_Label.pack(expand=True)

        #frame_bottom Design Layout
        play_Button.pack(side=LEFT)
        controls_Button.pack(side=RIGHT)

class ControlsMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.bg_main)

        ############################ Images ############################
        raw_controls = Image.open("resources/controls.jpg")
        raw_controls = raw_controls.resize((900,500))
        img_controls = ImageTk.PhotoImage(raw_controls)

        ############################ Widgets ############################
        controls_Label = Label(self,image=img_controls,bg=controller.bg_main)
        controls_Label.image = img_controls
        return_button = Button(self, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("MainMenu"))

        ############################ Design ############################
        controls_Label.pack()
        return_button.pack(side=BOTTOM)

class PlayerChooser(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.bg_main)

        ############################ Widgets ############################
        return_button = Button(self, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Verdana 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("MainMenu"))
        return_button.pack(side=BOTTOM)

if __name__ == "__main__":
    #game = Game()
    #game.mainloop()
    Game()


"""
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))
"""
