
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/tom/Documents/AWI Msc./2. Semester/Diskrete Simulation/Beleg/Gui/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1283x602")
window.configure(bg = "#8C8C8C")


canvas = Canvas(
    window,
    bg = "#8C8C8C",
    height = 602,
    width = 1283,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1283.0,
    66.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    33.0,
    169.0,
    727.0,
    524.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    818.0,
    104.0,
    1265.0,
    524.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    33.0,
    105.0,
    205.0,
    151.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    82.0,
    120.0,
    anchor="nw",
    text="170,000 €",
    fill="#000000",
    font=("Inter SemiBold", 19 * -1)
)

canvas.create_text(
    41.0,
    105.0,
    anchor="nw",
    text="Umsatz",
    fill="#000000",
    font=("Inter SemiBold", 11 * -1)
)

canvas.create_rectangle(
    294.0,
    106.0,
    466.0,
    152.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    347.0,
    119.0,
    anchor="nw",
    text="140,000 € ",
    fill="#000000",
    font=("Inter SemiBold", 19 * -1)
)

canvas.create_text(
    305.0,
    108.0,
    anchor="nw",
    text="Profit",
    fill="#000000",
    font=("Inter SemiBold", 11 * -1)
)

canvas.create_rectangle(
    555.0,
    104.0,
    727.0,
    150.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    629.0,
    119.0,
    anchor="nw",
    text="2000  ",
    fill="#000000",
    font=("Inter SemiBold", 19 * -1)
)

canvas.create_text(
    566.0,
    106.0,
    anchor="nw",
    text="Kunden",
    fill="#000000",
    font=("Inter SemiBold", 11 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    46.0,
    32.0,
    image=image_image_1
)

canvas.create_text(
    80.0,
    8.0,
    anchor="nw",
    text="Monte Carlo Simulations Tool - Eisdielengeschäft in Dresden",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
