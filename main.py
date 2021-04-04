import curses
import settings.strings as s

M_BLOCK_WIDTH = 22

class Terminal:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        self.__init_colors()

    @staticmethod
    def __init_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def __get_size(self):
        return self.screen.getmaxyx()

    def __create_block(self, x, y, text_len, text_row_count, title=''):
        box = curses.newwin(text_row_count, text_len, y, x)
        box.border()
        return box

    def __init_menu_page(self):
        key = 0
        while key != ord('q'):
            self.screen.clear()
            self.screen.refresh()
            height, width = self.__get_size()
            # Header block
            header_block = self.__create_block(width // 2 - (len(s.M_HEADER) + 2) // 2, height // 2 - 10, M_BLOCK_WIDTH, 3)
            header_block.addstr(1, 5, s.M_HEADER, curses.color_pair(1))

            # Menu block
            menu_block = self.__create_block(width//2 - len(s.M_ITEM1)//2, height//2 - 6, M_BLOCK_WIDTH, 9)
            menu_block.addstr(1, 3, s.M_ITEM1, curses.color_pair(1))
            menu_block.addstr(4, 3, s.M_ITEM2, curses.color_pair(1))
            menu_block.addstr(7, 3, s.M_ITEM3, curses.color_pair(1))

            self.screen.addstr(0, 0, f'hb{(len(s.M_HEADER) + 8) };mb{len(s.M_ITEM1) + 8}')

            menu_block.refresh()
            header_block.refresh()
            self.screen.refresh()
            key = self.screen.getch()

        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    def run(self):
        curses.curs_set(0)
        self.__init_menu_page()


if __name__ == '__main__':
    app = Terminal()
    app.run()