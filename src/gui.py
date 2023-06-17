import tkinter as tk
from tkinter import filedialog, messagebox
from main import convert_gif_to_anim
from PIL import Image, ImageTk
import os
import shutil

# Initialise global variable(s)
target_file_path = None
selected_gif_image = None
image_label = None

# Create GUI window
root = tk.Tk()
root.title("GIF to anim converter")
root.geometry("800x320")

# Add width parameter user input
width_input = tk.StringVar(value="80")

# Add label above the Spinbox
label = tk.Label(root, text="Width:")
label.pack()

# Make a Spinbox for the width_input variable
text_box = tk.Spinbox(root, from_=0, to=1000, textvariable=width_input, width=8)
text_box.pack()

# Let the user select a .gif file
def select_file():
    global target_file_path
    file_path = filedialog.askopenfilename(filetypes=[("GIF Files", "*.gif")])

    if(file_path):
        target_file_path = file_path
        show_gif_image()

# Display the selected .gif
def show_gif_image():
    global gif_image, image_label
    try:
        image = Image.open(target_file_path)
        gif_image = ImageTk.PhotoImage(image)
        if image_label:
            image_label.destroy()
        image_label = tk.Label(root, image=gif_image)
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open GIF file: {str(e)}")

# Clear the work folder
def clear_work_folder():
    folder_path = "work"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        os.mkdir(folder_path)

def exec(target, width=80):
    if(target):
        clear_work_folder()
        convert_gif_to_anim(target, width=width)
        messagebox.showinfo("Success", "Succesfully created animation.txt!")
    else:
        messagebox.showinfo("Info", "Please select a file path!")

select_button = tk.Button(root, text="Select GIF", command=select_file)
select_button.pack(pady=10)

exec_button = tk.Button(root, text="Convert to Animation", command=lambda: exec(target_file_path, int(width_input.get())))
exec_button.pack(pady=10)

root.mainloop()
