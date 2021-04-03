#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#kate: syntax Python ;

# a skeleton menu with python2 & py3                  https://paste.cutelyst.org/

# https://0bin.net/paste/yauebNkDNbwgZqwy#a2YfWpSTHh0RV-0Yfz3FIypudIU6oi4DWvV9EGXo1Pv

'''function 1 on F1 1 and NUM-1'''
def funkt1():
    return 1

def funkt2():
    return 2

def funkt3():
    return 3

def funkt4():
    return 4

def funkt5():
    return 5

def funkt6():
    return 6

def funkt7():
    return 7

def funkt8():
    return 8

def funkt9():
    return 9




import sys,os
import curses

global menuE
global e
global noofmes
global keychar
e       = 0
menuE   = 1   # active entry
noofmes = 10  # number of menu entries +1
keychar = " " # like 1 or 2 ...

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))


def draw_menu(stdscr):
    global menuE
    global e
    global noofmes
    global keychar
    k        = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN,  curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED,   curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        ki              = int(k)
        try:    keychar = chr(k)
        except: keychar = 0
        callfunc        = False


        while switch(k):
            if case(49, 265, 360): # allows keys   1  or  NUM-1  or  F1     to be  Entry1    for  0..9
                menuE = 1
                break
            if case(50, 266     ): # 258   mouse u
                menuE = 2
                break
            if case(51, 267, 338):
                menuE = 3
                break
            if case(52, 268     ): #260
                menuE = 4
                break
            if case(53, 269, 69):
                menuE = 5
                break
            if case(54, 270     ): #261
                menuE = 6
                break
            if case(55, 271, 262):
                menuE = 7
                break
            if case(56, 272     ): #259   mouse d
                menuE = 8
                break
            if case(57, 273, 339):
                menuE = 9
                break
            if case(10, 32 , 83 ):   # SPACE  ,   ENTER  ,   83 mouse middle
                callfunc = True
                break
            pass
            break

        if callfunc:
            if   menuE == 1: e = funkt1()
            elif menuE == 2: e = funkt2()
            elif menuE == 3: e = funkt3()
            elif menuE == 4: e = funkt4()
            elif menuE == 5: e = funkt5()
            elif menuE == 6: e = funkt6()
            elif menuE == 7: e = funkt7()
            elif menuE == 8: e = funkt8()
            elif menuE == 9: e = funkt9()


        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
            menuE = (menuE + 1) % noofmes


        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
            menuE = (menuE - 1) % noofmes

        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1

        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1


        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title        = "Python2 , py3  menu demo with lib ´curses´ "[:width-1]
        subtitle     = "because py2 will never die!"[:width-1]
        keystr       = str(e) + " <-- funkt  " + "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title    = int((  width // 2) - (len(title)    // 2) - len(title)    % 2)
        start_x_subtitle = int((  width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr   = int((  width // 2) - (len(keystr)   // 2) - len(keystr)   % 2)
        start_y          = int(( height // 2) -                   2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1,  0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y -6, start_x_title, title)


        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr( start_y - 4, start_x_subtitle, subtitle)

        #stdscr.addstr(start_y - 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr( start_y - 2, start_x_keystr, keystr)


        # menu
        stdscr.addstr(start_y + 0,  start_x_subtitle, "~~~  Menu  ~~~")


        if menuE == 1 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 1,  start_x_subtitle, "1 Entry1")
        if menuE == 2 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 2,  start_x_subtitle, "2 Entry2")
        if menuE == 3 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 3 , start_x_subtitle, "3 Entry3")
        if menuE == 4 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 4 , start_x_subtitle, "4 Entry4")
        if menuE == 5 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 5 , start_x_subtitle, "5 Entry5")
        if menuE == 6 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 6 , start_x_subtitle, "6 Entry6")
        if menuE == 7 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 7 , start_x_subtitle, "7 Entry7")
        if menuE == 8 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 8 , start_x_subtitle, "8 Entry8")
        if menuE == 9 :
            stdscr.attron( curses.A_BOLD)
        else          :  stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(start_y + 9 , start_x_subtitle, "9 Entry9")


        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
