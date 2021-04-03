import curses

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

stdscr = curses.initscr()

height = 20
width = 60
pos_y = 0
pos_x = 0
window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window

window.keypad(True)
curses.noecho()
curses.curs_set(0)

window.border(0)
window.nodelay(True)

key = KEY_RIGHT         #key defaulted to KEY_RIGHT
pos_x = 5               #initial x position
pos_y = 5               #initial y position
window.addch(pos_y,pos_x,'*')   #print initial dot

while key != 27:
    window.timeout(100)
    keystroke = window.getch()  # get current key being pressed
    if keystroke is not -1:  # key is pressed
        key = keystroke
        window.addch(pos_y, pos_x, ' ')  # erase last dot
        if key == KEY_RIGHT:  # right direction
            pos_x = pos_x + 1  # pos_x increase
        elif key == KEY_LEFT:  # left direction
            pos_x = pos_x - 1  # pos_x decrease
        elif key == KEY_UP:  # up direction
            pos_y = pos_y - 1  # pos_y decrease
        elif key == KEY_DOWN:  # down direction
            pos_y = pos_y + 1  # pos_y increase
        window.addch(pos_y, pos_x, '*')  # draw new dot

curses.endwin()