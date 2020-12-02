from tkinter import *
from tkinter import filedialog
import tkinter

class EditWindow():
    def __init__(self):
        #--VARIABLES--#
        self.tk = Tk()
        self.version = "V0.1"
        self.width = 800
        self.height = 540
        self.currentFile = None
        self.currentFileVar = StringVar()
        self.tk.title(f"Pedit Version: {self.version} | {self.currentFile}")
        self.lastCheckedText = ""
        #--VARIABLES--#


        #--FRAMES--#
        self.masterFrame = Frame(self.tk, width=self.width, height=self.height, bg="#F0F0A4") #Yellowish
        self.menuFrame = Frame(self.masterFrame, width=self.width*0.05, height=self.height, bg="#E1E1E1")
        self.textFrame = Frame(self.masterFrame, width=self.width, height=self.height, bg="#ACFCFC") #Baby blue
        self.fileLabelFrame = Frame(self.textFrame, width=self.width, height=self.height*0.025, bg="#E1E1E1")
        #--FRAMES--#


        #--WIDGETS--#
        self.textScrollbarY = Scrollbar(self.textFrame)
        self.textArea = Text(self.textFrame, wrap='none', yscrollcommand=self.textScrollbarY.set, bg="#FBFBFB")
        self.newFileButton = Button(self.menuFrame, text="New File", command=self.NewFile, bg="#E1E1E1")
        self.openFileButton = Button(self.menuFrame, text="Open File", command=self.OpenFile, bg="#E1E1E1")
        self.saveFileButton = Button(self.menuFrame, text="Save File", command=self.SaveFile, bg="#E1E1E1")
        self.saveFileAsButton = Button(self.menuFrame, text="Save File As", command=self.SaveFileAs, bg="#E1E1E1")
        self.UpdateFileDisplayName(None)
        self.currentFileLabel = Label(self.fileLabelFrame, textvariable=self.currentFileVar, bg="#E1E1E1")
        
        #--WIDGETS--#


        #--ORGANIZATION--#
        Grid.rowconfigure(self.tk, 0, weight=1)
        Grid.columnconfigure(self.tk, 0, weight=1)
        
        Grid.rowconfigure(self.masterFrame, 0, weight=1)
        Grid.columnconfigure(self.masterFrame, 0, weight=1)
        Grid.columnconfigure(self.masterFrame, 1, weight=20)
        Grid.rowconfigure(self.textFrame, 0, weight=1)
        Grid.rowconfigure(self.textFrame, 1, weight=40)
        Grid.columnconfigure(self.textFrame, 0, weight=1)
        for i in range(20):
            Grid.rowconfigure(self.menuFrame, i, weight=1)
        Grid.columnconfigure(self.menuFrame, 0, weight=1)
        Grid.columnconfigure(self.fileLabelFrame, 0, weight=1)
        Grid.rowconfigure(self.fileLabelFrame, 0, weight=1)
        
        self.masterFrame.grid(row=0,column=0,sticky="nsew")
        self.menuFrame.grid(row=0,column=0,sticky="nsew")
        self.textFrame.grid(row=0,column=1,sticky="nsew")
        self.textArea.grid(row=1,column=0,sticky="nsew")
        self.newFileButton.grid(row=0,column=0,sticky="nsew")
        self.openFileButton.grid(row=1,column=0,sticky="nsew")
        self.saveFileButton.grid(row=2,column=0,sticky="nsew")
        self.saveFileAsButton.grid(row=3,column=0,sticky="nsew")
        self.fileLabelFrame.grid(row=0,column=0,sticky="nsew")
        self.currentFileLabel.grid(row=0,column=0,sticky="nsew")

        
        self.textScrollbarY.config(command=self.textArea.yview)
        #--ORGANIZATION--#


        #--BINDS--#
        self.textArea.bind('<KeyRelease>', self.CompareChanges)
        #--BINDS--#
        

        #--LOOP--#
        self.tk.mainloop()
        #--LOOP--#


    def CompareChanges(self, event=None):
        if not self.lastCheckedText == self.textArea.get('0.0','end'):
            self.lastCheckedText = self.textArea.get('0.0','end')
            self.saveFileButton.configure(background="#E0C1C1")
            self.saveFileAsButton.configure(background="#E0C1C1")
    def UpdateFileDisplayName(self, newVal):
        self.currentFile = newVal
        self.currentFileVar.set(f"File opened: {self.currentFile}")
        self.tk.title(f"Pedit Version: {self.version} | {self.currentFileVar.get()}")
    def NewFile(self):
        if not self.SaveFileAs() == "n/a":
            self.UpdateFileDisplayName(None)
            self.textArea.delete('0.0','end')
            self.saveFileButton.configure(bg="#E1E1E1")
            self.saveFileAsButton.configure(bg="#E1E1E1")
    def OpenFile(self):
        savedFile = filedialog.askopenfilename(title = "Open File", filetypes = (("Accepted File Types", "*.txt *.py *.pyw *.txt.backup *.py.backup *.pyw.backup"),("Normal Files", "*.txt *.py *.pyw"), ("Backup Files", "*.txt.backup *.py.backup *.pyw.backup")))
        if savedFile.strip() == "":
            savedFile = None
        if savedFile:
            self.UpdateFileDisplayName(savedFile)
            with open(self.currentFile, "r") as file:
                contents = file.read()
                self.textArea.delete('0.0','end')
                self.textArea.insert(INSERT, contents)
                self.saveFileButton.configure(bg="#E1E1E1")
                self.saveFileAsButton.configure(bg="#E1E1E1")
                print(len(contents.split('\n')))
        self.tk.focus_force()
    def SaveFile(self):
        if self.currentFile:
            with open(self.currentFile, "w") as file:
                file.write(self.textArea.get("0.0","end"))
                self.saveFileButton.configure(bg="#E1E1E1")
                self.saveFileAsButton.configure(bg="#E1E1E1")
        else:
            savedFile = filedialog.asksaveasfilename(title = "Save File", filetypes = (("Accepted File Types", "*.txt *.py *.pyw *.txt.backup *.py.backup *.pyw.backup"),("Normal Files", "*.txt *.py *.pyw"), ("Backup Files", "*.txt.backup *.py.backup *.pyw.backup")))
            if savedFile.strip() == "":
                savedFile = None
            if savedFile:
                self.UpdateFileDisplayName(savedFile)
                with open(savedFile,"w") as file:
                    file.write(self.textArea.get("0.0","end"))
                    self.saveFileButton.configure(bg="#E1E1E1")
                    self.saveFileAsButton.configure(bg="#E1E1E1")
    def SaveFileAs(self):
        savedFile = filedialog.asksaveasfilename(title = "Save File As...", filetypes = (("Accepted File Types", "*.txt *.py *.pyw *.txt.backup *.py.backup *.pyw.backup"),("Normal Files", "*.txt *.py *.pyw"), ("Backup Files", "*.txt.backup *.py.backup *.pyw.backup")))
        if savedFile.strip() == "":
            savedFile = None
            return "n/a"
        if savedFile:
            self.UpdateFileDisplayName(savedFile)
            with open(savedFile,"w") as file:
                file.write(self.textArea.get("0.0","end"))
                self.saveFileButton.configure(bg="#E1E1E1")
                self.saveFileAsButton.configure(bg="#E1E1E1")
        
window = EditWindow()


