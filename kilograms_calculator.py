


from tkinter import*
root = Tk()
root.title("Lab 10 Kilograms conversion")
root.minsize (350,250)
root.configure(bg = "lightgrey")

L1 = Label(root, text = "Enter kilograms: ", bg = "lightgrey", fg = "black", font = "arial 10")
L1.place(x = 25, y = 25)
L2 = Label(root, text = "Choose a mass/weight: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2.place(x = 25, y = 50)
L3 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L3.place(x = 25, y = 150)

E1 = Entry(root, bg = "white", fg = "black", bd = 3)
E1.place(x = 100, y = 25)

def gramsconversion():
    kilograms = int(E1.get())
    a1 = "{:3f}".format(kilograms * 1000)
    L4.config(text = str(a1) + "grams")
def ouncesconversion():
    kilograms = int(E1.get())
    a2 = kilograms * 35.27396
    L4.config(text = str(a2) + "ounces")
def poundsconversion():
    kilograms = int(E1.get())
    a3 = kilograms * 2.2046
    L4.config(text = str(a3) + "pounds")

B1 = Button(root, text = "grams", bg = "white", fg = "black", font = "arial 10", command = gramsconversion, bd = 3)
B1.place(x = 25, y = 110)
B2 = Button(root, text = "ounces", bg = "white", fg = "black", font = "arial 10", command = ouncesconversion, bd = 3)
B2.place(x = 100, y = 110)
B3 = Button(root, text = "pounds", bg = "white", fg = "black", font = "arial 10", command = poundsconversion, bd = 3)
B3.place(x = 190, y = 110)


L4 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L4.place(x = 100, y = 150)
root.mainloop()