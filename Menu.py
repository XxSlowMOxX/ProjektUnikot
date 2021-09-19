import curses

def menu(options):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(False)
    stdscr.clear()

    def select(index):
        i = 0
        for option in options:
            stdscr.addstr((i*2)+1, 0, "  " + option + "   ")
            stdscr.addstr(i*2,0,(len(options[i]) + 5) * " ")
            stdscr.addstr((i*2) + 2,0,(len(options[i]) + 5) * " ")
            stdscr.addstr((i*2) + 1,0," ")
            stdscr.addstr((i*2) + 1,len(options[i]) + 4, " ")
            i = i+1

        stdscr.addstr(index*2,0,(len(options[index]) + 5) * "#")
        stdscr.addstr((index*2) + 2,0,(len(options[index]) + 5) * "#")
        stdscr.addstr((index*2) + 1,0,"#")
        stdscr.addstr((index*2) + 1,len(options[index]) + 4, "#")
        stdscr.refresh()

    current = 0
    select(current)
    while True:
        num = stdscr.getch()
        if (num == 258):
            current = current + 1
        elif (num == 259):
            current = current - 1
        elif (num == 10):
            break
        select(current%len(options))
    return current




#258 = runter
#259 = hoch
#10 = Enter

stdscr = curses.initscr()
menu(["Singleplayer", "Multiplayer", "Optionen", "Ist das nicht cool?"])
