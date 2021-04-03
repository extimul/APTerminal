import curses as crs


def run():
    screen = crs.initscr()
    crs.start_color()
    crs.use_default_colors()
    if crs.can_change_color():
        crs.init_color(1, 1000, 0, 0)
        crs.init_color(2, 0, 1000, 0)
        crs.init_color(3, 1000, 1000, 0)
        crs.init_color(4, 0, 0, 1000)
        crs.init_color(5, 1000, 500, 1000)
        crs.init_color(6, 500, 500, 1000)
        crs.init_color(7, 1000, 750, 325)

    crs.init_pair(1, -1, 1)
    crs.init_pair(2, -1, 2)
    crs.init_pair(3, -1, 3)
    crs.init_pair(4, -1, 4)
    crs.init_pair(5, -1, 5)
    crs.init_pair(6, -1, 6)
    crs.init_pair(7, -1, 7)

    crs.noecho()
    crs.cbreak()
    crs.curs_set(0)

    wTitle = crs.newwin(6, 19, 0, 4)
    wScore = crs.newwin(4, 17, 6, 5)
    wCntrl = crs.newwin(14, 23, 10, 2)
    wBoard = crs.newwin(24, 22, 0, 27)
    wBoard.keypad(True)
    wBoard.nodelay(True)
    wNextP = crs.newwin(7, 19, 0, 51)
    wStats = crs.newwin(17, 19, 7, 51)
    # Draw boarders of windows
    wTitle.border()
    wScore.border()
    wCntrl.border()
    wBoard.border()
    wNextP.border()
    wStats.border()

    wTitle.refresh()
    wScore.refresh()
    wCntrl.refresh()
    wBoard.refresh()
    wNextP.refresh()
    wStats.refresh()

    crs.napms(10000)
    crs.endwin()


if __name__ == '__main__':
    run()