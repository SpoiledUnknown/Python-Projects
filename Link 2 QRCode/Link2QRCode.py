import os
import qrcode as qr
import customtkinter as ctk

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_path = os.path.join(desktop_path, 'qrcodes')

# Function to create QR code
def Create_Qr_Code():
    global img
    img = qr.make(link)
    type(img)

# Function to save image
def Save_Image():
    global img
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    existing_files = os.listdir(folder_path)

    max_index = 0
    for filename in existing_files:
        if filename.startswith('code'):
            try:
                index = int(filename.split('.')[0][len('code'):])
                max_index = max(max_index, index)
            except ValueError:
                pass

    new_filename = f"code{max_index + 1}.png"
    img_path = os.path.join(folder_path, new_filename)

    img.save(img_path)

# GUI setup
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("350x250")
root.title("QR Code Generator")
root.resizable(False, False)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both")

label = ctk.CTkLabel(master=frame, text="QR Code Generator", font=("Roboto", 24))
label.pack(pady=12, padx=10)

link = ctk.CTkEntry(master=frame, placeholder_text="https://www.youtube.com/c/spoiledunknown")
link.pack(pady=12, padx=10)

button1 = ctk.CTkButton(master=frame, text="Create Code", command=Create_Qr_Code)
button1.pack(pady=12, padx=10)

button2 = ctk.CTkButton(master=frame, text="Save Image", command=Save_Image)
button2.pack(pady=12, padx=10)

root.mainloop()
