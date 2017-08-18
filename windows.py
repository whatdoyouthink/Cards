from tkinter import *
from Classes import newWin
root=Tk()

mainWin=newWin(root, "Карточки")
mainWin.btnNewDeck=mainWin.addButton("Новая колода")
mainWin.btnSelectDeck=mainWin.addButton("Выбрать колоду")


selectDeckWin=newWin(root, "Выбор колоды")
selectDeckWin.btnShowDecks=selectDeckWin.addButton("Показать колоды")
selectDeckWin.backBtn=selectDeckWin.addButton("На главную")

newDeckWin=newWin(root, "Новая колода")
newDeckWin.addLabel("Введите имя новой колоды")
newDeckWin.entr=newDeckWin.addEntry()
newDeckWin.btnGo=newDeckWin.addButton("Готово")

def main(args):
	
	return 0

if __name__ == '__main__':
    import sys
    print ("Запущен файл содержащий интерфейс основных окон")
    sys.exit(main(sys.argv))
