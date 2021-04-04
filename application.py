import npyscreen
import curses


class Terminal(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, "Main Menu")


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.BoxTitle, name="Menu", rely=2, relx=2, max_height=terminal_dimensions()[0] - 10,
                 max_width=20)


def terminal_dimensions():
    return curses.initscr().getmaxyx()


def main():
    terminal = Terminal()
    terminal.run()


if __name__ == '__main__':
    main()