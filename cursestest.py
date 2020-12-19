import curses
from time import sleep
def main(stdscr):
    curses.cbreak()
    stdscr.clear()
    stdscr.keypad(True)
    stdscr.nodelay(True)

    while True:
        inp = stdscr.getch()
        if inp!= -1:
            
            stdscr.addstr(0,0,"You preseed"+ str(inp)+"      ") 
            stdscr.refresh()




curses.wrapper(main)
