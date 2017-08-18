from tkinter import *
import functions
import windows

class newWin:
	def __init__(self, parent, name):
		self.parent=parent
		self.frame = Frame(parent)
		self.name=name
	
	def start(self):
		self.parent.title(self.name)
		self.frame.pack(expand=YES, fill=BOTH)
		self.parent.mainloop()
		
	def addButton(self, txt, conf="(expand=YES, fill=BOTH)"):
		btn=Button(self.frame, text=txt)
		exec("btn.pack"+conf)
		return btn
		
	def addLabel(self, txt, conf="(expand=YES, fill=BOTH)"):
		lbl=Label(self.frame, text=txt)
		exec("lbl.pack"+conf)
		return lbl
	def addEntry(self, conf="(expand=YES, fill=X)"):
		entr=Entry(self.frame)
		exec("entr.pack"+conf)
		return entr
	
		

class Card:
	def __init__(self, front, back):
		self.front=front
		self.back=back

class Deck:
	def __init__(self, name, reverse=0):
		self.name=name
		self.reverse=reverse
		self.cards=[]
		self.win=0
	def add(self, card):
		self.cards.append(card)
		
	def delete(self, card):
		self.cards.remove(card) 
		
	def back(self):
		functions.changeTk(self.win, windows.selectDeckWin)
		
	def makeDeckWin(self):
		
		print(self.name)
		self.win=newWin(windows.root, self.name)
		self.btnEdit=self.win.addButton("Редактировать")
		self.btnLearn=self.win.addButton("Учить")
		self.btnBack=self.win.addButton("Назад")
		self.btnBack.config(command=self.back)
		
		
		functions.changeTk(windows.selectDeckWin, self.win)
		
		
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
