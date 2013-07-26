from tkinter import *
import time
import os

class JournalReader():
    #ROOT_DIR = r"C:/Users/Henry/Dropbox/Journal/"
    
    def __init__(self, root):
        
        self.leftFrame = Frame(root)
        self.leftFrame.pack(side=LEFT)

        intVar = IntVar()
        files = self.getOrderedFiles()
        i = 0
        for file in files:
            b=RadioButton(self.leftFrame, text=file, variable=v, value=i, indicatoron=0)
            i += 1
        
        self.rightFrame = Frame(root)
        self.rightFrame.pack(side=RIGHT)
        #goals = self.getPreviousGoals()
        self.goalsFrame = Frame(self.rightFrame)
        self.goalsFrame.grid(row=0, column=0)
        self.frame=Frame(self.rightFrame)
        self.frame.grid(row=1, column=0)
        self.shortGoalsLabel = Label(self.goalsFrame, text="Short Term Goals: ")
        self.shortGoalsLabel.grid(row=0, column=0)
        self.shortGoals =Text(self.goalsFrame, height=2)
        #self.shortGoals.insert(1.0, goals[0])
        self.shortGoals.bind("<Tab>", focus_next_window)
        self.shortGoals.grid(row=0, column=1)
        self.mediumGoalsLabel = Label(self.goalsFrame, text="Medium Term Goals: ")
        self.mediumGoalsLabel.grid(row=1, column=0)
        self.mediumGoals = Text(self.goalsFrame, height=2)
        #self.mediumGoals.insert(1.0, goals[1])
        self.mediumGoals.bind("<Tab>", focus_next_window)
        self.mediumGoals.grid(row=1, column=1)
        self.textArea = Text(self.frame, height = 20)
        self.textArea.grid(row=1, column=0)
        self.textArea.bind("<Tab>", focus_next_window)
        #self.button = Button(self.frame, text="Submit", command = self.onSubmit)
        #self.button.grid(row=2, column=0)

    def getOrderedFiles(self):
        files = os.listdir()
        unsortedEntries = []
        for file in files:
            if ".journal" in file:
                unsortedEntries += [file]
        if len(unsortedEntries) is 0:
            return ["",""]
        sortedFiles = sorted(unsortedEntries, reverse=True)
        return sortedFiles

    
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")
        
root = Tk()
app = JournalReader(root)
root.wm_title("Journal Reader")
root.mainloop()
