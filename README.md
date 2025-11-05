# Python_qr_code_app

# 📷 QR-Code Scanner (Tkinter + OpenCV)

A small desktop **QR-code scanner** built with **Tkinter** for the GUI and **OpenCV** for decoding QR codes.  
Simple and easy to run — select an image file containing a QR code and the app will read & show the decoded text.

---

## Table of Contents
- [About](#about)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Notes](#notes)  
- [Example Session](#example-session)  
- [How it works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  
- [Script (`qr_scanner.py`)](#script-qr_scannerpy)

---

## About
This script provides a simple GUI window where a user can select an image (e.g., `.jpg`) and press **Read QR-code** to decode any QR content in that image. Decoded text is shown in a message box.

---

## Features
- Graphical interface using Tkinter.  
- File picker to choose an image from disk.  
- Uses OpenCV's `QRCodeDetector` to detect & decode QR codes.  
- Minimal dependencies and straightforward usage.

---

## Requirements
- Python 3.x  
- OpenCV (`opencv-python`)  
- Tkinter (usually included with standard Python installs on Windows/macOS; on some Linux distros you may need `python3-tk`)

---

## Installation

Install OpenCV via pip:

```bash
pip install opencv-python
```

Make sure Tkinter is available. On Debian/Ubuntu:

```bash
sudo apt install python3-tk
```

Create a project folder and put the script file (recommended name: `qr_scanner.py`) there. If you want the small logo shown in the GUI, add an image named `logo.png` in the same folder (optional).

---

## Usage

Run the script from a terminal or by double-clicking (on systems configured for `.py` execution):

```bash
python qr_scanner.py
```

1. Click **Select Image** and choose a JPG file (or change the file dialog to accept other formats).  
2. The file path will appear in the entry field.  
3. Click **Read QR-code** — a message box will display the decoded text (or an empty string if nothing decoded).

---

## Notes
- The file dialog currently filters for `*.jpg`. If your images are PNG or other formats, change the `filetypes` parameter in the `open()` function.  
- `logo.png` is optional; if it's missing the script will raise an error when trying to load the image. Either add a logo file or remove that part of the code.

---

## Example Session
- Launch app → Click **Select Image** → choose `my_qr.jpg` → Click **Read QR-code** → dialog shows the decoded URL/text.

---

## How it works
- Tkinter builds a simple UI with an `Entry`, labels, and two buttons.  
- `filedialog.askopenfile` returns a file path that is placed in the entry widget.  
- OpenCV's `cv2.QRCodeDetector()` is used to `detectAndDecode` the image read with `cv2.imread()`.  
- The decoded string is shown with `tkinter.messagebox.showinfo()`.

---

## Customization ideas
- Accept multiple image formats (add `("Images", "*.png;*.jpg;*.jpeg;*.bmp")`).  
- Add webcam scanning: use `cv2.VideoCapture(0)` and apply `detectAndDecode` on frames for live scanning.  
- Save scan history to a text file.  
- Handle cases where `cv2.imread` returns `None` (invalid path) and show a friendly error.  
- Improve UI layout, add icons or status labels.

---

## Contributing
Small project — contributions welcome. Suggestions:
- Add live camera scanning mode.  
- Better error handling & cross-platform packaging (PyInstaller) to make an executable.

---

## License
Free to use. Add an MIT or other license file if you want to publish with explicit terms.

---

## Script: `qr_scanner.py`
Copy the exact code below into `qr_scanner.py`:

```python
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
```
