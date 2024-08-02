#GUI for intro tab
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
def show_welcome_and_website():
    # Create the main window
    root = tk.Tk()
    root.title("Click Here")
    # Set window size
    root.geometry("700x400")# Width x Height
    root.resizable(False,False)
    # Load and display background image
    background_image = Image.open("flight.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root,text="hi", image=background_photo)
    background_label.place(x=-120, y=0, relwidth=1, relheight=1)
    # Function to handle button click
    def on_button_click():
        user_name = simpledialog.askstring("Input", "Enter your name:")
        welcome_label.config(text=f"Welcome,{user_name}!\n To Carry You")
    # Create a button
    button = tk.Button(root, text="Click Here", command=on_button_click,bg="LightPink1",fg="midnight blue")
    button.pack(pady=40)
    # Create labels to display the welcome message and website name
    welcome_label = tk.Label(root, text="", font=("Times New Roman", 16), fg="black",bg="salmon1")
    welcome_label.pack(pady=10)
    welcome_label.place(x=490,y=0,width=220,height=400)
    # Run the main loop
    root.mainloop()
if __name__ == "__main__":
    show_welcome_and_website()
