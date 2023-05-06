from PIL import Image
import tkinter as tk
from tkinter import filedialog

class Img2PDF_Converter:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")

        self.label = tk.Label(master, text="Select files to open:")
        self.label.pack()

        self.button = tk.Button(master, text="Browse files", command=self.on_button_clicked)
        self.button.pack()

        self.filename_label = tk.Label(master, text="", wraplength=700, height=10)
        self.filename_label.pack()


    def on_button_clicked(self):
        filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        filenames = filedialog.askopenfilenames(title="Select files", filetypes=filetypes)

        image_list = []

        if filenames:
            self.image_filenames = list(filenames)
            self.filename_label.config(text="Selected files\n" + "\n".join(self.image_filenames))
            # print("Selected files:")
            for i, filename in enumerate(self.image_filenames):
                # print(f"Image{i+1}: {filename}")
                image_list.append(Image.open(filename).convert('RGB'))

        output_filename = '/Users/rogerteong/Desktop/Education Transcript/output.pdf'
        with open(output_filename, 'wb') as f:
            image_list[0].save(f, format='PDF', save_all=True, append_images=image_list[1:])

        



if __name__ == "__main__":
    root = tk.Tk()
    my_gui = Img2PDF_Converter(root)
    root.mainloop()