import curses
import time

def main(stdscr):
    stdscr.nodelay(True)    
    while True:
        stdscr.addstr(0,0,str(stdscr.getch()))
        for i in range(3):
            stdscr.addstr(1,0,str(i))
            time.sleep(1)
            stdscr.refresh()
    stdscr.clear()

	


curses.wrapper(main)
