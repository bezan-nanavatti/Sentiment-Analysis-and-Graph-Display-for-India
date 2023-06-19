from tkinter import *
root = Tk()

def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("Display Plot")
    img = PhotoImage(file='codeforproject/imgplot.png')
    l = Label(newWindow, image=img, height=900, width=900)
    l.pack()
    newWindow.mainloop()

frame = Frame(root, padx=100, pady=100)
frame1 = Frame(frame, padx=50, pady=50)
frame1.pack()
frame2 = Frame(frame, padx=50, pady=50)
frame2.pack()
frame.pack()

button1 = Button(frame1, text = 'Display', fg ='red', command=openNewWindow)
button1.pack()

label = Label(frame2, text='Enter File for Sentiment Analysis').pack()
clicked = StringVar()
clicked.set( "Use existing file" )

options = [
    "Use existing file",
    "Upload file" 
]
menu = OptionMenu(frame2, clicked, *options)

menu.pack()
root.mainloop()