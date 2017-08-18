#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  maininterf.py
#  
#  Copyright 2017 q <q@q-X550CC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
	import tkinter
	tk=tkinter
	root=tk.Tk()
	root.title("Карточки")
	tk.Button(root, text="Новая колода").pack(expand=tk.YES, fill=tk.BOTH)
	tk.Button(root, text="Выбрать колоду").pack(expand=tk.YES, fill=tk.BOTH)
	tk.mainloop()
	return 0

if __name__ == '__main__':
    import sys
    print ("Открыт не тот файл")
    sys.exit(main(sys.argv))
