import curses
import settings.strings as s

M_BLOCK_WIDTH = 22


class Terminal:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        self.screen.nodelay(True)
        self.__init_colors()

    @staticmethod
    def __init_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def __get_size(self):
        return self.screen.getmaxyx()

    def __create_block(self, h, l, y, x):
        win = curses.newwin(h, l, y, x)
        # win.clear()
        win.border()
        return win

    def __display_menu(self, selected_row, menu_items):
        height, width = self.__get_size()
        menu_block = self.__create_block(width // 2 - len(s.M_ITEM1) // 2, height // 2 - 6, M_BLOCK_WIDTH, 9)
        menu_block.keypad(True)
        menu_block.refresh()
        for index, row in enumerate(menu_items):
            # x = width//2 - len(row)//2
            # y = height//2 - len(menu_items)//2 + index
            if index == selected_row:
                menu_block.attron(curses.color_pair(2))
                menu_block.addstr(index + 1, 3, row)
                menu_block.attroff(curses.color_pair(1))
            else:
                menu_block.addstr(index + 1, 3, row)

        menu_block.refresh()

    def __init_data_recording_page(self):
        try:
            key = 0
            self.screen.refresh()
            while 1:
                h, w = self.__get_size()

                self.screen.refresh()

                win1 = self.__create_block(h - 20, w // 2 - 10, 5, 5)
                win2 = self.__create_block(h - 10, w // 2 - 10, 5, 5 + w // 2)
                win3 = self.__create_block(5, w - 10, h - 5, 5)
                win1.refresh()
                win2.refresh()
                win3.refresh()

                key = self.screen.getch()
                if key == ord('q'):
                    self.__close_terminal()

                win1.clear()
                win2.clear()
                win3.clear()
                self.screen.refresh()
        except Exception:
            self.__close_terminal()

    def __close_terminal(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    # def __init_menu_page(self):
    #
    #     h, w = self.__get_size()
    #
    #
    #     # current_row = 0
    #     # key = 0
    #     # menu = [s.M_ITEM1, s.M_ITEM2, s.M_ITEM3]
    #     # self.__display_menu(current_row, menu)
    #     # while 1:
    #     #     key = self.screen.getch()
    #     #     height, width = self.__get_size()
    #     #     # Header block
    #     #     header_block = self.__create_block(width // 2 - (len(s.M_HEADER) + 2) // 2, height // 2 - 10, M_BLOCK_WIDTH, 3)
    #     #     header_block.addstr(1, 5, s.M_HEADER, curses.color_pair(1))
    #     #
    #     #     menu_block = self.__create_block(width // 2 - len(s.M_ITEM1) // 2, height // 2 - 6, M_BLOCK_WIDTH, 9)
    #     #     menu_block.keypad(True)
    #     #     menu_block.refresh()
    #     #     for index, row in enumerate(menu):
    #     #         # x = width//2 - len(row)//2
    #     #         # y = height//2 - len(menu_items)//2 + index
    #     #         if index == current_row:
    #     #             menu_block.attron(curses.color_pair(2))
    #     #             menu_block.addstr(index + 1, 3, row)
    #     #             menu_block.attroff(curses.color_pair(1))
    #     #         else:
    #     #             menu_block.addstr(index + 1, 3, row)
    #     #
    #     #     menu_block.refresh()
    #     #
    #     #     if key == curses.KEY_UP and current_row > 0:
    #     #         current_row -= 1
    #     #     elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
    #     #         current_row += 1
    #     #
    #     #     # self.__display_menu(current_row, menu)
    #     #
    #     #     # menu_block.addstr(1, 3, s.M_ITEM1, curses.color_pair(1))
    #     #     # menu_block.addstr(4, 3, s.M_ITEM2, curses.color_pair(1))
    #     #     # menu_block.addstr(7, 3, s.M_ITEM3, curses.color_pair(1))
    #     #     #
    #     #     # self.screen.addstr(0, 0, f'hb{width // 2 - (len(s.M_HEADER) + 2) // 2};mb{width//2 - len(s.M_ITEM1)//2}')
    #     #
    #     #     header_block.refresh()
    #     #     menu_block.refresh()
    #     #     self.screen.refresh()
    #
    #
    #
    #
    #     # curses.nocbreak()
    #     # self.screen.keypad(False)
    #     # curses.echo()
    #     # curses.endwin()

    def run(self):
        curses.curs_set(0)
        self.__init_data_recording_page()


if __name__ == '__main__':
    app = Terminal()
    app.run()