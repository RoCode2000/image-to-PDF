from PIL import Image
import tkinter as tk
from tkinter import filedialog

class Img2PDF_Converter:
    def __init__(self, master):
        self.master = master

        #GUI Label
        master.title("Image To PDF Converter")

        # Select files label
        self.label = tk.Label(master, text="Select files to open:")
        self.label.pack()

        # Select files button
        self.button = tk.Button(master, text="Browse files", command=self.on_button_clicked)
        self.button.pack()

        # Label for selected files
        self.filename_label = tk.Label(master, text="", wraplength=700, height=10)
        self.filename_label.pack()

        # Save Button
        self.save_button = tk.Button(master, text="Save", command=self.on_save_button_clicked)
        self.save_button.pack()

    def on_save_button_clicked(self):
        # Output folder variable
        output_filename = ''
        # Output file types
        filetypes = [("PDF files", "*.pdf")]
        # Select folder to save output into
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes=filetypes, defaultextension=".pdf")
        # Once folder is selected
        if filename:
            output_filename = filename
            image_list = []
            # Loop through selected filename
            for i, filename in enumerate(self.image_filenames):
                # Convert and append those filenames into 'RGB' and image_list respectively
                image_list.append(Image.open(filename).convert('RGB'))
            with open(output_filename, 'wb') as f:
                # Append them one after another and save it in a PDF format
                image_list[0].save(f, format='PDF', save_all=True, append_images=image_list[1:])

    def on_button_clicked(self):
        # Different expected image file type
        filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        # Select files from folder
        filenames = filedialog.askopenfilenames(title="Select files", filetypes=filetypes)
        # Once files are selected
        if filenames:
            # Put them in a list
            self.image_filenames = list(filenames)
            # Put them in label and segment them neatly
            self.filename_label.config(text="Selected files:\n" + "\n".join(self.image_filenames))


if __name__ == "__main__":
    root = tk.Tk()
    main = Img2PDF_Converter(root)
    root.mainloop()