from tkinter import *
import time
import os

class Journal():
    #ROOT_DIR = r"C:/Users/Henry/Dropbox/Journal/"
    
    def __init__(self, root):

        goals = self.getPreviousGoals()
        self.goalsFrame = Frame(root)
        self.goalsFrame.pack(side=TOP)
        self.frame=Frame(root, borderwidth=1, relief=SOLID)
        self.frame.pack(side=TOP)
        self.shortGoalsLabel = Label(self.goalsFrame, text="Short Term Goals: ")
        self.shortGoalsLabel.grid(row=0, column=0)
        self.shortGoals =Text(self.goalsFrame, height=2)
        self.shortGoals.insert(1.0, goals[0])
        self.shortGoals.bind("<Tab>", focus_next_window)
        self.shortGoals.grid(row=0, column=1)
        self.mediumGoalsLabel = Label(self.goalsFrame, text="Medium Term Goals: ")
        self.mediumGoalsLabel.grid(row=1, column=0)
        self.mediumGoals = Text(self.goalsFrame, height=2)
        self.mediumGoals.insert(1.0, goals[1])
        self.mediumGoals.bind("<Tab>", focus_next_window)
        self.mediumGoals.grid(row=1, column=1)
        self.textArea = Text(self.frame, height = 20)
        self.textArea.grid(row=1, column=0)
        self.textArea.bind("<Tab>", focus_next_window)
        self.button = Button(self.frame, text="Submit", command = self.onSubmit)
        self.button.grid(row=2, column=0)

    def onSubmit(self):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        f = open(timestamp + ".journal", 'w')
        f.write(' '.join(self.shortGoals.get(1.0, END).split("\n")) + "\n")
        f.write(' '.join(self.mediumGoals.get(1.0, END).split("\n")) + "\n")
        f.write(self.textArea.get(1.0, END))
        f.close()
        root.destroy()

    def getPreviousGoals(self):
        files = os.listdir()
        unsortedEntries = []
        for file in files:
            if ".journal" in file:
                unsortedEntries += [file]
        if len(unsortedEntries) is 0:
            return ["",""]
        sortedFiles = sorted(unsortedEntries, reverse=True)
        file = sortedFiles[0]
        f = open(file, 'r')
        retVal = [f.readline().replace("\n", ""), f.readline().replace("\n", "")]
        return retVal

    
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")
        
root = Tk()
app = Journal(root)
root.wm_title("Journal")
root.mainloop()
