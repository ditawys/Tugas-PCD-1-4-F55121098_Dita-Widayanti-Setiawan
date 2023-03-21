#Dita Widayanti Setiawan_F55121098_Kelas C
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class ImageApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.image_path = None
        self.image = None
        self.filtered_image = None

    def create_widgets(self):
        self.select_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.select_button.pack(side="top")

        self.median_button = tk.Button(self, text="Median Filter", command=self.median_filter)
        self.median_button.pack(side="left")

        self.gaussian_button = tk.Button(self, text="Gaussian Filter", command=self.gaussian_filter)
        self.gaussian_button.pack(side="left")

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack(side="bottom")

    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.filtered_image = self.image.copy()
            self.show_image(self.image)

    def show_image(self, image):
        self.canvas.delete("all")
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(250, 250, image=photo)
        self.canvas.image = photo

    def median_filter(self):
        if self.image_path:
            self.filtered_image = self.image.copy()
            self.filtered_image = self.filtered_image.filter(ImageFilter.MedianFilter())
            self.show_image(self.filtered_image)

    def gaussian_filter(self):
        if self.image_path:
            self.filtered_image = self.image.copy()
            self.filtered_image = self.filtered_image.filter(ImageFilter.GaussianBlur(radius=3))
            self.show_image(self.filtered_image)

root = tk.Tk()
app = ImageApp(master=root)
app.mainloop()

