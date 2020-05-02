from tkinter import *
from tkinter import messagebox as mBox
from PIL import ImageTk, Image
import testPygame

class Game(Tk):
    def __init__(self,state):
        Tk.__init__(self)

        self.state = state
        self.bg_main = "#%02x%02x%02x" % (247,219,151) #beige
        self.fg_main = "#%02x%02x%02x" % (241,127,19) #orange
        self.playerID = 1
        self.opponentID = 2
        self.playerPath = "resources/plebe/plebeStanding.png"
        self.opponentPath = "resources/dpe/dpeStanding.png"
        raw_player = Image.open(self.playerPath)
        raw_player = raw_player.resize((240,360))
        self.img_player = ImageTk.PhotoImage(raw_player)

        raw_opponent = Image.open(self.opponentPath)
        raw_opponent = raw_opponent.resize((240,360))
        self.img_opponent = ImageTk.PhotoImage(raw_opponent)

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
                  ChooseOpponentScreen,IdleScreen):
            page_name = F.__name__
            frame = F(parent=root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        if (self.state == "startup"):
            self.show_frame("MainScreen")
        if (self.state == "resume"):
            root.withdraw()
            self.show_frame("IdleScreen")

        ############################ Main Loop ############################
        root.bind("<Control-q>",doQuit)
        root.mainloop()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def runGame(self):
        testPygame.play_game(self.playerID,self.opponentID)

    def setPlayer(self,imageID):
        self.playerID = imageID
        if (imageID == 1):
            self.playerPath = "resources/plebe/plebeStanding.png"
        if (imageID == 2):
            self.playerPath = "resources/dpe/dpeStanding.png"
        if (imageID == 3):
            self.playerPath = "resources/supt/suptStanding.png"
        if (imageID == 4):
            self.playerPath = "resources/acu/acuStanding.png"
        raw_player = Image.open(self.playerPath)
        raw_player = raw_player.resize((240,360))
        self.img_player = ImageTk.PhotoImage(raw_player)
        frame = self.frames["IdleScreen"]
        frame.updatePlayerImage(self.img_player)

    def setOpponent(self,imageID):
        self.opponentID = imageID
        if (imageID == 1):
            self.opponentPath = "resources/plebe/plebeStanding.png"
        if (imageID == 2):
            self.opponentPath = "resources/dpe/dpeStanding.png"
        if (imageID == 3):
            self.opponentPath = "resources/supt/suptStanding.png"
        if (imageID == 4):
            self.opponentPath = "resources/acu/acuStanding.png"
        raw_opponent = Image.open(self.opponentPath)
        raw_opponent = raw_opponent.resize((240,360))
        self.img_opponent = ImageTk.PhotoImage(raw_opponent)
        frame = self.frames["IdleScreen"]
        frame.updateOpponentImage(self.img_opponent)

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
        controls_button.pack(side=LEFT)
        play_button.pack(side=RIGHT)

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
        back_button = Button(frame_bottom, text="Return to Menu",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=20,
            command=lambda: controller.show_frame("MainScreen"),activebackground=bgMain)

        ############################ Design ############################
        #frame_top Design Layout
        controlsTitle_label.pack(expand=True)

        #frame_middle Design Layout
        controls_label.pack(expand=True)

        #frame_bottom Design Layout
        back_button.pack(expand=True)

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
        raw_plebe1 = raw_plebe1.resize((200,300))
        img_plebe1 = ImageTk.PhotoImage(raw_plebe1)

        raw_dpe1 = Image.open("resources/dpe/dpeStanding.png")
        raw_dpe1 = raw_dpe1.resize((200,300))
        img_dpe1 = ImageTk.PhotoImage(raw_dpe1)

        raw_supt1 = Image.open("resources/supt/suptStanding.png")
        raw_supt1 = raw_supt1.resize((200,300))
        img_supt1 = ImageTk.PhotoImage(raw_supt1)

        raw_acu1 = Image.open("resources/acu/acuStanding.png")
        raw_acu1 = raw_acu1.resize((200,300))
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

        plebe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,value=1,variable=playerVar,
            padx=65,activebackground="white",indicatoron=0,text="Plebe",font="Helvetica 20 bold",
            command=lambda: controller.setPlayer(playerVar.get()))
        dpe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,value=2,variable=playerVar,
            padx=65,activebackground="white",indicatoron=0,text="DPE",font="Helvetica 20 bold",
            command=lambda: controller.setPlayer(playerVar.get()))
        supt1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,value=3,variable=playerVar,
            padx=65,activebackground="white",indicatoron=0,text="SUPT",font="Helvetica 20 bold",
            command=lambda: controller.setPlayer(playerVar.get()))
        acu1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,value=4,variable=playerVar,
            padx=65,activebackground="white",indicatoron=0,text="ACU",font="Helvetica 20 bold",
            command=lambda: controller.setPlayer(playerVar.get()))

        back_button = Button(frame_bottom, text="Back",cursor="hand2",
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
        back_button.pack(side=LEFT)
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
        raw_plebe1 = raw_plebe1.resize((200,300))
        img_plebe1 = ImageTk.PhotoImage(raw_plebe1)

        raw_dpe1 = Image.open("resources/dpe/dpeStanding.png")
        raw_dpe1 = raw_dpe1.resize((200,300))
        img_dpe1 = ImageTk.PhotoImage(raw_dpe1)

        raw_supt1 = Image.open("resources/supt/suptStanding.png")
        raw_supt1 = raw_supt1.resize((200,300))
        img_supt1 = ImageTk.PhotoImage(raw_supt1)

        raw_acu1 = Image.open("resources/acu/acuStanding.png")
        raw_acu1 = raw_acu1.resize((200,300))
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
            padx=65,activebackground="white",indicatoron=0,text="Plebe",font="Helvetica 20 bold",
            command=lambda: controller.setOpponent(opponentVar.get()))
        dpe1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=2,
            padx=65,activebackground="white",indicatoron=0,text="DPE",font="Helvetica 20 bold",
            command=lambda: controller.setOpponent(opponentVar.get()))
        supt1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=3,
            padx=65,activebackground="white",indicatoron=0,text="SUPT",font="Helvetica 20 bold",
            command=lambda: controller.setOpponent(opponentVar.get()))
        acu1_radiobutton = Radiobutton(frame_middleBottom,bg=fgMain,variable=opponentVar,value=4,
            padx=65,activebackground="white",indicatoron=0,text="ACU",font="Helvetica 20 bold",
            command=lambda: controller.setOpponent(opponentVar.get()))

        back_button = Button(frame_bottom, text="Go Back",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("ChoosePlayerScreen"),activebackground=bgMain)
        next_button = Button(frame_bottom, text="Next",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("IdleScreen"),activebackground=bgMain)

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
        back_button.pack(side=LEFT)
        next_button.pack(side=RIGHT)

class IdleScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        bgMain = controller.bg_main
        fgMain = controller.fg_main
        self.config(bg=bgMain)

        ############################ Frames ############################
        frame_top = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_middle = Frame(self,highlightbackground=bgMain,highlightthickness=1)
        frame_bottom = Frame(self,highlightbackground=bgMain,highlightthickness=1)

        frame_top.pack(expand=True)
        frame_middle.pack(expand=True)
        frame_bottom.pack(expand=True)

        ############################ Widgets ############################
        ready_label = Label(frame_top,text="Get Ready!",
            font="Helvetica 40 bold italic underline",bg=bgMain)

        self.player_label = Label(frame_middle,image=controller.img_player,bg=bgMain,height=374)
        self.player_label.image = controller.img_player
        self.opponent_label = Label(frame_middle,image=controller.img_opponent,bg=bgMain,height=374)
        self.opponent_label.image = controller.img_opponent

        vs_label = Label(frame_middle,text=" vs.",font="Helvetica 60 bold",bg=bgMain,height=4)

        back_button = Button(frame_bottom, text="Go Back",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.show_frame("ChooseOpponentScreen"),activebackground=bgMain)
        fight_button = Button(frame_bottom, text="Fight!",cursor="hand2",
            bg=controller.fg_main,font="Helvetica 28 bold",borderwidth=5,padx=10,pady=6,width=15,
            command=lambda: controller.runGame(),activebackground=bgMain)


        ############################ Design ############################
        #frame_top Design Layout
        ready_label.pack(expand=True)

        #frame_middle Design Layout
        self.player_label.grid(row=0,column=0)
        vs_label.grid(row=0,column=1)
        self.opponent_label.grid(row=0,column=2)

        #frame_bottom Design Layout
        back_button.pack(side=LEFT)
        fight_button.pack(side=RIGHT)

    def updatePlayerImage(self,img):
        self.player_label.config(image=img)

    def updateOpponentImage(self,img):
        self.opponent_label.config(image=img)

if __name__ == "__main__":
    state = "startup"
    Game(state)
