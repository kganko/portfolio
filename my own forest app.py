# as a tribute to the best app ever created - Forest! Thank you for helping me with my Python journey and saving the planet <3

from plyer import notification
import tkinter as tk
import time
from tkinter import *
from PIL import ImageTk, Image

# window settings
window = tk.Tk()
window.geometry("300x250")
window.title("Time to start your amazing productivity journey")

# variables
hour = StringVar()
minute = StringVar()
second = StringVar()


# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")


# entry part
hourEntry = Entry(window, width=3, font=("Futura", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=200)
minuteEntry = Entry(window, width=3, font=("Futura", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=200)
secondEntry = Entry(window, width=3, font=("Futura", 18, ""), textvariable=second)
secondEntry.place(x=180, y=200)


# image settings
image = Image.open("pine-tree.png")
resize_image = image.resize((160, 160))
img = ImageTk.PhotoImage(resize_image)


label1 = Label(image=img)
label1.image = img
label1.pack()


def submit():
	try:
		temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
	except:
		print("Please input the right value")
	while temp > -1:

		# dividing for seconds
		mins, secs = divmod(temp, 60)

		# time converting
		hours = 0
		if mins > 60:
			hours, mins = divmod(mins, 60)

		# change format
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# clock mechanism
		window.update()
		time.sleep(1)

		# finishing
		if temp == 0:
			window.quit()

		temp -= 1


# button widget
btn = Button(window, text='Set Time Countdown', bd='5', command=submit)
btn.place(x=90, y=160)

window.mainloop()

notification.notify(
	title="Time is up!",
	message=f"Congrats! You stayed focused for so long. Time for a break!",
	timeout=10
)