from Classes import *
import windows
import pickle
def changeTk(win1, win2):
	win1.frame.pack_forget()
	win2.start()
	return 0

def newDeck(name):
	deck=Deck(name)
	f = open("Date/date.pickle", "rb")
	decks=pickle.load(f)
	decks=pickle.loads(decks)
	decks.append(deck)
	f.close()
	f = open("Date/date.pickle", "wb")
	pikd=pickle.dumps(decks)
	pickle.dump(pikd, f)
	f.close()
	print("Колода с именем")
	print(deck.name)
	changeTk(windows.newDeckWin, windows.mainWin)

def showDecks():
	f = open("Date/date.pickle", "rb")
	decks=pickle.load(f)
	decks=pickle.loads(decks)
	f.close()
	windows.selectDeckWin.btnShowDecks.pack_forget()
	for i in decks:
		windows.selectDeckWin.btn=windows.selectDeckWin.addButton(i.name)
		windows.selectDeckWin.btn.config(command=i.makeDeckWin)
def main(args):
	return 0

if __name__ == '__main__':
    import sys
    print ("Открыт файл со вспомогательными функциями")
    sys.exit(main(sys.argv))
