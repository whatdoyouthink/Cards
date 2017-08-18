import windows
from functions import *
def binding():
	windows.mainWin.btnNewDeck.config(command=lambda: changeTk(windows.mainWin, windows.newDeckWin))
	windows.mainWin.btnSelectDeck.config(command=lambda: changeTk(windows.mainWin, windows.selectDeckWin))
	windows.selectDeckWin.backBtn.config(command=lambda: changeTk(windows.selectDeckWin, windows.mainWin))
	
	windows.newDeckWin.btnGo.config(command=lambda:newDeck(windows.newDeckWin.entr.get()))
	
	windows.selectDeckWin.btnShowDecks.config(command=showDecks)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
