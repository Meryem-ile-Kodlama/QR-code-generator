from tkinter import *
import pyqrcode # pip install pyqrcode - pip install pypng
import os

root = Tk()
root.title("QR Code Generator")
root.geometry("500x550")

def create_code():
    qr_code = pyqrcode.create(my_entry.get())

    file_path = "C:\\Users\\merye\\OneDrive\\Desktop\\qr_code.png"
    base_name, extension = os.path.splitext(file_path)
    counter = 1

    while os.path.exists(file_path):
        file_path = f"{base_name}_{counter}{extension}"
        counter += 1

    qr_code.png(file_path, scale=5)

    image = PhotoImage(file=file_path)
    my_label.config(image=image)
    my_label.image = image

def clear_all():
    my_entry.delete(0, END)
    my_label.config(image="")

#Create GUI
my_entry = Entry(root, font="Helvetica 18")
my_entry.pack(pady=20)

create_button = Button(root, text="Create QR Code", command=create_code)
create_button.pack(pady=20)

clear_button = Button(root, text="Clear", command=clear_all)
clear_button.pack()

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()