#GUI for intro tab
import tkinter as tk
from PIL import Image, ImageTk
def show_Goodbye():
    root = tk.Tk()
    root.geometry("600x400")
    root.resizable(False,False)
    background_image = Image.open("flight.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root,image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    a="'Thank you for choosing Carry You for your travel needs.\n We would love to serve you again. Safe travels!"
    welcome_label = tk.Label(root, text=a, font=("Times New Roman", 16), fg="black",bg='LightSalmon')
    welcome_label.pack(pady=10)
    welcome_label.place(x=0,y=60,width=600,height=100)
    root.mainloop()
if __name__ == "__main__":
    show_Goodbye()