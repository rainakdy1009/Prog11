from tkinter import *

root = Tk()

w = Label(root, text="Ford vs Ferrari")
w.pack()


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command = frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.question = Button(
            frame, text= "Ask a question to Mr.Ford!", fg='orange', command=self.ask_q
            )
        self.question.pack(side=LEFT)

        self.value = Button(frame, text="?", fg= 'purple', command=self.boring)
        self.value.pack(side=LEFT)

        self.quessWhat = Button(frame, text="셰인 포드", fg= 'green', command=self.korean)
        self.quessWhat.pack(side=LEFT)

        self.x = Button(frame, text="안녕하세요", fg='blue', command = self.greeting)
        self.x.pack(side=LEFT)


    def say_hi(self):
        print("Hi there, Mr.Ford")

    def ask_q(self):
        print("What is our assignment today?")

    def boring(self):
        print("I like python")

    def korean(self):
        print("It's 'Shane Ford' in Korean")

    def greeting(self):
        print("It means 'Hello' in Korean (an-niong-ha-se-yo)")


app = App(root)

root.mainloop()
root.destroy()

##from tkinter import *
##
##root = Tk()
##
##root.geometry("400x300")
##
##class Window(Frame):
##
##    def __init__(self, master = None):
##
##        Frame.__init__(self, master)
##
##        self.master = master
##
##        self.init_window()
##
##    def init_window(self):
##
##        self.master.title("GUI")
##
##        self.pack(fill=BOTH, expand=1)
##
##        quitButton = Button(self, text="Exit", command = self.client_exit)
##
##        quitButton.place(x=0, y=0)
##
##    def client_exit(self):
##        exit()
##
##app = Window(root)
##
##root.mainloop()
