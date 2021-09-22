from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageFilter

root = Tk()
root.title("Photo Editor")

global img_display, img_work, img_og


def select_file():
    global img_display, img_work, img_og
    filename = fd.askopenfilename(parent=root)
    img_work = Image.open(filename)
    img_og = Image.open(filename)
    img_display = ImageTk.PhotoImage(img_work.resize((1024, 512)))
    img_work = img_work.resize((1024, 512))
    canvas.create_image(20, 20, anchor=NW, image=img_display)


def b_w():
    global img_display, img_work
    img_work = img_work.convert('RGB')
    width, height = img_work.size

    pixels = img_work.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img_work.getpixel((px, py))

            bw_r = int((r + g + b) / 3)
            bw_g = int((r + g + b) / 3)
            bw_b = int((r + g + b) / 3)

            pixels[px, py] = (bw_r, bw_g, bw_b)

    img_display = ImageTk.PhotoImage(img_work)
    canvas.create_image(20, 20, anchor=NW, image=img_display)


def sepia():
    global img_display, img_work
    img_work = img_work.convert('RGB')
    width, height = img_work.size

    pixels = img_work.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img_work.getpixel((px, py))

            s_r = int((0.759 * r) + (0.398 * g) + (0.194 * b))
            s_g = int((0.676 * r) + (0.354 * g) + (0.173 * b))
            s_b = int((0.524 * r) + (0.277 * g) + (0.136 * b))

            for s in [s_r, s_g, s_b]:
                if s > 255:
                    s = 255

            pixels[px, py] = (s_r, s_g, s_b)

    img_display = ImageTk.PhotoImage(img_work)
    canvas.create_image(20, 20, anchor=NW, image=img_display)


def flip():
    global img_display, img_work
    img_work = img_work.transpose(Image.FLIP_LEFT_RIGHT)
    img_display = ImageTk.PhotoImage(img_work)
    canvas.create_image(20, 20, anchor=NW, image=img_display)


def reset():
    global img_work, img_display
    img_work = img_og.resize((1024, 512))
    img_display = ImageTk.PhotoImage(img_og.resize(1024, 512))
    canvas.create_image(20, 20, anchor=NW, image=img_display)


def blur():
    global img_work, img_display
    img_work = img_work.filter(ImageFilter.BoxBlur(5))
    img_display = ImageTk.PhotoImage(img_work)
    canvas.create_image(20, 20, anchor=NW, image=img_display)


reset = Button(text="reset", command=reset)  # done
b_w = Button(text="B&W", command=b_w)  # done
open_image = Button(text="Click here to open image", command=select_file)  # done
flip = Button(text="flip", command=flip)  # done
blur = Button(text='blur', command=blur)  # done
sepia = Button(text='sepia', command=sepia)  # done
canvas = Canvas(root, width=2500, height=2500)

reset.pack()
b_w.pack()
open_image.pack()
flip.pack()
blur.pack()
sepia.pack()
canvas.pack()

root.mainloop()
