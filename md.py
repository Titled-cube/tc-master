
#Import all packages
import time
import turtle
from contextlib import contextmanager

#globalling
global text
text = "-"
global nameInput1
nameInput1 = ""

global title_window_warning
title_window = "-"

global text_window_warning
text_window = "Distrubituve TitledCube_STUDIO  ---(key of securety : TC_89797899068667e}{}\]89{)\n \n \n \n \n \n \n \n \n \n \n \n \n\n \n \n \n"

global title_window_info
title_window_info = "-"

global text_window_info
text_window_info = "Distrubituve TitledCube_STUDIO  ---(key of securety : TC_89797899068667e}{}\]89{)\n \n \n \n \n \n \n \n \n \n \n \n \n\n \n \n \n"

global title_window_error
title_window = "-"

global text_window_error
text_window = "Distrubituve TitledCube_STUDIO  ---(key of securety : TC_89797899068667e}{}\]89{)\n \n \n \n \n \n \n \n \n \n \n \n \n\n \n \n \n"

global license_key
license_key = "KEY-KEY"

global enter_text_lk
enter_text_lk = "Please enter your key in type XXX-XXX"

#first function
def HelloWorld():
    print("Hello world !")
#second function
def InputName():
    print("Hello, what your name ?")
    nameInput1 = input()
#third and all time functions

    
def timestop_5():
    time.sleep(5)
def timestop_10():
    time.sleep(10)
def timestop_15():
    time.sleep(20)
def timestop_20():
    time.sleep(20)
def timestop_25():
    time.sleep(25)
def timestop_30():
    time.sleep(30)

def timer_input():
    print("Please, enter seconds from timer:")
    sec_time_input = input()
    time.sleep(sec_time_input)

#TKINTER

import tkinter as tk
import tkinter.messagebox as mb

def show_warning():
    msg = "Warning: Something went wrong!"
    mb.showwarning("____________ Warning please read ____________", msg)

def show_info_save():
    msg = "Your settings are saved"

def show_NowKnow_error():
    msg = "The application has detected an unknown error"
    mb.showerror("_________________ Error ____________", msg)

def show_info():
    msg = info
    mb.showinfo("____________ Information ____________", msg)

def show_virus_error():
    msg = "YOUR APlIccccationnnnnn has ggpoopoooty a viryus"
    mb.showerror("_________________ Error ____________", msg)

def show_licensy():
    msg = "Your licensy is activate ! Please save your code \n YOUR FROMMING CODE : \n TC_O7P"
    mb.showinfo("_________________ Licensy ____________", msg)

def printen():
    print(text)

def interactive_show_error():
    

    msg = text_window_error
    mb.showerror(title_window_error, msg)


def interactive_show_info():

    msg = text_window_info
    mb.showinfo(title_window_info, msg)


def interactive_show_warning():
    title_window = "-"
    
    text_window = "Distrubituve TitledCube_STUDIO  ---(key of securety : TC_89797568668667e}{}\]89{)\n \n \n \n \n \n \n\n \n \n \n\n \n \n \n\n \n \n \n\n \n \n \n\n \n \n \n\n \n \n \n"

    msg = text_window_warning
    mb.showwarning(title_window_warning, msg)


def licensy_key1():
    print(enter_text_lk)
    key_user_input = input()
    if key_user_input == license_key :
        print("Licensy is activatied !")
        show_licensy()


def t_v():
    print("T>V")


