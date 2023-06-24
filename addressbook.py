import tkinter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

dictListOfEmails = {
    "Anna": "anna@company.com",
    "Brian": "brian@company.com",
    "Charles": "charles@gmail.com",
    "Derek": "derek@private.com"
}

import pandas as pd
df = pd.DataFrame(dictListOfEmails.items(),columns=["name", "address"])
print(df)

win= tkinter.Tk()

win.title('Your personal emails list')
win.geometry('850x400')

message = 'Hello! Welcome to your own personal address book. You can add and remove addresses from here too!'
msg = tkinter.Message(win, text = message, width = 250)
msg.config(bg='blue',fg='white')
msg.pack()

def show():
    win = tkinter.Tk()
    win.title('All your emails here')  # setting title of the window
    win.geometry('850x500')
    lab = tkinter.Label(win, text=df, width=800, height=800)
    lab.pack()

def add():
    win = tkinter.Tk()
    win.geometry('300x300')
    tkinter.Label(win, text='Name').grid(row=0)
    tkinter.Label(win, text='Email').grid(row=1)
    ent1 = tkinter.Entry(win)
    ent2 = tkinter.Entry(win)
    ent1.grid(row=0, column=1)
    ent2.grid(row=1, column=1)
    dictListOfEmails.update({ent1.get(): ent2.get()})


def remove():
    win = tkinter.Tk()
    win.geometry('300x300')
    tkinter.Label(win, text='Name').grid(row=0)
    tkinter.Label(win, text='Email').grid(row=1)
    ent1 = tkinter.Entry(win)
    ent2 = tkinter.Entry(win)
    ent1.grid(row=0, column=1)
    ent2.grid(row=1, column=1)
    dictListOfEmails.pop(ent1)

    btnremovequit = tkinter.Button(win, text="Save and close", width=15, height=5, command=win.quit)
    btnremovequit.place(x=15, y=90)
    win.mainloop()

def close():
    win.mainloop()


btnshow = tkinter.Button(win, text="Show All", width=15, height=5, command=show)
btnshow.place(x=150,y=90)

btnadd = tkinter.Button(win, text="Add new record", width=15, height=5, command=add)
btnadd.place(x=300,y=90)

btnremove = tkinter.Button(win, text="Remove record", width=15, height=5, command=remove)
btnremove.place(x=450,y=90)

btnclose = tkinter.Button(win, text="Save and close", width=15, height=5, command=win.quit)
btnclose.place(x=600,y=90)

win.mainloop()


# initializing variables with values
fileName = 'youraddressbook.pdf'
documentTitle = 'Your address book'
title = 'All your contacts'
subTitle = 'Use them now'
textLines = [
    dictListOfEmails
]
#image = 'image.jpg'

pdf = canvas.Canvas(fileName)

# setting the title of the document
pdf.setTitle(documentTitle)


# creating the title by setting it's font
# and putting it on the canvas
pdf = canvas.Canvas(fileName)

# setting the title of the document
pdf.setTitle(documentTitle)

pdf.drawCentredString(300, 770, title)

pdf.setFillColorRGB(0, 0, 0)
pdf.setFont("Courier-Bold", 35)
pdf.drawCentredString(290, 720, subTitle)

# creating a multiline text using
# textline and for loop
text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)

#for line in textLines:
text.textLine()

pdf.drawText(text)

# saving the pdf
pdf.save()
