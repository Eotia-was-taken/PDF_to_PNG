from pdf2image import convert_from_path
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter as tk
from PIL import ImageTk
import os

from typing import List, Tuple


class CanvasControl:

    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.current_img_index = 0
        self.images: List = []
        self._display_images: List[ImageTk.PhotoImage] = []
        self.transparent = False

    def set_images(self, images: List):
        self.images = images
        self._display_images = [ImageTk.PhotoImage(image) for image in images]
        self._display_image()

    @property
    def current_img(self):
        return self._display_images[self.current_img_index]

    def next(self):
        if self._display_images is None:
            return

        self.current_img_index = min(self.current_img_index + 1, len(self._display_images) - 1)
        self._display_image()

    def prev(self):
        if self._display_images is None:
            return
        self.current_img_index = max(self.current_img_index - 1, 0)
        self._display_image()

    def _display_image(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_img)
        self.canvas.pack()


def read_pdf(path: str, page_size: Tuple[int, int], transparent: bool):
    return convert_from_path(path, size=page_size, fmt="png", transparent=transparent)


def open_file(canvas_control: CanvasControl, width: int, height: int, transparent: bool, save_button: tk.Button) -> List:
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not filepath:
        return []
    canvas_control.canvas.config(width=width, height=height)
    canvas_control.canvas.scale("all", 0, 0, width, height)
    images = read_pdf(filepath, page_size=(width, height), transparent=transparent)
    canvas_control.set_images(images)
    save_button['state'] = tk.NORMAL

    return images


def save_pngs(canvas_control: CanvasControl, prefix: str):

    directory = askdirectory(initialdir=os.getcwd())
    prefix = prefix + "_" if len(prefix) != 0 else ""
    for i, image in enumerate(canvas_control.images):
        file_path = os.path.normpath(f"{directory}/{prefix}page_{i}.png")
        image.save(file_path)

    tk.messagebox.showinfo("File saved!", message=f"Images saved to {directory}")
