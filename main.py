import curses
import curses.ascii
import settings.strings as s
import datetime as dt
# import libs.async_program

M_BLOCK_WIDTH = 22


class Terminal:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.noecho()
        curses.curs_set(0)
        curses.halfdelay(1)
        self.__init_colors()

    @staticmethod
    def __init_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def __get_size(self):
        return self.screen.getmaxyx()

    def __create_block(self, h, l, y, x):
        win = curses.newwin(h, l, y, x)
        win.border()
        return win

    def __init_top_bar(self, width):
        status_bar_str = 'Press: "Enter" to start | "ESC" to stop | "Tab" to exit |'
        self.screen.attron(curses.color_pair(2))
        self.screen.addstr(0, 0, status_bar_str)
        self.screen.addstr(0, len(status_bar_str), " " * (width - len(status_bar_str) - 1))
        self.screen.attroff(curses.color_pair(2))

    # def __display_menu(self, selected_row, menu_items):
    #     height, width = self.__get_size()
    #     menu_block = self.__create_block(width // 2 - len(s.M_ITEM1) // 2, height // 2 - 6, M_BLOCK_WIDTH, 9)
    #     menu_block.keypad(True)
    #     menu_block.refresh()
    #     for index, row in enumerate(menu_items):
    #         # x = width//2 - len(row)//2
    #         # y = height//2 - len(menu_items)//2 + index
    #         if index == selected_row:
    #             menu_block.attron(curses.color_pair(2))
    #             menu_block.addstr(index + 1, 3, row)
    #             menu_block.attroff(curses.color_pair(1))
    #         else:
    #             menu_block.addstr(index + 1, 3, row)
    #
    #     menu_block.refresh()

    def __init_data_recording_page(self):
        try:
            key = 0
            while key != ord('q'):
                key = self.screen.getch()

                h, w = self.__get_size()

                # Init blocks
                win1 = self.__create_block(h - 15, w // 2 - 10, 5, 5)
                win2 = self.__create_block(h - 15, w // 2 - 10, 5, 5 + w // 2)
                win3 = self.__create_block(5, w - 10, h - 5, 5)

                # Headers
                block_center = (w // 2 - 20) // 2
                win1.addstr(0, block_center, 'Devices')
                win2.addstr(0, block_center, 'Data')
                win3.addstr(0, 5, 'Input')

                block_list = [win1, win2, win3]

                self.__init_top_bar(w)

                win1.addstr(5, 5, str(dt.datetime.now()), curses.color_pair(3))

                if key == curses.KEY_UP:
                    win2.addstr(5, 5, chr(key))
                else:
                    win3.addstr(1, 1, 'Waiting')

                for i in range(len(block_list)):
                    block_list[i].refresh()

                self.screen.refresh()

        except Exception:
            self.__close_terminal()
        finally:
            self.__close_terminal()

    def __close_terminal(self):
        self.screen.clear()
        self.screen.keypad(False)
        curses.nocbreak()
        curses.curs_set(1)
        curses.echo()
        curses.endwin()

    def run(self):
        self.__init_data_recording_page()


if __name__ == '__main__':
    app = Terminal()
    app.run()