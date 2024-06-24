from tkinter import *
from playsound import playsound
import time
from PIL import Image, ImageTk

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font=('arial', 30, 'bold'), bg="#000", fg="#ea3548")
heading.pack(pady=10)

Label(root, font=("arial", 15, "bold"), text="Current time:", bg="papaya whip").place(x=65, y=70)

def clock():
    clock_time = time.strftime("%H:%M:%S")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(root, font=("arial", 15, "bold"), fg="#000", bg="papaya whip")
current_time.place(x=190, y=70)
clock()

# Timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font=("arial", 50), bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font=("arial", 50), bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font=("arial", 50), bg="#000", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")

Label(root, text="Hours", font=("arial", 12), bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="Min", font=("arial", 12), bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="Sec", font=("arial", 12), bg="#000", fg="#fff").place(x=345, y=200)

def Timer():
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())

    while times > -1:
        minute, second = divmod(times, 60)
        hour = 0
        if minute >= 60:
            hour, minute = divmod(minute, 60)

        sec.set(f"{second:02d}")
        mins.set(f"{minute:02d}")
        hrs.set(f"{hour:02d}")

        root.update()
        time.sleep(1)

        if times == 0:
            sec.set("00")
            mins.set("00")
            hrs.set("00")
            playsound("alarm.mp3")

        times -= 1

def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def eggs():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

def face():
    hrs.set("00")
    mins.set("10")
    sec.set("00")

button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font=("arial", 10, "bold"), command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)

image1 = Image.open("brush.png")
brush_image = ImageTk.PhotoImage(image1)
button1 = Button(root, image=brush_image, bd=0, bg="#000", activebackground="#000", command=brush)
button1.place(x=7, y=300)

image2 = Image.open("face.png")
face_image = ImageTk.PhotoImage(image2)
button2 = Button(root, image=face_image, bd=0, bg="#000", activebackground="#000", command=face)
button2.place(x=137, y=300)

image3 = Image.open("eggs.png")
eggs_image = ImageTk.PhotoImage(image3)
button3 = Button(root, image=eggs_image, bd=0, bg="#000", activebackground="#000", command=eggs)
button3.place(x=267, y=300)

root.mainloop()
