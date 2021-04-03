import curses


class Terminal:
    def __init__(self):
        self.scr, width, height = self.__init_screen()

    def __init_screen(self):
        screen = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        x, y = screen.getmaxyx()
        return screen, x, y

    def run(self):
        self.scr.keypad(True)
        self.scr.clear()
        self.scr.refresh()
        k = self.scr.getch()


if __name__ == '__main__':
    app = Terminal()
    app.run()