import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from gpiozero import LED


# USE GPIO NUMBERS NOT PIN NUMBERS
GPIO.setmode(GPIO.BCM)

# PIN DEFINITION
red_led = LED(18)
blue_led = LED(23)
green_led = LED(24)

# GUI DEFINITIONS
win = Tk()
win.title("5.2C RPI - Making a GUI")
myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold")

topFrame = Frame(win)
topFrame.pack(side = TOP)
bottomFrame = Frame(win)
bottomFrame.pack(side = BOTTOM)

#VARIABLE DEFINITIONS
rad = StringVar()

# EVENT FUNCTIONS   

def red_ledOn():
        radio_button_label.config(text = rad.get() + " LED radio button is selected")

        red_led.on()
        blue_led.off()
        green_led.off()

        print("RED")


def blue_ledOn():
        radio_button_label.config(text = rad.get() + " LED radio button is selected")
    
        red_led.off()
        blue_led.on()
        green_led.off()

        print("BLUE")
        
def green_ledOn():
        radio_button_label.config(text = rad.get() + " LED radio button is selected")
        
        red_led.off()
        blue_led.off()
        green_led.on()

        print("GREEN")

def close():
    GPIO.cleanup()
    win.destroy()

# WIDGETS

radio_button_label = Label(topFrame)
radio_button_label.pack()
radio_button_label.config(text = "No option selected")
R1 = Radiobutton(topFrame, text="Red LED", variable=rad, value = 'Red', command = red_ledOn)
R1.pack()
R2 = Radiobutton(topFrame, text="Blue LED", variable=rad, value = 'Blue', command = blue_ledOn)
R2.pack()
R3 = Radiobutton(topFrame, text="Green LED", variable=rad, value = 'Green', command = green_ledOn)
R3.pack()

exit_button = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red')
exit_button.pack()


win.protocol("WM_DELETE_WINDOW", close) #EXIT CLEANLY

win.mainloop() # LOOP FOREVER

