from time import sleep
import curses, curses.panel


def make_block(h,l, y,x):
    win = curses.newwin(h,l, y,x)
    win.clear()
    win.border()
    return win


def test(stdscr):

    stdscr.refresh()
    while 1:
        h, w = stdscr.getmaxyx()

        stdscr.refresh()

        win1 = make_block(h - 20, w // 2 - 10, 5, 5)
        win2 = make_block(h - 10, w // 2 - 10, 5, 5 + w // 2)
        win3 = make_block(5, w - 10, h - 5, 5)
        curses.panel.update_panels()
        win1.refresh()
        win2.refresh()
        win3.refresh()

        key = stdscr.getch()

        win1.clear()
        win2.clear()
        win3.clear()
        stdscr.clear()



if __name__ == '__main__':
    curses.wrapper(test)