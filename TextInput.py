import curses
import curses.textpad as textpad

def TextInput(stdscr, field, width=10):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(False)
    stdscr.clear()
    curses.noecho()

    textwin = stdscr.subwin(1,width, int(stdscr.getmaxyx()[0]/2), int(stdscr.getmaxyx()[1]/2)- int(width/2))

    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) + 2, int(stdscr.getmaxyx()[1] / 2) - int(width / 2) - 2,
                  "+" * (width + 3))
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) - 2, int(stdscr.getmaxyx()[1] / 2) - int(width / 2) - 2,
                  "+" * (width + 3))
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) - 2, int(stdscr.getmaxyx()[1] / 2) - int(len(field) / 2),
                  field)

    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) , int(stdscr.getmaxyx()[1] / 2) - int(width / 2) - 2, "#")
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) + 1, int(stdscr.getmaxyx()[1] / 2) - int(width / 2) - 2, "#")
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) - 1, int(stdscr.getmaxyx()[1] / 2) - int(width / 2) - 2, "#")
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2), int(stdscr.getmaxyx()[1] / 2) + int(width / 2), "#")
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) + 1, int(stdscr.getmaxyx()[1] / 2) + int(width / 2), "#")
    stdscr.addstr(int(stdscr.getmaxyx()[0] / 2) - 1, int(stdscr.getmaxyx()[1] / 2) + int(width / 2), "#")

    stdscr.refresh()
    pad = textpad.Textbox(textwin).edit()

    stdscr.nodelay(False)
    return pad
