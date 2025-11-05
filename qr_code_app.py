import cv2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

window = Tk()
window.geometry("310x435+500+100")
window.title("Qr-code scanner")


def open():
    file = filedialog.askopenfile(mode="r", filetypes=[("Files", "*.jpg")])
    if file:
        filepath = os.path.abspath(file.name)
        Ent1.insert(0, str(filepath))


def scan():
    d = Ent1.get()
    res = cv2.QRCodeDetector()
    val, points, s_qr = res.detectAndDecode(cv2.imread(d))
    messagebox.showinfo("Qr-Scan", val)


text = Label(window, text="QR_SCANNER", fg="white", bg="black")
text.pack(fill=X)

photo = PhotoImage(file="logo.png")
imo = Label(window, image=photo)
imo.place(x=40, y=40, width=230, height=190)

lbl1 = Label(window, text="QR-code Scanner", font=("Tajawal", 12))
lbl1.place(x=100, y=250)

Ent1 = Entry(window, font=("Tajawal", 12), width=31)
Ent1.place(x=15, y=290)

btn = Button(
    window,
    text="Select Image",
    fg="white",
    bg="green",
    width=35,
    font=("Tajawal", 12),
    command=open,
)
btn.place(x=10, y=340)

btn1 = Button(
    window,
    text="Read QR-code",
    fg="white",
    bg="red",
    width=35,
    font=("Tajawal", 12),
    command=scan,
)
btn1.place(x=10, y=383)


window.mainloop()
