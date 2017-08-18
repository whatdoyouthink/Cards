from Classes import *
import pickle
d=Deck("test")
decks=[]
decks.append(d)
f= open("Date/date.pickle", "wb")
pikd=pickle.dumps(decks)
pickle.dump(pikd, f)
