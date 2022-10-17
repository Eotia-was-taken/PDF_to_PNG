import tkinter as tk
from util import CanvasControl, open_file, save_pngs


if __name__ == "__main__":
    default_width = 660
    default_height = 854

    window = tk.Tk()
    transparent = tk.BooleanVar()
    width = tk.IntVar()
    width.set(default_width)
    height = tk.IntVar()
    height.set(default_height)

    title = "Convert PDF to PNG"
    page_size = (default_width, default_height)
    window.title("PDF to PNG")

    prefix_label = tk.Label(window, text="Prefix: ")
    prefix = tk.Entry(width=16)
    width_label = tk.Label(window, text="Width: ")
    width_entry = tk.Entry(window, width=8, textvariable=width)
    height_label = tk.Label(window, text="Height: ")
    height_entry = tk.Entry(window, width=8, textvariable=height)

    save_path_label = tk.Label(window, text="Save Path: ")
    save_path_entry = tk.Entry(window, width=50)

    canvas = tk.Canvas(window, width=default_width, height=default_height)
    current_img = None
    current_img_index = 0
    images = None

    canvas_control = CanvasControl(canvas=canvas)
    next_button = tk.Button(text="Next image", command=canvas_control.next)
    prev_button = tk.Button(text="Prev image", command=canvas_control.prev)
    transparent_button = tk.Checkbutton(
        text="Transparent", variable=transparent, onvalue=True, offvalue=False)

    save_button = tk.Button(text="Save PNGs", state=tk.DISABLED, command=lambda: save_pngs(
                                                                        canvas_control=canvas_control,
                                                                        prefix=prefix.get()))

    open_pdf_button = tk.Button(text="Open PDF", command=lambda: open_file(canvas_control=canvas_control,
                                                                           width=width.get(),
                                                                           height=height.get(),
                                                                           transparent=transparent.get(),
                                                                           save_button=save_button))
    transparent_button.select()
    transparent_button.pack()
    width_label.pack()
    width_entry.pack()
    height_label.pack()
    height_entry.pack()
    open_pdf_button.pack()
    next_button.pack()
    prev_button.pack()
    prefix_label.pack()
    prefix.pack()
    save_button.pack()
    canvas.pack()

    window.mainloop()
