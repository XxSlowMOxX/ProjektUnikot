import curses

def main(stdscr):
	while True:
		stdscr.addstr(str(stdscr.getch()))
	


curses.wrapper(main)
