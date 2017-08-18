import windows
from bindToBtns import binding
def main(args):
	binding()
	windows.mainWin.start()
	
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
