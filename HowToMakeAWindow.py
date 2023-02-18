######------ PYTHON STUDIO ------######
from tkinter import * # Imports Tkinter
window = Tk() # Window is the variable, window refers to Tk()
window.config(background='black') # Configures the window to make the background black
window.title('This is a test window') # Changes The Text Of The Title/Header Of The Window
label = Label(window,text='Hello, This is a text label') # Adds Text To Your Window
label.pack() # Makes The Label visible On The Window
window.geometry('300x300+200+300') # Changes The Size And Position of the window
window.mainloop() # Keeps The Window Open Instead Of Instantly Crashing