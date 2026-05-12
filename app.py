import qrcode
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create folder automatically
if not os.path.exists("generated_qr"):
    os.makedirs("generated_qr")

def generate_qr():
    data = entry.get()

    if data == "":
        messagebox.showerror("Error", "Please enter text or URL")
        return

    # Generate QR
    img = qrcode.make(data)

    # Save image
    path = "generated_qr/my_qr.png"
    img.save(path)

    # Display image
    qr_img = Image.open(path)
    qr_img = qr_img.resize((200, 200))

    photo = ImageTk.PhotoImage(qr_img)

    qr_label.config(image=photo)
    qr_label.image = photo

    messagebox.showinfo("Success", "QR Code Generated!")

# Main window
root = tk.Tk()

root.title("Smart QR Generator")

root.geometry("400x450")

title = tk.Label(root, text="QR Generator", font=("Arial", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn = tk.Button(root, text="Generate QR", command=generate_qr)
btn.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()