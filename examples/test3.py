import curses
import sys

import npyscreen
npyscreen.disableColor()

def main():
    app = App()
    app.run()

class App(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.FormBaseNew(name = "COMMUNICATIONS")
        column_height = terminal_dimensions()[0] - 9
        widget_contacts = form.add(
            Column,
            name       = "CONTACTS",
            relx       = 2,
            rely       = 2,
            max_width  = 20,
            max_height = column_height
        )
        widget_messages = form.add(
            Column,
            name       = "MESSAGES",
            relx       = 23,
            rely       = 2,
            max_height = column_height
        )
        widget_input = form.add(
            npyscreen.BoxTitle,
            name       = "INPUT",
            max_height = 5
        )
        widget_input.resize
        widget_contacts.values  = ["alice", "bob"]
        widget_messages.values  = ["2018-09-19T2001Z    a message", "2018-09-19T2002Z    another message"]
        widget_input.values     = ["sup"]
        #exit_button = form.add(
        #    ExitButton,
        #    name       = "EXIT",
        #    #relx       = 78,
        #    rely       = 23
        #)
        widget_contacts.max_height = 5
        form.edit()

class Column(npyscreen.BoxTitle):
    def resize(self):
        self.max_height = int(0.73 * terminal_dimensions()[0])

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)

def terminal_dimensions():
    return curses.initscr().getmaxyx()

if __name__ == "__main__":
    main()